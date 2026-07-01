# Chapter ingest — `ai_engineering_2025` · Chapter 9

**Corpus:** cs-ai-textbook-canon · **Slug:** ai_engineering_2025 · **Wave:** w1_foundation  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch09_ingest.md`

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
| **chapter_number** | 9 |
| **chapter_title** | Inference Optimization |
| **page_range** | Not present in text export; logical span from `Chapter 9. Inference Optimization` through `Summary` before Ch. 10 |

---

## scope

Chapter 9 closes Huyen's **model-adaptation arc** by shifting from making models *better* (prior chapters) to making them **faster and cheaper** at inference. The chapter is interdisciplinary—model researchers, application developers, system engineers, compiler designers, hardware architects, and data-center operators all contribute. Focus is **model-level** and **service-level** optimization, plus an **AI accelerators** overview; hardware design itself is out of scope.

**Major arcs:**

1. **Vocabulary and bottlenecks** — training vs inference; inference server vs service; compute-bound vs memory bandwidth-bound (Roofline); LLM **prefill** (compute-bound) vs **decode** (memory bandwidth-bound); online vs batch APIs.
2. **Performance metrics** — latency (TTFT, TPOT, TBT/ITL), throughput (TPS, RPM), **goodput** (SLO satisfaction), utilization (nvidia-smi GPU util vs **MFU** vs **MBU**).
3. **AI accelerators** — GPUs vs CPUs; inference-specialized chips; FLOP/s by precision; memory hierarchy (DRAM, HBM, SRAM); power/TDP; chip selection heuristics.
4. **Model optimization** — compression (quantization Ch. 7, distillation Ch. 8, pruning); autoregressive decoding (speculative decoding, inference with reference, parallel/Jacobi/Medusa decoding); attention/KV cache (redesign, PagedAttention, FlashAttention, kernels/compilers).
5. **Service optimization** — batching (static, dynamic, continuous/Orca); prefill/decode disaggregation; prompt caching; parallelism (replica, tensor, pipeline, context, sequence).

**Prerequisites cited:** Ch. 2 (transformer, prefill/decode, autoregression), Ch. 7 (quantization, numerical precision), Ch. 8 (distillation).

**Out of scope (stated):** hardware architecture design; full compiler/kernel tutorial; Ch. 10 system integration (forward ref).

**Manifest note:** Framework spine — pair with **hands_on_llms_2024** for vLLM/torch.compile labs; **designing_ml_systems_2022** for serving overlap.

---

## key_findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

### Framing: why inference optimization matters

- Slow models lose users or become useless (e.g., two-day stock prediction); expensive models fail ROI (lines 18091–18095).
- Optimization spans **model, hardware, and service** levels; this chapter focuses model + service with accelerator overview (lines 18097–18117).
- Even API consumers benefit from understanding techniques to **evaluate providers and diagnose latency/cost** (lines 18125–18130).
- Inference = forward pass only; training adds backward pass (footnote ¹, Ch. 7 cross-ref) (lines 18134–18138).

### Bottlenecks and LLM inference profile

| Bottleneck | Determined by | LLM phase |
|------------|---------------|-----------|
| Compute-bound | Arithmetic intensity / FLOP/s | Prefill (parallel input tokens) |
| Memory bandwidth-bound | Data transfer rate CPU↔GPU, HBM | Decode (sequential token gen) |

(lines 18175–18256)

- **Roofline model** (Williams et al. 2009): arithmetic intensity classifies workloads; Nsight roofline charts (lines 18213–18232).
- Image generators (Stable Diffusion) often compute-bound; autoregressive LMs typically bandwidth-bound at decode (lines 18234–18237).
- Prefill and decode **often decoupled onto separate machines** in production (lines 18264–18266).
- Context length, output length, and batching strategy shift bottleneck mix; long context tends bandwidth-bound unless optimized (lines 18268–18273).
- `[contested]` Author: many current AI workloads are memory bandwidth-bound; future HW/SW may flip to compute-bound (lines 18275–18279).

**Terminology note:** "memory-bound" ambiguous—systems engineers often mean bandwidth; AI engineers often mean OOM/capacity (lines 18195–18211, footnote ³).

### Online vs batch APIs

- **Online:** latency-optimized, process on arrival; may still micro-batch (lines 18283–18300).
- **Batch:** cost-optimized; Gemini/OpenAI ~50% cost reduction, hours vs seconds turnaround (lines 18288–18295).
- Batch FM APIs ≠ traditional ML batch (precomputed recs); open-ended prompts prevent precomputation (lines 18333–18349).
- Customer-facing: chatbots, code gen → online. Batch fit: synthetic data, periodic reports, onboarding doc processing, model migration reprocessing, bulk personalization, knowledge-base reindex (lines 18302–18321).
- **Streaming** reduces wait for first token but prevents pre-scoring responses before display (lines 18323–18331).

### Latency metrics

- **TTFT** = prefill duration; conversational chat expects near-instant; document summarization tolerates longer (lines 18367–18374).
- **TPOT** = per-token decode after first; ~120 ms/token (~6–8 tok/s) matches fast human reading (lines 18376–18386).
- Total latency ≈ TTFT + TPOT × output tokens (line 18394).
- TTFT/TPOT trade-off tunable by shifting compute between prefill and decode instances (lines 18396–18403).
- CoT/agentic flows: model TTFT (internal plan) ≠ user-visible TTFT; **time to publish** metric (lines 18405–18410).
- Latency is a **distribution**—use p50/p90/p95/p99, not averages alone (lines 18428–18444).

### Throughput, cost, and goodput

- Throughput = output tokens/s across all users; count input/output separately when prefill/decode decoupled (lines 18448–18456).
- Also measured as RPS or RPM for concurrent-request throttling (lines 18462–18469).
- Worked cost example: $2/h, 100 tok/s decode → ~$5.56/M output tokens; prefill 100 req/min → $0.33/1K requests; combined $1.44/1K requests (lines 18471–18483).
- LinkedIn (2024): willing to sacrifice TTFT/TPOT can **2–3× throughput** (lines 18498–18501).
- **Goodput** = requests/s meeting SLO (e.g., TTFT ≤200 ms AND TPOT ≤100 ms); 100 RPM with 30 SLO-compliant → goodput 30 RPM (lines 18505–18518).

### Utilization: MFU and MBU

- nvidia-smi **GPU utilization** (% time busy) misleading—can show 100% at 1/100 capacity (lines 18526–18542).
- **MFU** = observed tok/s vs peak-FLOP/s theoretical max (PaLM term) (lines 18544–18552).
- **MBU** = (param_count × bytes/param × tok/s) / theoretical bandwidth (lines 18554–18581).
- Example: 7B FP16 @ 100 tok/s → 700 GB/s on A100-80GB (2 TB/s) → MBU 70%; quantization reduces bytes/param (lines 18569–18576).
- Training MFU typically > inference MFU; prefill MFU > decode MFU; training MFU >50% considered good (lines 18592–18598).
- Table 9-1: GPT-3 21.3% MFU on V100; PaLM 46.2% on TPU v4 (lines 18599–18609).
- Llama 2-70B FP16 MBU declines as concurrent users rise (shift toward compute-bound) (lines 18611–18614).

### AI accelerators (overview)

- AlexNet 2012 GPU success catalyzed deep learning boom vs thousands of CPUs (lines 18641–18649).
- **CPUs:** few powerful cores, sequential/OS/I/O; **GPUs:** thousands of smaller cores, matmul-heavy parallel work (lines 18658–18673).
- Inference can exceed training cost at scale; **up to 90% of ML cost** for deployed systems is inference (Desislavov et al. 2023) (lines 18686–18690).
- Inference chips optimize lower precision + faster memory vs training's large memory/backprop (lines 18692–18702).
- Key specs: FLOP/s (precision-dependent), memory size/bandwidth, power/TDP (lines 18726–18730).
- H100 SXM Table 9-2: TF32 989 TFLOP/s; BF16/FP16 1,979; FP8 3,958 (with sparsity) (lines 18751–18771).
- Memory hierarchy: CPU DRAM (25–50 GB/s), GPU HBM (256 GB/s–1.5+ TB/s, 24–80 GB), on-chip SRAM (>10 TB/s, ~40 MB) (lines 18794–18826).
- H100 peak ~7,000 kWh/year ≈ 70% avg US household electricity (lines 18853–18858).
- Selection: compute-bound → more FLOP/s; memory-bound → bandwidth + capacity (lines 18880–18883).

### Model optimization

**Archery metaphor:** model = arrows; hardware = archer; service = shooting process (lines 18901–18906).

- Optimization may **degrade quality**—same Llama served by different providers shows benchmark variance (Cerebras 2024, Fig. 9-8) (lines 18908–18916).
- Three transformer inference pain points: **model size**, **autoregressive decoding**, **attention mechanism** (lines 18928–18931).

**Compression:**

| Technique | Status (as of writing) | Notes |
|-----------|-------------------------|-------|
| Weight-only quantization | Most popular | Easy, effective; FP32→FP16 halves memory |
| Distillation | Common | Smaller model, comparable behavior |
| Pruning | Less common in practice | 90%+ sparse params possible (Frankle & Carbin) but HW sparsity support uneven |

(lines 18933–18980)

**Autoregressive decoding:**

- Output token costs ~2–4× input token across providers; 1 output token ≈ 100 input tokens for latency (Anyscale/Kadous 2023) (lines 18987–18991).
- **Speculative decoding:** draft model proposes K tokens; target verifies in parallel; accept longest agreeing prefix + 1 target token; turns decode profile toward prefill; idle FLOPs during bandwidth-bound decode (lines 19000–19055).
- Chinchilla-70B + 4B draft: 8× faster draft, >50% latency reduction (Chen et al. 2023); ~50 lines PyTorch; in vLLM, TensorRT-LLM, llama.cpp (lines 19064–19076).
- **Inference with reference:** copy overlapping spans from input instead of generating (Yang et al. 2023, ~2× speedup for RAG/code/multi-turn) (lines 19078–19101).
- **Parallel decoding:** Lookahead (Jacobi verify), Medusa (multi-head, NVIDIA 1.9× Llama 3.1 on HGX H200); harder to implement (lines 19109–19165).

**Attention / KV cache:**

- KV cache stores prior key/value vectors for reuse at decode; training doesn't need it (lines 19169–19196).
- Attention compute O(n²); KV cache size linear in sequence length (lines 19198–19201).
- Pope et al.: 500B+ model, batch 512, ctx 2048 → **3 TB KV cache** (3× model weights) (lines 19203–19206).
- KV size formula: 2 × B × S × L × H × M; Llama 2 13B example → **54 GB** unoptimized (lines 19221–19243).
- **Redesign (train/finetune only):** local windowed attention (Beltagy 2020), cross-layer attention, multi-query/grouped-query attention (Shazeer 2019; Ainslie 2023) (lines 19245–19277).
- Character.AI: avg 180-message dialogs; MQA + local/global interleave + cross-layer → **>20× KV reduction** (lines 19279–19287).
- **Runtime KV management:** vLLM **PagedAttention** (Kwon 2023); KV quant, adaptive compression, selective KV (lines 19289–19304).
- **Kernels:** FlashAttention fuses ops (Dao 2022); FlashAttention-3 for H100 (Shah 2024); vectorization, parallelization, loop tiling, operator fusion (lines 19306–19391).
- PyTorch case study (Llama-7B, A100): torch.compile → INT8 → INT4 → speculative decoding cumulative throughput gains (Fig. 9-14); quality impact unclear (lines 19408–19427).

### Service optimization

- Service techniques **don't modify models**—no quality change (lines 19440–19446).

**Batching:**

| Type | Behavior | Latency trade-off |
|------|----------|-------------------|
| Static | Fixed batch size; wait until full | First request waits for last |
| Dynamic | Max size OR time window (e.g., 4 req or 100 ms) | Controlled; may under-fill |
| Continuous (Orca) | Return completed requests immediately; refill batch | Best for variable output lengths |

(lines 19448–19505)

**Prefill/decode disaggregation:**

- Same GPU running both competes for resources; adding query adds prefill that slows existing decode TPOT (lines 19507–19518).
- DistServe (Zhong 2024), Inference Without Interference (Hu 2024): separate instances improve throughput under latency SLOs; NVLink overhead modest (lines 19520–19529).
- Prefill:decode ratio examples: long input + low TTFT priority → 2:1–4:1; short input + TPOT priority → 1:2–1:1 (lines 19531–19537).

**Prompt caching:**

- Cache overlapping segments (system prompt, long docs, prior turns); also prefix/context cache (lines 19539–19556).
- 1K-token system prompt × 1M daily calls ≈ **1B tokens saved/day** (lines 19562–19566).
- Anthropic Table 9-3: book chat (100K cached) TTFT 11.5s→2.4s (−79%), cost −90%; multi-turn −75% latency, −53% cost (lines 19571–19588).
- Gemini: cached input 75% discount; storage $1/M tokens/hour (lines 19573–19576).

**Parallelism:**

- **Replica parallelism:** duplicate model instances; bin-packing across model sizes and GPU memory (lines 19601–19621).
- **Tensor parallelism:** split operators across devices; reduces latency but adds comm overhead (lines 19628–19646).
- **Pipeline parallelism:** stage split; increases per-request latency—avoid for strict latency, common in training (lines 19648–19668).
- **Context/sequence parallelism:** split long inputs across devices (lines 19670–19684).

### Summary (chapter-authored)

- Usability hinges on inference cost/latency; metrics (TTFT, TPOT, throughput, goodput) precede optimization (lines 19688–19704).
- Model-level changes may alter behavior; service-level keeps model intact (lines 19718–19722).
- Workload-dependent choices: KV cache for long context; prompt cache for overlapping prefixes (lines 19739–19748).
- **Most impactful across use cases:** quantization, tensor parallelism, replica parallelism, attention optimization (lines 19750–19755).
- Inference optimization **concludes model-adaptation techniques**; Ch. 10 integrates into systems (lines 19757–19759).

---

## coverage_attestation

| Check | Status |
|-------|--------|
| **Source file** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ai_engineering_2025.txt` |
| **Lines read** | 18084–19895 (inclusive) |
| **Chapter boundary** | Starts `Chapter 9. Inference Optimization` (18084); ends before `Chapter 10. AI Engineering Architecture and User Feedback` (19896) |
| **Wrong-file flag** | `false` |
| **Sections in slice** | Intro · Understanding Inference Optimization (overview, bottlenecks, online/batch, metrics) · AI Accelerators (overview, selection) · Inference Optimization (model: compression, decoding, attention/kernels; service: batching, disaggregation, prompt cache, parallelism) · Summary · footnotes ¹–²⁷ |
| **Deferred** | Figure placeholders; full kernel/compiler tutorials; Ch. 10+ |
| **Cross-chapter refs cited, not re-ingested** | Ch. 2, 7, 8; forward Ch. 10 |
| **Tables in slice** | 9-1 (MFU examples), 9-2 (H100 FLOP/s), 9-3 (prompt caching Anthropic) |
| **Figures referenced** | 9-1 through 9-19 (not rendered in text export) |

