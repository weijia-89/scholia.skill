# Worker 11 — Piranesi 0630 mirror + separation guard

**Status key:** `pipeline_lane.worker_11_piranesi_0630_mirror`  
**Scope ID:** `deai-corpus-pipeline-hardening-20260627`  
**depends_on:** `worker_05_verification_grep`  
**Parallel with:** worker 10 (different repo paths)

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md` |
| 2 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/INDEX.md` |
| 3 | `/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/ATTACHMENTS.md` |

**Paste:** this entire prompt.

---

## Iron laws

- Scholia owns chapter fan-out; Piranesi mirrors flat upload files only — **no duplicate slice packs**.
- **No** Piranesi S2/S3/S4 re-runs for this corpus.
- Cursor implements from `chatprd_returns/` only.
- Detection canon inherit: `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md`

---

## Task A — Piranesi ATTACHMENTS.md sync note

**Path:** `/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/ATTACHMENTS.md`

ADD section:

- scholia corpus owns per-chapter fan-out at `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/`
- Piranesi 0630 wave uses monolith paper attaches only for S1 batch
- No duplicate chapter slice packs in Piranesi tree

Create file with header if absent.

---

## Task B — Separation guard in 0630 manifest

**Path:** `/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/manifest.yaml` (if present) or README in same directory

ADD note:

```yaml
ingest_author: scholia
implement_from: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/
orchestrator: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md
```

---

## Verify

```bash
grep -i scholia /Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/ATTACHMENTS.md
grep -i "chatprd_returns" /Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/manifest.yaml /Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus/README.md 2>/dev/null || true
```

**On PASS:** `orchestrator_status.yaml` → `worker_11_piranesi_0630_mirror.status: done`

---

## Out of scope

- Scholia PIPELINE/INDEX edits (worker 10)
- Skill patches
- Re-export PDFs
