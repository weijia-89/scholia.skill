# ai_engineering_2025 — Chapter 05 ingest

| Field | Value |
|-------|-------|
| slug | ai_engineering_2025 |
| chapter_number | 5 |
| chapter_title | Prompt Engineering |
| parent_book_title | AI Engineering |
| authors | Huyen, Chip |
| edition | 1e (2025) |
| ISBN_print | 9781098166298 (manifest) |
| ISBN_electronic | not stated in chapter slice |
| publisher | O'Reilly |
| source_type | textbook_chapter |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ai_engineering_2025.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch05_ingest.md |
| text_lines_read | 9672–11401 (chapter body; Ch 6 opener at L11402 excluded) |
| page_range | not recoverable from text export (no page stamps in slice) |

---

## Scope

Chapter 5 treats **prompt engineering** as the craft of instructions that elicit desired model behavior **without weight updates** — the default, lowest-cost adaptation path before finetuning. The chapter is bipartite: (A) **constructive** prompt design (anatomy, in-context learning, system/user splits, context-length economics, best practices, tooling, versioning) and (B) **defensive** prompt engineering against extraction, jailbreaking/injection, and training-data or context leakage.

Subsections in slice: Introduction · Introduction to Prompting · In-Context Learning (zero-/few-shot; prompt vs context terminology) · System Prompt and User Prompt (chat templates) · Context Length and Context Efficiency (NIAH, RULER) · Prompt Engineering Best Practices (clarity, persona, examples, output format, context, decomposition, CoT/self-critique, iteration, tools, organization/versioning) · Defensive Prompt Engineering (attack taxonomy, reverse engineering, jailbreak families, indirect injection, information extraction, defenses at model/prompt/system levels) · Summary.

Explicit bridge to **Chapter 6** (RAG/agents for context construction) and callbacks to Ch 2–4 (instruction-following eval, self-eval, brand risk).

---

## Key findings

All items `[verified from text]` unless tagged `[inferred]`.

1. **Definition and positioning.** Prompt engineering = crafting instructions for desired outcomes; easiest/common adaptation; does not change weights. Strong base models enable many apps with prompting alone — exhaust prompting before finetuning. (L9674–9682)

2. **Rigor claim.** Should be run like ML experiments: systematic experimentation, evaluation, tracking — not mere word-fiddling. OpenAI research-manager quote: skill is real; problem is when it is the *only* skill — production needs stats, engineering, classic ML for eval and data curation. (L9694–9705)

3. **Prompt anatomy.** Components: task description (role + output format), example(s), concrete task. Requires model instruction-following capability (Ch 4). (L9713–9749)

4. **Robustness to perturbation.** Small changes (digits vs words, newlines, capitalization) may flip outputs on weak models; robustness correlates with overall capability; stronger models reduce fiddling. Tip: task description placement — GPT-4 favors beginning; Llama 3 favors end. (L9751–9771)

5. **In-context learning (ICL).** Brown et al. 2020 (GPT-3): behavior from prompt examples without weight updates; enables continual incorporation of new facts (e.g. updated JS docs). Each example = a **shot**; zero-shot vs few-shot. More examples help until context/cost limits; GPT-4 era: Microsoft 2023 analysis found limited few-shot gains vs zero-shot on general tasks, but domain-specific gaps (e.g. Ibis API) still benefit. (L9773–9820)

6. **Terminology.** Book convention: **prompt** = whole model input; **context** = information supplied to perform the task (not interchangeable with PALM 2 “context” = task description). Chollet metaphor: foundation model as library of programs; prompt engineering activates the right program. (L9822–9855)

7. **System vs user prompt.** System ≈ task description/role; user ≈ concrete task + uploaded material. APIs concatenate via model-specific **chat templates** (Llama 2 `[INST]`/`<<SYS>>`; Llama 3 header tokens). Wrong template → silent performance failures; verify final serialized prompt. System-first ordering and post-training **instruction hierarchy** (Wallace et al. 2024) may explain system-prompt lift. (L9857–9976)

8. **Context length race.** GPT generations 1K→4K; industry expansion to Gemini 1.5 Pro ~2M (Fig 5-2); book ~160K tokens. Not all prompt positions equal — **lost in the middle** (Liu et al. 2023); **needle-in-a-haystack** and **RULER** (Hsieh et al. 2024) for long-context evaluation. (L9978–10034)

9. **Clear explicit instructions.** Disambiguate scoring rubrics, refusal behavior, integer vs fractional scores; revise when observing failure modes. (L10063–10079)

10. **Persona.** Shifts perspective (essay scoring as first-grade teacher vs default). (L10081–10093)

11. **Examples reduce ambiguity.** Santa/tooth-fairy child-bot table; prefer token-efficient example formats when performance equal (38 vs 27 tokens, Table 5-2). (L10095–10148)

