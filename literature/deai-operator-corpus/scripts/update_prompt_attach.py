#!/usr/bin/env python3
"""Patch ChatPRD attach sections in all per-source prompts."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

PROJECT = Path("/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus")
PROMPTS = PROJECT / "prompts"
MANIFEST = PROJECT / "manifest.yaml"

ATTACH_RE = re.compile(
    r"## ChatPRD attach \(≤8 files — flat names\)\s*\n.*?(?=^## |\Z)",
    re.MULTILINE | re.DOTALL,
)

AFTER_RE = re.compile(
    r"(\d+\. Run `bash .*refresh_attach_packs\.sh`\s*\n)",
    re.MULTILINE,
)


def attach_block(prefix: str) -> str:
    upload = f"/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/{prefix}_ATTACH.txt"
    return f"""## ChatPRD attach (one upload file)

Upload to **new ChatPRD window** (Opus 4.6). Attach **only** this self-contained file (stable context + primary text embedded):

1. `{upload}`

**Paste:** entire body of this prompt file.

**Do NOT:** upload anything else from this project folder. Full exports for chapter fan-out live in `source_exports/` (not for ChatPRD attach).

"""


def main() -> None:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    for entry in data.get("entries", []):
        prefix = Path(entry["text_path"]).stem
        path = PROMPTS / f"{prefix}_ingest.md"
        if not path.is_file():
            print(f"SKIP missing prompt: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not ATTACH_RE.search(text):
            print(f"SKIP no attach section: {path.name}")
            continue
        text = ATTACH_RE.sub(attach_block(prefix), text)
        text = AFTER_RE.sub(
            "2. Run `bash /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/export_text.sh` if source text changed\n",
            text,
        )
        text = text.replace(
            "use `_slice` + full attach; middle re-read on full text before magnitude claims.",
            "note truncated primary in attach file; middle re-read on `source_exports/` full export before magnitude claims if needed.",
        )
        path.write_text(text, encoding="utf-8")
        print(f"PATCH {path.name}")


if __name__ == "__main__":
    main()
