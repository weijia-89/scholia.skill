#!/usr/bin/env python3
"""Build text slice attachments for phase-2 subagents from coverage attestation."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import CORPUS, PIPELINE, TEXT  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"
ATTACH = PIPELINE / "attachments"


def slice_text(text_path: Path, start: int, end: int) -> str:
    lines = text_path.read_text(encoding="utf-8", errors="replace").splitlines()
    # coverage attestation uses 1-based inclusive line numbers
    chunk = lines[max(0, start - 1) : end]
    return "\n".join(chunk)


def header(ch: dict, body: str) -> str:
    return f"""# Text slice — {ch['ingest_file']}
# corpus: {CORPUS}
# slug: {ch['slug']} · chapter: {ch['chapter_id']}
# hooks: {ch['hooks']} · route: {ch['route']}
# DO NOT monolith-read — subagent uses this slice + ingest only.

{body}
"""


def main() -> int:
    if not CURRICULUM.is_file():
        print(f"Missing {CURRICULUM}", file=sys.stderr)
        return 2
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    ATTACH.mkdir(parents=True, exist_ok=True)
    count = 0
    for wave_def in (data.get("waves") or {}).values():
        for batch in wave_def.get("batches") or []:
            for ch in batch.get("chapters") or []:
                if ch.get("route") == "skip":
                    continue
                text_path = ch.get("text_path")
                line_range = ch.get("text_slice")
                out_name = ch["ingest_file"].replace("_ingest.md", "_SLICE.txt")
                out_path = ATTACH / out_name
                if text_path and line_range and Path(text_path).is_file():
                    body = slice_text(Path(text_path), line_range[0], line_range[1])
                else:
                    ingest = Path(ch["ingest_path"])
                    body = ingest.read_text(encoding="utf-8", errors="replace")[:12000]
                    body += "\n\n[NOTE: full text slice unavailable — use ingest + coverage_attestation]\n"
                out_path.write_text(header(ch, body), encoding="utf-8")
                count += 1
                print(f"SLICE {out_name}")
    print(f"Wrote {count} attachments -> {ATTACH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
