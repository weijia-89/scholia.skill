# ChatPRD returns — deai-operator-corpus

Live ingests and synthesis outputs:

| Stage | Path pattern |
| ----- | ------------ |
| Initial ingest | `chatprd_returns/{slug}_*_ingest.md` |
| Evidence digest | `chatprd_returns/corpus_evidence_digest_*.md` |
| Refined digest | `chatprd_returns/{slug}_refined_YYYYMMDD.md` |
| Corpus skill brief | `chatprd_returns/deai_operator_corpus_skill_brief_*.md` |
| Cursor handoff | `chatprd_returns/cursor_implement_brief_YYYYMMDD.md` |
| Composer-ready patches | `chatprd_returns/four_source_batch_composer_ready_20250629.md` |
| Refined digests (on disk) | `01_corpus_3375627_refined_ingest.md`, `05_baker_refined_ingest.md` |

## Evergreen / agent handoffs

| Artifact | Path |
| -------- | ---- |
| Composer ingest template | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |
| Incorporation plan | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |
| AGENT_01 (run first) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/AGENT_01_implement_skill_patches.md` |
| AGENT_02 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/AGENT_02_piranesi_scholia_composer_hardening.md` |

## After initial ingest

1. Save ingest from ChatPRD (Opus 4.6).
2. **Refine** — attach saved ingest + primary ATTACH + optional `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` → paste `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md`
3. **Evidence digest** — `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` (resolve NEEDS_REVIEW)
4. **Skill brief** — `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md`
5. **Cursor handoff** — `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` → `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md`

Full flow + attach tables: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/KICKOFF_ORCHESTRATOR_corpus_extraction_wave.md`

Cursor does **not** author ingests or synthesis files.
