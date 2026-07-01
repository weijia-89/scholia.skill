#!/usr/bin/env python3
"""Build Phase 3 merge-window ChatPRD attach folders.

Output: synth_attach/{window_id}/ — contract + ingests + Gate A primaries (spare slots only; ≤8 total).

Operator manifest: localonly/phase3_window_manifests/{window_id}.md
Digest prompt is paste-only.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import TypedDict

from prompt_chain import (
    PROJECT,
    RETURNS,
    SYNTH_CONTRACT,
    SYNTH_EVIDENCE,
)

SYNTH_ATTACH = PROJECT / "synth_attach"
ATTACH_DIR = PROJECT / "attachments"
WINDOW_MANIFESTS = PROJECT / "localonly/phase3_window_manifests"
MAX_ATTACH = 8
MAX_INGESTS = MAX_ATTACH - 1  # slot 0 = contract; Gate A uses spare slots after ingests
CONTRACT_ATTACH_NAME = "00_CORPUS_SYNTH_CONTRACT.md"

# 37 ingests → 6 windows (7+7+7+7+7+2). Contract consumes one attach slot per window.
PHASE3_WINDOWS: list[dict[str, object]] = [
    {
        "id": "3A_deai_craft_ethics",
        "priority": "p0_deai",
        "lane": "deai",
        "theme": "Long craft (I–IV) + McKee ethics + AI-writing research (s00146)",
        "slugs": [
            "long_2018_portable_mentor_part03",
            "long_2018_portable_mentor_part01",
            "long_2018_portable_mentor_part04",
            "long_2018_portable_mentor_part02",
            "corpus_3375627",
            "jones_2015_jslw",
            "s00146_2024_ai_writing",
        ],
    },
    {
        "id": "3A_deai_process_research",
        "priority": "low_deai",
        "lane": "deai",
        "theme": "Long Part V revision process + AI-writing research (s40979)",
        "slugs": [
            "long_2018_portable_mentor_part05",
            "s40979_2024_ai_writing",
        ],
    },
    {
        "id": "3B_baker_ginna",
        "priority": "medium",
        "lane": "tic_both",
        "theme": "Baker professional writing/speaking + Ginna editor craft (ch14–15)",
        "slugs": [
            "baker_2020_prof_writing_speaking_ch01",
            "baker_2020_prof_writing_speaking_ch03",
            "baker_2020_prof_writing_speaking_ch05",
            "baker_2020_prof_writing_speaking_ch06",
            "baker_2020_prof_writing_speaking_ch07",
            "ginna_what_editors_do_ch14",
            "ginna_what_editors_do_ch15",
        ],
    },
    {
        "id": "3B_workplace_rhetoric",
        "priority": "medium",
        "lane": "tic_both",
        "theme": "Ginna parts + Henry workplace + Peeples rhetoric + Terk L02",
        "slugs": [
            "ginna_what_editors_do_part02",
            "ginna_what_editors_do_part03",
            "henry_2000_writing_workplace_part02",
            "henry_2000_writing_workplace_ch06",
            "peeples_2003_prof_writing_rhetoric_ch02",
            "peeples_2003_prof_writing_rhetoric_ch06",
            "terk_prof_writing_skills_lesson02",
        ],
    },
    {
        "id": "3B_skills_business_writing",
        "priority": "medium",
        "lane": "tic_both",
        "theme": "Terk lessons (L03–07) + Locker W231 business writing (ch02–06)",
        "slugs": [
            "terk_prof_writing_skills_lesson03",
            "terk_prof_writing_skills_lesson04",
            "terk_prof_writing_skills_lesson07",
            "locker_2012_prof_writing_w231_ch02",
            "locker_2012_prof_writing_w231_ch03",
            "locker_2012_prof_writing_w231_ch05",
            "locker_2012_prof_writing_w231_ch06",
        ],
    },
    {
        "id": "3B_craft_structure",
        "priority": "medium",
        "lane": "tic_both",
        "theme": "Locker advanced chapters + Munier openings + Olmstead craft elements",
        "slugs": [
            "locker_2012_prof_writing_w231_ch07",
            "locker_2012_prof_writing_w231_ch08",
            "munier_2016_writers_guide_beginnings_ch01",
            "munier_2016_writers_guide_beginnings_ch02",
            "olmstead_2011_elements_writing_craft_craft01",
            "olmstead_2011_elements_writing_craft_craft02",
            "olmstead_2011_elements_writing_craft_craft03",
        ],
    },
]


class WindowSpec(TypedDict):
    id: str
    priority: str
    lane: str
    theme: str
    slugs: list[str]


def _window_specs() -> list[WindowSpec]:
    return PHASE3_WINDOWS  # type: ignore[return-value]


def _slug_from_ingest(path: Path) -> str:
    name = path.name
    for suffix in ("_20260628_ingest.md", "_ingest.md"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem


def _ingest_return_for_slug(slug: str) -> Path | None:
    hits = [
        p
        for p in RETURNS.glob(f"{slug}_*_ingest.md")
        if "refined" not in p.name
    ]
    if not hits:
        hits = [p for p in RETURNS.glob(f"*{slug}*ingest.md") if "refined" not in p.name]
    return sorted(hits)[-1] if hits else None


def _gate_a_attach_for_slug(slug: str) -> Path | None:
    """Primary Gate A slice on disk (attachments/*_ATTACH.txt)."""
    hits = list(ATTACH_DIR.glob(f"*_{slug}_ATTACH.txt"))
    if not hits:
        hits = [p for p in ATTACH_DIR.glob(f"*{slug}*ATTACH.txt") if p.is_file()]
    return sorted(hits)[-1] if hits else None


def _copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _contract_attach_path(out_dir: Path) -> Path:
    return out_dir / CONTRACT_ATTACH_NAME


def _is_allowed_attach(name: str) -> bool:
    return (
        name == CONTRACT_ATTACH_NAME
        or name.endswith("_ingest.md")
        or name.endswith("_ATTACH.txt")
    )


def _window_manifest_md(spec: WindowSpec, attach_paths: list[Path]) -> str:
    window_id = spec["id"]
    lines = [
        f"# {window_id}",
        "",
        f"**Theme:** {spec['theme']}",
        f"**Priority:** {spec['priority']} · **Lane:** {spec['lane']}",
        "",
        "## ChatPRD session (hard limit: 8 attachments)",
        "",
        "1. **Paste** digest prompt (do not attach):",
        f"   `{SYNTH_EVIDENCE.resolve()}`",
        f"2. **Attach all {len(attach_paths)} file(s)** from folder (contract **first** — MUST READ):",
        f"   `{SYNTH_ATTACH.resolve()}/{window_id}/`",
        "",
    ]
    for i, p in enumerate(attach_paths, start=1):
        tag = " **MUST READ FIRST**" if p.name == CONTRACT_ATTACH_NAME else ""
        lines.append(f"{i}. `{p.resolve()}`{tag}")
    lines.extend(
        [
            "",
            f"**Ingest slugs ({len(spec['slugs'])}):** {', '.join(spec['slugs'])}",
            "",
            "## Document output title (ChatPRD save)",
            "",
            f"`corpus_evidence_digest_{window_id}_YYYYMMDD.md`",
            "",
            f"**Returns folder:** `{RETURNS.resolve()}`",
            "",
        ]
    )
    return "\n".join(lines)


def build_window(window_id: str, *, clean: bool = False) -> Path | None:
    spec: WindowSpec | None = next((w for w in _window_specs() if w["id"] == window_id), None)
    if not spec:
        return None

    slugs: list[str] = spec["slugs"]
    if len(slugs) > MAX_INGESTS:
        print(
            f"ERROR: {window_id} has {len(slugs)} ingests (max {MAX_INGESTS} with contract) — split window",
            file=sys.stderr,
        )
        return None

    out_dir = SYNTH_ATTACH / window_id
    if clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    attach_paths: list[Path] = []

    contract_dst = _contract_attach_path(out_dir)
    _copy(SYNTH_CONTRACT, contract_dst)
    attach_paths.append(contract_dst)

    for i, slug in enumerate(slugs, start=1):
        ingest_src = _ingest_return_for_slug(slug)
        if not ingest_src:
            print(f"WARN: missing ingest for {slug} in {window_id}", file=sys.stderr)
            continue
        dst = out_dir / f"{i:02d}_{ingest_src.name}"
        _copy(ingest_src, dst)
        attach_paths.append(dst)

    budget = MAX_ATTACH - len(attach_paths)
    ga_i = 0
    for slug in slugs:
        if budget <= 0:
            break
        ga_src = _gate_a_attach_for_slug(slug)
        if not ga_src:
            print(f"WARN: missing Gate A attach for {slug} in {window_id}", file=sys.stderr)
            continue
        ga_i += 1
        ga_dst = out_dir / f"GA{ga_i:02d}_{ga_src.name}"
        _copy(ga_src, ga_dst)
        attach_paths.append(ga_dst)
        budget -= 1

    for p in out_dir.iterdir():
        if p.is_file() and not _is_allowed_attach(p.name):
            p.unlink()
            print(f"Removed disallowed attach file: {p.name}", file=sys.stderr)

    if len(attach_paths) > MAX_ATTACH:
        print(f"ERROR: {window_id} has {len(attach_paths)} attach files", file=sys.stderr)
        return None

    WINDOW_MANIFESTS.mkdir(parents=True, exist_ok=True)
    manifest = WINDOW_MANIFESTS / f"{window_id}.md"
    manifest.write_text(_window_manifest_md(spec, attach_paths), encoding="utf-8")

    return out_dir


def pack_attach_paths(window_id: str) -> list[str]:
    """Contract first, then ingests, then Gate A primaries — ≤8 total."""
    d = SYNTH_ATTACH / window_id
    if not d.is_dir():
        return []
    contract = d / CONTRACT_ATTACH_NAME
    ingests = sorted(
        p for p in d.iterdir() if p.is_file() and p.name.endswith("_ingest.md")
    )
    gate_a = sorted(
        p for p in d.iterdir() if p.is_file() and p.name.endswith("_ATTACH.txt")
    )
    paths: list[Path] = []
    if contract.is_file():
        paths.append(contract)
    paths.extend(ingests)
    paths.extend(gate_a)
    if len(paths) > MAX_ATTACH:
        print(f"ERROR: {window_id} attach folder has {len(paths)} files", file=sys.stderr)
    return [str(p.resolve()) for p in paths[:MAX_ATTACH]]


def all_window_ids() -> list[str]:
    return [w["id"] for w in _window_specs()]


def all_assigned_slugs() -> list[str]:
    slugs: list[str] = []
    for w in _window_specs():
        slugs.extend(w["slugs"])
    return slugs


def verify_slug_coverage() -> bool:
    expected = {
        _slug_from_ingest(p)
        for p in RETURNS.glob("*_20260628_ingest.md")
        if "refined" not in p.name
    }
    assigned = set(all_assigned_slugs())
    missing = expected - assigned
    extra = assigned - expected
    if missing:
        print(f"ERROR: unassigned slugs: {sorted(missing)}", file=sys.stderr)
    if extra:
        print(f"ERROR: unknown slugs in windows: {sorted(extra)}", file=sys.stderr)
    if len(assigned) != len(all_assigned_slugs()):
        print("ERROR: duplicate slug in PHASE3_WINDOWS", file=sys.stderr)
        return False
    for w in _window_specs():
        n = len(w["slugs"])
        if n > MAX_INGESTS:
            print(f"ERROR: window {w['id']} has {n} ingests (max {MAX_INGESTS})", file=sys.stderr)
            return False
    return not missing and not extra


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window", help="Build one window id only")
    ap.add_argument("--clean", action="store_true", help="Remove synth_attach before build")
    ap.add_argument("--list", action="store_true", help="Print built folder paths")
    args = ap.parse_args()

    if not verify_slug_coverage():
        return 1

    if args.clean and SYNTH_ATTACH.exists() and not args.window:
        shutil.rmtree(SYNTH_ATTACH)

    window_ids = [args.window] if args.window else all_window_ids()
    built = 0
    for wid in window_ids:
        path = build_window(wid, clean=args.clean and bool(args.window))
        if path:
            built += 1
            if args.list:
                print(path.resolve())
    print(f"Built {built} attach folder(s) under {SYNTH_ATTACH.resolve()}", file=sys.stderr)
    print(f"Manifests: {WINDOW_MANIFESTS.resolve()}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
