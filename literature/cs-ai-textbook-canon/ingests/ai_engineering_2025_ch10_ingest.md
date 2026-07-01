# Chapter ingest — `ai_engineering_2025` · Chapter 10

**Corpus:** cs-ai-textbook-canon · **Slug:** ai_engineering_2025 · **Wave:** w1_foundation  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch10_ingest.md`

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **parent_book_title** | AI Engineering |
| **authors** | Chip Huyen |
| **edition** | 1e (First Edition, December 2024 release) |
| **publisher** | O'Reilly Media |
| **ISBN_print** | 978-1-098-16630-4 [verified from text, line 116] |
| **ISBN_electronic** | 9781098166298 [from corpus_manifest.yaml] |
| **chapter_number** | 10 |
| **chapter_title** | AI Engineering Architecture and User Feedback |
| **page_range** | Not present in text export; logical span from `Chapter 10. AI Engineering Architecture and User Feedback` through `Summary` before Epilogue (21648) |

---

## scope

Chapter 10 is the **systems-integration capstone** of Huyen's AI-engineering framework: how to assemble prior techniques (RAG, guardrails, routing, caching, agents, observability, orchestration) into a production architecture, and how to design **user feedback** as both product signal and proprietary training data for the data flywheel (Ch. 8).

**Major arcs:**

1. **Progressive architecture** — start query→model→response; add context construction, guardrails, router/gateway, system caches, agent loops/write actions (Figs. 10-1 through 10-10).
2. **Monitoring & observability** — MTTD/MTTR/CFR; metrics/logs/traces; drift (prompt, user behavior, underlying model); evaluation↔monitoring loop.
3. **Pipeline orchestration** — component definition + chaining; parallel routing/PII; LangChain/LlamaIndex et al.; warning vs Airflow/Metaflow.
4. **User feedback** — explicit vs implicit; conversational NL feedback signals; when/how to collect; biases and degenerate feedback loops.

**Prerequisites cited:** Ch. 3 (semantic similarity), Ch. 4 (quality metrics), Ch. 5 (prompt attacks, defenses), Ch. 6 (RAG, agents, write actions), Ch. 8 (data flywheel), Ch. 9 (KV/prompt caching, inference latency).

**Out of scope (stated or implied):** full traditional observability treatise; tool-gateway pattern (noted as uncommon); executable production deployment; legal deep-dive on feedback consent.

**Slice boundary note:** Requested lines 19896–23108 include Epilogue, Index, and Colophon after chapter Summary (21645); ingest content stops at chapter-authored Summary + footnotes ¹–¹² (21600–21646).

---

## key_findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

### Framing

- Only user exposure validates whether an application achieves its goal (lines 19909–19911).
- User feedback is doubly critical for AI: product guidance **and** model-improvement data source; conversational UI eases giving feedback but complicates signal extraction (19911–19918).
- Architecture validated across multiple companies as general; individual apps may deviate (19926–19928).
- Component order is pedagogical, not mandatory (19958–19960).

### Progressive architecture (five steps + observability + orchestration)

| Step | Addition | Core idea |
|------|----------|-----------|
| 0 | Baseline | Query → Model API → response; no context/guardrails (19930–19940) |
| 1 | Context | RAG + tools = "feature engineering" for FMs; provider support varies (19967–19999) |
| 2 | Guardrails | Input (PII leak, bad prompts); output (quality + security failures); retry/parallel/human fallback (20001–20176) |
| 3 | Router + gateway | Intent routing; unified multi-vendor interface; access control, cost, fallback (20178–20348) |
| 4 | Caches | Exact + semantic system caching; leakage warning for personalized answers (20356–20468) |
| 5 | Agents | Loops, parallel/branching, write actions (email, orders, transfers) (20470–20504) |

**Context construction (Step 1):** Providers differ in document limits, retrieval algorithms, chunk sizes, tool types, parallel function execution, long-running jobs (19984–19993). Context construction ≈ feature engineering for foundation models (19977–19980).

**Guardrails (Step 2):**

- **Input risks:** employee pasting secrets; system-prompt internal data; tools retrieving private DB fields (20017–20029). Mitigate via sensitive-data detection (PII, faces, IP keywords); block or mask with reverse-PII map for unmasking in responses (20031–20056).
- **Output failures:** empty responses; malformatted JSON; hallucinations; bad quality; toxic/PII/remote-execution/brand-risk content (20067–20097). Track **false refusal rate** alongside security failures (20098–20102).
- **Retry policy:** probabilistic models → retry on empty/malformed; parallel duplicate calls trade cost for latency (20104–20117). Human transfer on phrases, sentiment anger, or turn-count loops (20119–20126).
- **Trade-offs:** latency vs reliability; streaming complicates output guardrails (20130–20143). Third-party APIs supply built-in guardrails; self-hosting reduces external-leak input needs (20145–20151).
- **OTS tools:** Purple Llama, NeMo Guardrails, PyRIT, Azure filters, Perspective API, OpenAI moderation (20160–20167).

**Router (Step 3):** Specialized/cheaper models per intent; out-of-scope stock declines; ambiguity clarification ("Freezing" example) (20183–20220). Next-action predictors for agents and memory hierarchy (20222–20231). Classifiers often GPT-2/BERT/Llama-7B or smaller scratch models—fast/cheap (20233–20238). Context truncation vs reroute when retrieval exceeds target model window (20240–20246). Routing often **before** retrieval; pattern: routing → retrieval → generation → scoring (20252–20258).

**Gateway (Step 3):** Unified wrapper (illustrative Flask/OpenAI+Gemini code, 20284–20315); centralized tokens; per-user/app model ACL; rate-limit/cost monitoring; fallback on API failure (20317–20331). Also load balancing, logging, analytics, caching, guardrails (20333–20336). Examples: Portkey, MLflow AI Gateway, Wealthsimple LLM Gateway, TrueFoundry, Kong, Cloudflare (20338–20341).

**Caching (Step 4):**

- **Exact:** reuse identical queries; embedding-search cache; multi-step/expensive actions benefit; LRU/LFU/FIFO eviction; classifier for cache-worthiness; avoid caching user-specific or time-sensitive queries (20367–20397).
- **Leakage warning:** membership-dependent return policy cached for wrong user (20401–20408).
- **Semantic:** embedding similarity threshold; higher hit rate but performance risk; components fragile; vector-search cost (20410–20458). Author: value "more dubious" than exact cache—evaluate before adopting (20442–20458).

**Agents (Step 5):** Response fed back for more retrieval (loop); write actions increase capability and risk (20487–20494). Complexity → more failure modes (20496–20500).

### Monitoring and observability

- Goal = evaluation goal: mitigate risks, discover opportunities (failures, attacks, drift, cost savings) (20518–20524).
- **DevOps trio:** MTTD, MTTR, CFR—high CFR implies pre-deploy evaluation gap (20526–20546). Evaluation metrics should translate to monitoring; monitoring issues feed evaluation pipeline (20540–20546).
- **Monitoring vs observability:** monitoring watches outputs without guaranteeing diagnosability; observability assumes internal state inferable from external outputs + instrumentation (20548–20569).
- **Metrics:** design around failure modes, not vanity scores (20573–20587). Format failures easiest; open-ended → factual consistency, conciseness, AI judges; safety/toxicity/refusal rates; conversational signals (stop-generation, turns, token lengths, output diversity) (20598–20631). Per-component metrics (RAG context relevance/precision; vector DB storage/query time) (20637–20641). Correlate to north-star (DAU, session duration, subscriptions) (20643–20650). Latency: TTFT, TPOT, total; per-user scaling (20652–20664). Costs: queries, token volumes, TPS, rate-limit headroom (20666–20670). Spot vs exhaustive checks; slice by user, release, prompt version, time (20672–20682).
- **Logs:** append-only events; log configs, prompts, queries, outputs, tools, timings, tags/IDs; "log everything" with AI log analysis (20684–20725). **Manual daily production inspection** changes developer perception of good/bad (Shankar et al. 2024) (20727–20733).
- **Traces:** link events into request timeline (LangSmith example, Fig. 10-11); pinpoint failure step (20735–20751).
- **Drift:** system-prompt changes (template/typo edits); user behavior adaptation (Google query framing, self-driving bullying, Liu et al. 2020); silent underlying model updates—Chen et al. 2023 GPT-4/3.5 Mar vs Jun benchmarks; Voiceflow 10% drop GPT-3.5-turbo-0301→1106 (20757–20797).

### AI pipeline orchestration

- **Components definition** + **chaining** (function composition): process query → retrieve → prompt → generate → evaluate → human route if bad (20801–20835).
- Orchestrator passes data, validates step I/O, alerts on mismatch (20837–20841).
- **≠ workflow orchestrator** (Airflow, Metaflow) (20843–20846). Parallelize independent steps (routing + PII removal) under latency pressure (20848–20851).
- Tools: LangChain, LlamaIndex, Flowise, Langflow, Haystack; many RAG/agent frameworks double as orchestrators (20853–20856).
- **Start without orchestrator**—external tools add abstraction/debug cost (20858–20862). Evaluate: integration/extensibility, complex pipelines (branch/parallel/errors), ease/performance/scale; avoid hidden API calls (20864–20895).

### User feedback

- Dual role: evaluate performance + inform development; proprietary data = competitive advantage; enables Ch. 8 flywheel (20897–20911). Early launch → data moat (20909–20911). Privacy/consent obligations (20913–20916). Open-source deploys hinder feedback collection (footnote ⁷).

**Explicit vs implicit:**

- Explicit: thumbs, stars, "did we solve your problem?"—standard, sparse, biased (20920–20926, 21157–21162).
- Implicit: inferred from actions; FM apps expand genres (20928–20933). Conversational UI blends feedback into dialogue (20935–20940).

**Uses:** evaluation metrics, model development/training, personalization (20966–20973).

**Natural language feedback signals:**

| Signal | Interpretation |
|--------|----------------|
| Early termination | User stops generation, exits, says stop, leaves agent hanging | 21001–21007 |
| Error correction | "No…", "I meant…", rephrasing | 21009–21021 |
| Action correction | "Bill is suspect not victim"; agent nudges ("check GitHub") | 21023–21033 |
| Confirmation requests | "Are you sure?", "Check again"—detail/trust gap | 21035–21040 |
| User edits | Strong wrong signal; preference pair (losing=original, winning=edited) | 21042–21052 |
| Complaints | Wrong/irrelevant/toxic/lengthy—Table 10-1 FITS clusters (Xu 2022; Yuan 2023) | 21054–21082 |
| Sentiment | Frustration without explicit reason; call-center voice loudness analogy | 21084–21093 |
| Model refusals | High refusal rate → unhappy users | 21095–21098 |

**Other conversational feedback:** regeneration (satisfaction vs options vs consistency check; usage-billing weakens idle regenerate); post-regen comparative prompts (Fig. 10-13); delete/rename/share/bookmark; turn count (positive for companions, negative for support); dialogue diversity vs loop detection (21105–21155).

**Explicit vs implicit tradeoff:** explicit easier to interpret, sparse, biased; implicit abundant, noisy—contextualize (e.g., share can be mistake-showcase or useful) (21157–21171). Combine signals (rephrase after share) (21173–21177).

### Feedback design

**When to collect:**

- **Onboarding:** calibration (face ID, voice wake word, skill level)—optional where not required (21195–21207).
- **On failure:** downvote, regenerate, model switch; conversational corrections; human handoff; inpainting as human–AI collaboration (DALL-E example) (21209–21234).
- **Low confidence:** side-by-side summaries; partial vs full display (Gemini)—reliability unsettled (footnote ¹⁰) (21236–21263). Google Photos "same person?" confirmation (21265–21272).
- **On success:** thumbs up/share—Apple HIG warns against soliciting positive feedback; some PMs want enthusiastic positive signals for feature focus; sample 1% to limit clutter/bias (21274–21298).

**How to collect:**

- Integrate into workflow; easy to ignore; incentives (21300–21305).
- **Midjourney:** 4 images → upscale (strong +), variations (weak +), regenerate (none good) (21307–21324).
- **Copilot:** gray draft, Tab accept vs keep typing reject (21330–21337).
- **Standalone chatbots** lack downstream outcome signal (email actually sent) vs integrated Gmail (21339–21345).
- Feedback needs **5–10 turn context** for root-cause analysis; consent/terms/donation flows (21347–21362). Explain use (personalize vs aggregate vs train) (21364–21368).
- Don't ask impossible comparisons (stats preference vote); add "I don't know" (21371–21376). Tooltips; avoid ambiguous UI (Luma angry-emoji placement bug) (21382–21400).
- **Public vs private feedback** affects candor vs discoverability (X private likes 2024) (21402–21413).

### Feedback limitations

| Bias | Mechanism | Mitigation hints |
|------|-----------|------------------|
| Leniency | Avoid conflict/extra work; Uber 4.8 avg, <4.6 risk | Distribution analysis; descriptive labels vs 1–5 stars | 21428–21465 |
| Randomness | Side-by-side fatigue | — | 21467–21474 |
| Position | First option clicked more | Randomize positions; position-aware success model | 21476–21487 |
| Preference | Length bias; recency in comparisons | — | 21489–21496 |

**Degenerate feedback loop:** feedback only on shown items; predictions influence feedback influence model—exposure/popularity bias, filter bubbles (21502–21521). Cat-photo amplification (or racism/sexism/explicit content) (21523–21530). RLHF-style training → **sycophancy**—models tell users what they want vs what's accurate (Stray 2023; Sharma et al. 2023) `[contested mechanism, verified citation]` (21532–21538). Understand limitations before incorporating feedback (21540–21543).

### Summary (chapter-authored)

- Two parts: integrative architecture + conversational feedback design (21547–21581).
- Component boundaries fluid; each addition adds capability/safety/speed but complexity and failure modes (21559–21568).
- FM observability extends traditional ML/software practices (21571–21575).
- Feedback design increasingly engineering responsibility—AI engineering closer to product (Ch. 1 theme) via flywheel and UX (21583–21591).
- Many AI challenges are **system problems** requiring whole-system view (21593–21598).

---

## coverage_attestation

| Check | Status |
|-------|--------|
| **Source file** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ai_engineering_2025.txt` |
| **Lines read** | 19896–21646 (chapter body + Summary footnotes); 21648–23108 scanned as Epilogue/Index/Colophon (out of chapter scope) |
| **Chapter boundary** | Starts `Chapter 10. AI Engineering Architecture and User Feedback` (19896); ends before `Epilogue` (21648) |
| **Wrong-file flag** | `false` |
| **Sections in slice** | Intro · AI Engineering Architecture (Steps 1–5) · Monitoring and Observability · AI Pipeline Orchestration · User Feedback (extracting, design, limitations) · Summary · footnotes ¹–¹² |
| **Deferred** | Figure placeholders; gateway code is illustrative non-functional; Epilogue/Index |
| **Cross-chapter refs cited, not re-ingested** | Ch. 1, 3, 4, 5, 6, 8, 9; *Designing Machine Learning Systems* monitoring chapter |
| **Tables in slice** | 10-1 (FITS feedback clusters) |
| **Figures referenced** | 10-1 through 10-21 (not rendered in text export) |

