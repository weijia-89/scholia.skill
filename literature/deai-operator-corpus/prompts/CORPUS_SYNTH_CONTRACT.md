# Corpus synthesis contract v0.2 (ChatPRD · Opus 4.6)

Project: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`  
Research scratchpad: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/research/opus46-synthesis-scratchpad.md`

## Mission

Preserve **semantics + mechanism + scope + primary anchors** across multi-stage synthesis. Extract high-value, high-evidence craft claims from closed-corpus primaries. **Drop** generic advice and unanchored paraphrase — but **never** drop survivor content to save words.

This contract governs: ingest → `synth_refine_per_source.md` → `synth_corpus_evidence_digest.md` → `synth_corpus_skill_brief.md` → `synth_cursor_implement_brief.md`.

---

## Opus 4.6 operating mode (synthesis author)

| Rule | Why |
| ---- | --- |
| **Gate A before kill/score** | External grounding beats intrinsic self-critique ([HUANG-SELFCORRECT-2023]; palamedes) |
| **Supplemental web verification** | Gate A mandatory for craft from primary; web confirms load-bearing external facts only (≤5 searches/window; palamedes P2–P3 bar) |
| **Adaptive depth** | Use full reasoning on verbatim match + mechanism extraction; do not rush to TL;DR |
| **Fresh window per stage** | Avoid lossy in-chat compaction; handoffs = files on disk |
| **≤8 attaches / window** | Effective context ≠ advertised 1M; split digest parts if needed |
| **≤4500w output / window** | Length degradation 13.9–85% on long tasks (Du et al. 2025, scholia C-R008) |

---

## Semantic preservation protocol (mandatory)

Execute **in order** every stage:

1. **Quote-first** — Build verbatim Q-bank from primary **before** craft moves, kill register, or merge.
2. **Row-not-prose** — Survivors live in **tables only**. No paragraph that restates table rows (TL;DR indexes IDs only).
3. **Provenance chain** — Every survivor row: `source_slug · source_row_id · Q-ID(s)`.
4. **Mechanism mandatory** — Empty mechanism → max MODERATE; empty falsifier → NEEDS_REVIEW.
5. **No summary-of-summary merge** — Cross-source digest merges **refined table rows**, never ingest TL;DR prose.
6. **Position anchor** — Restate FR-3 + ESL + 0628 inherit at **footer** of output (lost-in-the-middle mitigation).
7. **Middle re-read (FR-3)** — Primary attach >40k chars: verify quotes from start, middle, and end regions before Gate A PASS.

---

## Evidence grades

| Grade | Keep? | Criterion |
| ----- | ----- | --------- |
| STRONG | yes | Verbatim quote in primary + causal mechanism + operator-actionable craft + falsifier |
| MODERATE | yes if high value | Quote ok; thin mechanism or scope — flag in scope/limit |
| WEAK | no | No anchor, slogan, summary-only |
| WRONG / OVERSTATED / UNTESTED / ZOMBIE / HALLUCINATION-SUSPECTED | no | Kill register / §Dropped only |

**Rank:** skill-patch impact × evidence grade. Prefer fewer STRONG rows over many MODERATE rows.

---

## Gate A (primary source)

Every Q-ref must match attached primary or chapter slice **verbatim** (OCR uncertainty → note in scope/limit, downgrade to MODERATE). Mismatch → HALLUCINATION-SUSPECTED → drop from survivor sections.

Gate A is the **sole authority for craft moves extracted from the closed corpus**. Web search does not replace Gate A for quote-first craft extraction.

**Phase 3 digest (QC skipped):** Attached ingests were Gate A–verified at ingest. Treat ingest §4 Q-bank as primary anchor source for merge. Optional `*_ATTACH.txt` in the attach pack supports re-verification only — absence is **not** a blocker when ingest attestation confirms Gate A compliance.

---

## Supplemental web verification (refine + evidence digest)

**Scope:** ChatPRD synthesis stages only (`synth_refine_per_source.md`, `synth_corpus_evidence_digest.md`). **Not** ingest (primary-only FR-3) and **not** Piranesi export (Cursor export-only; see `/Users/dubs/Projects/piranesi.skill/SKILL.md`).

**When:** Load-bearing or STRONG claims where external confirmation would change keep/kill, grade, or resolve cross-source conflict on **external facts** (citations, stats, named methods, replication status).

**Bar (palamedes-aligned):**
- ≤5 independent web retrievals per window; log `RETRIEVAL-ORDER` before first `[T*-verified]` tag on a load-bearing claim.
- `read:body` minimum for magnitude/scope claims at L2+; abstract-only magnitude → `[priors-only]`.
- Falsifier per load-bearing claim: "what evidence would flip this?"
- Web confirms or falsifies facts **about** primary content — never imports new craft moves without a Gate A anchor.

**Provenance tag (web-confirmed survivors):** `source_slug · row_id · Q-ID · web URL · grade · read-depth`

**Kill:** Web-only claims with no Gate A anchor; first-read anchoring without independent second retrieval (palamedes FR-1).

---

## Semantic row (survivors)

`claim · mechanism · scope/limit · falsifier · lane · esl_preserve · provenance`

Lanes: `deai_removal` | `tic_enrichment` | `both` (split rationale on `both`).

---

## Ingest output schema (≤4500w)

```markdown
## 1) TL;DR (≤5 bullets — claim_id / move_id pointers only)
## 2) Coverage attestation
## 3) Gate A Q-bank (verbatim — FIRST)
## 4) Craft moves (ranked STRONG → MODERATE)
## 5) Skill incorporation (≥3 rows if borrowable)
## 6) Kill-list / dropped
## FOOTER — iron laws (repeat)
```

Papers: add §4b Claims register (C-001…) before craft moves.

---

## Stage-specific rules

| Stage | Preserve | May compress |
| ----- | -------- | ------------ |
| Refine | Q-bank, mechanism, scope, falsifier, kill audit | Ingest fluff, duplicate bullets |
| Evidence digest | Merged rows + dual quotes on conflict | Duplicate moves (keep richest anchor set) |
| Skill brief | move_id, patch intent, Q-ID pointers, ESL | Cross-source narrative |
| Cursor handoff | Tasks, paths, verify commands | Q-bank text (IDs remain) |

---

## Conflict & NEEDS_REVIEW

- Two sources disagree → **two quotes + two paths**; pick one with Gate A or mark `[unresolved]`.
- Attach truncation → NEEDS_REVIEW; cite full slice path on disk for operator.
- Never blend incompatible craft advice into one row.

---

## Iron laws (footer — repeat every output)

- FR-3: Gate A primary for craft extraction; ingest stays attached-primary-only
- Web: supplemental verification on refine/digest only (≤5/window; primary Q-ref + URL + grade)
- ESL: operator L1 Chinese — no native-norm polish; `[esl_preserve]`
- Detection: inherit `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md`
- Paths: full absolute under `/Users/dubs/Projects/`
- ChatPRD authors synthesis; Cursor implements from handoffs only

---

## Prompt index

| Stage | Path |
| ----- | ---- |
| Refine | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md` |
| Digest | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` |
| Skill brief | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` |
| Cursor handoff | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` |
| Pipeline | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md` |
