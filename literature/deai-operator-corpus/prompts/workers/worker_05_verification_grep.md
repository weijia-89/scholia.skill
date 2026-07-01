# Worker 05 — verification, stale-claim grep, status update

**Status key:** `skill_lane.worker_05_verification_grep`  
**Scope ID:** `deai-tic-corpus-wiring-20260627`  
**depends_on:** workers 01–04 all `done`

**Role:** Read-only verification + status YAML update. **Do not edit skill files** unless grep finds a clear paste omission (then fix minimal gap only).

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/orchestrator_status.yaml` |

**Paste:** this prompt.

## Task A — four-source post-paste checklist

Run Implementation Checklist from four-source batch (quotes verbatim, no 0628 re-litigation, ESL guards, tags preserved, lane separation, kill-list excluded, paths exist).

---

## Task B — plan verification matrix

| Check | Command |
| ----- | ------- |
| deai detection-bias | `grep -l "61.22" /Users/dubs/.cursor/skills/deai/SKILL.md` |
| deai feeling-attribution | `grep "feeling-attribution" /Users/dubs/.cursor/skills/deai/SKILL.md` |
| tic non-deficit | `grep "deficit orientation" /Users/dubs/.cursor/skills/tic/SKILL.md` |
| tic feeling-deletion | `grep "Feeling-Attribution Deletion" /Users/dubs/.cursor/skills/tic/SKILL.md` |
| craft-theory ethics | `grep "social context model" /Users/dubs/.cursor/skills/deai/craft-theory-reference.md` |
| deai tests | `python3 -m pytest /Users/dubs/.cursor/skills/deai/tests/ -q` |

---

## Task C — stale / banned claim grep

```bash
grep -i "indistinguishable from human" /Users/dubs/.cursor/skills/deai/SKILL.md /Users/dubs/.cursor/skills/deai/craft-theory-reference.md || true
grep -i "plagiarism checkers fail" /Users/dubs/.cursor/skills/deai/SKILL.md || true
grep -i "sound more native" /Users/dubs/.cursor/skills/tic/SKILL.md || true
```

Matches outside kill-list **prohibition** context = FAIL.

---

## Task D — update orchestrator status

Set in `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/orchestrator_status.yaml`:

- `worker_05_verification_grep.status: done`
- `meta.last_updated: <ISO date>`
- `meta.current_lane: pipeline`
- Fill `evidence` for workers 01–05 with PASS/FAIL + date

---

## Verify summary

| Worker key | Verify | PASS/FAIL |
| ---------- | ------ | --------- |
| worker_01_deai_signals | grep 61.22 + Prompt-Formula | |
| worker_02_deai_craft_theory_ethics | social context model + Liang bib | |
| worker_03_tic_message_craft | Non-Deficit + Feeling-Deletion | |
| worker_04_tic_voice_enrichment | Deliberate Repetition + L1 signature | |
| worker_05_verification_grep | pytest PASS + stale grep clean | |

**On all PASS:** operator re-runs orchestrator for pipeline lane dispatch.

---

## Out of scope

- Pipeline doc edits (worker 10+)
- Git commit unless operator asks
