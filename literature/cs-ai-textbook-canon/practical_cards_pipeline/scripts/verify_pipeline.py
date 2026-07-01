#!/usr/bin/env python3
"""Deterministic output harness for cs-ai practical_cards_pipeline artifacts.

Oracles PC-P01..PC-P14 — catches path typos, missing attach sections, bad ChatPRD
returns, and operator-table drift before merge/verify loops.
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import CORPUS, INGESTS, PIPELINE  # noqa: E402

SCHOLIA_SCRIPTS = CORPUS.parent.parent / "scripts"
sys.path.insert(0, str(SCHOLIA_SCRIPTS))

import verify_practical_cards as vpc  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"
OPERATOR_TABLE = PIPELINE / "references" / "chatprd-operator-table.md"
ATTACH_DIR = PIPELINE / "attachments"
PROMPT_DIR = PIPELINE / "prompts" / "chatprd"
RETURNS_DIR = PIPELINE / "chatprd_returns"
MANIFEST = CORPUS / "metadata" / "corpus_manifest.yaml"

ATTACH_SECTIONS = ("STABLE-CONTEXT", "PHASE-1-INGEST", "TEXT-SLICE")
FORBIDDEN_NAMES = frozenset({"README.md", "MANIFEST.md", "README", "MANIFEST"})


@dataclass
class Report:
    fails: int = 0
    warns: int = 0
    passes: int = 0
    oracle_hits: dict[str, int] = field(default_factory=dict)
    summary: bool = False

    def pass_(self, msg: str, oracle: str | None = None) -> None:
        self.passes += 1
        if oracle:
            self.oracle_hits[oracle] = self.oracle_hits.get(oracle, 0) + 1
        if not self.summary:
            print(f"PASS: {msg}")

    def fail(self, msg: str, oracle: str | None = None) -> None:
        self.fails += 1
        if oracle:
            self.oracle_hits[oracle] = self.oracle_hits.get(oracle, 0) + 1
        print(f"FAIL: {msg}")

    def warn(self, msg: str) -> None:
        self.warns += 1
        if not self.summary:
            print(f"WARN: {msg}")

    def exit_code(self) -> int:
        return 2 if self.fails else 0

    def print_footer(self) -> None:
        if self.summary and self.warns:
            print(f"WARN: {self.warns} optional check(s) suppressed in summary mode")
        print(
            f"---\nFails: {self.fails} · Warns: {self.warns} · Passes: {self.passes}"
        )
        if self.oracle_hits:
            hits = ", ".join(f"{k}={v}" for k, v in sorted(self.oracle_hits.items()))
            print(f"Oracles: {hits}")


def manifest_requires_quality() -> bool:
    if not MANIFEST.is_file():
        return False
    return vpc.manifest_requires_cards(CORPUS)


def stem_from_chapter(ch: dict) -> str:
    return ch["ingest_file"].replace("_ingest.md", "")


def paths_for_chapter(ch: dict) -> dict[str, Path]:
    stem = stem_from_chapter(ch)
    return {
        "attach": ATTACH_DIR / f"{stem}_ATTACH.txt",
        "prompt": PROMPT_DIR / f"{stem}_card_ingest.md",
        "return": RETURNS_DIR / f"{stem}_cards.yaml",
        "ingest": INGESTS / ch["ingest_file"],
    }


def iter_chapters(
    data: dict, *, batch_id: str | None = None, route: str | None = None
) -> list[tuple[str, dict]]:
    rows: list[tuple[str, dict]] = []
    for wave_def in (data.get("waves") or {}).values():
        for batch in wave_def.get("batches") or []:
            bid = batch.get("batch_id", "")
            if batch_id and bid != batch_id:
                continue
            for ch in batch.get("chapters") or []:
                if ch.get("route") == "skip":
                    continue
                if route and ch.get("route") != route:
                    continue
                rows.append((bid, ch))
    return rows


def load_curriculum(rep: Report) -> dict | None:
    if not CURRICULUM.is_file():
        rep.fail(f"PC-P01 curriculum missing: {CURRICULUM}", "PC-P01")
        return None
    try:
        data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        rep.fail(f"PC-P01 curriculum parse error: {exc}", "PC-P01")
        return None
    rep.pass_(f"PC-P01 curriculum loaded ({CURRICULUM})", "PC-P01")
    return data


def check_forbidden_upload_dirs(rep: Report) -> None:
    for folder in (ATTACH_DIR, RETURNS_DIR, PROMPT_DIR):
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if path.name in FORBIDDEN_NAMES:
                rep.fail(
                    f"PC-P11 forbidden upload artifact: {path}",
                    "PC-P11",
                )


def check_chapter_artifacts(
    rep: Report,
    bid: str,
    ch: dict,
    *,
    require_returns: bool,
    require_quality_level: bool,
) -> None:
    stem = stem_from_chapter(ch)
    label = f"{bid} · {ch['slug']} {ch['chapter_id']} ({stem})"
    paths = paths_for_chapter(ch)

    if not paths["ingest"].is_file():
        rep.fail(f"PC-P12 {label}: ingest missing {paths['ingest']}", "PC-P12")
    else:
        rep.pass_(f"PC-P12 {label}: ingest on disk", "PC-P12")

    if not paths["attach"].is_file():
        rep.fail(f"PC-P02 {label}: attach missing {paths['attach']}", "PC-P02")
        return
    rep.pass_(f"PC-P02 {label}: attach exists", "PC-P02")

    attach_text = paths["attach"].read_text(encoding="utf-8", errors="replace")
    for section in ATTACH_SECTIONS:
        marker = f"{'=' * 72}\n{section}"
        if marker not in attach_text:
            rep.fail(f"PC-P04 {label}: attach missing section {section}", "PC-P04")
        else:
            rep.pass_(f"PC-P04 {label}: attach has {section}", "PC-P04")

    if "[MISSING" in attach_text:
        rep.fail(f"PC-P05 {label}: attach contains [MISSING marker", "PC-P05")
    else:
        rep.pass_(f"PC-P05 {label}: attach has no [MISSING markers", "PC-P05")

    if not paths["prompt"].is_file():
        rep.fail(f"PC-P03 {label}: prompt missing {paths['prompt']}", "PC-P03")
        return
    rep.pass_(f"PC-P03 {label}: prompt exists", "PC-P03")

    prompt_text = paths["prompt"].read_text(encoding="utf-8", errors="replace")
    attach_abs = str(paths["attach"])
    return_abs = str(paths["return"])

    if attach_abs not in prompt_text:
        rep.fail(
            f"PC-P06 {label}: prompt missing attach absolute path",
            "PC-P06",
        )
    elif not Path(attach_abs).is_file():
        rep.fail(f"PC-P06 {label}: prompt attach path does not resolve", "PC-P06")
    else:
        rep.pass_(f"PC-P06 {label}: prompt references resolvable attach", "PC-P06")

    if return_abs not in prompt_text:
        rep.fail(
            f"PC-P07 {label}: prompt missing save path {paths['return'].name}",
            "PC-P07",
        )
    else:
        rep.pass_(f"PC-P07 {label}: prompt save path matches curriculum", "PC-P07")

    if "prompts/dispatch/" in prompt_text:
        rep.fail(
            f"PC-P13 {label}: prompt references subagent dispatch path",
            "PC-P13",
        )
    else:
        rep.pass_(f"PC-P13 {label}: prompt uses ChatPRD path only", "PC-P13")

    if paths["return"].is_file():
        errs = vpc.validate_card_file(
            paths["return"], require_quality_level=require_quality_level
        )
        if errs:
            for err in errs:
                rep.fail(f"PC-P10 {label}: {err}", "PC-P10")
        else:
            rep.pass_(f"PC-P10 {label}: return YAML validates", "PC-P10")
    elif require_returns:
        rep.fail(f"PC-P10 {label}: return required but missing {paths['return']}", "PC-P10")
    else:
        rep.warn(f"PC-P10 {label}: return not yet saved (optional)")


def parse_operator_table_paths(
    *, batch_id: str | None = None
) -> list[tuple[str, str, str, str, str]]:
    if not OPERATOR_TABLE.is_file():
        return []
    rows: list[tuple[str, str, str, str, str]] = []
    for line in OPERATOR_TABLE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        batch, chapter, attach, prompt, save = parts[:5]
        if batch.lower() == "batch" or chapter.lower() == "chapter":
            continue
        if batch_id and batch != batch_id:
            continue
        attach_path = attach.strip("`")
        if not attach_path.startswith("/"):
            continue
        rows.append((batch, chapter, attach, prompt, save))
    return rows


def check_operator_table(
    rep: Report,
    chapters: list[tuple[str, dict]],
    *,
    batch_id: str | None = None,
    route: str | None = None,
) -> None:
    if route and not batch_id:
        rep.pass_(
            f"PC-P08 operator table skipped (route-scoped: {route})",
            "PC-P08",
        )
        return

    if not OPERATOR_TABLE.is_file():
        rep.fail(f"PC-P08 operator table missing: {OPERATOR_TABLE}", "PC-P08")
        return

    table_rows = parse_operator_table_paths(batch_id=batch_id)
    expected = len(chapters)
    scope = batch_id or "all batches"
    if len(table_rows) != expected:
        rep.fail(
            f"PC-P08 operator table row count {len(table_rows)} != "
            f"curriculum {expected} (scope: {scope})",
            "PC-P08",
        )
    else:
        rep.pass_(
            f"PC-P08 operator table rows match curriculum ({expected}, {scope})",
            "PC-P08",
        )

    expected_keys = {
        (
            bid,
            f"{ch['slug']} {ch['chapter_id']}",
            str(paths_for_chapter(ch)["attach"]),
            str(paths_for_chapter(ch)["prompt"]),
            str(paths_for_chapter(ch)["return"]),
        )
        for bid, ch in chapters
    }
    table_keys = {
        (batch, chapter, attach.strip("`"), prompt.strip("`"), save.strip("`"))
        for batch, chapter, attach, prompt, save in table_rows
    }
    missing = expected_keys - table_keys
    extra = table_keys - expected_keys
    if missing:
        for row in sorted(missing):
            rep.fail(f"PC-P08 operator table missing row: {row[1]}", "PC-P08")
    if extra:
        for row in sorted(extra):
            rep.fail(f"PC-P08 operator table stale row: {row[1]}", "PC-P08")
    if not missing and not extra and table_rows:
        rep.pass_("PC-P08 operator table paths match curriculum", "PC-P08")

    bad_paths = 0
    for _batch, _chapter, attach, prompt, save in table_rows:
        for path_str in (attach.strip("`"), prompt.strip("`"), save.strip("`")):
            p = Path(path_str)
            if not p.is_file() and not path_str.endswith("_cards.yaml"):
                rep.fail(f"PC-P09 operator table path missing: {path_str}", "PC-P09")
                bad_paths += 1
    if bad_paths == 0 and table_rows:
        rep.pass_("PC-P09 operator table artifact paths resolve", "PC-P09")


def verify_pipeline(
    *,
    batch_id: str | None = None,
    route: str | None = None,
    require_returns: bool = False,
    summary: bool = False,
) -> int:
    rep = Report(summary=summary)
    require_quality = manifest_requires_quality()
    data = load_curriculum(rep)
    if data is None:
        rep.print_footer()
        return rep.exit_code()

    chapters = iter_chapters(data, batch_id=batch_id, route=route)
    if not chapters:
        rep.fail(
            f"PC-P14 no chapters for batch={batch_id!r} route={route!r}",
            "PC-P14",
        )
    else:
        scope = batch_id or "all non-skip"
        rep.pass_(f"PC-P14 scope {scope}: {len(chapters)} chapter(s)", "PC-P14")

    check_forbidden_upload_dirs(rep)
    for bid, ch in chapters:
        check_chapter_artifacts(
            rep,
            bid,
            ch,
            require_returns=require_returns,
            require_quality_level=require_quality,
        )
    check_operator_table(rep, chapters, batch_id=batch_id, route=route)

    rep.print_footer()
    return rep.exit_code()


def _write_fixture_tree(pipe: Path, corpus: Path, ch: dict, *, attach_body: str) -> Path:
    ingests = corpus / "ingests"
    ingests.mkdir(parents=True, exist_ok=True)
    for d in (
        pipe / "attachments",
        pipe / "prompts" / "chatprd",
        pipe / "chatprd_returns",
        pipe / "references",
    ):
        d.mkdir(parents=True, exist_ok=True)

    (ingests / ch["ingest_file"]).write_text("# ingest\n", encoding="utf-8")
    stem = stem_from_chapter(ch)
    attach = pipe / "attachments" / f"{stem}_ATTACH.txt"
    attach.write_text(attach_body, encoding="utf-8")
    prompt = pipe / "prompts" / "chatprd" / f"{stem}_card_ingest.md"
    ret = pipe / "chatprd_returns" / f"{stem}_cards.yaml"
    prompt.write_text(f"attach `{attach}`\nsave `{ret}`\n", encoding="utf-8")
    ret.write_text(
        """topic_slug: demo
