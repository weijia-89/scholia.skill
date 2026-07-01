# ChatPRD ingest — Writing Workplace Cultures — Part Two — Workplace Writing

> **Frozen** — ingest saved under `chatprd_returns/henry_2000_writing_workplace_part02_*_ingest.md`. Legacy schema; synthesis uses `synth_refine_per_source.md`.

## META

| Field | Value |
| ----- | ----- |
| Platform | ChatPRD · Opus 4.6 |
| Slug | `henry_2000_writing_workplace` |
| Chapter | `part02` — Part Two — Workplace Writing |
| Lane | `tic_enrichment` |
| Project | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/` |

## Scope

Read **attached slice only** (FR-3). `chapters_attested = `part02` only.

| rationale | Workplace genre survey. |

## ESL [esl_preserve] rules

- Operator is L1 Chinese; never recommend "sound more native" or erase legitimate L1-influenced syntax.
- Tag craft moves with `[esl_preserve]` when protecting non-native voice structure.
- Split **RLHF residue removal** (deai_removal) from **voice priming** (tic_enrichment); tag `lane` on each move.
- Structural borrow, not author pastiche — no cosplay voice.

## Canon (inherit only)

- `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md`

## ChatPRD attach

1. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/09_henry_2000_writing_workplace_part02_ATTACH.txt`

**Paste:** this prompt.

## Extract

Schema: `/Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md`

1. Metadata table (title, authors, year, venue/ISBN, text_path, ingest_path)
2. Scope + coverage_attestation
3. Key findings / claims register (C-001… with epistemic tags)
4. Verbatim quote bank Q-001… (Gate A — must appear in attached text)
5. Craft moves: `move_id` · `lane` · `structural_borrow` · `anti_pastiche` · `[esl_preserve]` · `deai_signal` · `source_anchor`
6. Lane A — deai_removal section (if lane is deai_removal or both)
7. Lane B — tic_enrichment section (if lane is tic_enrichment or both)
8. Kill-list / do-not-borrow
9. Bibliography tier
10. **Skill incorporation** table (KEEP/CHANGE/ADD/DROP per skill file)

## After save

Save to: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/henry_2000_writing_workplace_part02_YYYYMMDD_ingest.md`

**Completed ingest on disk — prompt frozen for audit.** Re-run not required.

Next (synthesis only): attach saved ingest + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/09_henry_2000_writing_workplace_part02_ATTACH.txt` → paste `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md` → `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/henry_2000_writing_workplace_part02_refined_YYYYMMDD.md`

**No Cursor skill patches from raw ingest.**