---

## pedagogy

### learning_objectives

After this chapter, a reader should be able to:

1. Sketch the **five-step progressive architecture** from bare Model API to agents with write actions.
2. Place **guardrails** (input PII, output quality/security) and explain retry, parallel, and human-fallback policies.
3. Design an **intent router** and **model gateway** for multi-model cost, ACL, and fallback.
4. Compare **exact vs semantic caching** and articulate personalization leakage risks.
5. Define **observability** metrics (MTTD/MTTR/CFR), logging, tracing, and drift classes for FM apps.
6. Contrast **AI pipeline orchestrators** with general workflow engines and list adoption criteria.
7. Extract **conversational feedback signals** (NL + behavioral) for eval, training, and personalization.
8. Design **when/how** to collect feedback without harming UX; name major **feedback biases** and degenerate loops.

### worked_examples_present

**Y** — Conceptual walkthroughs + one code sketch:

| Example | Lines (approx.) | Role |
|---------|-----------------|------|
| Simplest query→model architecture | 19930–19940 | Baseline |
| PII mask/unmask with reverse map | 20048–20056 | Input guardrail |
| Customer-support intent routing | 20196–20220 | Router |
| "Freezing" ambiguity clarification | 20216–20220 | Router |
| Melbourne memory vs search routing | 20227–20231 | Next-action router |
| Flask gateway OpenAI+Gemini sketch | 20284–20315 | Gateway pattern |
| Ecommerce return-policy cache leak | 20401–20408 | Exact-cache warning |
| Vietnam capital semantic cache | 20412–20437 | Semantic cache |
| Agent retrieval loop | 20476–20485 | Step 5 |
| Australia hotel preference dialogue | 20942–20964 | Implicit NL feedback |
| FITS complaint clusters (Table 10-1) | 21059–21076 | Complaint taxonomy |
| Midjourney 4-up feedback UI | 21307–21324 | Feedback design |
| Copilot accept/reject typing | 21330–21337 | Implicit feedback |
| Video recommender exposure bias | 21513–21521 | Degenerate loop |
| Cat-photo feedback amplification | 21523–21530 | Degenerate loop |

