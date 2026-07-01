#!/usr/bin/env python3
"""Patch ingest prompt footers for single-ingest + ChatPRD synthesis flow."""
from __future__ import annotations

import re
from pathlib import Path

PROJECT = Path("/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus")
PROMPTS = PROJECT / "prompts"

AFTER_RE = re.compile(
    r"\*\*After save:\*\*\s*\n\n.*?(?=## Platform split|## Piranesi|Piranesi wave|\Z)",
    re.DOTALL,
)

PLATFORM_RE = re.compile(
    r"## Platform split\s*\n\n.*?(?=Piranesi wave|\Z)",
    re.DOTALL,
)

NEW_AFTER = """**After save:**

1. Update `manifest.yaml` → `ingest_status: done` for this slug
2. **New ChatPRD window** → attach this saved ingest → paste `prompts/synth_refine_per_source.md`
3. Save refined digest → `chatprd_returns/{slug}_refined_YYYYMMDD.md`
4. Optional batch: `synth_corpus_skill_brief.md` → `synth_cursor_implement_brief.md` → Cursor Composer 2.5

**Cursor implement:** only from `cursor_implement_brief_*.md` — never patch skills directly from raw ingest.

"""

NEW_PLATFORM = """## Platform split

| Role | Platform | Action |
| ---- | -------- | ------ |
| Ingest author | ChatPRD · Opus 4.6 | This prompt + `_ATTACH.txt` |
| Refine / synthesis | ChatPRD · Opus 4.6 | `synth_refine_per_source.md` → `_refined_*.md` |
| Corpus brief | ChatPRD · Opus 4.6 | `synth_corpus_skill_brief.md` |
| Implementor handoff | ChatPRD · Opus 4.6 | `synth_cursor_implement_brief.md` |
| Skill patches | Cursor · Composer 2.5 | Execute handoff only — compensates Auto reasoning gaps |

"""


def main() -> None:
    for path in sorted(PROMPTS.glob("*_ingest.md")):
        text = path.read_text(encoding="utf-8")
        if "synth_refine_per_source" in text and "Composer 2.5" in text:
            print(f"SKIP {path.name}")
            continue
        if AFTER_RE.search(text):
            text = AFTER_RE.sub(NEW_AFTER, text)
        if PLATFORM_RE.search(text):
            text = PLATFORM_RE.sub(NEW_PLATFORM, text)
        text = re.sub(
            r"Piranesi wave S1–S4.*?\n",
            "",
            text,
        )
        path.write_text(text, encoding="utf-8")
        print(f"PATCH {path.name}")


if __name__ == "__main__":
    main()
