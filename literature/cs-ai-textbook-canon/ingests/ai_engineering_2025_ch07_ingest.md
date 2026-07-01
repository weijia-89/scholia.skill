# Chapter ingest — `ai_engineering_2025` · Chapter 7

**Corpus:** cs-ai-textbook-canon · **Slug:** ai_engineering_2025 · **Wave:** w1_foundation  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch07_ingest.md`

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **parent_book_title** | AI Engineering |
| **authors** | Chip Huyen |
| **edition** | 1e (First Edition, 2025) |
| **publisher** | O'Reilly Media |
| **ISBN_print** | 978-1-098-16630-4 [verified from text, line 116] |
| **ISBN_electronic** | 9781098166298 [corpus manifest; errata URL cites 9781098166304] |
| **chapter_number** | 7 |
| **chapter_title** | Finetuning |
| **page_range** | Not present in text export; logical span `Chapter 7. Finetuning` (line 13787) through `Summary` + footnotes before Ch. 8 (line 16188) |

---

## scope

Chapter 7 is the **weight-adaptation spine** of Huyen's AI-engineering framework: when and why to finetune versus prompting and RAG, the memory economics of training at foundation-model scale, parameter-efficient finetuning (PEFT) with deep coverage of LoRA and QLoRA, experimental model merging for multi-task and on-device deployment, and practical finetuning tactics (frameworks, hyperparameters).

**Major arcs within assigned slice (lines 13787–16187):**

1. **Finetuning overview** — transfer learning history; continued pre-training, supervised finetuning, preference finetuning, long-context finetuning; Code Llama pipeline (Fig 7-1); model developer vs application developer roles.
2. **When to finetune** — reasons for/against; task-specific degradation (alignment tax); domain-specific skepticism (BloombergGPT vs GPT-4); token-cost vs prompt caching; **finetuning is for form, RAG is for facts**; Ovadia et al. (2024) MMLU/current-events tables; 5-step adaptation workflow (Fig 7-3).
3. **Memory bottlenecks** — backprop trainable parameters; inference vs training memory formulas; activation dominance (Korthikanti et al.); numerical formats (FP32/16, BF16, TF32, INT8/4); quantization (PTQ, QAT, mixed precision); BitNet b1.58.
4. **Finetuning techniques** — full vs partial vs PEFT; Houlsby adapters; LoRA mechanics, intrinsic dimension, rank/config, multi-LoRA serving; QLoRA/NF4/Guanaco Elo table.
5. **Model merging** — vs ensembling; multi-task finetuning (simultaneous, sequential forgetting, parallel merge); summing (linear combo, task vectors, SLERP, TIES/DARE pruning); layer stacking/frankenmerging/MoE upcycling/SOLAR depthwise scaling; LoRA concatenation caveat.
6. **Finetuning tactics** — OpenAI progression vs distillation paths; framework/API landscape; hyperparameters (LR, batch size, epochs, prompt loss weight).

Author flags chapter as **most technically challenging to read**; memory-math section skippable with key-takeaways box (lines 13831–13835, 14359–14394). ML training basics deferred to external resources (GitHub pointers).

**Prerequisites cited:** Ch. 2 (finetuning types, semantic parsing), Ch. 4 (eval pipeline), Ch. 5–6 (prompting, RAG), Ch. 8 (instruction data, distillation data synthesis), Ch. 9 (inference, KV cache, prompt caching).

**Manifest note:** Framework spine — pair with **Hands-On LLMs** for executable LoRA/QLoRA paths.

---

## key_findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

### Framing: finetuning vs prompting

- Finetuning adapts models by **adjusting weights**; prompting adapts via instructions, context, tools (lines 13789–13793).
- Primary uses: domain capability, safety, **instruction-following and output format** (JSON/YAML) (lines 13795–13799).
- Higher memory footprint than prompting; PEFT dominant for accessibility (lines 13808–13821).
- Finetuning sits in **model training** territory; ML basics required (lines 13823–13829).

### Transfer learning and finetuning taxonomy

- Transfer learning (Bozinovski & Fulgosi 1976); Johnson et al. (2016) multilingual translation; LLM pre-training → specialized tasks with fewer examples (lines 13845–13873).
- InstructGPT view: finetuning **unlocks** latent capabilities (lines 13876–13879).
- Feature-based transfer (embedding + classifier head) common in vision; finetuning is weight-update transfer (lines 13881–13894).
- **Continued pre-training** on domain raw text before expensive supervised data (lines 13909–13916).
- Supervised finetuning on (input, output); preference finetuning on (instruction, winner, loser); long-context finetuning needs positional embedding changes, may hurt short sequences (lines 13932–13955).
- Application developers usually finetune **post-trained** models, not raw pre-trained (lines 13974–13978).

### When to finetune — decision framework

| Signal | Recommendation |
|--------|----------------|
| Missing/outdated facts | RAG first |
| Wrong format, style, relevance, syntax | Finetuning |
| Both | RAG first, then finetune if needed |
| Early project | Prompt systematically first |

(lines 14198–14276, 14307–14335)

- Finetune after extensive prompting; finetuning + prompting often combined (lines 13986–13988).
- **Reasons to finetune:** task quality, structured outputs, rare SQL dialects, bias mitigation (Wang & Russakovsky 2023; Garimella et al. 2022), **distill large→small** (Grammarly Flan-T5 vs GPT-3, 60× smaller, 82k pairs) (lines 13992–14036).
- **Reasons not to:** catastrophic **task narrowing** (footnote: alignment tax); maintenance burden; new base models may outpace finetuned models; unsystematic prompt experiments often blamed on "prompting failure" (lines 14047–14126).
- **Domain-specific caveat:** GPT-4-0314 beat BloombergGPT on financial benchmarks despite Bloomberg's $1.3–2.6M training cost; general models increasingly dominate domain specialists (lines 14130–14172) `[contested]` for proprietary internal use cases.
- Pre–prompt-caching: finetuning baked few-shot into weights to save tokens; prompt caching weakens that benefit (lines 14179–14190).
- Ovadia et al. (2024): RAG beats finetuning on current-events QA; base+RAG often beats finetuned+RAG; RAG+finetune helps ~43% of MMLU categories (lines 14221–14289).

### Memory bottlenecks

- Training memory ≫ inference because backward pass stores gradients + optimizer states per **trainable** parameter (lines 14365–14452).
- **Inference:** `N × M × 1.2` (weights + ~20% activations/KV); 13B @ 2 bytes ≈ 31.2 GB (lines 14476–14505).
- **Training:** weights + activations + gradients + optimizer states; Adam = 3 values per trainable param (lines 14507–14542).
- Activation memory can dwarf weights; **gradient checkpointing** trades compute for memory (lines 14544–14560).
- Format matters: loading Llama 2 as FP16 instead of BF16 degraded quality (lines 14668–14677).
- Quantization reduces bits; PTQ standard for inference; QAT simulates low precision; mixed precision training common (lines 14684–14856).

### PEFT, LoRA, QLoRA

- Full finetuning 7B + Adam @ 16-bit ≈ 56 GB weights/grads/opt alone (lines 14890–14905).
- Partial finetuning parameter-inefficient (~25% params for BERT-large GLUE parity per Houlsby et al. 2019) (lines 14917–14939).
- **PEFT:** adapters (Houlsby 2019, +latency) vs **soft prompts** (prefix-tuning, P-tuning, prompt tuning); LoRA dominates huggingface/peft issue analysis Oct 2024 (lines 14950–15056).
- **LoRA:** low-rank ΔW merged into W without inference layers; ~0.0027% trainable params for GPT-3 with comparable performance; intrinsic dimension argument (Aghajanyan et al.) (lines 15063–15148).
- Rank r often 4–64 sufficient; increasing r may not help (Databricks, LoRA paper) `[contested]` — Raschka found r=256 best on some tasks (lines 15268–15280).
- **Multi-LoRA serving:** keep W + separate (A,B) adapters — 100 customers: 1.68B vs 23.3M params example (lines 15291–15340).
- **QLoRA:** 4-bit NF4 weights, BF16 compute, paged optimizers; 65B on single 48 GB GPU; Guanaco 65B Elo 1022 vs ChatGPT 966 (May 2023 GPT-4 judge) (lines 15366–15426).
- LoRA limitation: generally weaker than full finetuning; implementation complexity for obscure architectures (lines 15357–15364).

### Model merging

- Parallel task finetuning + merge avoids sequential **catastrophic forgetting** (Kirkpatrick et al. 2016) (lines 15470–15497).
- **Ensembling** = multiple inference calls; **merging** = mix parameters (lines 15521–15542).
- **Summing:** linear combo, task vectors/task arithmetic (Ilharco et al. 2022), SLERP; TIES/DARE prune redundant task-vector params before merge (lines 15561–15692).
- **Layer stacking:** frankenmerging (Goliath-120B), MoE sparse upcycling (Komatsuzaki et al. 2022), SOLAR depthwise scaling (lines 15694–15756).
- **Concatenation** of LoRA ranks: higher perf possible but no memory win — author included for completeness (lines 15758–15774).

### Finetuning tactics

- **Progression path:** cheap model code test → mid model data test → best model experiments → price/performance frontier (OpenAI best practices) (lines 15806–15819).
- **Distillation path:** strong model on small data → synthetic data → cheaper student (lines 15821–15830).
- Start LoRA; try full finetuning later; LoRA better for small datasets and multi-adapter serving (lines 15837–15855).
- Frameworks: PEFT, Axolotl, unsloth, LitGPT, LLaMA-Factory; APIs trade customization for ease (lines 15857–15886).
- Hyperparameters: LR 1e-7–1e-3; batch size vs gradient accumulation; epochs 1–2 (millions of examples) vs 4–10 (thousands); prompt loss weight default ~10% (lines 15888–15981).

### Chapter close

- Finetuning execution is easy via frameworks; **deciding whether, acquiring data, serving, maintaining** is hard (lines 15983–16032).
- Forward: Ch. 8 dataset engineering for instruction data (lines 16029–16032).

---

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Chapter opener | read | 13787–13838 |
| Finetuning overview + transfer learning | read | 13839–13979 |
| When to finetune (reasons for/against) | read | 13980–14127 |
| Domain-specific tasks (BloombergGPT) | read | 14128–14177 |
| Token cost / Fig 7-2 | read | 14179–14195 |
| Finetuning and RAG + tables | read | 14196–14289 |
| Adaptation workflow Fig 7-3 | read | 14291–14340 |
| Memory bottlenecks (key takeaways) | read | 14342–14394 |
| Backpropagation + trainable params | read | 14396–14452 |
| Memory math (inference/training) | read | 14454–14560 |
| Numerical representations + Table 7-3 | read | 14567–14683 |
| Quantization (inference/training) | read | 14684–14856 |
| PEFT overview + partial vs full | read | 14858–14983 |
| PEFT taxonomy + soft prompts | read | 14985–15061 |
| LoRA mechanics + why it works | read | 15063–15186 |
| LoRA configurations + Table 7-5 | read | 15187–15290 |
| Serving LoRA / multi-LoRA | read | 15291–15355 |
| QLoRA + Guanaco table | read | 15366–15436 |
| Model merging + multi-task | read | 15438–15559 |
| Summing (linear, SLERP, TIES/DARE) | read | 15561–15692 |
| Layer stacking + SOLAR | read | 15694–15756 |
| Concatenation | read | 15758–15774 |
| Finetuning tactics | read | 15776–15981 |
| Summary + footnotes ¹–³⁷ | read | 15983–16187 |
| Chapter 8 opener | **deferred** | 16188+ (outside scope) |

- **Lines read:** 13787–16187 (full parent-requested range)
- **wrong_file_flag:** false
- **Amnesiac attestation:** Numbered findings trace to line ranges in `ai_engineering_2025.txt`; contested claims retained with source attribution

---

## pedagogy

### learning_objectives

Implicit from chapter arc (no numbered LO block in text):

- Decide when finetuning beats prompting and RAG using failure-mode taxonomy
- Estimate inference and training memory from parameter count and precision
- Choose among full finetuning, partial finetuning, PEFT, and quantization
- Configure LoRA (target matrices, rank, α) and serving mode (merged vs adapter)
- Apply QLoRA constraints for single-GPU large-model finetuning
- Evaluate model merging approaches for multi-task and on-device constraints
- Set core finetuning hyperparameters and interpret loss curves

### worked_examples_present

**Y**

| Example | Skill taught | Anchor |
|---------|--------------|--------|
| Code Llama finetuning pipeline (Fig 7-1) | Stacked finetuning types | 13957–13973 |
| Three-query task degradation (orders) | Task-narrowing risk | 14059–14072 |
| BloombergGPT vs GPT-4 Table 7-1 | Domain-model skepticism | 14145–14161 |
| Few-shot in prompt vs finetuned model (Fig 7-2) | Token/latency trade-off | 14179–14194 |
| Ovadia RAG vs FT tables 7-2 | RAG vs finetune evidence | 14229–14238 |
| 5-step adaptation workflow (Fig 7-3) | Production decision path | 14300–14335 |
| 13B inference memory calc | Back-of-napkin sizing | 14498–14505 |
| 13B Adam gradient memory | Trainable-param scaling | 14531–14542 |
| 7B full finetune 56 GB | Why PEFT needed | 14890–14905 |
| LoRA matrix decomposition (Fig 7-11) | LoRA mechanics | 15076–15096 |
| Multi-LoRA 100-customer storage | Adapter serving economics | 15317–15333 |
| LoRA vs weights memory Table 7-6 | Why QLoRA not smaller LoRA | 15375–15387 |
| Task vector 60%+60%→80% merge intuition | Merge value proposition | 15456–15461 |
| 100-customer LoRA param count | Option 1 vs 2 math | 15325–15333 |

### exercise_hooks

Chapter has **no numbered end-of-chapter exercises**. Hooks below are **operator extensions** from inline examples, formulas, and tables.

| ID | Prompt summary | Operator extension | Anchor |
|----|----------------|-------------------|--------|
| 7.DEC-1 | Three-query order finetune | Finetune on one task; measure regression on other two; try merge or separate models | 14059–14072 |
| 7.DEC-2 | RAG vs FT failure modes | Classify 20 eval failures as information vs behavior; route to RAG or LoRA | 14200–14276 |
| 7.DEC-3 | Ovadia replication | On current-events QA set, compare base, FT, RAG, FT+RAG | 14221–14289 |
| 7.MEM-1 | 13B memory napkin | Compute inference GB for chosen N, precision; compare to GPU VRAM | 14476–14505 |
| 7.MEM-2 | Trainable param budget | Given 24 GB GPU, max trainable params with Adam @ FP16 | 14507–14542 |
| 7.PEFT-1 | LoRA rank sweep | Sweep r ∈ {4,8,16,64,256} on one task; plot val loss vs rank | 15268–15280 |
| 7.PEFT-2 | Multi-LoRA serving | Implement merged vs separate adapters; measure load time and latency | 15298–15340 |
| 7.QLORA-1 | QLoRA 7B smoke | Finetune 7B with NF4 on single consumer GPU; log wall time vs FP16 LoRA | 15392–15431 |
| 7.MERGE-1 | Task vector average | Finetune two LoRA adapters; linear merge; eval both tasks | 15606–15611 |
| 7.MERGE-2 | TIES-style prune | Prune bottom 80% task-vector deltas before merge; compare full merge | 15672–15690 |
| 7.TAC-1 | Progression path | OpenAI-style: cheap code test → mid data test → frontier map | 15806–15819 |
| 7.TAC-2 | Prompt loss weight | Ablate 0% vs 10% vs 100% prompt contribution on instruction set | 15967–15981 |

---

## Operator hooks

### 1. Foundation layer (w1_foundation)

Chapter 7 is the **canon reference for weight-adaptation decisions** in the cs-ai-textbook-canon stack:

- **When-not-to-finetune gate** — systematic prompting and RAG first; eval pipeline from Ch. 4 required before adaptation ladder
- **Memory economics** — sizing formulas prerequisite for Ch. 9 inference optimization and deployment trade-offs
- **LoRA/QLoRA default path** — operational standard for application developers without full-finetune compute
- **Form vs facts** — pairs with Ch. 6 RAG; Ch. 8 for data acquisition once finetune is justified

Treat as **framework spine, not tutorial** per corpus manifest. Pair with **hands_on_llms_2024** for executable finetune notebooks and **ai_engineering_2025_ch08** for dataset strategy once finetune is chosen.

### 2. MDCalc alignment

**[none]** — No clinical deployment or regulated-workflow content. Pattern-portable only: eval-before-adapt, failure-mode routing (information vs behavior), human-in-the-loop before production model swaps, bias-mitigation via curated finetune data (with contested efficacy).

### 3. Redundancy

| Overlap with | Relationship |
|--------------|--------------|
| `ai_engineering_2025` Ch. 2 | Finetuning types recap; Ch. 7 deepens execution and memory |
| `ai_engineering_2025` Ch. 6 | RAG vs finetune decision boundary; Ch. 6 owns retrieval, Ch. 7 owns weights |
| `ai_engineering_2025` Ch. 8 | Instruction data, distillation synthesis — forward dependency |
| `ai_engineering_2025` Ch. 9 | Inference memory, KV cache, prompt caching — backward refs from Ch. 7 |
| `hands_on_llms_2024` | HOTL likely supersedes on LoRA/QLoRA code; keep AIE Ch.7 for decision framework and merge theory |

**Dedup rule:** Use this ingest for **go/no-go and method selection**; defer notebook execution to HOTL unless operator requests AIE-only path.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | Strong Y — memory math, LoRA decomposition, multi-LoRA storage, benchmark tables |
| Exercise hooks | Operator extensions only |
| Chapter boundary | Clean — ends 16187; Ch. 8 at 16188 |
| Citation density | High (PEFT/LoRA/QLoRA papers, Ovadia RAG study, merge literature 2022–2024) |
| Child-skill potential | `scholia.finetune-go-no-go`, `scholia.lora-memory-sizing`, `scholia.rag-vs-ft-router` reference cards |

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | 2025 1e; within ≤5-year preference |
| Author authority | **PASS** | O'Reilly textbook; practitioner pedigree (NVIDIA mixed-precision work cited in footnotes, Stanford MLSys) |
| Primary-source citation density | **PASS** | Dense: InstructGPT, Houlsby/LoRA/QLoRA, Ovadia RAG, Rozière Code Llama, task arithmetic, TIES/DARE, Korthikanti activations |
| Contested claims flagged | **PASS** | See table below |
| Worked examples (procedural chapter) | **PASS** | Memory formulas, LoRA math, workflow ladder, benchmark tables — procedural depth via calculation not code |

### Contested or oversimplified claims (not smoothed)

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Finetuning unlocks latent capabilities | 13876–13879 | InstructGPT framing; not universal |
| GPT-4 beats domain-specific BloombergGPT | 14145–14172 | Benchmark-limited; internal proprietary value may differ |
| Finetuning is for form, RAG for facts | 14264–14270 | Useful heuristic; Llama 3.1 team disputes knowledge via post-training (footnote ⁵) |
| RAG always beats finetune on current events | 14221–14238 | Ovadia et al. 2024 — dataset and model scope limited |
| Bias mitigation via finetune | 14009–14017 | `[contested]` — finetune can also entrench or shift biases |
| LoRA rank increase may not help | 15273–15277 | Databricks/LoRA paper vs Raschka r=256 counterexample |
| BitNet 1.58-bit ≈ 16-bit Llama 2 | 14751–14770 | Early-scale results; scaling contested |
| Model merging techniques experimental | 15544–15546 | Author explicit; many approaches may obsolete |
| Alignment tax terminology | 16034–16036 | Footnote: confusable with preference-alignment penalty |
| Small batch → unstable training | 15925–15936 | Footnote ³⁶: author couldn't find definitive citation |

**TEXTBOOK-Q1 chapter verdict:** **PASS** — flagship w1_foundation ingest for finetune decisioning and PEFT; flag RAG-vs-FT heuristic and domain-model anecdotes when cross-linking; pair with HOTL for hands-on LoRA.

---

## Glossary (chapter-local)

| Term | Definition per text |
|------|---------------------|
| Finetuning | Further training whole or part of model to adapt weights to a task |
| Transfer learning | Reuse knowledge from one task to accelerate learning on a related task |
| Continued pre-training | Self-supervised finetuning on domain raw text before supervised finetune |
| Supervised finetuning (SFT) | Training on (input, output) pairs including instructions |
| Preference finetuning | RL or comparative training on (instruction, winner, loser) |
| Full finetuning | Update all parameters |
| Partial finetuning | Freeze some layers; update subset |
| PEFT | Parameter-efficient finetuning — few trainable params, near full-FT quality |
| Adapter | Added modules (Houlsby) trained while base frozen |
| Soft prompt | Trainable continuous tokens prepended to guide behavior |
| LoRA | Low-rank adaptation merged into weight matrices without extra inference layers |
| LoRA rank (r) | Inner dimension of low-rank factorization |
| QLoRA | 4-bit quantized base weights + LoRA adapters + paged optimizers |
| Task vector | Finetuned weights minus base weights; supports task arithmetic |
| Model merging | Combine multiple models' parameters into one model |
| SLERP | Spherical linear interpolation for merge weights |
| Gradient checkpointing | Recompute activations instead of storing — saves memory |
| Quantization | Reduce bit width of weights/activations |
| Prompt loss weight | Fraction of loss attributed to prompt vs response tokens in SFT |

---

## Reciprocal index pointers

- **Prerequisites:** Ch. 2 (finetuning types, transformers), Ch. 4 (eval pipeline), Ch. 5 (prompting), Ch. 6 (RAG, semantic parsing)
- **Forward:** Ch. 8 dataset engineering (instruction data); Ch. 9 inference optimization, prompt caching, KV cache
- **External depth:** book GitHub (ML basics, multi-LoRA latency walkthrough); OpenAI finetuning best practices; Llama Police framework list; Carol Chen "Transformer Inference Arithmetic"; EleutherAI "Transformer Math 101"