### exercise_hooks

- **In-chapter exercises:** **N** — no end-of-chapter problem set.
- **Operator drill ideas `[inferred]`:**
  - Draw architecture diagram for your product at Steps 0–5; mark which components you already have.
  - Draft input/output guardrail checklist from Ch. 4–5 failure modes; set false-refusal alert threshold.
  - Spec router intents for a support bot; define out-of-scope stock responses.
  - Write cache eligibility rules; red-team personalized-query leakage scenario.
  - Define 10 monitoring metrics tied to one north-star; map eval pipeline metrics 1:1.
  - Instrument a trace schema (query, retrieval, prompt, model, tools, latency, cost).
  - Catalog implicit feedback signals available in your UI; pair each with confirmation signal.
  - Design Midjourney-style implicit feedback for your generative feature.
  - Bias audit: simulate position/leniency effects on A/B preference UI.

---

## Operator hooks

### 1. Foundation layer

Chapter 10 is the **w1_foundation systems capstone**—integrates prior chapters into deployable architecture and closes the loop to Ch. 8 data flywheel via user feedback.

**Upstream (assumed read):**

- **Ch. 4–6** — evaluation criteria, defenses, RAG/agents/write actions.
- **Ch. 8** — proprietary data flywheel fed by feedback.
- **Ch. 9** — KV/prompt caching, TTFT/TPOT latency vocabulary.

