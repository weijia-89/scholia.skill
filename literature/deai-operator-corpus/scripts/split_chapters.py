#!/usr/bin/env python3
"""Split source_exports into chapter slices per chapter_curriculum.yaml."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import EXPORT_DIR, PROJECT  # noqa: E402

CURRICULUM = PROJECT / "chapter_curriculum.yaml"
CHAPTER_DIR = EXPORT_DIR / "chapters"


def resolve_start(text: str, chapter: dict) -> int | None:
    """Prefer start_pattern over start_offset when both set (fixes wrong byte markers)."""
    pat = chapter.get("start_pattern")
    min_off = int(chapter.get("start_min_offset", 0))
    if pat:
        for m in re.finditer(pat, text, re.I | re.M):
            if m.start() >= min_off:
                return m.start()
    if chapter.get("start_offset") is not None:
        return int(chapter["start_offset"])
    return None


def split_book(book: dict) -> list[dict]:
    prefix = book["prefix"]
    export_path = EXPORT_DIR / f"{prefix}.txt"
    if not export_path.is_file():
        print(f"SKIP missing export: {export_path}")
        return []

    text = export_path.read_text(encoding="utf-8", errors="replace")
    chapters = book.get("chapters", [])
    resolved: list[tuple[int, dict, int]] = []
    for ch in chapters:
        start = resolve_start(text, ch)
        if start is None:
            print(f"WARN no start for {prefix}/{ch['chapter_id']}")
            continue
        resolved.append((start, ch, start))

    resolved.sort(key=lambda x: x[0])
    CHAPTER_DIR.mkdir(parents=True, exist_ok=True)
    built: list[dict] = []

    for i, (start, ch, _) in enumerate(resolved):
        end = resolved[i + 1][0] if i + 1 < len(resolved) else len(text)
        body = text[start:end].strip()
        if len(body) < 200:
            print(f"WARN short slice {prefix}/{ch['chapter_id']} ({len(body)} chars)")
            continue

        out_name = f"{prefix}_{ch['chapter_id']}.txt"
        out_path = CHAPTER_DIR / out_name
        out_path.write_text(body, encoding="utf-8")
        rel = f"source_exports/chapters/{out_name}"
        meta = {
            "prefix": prefix,
            "slug": book["slug"],
            "chapter_id": ch["chapter_id"],
            "title": ch["title"],
            "lanes": ch.get("lanes", []),
            "rationale": ch.get("rationale", ""),
            "start_offset": start,
            "end_offset": end,
            "char_len": len(body),
            "chapter_path": rel,
        }
        built.append(meta)
        print(f"SLICE {out_name} ({len(body):,} chars)")

    return built


def main() -> None:
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    all_built: list[dict] = []
    for book in data.get("books", []):
        if book.get("split_mode") == "epub_spine":
            print(f"SKIP byte split (epub_spine): {book['prefix']}")
            continue
        all_built.extend(split_book(book))

    index_path = CHAPTER_DIR / "_index.yaml"
    index_path.write_text(
        yaml.dump({"chapters": all_built}, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(f"Wrote {len(all_built)} chapter slices → {CHAPTER_DIR}")


if __name__ == "__main__":
    main()
