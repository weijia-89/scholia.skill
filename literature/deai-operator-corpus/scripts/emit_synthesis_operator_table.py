#!/usr/bin/env python3
"""Emit current-phase synthesis operator table (Phase 3+ only when QC skipped)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from build_synth_attach_packs import (
    PHASE3_WINDOWS,
    build_window,
    pack_attach_paths,
    verify_slug_coverage,
)
from prompt_chain import (
    PROJECT,
    RETURNS,
    SYNTH_CURSOR,
    SYNTH_EVIDENCE,
    SYNTH_SKILL_BRIEF,
)

SYNTH_ATTACH = PROJECT / "synth_attach"
DEFAULT_OUTPUT = PROJECT / "localonly/phase3_evidence_digest_operator_table.md"
ORDER = {"p0_deai": 0, "high": 1, "medium": 2, "low_deai": 3}


def _bullets(paths: list[str]) -> str:
    return "<br>".join(f"- {p}" for p in paths)


def _phase3_rows() -> list[tuple[str, str, str, list[str]]]:
    rows: list[tuple[str, str, str, list[str]]] = []
    for spec in PHASE3_WINDOWS:
        window_id = str(spec["id"])
        build_window(window_id, clean=False)
        attaches = pack_attach_paths(window_id)
        if not attaches:
            continue
        rows.append(
            (
                str(spec["priority"]),
                window_id,
                str(SYNTH_EVIDENCE.resolve()),
                attaches,
            )
        )
    rows.sort(key=lambda r: (ORDER.get(r[0], 9), r[1]))
    return rows


def _phase3_markdown(rows: list[tuple[str, str, str, list[str]]]) -> str:
    lines = [
        "## Phase 3 — Evidence digest (current)",
        "",
        f"**Synth attach packs:** `{SYNTH_ATTACH.resolve()}/{{window_id}}/`",
        f"**Returns folder:** `{RETURNS.resolve()}`",
        "",
        "Phase 2 refine **skipped**. **Attach (≤8):** contract first (MUST READ), ingests, then Gate A `*_ATTACH.txt` when spare slots exist. **Paste:** digest prompt only.",
        "",
        "| Priority | Window | Prompt | Attachments |",
        "| -------- | ------ | ------ | ----------- |",
    ]
    for pri, window, prompt, attaches in rows:
        lines.append(f"| {pri} | {window} | {prompt} | {_bullets(attaches)} |")
    return "\n".join(lines) + "\n"


def detect_phase() -> int:
    if not list(RETURNS.glob("corpus_evidence_digest*.md")):
        return 3
    if not list(RETURNS.glob("deai_operator_corpus_skill_brief_*.md")):
        return 4
    if not list(RETURNS.glob("cursor_implement_brief_*.md")):
        return 5
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--phase", type=int, choices=(3, 4, 5), help="Force phase (default: auto)")
    ap.add_argument("--output", type=Path, help=f"Write table to file (default: {DEFAULT_OUTPUT})")
    ap.add_argument("--build-only", action="store_true", help="Build synth_attach packs only")
    args = ap.parse_args()

    if args.build_only:
        from build_synth_attach_packs import main as build_main

        sys.argv = [sys.argv[0], "--clean"]
        return build_main()

    if not verify_slug_coverage():
        return 1

    phase = args.phase or detect_phase()
    body = ""

    if phase == 3:
        rows = _phase3_rows()
        if not rows:
            print("Phase 3 blocked — no merge windows built.", file=sys.stderr)
            return 2
        body = _phase3_markdown(rows)
    elif phase == 4:
        digests = sorted(RETURNS.glob("corpus_evidence_digest*.md"))
        if not digests:
            print("Phase 4 blocked — save evidence digest(s) first.", file=sys.stderr)
            return 2
        paths = [str(p.resolve()) for p in digests[:8]]
        body = (
            "## Phase 4 — Skill brief (current)\n\n"
            "| Prompt | Attachments |\n"
            "| ------ | ----------- |\n"
            f"| {SYNTH_SKILL_BRIEF.resolve()} | {_bullets(paths)} |\n"
        )
    elif phase == 5:
        briefs = sorted(RETURNS.glob("deai_operator_corpus_skill_brief_*.md"))
        if not briefs:
            print("Phase 5 blocked — save skill brief first.", file=sys.stderr)
            return 2
        p = str(briefs[-1].resolve())
        body = (
            "## Phase 5 — Cursor handoff (current)\n\n"
            "| Prompt | Attachments |\n"
            "| ------ | ----------- |\n"
            f"| {SYNTH_CURSOR.resolve()} | - {p} |\n"
        )
    else:
        print("All synthesis phases complete on disk.", file=sys.stderr)
        return 0

    print(body, end="")
    out_path = args.output or DEFAULT_OUTPUT
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body, encoding="utf-8")
    print(f"Wrote {out_path.resolve()}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
