#!/usr/bin/env python3
"""Convert inbox EPUBs to source_exports/ via Calibre ebook-convert."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import EXPORT_DIR, MANIFEST, PREFIX, export_rel  # noqa: E402

EBOOK_CONVERT = Path("/Applications/calibre.app/Contents/MacOS/ebook-convert")


def main() -> None:
    if not EBOOK_CONVERT.is_file():
        print(f"SKIP calibre missing: {EBOOK_CONVERT}")
        return

    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    changed = False
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    for entry in data.get("entries", []):
        if entry.get("format") != "epub":
            continue
        slug = entry["slug"]
        prefix = PREFIX[slug]
        export_path = EXPORT_DIR / f"{prefix}.txt"
        inbox = Path(entry["inbox_file"])
        if not inbox.is_file():
            print(f"SKIP missing inbox: {slug}")
            continue
        if export_path.is_file() and export_path.stat().st_size > 100:
            print(f"OK exists: {slug}")
            continue

        subprocess.run(
            [str(EBOOK_CONVERT), str(inbox), str(export_path)],
            check=True,
        )
        entry["text_path"] = export_rel(prefix)
        entry["text_status"] = "ready"
        entry["notes"] = ""
        changed = True
        print(f"EXPORTED EPUB: {slug} ({export_path.stat().st_size} chars)")

    if changed:
        MANIFEST.write_text(
            yaml.dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
