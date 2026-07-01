#!/usr/bin/env python3
"""Canonical ChatPRD synthesis chain paths — single source for relink."""
from __future__ import annotations

from pathlib import Path

PROJECT = Path("/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus")
PROMPTS = PROJECT / "prompts"
RETURNS = PROJECT / "chatprd_returns"

SYNTH_REFINE = PROMPTS / "synth_refine_per_source.md"
SYNTH_CONTRACT = PROMPTS / "CORPUS_SYNTH_CONTRACT.md"
SYNTH_SCRATCHPAD = PROJECT / "localonly/research/opus46-synthesis-scratchpad.md"
SYNTH_EVIDENCE = PROMPTS / "synth_corpus_evidence_digest.md"
SYNTH_SKILL_BRIEF = PROMPTS / "synth_corpus_skill_brief.md"
SYNTH_CURSOR = PROMPTS / "synth_cursor_implement_brief.md"
PIPELINE = PROMPTS / "PIPELINE.md"
KICKOFF = PROMPTS / "KICKOFF_ORCHESTRATOR_corpus_extraction_wave.md"
ORCHESTRATOR = PROMPTS / "ORCHESTRATOR_deai_tic_corpus.md"
EVERGREEN = PROMPTS / "evergreen_chatprd_composer_ingest.md"


def next_steps_block(save_slug: str, attach_abs: str | None = None) -> str:
    gate_a = f"\n   - Primary Gate A: `{attach_abs}`" if attach_abs else ""
    return f"""## Next steps (after save)

**Iron law:** No Cursor skill patches from raw ingest.

1. **Refine** — new ChatPRD window; attach saved ingest + primary attach (Gate A).{gate_a}
   - Optional contract: `{SYNTH_CONTRACT}`
   - Paste: `{SYNTH_REFINE}`
   - Save: `{RETURNS}/{save_slug}_refined_YYYYMMDD.md`
2. **Evidence digest** (batch) — attach up to 8 `_refined_*.md`; paste `{SYNTH_EVIDENCE}`; resolve NEEDS_REVIEW; save `{RETURNS}/corpus_evidence_digest_YYYYMMDD.md`
3. **Skill brief** — `{SYNTH_SKILL_BRIEF}` → `{SYNTH_CURSOR}` → Cursor `{ORCHESTRATOR}`

**Contract:** `{SYNTH_CONTRACT}` · **Pipeline:** `{PIPELINE}`"""


def platform_split_table() -> str:
    return f"""## Platform split

| Role | Platform | Prompt path |
| ---- | -------- | ----------- |
| Ingest author | ChatPRD · Opus 4.6 | This file + chapter/paper attach |
| Evidence filter | ChatPRD · Opus 4.6 | `{SYNTH_REFINE}` + `{SYNTH_CONTRACT}` |
| Cross-source merge | ChatPRD · Opus 4.6 | `{SYNTH_EVIDENCE}` |
| Implement plan | ChatPRD · Opus 4.6 | `{SYNTH_SKILL_BRIEF}` |
| Cursor handoff | ChatPRD · Opus 4.6 | `{SYNTH_CURSOR}` |
| Skill patches | Cursor · Composer 2.5 | `{ORCHESTRATOR}` + workers only |"""
