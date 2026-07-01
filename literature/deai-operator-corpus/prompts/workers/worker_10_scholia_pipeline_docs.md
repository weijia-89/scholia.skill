# Worker 10 — scholia pipeline docs (PIPELINE, ATTACHMENTS, INDEX)

**Status key:** `pipeline_lane.worker_10_scholia_pipeline_docs`  
**Scope ID:** `deai-corpus-pipeline-hardening-20260627`  
**depends_on:** `worker_05_verification_grep`

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md` |
| 3 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chapter_curriculum.yaml` |

**Paste:** this entire prompt.

---

## Evergreen rules (apply to doc edits)

| Rule | Target |
| ---- | ------ |
| Context length (~2000 tokens per handoff section; ≤3–4 files) | Document in PIPELINE orchestrator section |
| Section independence | Per-chapter ingest prompts |
| Do not claim "Auto routes to Composer 2.5" | Use "Auto pool" wording |
| stale_after / review_by on handoffs | Note in PIPELINE Step 5 |

---

## Task A — PIPELINE.md chapter fan-out + orchestrator

**Path:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md`

- ENSURE Step 1b documents per-chapter `{prefix}_{chapter_id}_ATTACH.txt` + matching ingest prompt.
- ADD orchestrator-first Step 5: ORCHESTRATOR → workers 01–05 (skill) then 10–13 (pipeline).
- ADD 8-file ChatPRD window budget note.

---

## Task B — ATTACHMENTS.md flat folder rules

**Path:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/ATTACHMENTS.md`

- UPDATE chapter naming `{prefix}_{chapter_id}_ATTACH.txt`; no subfolders.
- Papers 01–04 monolith attach only.
- ADD orchestrator + workers index row.

---

## Task C — INDEX.md agent handoff rows

**Path:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/INDEX.md`

- ADD rows: ORCHESTRATOR, `plans/orchestrator_status.yaml`, workers README, plan path.
- UPDATE Step 5 implement row: orchestrator-first (deprecate monolith AGENT_01/02 as redirects).

---

## Verify

```bash
grep "chapter_id" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md
grep "ORCHESTRATOR" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md
grep "ORCHESTRATOR" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/INDEX.md
grep "worker_01" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/INDEX.md
```

**On PASS:** `orchestrator_status.yaml` → `worker_10_scholia_pipeline_docs.status: done`

---

## Out of scope

- Piranesi 0630 paths (worker 11)
- Ingest script changes (worker 12)
- Skill file patches
