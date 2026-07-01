# deai-operator-corpus — ChatPRD ingest orchestration

**Root:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`  
**Piranesi sibling (wave S1–S4 batch):** `/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/`  
**Detection canon (inherit, do not re-litigate):** `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/`

## Pipeline (single ingest → ChatPRD synthesis → Cursor Composer 2.5)

| Step | Platform | Prompt / action |
| ---- | -------- | ----------------- |
| 1 Ingest | ChatPRD | `{prefix}_ingest.md` + `attachments/{prefix}_ATTACH.txt` → `chatprd_returns/` |
| 2 Refine | ChatPRD | `synth_refine_per_source.md` → `{slug}_refined_*.md` |
| 3 Corpus brief | ChatPRD | `synth_corpus_skill_brief.md` (optional) |
| 4 Handoff | ChatPRD | `synth_cursor_implement_brief.md` (+ optional `evergreen_chatprd_composer_ingest.md` preprocess) |
| 5 Implement | Cursor orchestrator → workers | `ORCHESTRATOR_deai_tic_corpus.md` → `prompts/workers/worker_01_*` … `worker_05_*` (skill), then `worker_10_*` … (pipeline) |

See `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md`

**No Piranesi S2–S4 re-runs for this corpus.**

## Separation

| Concern | Owner | Path |
| ------- | ----- | ---- |
| Per-source ChatPRD ingest | scholia corpus (this project) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/` |
| Piranesi wave S1–S4 batch | piranesi.skill | `/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/` |
| deai.skill / tic.skill wiring | Cursor implementor | separate patch wave after operator synthesis |

## Operator quick start

1. Export text: `bash /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/export_text.sh`
2. Open ChatPRD (Opus 4.6) → attach **one** `attachments/{prefix}_ATTACH.txt` (see `ATTACHMENTS.md`)
3. Paste prompt: `prompts/{prefix}_ingest.md`
4. Save return to `chatprd_returns/{slug}_YYYYMMDD_ingest.md`
5. Update `manifest.yaml` → `ingest_status: done`
6. When ready: trigger Cursor to implement skill patches from Skill incorporation tables

## Key paths

| File | Path |
| ---- | ---- |
| Manifest SSOT | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/manifest.yaml` |
| ChatPRD upload files | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/` (`*_ATTACH.txt` only) |
| Full text exports (not uploaded) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/source_exports/` |
| ChatPRD prompts | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/` (see `PIPELINE.md`) |
| ChatPRD returns | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/` |
| Incorporation plan | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |
| Orchestrator (dispatch) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md` |
| Orchestrator status | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/orchestrator_status.yaml` |
| Worker index | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/README.md` |
| AGENT_01 (redirect) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/AGENT_01_implement_skill_patches.md` |
| AGENT_02 (redirect) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/AGENT_02_piranesi_scholia_composer_hardening.md` |
| Evergreen Composer ingest | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |
| Granola returns | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/granola_returns/` |
| ATTACHMENTS runbook | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/ATTACHMENTS.md` |
| STATUS | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/STATUS.md` |

## Prompt index

| Prefix | Slug | Prompt |
| ------ | ---- | ------ |
| 01 | corpus_3375627 | `prompts/01_corpus_3375627_ingest.md` |
| 02 | jones_2015_jslw | `prompts/02_jones_2015_jslw_ingest.md` |
| 03 | s00146_2024_ai_writing | `prompts/03_s00146_2024_ai_writing_ingest.md` |
| 04 | s40979_2024_ai_writing | `prompts/04_s40979_2024_ai_writing_ingest.md` |
| 05–13 | textbooks | `prompts/{prefix}_{slug}_ingest.md` |

Wave batch (Piranesi): `/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/prompts/wave_01_s1_chatprd.md`  
Wave batch (scholia papers): `prompts/wave_01_papers_chatprd.md`
