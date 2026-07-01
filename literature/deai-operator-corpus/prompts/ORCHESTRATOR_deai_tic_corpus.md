# ORCHESTRATOR — deai / tic corpus implement wave

**Role:** Dispatch-only. No skill patches, primaries, or ChatPRD ingests in this turn.

**Scope:** skill `deai-tic-corpus-wiring-20260627` · pipeline `deai-corpus-pipeline-hardening-20260627`

**ChatPRD waves:** use `KICKOFF_ORCHESTRATOR_corpus_extraction_wave.md` + attach table (Prompt | Attach | Save to). Contract: `CORPUS_SYNTH_CONTRACT.md`.

## Read (≤3)

Paste this prompt only.

1. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md`
2. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/orchestrator_status.yaml`
3. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/README.md`

Do not read: primaries, `*_ATTACH.txt`, raw `*_ingest.md`.

## Iron laws

| Law | Rule |
| --- | ---- |
| ChatPRD authors ingests | Opus/ChatPRD only for S1 refine + synthesis |
| Composer implements | Workers paste from handoffs; no re-weighing evidence |
| No 0628 re-litigation | Inherit `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md` |
| ESL preserve | Every `[esl_preserve]` tag retained verbatim |
| Context budget | ≤8 files per **ChatPRD** window (operator attaches); ≤4 paths per **Cursor** worker (agent reads from disk) |
| One file touch group | Each worker edits one logical file cluster only |
| ANTI-PATTERN halt | Workers halt and report if patch conflicts with kill-list |

---

## Your workflow each turn

1. Read `orchestrator_status.yaml` — find first worker with `status: pending` whose `depends_on` are all `done`.
2. If skill lane incomplete, stay on skill lane. Pipeline lane unlocks after `worker_05_verification_grep` is `done`.
3. Output **operator dispatch card** (template below). Do not run worker tasks yourself.
4. After operator reports completion, tell them which YAML keys to set `done` + which verify commands to record under `evidence`.
5. Repeat until all non-optional workers are `done` or `blocked`.

---

## Dispatch order (serial defaults)

### Skill lane (run first)

| Order | Status key | Worker prompt | Parallel? |
| ----- | ---------- | ------------- | ----------- |
| 1 | `worker_01_deai_signals` | `workers/worker_01_deai_signals_patch.md` | — |
| 2a | `worker_02_deai_craft_theory_ethics` | `workers/worker_02_deai_craft_theory_ethics.md` | **Yes** with 2b after step 1 |
| 2b | `worker_03_tic_message_craft` | `workers/worker_03_tic_message_craft.md` | **Yes** with 2a after step 1 |
| 3 | `worker_04_tic_voice_enrichment` | `workers/worker_04_tic_voice_enrichment.md` | — (same file as 2b) |
| 4 | `worker_05_verification_grep` | `workers/worker_05_verification_grep.md` | — |

### Pipeline lane (after skill lane PASS)

| Order | Status key | Worker prompt | Parallel? |
| ----- | ---------- | ------------- | ----------- |
| 5a | `worker_10_scholia_pipeline_docs` | `workers/worker_10_scholia_pipeline_docs.md` | **Yes** with 5b |
| 5b | `worker_11_piranesi_0630_mirror` | `workers/worker_11_piranesi_0630_mirror.md` | **Yes** with 5a |
| 6 | `worker_12_ingest_prompt_templates` | `workers/worker_12_ingest_prompt_templates.md` | — |
| 7 | `worker_13_evergreen_mdc_rule` | `workers/worker_13_evergreen_mdc_rule.md` | Optional; anytime |

---

## Operator dispatch card (output this)

```markdown
## Next worker: {status_key}

**Composer session:** new chat · Composer 2.5 or Auto pool

**Paste prompt:**
/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/{worker_file}.md

**Read from disk (≤4):** agent reads paths listed in worker prompt — operator does not @-attach.

| # | Path |
| - | ---- |
| 1 | … |
| 2 | … |

**After worker finishes:**
1. Run verify commands from worker prompt
2. Set `orchestrator_status.yaml` → `{status_key}.status: done`
3. Fill `{status_key}.evidence` with PASS/FAIL + date
4. Re-run orchestrator for next dispatch

**Blocked?** Set `status: blocked`, fill `blocked_reason`, do not skip depends_on.
```

---

## Worker index (absolute paths)

| Key | Prompt |
| --- | ------ |
| worker_01_deai_signals | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_01_deai_signals_patch.md` |
| worker_02_deai_craft_theory_ethics | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_02_deai_craft_theory_ethics.md` |
| worker_03_tic_message_craft | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_03_tic_message_craft.md` |
| worker_04_tic_voice_enrichment | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_04_tic_voice_enrichment.md` |
| worker_05_verification_grep | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_05_verification_grep.md` |
| worker_10_scholia_pipeline_docs | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_10_scholia_pipeline_docs.md` |
| worker_11_piranesi_0630_mirror | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_11_piranesi_0630_mirror.md` |
| worker_12_ingest_prompt_templates | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_12_ingest_prompt_templates.md` |
| worker_13_evergreen_mdc_rule | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/worker_13_evergreen_mdc_rule.md` |

Full dependency graph: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/README.md`

---

## Deprecated monolith redirects

- `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/AGENT_01_implement_skill_patches.md` → workers 01–05
- `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/AGENT_02_piranesi_scholia_composer_hardening.md` → workers 10–13

---

## Out of scope (orchestrator never dispatches)

- ChatPRD per-chapter ingests (operator runs manually; track under `chapter_ingest_deferred`)
- Piranesi S2/S3/S4 re-export
- Git commit (operator asks explicitly)
- Reading `source_exports/` or `attachments/*_ATTACH.txt`
