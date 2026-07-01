#!/usr/bin/env python3
"""Emit operator table for ChatPRD external card extract (current wave batches)."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import PIPELINE  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"
OUT = PIPELINE / "references" / "chatprd-operator-table.md"


def main() -> int:
    if not CURRICULUM.is_file():
        print(f"Missing {CURRICULUM}", file=sys.stderr)
        return 2
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    lines = [
        "# ChatPRD operator table — practical cards phase 2",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Pipeline: `{PIPELINE}`",
        "",
        "**Iron law:** ≤8 ChatPRD uploads per window · one `*_ATTACH.txt` per chapter · paste prompt only.",
        "",
        "Regenerate:",
        "```bash",
        f"bash {PIPELINE}/scripts/refresh_pipeline.sh",
        "```",
        "",
        "| Batch | Chapter | Attach | Paste prompt | Save |",
        "| ----- | ------- | ------ | ------------ | ---- |",
    ]
    for wave_id, wave_def in (data.get("waves") or {}).items():
        for batch in wave_def.get("batches") or []:
            bid = batch.get("batch_id", "")
            for ch in batch.get("chapters") or []:
                if ch.get("route") == "skip":
                    continue
                stem = ch["ingest_file"].replace("_ingest.md", "")
                attach = f"{PIPELINE}/attachments/{stem}_ATTACH.txt"
                prompt = f"{PIPELINE}/prompts/chatprd/{stem}_card_ingest.md"
                save = f"{PIPELINE}/chatprd_returns/{stem}_cards.yaml"
                lines.append(
                    f"| {bid} | {ch['slug']} {ch['chapter_id']} | `{attach}` | `{prompt}` | `{save}` |"
                )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
