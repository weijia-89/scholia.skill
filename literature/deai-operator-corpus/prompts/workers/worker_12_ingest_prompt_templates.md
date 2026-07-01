# Worker 12 — prompt template SSOT verify

Status: `pipeline_lane.worker_12_ingest_prompt_templates` · Scope: `deai-corpus-pipeline-hardening-20260627` · depends_on: `worker_10_scholia_pipeline_docs`

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/prompt_chain.py` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/generate_chapter_prompts.py` |
| 4 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/rewrite_chatprd_prompts.py` |

## Task

Confirm lean evidence-first prompts are SSOT:

1. **Contract** — `CORPUS_SYNTH_CONTRACT.md` defines evidence grades + ingest/refine schemas.
2. **Generators** — chapter + full-source scripts emit matching templates; footers via `prompt_chain.next_steps_block`.
3. **Synth chain** — `synth_refine_per_source.md` … `synth_cursor_implement_brief.md` reference contract (no duplicate rigor essays).
4. **PIPELINE.md** — documents regen commands + ChatPRD attach-table orchestrator default.

If drift: fix generators (not hand-edit 46 ingests). Re-run:

```bash
python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/rewrite_chatprd_prompts.py
python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/generate_chapter_prompts.py
```

Spot-check: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/01_corpus_3375627_ingest.md`, `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/11_long_2018_portable_mentor_part03_ingest.md`

## Verify

```bash
grep -l "CORPUS_SYNTH_CONTRACT" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_*.md
grep "next_steps_block" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/rewrite_chatprd_prompts.py
grep "STRONG" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/01_corpus_3375627_ingest.md
```

**On PASS:** `orchestrator_status.yaml` → `worker_12_ingest_prompt_templates.status: done`

## Out of scope

- MDC rule (worker 13)
- Skill patches
