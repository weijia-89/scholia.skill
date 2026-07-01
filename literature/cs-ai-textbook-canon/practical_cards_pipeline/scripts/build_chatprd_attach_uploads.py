#!/usr/bin/env python3
"""Build ChatPRD upload files: one self-contained ATTACH.txt per chapter."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import CORPUS, PIPELINE  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"
STABLE = PIPELINE / "stable-context.txt"
ATTACH_DIR = PIPELINE / "attachments"
SLICE_DIR = ATTACH_DIR
INGESTS = CORPUS / "ingests"
MAX_INGEST_CHARS = 14_000


def attach_name(ch: dict) -> str:
    return ch["ingest_file"].replace("_ingest.md", "_ATTACH.txt")


def slice_body(ch: dict) -> tuple[str, str]:
    slice_path = SLICE_DIR / ch["ingest_file"].replace("_ingest.md", "_SLICE.txt")
    if slice_path.is_file():
        return slice_path.read_text(encoding="utf-8", errors="replace"), str(slice_path)
    ingest = INGESTS / ch["ingest_file"]
    if ingest.is_file():
        body = ingest.read_text(encoding="utf-8", errors="replace")[:MAX_INGEST_CHARS]
        return body, f"{ingest} (ingest fallback — run build_attach_slices.py)"
    return "[MISSING: no slice or ingest on disk]", "none"


def ingest_excerpt(ch: dict) -> str:
    ingest = INGESTS / ch["ingest_file"]
    if not ingest.is_file():
        return "[MISSING phase-1 ingest]"
    text = ingest.read_text(encoding="utf-8", errors="replace")
    if len(text) > MAX_INGEST_CHARS:
        return text[:MAX_INGEST_CHARS] + f"\n\n[TRUNCATED at {MAX_INGEST_CHARS} chars — full ingest on disk]\n"
    return text


def write_attach(ch: dict) -> None:
    stable = STABLE.read_text(encoding="utf-8").strip() if STABLE.is_file() else ""
    name = attach_name(ch)
    prompt_rel = f"prompts/chatprd/{ch['ingest_file'].replace('_ingest.md', '_card_ingest.md')}"
    primary, primary_label = slice_body(ch)
    phase1 = ingest_excerpt(ch)
    content = (
        f"{name} — ChatPRD upload (attach this file only)\n"
        f"Generated: {date.today().isoformat()}\n"
        f"Slug: {ch['slug']} · chapter: {ch['chapter_id']}\n"
        f"Project: {PIPELINE}\n"
        f"ChatPRD maximum: 8 uploaded files per window — this file is self-contained.\n"
        f"Also paste: {prompt_rel}\n\n"
        f"{'=' * 72}\nSTABLE-CONTEXT\n{'=' * 72}\n\n{stable}\n\n"
        f"{'=' * 72}\nPHASE-1-INGEST ({ch['ingest_file']})\n{'=' * 72}\n\n{phase1}\n\n"
        f"{'=' * 72}\nTEXT-SLICE ({primary_label})\n{'=' * 72}\n\n{primary}\n"
    )
    ATTACH_DIR.mkdir(parents=True, exist_ok=True)
    (ATTACH_DIR / name).write_text(content, encoding="utf-8")
    print(f"ATTACH {name}")


def main() -> int:
    if not CURRICULUM.is_file():
        print(f"Missing {CURRICULUM} — run plan_card_waves.py first", file=sys.stderr)
        return 2
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    count = 0
    for wave_def in (data.get("waves") or {}).values():
        for batch in wave_def.get("batches") or []:
            for ch in batch.get("chapters") or []:
                if ch.get("route") == "skip":
                    continue
                write_attach(ch)
                count += 1
    print(f"Wrote {count} ChatPRD attach files -> {ATTACH_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