---

## pedagogy

### learning_objectives

After this chapter, a reader should be able to:

1. Distinguish **compute-bound** vs **memory bandwidth-bound** workloads and map them to LLM **prefill** vs **decode**.
2. Define and interpret **TTFT**, **TPOT**, **throughput**, **goodput**, **MFU**, and **MBU** for capacity planning.
3. Compare **online**, **batch**, and **streaming** inference APIs and their cost/latency profiles.
4. Explain **speculative decoding**, **inference with reference**, and **parallel decoding** trade-offs for autoregressive LMs.
5. Size **KV cache** memory and name optimization buckets (architecture redesign, cache management, kernels).
6. Contrast **static**, **dynamic**, and **continuous** batching and **prefill/decode disaggregation**.
7. Evaluate **prompt caching** ROI for system prompts, long documents, and multi-turn apps.
8. Select among **replica**, **tensor**, and **pipeline** parallelism given latency vs throughput priorities.

### worked_examples_present

**Y** — Conceptual and quantitative walkthroughs (no executable code in chapter):

| Example | Lines (approx.) | Role |
|---------|-----------------|------|
| Stock prediction too slow | 18091–18094 | Latency stakes |
| Password decrypt vs CPU→GPU transfer | 18180–18193 | Bottleneck intuition |
| Prefill/decode profile (Ch. 2 recall) | 18239–18256 | LLM-specific bottlenecks |
| TTFT outlier skewing average | 18428–18435 | Percentile reporting |
| $2/h throughput → $/M tokens + prefill/decode split | 18471–18483 | Cost arithmetic |
| Goodput 100 RPM, 30 SLO-compliant | 18509–18518 | SLO-aware metric |
| 7B FP16 MBU on A100 | 18569–18581 | Bandwidth utilization |
| Chinchilla-70B speculative decoding | 19064–19070 | Draft/target speedup |
| Llama 2 13B KV cache 54 GB | 19239–19243 | Cache sizing |
| Local window 10K→1K tokens, 10× KV reduction | 19252–19258 | Attention redesign |
| 1M calls/day, 1K system prompt → 1B tokens saved | 19562–19566 | Prompt cache ROI |
| Bin-packing 8B–70B models on 24–80 GB GPUs | 19608–19617 | Replica placement |

