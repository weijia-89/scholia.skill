#!/usr/bin/env python3
"""Rewrite full-source ChatPRD ingest prompts — lean evidence-first template."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import PROJECT  # noqa: E402
from completed_ingest_slugs import is_frozen  # noqa: E402
from prompt_chain import next_steps_block  # noqa: E402

PROMPTS = PROJECT / "prompts"
CANON_0628 = (
    "/Users/dubs/Projects/piranesi.skill/research-projects/"
    "0628-deai-signal-removal/deai-signal-removal_decision_canon.md"
)
CONTRACT = f"{PROJECT}/prompts/CORPUS_SYNTH_CONTRACT.md"


def attach_abs(entry: dict) -> str:
    rel = entry.get("attach_upload") or f"attachments/{Path(entry['text_path']).stem}_ATTACH.txt"
    return str((PROJECT / rel).resolve())


def build_prompt(entry: dict) -> str:
    slug = entry["slug"]
    prefix = Path(entry["text_path"]).stem
    lane = entry.get("lane_hint", "both")
    stype = entry.get("source_type", "paper")
    title = entry.get("title", slug)
    attach = attach_abs(entry)
    save = f"{PROJECT}/chatprd_returns/{slug}_YYYYMMDD_ingest.md"

    fanout = ""
    if entry.get("chapter_fanout"):
        fanout = (
            f"\n**Chapter fan-out preferred** — use `{PROMPTS}/{prefix}_*_ingest.md` "
            f"per `{PROJECT}/chapter_curriculum.yaml`. Full attach below is fallback only.\n"
        )

    paper_claims = ""
    craft_section = "## 4) Craft moves (ranked STRONG → MODERATE)"
    skill_section = "## 5) Skill incorporation (≥3 rows if borrowable)"
    kill_section = "## 6) Kill-list / dropped"
    if stype == "paper":
        paper_claims = """
## 4) Claims register (STRONG/MODERATE only)
| C-ID | claim | tag | Q-ID |
"""
        craft_section = "## 5) Craft moves (ranked STRONG → MODERATE)"
        skill_section = "## 6) Skill incorporation (≥3 rows if borrowable)"
        kill_section = "## 7) Kill-list / dropped"

    scope_line = "attached primary only (FR-3)."
    if stype == "textbook" and entry.get("chapter_fanout"):
        scope_line = "attached slice only (FR-3). Prefer chapter fan-out ingests."

    return f"""# ChatPRD ingest — {title}

Platform: **Opus 4.6** · Slug: `{slug}` · Lane: `{lane}` · Type: {stype}  
Project: `{PROJECT}/`

## Attach

1. `{attach}`

**Paste:** this prompt. Optional: `{CONTRACT}`

## Task

Extract **high-value, evidence-based** claims from {scope_line} Follow **CORPUS_SYNTH_CONTRACT v0.2** — quote-first, row-not-prose, mechanism + falsifier. Rank STRONG → MODERATE.{fanout}
ESL: L1 Chinese — no native-norm polish; `[esl_preserve]`. Lane: `{lane}`.

Canon (inherit only): `{CANON_0628}`

## Output (≤4500w)

Save: `{save}`

```markdown
# Ingest — {slug}

## 1) TL;DR (≤5 bullets — STRONG first)

## 2) Coverage attestation
scope: {scope_line}

## 3) Gate A Q-bank (verbatim)
| Q-ID | quote | location hint |
{paper_claims}
{craft_section}
| id | lane | claim | mechanism | scope/limit | falsifier | esl_preserve | Q-ID |

{skill_section}
| skill | file (absolute) | KEEP/CHANGE/ADD/DROP | diff intent | Q-ID |

{kill_section}
| id | reason |
```

{next_steps_block(slug, attach)}
"""


def main() -> None:
    data = yaml.safe_load((PROJECT / "manifest.yaml").read_text(encoding="utf-8")) or {}
    count = 0
    for entry in data.get("entries", []):
        prefix = Path(entry["text_path"]).stem
        path = PROMPTS / f"{prefix}_ingest.md"
        if is_frozen(path):
            print(f"SKIP frozen {path.name}")
            continue
        path.write_text(build_prompt(entry), encoding="utf-8")
        count += 1
        print(f"WROTE {path.name}")
    print(f"Rewrote {count} full-source ingest prompts")


if __name__ == "__main__":
    main()
