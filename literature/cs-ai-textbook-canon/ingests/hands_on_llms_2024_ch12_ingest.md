# Chapter ingest — `hands_on_llms_2024` · Chapter 12

**Corpus:** cs-ai-textbook-canon · **Slug:** hands_on_llms_2024 · **Wave:** w1_foundation  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/hands_on_llms_2024_ch12_ingest.md`

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **parent_book_title** | Hands-On Large Language Models |
| **authors** | Jay Alammar, Maarten Grootendorst |
| **edition** | 1e (First Edition, September 2024) |
| **publisher** | O'Reilly Media |
| **ISBN_print** | 978-1-098-15095-2 [corpus manifest] |
| **ISBN_electronic** | 9781098150969 [verified from text, line 118] |
| **chapter_number** | 12 |
| **chapter_title** | Fine-Tuning Generation Models |
| **page_range** | Not present in text export; logical span `Chapter 12. Fine-Tuning Generation Models` (line 13222) through `Summary` + footnotes before Afterword (line 14497) |

---

## scope

Chapter 12 is the **executable generative fine-tuning capstone**: three-stage LLM training (pretrain → SFT → preference tuning), PEFT theory (adapters, LoRA, QLoRA), full TinyLlama QLoRA instruction tuning, generative evaluation methods, and DPO preference alignment — with ORPO noted as monolithic alternative.

**Major arcs within assigned slice (lines 13222–14497):**

1. **Three training steps** — language modeling (base model) → supervised fine-tuning (instruction following) → preference tuning (alignment/safety) (lines 13236–13297).
2. **SFT theory** — full fine-tuning on labeled instruction data; base models complete prompts instead of answering (lines 13299–13344).
3. **PEFT** — Houlsby adapters (3.6% params ≈ full BERT GLUE); LoRA low-rank decomposition; intrinsic dimension argument; QLoRA NF4 blockwise quantization + double quant + paged optimizers (lines 13346–13526).
4. **QLoRA instruction tuning lab** — UltraChat 3k subset; TinyLlama chat template; bitsandbytes 4-bit; peft LoRA r=64, alpha=32; SFTTrainer; merge_and_unload; ~1 GB load VRAM vs ~4 GB FP16 (lines 13528–13839).
5. **Evaluating generative models** — perplexity, ROUGE, BLEU, BERTScore; MMLU/GLUE/TruthfulQA/GSM8k/HellaSwag/HumanEval; leaderboards; LLM-as-judge; Chatbot Arena Elo; Goodhart's Law (lines 13841–14011).
6. **Preference tuning / RLHF** — reward model scoring; PPO (ChatGPT); DPO without separate reward model; Llama 2 dual reward models (helpfulness/safety) (lines 14013–14194).
7. **DPO lab** — distilabel-intel-orca-dpo-pairs ~6k; DPOTrainer beta=0.1; 200 steps; iterative SFT+DPO adapter merge; ORPO combines SFT+DPO (lines 14196–14394).
8. **Summary + book close** — two-step fine-tune pipeline recap (lines 14396–14497).

**Prerequisites cited:** Ch. 3 (language modeling), Ch. 11 (Trainer patterns, MLM), Ch. 7 quantization blog cross-ref.

**Manifest note:** **Primary executable pair for `ai_engineering_2025` Ch. 7** — HOTL owns QLoRA/SFT/DPO notebooks; AIE owns decision framework, memory formulas, merge theory.

---

## key_findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

### Three-step LLM training

| Step | Goal | Data | Output |
|------|------|------|--------|
| 1. Language modeling | Next-token prediction | Massive unlabeled text | Base/foundation model |
| 2. SFT | Follow instructions | Labeled instruction-response pairs | Instruction/chat model |
| 3. Preference tuning | Align to human preference | Chosen vs rejected completions | Aligned model |

(lines 13236–13292)

- Base models complete questions rather than answer them (lines 13309–13315).
- SFT uses next-token prediction conditioned on user input labels (lines 13264–13276).

### Full fine-tuning vs PEFT

- Full fine-tuning updates all parameters on smaller labeled set vs unlabeled pretrain (lines 13320–13344).
- **Adapters** (Houlsby et al. 2019): ~3.6% trainable params; within 0.4% of full fine-tune on GLUE; per-block modules swappable for task specialists (lines 13355–13392).
- **LoRA** (Hu et al. 2021): low-rank ΔW merged into frozen W; rank 8 on 12,288×12,288 → ~197K params/block vs 150M; target Q/V projections optionally only (lines 13401–13460).
- Intrinsic dimensionality (Aghajanyan et al.) supports low-rank effectiveness (lines 13447–13456).

### QLoRA mechanics

- Quantization reduces bits (FP32→FP16→4-bit NF4); naive mapping collapses nearby weights (lines 13464–13486).
- QLoRA (Dettmers et al. 2023): blockwise + distribution-aware NF4; double quantization; paged optimizers (lines 13487–13526).
- Quantization helps inference VRAM too (lines 13519–13521).

### QLoRA instruction tuning (TinyLlama)

- Base: `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T`; chat template from `TinyLlama-1.1BChat-v1.0` (lines 13537–13581).
- Data: `HuggingFaceH4/ultrachat_200k` test_sft subset 3,000 (lines 13575–13584).
- Quantization: `load_in_4bit`, `bnb_4bit_quant_type="nf4"`, `bnb_4bit_use_double_quant` → ~1 GB load vs ~4 GB (lines 13622–13651).
- LoRA: r=64, alpha=32, dropout 0.1, target all projection modules; rule of thumb alpha ≈ 2×r (lines 13662–13688).
- Training: batch 2, grad_accum 4, lr 2e-4, cosine scheduler, `paged_adamw_32bit`, fp16, gradient_checkpointing (lines 13714–13754).
- `SFTTrainer` with `peft_config`; save `TinyLlama-1.1B-qlora`; `merge_and_unload` for inference (lines 13773–13837).
- Remove `quantization_config` + `peft_config` for full SFT path (lines 13700–13706).
- Colab T4: training ~1 hour (lines 13794–13797).

### Generative evaluation

- Word-level: perplexity, ROUGE, BLEU, BERTScore — confidence not fluency/correctness (lines 13858–13882).
- Benchmarks table: MMLU, GLUE, TruthfulQA, GSM8k, HellaSwag, HumanEval (lines 13884–13907).
- Leaderboard overfitting risk (Open LLM Leaderboard) (lines 13918–13931).
- LLM-as-judge / pairwise comparison (Zheng et al.) (lines 13933–13953).
- Chatbot Arena: 800k+ human votes, Elo ratings (lines 13963–13976).
- **Goodhart's Law** quoted: optimizing a measure degrades it as target (lines 13998–14011).
- Author advice: evaluate for intended use case; operator is best evaluator (lines 13983–13996).

### Preference tuning: reward models, PPO, DPO

- Preference evaluator scores generation; high score reinforce, low discourage (lines 14030–14049).
- Reward model: LLM copy with classification head → scalar quality score per (prompt, generation) (lines 14055–14082).
- Training data: prompt + accepted + rejected completion pairs (lines 14090–14111).
- Three stages: collect preferences → train reward model → fine-tune LLM with reward signal (lines 14129–14141).
- Llama 2: separate helpfulness and safety reward models (lines 14143–14149).
- **PPO** (Schulman et al.): used for original ChatGPT; complex — trains reward model + policy (lines 14151–14161).
- **DPO** (Rafailov et al.): no separate reward model; reference LLM vs trainable LLM log-prob shift on chosen/rejected (lines 14163–14194).

### DPO lab

- Dataset: `argilla/distilabel-intel-orca-dpo-pairs`; filter ties, chosen_score≥8, not in GSM8k train → ~6k (lines 14216–14249).
- Load merged QLoRA SFT model, re-quantize 4-bit, new LoRA for DPO (lines 14251–14303).
- `DPOConfig`: lr 1e-5, max_steps=200, warmup_ratio=0.1 (lines 14318–14335).
- `DPOTrainer` beta=0.1; save `TinyLlama-1.1B-dpo-qlora` (lines 14343–14361).
- Merge SFT then DPO adapters sequentially (lines 14363–14383).
- **ORPO** (Hong et al. 2024): combines SFT+DPO in single training loop (lines 14390–14394).

---

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Chapter opener | read | 13222–13234 |
| Three LLM training steps | read | 13236–13297 |
| SFT theory + full fine-tuning | read | 13299–13344 |
| PEFT adapters | read | 13346–13399 |
| LoRA theory | read | 13401–13460 |
| QLoRA quantization theory | read | 13462–13526 |
| Instruction data templating | read | 13537–13603 |
| Model quantization (bitsandbytes) | read | 13603–13651 |
| LoRA configuration (peft) | read | 13653–13706 |
| Training configuration | read | 13708–13764 |
| SFTTrainer training + merge | read | 13766–13839 |
| Evaluating generative models | read | 13841–14011 |
| Preference tuning / RLHF theory | read | 14013–14194 |
| DPO data + quantization + train | read | 14196–14383 |
| ORPO mention | read | 14390–14394 |
| Summary + footnotes ¹–²³ | read | 14396–14496 |
| Afterword | **deferred** | 14498+ (outside scope) |

- **Lines read:** 13222–14497 (full parent-requested range; index/afterword excluded)
- **wrong_file_flag:** false
- **Amnesiac attestation:** Hyperparameters and metrics trace to `hands_on_llms_2024.txt`

---

## pedagogy

### learning_objectives

Implicit from chapter arc:

- Distinguish pretrain, SFT, and preference tuning stages and their data
- Explain adapters, LoRA, and QLoRA memory/parameter trade-offs
- Run QLoRA instruction tuning on TinyLlama with SFTTrainer
- Select generative eval methods for a target use case
- Describe reward models, PPO, and DPO alignment pipelines
- Execute DPO fine-tuning and merge stacked adapters

### worked_examples_present

**Y**

| Example | Skill taught | Anchor |
|---------|--------------|--------|
| Base model completes vs answers | Why SFT needed | 13309–13315 |
| LoRA 10×10 → 10+10 decomposition | Rank efficiency intuition | 13419–13433 |
| UltraChat formatted prompt | Chat template application | 13589–13601 |
| 4-bit load 1 GB vs 4 GB | Quantization VRAM win | 13646–13651 |
| Merged model instruction response | Post-QLoRA behavior | 13825–13837 |
| Perplexity next-word diagram | Word-level metric limit | 13871–13877 |
| DPO prompt/chosen/rejected format | Alignment data shape | 14218–14231 |
| SFT+DPO double merge | Stacked adapter deployment | 14363–14383 |

### exercise_hooks

| ID | Prompt summary | Operator extension | Anchor |
|----|----------------|-------------------|--------|
| 12.QLORA-1 | Rank sweep | Sweep r ∈ {8,16,32,64}; compare merged model on 10 prompts | 13678–13688 |
| 12.QLORA-2 | Full vs QLoRA | Run same 3k subset with/without quantization_config | 13700–13706 |
| 12.EVAL-1 | Use-case eval | Pick 2 benchmarks aligned to operator task; avoid leaderboard-only | 13983–13996 |
| 12.GOODHART-1 | Metric gaming | Design prompt where high BLEU fails human quality | 13998–14011 |
| 12.DPO-1 | Beta ablation | Sweep DPO beta; compare verbosity/safety on held-out prompts | 14352–14355 |
| 12.ORPO-1 | ORPO compare | `[inferred]` — replicate DPO section with ORPO per footnote ²³ | 14390–14394 |

---

## Operator hooks

### 1. Foundation layer (w1_foundation)

Chapter 12 is the **generative fine-tune executable canon** for cs-ai-textbook-canon:

- **QLoRA default lab path** — TinyLlama + peft + trl stack reproducible on consumer GPU
- **SFT → DPO stack** — two-loop alignment pattern; ORPO for single-loop experiments
- **Eval humility** — no single metric; use-case benchmarks + human review
- **Pairs with AIE Ch. 7** — decision/memory/merge theory there; notebooks here

### 2. MDCalc alignment

**[pattern-portable]** — Preference tuning framed around safety/helpfulness (Llama 2 dual reward models, lines 14143–14149). No clinical deployment guidance. Regulated use requires domain eval beyond public benchmarks; NER/de-id from Ch. 11 is separate gate.

### 3. Redundancy

| Overlap with | Relationship |
|--------------|--------------|
| `ai_engineering_2025` Ch. 7 | **AIE Ch. 7 = when-to-finetune, memory economics, LoRA/QLoRA theory, multi-LoRA serving, model merging (TIES/DARE), hyperparameter tactics; HOTL Ch. 12 = runnable TinyLlama QLoRA SFT + DPO with trl/peft/bitsandbytes** |
| `ai_engineering_2025` Ch. 8 | AIE dataset engineering for instruction data; HOTL uses UltraChat subset templating only |
| `ai_engineering_2025` Ch. 4 | AIE eval pipeline; HOTL generative eval survey overlaps MMLU/leaderboard vocabulary |
| `hands_on_llms_2024` Ch. 11 | Encoder fine-tune; Ch. 12 generative fine-tune — complementary |
| `hands_on_llms_2024` Ch. 10 | Embedding training; different model head |

**Dedup rule:** **AIE Ch. 7 for go/no-go, sizing, and method selection; HOTL Ch. 12 for executing QLoRA SFT/DPO.** Do not duplicate AIE merge theory in HOTL workflows unless operator extends labs.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | Strong Y — end-to-end QLoRA + DPO |
| Exercise hooks | Operator extensions |
| Chapter boundary | Clean — ends 14417; afterword 14498 |
| Citation density | High (Houlsby, Hu, Dettmers, Rafailov, Schulman, ORPO) |
| Child-skill potential | `scholia.qlora-instruction-tune`, `scholia.dpo-alignment-lab` |

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | 2024 1e |
| Author authority | **PASS** | Practitioner authors; cites primary PEFT/alignment papers |
| Primary-source citation density | **PASS** | Houlsby, Pfeiffer AdapterHub, Hu LoRA, Dettmers QLoRA, Rafailov DPO |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Full GPU-oriented labs |

### Contested or oversimplified claims (not smoothed)

| Claim | Text anchor | Flag |
|-------|-------------|------|
| LoRA rank 8 sufficient for 175B blocks | 13450–13455 | Illustrative; task/model dependent |
| Higher epochs degrade performance | 13734–13736 | Generalization caveat; underfitting on small data |
| QLoRA higher LR for models >33B | 13738–13741 | TinyLlama lab uses 2e-4 regardless |
| Leaderboard top = best model | 13928–13931 | Overfitting/public benchmark risk explicit |
| DPO more stable than PPO | 14191–14194 | Authors' finding; setup dependent |
| SFT+DPO two loops cost | 14385–14388 | ORPO alternative noted |

**TEXTBOOK-Q1 chapter verdict:** **PASS** — flagship w1_foundation generative fine-tune ingest; mandatory AIE Ch. 7 pairing documented in redundancy.

---

## Glossary (chapter-local)

| Term | Definition per text |
|------|---------------------|
| Base model | LLM after language-modeling pretrain; poor instruction follower |
| SFT | Supervised fine-tuning on labeled input-output pairs for instruction following |
| Preference tuning | Fine-tune to prefer some completions over others (alignment) |
| PEFT | Parameter-efficient fine-tuning — update small param subset |
| Adapter | Small trainable modules inserted in Transformer blocks |
| LoRA | Low-rank adaptation matrices merged into frozen weights |
| QLoRA | 4-bit quantized base weights + LoRA + paged optimizers |
| Reward model | Scalar scorer for (prompt, generation) quality |
| PPO | Proximal Policy Optimization — RL fine-tune with reward model |
| DPO | Direct Preference Optimization — preference loss without separate reward model |
| ORPO | Odds Ratio Preference Optimization — combined SFT+DPO single loop |
| Instruction tuning | SFT specifically for chat/instruction following |

---

## Reciprocal index pointers

- **Prerequisites:** Ch. 3 (generative models), Ch. 11 (Trainer, MLM), Ch. 7 blog (quantization visual guide)
- **AIE pair:** `ai_engineering_2025_ch07_ingest.md` — framework spine vs HOTL hands-on code
- **Forward:** Book afterword (14498); operator extends to production serving (AIE Ch. 9)
- **External depth:** peft, trl, bitsandbytes docs; QLoRA paper; Raschka LoRA tips; Chatbot Arena
