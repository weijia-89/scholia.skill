# AGENT_01 — Implement deai / tic skill patches (redirect)

> **Deprecated monolith.** Use orchestrator + worker prompts instead. This file remains for bookmark compatibility.

**Scope ID:** `deai-tic-corpus-wiring-20260627`

---

## Use this instead

| Step | Action |
| ---- | ------ |
| 1 | Open `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md` |
| 2 | Attach plan + status + workers README (see orchestrator prompt) |
| 3 | Follow orchestrator dispatch cards for workers 01–05 |

**Worker index:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/README.md`  
**Status:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/orchestrator_status.yaml`

---

## Worker mapping (former AGENT_01 tasks)

| Former task | Worker |
| ----------- | ------ |
| PATCH 1 deai signals | `workers/worker_01_deai_signals_patch.md` |
| Bibliography + McKee ethics | `workers/worker_02_deai_craft_theory_ethics.md` |
| PATCH 2 Locker message craft | `workers/worker_03_tic_message_craft.md` |
| PATCH 2 Long voice enrichment | `workers/worker_04_tic_voice_enrichment.md` |
| Checklist + pytest | `workers/worker_05_verification_grep.md` |

---

## Iron laws (unchanged)

- ChatPRD authors ingests; Composer implements from handoffs
- No 0628 re-litigation
- ESL preserve mandatory
- ≤4 attach per worker

After skill lane PASS → orchestrator dispatches pipeline workers 10–13 (formerly AGENT_02).
