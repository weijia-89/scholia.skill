#!/usr/bin/env python3
"""Restore cleaned legacy ingest prompts for slugs already saved in chatprd_returns."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from completed_ingest_slugs import (  # noqa: E402
    discover_completed_slugs,
    prompt_path_for_slug,
)
from corpus_paths import PROJECT  # noqa: E402
from prompt_chain import SYNTH_REFINE  # noqa: E402

PROMPTS = PROJECT / "prompts"
RETURNS = PROJECT / "chatprd_returns"
MANIFEST = PROJECT / "manifest.yaml"
CURRICULUM = PROJECT / "chapter_curriculum.yaml"
CANON_0628 = (
    "/Users/dubs/Projects/piranesi.skill/research-projects/"
    "0628-deai-signal-removal/deai-signal-removal_decision_canon.md"
)

ESL = """- Operator is L1 Chinese; never recommend "sound more native" or erase legitimate L1-influenced syntax.
- Tag craft moves with `[esl_preserve]` when protecting non-native voice structure.
- Split **RLHF residue removal** (deai_removal) from **voice priming** (tic_enrichment); tag `lane` on each move.
- Structural borrow, not author pastiche — no cosplay voice."""

EXTRACT_PAPER = """1. Metadata table (title, authors, year, venue/ISBN, text_path, ingest_path)
2. Scope + coverage_attestation
3. Key findings / claims register (C-001… with epistemic tags)
4. Verbatim quote bank Q-001… (Gate A — must appear in attached text)
5. Craft moves: `move_id` · `lane` · `structural_borrow` · `anti_pastiche` · `[esl_preserve]` · `deai_signal` · `source_anchor`
6. Lane A — deai_removal section (if lane is deai_removal or both)
7. Lane B — tic_enrichment section (if lane is tic_enrichment or both)
8. Kill-list / do-not-borrow
9. Bibliography tier
10. **Skill incorporation** table (KEEP/CHANGE/ADD/DROP per skill file)"""

EXTRACT_CHAPTER = EXTRACT_PAPER  # same scholia chapter schema


def attach_abs(entry: dict) -> str:
    rel = entry.get("attach_upload") or f"attachments/{Path(entry['text_path']).stem}_ATTACH.txt"
    return str((PROJECT / rel).resolve())


def after_save_block(save_slug: str, attach: str) -> str:
    return f"""## After save

Save to: `{RETURNS}/{save_slug}_YYYYMMDD_ingest.md`

**Completed ingest on disk — prompt frozen for audit.** Re-run not required.

Next (synthesis only): attach saved ingest + `{attach}` → paste `{SYNTH_REFINE}` → `{RETURNS}/{save_slug}_refined_YYYYMMDD.md`

**No Cursor skill patches from raw ingest.**"""


def legacy_paper(entry: dict) -> str:
    slug = entry["slug"]
    title = entry.get("title", slug)
    lane = entry.get("lane_hint", "both")
    attach = attach_abs(entry)
    schema = "/Users/dubs/Projects/scholia.skill/prompts/literature-paper-ingest.md"
    authors = ", ".join(entry.get("authors") or ["unknown"])
    year = entry.get("year") or "identify on ingest"

    return f"""# ChatPRD ingest — {title}

> **Frozen** — ingest saved under `chatprd_returns/{slug}_*_ingest.md`. Legacy schema; synthesis uses `synth_refine_per_source.md`.

## META

| Field | Value |
| ----- | ----- |
| Platform | ChatPRD · Opus 4.6 |
| Slug | `{slug}` |
| Lane | `{lane}` |
| Project | `{PROJECT}/` |

## Source identity

| Field | Value |
| ----- | ----- |
| title | {title} |
| authors | {authors} |
| year | {year} |
| lane | `{lane}` |

## Scope

Read **attached primary only** (FR-3). Gate A verbatim Q-bank. ≤4500w (scholia SF-12).

## ESL [esl_preserve] rules

{ESL}

## Canon (inherit only — do not re-litigate)

- `{CANON_0628}`

## ChatPRD attach

1. `{attach}`

**Paste:** this prompt.

## Extract

Schema: `{schema}`

{EXTRACT_PAPER}

{after_save_block(slug, attach)}
"""


def legacy_chapter(book: dict, chapter: dict) -> str:
    prefix = book["prefix"]
    cid = chapter["chapter_id"]
    slug = book["slug"]
    save_slug = f"{slug}_{cid}"
    lanes = chapter.get("lanes", ["tic_enrichment"])
    lane = "both" if "both" in lanes else lanes[0]
    attach = str((PROJECT / "attachments" / f"{prefix}_{cid}_ATTACH.txt").resolve())
    schema = "/Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md"
    rationale = chapter.get("rationale", "See chapter_curriculum.yaml")
    boundary = ""
    note = (chapter.get("slice_boundary_note") or "").strip()
    if note:
        boundary = f"\n**Slice note:** {note}\n"

    return f"""# ChatPRD ingest — {book.get('title', slug)} — {chapter['title']}

> **Frozen** — ingest saved under `chatprd_returns/{save_slug}_*_ingest.md`. Legacy schema; synthesis uses `synth_refine_per_source.md`.

## META

| Field | Value |
| ----- | ----- |
| Platform | ChatPRD · Opus 4.6 |
| Slug | `{slug}` |
| Chapter | `{cid}` — {chapter['title']} |
| Lane | `{lane}` |
| Project | `{PROJECT}/` |

## Scope

Read **attached slice only** (FR-3). `chapters_attested = `{cid}` only.

| rationale | {rationale} |
{boundary}
## ESL [esl_preserve] rules

{ESL}

## Canon (inherit only)

- `{CANON_0628}`

## ChatPRD attach

1. `{attach}`

**Paste:** this prompt.

## Extract

Schema: `{schema}`

{EXTRACT_CHAPTER}

{after_save_block(save_slug, attach)}
"""


def main() -> None:
    completed = discover_completed_slugs()
    manifest = {e["slug"]: e for e in (yaml.safe_load(MANIFEST.read_text()) or {}).get("entries", [])}
    curriculum = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    chapter_by_slug = {}
    for book in curriculum.get("books", []):
        for ch in book.get("chapters", []):
            chapter_by_slug[f"{book['slug']}_{ch['chapter_id']}"] = (book, ch)

    count = 0
    for slug in sorted(completed):
        path = prompt_path_for_slug(slug)
        if not path:
            print(f"SKIP no prompt mapping: {slug}")
            continue
        if slug in chapter_by_slug:
            book, ch = chapter_by_slug[slug]
            text = legacy_chapter(book, ch)
        elif slug in manifest:
            text = legacy_paper(manifest[slug])
        else:
            print(f"SKIP no metadata: {slug}")
            continue
        path.write_text(text, encoding="utf-8")
        count += 1
        print(f"RESTORE {path.name} ({slug})")
    print(f"Restored {count} frozen legacy prompts")


if __name__ == "__main__":
    main()
