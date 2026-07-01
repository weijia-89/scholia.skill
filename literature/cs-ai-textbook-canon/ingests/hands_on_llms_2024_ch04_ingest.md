# Chapter ingest — Hands-On Large Language Models, Chapter 4

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Text Classification |
| **authors** | Jay Alammar, Maarten Grootendorst |
| **edition** | 1st Edition (2024) |
| **ISBN_print** | 9781098150952 |
| **ISBN_electronic** | not stated in chapter slice |
| **chapter_number** | 4 |
| **page_range** | not marked in text export; chapter spans lines 4061–4977 (chapter 5 begins line 4978) |
| **parent_book_title** | Hands-On Large Language Models |
| **publisher** | O'Reilly Media |
| **year** | 2024 |

## Scope

Chapter 4 opens **Part II: Using Pretrained Language Models** with **supervised sentiment classification** on the **rotten_tomatoes** dataset (binary positive/negative; 8530 train / 1066 test). It compares **representation** vs **generative** approaches:

**Representation models:**
- **Task-specific** pipeline (`cardiffnlp/twitter-roberta-base-sentiment-latest`) — F1 **0.80** weighted.
- **Embedding + classifier:** `sentence-transformers/all-mpnet-base-v2` + logistic regression — F1 **0.85**.
- **Zero-shot** via label-description embeddings + cosine similarity — F1 **0.78** without labels.

**Generative models:**
- **Flan-T5-small** (`text2text-generation`) with prompt prefix — F1 **0.84**.
- **GPT-3.5-turbo-0125** via OpenAI API — F1 **0.91** (data-contamination caveat).

Includes model-selection guidance (MTEB leaderboard, BERT family timeline), metrics pedagogy (precision/recall/F1, confusion matrix), and tips (TF-IDF+logistic baseline, API cost/rate limits, embedding APIs for CPU).

Out of scope: fine-tuning BERT (ch.11), embedding model training (ch.10), unsupervised clustering (ch.5).

## Key findings

All quotes **[verified from text]** from lines 4061–4977.

### Task framing

- Classification assigns a **label/class** to input text — sentiment, intent, NER, language detection. (lines 4063–4073)
- Chapter uses **pretrained frozen** models; fine-tuning deferred to ch.11. (lines 4090–4185)
- Tip: compare against **TF-IDF + logistic regression** baseline. (lines 4104–4109)

### Dataset

- `load_dataset("rotten_tomatoes")` — 5331 pos + 5331 neg reviews; labels 0/1. (lines 4111–4162)

### Representation — task-specific

- Model: **Twitter-RoBERTa-base-sentiment** (tweet-trained, not movie domain). (lines 4239–4270)
- `pipeline(..., return_all_scores=True)`; map negative vs positive scores with `argmax`. (lines 4298–4304)
- **Weighted F1 = 0.80** on test. (lines 4324–4376)
- Improvement paths: domain SST-2 DistilBERT; or embedding route. (lines 4378–4383)

### Representation — embeddings + classifier

- Two-step: frozen embedding model → train **logistic regression** on CPU. (lines 4384–4468)
- Embeddings shape **(8530, 768)**. (lines 4432–4448)
- **Weighted F1 = 0.85**. (lines 4473–4490)
- Tip: external embedding APIs (Cohere, OpenAI) for CPU-only pipeline. (lines 4492–4499)

### Zero-shot with embeddings

- Label strings embedded: "A negative review" / "A positive review"; **cosine similarity** to documents. (lines 4501–4564)
- **Weighted F1 = 0.78** with no labeled training data. (lines 4566–4594)
- Tip: refine label text to "A very negative/positive **movie** review". (lines 4596–4604)
- Note: NLI zero-shot exists but chapter demonstrates **embedding flexibility**. (lines 4582–4590)

### Generative — Flan-T5

- Encoder–decoder **T5** text-to-text; Flan-T5 instruction-tuned on 1000+ tasks. (lines 4638–4680)
- Prompt: `"Is the following sentence positive or negative? "` + review. (lines 4703–4709)
- Map generated "negative"/"positive" → 0/1; **F1 = 0.84**. (lines 4732–4759)

### Generative — ChatGPT

- Instruction tuning + **preference ranking** overview (figures 4-22, 4-23); detail in ch.12. (lines 4761–4796)
- OpenAI API client; system + user messages; `temperature=0`. (lines 4810–4837)
- Classification prompt requests **1/0 only**; test set ~**3 cents** on gpt-3.5-turbo-0125 at writing. (lines 4843–4864)
- Rate limits → exponential backoff tip. (lines 4866–4880)
- **Weighted F1 = 0.91** — but > "we cannot easily use these kinds of metrics" due to unknown training data overlap. (lines 4900–4916)

### Metrics pedagogy

