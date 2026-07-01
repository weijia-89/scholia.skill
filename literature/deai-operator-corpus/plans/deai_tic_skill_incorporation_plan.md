# deai / tic skill incorporation plan — deai-operator-corpus

**Scope ID:** `deai-tic-corpus-wiring-20260627`  
**Status:** Plan only — **do not implement in planning session**  
**Operator:** Wei Jia · ESL preserve mandatory  
**Implementor:** Cursor orchestrator + workers via `prompts/ORCHESTRATOR_deai_tic_corpus.md` (status: `plans/orchestrator_status.yaml`)

---

## Canonical refined digests (ChatPRD returns)

| Artifact | Path | Lane | Notes |
| -------- | ---- | ---- | ----- |
| McKee & Porter AIES 2020 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/01_corpus_3375627_refined_ingest.md` | both (ethics frame) | Full paper; pre-RLHF; rhetorical-context framework |
| Baker 2020 Ch.1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/05_baker_refined_ingest.md` | tic_enrichment | Ch.1 only (truncated-era ingest); chapter fan-out pending for ch3–7 |
| Four-source batch (Composer-ready) | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md` | deai + tic | Ranade, Locker, Long, Lu & Ai — **primary implement block** |
| Composer ingest discipline | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` | meta | Preprocess ChatPRD output before Cursor handoff |

**Dedupe note:** Baker duplicate in Downloads — kept `(1)` variant as `05_baker_refined_ingest.md` (richer operator metadata, 23k vs 18k).

---

## Evidence matrix (pre-implementation)

| Row | Source | Claim / patch | Tag | deai | tic | PASS |
| --- | ------ | ------------- | --- | ---- | --- | ---- |
| E-01 | Lu & Ai 2015 | Non-deficit NNS framing | verified | inherit | ADD | |
| E-02 | Liang 2023 | 61.22% NNS false-positive (detectors) | verified | ADD | — | |
| E-03 | Ranade 2024 | Prompt-formula residue (7-element sequence) | inferred, stale | ADD | — | |
| E-04 | Locker BAC 10e | Feeling-attribution deletion | inferred:craft-transfer | ADD | ADD | |
| E-05 | Long 2018 | Synonym rotation / deliberate repetition | speculative:symptom-overlap | ADD | ADD | |
| E-06 | Long 2018 | Abstract hedging → concreteness | speculative:symptom-overlap | ADD | ADD | |
| E-07 | McKee & Porter 2020 | Social context model; transparency ethic | verified | ADD (ethics) | ADD (context) | |
| E-08 | Baker 2020 Ch.1 | Workplace register / audience analysis | verified (ch1 only) | — | ADD (defer ch3–7) | |

---

## deai.skill — KEEP / CHANGE / ADD / DROP

| Action | Target | Rationale | Evidence |
| ------ | ------ | --------- | -------- |
| **KEEP** | 0628 detection canon wiring | Do not re-litigate | `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md` |
| **ADD** | Detection-bias principle (NNS false positives) | Composer-ready block | `four_source_batch_composer_ready_20250629.md` PATCH 1 |
| **ADD** | Signals: prompt-formula, genre over-conformity, audience echo-back, feeling-attribution, synonym rotation, abstract hedging | RLHF/craft overlap | same PATCH 1 |
| **ADD** | Kill-list banned claims | Prevent stale detector myths | same PATCH 1 |
| **ADD** | Bibliography: Liang, Lu & Ai, Ranade, Long, Locker | craft-theory-reference.md | same PATCH 1 |
| **ADD** | Rhetorical-context ethics frame (light touch) | McKee & Porter social-context model | `01_corpus_3375627_refined_ingest.md` C-002–C-007 |
| **DROP** | Any `[verified]` promotion of `[inferred]`/`[speculative]` without new evidence | Kill-list | four-source batch |
| **CHANGE** | RLHF wording to "feeling-attribution / RLHF residue" | Align 0628 + Locker | E-04 |

