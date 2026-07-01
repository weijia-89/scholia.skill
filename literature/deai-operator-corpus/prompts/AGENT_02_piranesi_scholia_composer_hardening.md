# AGENT_02 — Piranesi / scholia Composer hardening (redirect)

> **Deprecated monolith.** Use orchestrator + pipeline workers instead. This file remains for bookmark compatibility.

**Scope ID:** `deai-corpus-pipeline-hardening-20260627`

---

## Use this instead

| Step | Action |
| ---- | ------ |
| 1 | Complete skill lane workers 01–05 first |
| 2 | Re-run `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md` |
| 3 | Dispatch pipeline workers 10–13 per orchestrator cards |

**Worker index:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/README.md`  
**Status:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/orchestrator_status.yaml`

---

## Worker mapping (former AGENT_02 tasks)

| Former task | Worker |
| ----------- | ------ |
| PIPELINE / ATTACHMENTS / INDEX | `workers/worker_10_scholia_pipeline_docs.md` |
| Piranesi 0630 mirror + manifest | `workers/worker_11_piranesi_0630_mirror.md` |
| synth brief + chapter prompt generator | `workers/worker_12_ingest_prompt_templates.md` |
| Evergreen MDC rule (optional) | `workers/worker_13_evergreen_mdc_rule.md` |

---

## Iron laws (unchanged)

- No Piranesi S2/S3/S4 re-runs for this corpus
- Scholia owns chapter fan-out; Piranesi mirrors flat uploads only
- Detection canon inherit from 0628 project — do not re-litigate
