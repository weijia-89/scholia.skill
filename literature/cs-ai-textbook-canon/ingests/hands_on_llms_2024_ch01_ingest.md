# Chapter ingest — Hands-On Large Language Models, Chapter 1

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | An Introduction to Large Language Models |
| **authors** | Jay Alammar, Maarten Grootendorst |
| **edition** | 1st Edition (2024) |
| **ISBN_print** | 9781098150952 |
| **ISBN_electronic** | not stated in chapter slice (O'Reilly print ISBN in manifest) |
| **chapter_number** | 1 |
| **page_range** | not marked in text export; chapter spans lines 511–1598 (chapter 2 begins line 1599) |
| **parent_book_title** | Hands-On Large Language Models |
| **publisher** | O'Reilly Media |
| **year** | 2024 |

## Scope

Chapter 1 is the book’s conceptual scaffold and first code touchpoint. It defines **Language AI** (interchangeable with NLP in practice), narrates a compressed history from **bag-of-words** through **word2vec**, **RNN encoder–decoder attention**, the **Transformer** (“Attention is all you need,” 2017), **BERT** (encoder-only / representation models), and **GPT** (decoder-only / generative models). It widens the book’s definition of **LLM** beyond decoder-only giants to include smaller representation models runnable on consumer hardware.

The chapter covers the **pretrain → fine-tune** training paradigm vs one-step classical ML; application patterns (classification, clustering, RAG, agents, multimodal); **responsible development** (bias, transparency, harmful content, IP, regulation); **GPU-poor** positioning (Colab T4, 16 GB VRAM minimum); **proprietary API** vs **open-weight** models and framework choices (Hugging Face Transformers, llama.cpp, LangChain); and **first generation** with **Phi-3-mini** via `pipeline`.

Sections in slice: opening motivation (GPT-2, ChatGPT); What Is Language AI; A Recent History of Language AI (bag-of-words, embeddings, RNN/attention, Transformer, BERT, GPT, 2023 generative wave, moving LLM definition); Training Paradigm; Applications; Responsible LLM Development; Limited Resources; Interfacing (closed/open, frameworks); Generating Your First Text; Summary. Footnotes ¹–¹⁶ cite McCarthy, Sebastiani, Mikolov, Bahdanau, Vaswani, Devlin, Radford, Brown, OpenAI GPT-4, Mamba/RWKV, Llama 2, Phi-3.

Out of scope: tokenization depth (ch.2), Transformer internals (ch.3), classification workflows (ch.4+), fine-tuning detail (ch.11–12).

## Key findings

All quotes **[verified from text]** from lines 511–1598 of the corpus export.

### Framing and chapter questions

- 2023 framed as transformative for **Language AI**; book scaffolds fundamentals and answers: what is Language AI, what are LLMs, use cases, and how to use them. (lines 534–558)
- **Language AI** encompasses non-LLM technologies (e.g., retrieval augmenting LLMs in ch.8). > "We use the term Language AI to encompass technologies that technically might not be LLMs but still have a significant impact on the field" (lines 591–593)

### Historical stack (representation → generation)

- **Bag-of-words:** tokenization → vocabulary → count vectors; still relevant (ch.5). (lines 622–664)
- **word2vec (2013):** semantic embeddings via neural nets; static "bank" ambiguity motivates context. (lines 666–768)
- **RNN encoder–decoder + attention (2014):** sequential, hard to parallelize; attention amplifies relevant input signals. (lines 770–836)
- **Transformer (2017):** attention-only, parallel training; encoder/decoder stacks, self-attention, masked decoder positions. (lines 838–901)
- **BERT (2018):** encoder-only; [CLS] for classification; **masked language modeling**; transfer learning / feature extraction without task fine-tune. (lines 903–976)
- **GPT-1+:** decoder-only; scale GPT-1 117M → GPT-2 1.5B → GPT-3 175B; **context length**; instruct/chat fine-tune. (lines 978–1037)
- Book’s **expanded LLM definition:** includes non-generative and sub-1B models on consumer hardware. > "to us, 'large language models' are also models that do not generate text and can be run on consumer hardware" (lines 1098–1105)

### Training, applications, ethics, access

- **Two-step LLM training:** (1) pretraining / language modeling → foundation/base model; (2) fine-tuning / post-training for tasks or instruction-following. Llama 2 cited at **2 trillion tokens**. (lines 1107–1151)
- Application vignettes map to later chapters: supervised/unsupervised classification, semantic search/RAG, prompt engineering + tools, multimodal (ch.9). (lines 1153–1195)
- **Responsible usage** flags: training-data bias opacity, human-vs-LLM transparency (medical-device regulation example), hallucination/fake news, IP uncertainty, **European AI Act**. (lines 1197–1240)
- **GPU-poor** audience: Colab free T4 **16 GB VRAM** minimum; Llama 2 training cost anecdote (> $5M at $1.50/hr × 3.3M GPU-hours). (lines 1242–1272)
- **Closed models:** API access, no self fine-tune, data leaves premises; **open models:** local control, license caveats ("ongoing discussions" on true open source). Authors prefer open where possible. (lines 1284–1361)
- Framework focus: backend packages (Transformers, llama.cpp, LangChain); GUI chat UIs named as tips only. (lines 1363–1397)

### First code: Phi-3-mini

- Canonical generative model: **microsoft/Phi-3-mini-4k-instruct** (3.8B params, MIT license, <8 GB VRAM; quantization <6 GB). (lines 1414–1427)
- Load model + tokenizer; `pipeline("text-generation", …)` with `return_full_text=False`, `max_new_tokens`, `do_sample=False` (greedy); chat messages `role`/`content`. (lines 1429–1516)

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/hands_on_llms_2024.txt` |
| **lines_read** | 511–1598 (inclusive) |
| **chapter_boundary** | Starts line 511 (`Chapter 1. An Introduction to Large Language Models`); ends line 1598 (footnote ¹⁶ before `Chapter 2` at 1599) |
| **wrong_file_flag** | false |
| **adjacent_chapter_bleed** | none ingested (ch.2 heading excluded) |
| **figure_placeholders** | Many `[]` image placeholders; pedagogical content in prose and figure captions |

## Pedagogy

### learning_objectives

Explicit chapter questions (lines 549–558):

1. What is Language AI?
2. What are large language models?
3. What are common use cases and applications?
4. How can we use LLMs ourselves?

Implicit objectives evidenced in text:

- Distinguish **representation** (encoder-only, embeddings, teal icon) vs **generative** (decoder-only, pink icon) models.
- Trace historical motivations for attention and Transformers.
- Contrast **pretrain/fine-tune** vs single-task ML training.
- Choose **API vs local** deployment with tradeoffs (cost, privacy, fine-tuning).
- Run first **Hugging Face** generation with Phi-3 and understand tokenizer coupling.

### worked_examples_present

**Y**

| Example | Lines (approx.) | Role |
|---------|-----------------|------|
| Bag-of-words two-sentence vocabulary | 628–660 | Representation models |
| word2vec neighbor learning / "apple" vs "baby" properties | 688–727 | Embeddings intuition |
| English→Dutch RNN translation + attention | 776–832 | Context before Transformers |
| Transformer encoder/decoder block diagram narrative | 848–896 | Architecture primer |
| BERT MLM + fine-tune for classification | 927–949 | Transfer learning |
| GPT scale ladder + context window | 987–1037 | Generative LLMs |
| Phi-3 `AutoModelForCausalLM` + pipeline chicken joke | 1447–1516 | Executable first generation |

### exercise_hooks

No numbered end-of-chapter exercises. Scholía hooks:

| ID | Prompt (derived) | Scholía hook |
|----|------------------|--------------|
| hotl-ch01-1 | Map a use case (support bot, doc QA, sentiment) to book chapter refs in applications list | Curriculum routing card |
| hotl-ch01-2 | List three risks from Responsible LLM section for a regulated domain | Ethics gate |
| hotl-ch01-3 | API vs open-weight: decide for patient notes vs public blog drafting | Deployment decision |
| hotl-ch01-4 | Reproduce Phi-3 pipeline; vary `do_sample` / `max_new_tokens` | Bridges to ch.6 sampling |
| hotl-ch01-5 | Explain why static word2vec fails on polysemy ("bank") | Motivation for ch.2 contextual embeddings |

GitHub book repository referenced at book level for Colab notebooks (outside slice).

## Operator hooks

### Foundation layer

**w1_foundation procedural complement** to AI Engineering 2025 (framework spine). This chapter supplies:

- **Visual history** of Language AI (bag-of-words → Transformer → BERT/GPT) that AIE ch.1 summarizes more abstractly.
- **Representation vs generative** taxonomy reused in ch.4–12.
- **Pretrain/fine-tune** and **foundation model** vocabulary aligned with AIE adaptation triad.
- **Hands-on stack anchor:** Hugging Face Hub, Transformers, Phi-3, Colab GPU-poor defaults — the tutorial path AIE defers to manifest `ingest_note`.

Without this chapter, later Hands-on chapters (tokens, internals, classification) lack shared iconography and historical motivation.

### MDCalc alignment

**[peripheral]**

- **Regulated deployment:** medical-field LLM apps "might be regulated as medical devices" (lines 1215–1217) — pattern-portable, not clinical workflow detail.
- **Transparency / human-in-the-loop:** undisclosed LLM-in-human-interaction risk (lines 1211–1215).
- No agents, trace tooling, or MDCalc-specific observability. NAM/Aliferis and LangSmith/Langfuse snapshots cover clinical/ops layers.

### Redundancy

| Canon title | Overlap | Gap / distinction |
|-------------|---------|-------------------|
| **AI Engineering 2025** | LM/LLM definitions, foundation models, pretrain/fine-tune, application patterns | AIE = planning/eval spine; Hands-on ch.1 = illustrated history + first code |
| **Grokking Algorithms 2e** | None substantive | No asymptotic analysis |
| **Philosophy of Software Design 2e** | Complexity/theme only distant | No design methodology |
| **Prompt Engineering for LLMs 2024** | Forward refs to prompt engineering (ch.6) | PE book not in history tour |
| **DDIA / UDS / Kästner** | Scale/cost motifs | Systems/ops assume LM literacy from here or AIE |

**Verdict:** Medium overlap with **AIE ch.1** — Hands-on is the designated **tutorial + visual history** slot; dedupe in SYNTHESIS by routing code paths here.

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| **Worked examples** | Y — narrative figures + Phi-3 pipeline |
| **Exercise hooks** | Moderate — tips and forward refs; no numbered drills |
| **Chapter boundary** | Clean — self-contained overview ending in Summary |
| **Anchor density** | High — dated milestones, parameter counts, cited papers in footnotes |
| **Ingest suitability** | Strong seed for timeline cards, repr vs gen taxonomy, API/local matrix |

## TEXTBOOK-Q1 gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** (≤5 y) | **PASS** | 2024 O'Reilly; Phi-3, GPT-4, Mamba/RWKV footnotes |
| **Author authority** | **PASS** | Alammar (Illustrated Transformer ecosystem); Grootendorst (BERTopic); O'Reilly tier |
| **Primary-source citation density** | **PASS** | 16 footnoted papers/reports in slice (Vaswani, Devlin, Brown, Touvron, etc.) |
| **Contested claims flagged** | **PASS** | "Open source" licensing debate noted; LLM definition explicitly provisional; hallucination/factuality limits foreshadow RAG (ch.8) |
| **Worked examples (procedural)** | **PASS** | Full Phi-3 load/generate walkthrough |

**TEXTBOOK-Q1 overall: PASS**

---

*Ingest agent: hotl-ingest-ch01-04 · hands_on_llms_2024 ch01 · lines 511–1598 · word cap ≤4500*