- **Precision**, **recall**, **accuracy**, **F1** defined via confusion matrix framing. (lines 4336–4373)
- Book standard: **weighted average F1** for class balance. (lines 4372–4375)

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/hands_on_llms_2024.txt` |
| **lines_read** | 4061–4977 (inclusive) |
| **chapter_boundary** | Starts line 4061 (`Chapter 4. Text Classification`); ends line 4977 (footnote ⁸ before ch.5 at 4978) |
| **wrong_file_flag** | false |
| **adjacent_chapter_bleed** | Part II header line 4059 outside slice; ch.5 excluded |
| **figure_placeholders** | Multiple `[]`; metric figures described in prose |

## Pedagogy

### learning_objectives

From chapter outline (lines 4075–4102) and summary (lines 4921–4950):

1. Load and inspect a Hugging Face **datasets** classification benchmark.
2. Run a **task-specific encoder** pipeline for sentiment.
3. Build **embedding features + classical classifier** without fine-tuning LM.
4. Perform **zero-shot** classification via label embeddings.
5. Use **encoder–decoder** (Flan-T5) and **decoder-only API** (GPT-3.5) for classification via prompting.
6. Evaluate with **classification_report** / weighted F1 and interpret precision/recall tradeoffs.

### worked_examples_present

**Y**

| Example | Lines (approx.) | Role |
|---------|-----------------|------|
| `rotten_tomatoes` load + label inspect | 4123–4162 | Data plumbing |
| Twitter-RoBERTa pipeline batch inference | 4259–4334 | Task-specific encoder |
| SentenceTransformer + LogisticRegression | 4426–4485 | Embedding classifier |
| Zero-shot cosine similarity labels | 4535–4580 | Label-only supervision |
| Flan-T5 text2text with prompt prefix | 4687–4756 | Seq2seq classification |
| OpenAI `chatgpt_generation` + batch eval | 4810–4910 | Closed API classification |

### exercise_hooks

| ID | Prompt (derived) | Scholía hook |
|----|------------------|--------------|
| hotl-ch04-1 | Replicate TF-IDF+logistic baseline vs embedding F1 | Strong baseline discipline |
| hotl-ch04-2 | Swap Twitter-RoBERTa for SST-2 DistilBERT; compare F1 | Domain transfer |
| hotl-ch04-3 | Tune label description strings for zero-shot | Prompt/label engineering |
| hotl-ch04-4 | Cost-estimate API classification for N=10k reviews | Production economics |
| hotl-ch04-5 | Plot confusion matrix for worst method; analyze errors | Error analysis |
| hotl-ch04-6 | Try `flan-t5-large` vs small — accuracy/latency tradeoff | Model selection |

Tips in text are explicit exercise-like prompts (label wording, skip API to save credits).

## Operator hooks

### Foundation layer

**First Part II application chapter** — turns ch.1–3 concepts into **evaluated pipelines**. Establishes canon patterns:

- **Encoder vs generative** classification mechanics (logits vs generated text).
- **Frozen pretrained + lightweight head** — default GPU-poor path before ch.11 fine-tune.
- **Hugging Face** `datasets`, `pipeline`, `sentence-transformers`, OpenAI client — stack reused in ch.5–12.
- **Weighted F1** as book evaluation convention — aligns with later eval chapters and AIE evaluation themes.

Bridges to clinical/doc tracks only via generic classification/metrics literacy (not domain-specific).

### MDCalc alignment

**[peripheral]**

- **Eval metrics:** precision/recall/F1 pedagogy applicable to classifier components in agent pipelines.
- **API cost / rate limits:** production guardrails for closed models (lines 4859–4880).
- **Data leakage caveat** on GPT-3.5 benchmark scores — epistemic humility for eval (lines 4912–4916).
- No clinical NLP, PHI, or trace observability.

### Redundancy

| Canon title | Overlap | Gap / distinction |
|-------------|---------|-------------------|
| **AI Engineering 2025** | Classification as application pattern; eval importance | AIE conceptual; Hands-on ch.4 is full benchmark lab with scores |
| **Grokking Algorithms 2e** | None | — |
| **Philosophy of Software Design 2e** | None | — |
| **Simon/Aliferis healthcare** | Supervised classification theme | Healthcare book domain-specific; this is tutorial |
| **Prompt Engineering for LLMs 2024** | Prompt engineering for GPT classification | PE deeper on prompts; Hands-on compares 5 paradigms |

**Verdict:** Low–medium overlap with **AIE** application taxonomy — Hands-on owns **executable classification shootout**.

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| **Worked examples** | Y — five complete pipelines with reported F1 |
| **Exercise hooks** | Strong — tips + comparative methods |
| **Chapter boundary** | Clean |
| **Anchor density** | High — model IDs, metrics, costs |
| **Ingest suitability** | Excellent for method-selection decision table |

## TEXTBOOK-Q1 gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | gpt-3.5-turbo-0125, Flan-T5, MTEB reference |
| **Author authority** | **PASS** | O'Reilly hands-on tier |
| **Primary-source citation density** | **PASS** | Pang & Lee rotten_tomatoes; RoBERTa, Sentence-BERT, T5, Flan papers footnoted |
| **Contested claims flagged** | **PASS** | GPT-3.5 eval contamination uncertainty; NLI vs embedding zero-shot choice explained |
| **Worked examples** | **PASS** | End-to-end sklearn + HF + OpenAI |

**TEXTBOOK-Q1 overall: PASS**

---

*Ingest agent: hotl-ingest-ch01-04 · hands_on_llms_2024 ch04 · lines 4061–4977 · word cap ≤4500*