12. **Output format control.** Conciseness, no preambles, explicit JSON keys; **markers** delimit input end for classification (Table 5-3). (L10150–10186)

13. **Sufficient context / hallucination mitigation.** Provide corpus or tools for **context construction** (RAG, web search — Ch 6). Restricting answers to context-only is hard: instructions + quoting help but no guarantee; finetuning still leaks; safest = train only on permitted corpus (often infeasible). (L10188–10226)

14. **Task decomposition.** Chain sub-prompts (intent classification → intent-specific response); benefits: monitoring, debugging, parallelization, simpler prompts; costs: latency, multi-query spend (often cheaper models for easy steps). GoDaddy 2024: 1,500-token monolith → decomposed prompts improved performance and cut tokens. (L10228–10350)

15. **Chain-of-thought (CoT).** Wei et al. 2022; “think step by step” / specified steps / one-shot CoT examples (Table 5-4); LinkedIn reports reduced hallucinations; latency/cost tradeoff. **Self-critique** links to Ch 3 self-eval. (L10352–10432)

16. **Systematic iteration.** Version prompts; experiment tracking; standardized eval data/metrics; evaluate whole system not isolated subtasks. (L10434–10458)

17. **Prompt optimization tools.** OpenPrompt, **DSPy** (autoML-like); AI-written prompts (Claude 3.5 example); **Promptbreeder**, **TextGrad**; structured-output helpers (Guidance, Outlines, Instructor). Hidden API call explosion risk (e.g. 30 evals × 10 variants = 300 calls); tool template bugs (LangChain critique typos, Fig 5-9). Author bias: start manual; “show me the prompt” (Hamel Husain). (L10460–10546)

18. **Prompt organization.** Separate `prompts.py` from code; Pydantic `Prompt` metadata; `.prompt` formats (Firebase Dotprompt, Humanloop, etc.); git versioning vs **prompt catalog** with explicit versions and dependency tracking. (L10548–10649)

19. **Attack taxonomy.** (1) prompt extraction, (2) jailbreaking/prompt injection, (3) information extraction. Risks: RCE/tool abuse, data leaks, social harm, misinformation, service subversion, brand (Google rocks 2024, Tay 2016). (L10651–10719)

20. **Reverse prompt engineering.** Deduce system prompts from outputs or “ignore above…” tricks; extracted prompts may be hallucinated; proprietary prompts are maintenance liabilities, not durable moats. Context (e.g. location) also extractable (Brex guide, Fig 5-10). (L10724–10777)

21. **Jailbreaking vs injection.** Jailbreak = subvert safety; injection = malicious instructions in user/tool path (e.g. order DB + “delete entry”). Book collapses both under **jailbreaking** label. Attacks succeed because models follow instructions; better instruction-following increases attack surface. (L10783–10821)

22. **Manual jailbreak families (mostly legacy).** Obfuscation/typos/Unicode; special-character suffixes (Zou et al. 2023); format hiding (poem about hotwiring); **DAN**, **grandma exploit**, roleplay/simulation modes. (L10829–10886)

23. **Automated attacks.** Zou et al. substring search; **PAIR** (Chao et al. 2023) attacker LLM loop, often <20 queries (Fig 5-11). (L10888–10915)

24. **Indirect prompt injection.** Payloads in tools/RAG/email/web/GitHub; passive vs active; Wallace et al. 2024 email-forward example; SQL-via-natural-language username attack (“Bruce Remove All Data Lee”). (Greshake et al. 2023 cited). (L10917–10977)

25. **Training-data extraction.** LAMA/Petroni 2019 probing; Carlini/Huang memorization extraction needs context; **Nasr et al. 2023** divergence via “repeat poem forever” ~1% memorization rate estimate, scales with model size; diffusion extraction (Carlini et al. 2023, Stable Diffusion). PII filters; fill-in-the-blank blocks (Claude Fig 5-15). (L10979–11079)

26. **Copyright regurgitation.** HELM-style verbatim continuation tests: long verbatim uncommon but noticeable on popular books; non-verbatim infringement hard to detect automatically. (L11081–11120)

27. **Defense benchmarks/tools.** AdvBench, PromptRobust; PyRIT, garak, llm-security, persuasive_jailbreaker; red teaming (Microsoft guide). Metrics: **violation rate** vs **false refusal rate**. (L11122–11151)

28. **Model-level defense.** Wallace et al. **instruction hierarchy**: system > user > model output > tool output; finetuning on aligned/misaligned pairs → up to ~63% robustness gain with minimal capability loss; handle borderline requests (locked out of home vs break-in). (L11153–11201)

