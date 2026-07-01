# Chapter ingest — `ai_engineering_2025` · Chapter 4

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | AI Engineering |
| **authors** | Chip Huyen |
| **edition** | 1st Edition (2025) |
| **ISBN_print** | 978-1-098-16629-8 |
| **ISBN_electronic** | 978-1-098-16630-4 |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 4 |
| **chapter_title** | Evaluate AI Systems |
| **page_range** | Printed page numbers absent from text export; logical span Ch. 4 opening through Summary + footnotes ¹–²⁹ |
| **parent_book_title** | AI Engineering |

## Scope

Chapter 4 is the book's **evaluation spine** for production generative-AI applications. It opens with **evaluation-driven development (EDD)**—define how an application will be judged before building—and argues evaluation is the **biggest bottleneck to AI adoption**. The chapter organizes criteria into four buckets: **domain-specific capability**, **generation capability**, **instruction-following capability**, and **cost/latency**.

Part one surveys **how to measure** each bucket. Domain capabilities use exact evaluation (functional correctness for code, MCQ accuracy for knowledge/reasoning, efficiency metrics like BIRD-SQL runtime). Generation capabilities trace NLG heritage (fluency, coherence, faithfulness) but center on **factual consistency** (local vs global; entailment/NLI scorers; AI judges; SelfCheckGPT; SAFE search-augmented verification) and **safety/toxicity** (moderation taxonomies, specialized classifiers, RealToxicityPrompts, BOLD, political-bias studies). Instruction-following covers IFEval (25 auto-verifiable format constraints) and INFOBench (broader content/style constraints with yes/no criteria + GPT-4 judges), plus **roleplaying** evaluation (RoleLLM, CharacterEval). Cost/latency introduces Pareto tradeoffs, token/API vs self-host economics, and Table 4-3-style selection matrices.

Part two covers **model selection**: hard vs soft attributes, a four-step workflow (filter → public signals → private experiments → production monitoring), and an extended **build-vs-buy** analysis (open weight vs open model licenses; seven axes—privacy, lineage/copyright, performance, functionality, cost, control, on-device). It then navigates **public benchmarks and leaderboards** (lm-evaluation-harness, HELM vs Hugging Face Open LLM Leaderboard composition, correlation/saturation, averaging vs mean win rate), **model drift** (Chen et al. GPT-3.5/4 benchmark shifts), and **data contamination** (Schaeffer satire; n-gram overlap vs perplexity detection; intentional post-training contamination).

