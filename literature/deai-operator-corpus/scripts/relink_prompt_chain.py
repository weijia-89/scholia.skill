#!/usr/bin/env python3
"""Relink After save / Platform split in paper + monolith ingest prompts."""
from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from prompt_chain import PROMPTS, next_steps_block, platform_split_table  # noqa: E402

OLD_AFTER = re.compile(
    r"\*\*After save:\*\*.*?(?=\n## |\Z)",
    re.DOTALL,
)
OLD_PLATFORM = re.compile(
    r"## Platform split.*?(?=\n## |\Z)",
    re.DOTALL,
)
OLD_FOOTER = re.compile(
    r"After save → `prompts/synth_refine_per_source\.md`.*",
)
OLD_GRANOLA = re.compile(
    r"\*\*Cursor does NOT author this ingest\.\*\* Operator saves ChatPRD return → optional Granola S4 batch synthesis → Cursor implements skill patches only when operator triggers\.",
)


def slug_from_path(path: Path) -> str:
    name = path.stem.replace("_ingest", "")
    # 05_baker_2020... -> baker_2020... from manifest pattern
    parts = name.split("_", 1)
    return parts[1] if len(parts) == 2 and parts[0].isdigit() else name


def relink_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    slug = slug_from_path(path)

    # chapter fan-out: prefix_chapterid_ingest -> slug_chapterid
    m = re.match(r"^\d+_(.+)_ingest$", path.stem)
    if m and "_" in m.group(1):
        # already handled by generate_chapter_prompts if *_lesson* or *_ch* or *_part*
        pass

    if OLD_FOOTER.search(text):
        text = OLD_FOOTER.sub("", text).rstrip() + "\n\n" + next_steps_block(slug) + "\n"
    elif OLD_AFTER.search(text):
        text = OLD_AFTER.sub(next_steps_block(slug) + "\n\n", text)

    text = OLD_GRANOLA.sub(
        "**Cursor does NOT author ingests.** Implement only from refined digest + evidence digest gate.",
        text,
    )

    if OLD_PLATFORM.search(text):
        text = OLD_PLATFORM.sub(platform_split_table() + "\n\n", text)
    elif "## Platform split" not in text and "## Next steps" in text:
        text = text.rstrip() + "\n\n" + platform_split_table() + "\n"

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(PROMPTS.glob("*_ingest.md")):
        if relink_file(path):
            print(f"RELINK {path.name}")
            changed += 1
    print(f"Relinked {changed} prompts")


if __name__ == "__main__":
    main()