### exercise_hooks

- **In-chapter exercises:** **N** — no end-of-chapter problem set.
- **Operator drill ideas `[inferred]`:**
  - Profile a local LLM run: estimate MFU/MBU from param count, precision, observed tok/s.
  - Plot TTFT vs input length from API logs; compute p95/p99.
  - Model cost: given $/GPU-hour and tok/s, compare online vs batch API pricing.
  - Size KV cache for your context window, batch size, and layer count.
  - Sketch prefill:decode instance ratio for your traffic (input/output length distribution).
  - BenchmarkClosed prompt-cache savings for fixed system prompt + daily query volume.

---

## Operator hooks

### 1. Foundation layer

Chapter 9 is the **Track B rank-1 framework spine** for production inference decisions. It completes the adaptation stack:

- **ai_engineering_2025 Ch. 2** — transformer, prefill/decode vocabulary (required).
- **ai_engineering_2025 Ch. 7** — quantization (referenced heavily).
- **ai_engineering_2025 Ch. 8** — distillation (referenced).
- **hands_on_llms_2024** — procedural complement for vLLM, llama.cpp, torch.compile `[manifest tag]`.
- **designing_ml_systems_2022** — serving/infrastructure overlap (optional deepen).

Downstream: **Ch. 10** integrates techniques into AI engineering architecture and user feedback.

