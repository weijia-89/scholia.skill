# Chapter ingest — `prompt_engineering_llms_2024` · Chapter 10

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Prompt Engineering for LLMs |
| **authors** | John Berryman, Albert Ziegler |
| **edition** | 1st Edition (2025 copyright; first release 2024-11-04 per revision history) |
| **ISBN_print** | 978-1-098-15615-2 |
| **ISBN_electronic** | 978-1-098-15615-2 (single ISBN in export; O'Reilly online edition) |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 10 |
| **chapter_title** | Evaluating LLM Applications |
| **page_range** | Printed page numbers absent from text export; logical span Ch. 10 opening through Conclusion (before Ch. 11) |
| **parent_book_title** | Prompt Engineering for LLMs |

## Scope

Chapter 10 is the book's **evaluation spine**, grounded in GitHub Copilot practice: eval code written first enabled fast iteration. Split: **offline** (lab, pre-ship) vs **online** (live users, higher stakes, higher validity).

**What Are We Even Testing?** Three targets: model, individual prompt/API pass, whole application loop (Ch. 4 loop). Prefer regression (whole loop) plus unit tests for critical passes; record latency/tokens always. Model swap → broad regression; prompt tweak → unit tests; architecture change → regression.

**Offline — Example Suites**: 5–20 inputs, script emitting prompt+completion files, git-diff eyeball review—not automated pass/fail; early value before metrics exist. PR summarization anecdote (terse/verbose/functionality paragraphs; fluff suppression from Ch. 7). Upgrade path (Figure 10-1 tech tree): need many examples + auto scoring. Multi-call loops: **canned conversations** (evaluate each pass independently) or **user mock** (profile-driven simulated user, whole-loop test with bias risk).

**Finding Samples**: (1) mine existing records (form summaries, Copilot open-source function-body reconstruction—approximate but infinite); (2) app telemetry (realistic but delayed, stale on app changes, consent burden, suggestion-contaminated "solutions"); (3) **synthetic** LLM generation (solution→problem or situation-only; combinatorial topic grids; same-model test bias warning).

**Evaluating Solutions** (easiest→hardest): **Gold standard** exact/partial match (yes/no counting; logprobs for binary—Ch. 7; partial metrics on critical aspects—smart home "I'm chilly" heating vs exact 77°F example; tool-call syntax partial match Figure 10-3); **functional testing** (parse validity, tool/type checks; Copilot unit-test pass on reimplemented functions); **LLM assessment** (not self-grading—third-party framing from Ch. 6 advice conversations; relative not absolute quality warning).

**SOMA Assessment**: **S**pecific questions, **O**rdinal scales (1–5 with rubric descriptions), **M**ulti-**A**spect coverage; intent vs execution split; RTC (relevance-truth-completeness) from Copilot chat scoring; break apart Goldilocks "just right" questions; ground in human inter-rater agreement (Kendall's Tau stability when adding model at T=0). Example 10-1 smart-home effectiveness rubric.

**Online Evaluation**: **A/B testing** (offline filter first; guardrail metrics; Optimizely/VWO/AB Tasty; client rollout lag). **Metrics** hierarchy: (1) direct feedback (thumbs, contrastive A/B—intrusive); (2) functional correctness; (3) user acceptance/click-through; (4) achieved impact; (5) incidental (latency, conversation length—ambiguous). Copilot finding: acceptance correlated with self-reported productivity more than impact proxies. Delayed feedback valuable for travel suggestions.

**Sections ingested:** What Are We Testing · Offline (suites, samples, solution eval, SOMA) · Online (A/B, metrics) · Conclusion.

Cross-refs: Ch. 4 (loop), Ch. 7 (logprobs, fluff), Ch. 6 (advice/third-party grading), Ch. 9 (task-level eval), **ai_engineering_2025 Ch. 4** (eval pair in canon).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Evaluation philosophy

- Copilot's first code was evaluation—enables directional change detection. [verified from text, lines 9376–9385]
- Offline = safe/scalable/pre-ship; online = valid but risky/bandwidth-limited. [verified from text, lines 9389–9405]
- Test whole loop first when choosing one harness; add critical unit tests. [verified from text, lines 9428–9474]

### Example suites and samples

- Example suites: systematic git-diff review before automated metrics. [verified from text, lines 9483–9536]
- Copilot eval mined function bodies from open source—approximate distribution. [verified from text, lines 9630–9647]
- Synthetic data: beware same-model generation bias in model comparisons. [verified from text, lines 9707–9712]

### Solution scoring

- Partial match must distinguish breaking vs benign divergence (smart home example). [verified from text, lines 9781–9816]
- Evaluate first decision likely to fail in token chain (tool choice before args). [verified from text, lines 9825–9842]
- LLM-as-judge: third-party framing; assessments relative not absolute. [verified from text, lines 9886–9911]

### SOMA and online

- SOMA: specific ordinal multi-aspect questions; intent vs execution. [verified from text, lines 9915–10004]
- Validate LLM judge against multi-human agreement stability. [verified from text, lines 10061–10073]
- Online: start with acceptance/impact metrics; use direct feedback if needed; guardrails on regressions. [verified from text, lines 10270–10279]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt` |
| **Lines read** | 9369–10309 (inclusive) |
| **Chapter boundary** | Starts `Chapter 10. Evaluating LLM Applications` (L9369); ends before `Chapter 11. Looking Ahead` (L10310) |
| **Wrong-file flag** | `false` |
| **Sections deferred** | Footnotes ¹–³ retained in chapter; RTC paper detail |
| **Figures** | Figs. 10-1–10-4, Example 10-1 |
| **Amnesiac rule** | Copilot anecdotes from chapter text |

## Pedagogy

### Learning objectives

1. Distinguish offline vs online evaluation and when each applies in the lifecycle.
2. Build an example suite and plan graduation to automated harnesses.
3. Source evaluation data from mining, telemetry, or synthesis with bias awareness.
4. Apply gold-standard, functional, and LLM-assessment scoring appropriately.
5. Design SOMA rubrics with ordinal multi-aspect coverage and human grounding.
6. Select online metrics (feedback, acceptance, impact, guardrails) for A/B tests.

### worked_examples_present

**Y** — PR summarization iteration, Copilot function-body mining, smart-home partial match, SOMA Example 10-1, tool-call eval Figure 10-3.

### exercise_hooks

- No printed exercises; **instructor hooks `[inferred]`:**
  - Build 10-example suite with git-diff workflow for a single prompt change.
  - Draft SOMA rubric for a tool-using agent task; calibrate against 3 human raters.
  - Map PE Ch. 10 offline tree to AIE Ch. 4 EDD buckets for one app.

## Operator hooks

### 1. Foundation layer

Ch. 10 is **w2_systems_llm eval canon** for PE—direct **eval pair** with **ai_engineering_2025 Ch. 4** (EDD, private benchmarks, pipeline design). PE emphasizes Copilot-first example suites, SOMA/RTC, and prompt-engineer-accessible partial metrics; AIE emphasizes production criteria buckets and leaderboard skepticism—index both, dedup in SYNTHESIS.

### 2. MDCalc alignment

**[moderate]** — Offline harness + human-grounded LLM judges before live clinical-adjacent features; slice/partial metrics echo regulated QA sampling—not a substitute for clinical validation.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **ai_engineering_2025 Ch. 4** | **High** | Canonical pair—PE: SOMA/example suites; AIE: EDD/leaderboards |
| **designing_ml_systems_2022** | Low–medium | Slice eval |
| **responsible_ai_practice_2025** | Low | Governance |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** |
| Exercise hooks | **Weak in text** |
| Chapter boundary | **Clean** |
| Ingest suitability | **High** — eval pair anchor |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2024–2025 Copilot-first practices |
| **Author authority** | **PASS** | Copilot eval architects |
| **Citation density** | **PASS** | Psychometrics footnote; RTC reference |
| **Contested claims** | **PASS** | LLM self-assessment limits explicit |
| **Worked examples** | **PASS** | SOMA template, partial-match walkthrough |

**Overall TEXTBOOK-Q1:** **PASS** — **eval pair** with `ai_engineering_2025_ch04_ingest.md`

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PE-C10-001 | Evaluation code preceded Copilot feature code | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch10_ingest.md | Opening |
| PE-C10-002 | Example suites enable pre-metric prompt iteration via diffs | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch10_ingest.md | Example Suites |
| PE-C10-003 | LLM assessment is relative quality; use third-party framing | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch10_ingest.md | LLM assessment |
| PE-C10-004 | SOMA: specific ordinal multi-aspect rubrics grounded in humans | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch10_ingest.md | SOMA Assessment |
| PE-C10-005 | Copilot acceptance correlated with user productivity reports | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch10_ingest.md | Metrics |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
