# Worker 03 — tic.skill message craft moves (Locker / PATCH 2 part A)

**Status key:** `skill_lane.worker_03_tic_message_craft`  
**Scope ID:** `deai-tic-corpus-wiring-20260627`  
**depends_on:** `worker_01_deai_signals` (feeling-attribution cross-ref in deai SKILL)

**Cover-letter note:** Employment-genre cover-letter hooks are **deferred** until Baker ch07 + Locker ch08 chapter ingests complete. This worker applies four-source **message craft** moves that underpin professional letters — not Baker/Locker chapter-specific templates.

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |

**Paste:** this prompt.

## Enforce

- **MUST NOT** add "sound more native" or elegant-variation pressure.
- Keep every `[esl_preserve]` tag verbatim.
- **ANTI-PATTERN halt:** if kill-list conflict, stop and report.
- **One file touch group:** `/Users/dubs/.cursor/skills/tic/SKILL.md` only — **first half** of PATCH 2.

---

## Task

From PATCH 2 in four-source batch, paste into `/Users/dubs/.cursor/skills/tic/SKILL.md` under voice-craft (create section if absent):

| Section | Action |
| ------- | ------ |
| Core Principle: Non-Deficit Framing | ADD |
| Move: Subject-Slot Swap | ADD |
| Move: Negative-Context Passive/Impersonal | ADD |
| Move: Feeling-Attribution Deletion | ADD |
| Move: Organization-Resistance Calibration | ADD |

**Stop before** "Move: Deliberate Repetition" — worker 04 owns remainder.

**Evidence:** Plan E-01, E-04 (partial).

---

## Verify

```bash
grep "Non-Deficit Framing" /Users/dubs/.cursor/skills/tic/SKILL.md
grep "Feeling-Attribution Deletion" /Users/dubs/.cursor/skills/tic/SKILL.md
grep "Organization-Resistance Calibration" /Users/dubs/.cursor/skills/tic/SKILL.md
grep "deficit orientation" /Users/dubs/.cursor/skills/tic/SKILL.md
```

| Check | PASS/FAIL |
| ----- | --------- |
| Non-deficit quote present | |
| Feeling-deletion move present | |
| Resistance calibration present | |
| No native-norm polish language added | |

**On PASS:** `orchestrator_status.yaml` → `worker_03_tic_message_craft.status: done`

---

## Out of scope

- Long / Lu & Ai enrichment moves (worker 04)
- Kill List section at PATCH 2 footer (worker 04)
- Baker ch07 cover-letter genre hooks (chapter ingest deferred)