Prerequisite stack: model behavior (Ch. 2) → finetune/quantize (Ch. 7–8) → **inference optimization (Ch. 9)** → system architecture (Ch. 10).

### 2. MDCalc alignment

**[peripheral]** — No clinical deployment procedures. Portable patterns for regulated/latency-sensitive domains:

- **SLO/goodput framing** — clinical chat or decision-support needs explicit TTFT/TPOT targets, not average latency alone.
- **Batch vs online** — offline chart summarization vs real-time CDS mirrors chapter's API split.
- **Quality degradation risk** — provider-specific optimization (Fig. 9-8) parallels validating model behavior across serving stacks in clinical AI.
- **Cost/throughput trade-offs** — capacity planning for high-volume screening workflows.

Not a substitute for Simon/Aliferis or NAM gen-AI health canon on clinical validation.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **ai_engineering_2025 Ch. 2** | High | Prefill/decode, autoregression, attention basics |
| **ai_engineering_2025 Ch. 7** | High | Quantization as primary compression lever |
| **ai_engineering_2025 Ch. 8** | Medium | Distillation cross-ref only |
| **hands_on_llms_2024** | Medium | Serving tutorials — use for code, AIE for strategy |
| **designing_ml_systems_2022** | Medium | ML serving, batching intuition |
| **understanding_distributed_systems_2022 / ddia** | Low | Parallelism/replica concepts at systems layer |
| **grokking / Ousterhout** | None meaningful | |

