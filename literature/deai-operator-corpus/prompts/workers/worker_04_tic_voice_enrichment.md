# Worker 04 — tic.skill voice enrichment (Long + Lu & Ai / PATCH 2 part B)

**Status key:** `skill_lane.worker_04_tic_voice_enrichment`  
**Scope ID:** `deai-tic-corpus-wiring-20260627`  
**depends_on:** `worker_03_tic_message_craft` (same file; append after Locker moves)

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md` |

**Paste:** this prompt.

## Enforce

- Paste blocks **verbatim** after worker 03 sections in voice-craft.
- Preserve `[speculative:symptom-overlap]`, `[inferred:craft-transfer]`, `[esl_preserve]` tags.
- **ANTI-PATTERN halt** on kill-list conflicts.

---

## Task

From PATCH 2, append to `/Users/dubs/.cursor/skills/tic/SKILL.md` voice-craft section:

| Section | Action |
| ------- | ------ |
| Move: Deliberate Repetition | ADD |
| Move: Before/After Paragraph Revision Drill | ADD |
| Move: L1-Chinese Syntactic Signature as Voice Resource | ADD |
| Move: Lexicon Practice (Enrichment Drill) | ADD |
| Kill List — Patterns to Reject | ADD |

**Evidence:** Plan E-05; Long + Lu & Ai craft transfer rows.

---

## Verify

```bash
grep "Deliberate Repetition" /Users/dubs/.cursor/skills/tic/SKILL.md
grep "L1-Chinese Syntactic Signature" /Users/dubs/.cursor/skills/tic/SKILL.md
grep "Kill List" /Users/dubs/.cursor/skills/tic/SKILL.md
grep "sound more natural" /Users/dubs/.cursor/skills/tic/SKILL.md
```

Last grep should match only **prohibition** context in kill list, not affirmative guidance.

| Check | PASS/FAIL |
| ----- | --------- |
| Deliberate repetition move present | |
| L1-Chinese signature move present | |
| Kill list present | |
| ESL guards intact | |

**On PASS:** `orchestrator_status.yaml` → `worker_04_tic_voice_enrichment.status: done`

---

## Out of scope

- Locker moves (worker 03 — do not duplicate)
- deai.skill files
- pytest (worker 05)
