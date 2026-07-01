# ChatPRD ingest — The Writer's Portable Mentor — Part I — Your Move

Platform: **Opus 4.6** · Slug: `long_2018_portable_mentor` · Chapter: `part01` · Lane: `both`  
Project: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`

## Attach

1. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part01_ATTACH.txt`

**Paste:** this prompt. Optional: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

## Task

Extract **high-value, evidence-based** craft claims from the attached slice **only** (FR-3). Follow **CORPUS_SYNTH_CONTRACT v0.2** — quote-first, row-not-prose, mechanism + falsifier on survivors. Rank STRONG → MODERATE.

| Field | Value |
| ----- | ----- |
| chapter_id | `part01` only |
| rationale | Daily writing + working with language / gathering words — diction foundations for deai_removal and tic habit. |

ESL: operator L1 Chinese — no native-norm polish; tag `[esl_preserve]`. Lanes: `both` / both.

Canon (inherit only): `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md`

## Output (≤4500w)

Save: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part01_YYYYMMDD_ingest.md`

```markdown
# Ingest — long_2018_portable_mentor_part01

## 1) TL;DR (≤5 bullets — strongest claims first)

## 2) Coverage attestation
chapters_attested: `part01` only

## 3) Gate A Q-bank (verbatim from slice)
| Q-ID | quote | location hint |

## 4) Craft moves (ranked: STRONG → MODERATE)
| id | lane | claim | mechanism | scope/limit | falsifier | esl_preserve | Q-ID |

## 5) Skill incorporation (≥3 rows if borrowable)
| skill | file (absolute) | KEEP/CHANGE/ADD/DROP | diff intent | Q-ID |
```

## Next steps (after save)

**Iron law:** No Cursor skill patches from raw ingest.

1. **Refine** — new ChatPRD window; attach saved ingest + primary attach (Gate A).
   - Primary Gate A: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part01_ATTACH.txt`
   - Optional contract: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`
   - Paste: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md`
   - Save: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part01_refined_YYYYMMDD.md`
2. **Evidence digest** (batch) — attach up to 8 `_refined_*.md`; paste `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md`; resolve NEEDS_REVIEW; save `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/corpus_evidence_digest_YYYYMMDD.md`
3. **Skill brief** — `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` → `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` → Cursor `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md`

**Contract:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` · **Pipeline:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md`

## Platform split

| Role | Platform | Prompt path |
| ---- | -------- | ----------- |
| Ingest author | ChatPRD · Opus 4.6 | This file + chapter/paper attach |
| Evidence filter | ChatPRD · Opus 4.6 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` |
| Cross-source merge | ChatPRD · Opus 4.6 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` |
| Implement plan | ChatPRD · Opus 4.6 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` |
| Cursor handoff | ChatPRD · Opus 4.6 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` |
| Skill patches | Cursor · Composer 2.5 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md` + workers only |

