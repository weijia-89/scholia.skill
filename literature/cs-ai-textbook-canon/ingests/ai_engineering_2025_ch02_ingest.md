# Chapter ingest — AI Engineering (1e) · Chapter 2

| Field | Value |
|-------|-------|
| slug | ai_engineering_2025 |
| source_type | textbook |
| pdf_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/ai_engineering_2025.pdf |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ai_engineering_2025.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch02_ingest.md |
| text_lines_read | 2739–5260 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | AI Engineering |
| authors | Chip Huyen |
| edition | First Edition (December 2024) |
| ISBN_print | 978-1-098-16630-4 [verified from text, line 116] |
| ISBN_electronic | [not distinguished in text export; O'Reilly online editions noted at lines 76–78 without separate ISBN] |
| publisher | O'Reilly Media, Inc. |
| chapter_number | 2 |
| chapter_title | Understanding Foundation Models |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

**Manifest note:** `corpus_manifest.yaml` lists ISBN `9781098166298`; copyright page in text export shows `9781098166304`. Operator should reconcile before citation.

---

## Scope

Chapter 2 is the book's **foundation-model literacy** chapter: how training data, architecture, scale, post-training alignment, and **sampling** jointly determine what a ready-made model can do and how it behaves in production. Huyen explicitly scopes out competitive pre-training recipes (confidentiality, opacity) and nitty-gritty training mechanics in favor of **downstream-consequential design decisions**—language/domain coverage, transformer vs alternatives, Chinchilla-style compute budgeting, SFT/RLHF/DPO, and the probabilistic decode stack (temperature, top-k/p, test-time compute, structured outputs, inconsistency, hallucination). The chapter is **conceptual with technical depth** in the transformer and RLHF sections; it forward-references Ch. 3–9 (evaluation, prompting, memory, dataset engineering, finetuning, inference optimization). Operators building on Ch. 1's AI-vs-ML framing should treat Ch. 2 as prerequisite vocabulary for the rest of the canon spine.

---

## Key findings

1. **Training data as capability ceiling** (lines 2800–2863): Models inherit tasks present in training data; web-scale sources (Common Crawl, C4) dominate disclosed LLM corpora despite quality concerns (misinformation, bias). "Use what we have" yields strong generalists but weak fit for niche languages, domains, and tasks. Gunasekar et al. (2023): 7B high-quality coding tokens trained a 1.3B model beating larger baselines—quality can trump scale.

2. **Multilingual imbalance** (lines 2865–3017): English ~46% of Common Crawl (Lai et al., 2023); low-resource languages severely under-represented (Table 2-2 ratios up to 231×). GPT-4 MMLU and Project Euler math gaps correlate with representation but also linguistic/cultural structure. Translate-to-English pipelines lose information (e.g., Vietnamese kinship pronouns). Non-English costs: NewsGuard misinformation compliance asymmetry (Chinese vs English); tokenization inefficiency (Burmese median 72 tokens vs English 7 on MASSIVE → ~10× latency/cost). Many language-specific models exist (ChatGLM, PhoGPT, Jais, etc.).

3. **Domain-specific gaps** (lines 3019–3097): General models excel on domains present in web crawl (Fig. 2-3) but fail on tasks absent from public data (drug discovery, cancer screening). Examples: AlphaFold, BioNeMo, Med-PaLM2. Domain finetune on general base is common alternative to training from scratch.

4. **Transformer motivation** (lines 3110–3200): Replaces seq2seq RNN bottlenecks—attention over all input tokens (parallel prefill) vs single final hidden state; decode remains autoregressive. Prefill/decode split motivates Ch. 9 inference optimizations.

5. **Attention mechanics** (lines 3202–3273): Q/K/V dot-product attention; multi-head (Llama 2-7B: 4096 dim, 32 heads → 128 per head); context-length cost from growing K/V cache (Ch. 7, 9). Softmax attention formula present in text export.

6. **Transformer block anatomy** (lines 3274–3360): Attention + MLP (ReLU/GELU); embedding + positional encoding; unembedding head; scale driven by layers, model dim, FFN dim, vocab (Table 2-4 Llama 2/3 specs). Context length can exceed position indices via techniques noted but not detailed here.

7. **Architecture alternatives** (lines 3362–3436): RWKV (parallelized RNN); SSM lineage S4 → H3 → Mamba (linear-time inference, strong long-context claims) → Jamba hybrid (52B MoE, 256K context). New architectures must beat heavily optimized transformers at target scale/hardware; book argues adaptation techniques largely survive architecture shifts.

8. **Model size triad** (lines 3438–3617): Parameters (capacity, memory: 7B × 2 bytes ≈ 14 GB floor); training tokens (better metric than sample count for LLMs); FLOPs (training cost). MoE sparsity (Mixtral 8×7B: 46.7B total, 12.9B active/token). Under-training punishes large models; Llama token counts 1.4T → 2T → 15T; RedPajama-v2 30T tokens. FLOP vs FLOP/s vs FLOPs notation warning; GPT-3-175B ~$4.1M at illustrative H100 assumptions (70% util, $2/h).

9. **Inverse scaling & Chinchilla** (lines 3618–3730): Perez et al. (2022): more alignment can worsen preference alignment on some dimensions; Inverse Scaling Prize found limited real-world inverse scaling. **Chinchilla law** (DeepMind 2022): ~20× training tokens per parameter for compute-optimal dense pre-training; production tradeoffs favor smaller deployable models (Llama; Sardana et al. 2023 inference-aware scaling). Last-mile cost: 2% vs 3% error can require order-of-magnitude more data/compute.

10. **Scaling bottlenecks** (lines 3774–3862): Training data exhaustion (Villalobos et al. 2022/2024, Fig. 2-9); SEO/poisoning of future corpora; AI-on-AI training degradation (Shumailov et al. 2023, nuanced in Ch. 8); proprietary data as moat; C4 restrictions >28–45% (Longpre et al. 2024). Electricity: datacenters 1–2% global power → 4–20% by 2030 estimates; caps ~50× growth (~2 orders of magnitude).

11. **Post-training pipeline** (lines 3864–3946): Pre-training optimizes next-token (completion); post-training → conversation + safety. Two steps: **SFT** on demonstration (prompt, response) data; **preference finetuning** (RLHF, DPO, RLAIF). InstructGPT: 2% compute post-training vs 98% pre-training. Shoggoth meme (Fig. 2-11) as cultural shorthand.

12. **SFT economics** (lines 3948–4059): Completion vs conversation ("How to make pizza" ambiguity); InstructGPT labeler demographics (~90% college+, 1/3 master's); ~$10/pair × 13k ≈ $130k demonstration cost. LAION volunteer bias (90% male self-report). Gopher dialogue heuristics; synthetic data deferred to Ch. 8.

13. **Preference finetuning / RLHF** (lines 4061–4233): Universal human preference is contested. RLHF: train reward model on comparisons (pairwise > pointwise); InstructGPT ranking UI, ~73% inter-labeler agreement; Anthropic HH-RLHF example shows preference diversity. Loss on sigmoid(score_win − score_loss); PPO optimization. DPO adopted by Llama 3 for simplicity; Touvron et al. claim RLHF drives superior writing. **Best-of-N** without RL: Stitch Fix, Grab use RM to pick among samples.

14. **Sampling fundamentals** (lines 4235–4307): LM outputs logits → softmax → sample next token; greedy sampling boring for generation. Probabilistic outputs underpin inconsistency and hallucination.

15. **Sampling controls** (lines 4318–4487): **Temperature** reshapes distribution (T→0 ≈ argmax); **top-k** truncates vocab for cost/diversity; **top-p** (nucleus) dynamic cutoff; min-p variant; stop tokens vs max tokens (JSON truncation risk).

16. **Test-time compute** (lines 4488–4627): Best-of-N, beam search, diverse samples via varied hyperparameters. Selection: average logprob (OpenAI `best_of`), reward model/verifier (Cobbe et al. 2021: verifier ≈ 30× param boost), majority vote (Gemini MMLU 32 samples), parallel first-valid for latency. OpenAI verifier peak ~400 samples then degradation vs Stanford "Monkey Business" log-linear to 10k—production rarely samples hundreds. Snell et al. (2024): inference-time scaling can beat param scaling.

17. **Structured outputs** (lines 4628–4824): Semantic parsing (text-to-SQL, regex examples); downstream JSON for agents (Ch. 6). Layers: prompting → post-processing (LinkedIn YAML 90%→99.99%) → test-time retry → **constrained sampling** (grammar-filtered logits; latency cost) → finetuning / classifier head (feature-based transfer, Ch. 7). JSON mode guarantees syntax not semantics.

18. **Probabilistic failure modes** (lines 4825–5053): **Inconsistency**—same prompt variance (Fig. 2-23 essay scoring 3/5 vs 5/5); cache, fixed temperature/seed (not 100% guaranteed across hardware); prompt/memory mitigations (Ch. 5–6). **Hallucination**—two hypotheses: (1) Ortega et al. self-delusion / snowballing (Zhang et al. 2023); (2) Leo Gao / Schulman labeler–model knowledge mismatch during SFT. RLHF mixed evidence (InstructGPT Fig. 2-26: worse hallucination metric, preferred overall). Mitigations: truthfulness prompts, concision, verification/RL with source grounding; detection in Ch. 4.

19. **Chapter summary** (lines 5054–5109): Bridges to Ch. 3 evaluation as first systematic engineering step after understanding model behavior.

---

## Section digest (anchored)

### Opening (lines 2739–2799)

Positions chapter as **application-oriented model literacy** under opacity of frontier training. Four pillars: data distribution, architecture/size, post-training alignment, sampling. Explicit skip-ahead for familiar readers.

### Training Data → Multilingual → Domain (lines 2800–3098)

Narrative arc: data availability → quality tradeoffs → language/domain specialization. Tables 2-1–2-3 anchor quantitative claims. Figures 2-1–2-3 referenced; several figure bodies are `[alt text]` placeholders in export.

### Modeling — Architecture (lines 3099–3436)

Seq2seq → transformer pedagogical path (Fig. 2-4). Dense attention/block exposition with Llama sizing tables. Alternative architecture survey current to ~2024 (Mamba, Jamba). Technically skippable per author note.

### Modeling — Scale (lines 3438–3773)

MoE, token accounting, FLOP budgeting worked example, Chinchilla optimality, hyperparameter extrapolation for one-shot large runs, emergent abilities caveat (Wei et al. 2022).

### Scaling bottlenecks (lines 3774–3862)

Data wall, consent/forgetting open question, model collapse anxiety, licensing restrictions, energy ceiling—**contested forecasting** flagged.

### Post-Training (lines 3864–4233)

SFT demonstration taxonomy (Fig. 2-12 pie); RLHF reward-model math sketched; industry cost anecdotes ($3.50/comparison, $25/response). Controversial-topic alignment tension (boring vs upsetting users).

### Sampling (lines 4235–5053)

Largest section; author's stated favorite topic. Worked temperature example (logits [1,2]). Production patterns: structured output stack, test-time compute economics, hallucination theory survey. Customer-support stat: ~20% tickets on inconsistency (footnote ³⁷).

### Summary + footnotes (lines 5054–5260)

Recap; extensive footnotes carry citations, hardware notes, and editorial asides. Chapter boundary ends before line 5261 (`Chapter 3`).

---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Explain how training-data distribution limits language, domain, and task capability—and when finetuning vs from-scratch specialization applies.
2. Describe why transformers displaced seq2seq (attention, parallel prefill) and name at least one alternative architecture trajectory (RWKV, Mamba/Jamba).
3. Interpret model scale via parameters, training tokens, and FLOPs; apply Chinchilla's ~20× token-per-parameter rule of thumb at a high level.
4. Contrast pre-training, SFT, and preference finetuning goals and compute fractions (InstructGPT 98/2 split).
5. Configure and reason about temperature, top-k, top-p, and stopping conditions for latency vs creativity tradeoffs.
6. Compare structured-output techniques (prompt, post-process, constrained decode, finetune) by reliability and cost.
7. Distinguish inconsistency (sampling/hardware) from hallucination (training/objective hypotheses) and cite mitigation strategies deferred to later chapters.

### worked_examples_present

**Y** — Multiple narrative and numeric worked examples: attention Q/K/V walkthrough; Llama dimension tables; temperature softmax on logits [1,2]; GPT-3 training cost calculation; Chinchilla token/param pairing; InstructGPT demonstration rows (Table 2-6); RLHF comparison row (Table 2-7); text-to-regex GPT-4o prompts; logprob sequence product; LinkedIn YAML repair; essay-scoring inconsistency screenshot (Fig. 2-23); LLaVA milk hallucination (Fig. 2-24). Not a hands-on lab chapter—examples are explanatory, not executable notebooks.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derived hooks:

1. **Language audit:** For a target locale, estimate token multiplier vs English using the model provider's tokenizer; relate to API cost/latency budget.
2. **Chinchilla back-of-envelope:** Given a FLOP budget and param count, compute implied optimal training tokens; compare to a published model card.
3. **Sampling sweep:** Same prompt across temperatures {0, 0.7, 1.2}; classify outputs for consistency vs creativity; tie to product UX requirements.
4. **Structured-output ladder:** Implement prompting-only vs post-processing vs constrained decode for a fixed JSON schema; measure validity rate and p95 latency.
5. **Failure taxonomy:** Label production failures as data-gap, alignment-gap, sampling inconsistency, or hallucination using this chapter's frameworks.
6. **Best-of-N economics:** Model cost of N samples + selector (logprob vs RM) for a task with measurable success rate.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Chapter title + intro | Read | 2739–2799 |
| Training Data | Read | 2800–2863 |
| Multilingual Models | Read | 2865–3017 |
| Domain-Specific Models | Read | 3019–3097 |
| Modeling (overview) | Read | 3099–3109 |
| Model Architecture / Transformer | Read | 3110–3360 |
| Other model architectures | Read | 3362–3436 |
| Model Size | Read | 3438–3617 |
| Inverse Scaling | Read | 3618–3640 |
| Chinchilla / scaling law | Read | 3641–3730 |
| Scaling extrapolation | Read | 3731–3773 |
| Scaling bottlenecks | Read | 3774–3862 |
| Post-Training (overview) | Read | 3864–3946 |
| Supervised Finetuning | Read | 3948–4059 |
| Preference Finetuning / RLHF | Read | 4061–4233 |
| Sampling (all subsections) | Read | 4235–5053 |
| Summary | Read | 5054–5109 |
| Chapter footnotes | Read | 5111–5260 |
| Chapter 3+ | Deferred | 5261 onward |
| Figures 2-3, 2-5, 2-6, 2-7 | Partial | `[]` or alt-text only in export |
| Page numbers | Not in export | operator confirm via PDF |

**Attestation:** Single-file read of `ai_engineering_2025.txt` lines 2739–5260 only. Boundary: ends at footnote ³⁷ before `Chapter 3` at line 5261.

---

## Operator hooks

### 1. Foundation layer

Chapter 2 is the **w1_foundation spine** for everything downstream in *AI Engineering*: model selection (Ch. 3–4), prompting (Ch. 5), RAG/agents (Ch. 6–7), data engineering (Ch. 8), finetuning (Ch. 7), and inference (Ch. 9) all assume fluency in **data → architecture → scale → alignment → sampling**. For scholia canon, it pairs with **hands_on_llms_2024** (implementation tutorials) and supersedes shallow "what is an LLM" blog posts. Prerequisite: Ch. 1 AI-engineering definition; without Ch. 2, evaluation chapters read as disconnected checklists. Sampling and probabilistic-behavior material is **unique high-value** relative to **philosophy_software_design_2e_2021** and **grokking_algorithms_2e_2024**.

### 2. MDCalc alignment

**[core-adjacent]** — Not clinical-content specific, but directly relevant to **regulated / high-stakes AI deployment** patterns MDCalc-style stacks care about:

- **Multilingual + tokenization cost** → latency/SLO and non-English clinical UX.
- **Domain-specific models** → biomedicine examples (Med-PaLM2, BioNeMo) parallel specialty scoring tools.
- **Hallucination / inconsistency** → fatal for medico-legal outputs; chapter cites law-firm sanction (June 2023) and vaccine Q&A risk.
- **Structured outputs + constrained sampling** → tool/agent schemas, eval harnesses.
- **RLHF preference ambiguity** → safety-policy tuning for sensitive topics.

No MDCalc employer-stack claims; patterns are portable.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **hands_on_llms_2024** | High on transformer basics; AIE Ch. 2 adds scale laws, RLHF economics, sampling/production depth. Prefer AIE for engineering tradeoffs; Hands-On for code walkthroughs. |
| **grokking_algorithms_2e_2024** | Low; no shared algorithms pedagogy. |
| **philosophy_software_design_2e_2021** | Low; complexity/obviousness lenses apply to agent/tool interfaces only by analogy. |
| **ddia_2e_2026 / understanding_distributed_systems_2022** | Low–medium on scale/cost; AIE focuses model not data-system replication. |
| **prompt_engineering_llms_2024** | Medium on sampling/decoding; AIE broader (training + alignment + test-time compute). |

**Net:** Do not skip—canonical **foundation-model systems** chapter for Track B rank-1 title.

### 4. Scholia fit

- **Worked examples:** Y — sufficient for conceptual + numeric literacy; tag **conditional** for operators wanting runnable labs (defer to Hands-On LLMs).
- **Exercise hooks:** Absent in source; six hooks above are operator-derived.
- **Chapter boundary quality:** **Clean** — self-contained with Summary; heavy forward refs to Ch. 3–9 are explicit, not synthesized.
- **Export gaps:** Multiple figures/table graphics lost (`[]`); ISBN manifest mismatch; page numbers absent.
- **Complement flag:** Per manifest `ingest_note`, procedural depth on transformer implementation may need **hands_on_llms_2024** in parallel.

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency (≤5y unless classic) | **PASS** | 1e Dec 2024; current at ingest 2026-06-25. Frontier model names will age; frameworks (Chinchilla, RLHF) remain durable. |
| Author authority (textbook tier) | **PASS** | Chip Huyen—Stanford/snorkel lineage, production ML/AI engineering practitioner; O'Reilly textbook with peer praise (Metz, swyx, etc.). |
| Primary-source citation density | **PASS** | Heavy inline citations: Vaswani et al. 2017, Brown et al. 2020, Touvron et al. 2023, DeepMind Chinchilla 2022, Ouyang/InstructGPT, Villalobos, Shumailov, Cobbe verifiers, Snell test-time compute, etc. Tables attribute Lai et al., Washington Post, OpenAI. |
| Contested claims flagged | **PASS** | Flagged: Common Crawl quality vs ubiquity; translate-to-English adequacy; NewsGuard Chinese misinformation asymmetry (author offers speculative footnote); inverse scaling prize null results; RLHF vs hallucination (Fig. 2-26 contradiction); data-exhaustion projections; AI-on-AI collapse (nuanced Ch. 8); Schulman "models know what they know"; test-time compute scaling limits in production; temperature 0 non-literality. |
| Worked examples (procedural chapters) | **PASS** | Mixed conceptual/procedural; sampling and cost arithmetic are actionable without code. Meets bar for foundation chapter. |

**TEXTBOOK-Q1 verdict:** **PASS** — suitable foundation-track ingest; operator should refresh model-card numbers (Llama 3+, provider APIs) and reconcile ISBN before hard citations.

---

## Cross-references (forward pointers in text)

| Reference | Topic |
|-----------|-------|
| Chapter 1 | Self-supervision, backprop pointer |
| Chapter 3–4 | Evaluation methodology, hallucination metrics |
| Chapter 4–5 | Instruction-following, prompting clarity |
| Chapter 5–6 | Prompt/memory mitigations for inconsistency |
| Chapter 6 | Agentic structured outputs, tools |
| Chapter 7 | Finetuning, memory, FLOP formats, classifier heads |
| Chapter 8 | Dataset quality, synthesis, AI-generated training data |
| Chapter 9 | Inference optimization, prefill/decode, utilization |

---

## Provenance notes

- Claims `[verified from text]` trace to lines 2739–5260 of `ai_engineering_2025.txt`.
- ISBN from line 116; manifest ISBN conflict noted above.
- `[inferred]` used for MDCalc tagging, canon redundancy judgments, and scholia complement recommendations—not stated in chapter text.
- Figure placeholders (`[]`, alt-text-only) in export: operator should verify visuals in PDF before teaching from diagrams.

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Foundation model | Large pre-trained model adaptable to many downstream tasks |
| Common Crawl / C4 | Web crawl corpora; C4 is Google's cleaned subset |
| Low-resource language | Language with limited representation in training data |
| Transformer | Attention-based architecture; parallel prefill, autoregressive decode |
| Prefill / decode | Input processing vs sequential token generation at inference |
| Chinchilla scaling law | ~20× training tokens per parameter for compute-optimal dense training |
| MoE | Mixture-of-experts; subset of experts active per token |
| SFT | Supervised finetuning on (prompt, response) demonstrations |
| RLHF | Reward model from comparisons + RL (e.g., PPO) to maximize reward |
| DPO | Direct Preference Optimization; simpler alternative to RLHF |
| Sampling | Stochastic choice of next token from probability distribution |
| Temperature | Logit scaling before softmax; controls creativity vs determinism |
| Top-k / top-p | Truncate candidate tokens for efficiency or contextual appropriateness |
| Test-time compute | Extra inference work (multiple samples, beam search) for quality |
| Structured outputs | Machine-parseable formats (JSON, SQL, regex) |
| Constrained sampling | Filter logits to grammar-valid tokens during generation |
| Hallucination | Output not grounded in facts; distinct from sampling randomness |
| Inconsistency | Variable outputs for same/similar prompts |