---

## tic.skill — KEEP / CHANGE / ADD / DROP

| Action | Target | Rationale | Evidence |
| ------ | ------ | --------- | -------- |
| **KEEP** | ESL preserve rules | Operator L1 Chinese | canon + Lu & Ai non-deficit quote |
| **ADD** | Non-deficit framing principle | Lu & Ai 2015 §2 | four-source PATCH 2 |
| **ADD** | Moves: subject-slot swap, negative-context passive, feeling-deletion, resistance calibration, deliberate repetition, before/after drill | Locker + Long craft | four-source PATCH 2 |
| **ADD** | Cover-letter / employment genre hooks (when Baker ch7 ingested) | Deferred until chapter ingest | Baker ch7 attach pending |
| **DROP** | "Sound more native" or elegant-variation pressure | ESL regression | evergreen + PATCH 2 guards |

---

## Composer 2.5 risk mitigations

Apply `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md`:

1. **Pre-resolve decisions** — implement from `four_source_batch_composer_ready_20250629.md` verbatim; do not re-weigh evidence.
2. **Section independence** — one patch file section per task in AGENT_01.
3. **YAML anchors** — preserve exact percentages (61.22% NNS FPR), paths, tag strings.
4. **ANTI-PATTERN blocks** — enforce kill-list and ESL guards as prohibitions.
5. **Verify per task** — grep + pytest per AGENT_01 checklist.
6. **Scope ceiling** — ≤1 file touch group per Composer session task.

Also: `prompts/synth_cursor_implement_brief.md` failure-mode blocks (scope creep, hallucinated paths, skipped verify).

---

## Chapter fan-out status (corpus infra)

| Component | Path | Status |
| --------- | ---- | ------ |
| Curriculum | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chapter_curriculum.yaml` | Done |
| Split script | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/split_chapters.py` | Done |
| Chapter slices | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/source_exports/chapters/` | 28 slices |
| Per-chapter attaches | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/*_{chapter_id}_ATTACH.txt` | Done |
| Per-chapter prompts | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/*_{chapter_id}_ingest.md` | Done |
| Papers 01–04 | Full monolith attach (no fan-out) | Done |

**Operator next ingests:** Baker ch03, ch07; Locker ch08 — highest tic yield per curriculum.

---

## Implementation order (orchestrator workers 01–05)

1. Worker 01 — PATCH 1 body → `/Users/dubs/.cursor/skills/deai/SKILL.md`  
2. Worker 02 — bibliography + McKee ethics → `craft-theory-reference.md` (∥ worker 03 after 01)  
3. Worker 03 — PATCH 2 Locker moves → `/Users/dubs/.cursor/skills/tic/SKILL.md`  
4. Worker 04 — PATCH 2 Long + Lu & Ai → tic.skill (serial after 03)  
5. Worker 05 — post-paste checklist + pytest + status yaml  

See `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/workers/README.md`

**Out of scope:** Re-ingest primaries; Piranesi S2–S4; Baker ch3–7 until operator runs chapter ingests.

---

## Verification checklist (operator fills after AGENT_01)

| Check | Command / action | PASS/FAIL |
| ----- | ---------------- | --------- |
| deai detection-bias present | `grep -l "61.22" /Users/dubs/.cursor/skills/deai/SKILL.md` | |
| deai feeling-attribution signal | `grep "feeling-attribution" /Users/dubs/.cursor/skills/deai/SKILL.md` | |
| tic non-deficit framing | `grep "deficit orientation" /Users/dubs/.cursor/skills/tic/SKILL.md` | |
| tic feeling-deletion move | `grep "Feeling-Attribution Deletion" /Users/dubs/.cursor/skills/tic/SKILL.md` | |
| ESL guards preserved | manual read `[esl_preserve]` rows | |
| deai tests | `python3 -m pytest /Users/dubs/.cursor/skills/deai/tests/ -q` | |
