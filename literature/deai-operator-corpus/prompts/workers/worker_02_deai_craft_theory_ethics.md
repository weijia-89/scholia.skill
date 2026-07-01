# Worker 02 — deai craft-theory bibliography + McKee ethics frame

**Status key:** `skill_lane.worker_02_deai_craft_theory_ethics`  
**Scope ID:** `deai-tic-corpus-wiring-20260627`  
**depends_on:** `worker_01_deai_signals` (feeling-attribution cross-ref must exist in deai SKILL first)

**Note:** User-facing name "calibration" in tic lane refers to Organization-Resistance Calibration (worker 03). This worker owns **craft-theory-reference.md** + McKee & Porter ethics bullets.

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/01_corpus_3375627_refined_ingest.md` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |

**Paste:** this prompt.

## Enforce

- Paste bibliography block **verbatim** from PATCH 1 footer section.
- McKee bullets: tag `[verified]` claims only; C-010 as `[inferred]`.
- **One file touch group:** `/Users/dubs/.cursor/skills/deai/craft-theory-reference.md` only.

---

## Task A — Bibliography (PATCH 1)

From `four_source_batch_composer_ready_20250629.md` PATCH 1 section **"Bibliography Additions for craft-theory-reference.md"**, paste all five entries into `/Users/dubs/.cursor/skills/deai/craft-theory-reference.md` (create file with header if absent).

---

## Task B — McKee & Porter ethics frame (minimal ADD)

From `01_corpus_3375627_refined_ingest.md`, ADD 3–5 bullets:

| Claim | Tag | Source |
| ----- | --- | ------ |
| Social context model | `[verified]` | C-002 |
| Transparency ethic | `[verified]` | C-003 |
| Contextual fluency continuum | `[verified]` | C-005 |
| (optional fourth bullet from C-006/C-007 if present) | per ingest tags | |
| C-010 if referenced | `[inferred]` only | |

Place under ethics / rhetorical-context subsection. Light touch — no essay prose.

**Evidence:** Plan E-07.

---

## Verify

```bash
grep "social context model" /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
grep "Liang" /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
grep "Lu, X." /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
```

| Check | PASS/FAIL |
| ----- | --------- |
| Bibliography five entries present | |
| Social context model present | |
| No `[inferred]` promoted to `[verified]` | |

**On PASS:** `orchestrator_status.yaml` → `worker_02_deai_craft_theory_ethics.status: done`

---

## Out of scope

- Edits to `/Users/dubs/.cursor/skills/deai/SKILL.md` (worker 01)
- tic.skill (workers 03–04)