**Downstream / adjacent:**

- **hands_on_llms_2024** — procedural complement for gateway/orchestrator implementation.
- **Huyen, Designing ML Systems (2022)** — traditional monitoring chapter (footnote ⁵).

Prerequisite stack: evaluation (Ch. 4) → prompting/security (Ch. 5) → RAG/agents (Ch. 6) → data (Ch. 8) → inference (Ch. 9) → **architecture + feedback (Ch. 10)**.

### 2. MDCalc alignment

**[high relevance]** — Clinical and regulated-AI deployments mirror several chapter patterns:

- **Guardrails:** PHI input masking before external APIs; output toxicity/PII; false refusal vs blocked legitimate clinical queries.
- **Human fallback:** escalation when sentiment/turn-count thresholds hit—maps to clinical escalation pathways.
- **Observability:** drift on silent model API updates—critical for validated clinical AI; CFR tied to change control.
- **Feedback:** conversational correction ("you meant creatinine not glucose") as implicit signal; consent for training on clinician edits.
- **Caching warning:** patient-specific answers must not serve other patients—direct parallel to membership-dependent ecommerce leak.
- **Write actions:** order/transfer analogs (prescription, lab order) demand highest guardrail tier.

Pair with NAM/gen-AI health canon for consent governance; not a substitute for clinical validation frameworks.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **ai_engineering_2025 Ch. 5** | High | Prompt attacks, defenses → guardrail placement |
| **ai_engineering_2025 Ch. 6** | High | Context, agents, write actions |
| **ai_engineering_2025 Ch. 8** | High | Feedback → flywheel data |
| **ai_engineering_2025 Ch. 9** | Medium | Inference caching vs system caching |
| **ai_engineering_2025 Ch. 4** | Medium | Metrics, evaluation↔monitoring |
| **hands_on_llms_2024** | Medium | Orchestrator tutorials |
| **Huyen, Designing ML Systems** | Medium | Monitoring fundamentals |
| **prompt_engineering_llms_2024** | Low | Security overlap only |