cards:
  - exercise_name: Demo
    steps: [one, two, three]
    source_anchor: C-1
    procedure_gap: false
    quality_level: full
""",
        encoding="utf-8",
    )
    curriculum = {
        "waves": {
            "w_test": {
                "batches": [{"batch_id": "batch_01", "chapters": [ch]}],
            }
        }
    }
    (pipe / "card_curriculum.yaml").write_text(
        yaml.safe_dump(curriculum), encoding="utf-8"
    )
    (pipe / "references" / "chatprd-operator-table.md").write_text(
        f"| batch_01 | demo_book 01 | `{attach}` | `{prompt}` | `{ret}` |\n",
        encoding="utf-8",
    )
    return ingests


def run_self_test() -> int:
    rep = Report()
    good_attach = (
        "=" * 72 + "\nSTABLE-CONTEXT\n" + "=" * 72 + "\n\n"
        + "=" * 72 + "\nPHASE-1-INGEST\n" + "=" * 72 + "\n\n"
        + "=" * 72 + "\nTEXT-SLICE\n" + "=" * 72 + "\n\n"
    )
    ch = {
        "ingest_file": "demo_book_ch01_ingest.md",
        "slug": "demo_book",
        "chapter_id": "01",
        "route": "fan-out",
        "hooks": 3,
    }

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        pipe = root / "practical_cards_pipeline"
        corpus = root / "corpus"
        ingests = _write_fixture_tree(pipe, corpus, ch, attach_body=good_attach)

        global CURRICULUM, OPERATOR_TABLE, ATTACH_DIR, PROMPT_DIR, RETURNS_DIR, INGESTS, PIPELINE, CORPUS, MANIFEST
        old = (
            CURRICULUM,
            OPERATOR_TABLE,
            ATTACH_DIR,
            PROMPT_DIR,
            RETURNS_DIR,
            INGESTS,
            PIPELINE,
            CORPUS,
            MANIFEST,
        )
        CURRICULUM = pipe / "card_curriculum.yaml"
        OPERATOR_TABLE = pipe / "references" / "chatprd-operator-table.md"
        ATTACH_DIR = pipe / "attachments"
        PROMPT_DIR = pipe / "prompts" / "chatprd"
        RETURNS_DIR = pipe / "chatprd_returns"
        INGESTS = ingests
        PIPELINE = pipe
        CORPUS = corpus
        MANIFEST = corpus / "metadata" / "corpus_manifest.yaml"

        if verify_pipeline(batch_id="batch_01", require_returns=True) == 0:
            rep.pass_("self-test good fixture PASS")
        else:
            rep.fail("self-test good fixture should PASS")

        bad_attach = good_attach + "\n[MISSING: slice]\n"
        _write_fixture_tree(pipe, corpus, ch, attach_body=bad_attach)
        if verify_pipeline(batch_id="batch_01", require_returns=True) == 2:
            rep.pass_("self-test PC-P05 detects [MISSING marker")
        else:
            rep.fail("self-test PC-P05 should FAIL on [MISSING marker")

        CURRICULUM, OPERATOR_TABLE, ATTACH_DIR, PROMPT_DIR, RETURNS_DIR, INGESTS, PIPELINE, CORPUS, MANIFEST = old

    print(f"---\nSelf-test fails: {rep.fails}")
    return 2 if rep.fails else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run regression oracles")
    parser.add_argument("--batch", metavar="BATCH_ID", help="limit to one batch_id")
    parser.add_argument(
        "--route",
        choices=("fan-out", "inline"),
        help="limit to route type",
    )
    parser.add_argument(
        "--require-returns",
        action="store_true",
        help="fail when chatprd_returns/*.yaml missing for scoped chapters",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="print FAIL only; suppress PASS/WARN lines (counts at end)",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()

    return verify_pipeline(
        batch_id=args.batch,
        route=args.route,
        require_returns=args.require_returns,
        summary=args.summary,
    )


if __name__ == "__main__":
    raise SystemExit(main())