**Dedup guidance:** Treat **TTFT/TPOT decomposition**, **MFU/MBU definitions**, **KV cache formula**, and **continuous batching vs disaggregated prefill/decode** as canonical; other ingests should cross-link rather than re-derive.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — cost arithmetic, MBU calculation, KV sizing, prompt-cache ROI |
| Exercise hooks | **Weak in-chapter** — operator-authored drills required |
| Chapter boundary | **Clean** — closes adaptation arc; explicit Ch. 10 handoff |
| Citation density | **High** — Roofline, Orca, FlashAttention, DistServe, Anthropic caching, etc. |
| Anchor density | **High** for metrics and techniques; figures degraded in text export |
| Complement need | **Conditional** — pair with Hands-On LLMs for serving implementation |

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 1e, ©2025, Dec 2024 release; ≤5 years |
| **Author authority** | **PASS** | Chip Huyen; O'Reilly textbook; production ML/AI engineering pedigree |
| **Primary-source citation density** | **PASS** | Williams (Roofline), Yu (Orca), Dao (FlashAttention), Kwon (PagedAttention), Zhong (DistServe), Chowdhery (MFU/PaLM), vendor benchmarks |
| **Contested claims flagged** | **PASS** | Memory-bound terminology ambiguity; nvidia-smi utilization misleading; peak FLOP/s "hacking" (fn ¹²); pruning less common in practice; PyTorch Llama-7B quality impact unclear; Cerebras provider variance experiment |
| **Worked examples (procedural chapter)** | **PASS** | Multiple quantitative examples (cost, MBU, KV cache, prompt caching Table 9-3) |