**Dedup guidance:** Treat **five-step architecture progression**, **routing→retrieval→generation→scoring pattern**, and **degenerate feedback loop** warnings as canonical; cross-link rather than re-derive in product runbooks.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — progressive architecture, multiple product UI references |
| Exercise hooks | **Weak in-chapter** — operator drills required |
| Chapter boundary | **Clean** — book-closing integrative chapter |
| Citation density | **Medium-high** — Shankar, Chen, Liu, Xu, Sharma, Stray; many product anecdotes |
| Anchor density | **High** for architecture steps; figures degraded in export |
| Complement need | **Conditional** — pair with Hands-On LLMs + org-specific observability stack |

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 1e, ©2025, Dec 2024 release; ≤5 years |
| **Author authority** | **PASS** | Chip Huyen; O'Reilly; production AI engineering pedigree |
| **Primary-source citation density** | **PASS** | Shankar et al. 2024; Chen et al. 2023; Liu et al. 2020; Xu et al. 2022 FITS; Sharma et al. 2023; RL/NLP feedback literature (Fu, Goyal, Zhou & Small, Sumers; Alexa/Spotify/Yahoo voice) |
| **Contested claims flagged** | **PASS** | Semantic cache "dubious" value; guardrails vs latency tradeoff (footnote ³); partial vs full side-by-side feedback unsettled (¹⁰); Uber rating labels "not validated" (¹²); sycophancy from feedback training (Stray/Sharma); orchestrator "start without one" vs vendor platform creep (⁶) |
| **Worked examples (procedural chapter)** | **PASS** | Stepwise architecture build; gateway sketch; extensive feedback UI case studies |

