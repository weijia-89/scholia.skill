# Worker 01 — deai.skill signals patch (PATCH 1 body)

**Status key:** `skill_lane.worker_01_deai_signals`  
**Scope ID:** `deai-tic-corpus-wiring-20260627`  
**IRON LAW:** Execute only. Do not re-read primaries. Do not author ingests. Do not re-litigate 0628 detection canon.

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |

**Paste:** this prompt.

## Enforce

- **DIRECTIVE** / **MUST** lines in four-source batch = hard constraints.
- **ANTI-PATTERN** / kill-list blocks = prohibitions — **halt and report** conflicts.
- Paste patch blocks **verbatim** — no paraphrase.
- **One file touch group:** this worker touches `/Users/dubs/.cursor/skills/deai/SKILL.md` only.

---

## Task

From `four_source_batch_composer_ready_20250629.md` **PATCH 1**, paste into `/Users/dubs/.cursor/skills/deai/SKILL.md`:

| Section | Action |
| ------- | ------ |
| Detection-Bias Principle | ADD under detection-bias / signal-identification (create section if absent) |
| Signal: Prompt-Formula Residue | ADD |
| Signal: Genre Over-Conformity | ADD |
| Signal: Audience Echo-Back | ADD |
| Signal: Feeling-Attribution (RLHF Residue) | ADD |
| Signal: Synonym Rotation | ADD |
| Signal: Abstract Hedging | ADD |
| Banned Claims — Kill List | ADD |

**Do NOT** paste bibliography entries (worker 02 owns `craft-theory-reference.md`).

**ESL guard:** Preserve every ESL guard paragraph verbatim.

**Evidence:** Plan E-02 through E-06.

---

## Verify

```bash
grep -c "61.22" /Users/dubs/.cursor/skills/deai/SKILL.md
grep "Prompt-Formula" /Users/dubs/.cursor/skills/deai/SKILL.md
grep "feeling-attribution" /Users/dubs/.cursor/skills/deai/SKILL.md
grep "\[esl_preserve\]" /Users/dubs/.cursor/skills/deai/SKILL.md
```

| Check | PASS/FAIL |
| ----- | --------- |
| 61.22% NNS FPR present | |
| Prompt-Formula signal present | |
| Kill-list not violated as supported claims | |
| No 0628 canon re-litigation | |

**On PASS:** operator sets `orchestrator_status.yaml` → `worker_01_deai_signals.status: done`

---

## Out of scope

- `craft-theory-reference.md` (worker 02)
- `tic.skill` (workers 03–04)
- pytest (worker 05)
- Git commit unless operator asks