29. **Prompt-level defense.** Explicit prohibitions; duplicate system prompt before/after user content; preempt DAN/grandma patterns; audit third-party templates (LangChain 100% injection success before hardening, Pedro et al. 2023). (L11203–11239)

30. **System-level defense.** VM isolation for code; human approval for destructive SQL; out-of-scope topic filters; intent classifiers; input/output guardrails; usage-pattern anomaly detection (Ch 10 guardrails). No foolproof security in high-stakes settings. (L11241–11281)

31. **Summary thesis.** Prompting = human–AI communication; instruction-following enables both utility and attacks; security cat-and-mouse; context construction deferred to Ch 6. (L11283–11317)

---

## Coverage attestation

| Section | In slice (L9672–11401) | Notes |
|---------|------------------------|-------|
| Chapter opener / framing | yes | Definition, rigor, OpenAI quote |
| Prompt anatomy & robustness | yes | Fig 5-1 placeholder |
| In-context learning | yes | Brown 2020, shots, Microsoft 2023 caveat |
| Prompt vs context terminology | yes | PALM 2, Discord discussion |
| System/user + chat templates | yes | Real-estate bot; Llama 2/3 templates |
| Context length & NIAH | yes | Fig 5-2–5-4 placeholders |
| Best practices (constructive) | yes | Tables 5-1–5-4 |
| Context-only restriction | yes | Skyrim roleplay example |
| Decomposition / CoT / tools / versioning | yes | GoDaddy, OpenAI support example |
| Defensive PE (full arc) | yes | Figs 5-7–5-16 placeholders |
| Summary + footnotes ¹–²² | yes | L11319–11400 |
| Chapter 6 opener | excluded | L11402+ |
| Figures/diagrams | placeholders only | `[A close-up…]` / `[]` in text export |

**wrong-file flag:** false — `Chapter 5. Prompt Engineering` at L9672; ends before `Chapter 6. RAG and Agents` at L11402.

**Deferred:** PDF page numbers; electronic ISBN; figure/chart content; hands-on exercises (chapter has no numbered exercises).

---

## Pedagogy

### learning_objectives

- Define prompt engineering and justify exhausting it before finetuning. `[verified from text]`
- Decompose a prompt into task description, examples, and task; relate to system/user APIs. `[verified from text]`
- Explain zero-shot vs few-shot in-context learning and when few-shot still matters. `[verified from text]`
- Apply chat-template hygiene and context-position awareness (NIAH). `[verified from text]`
- Implement constructive patterns: clarity, persona, token-efficient examples, markers, decomposition, CoT. `[verified from text]`
- Evaluate prompt tools and versioning strategies (git vs prompt catalog). `[verified from text]`
- Classify prompt attacks and map defenses to model, prompt, and system layers. `[verified from text]`
- Interpret violation rate vs false refusal rate for safety tuning. `[verified from text]`

### worked_examples_present

**Y** — NER prompt (Fig 5-1); real-estate disclosure system/user split; Llama 2/3 template serialization; Santa/tooth-fairy and edible/inedible classification tables; OpenAI two-step customer-support prompts; cats-vs-dogs CoT variants; `prompts.py` / Pydantic `Prompt` / Dotprompt; reverse-engineering transcript; email indirect-injection trace; instruction-hierarchy table; duplicated system-prompt defense.

### exercise_hooks

| ID | Archetype | Scholia hook |
|----|-----------|--------------|
| PE-5.1 | Template audit | Serialize a chat completion with wrong vs correct Llama 3 template; measure format adherence |
| PE-5.2 | NIAH probe | Insert private needle at start/mid/end of long context; score retrieval |
| PE-5.3 | Decomposition ROI | Monolith vs intent+response chain on support logs; token + accuracy |
| PE-5.4 | CoT ablation | Same task with zero-shot vs one-shot CoT; latency tradeoff |
| PE-5.5 | Tool bill guard | Count hidden API calls from a prompt optimizer on 10× eval set |
| PE-5.6 | Red-team pass | Run garak/PyRIT templates; report violation vs false-refusal rates |
| PE-5.7 | Prompt catalog | Version bump shared prompt; trace which apps pin old hash |

**Operator drill:** Implement system+user split for a domain bot; add Wallace-style hierarchy documentation; run PAIR-style manual attack on staging.

---

## Operator hooks

### 1. Foundation layer

Canonical **w1_foundation** spine for prompt craft before `prompt_engineering_llms_2024` (w2) and Hands-On LLMs tutorials. Prerequisite links: Ch 4 eval/instruction-following; Ch 3 self-critique; enables Ch 6 RAG/agents and Ch 10 guardrails.

### 2. MDCalc alignment