**Overall TEXTBOOK-Q1:** **PASS** — suitable foundation-track capstone ingest; operator should treat vendor product anecdotes (ChatGPT, Gemini, Midjourney, Voiceflow) as illustrative and re-verify model-version drift claims against current API release notes.

---

## Provenance anchors (sample)

| claim-id | claim | relation | section-anchor | text lines |
|----------|-------|----------|----------------|------------|
| AIE-C10-001 | Progressive architecture: context → guardrails → router/gateway → cache → agents | compressed | AI Engineering Architecture | 19942–19956 |
| AIE-C10-002 | Context construction = feature engineering for FMs | quoted | Step 1 | 19977–19980 |
| AIE-C10-003 | PII mask + reverse map for external API calls | compressed | Input guardrails | 20048–20056 |
| AIE-C10-004 | Track false refusal rate with security failures | compressed | Output guardrails | 20098–20102 |
| AIE-C10-005 | Routing→retrieval→generation→scoring common pattern | compressed | Router | 20252–20258 |
| AIE-C10-006 | Personalized cache can leak across users | compressed | Exact caching Warning | 20401–20408 |
| AIE-C10-007 | Semantic cache value more dubious; threshold trial-and-error | compressed | Semantic caching | 20442–20458 |
| AIE-C10-008 | MTTD, MTTR, CFR observability trio | compressed | Monitoring | 20526–20538 |
| AIE-C10-009 | Evaluation metrics should map to monitoring metrics | compressed | Monitoring | 20540–20546 |
| AIE-C10-010 | Silent API model updates—Chen 2023 GPT-4 drift | compressed | Drift detection | 20786–20795 |
| AIE-C10-011 | Start without orchestrator; abstraction hides debug detail | compressed | Orchestration | 20858–20862 |
| AIE-C10-012 | User edits → preference pair for alignment | compressed | Error correction | 21047–21052 |
| AIE-C10-013 | FITS eight complaint clusters (Table 10-1) | compressed | Complaints | 21059–21076 |
| AIE-C10-014 | Degenerate feedback loop / exposure bias | compressed | Feedback Limitations | 21502–21521 |
| AIE-C10-015 | Feedback training → sycophancy (Sharma 2023) | compressed | Degenerate feedback loop | 21534–21538 |
| AIE-C10-016 | AI engineering closer to product via flywheel + UX | compressed | Summary | 21583–21591 |

---

## Recap bullets (chapter-authored)

- Integrative architecture framework; exact layout varies by app (21551–21557).
- Component separation fluid; overlap expected (e.g., guardrails in gateway) (21559–21563).
- Each component trades capability/safety/speed for complexity (21565–21568).
- Observability essential; FMs need new metrics beyond traditional ML (21567–21575).
- Conversational feedback enables analytics, improvement, flywheel (21577–21581).
- Engineers increasingly own feedback design for model data needs (21583–21588).
- System-level thinking required for real AI problems (21593–21598).

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