Part three prescribes **designing a custom evaluation pipeline** for open-ended tasks: evaluate end-to-end and per-component outputs; turn-based vs task-based evaluation (twenty_questions example); write unambiguous rubrics with positive/negative scope; tie metrics to business outcomes; mix cheap classifiers with expensive AI judges and logprobs; slice data (Simpson's paradox); bootstrap sample-size reliability; meta-evaluate the pipeline (signal, reproducibility, metric correlation, cost/latency); iterate with experiment tracking.

**Sections ingested:** Evaluation Criteria (EDD, domain-specific, generation/factual consistency/safety, instruction-following/roleplaying, cost-latency) · Model Selection (workflow, build vs buy, public benchmarks/leaderboards/contamination) · Design Your Evaluation Pipeline (Steps 1–3 + iterate) · Summary · footnotes ¹–²⁹.

Cross-refs: Ch. 3 (automatic evaluation methods), Ch. 5 (prompt engineering, safety hardening), Ch. 6 (RAG eval, context retrieval), Ch. 7–9 (finetuning, inference optimization), Ch. 8 (annotation/synthetic data), Ch. 10 (monitoring, user feedback).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Evaluation-driven development and criteria buckets (opening)

- Deployed applications with no evaluation are worse than undeployed ones—maintenance cost without knowing if value is delivered. [verified from text, lines 7257–7273]
- **Evaluation-driven development**: define evaluation criteria before building; analogous to test-driven development. [verified from text, lines 7275–7281]
- Common production apps have clear metrics: recommender engagement, fraud dollars saved, code functional correctness, close-ended classification tasks. [verified from text, lines 7288–7304]
- Focusing only on measurable outcomes is like searching under the lamppost—may miss high-value unevaluable applications. [verified from text, lines 7306–7311]
- Author's thesis: **evaluation is the biggest bottleneck to AI adoption**; reliable pipelines unlock new applications. [verified from text, lines 7313–7315]
- Four criteria buckets: domain-specific capability, generation capability, instruction-following, cost/latency—with legal-contract summarization as unifying example. [verified from text, lines 7317–7330]

### Domain-specific capability

- Capabilities constrained by architecture, size, and training data; models lacking required training (e.g., Latin) won't work. [verified from text, lines 7338–7346]
- Thousands of public benchmarks; coding uses functional correctness (Ch. 3); efficiency measurable via runtime/memory (BIRD-SQL example). [verified from text, lines 7348–7369]
- Code readability lacks exact metrics—subjective/AI-judge evaluation. [verified from text, lines 7371–7375]
- Non-coding domains often use MCQs; 75% of Eleuther harness tasks MCQ-based (MMLU, AGIEval, ARC-C) as of April 2024. [verified from text, lines 7377–7391]
- MCQ sensitivity: extra spaces or "Choices:" phrasing can flip answers (Alzahrani et al., 2024). [verified from text, lines 7430–7436]
- MCQs test classification/knowledge/reasoning, not open-ended generation—poor fit for summarization/translation/essays. `[contested in chapter]` [verified from text, lines 7438–7447]

### Generation capability, factual consistency, safety

- NLG metrics (fluency, coherence, faithfulness/relevance) persist but fluency/coherence less critical for strong models; still useful for weak models, creative writing, low-resource languages. [verified from text, lines 7451–7482]
- **Hallucination** undesirable for factual tasks; **factual consistency** and **safety** (toxicity, bias umbrella) are primary new concerns. [verified from text, lines 7484–7491]
- **Local** factual consistency: output vs provided context (RAG, summarization, support bots). **Global**: vs open knowledge (general chat, fact-checking). [verified from text, lines 7512–7538]
- Hardest step is determining trusted facts; models weight relevance over scientific tone (Wan et al., 2024). [verified from text, lines 7550–7568]
- Tip: benchmark should overweight query types where model hallucinates (niche knowledge; questions about nonexistent statements). [verified from text, lines 7572–7588]
- AI-as-judge for consistency; SelfCheckGPT (multi-sample disagreement); SAFE (decompose → self-contain → search → verify). [verified from text, lines 7593–7650]
- Textual entailment (entailment/contradiction/neutral) frames consistency; specialized NLI scorers (e.g., DeBERTa-v3-base-mnli-fever-anli). [verified from text, lines 7652–7682]
- TruthfulQA: 817 misconception-prone questions, 38 categories; GPT-judge finetuned predictor ~90–96% human agreement (Lin et al., 2022). [verified from text, lines 7684–7690]

### Instruction-following, roleplaying, cost/latency

- Poor instruction-following breaks structured outputs (JSON/regex) even when domain capability exists (sentiment → HAPPY/ANGRY). [verified from text, lines 7825–7837]
- Conflation warning: failure on lục bát poem could be domain or instruction failure. [verified from text, lines 7848–7853]
- **IFEval**: 25 auto-verifiable instruction types (keywords, length, JSON, bullets, etc.); score = fraction followed. [verified from text, lines 7871–7905]
- **INFOBench**: broader content/style constraints; yes/no criteria per instruction; GPT-4 reasonable automatic verifier vs AMT. [verified from text, lines 7907–7943]
- Tip: curate **your own** instruction benchmark (YAML output, ban "As a language model", etc.). [verified from text, lines 7953–7959]
- Roleplaying: 8th most common LMSYS use case; hard to automate—RoleLLM, CharacterEval; evaluate style + knowledge + negative knowledge. [verified from text, lines 7961–8001]
- Cost/latency: Pareto optimization; filter by hard latency ceiling first; metrics include TTFT, time per token/query; API token pricing vs self-host fixed cluster amortization; popular 7B/65B sizes match GPU memory tiers. [verified from text, lines 8028–8084]
- Table 4-3 exemplar matrix: cost/TPM/latency/HumanEval/pass@1/internal hallucination score/Elo. [verified from text, lines 8086–8116]

### Model selection workflow and build vs buy

- Goal: best model **for your application**, revisited across prompt engineering and finetuning iterations. [verified from text, lines 8126–8137]
- Two-step selection pattern: best achievable performance → cost–performance mapping. [verified from text, lines 8139–8145]
- **Hard attributes** (license, privacy, model size) vs **soft** (accuracy, toxicity—improvable); latency hard if API-hosted, soft if self-hosted optimizable. [verified from text, lines 8152–8174]
- Four-step workflow (Fig. 4-5): filter hard constraints → public benchmarks/leaderboards → private eval pipeline → production monitoring (iterative). [verified from text, lines 8176–8204]
- **Open weight** vs **open model** (training data public); author uses "open source" loosely for all public-weight models. [verified from text, lines 8226–8251]
- License checklist: commercial use, MAU restrictions (Llama 700M), synthetic-data/distillation permissions. [verified from text, lines 8271–8290]
- Seven build-vs-buy axes with Table 4-4 pros/cons: privacy (Samsung ChatGPT leak), lineage/IP uncertainty, performance gap `[contested in chapter]` (author doubts open source will match strongest proprietary incentives), functionality (function calling, logprobs, finetuning access), API vs engineering cost, control/transparency (Convai finetuning example), on-device. [verified from text, lines 8353–8657]

### Public benchmarks, leaderboards, contamination

- Thousands of benchmarks; lm-evaluation-harness 400+; OpenAI evals ~500. [verified from text, lines 8666–8678]
- Leaderboard limits: compute constraints (HELM Lite dropped MS MARCO; HF dropped HumanEval initially); small benchmark sets (HF 4→6→revamped 2024 with MATH lvl 5, MMLU-PRO, GPQA, MuSR, BBH, IFEval). [verified from text, lines 8703–8819]
- Benchmark correlation matters—ARC-C/MMLU/WinoGrande strongly correlated; TruthfulQA moderately independent (Table 4-5). [verified from text, lines 8791–8836]
- HF averages scores equally; HELM uses mean win rate across scenarios. [verified from text, lines 8842–8854]
- Custom private leaderboards should weight benchmarks to application (coding agent → code benchmarks). [verified from text, lines 8864–8876]
- **Model drift**: Chen et al. (2023) significant GPT-3.5/4 benchmark shifts Mar–Jun 2023; perception may reflect eval difficulty not intentional degradation. `[contested in chapter]` [verified from text, lines 8878–8896]
- HELM full eval ~$80K–$100K for 30 models. [verified from text, lines 8902–8905]
- **Data contamination**: training on test data inflates scores; Schaeffer 1M-param near-perfect via benchmark-only training; unintentional web scrape inclusion common. [verified from text, lines 8922–8948]
- Intentional contamination for user-facing quality also occurs post-selection. [verified from text, lines 8956–8964]
- Detection: n-gram overlap (accurate, needs training data) vs perplexity (cheaper, less accurate); GPT-3 had 13 benchmarks ≥40% in training (Brown et al., 2020). [verified from text, lines 8973–9019]
- Public benchmarks filter bad models but won't find best for your app. [verified from text, lines 9031–9035]

### Custom evaluation pipeline design

- **Step 1**: Evaluate end-to-end and each component; per-turn vs per-task (task more important but boundary-ambiguous); twenty_questions BIG-bench as task eval example. [verified from text, lines 9048–9117]
- **Step 2**: Unambiguous guidelines defining what app should and **shouldn't** do; LinkedIn Job Assessment—correct but unhelpful "terrible fit" response; LangChain 2.3 feedback types average; rubrics with scored examples validated by humans; map eval metrics to business automation %; usefulness thresholds. [verified from text, lines 9120–9213]
- **Step 3**: Mix methods per criterion (classifier + AI judge + logprobs confidence); human eval as North Star (LinkedIn ~500 daily conversations); production vs experiment data differences; slice-based eval (bias debug, Simpson's paradox Table 4-6); multiple eval sets (production distribution, failure modes, typos, out-of-scope); bootstrap for set size reliability; OpenAI sample-size rule (~10/100/1K/10K for 30%/10%/3%/1% deltas at 95% confidence, Table 4-7). [verified from text, lines 9227–9414]
- Meta-evaluate pipeline: right signals, reproducibility (temperature 0 for judges), metric correlation, cost/latency of eval itself; iterate with experiment tracking. [verified from text, lines 9416–9470]
- Summary thesis: no perfect low-dimensional score for high-dimensional systems, but combining methods mitigates limitations; dedicated eval discussion ends here but recurs (Ch. 6 retrieval/agents, 7/9 cost, 8 data quality, 10 user feedback). [verified from text, lines 9472–9523]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ai_engineering_2025.txt` |
| **Lines read** | 7222–9671 (inclusive) |
| **Chapter boundary** | Starts `Chapter 4. Evaluate AI Systems` (L7222); ends before `Chapter 5. Prompt Engineering` (L9672) |
| **Wrong-file flag** | `false` — slug matches `ai_engineering_2025` |
| **Sections deferred** | Ch. 3 eval-method detail (referenced not re-ingested); Ch. 5+ forward refs only |
| **Figures** | Figs. 4-1–4-10, Tables 4-1–4-7 referenced; image data `[]` or alt-text placeholders only in export |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L69–116 and corpus manifest |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Articulate **evaluation-driven development** and enumerate the four evaluation criteria buckets for a concrete application.
2. Choose **exact vs subjective** metrics for domain, generation, and instruction-following tasks; explain MCQ limitations for generative evaluation.
3. Distinguish **local vs global** factual consistency and describe AI-judge, entailment, SelfCheckGPT, and SAFE verification patterns.
4. Apply **IFEval/INFOBench** lessons to build a custom instruction-following benchmark for production schemas.
5. Execute the **four-step model selection workflow** and decide API vs self-host using the seven-axis framework.
6. Critique **public leaderboards** (coverage, correlation, saturation, contamination) and justify a private benchmark set.
7. Design a **multi-level evaluation pipeline** with rubrics, slicing, sample-size reasoning, and meta-evaluation of the eval system itself.

### worked_examples_present

**Y** — Multiple worked scenarios, tables, and prompts:

| Example | Section | Role |
|---------|---------|------|
| Legal contract summarization criteria | Evaluation Criteria | Four-bucket mapping |
| MMLU sample MCQ | Domain-specific | MCQ format |
| TruthfulQA category table | Factual consistency | Benchmark illustration |
| Liu et al. factual-consistency judge prompt | Factual consistency | AI-judge template |
| SAFE four-step verification | Factual consistency | Search-augmented eval |
| Entailment Mary/fruits | Factual consistency | NLI framing |
| IFEval instruction types (Table 4-2) | Instruction-following | Auto-verifiable constraints |
| INFOBench hotel questionnaire criteria | Instruction-following | Yes/no rubric |
| RoleLLM judge prompt excerpt | Roleplaying | AI-judge structure |
| Fictional selection matrix (Table 4-3) | Cost/latency | Model gate example |
| Resume PDF two-step extraction | Eval pipeline Step 1 | Component eval |
| twenty_questions dialog | Eval pipeline Step 1 | Task-based eval |
| LinkedIn Job Assessment | Eval pipeline Step 2 | Good vs correct |
| Simpson's paradox surgery table | Eval pipeline Step 3 | Slice aggregation trap |
| Bootstrap / OpenAI sample-size table | Eval pipeline Step 3 | Statistical confidence |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Draft EDD criteria doc for a RAG support bot before writing prompts; include out-of-scope behavior.
  - Build a 50-example private benchmark with slices (short/long queries, typos, OOS); bootstrap variance check.
  - Reproduce Table 4-5-style correlation analysis on two public benchmarks relevant to your domain.
  - Red-team: argue for and against author's claim that strongest open models will lag proprietary models.
  - Map three evaluation metrics to hypothetical business automation thresholds for a customer-support use case.
  - Compare HF averaging vs HELM mean win rate on the same three models for your weighted criteria.

## Operator hooks

### 1. Foundation layer

Chapter 4 is the **w1_foundation evaluation canon** for *AI Engineering*—the operational bridge from Ch. 3's automatic eval mechanics to Ch. 5 prompt engineering and Ch. 6 RAG/agent evaluation. It establishes vocabulary the rest of the book assumes: EDD, criteria buckets, private vs public benchmarks, contamination skepticism, and pipeline design. For the cs-ai-textbook-canon stack, this chapter is **prerequisite** before **hands_on_llms_2024** (tooling tutorials) and complements **designing_ml_systems_2022** slice-based eval (explicitly cross-cited). It supersedes shallow "pick the highest MMLU model" guidance and should be indexed before any production agent/eval runbook. Pairs with **philosophy_software_design_2e_2021** Ch. 15 (spec-before-code) and Ch. 4 (deep interfaces) at the pattern level—evaluation rubrics as informal contracts.

### 2. MDCalc alignment

**[moderate]** — Directly applicable to regulated/clinical-adjacent AI engineering without clinical claims:

- **Eval-before-build**: Define factual-consistency and safety criteria before deploying LLM features touching user-facing medical information; local consistency against retrieved policy/context mirrors RAG patterns in Ch. 6.
- **Private benchmarks over public leaderboards**: MMLU/bar-exam scores `[peripheral]` for clinical utility; contamination and MCQ/generation gap mean **custom eval sets** with slice analysis (demographics, query length, OOS) are load-bearing.
- **Build vs buy**: Data-privacy axis (Samsung-style leak) and lineage/IP concerns map to enterprise health deployments; author notes some enterprises trust hyperscaler-hosted APIs over startups.
- **Human eval North Star**: LinkedIn 500-conversation manual review pattern portable to high-stakes QA sampling—not a substitute for clinical validation.
- **No employer-stack claims**; no LangSmith/Langfuse-specific APIs cited.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **designing_ml_systems_2022** | High | Slice-based eval, Simpson's paradox—Huyen cites own O'Reilly title; dedup by pointing to DMS for ML-system slicing depth, AIE Ch. 4 for LLM/foundation-model eval |
| **hands_on_llms_2024** | Medium | Tutorial complement for implementing judges/harnesses; AIE Ch. 4 is framework not notebook |
| **responsible_ai_practice_2025** | Low–medium | Safety/toxicity taxonomy overlap; RAP likely deeper on fairness governance |
| **llmops_aryan_2025** | Low | Production ops angle; Ch. 4 eval pipeline design is upstream |
| **philosophy_software_design_2e_2021** | Low | Rubric-as-interface; EDD ≈ test-first design metaphor |
| **grokking_algorithms_2e_2024** | None | — |

**Dedup guidance:** Treat **ai_engineering_2025 Ch. 4** as canonical for **EDD + private eval pipeline + leaderboard skepticism** in SYNTHESIS; reference Ch. 3 ingest for metric implementation detail rather than duplicating perplexity/logprob mechanics here.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — tables, prompts, multi-step pipelines, build-vs-buy matrix |
| Exercise hooks | **Weak in text** — no printed exercises; hooks require operator labs |
| Chapter boundary quality | **Clean** — three-part arc with Summary; footnotes belong to chapter |
| Ingest suitability | **High** — dense, citation-backed, contested opinions preserved (open vs proprietary, MCQ validity, model drift) |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | Published 2025 (O'Reilly); copyright L69; session Jun 2025—current for generative-AI engineering |
| **Author authority** | **PASS** | Chip Huyen—practitioner/educator; endorsements from OpenAI/enterprise practitioners in front matter; textbook from O'Reilly |
| **Primary-source citation density** | **PASS** | Heavy citations: Liu/Luo/Lin (factual eval), Zhou (IFEval), Qin (INFOBench), Wei (SAFE), Chen (drift), Brown (contamination), Balázs Galambosi correlation, industry anecdotes with named studies |
| **Contested claims flagged** | **PASS** | MCQ vs generation gap, open-source ever catching proprietary best, OpenAI drift explanations, leaderboard selection opacity—all preserved not smoothed |
| **Worked examples (procedural/conceptual)** | **PASS** | Pipeline steps, rubric design, benchmark tables, SAFE/self-check workflows |

**Overall TEXTBOOK-Q1:** **PASS** — core foundation-track ingest; operator should treat specific benchmark names (HF 2023 six-pack vs 2024 revamp) as **illustrative** and re-verify against current leaderboards.

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| AIE-C04-001 | Evaluation is the biggest bottleneck to AI adoption | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Evaluation-Driven Development |
| AIE-C04-002 | Define evaluation criteria before building (EDD) | quoted | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Evaluation-Driven Development |
| AIE-C04-003 | MCQs test classification not open-ended generation quality | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Domain-Specific Capability |
| AIE-C04-004 | Local vs global factual consistency distinction | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Factual consistency |
| AIE-C04-005 | Four-step model selection workflow (filter → public → private → monitor) | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Model Selection Workflow |
| AIE-C04-006 | Public benchmark contamination undermines leaderboard trust | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Data contamination |
| AIE-C04-007 | Evaluate each component and end-to-end; task-based > turn-based importance | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Design pipeline Step 1 |
| AIE-C04-008 | Correct response ≠ good response (LinkedIn Job Assessment) | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Evaluation guideline |
| AIE-C04-009 | OpenAI sample-size rule: 3× smaller delta → ~10× more examples | compressed | AI Engineering 1e | ISBN 978-1-098-16629-8 | literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch04_ingest.md | Step 3 sample size |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