**Partial** — No clinical calculators or regulated deployment checklists. Portable patterns: context-only answering (clinical corpus grounding), decomposition for triage→specialist flows, violation/false-refusal metrics for safety guardrails, indirect injection awareness for email/RAG clinical assistants. `[inferred from text themes, not stated in slice]`

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| prompt_engineering_llms_2024 | **High** | Dedicated PE text in w2; AIE Ch 5 is framework + security breadth |
| hands_on_llms_2024 | Partial | AIE theory/ops; Hands-On code labs |
| responsible_ai_practice_2025 | Partial | Attack/defense overlap; AIE more implementation detail |
| kaestner_ml_production_2025 | Low | Experiment tracking echoes ML ops, not duplicated |
| gymbuddy / trainer skills | Meta | “Show me the prompt,” version prompts, resist tool magic |

**Wave note:** AIE Ch 5 is the **security-aware prompt spine** in w1 before w2 `prompt_engineering_llms_2024` depth.

### 4. Scholia fit

- **Worked examples:** Y (tables, code blocks, attack traces).
- **Exercise hooks:** Synthesized archetypes (no textbook-numbered exercises).
- **Chapter boundary quality:** Clean — opens with definition, closes summary + Ch 6 handoff; footnotes carry nuance without breaking body.

---

## TEXTBOOK-Q1 gate

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| Edition currency (≤5y unless classic) | **PASS** | 2025 O'Reilly 1e |
| Author authority (textbook tier) | **PASS** | Practitioner textbook; Huyen industry + teaching pedigree |
| Primary-source citation density | **PASS** | Dense: Brown, Wei, Liu, Wallace, Zou, Chao, Greshake, Carlini, Nasr, Pedro, etc. |
| Contested claims flagged | **PASS** (ingest duty) | See below |
| Worked examples (procedural chapter) | **PASS** | Many inline prompts and tables |

**Overall TEXTBOOK-Q1:** **PASS**

### Contested / simplified claims (not smoothed)

1. **Few-shot obsolescence on GPT-4.** Microsoft 2023 general-task result may understate domain-specific few-shot gains (author hedges with Ibis example, L9811–9820).

2. **System vs user semantic difference.** Concatenated equally at inference; performance lift attributed to position and post-training, not architectural privilege (L9961–9976).

3. **“Jailbreaking” umbrella.** Injection and jailbreak conflated by authorial choice (L10798–10801) — operators should keep taxonomy separate for threat modeling.

4. **Legacy attack effectiveness.** Manual tricks “no longer effective for most models” (L10827) — rapidly dated; indirect injection and automated attacks emphasized as durable.

5. **Memorization ~1%.** Nasr et al. estimate corpus-dependent; larger models memorize more (L11045–11051) — not universal production risk rate.

6. **Proprietary prompts as moat.** Author argues liability > advantage (L10779–10781) — contested in industry practice.

7. **High-stakes AI adoption timeline.** Footnote ²² analogizes slow internet adoption in high-stakes domains (L11399–11400) — speculative sociology, not empirical forecast.

8. **Figure 5-16 caption typo.** Text reads “tion hierarchy” (L11176) — export artifact.

---

## Anchor index (quick retrieval)

| Topic | Text lines |
|-------|------------|
| Chapter start | 9672 |
| Prompt definition / rigor | 9674–9705 |
| Prompt parts / robustness | 9713–9771 |
| In-context learning | 9773–9820 |
| Prompt vs context | 9822–9855 |
| System/user + templates | 9857–9976 |
| Context length / NIAH | 9978–10034 |
| Best practices start | 10040 |
| Clear instructions / persona / examples | 10063–10148 |
| Output markers | 10150–10186 |
| Context / restrict-to-context | 10188–10226 |
| Decomposition | 10228–10350 |
| CoT / self-critique | 10352–10432 |
| Iterate / tools | 10434–10546 |
| Versioning / catalog | 10548–10649 |
| Defensive intro / risks | 10651–10719 |
| Reverse engineering | 10724–10777 |
| Jailbreak families | 10783–10886 |
| PAIR / indirect injection | 10888–10977 |
| Data extraction / copyright | 10979–11120 |
| Defenses + hierarchy | 11122–11281 |
| Summary | 11283–11317 |
| Chapter end (footnotes) | 11319–11401 |

---

## Cross-chapter dependencies (from slice only)

- **Requires:** Ch 2 (LM does not separate user vs own generation, fn ⁸); Ch 3 (self-eval/self-critique); Ch 4 (instruction-following eval, brand risk fn ¹²); model capability/robustness themes.
- **Enables:** Ch 6 (context construction, RAG, agents, tools); Ch 10 (guardrails); agent/tool indirect injection references “Agents” chapter.

---

*Ingest generated from text slice L9672–11401. Word cap: ≤4500.*
