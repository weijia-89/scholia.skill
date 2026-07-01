#!/usr/bin/env python3
"""Generate per-chapter ChatPRD ingest prompts from chapter_curriculum.yaml."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import PROJECT  # noqa: E402
from completed_ingest_slugs import is_frozen  # noqa: E402
from prompt_chain import next_steps_block  # noqa: E402

CURRICULUM = PROJECT / "chapter_curriculum.yaml"
PROMPTS = PROJECT / "prompts"


def attach_name(prefix: str, chapter_id: str) -> str:
    return f"{prefix}_{chapter_id}_ATTACH.txt"


def prompt_name(prefix: str, chapter_id: str) -> str:
    return f"{prefix}_{chapter_id}_ingest.md"


def lane_primary(lanes: list[str]) -> str:
    if "both" in lanes:
        return "both"
    if "deai_removal" in lanes:
        return "deai_removal"
    return "tic_enrichment"


def build_prompt(book: dict, chapter: dict) -> str:
    prefix = book["prefix"]
    cid = chapter["chapter_id"]
    lanes = chapter.get("lanes", ["tic_enrichment"])
    lane = lane_primary(lanes)
    attach = attach_name(prefix, cid)
    attach_abs = PROJECT / "attachments" / attach
    save_slug = f"{book['slug']}_{cid}"

    rationale = (chapter.get("rationale", "See chapter_curriculum.yaml") or "").replace("\n", " ").strip()

    boundary_block = ""
    note = chapter.get("slice_boundary_note", "").strip()
    if note:
        boundary_block = f"""
## Slice boundary (curriculum)

{note}
"""

    return f"""# ChatPRD ingest — {book.get('title', book['slug'])} — {chapter['title']}

Platform: **Opus 4.6** · Slug: `{book['slug']}` · Chapter: `{cid}` · Lane: `{lane}`  
Project: `{PROJECT}/`

## Attach

1. `{attach_abs}`

**Paste:** this prompt. Optional: `{PROJECT}/prompts/CORPUS_SYNTH_CONTRACT.md`

## Task

Extract **high-value, evidence-based** craft claims from the attached slice **only** (FR-3). Follow **CORPUS_SYNTH_CONTRACT v0.2** — quote-first, row-not-prose, mechanism + falsifier on survivors. Rank STRONG → MODERATE.

| Field | Value |
| ----- | ----- |
| chapter_id | `{cid}` only |
| rationale | {rationale} |
{boundary_block}
ESL: operator L1 Chinese — no native-norm polish; tag `[esl_preserve]`. Lanes: `{lane}` / {', '.join(lanes)}.

Canon (inherit only): `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md`

## Output (≤4500w)

Save: `{PROJECT}/chatprd_returns/{save_slug}_YYYYMMDD_ingest.md`

```markdown
# Ingest — {save_slug}

## 1) TL;DR (≤5 bullets — strongest claims first)

## 2) Coverage attestation
chapters_attested: `{cid}` only

## 3) Gate A Q-bank (verbatim from slice)
| Q-ID | quote | location hint |

## 4) Craft moves (ranked: STRONG → MODERATE)
| id | lane | claim | mechanism | scope/limit | falsifier | esl_preserve | Q-ID |

## 5) Skill incorporation (≥3 rows if borrowable)
| skill | file (absolute) | KEEP/CHANGE/ADD/DROP | diff intent | Q-ID |
```

{next_steps_block(save_slug, str(attach_abs))}
"""


def main() -> None:
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    count = 0
    for book in data.get("books", []):
        prefix = book["prefix"]
        for ch in book.get("chapters", []):
            name = prompt_name(prefix, ch["chapter_id"])
            path = PROMPTS / name
            if is_frozen(path):
                print(f"SKIP frozen {name}")
                continue
            path.write_text(build_prompt(book, ch), encoding="utf-8")
            count += 1
            print(f"PROMPT {name}")
    print(f"Wrote {count} chapter ingest prompts → {PROMPTS}")


if __name__ == "__main__":
    main()