**Overall TEXTBOOK-Q1:** **PASS** — suitable foundation-track ingest for inference strategy; operator should treat vendor pricing/caching numbers as time-stamped (Gemini/Anthropic "as of writing") and validate MFU/MBU with own profiling.

---

## Provenance anchors (sample)

| claim-id | claim | relation | section-anchor | text lines |
|----------|-------|----------|----------------|------------|
| AIE-C09-001 | Inference optimization spans model, hardware, service levels | compressed | intro | 18097–18117 |
| AIE-C09-002 | Prefill compute-bound; decode memory bandwidth-bound | compressed | Computational bottlenecks | 18239–18256 |
| AIE-C09-003 | Batch APIs ~50% cost vs online (Gemini/OpenAI as of writing) | compressed | Online and batch | 18288–18295 |
| AIE-C09-004 | Total latency ≈ TTFT + TPOT × output tokens | quoted | Latency metrics | 18394 |
| AIE-C09-005 | Goodput = requests meeting SLO, not raw throughput | compressed | Goodput | 18505–18518 |
| AIE-C09-006 | MFU/MBU preferred over nvidia-smi GPU utilization | compressed | Utilization | 18526–18558 |
| AIE-C09-007 | Inference up to 90% of deployed ML cost (Desislavov) | compressed | Accelerators | 18686–18690 |
| AIE-C09-008 | Speculative decoding: draft proposes, target verifies parallel | compressed | Speculative decoding | 19000–19055 |
| AIE-C09-009 | KV cache 500B model can reach 3 TB (Pope et al.) | compressed | KV cache | 19203–19206 |
| AIE-C09-010 | Character.AI >20× KV reduction via attention designs | compressed | Attention redesign | 19279–19287 |
| AIE-C09-011 | Continuous batching (Orca) returns completed responses immediately | compressed | Batching | 19492–19500 |
| AIE-C09-012 | Prefill/decode disaggregation improves throughput under SLO | compressed | Decoupling | 19520–19529 |
| AIE-C09-013 | Prompt cache: 1K system × 1M calls ≈ 1B tokens/day saved | compressed | Prompt caching | 19562–19566 |

---

## Recap bullets (chapter-authored)

- Inference cost/latency determine usability; metrics before optimization (19688–19693).
- TTFT tied to prefill; TPOT to decode; throughput tied to cost; latency/throughput trade-off (19695–19704).
- Hardware choice constrains optimization; accelerator overview provided (19706–19708).
- Model-level optimization may change behavior; service-level keeps model intact (19718–19722).
- Transformer bottlenecks: attention (KV cache, kernels) and autoregressive decoding (19724–19732).
- Service techniques: batching, prefill/decode decoupling, prompt caching, parallelism (19734–19737).
- Technique choice workload-dependent; top four: quantization, tensor parallelism, replica parallelism, attention optimization (19739–19755).

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
