# Chapter ingest — `hands_on_llms_2024` · Chapter 10

**Corpus:** cs-ai-textbook-canon · **Slug:** hands_on_llms_2024 · **Wave:** w1_foundation  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/hands_on_llms_2024_ch10_ingest.md`

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
| **chapter_number** | 10 |
| **chapter_title** | Creating Text Embedding Models |
| **page_range** | Not present in text export; logical span `Chapter 10. Creating Text Embedding Models` (line 10485) through `Summary` + footnotes before Ch. 11 (line 11980) |

---

## scope

Chapter 10 is the **procedural spine for training and fine-tuning text embedding models** via contrastive learning and sentence-transformers: from scratch training on MNLI, loss-function comparison, supervised fine-tuning, Augmented SBERT, and unsupervised TSDAE with domain adaptation.

**Major arcs within assigned slice (lines 10485–11980):**

1. **Embedding models recap** — semantic vs task-specific similarity (sentiment); steering via training examples (lines 10504–10559).
2. **Contrastive learning** — similar close, dissimilar far; contrastive explanation analogy; word2vec as early contrastive NLP (lines 10565–10630).
3. **SBERT architecture** — cross-encoder overhead (n·(n−1)/2 pairs); bi-encoder/Siamese + mean pooling; softmax on concatenated embeddings (lines 10636–10701).
4. **Creating from scratch** — MNLI 50k subset from GLUE; `bert-base-uncased`; SoftmaxLoss; STSB evaluator; `SentenceTransformerTrainer` + fp16 (lines 10707–10936).
5. **MTEB evaluation** — 8 tasks, 58 datasets, 112 languages; Banking77Classification example (lines 10945–10986).
6. **Loss functions** — CosineSimilarityLoss (0.72 Pearson vs 0.59 softmax); MNR/InfoNCE (0.80); easy vs hard negatives; larger batch helps MNR (lines 10999–11323).
7. **Supervised fine-tuning** — `all-MiniLM-L6-v2` + MNR → 0.85 Pearson; data quality > size (lines 11325–11453).
8. **Augmented SBERT** — cross-encoder on 10k gold → silver labels on 40k pairs → bi-encoder; 0.71 with 20% data vs 0.72 full (lines 11455–11683).
9. **Unsupervised TSDAE** — denoising auto-encoder; [CLS] pooling; 0.70 on STSB without labels; domain adaptation pipeline (lines 11685–11904).
10. **Summary** — forward to Ch. 11 representation fine-tuning (lines 11906–11980).

**Prerequisites cited:** Ch. 2 (word2vec), Ch. 4–5–8 (embedding applications), Ch. 9 (CLIP contrastive foreshadow).

**Manifest note:** Executable complement to `ai_engineering_2025` Ch. 6 RAG/embedding framing and Ch. 3 eval — owns training notebooks.

---

## key_findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

### Embeddings and contrastive learning

- Embedding models map text → vectors capturing semantic (or task-specific) similarity (lines 10511–10559).
- Contrastive learning: teach similarity/dissimilarity through positive/negative pairs; contrastive explanation ("Why P and not Q?") motivates design (lines 10567–10613).
- word2vec is an early contrastive NLP example (neighbor vs random negatives) (lines 10620–10630).

### SBERT and bi-encoders

- Cross-encoder BERT: two sentences jointly scored — accurate but O(n²) for corpus comparison; no standalone embeddings (lines 10646–10655).
- Mean-pooling BERT outputs worse than GloVe averages per Reimers & Gurevych citation (lines 10657–10659).
- sentence-transformers: Siamese bi-encoder, mean pooling, contrastive optimization — fast embeddings for semantic search (lines 10665–10701).

### Training from scratch (baseline ladder)

| Loss / setup | STSB pearson_cosine (reported) | Anchor |
|--------------|-------------------------------|--------|
| SoftmaxLoss, bert-base-uncased, MNLI 50k | 0.598 | 10920–10935 |
| CosineSimilarityLoss | 0.722 | 11127–11140 |
| MNR loss | 0.809 | 11257–11269 |
| Fine-tune all-MiniLM-L6-v2 + MNR | 0.851 | 11418–11428 |
| Augmented SBERT (10k gold + silver) | 0.710 | 11660–11673 |
| TSDAE unsupervised | 0.699 | 11856–11867 |

- Smaller datasets increase training instability; prefer larger quality data when possible (lines 10752–10755).
- Default: all LLM layers trainable in sentence-transformers; freezing generally not advised (lines 10801–10806).
- MNLI labels: 0=entailment, 1=neutral, 2=contradiction; used for positives/negatives (lines 10760–10775).
- MNR triplets: anchor + positive (entailment) + in-batch negative; 50k MNLI → 16,875 entailment rows (lines 11172–11199).
- Hard negatives (topic-related wrong answers) improve MNR vs easy random negatives (lines 11279–11320).
- Main training difficulty: **curating quality pairs**, especially hard negatives (lines 11445–11450).

### Augmented SBERT

- Four steps: fine-tune cross-encoder on gold → create unlabeled pairs → cross-encoder silver labels → train bi-encoder on gold+silver (lines 11474–11485).
- Silver pair generation tip: semantic search top-k better than random cross-pairing (lines 11566–11573).
- 20% labeled data + augmentation ≈ full-data cosine loss (0.71 vs 0.72) (lines 11671–11673).

### TSDAE and domain adaptation

- TSDAE: delete words → encoder embedding → decoder reconstructs full sentence; decoder discarded at inference (lines 11698–11723).
- [CLS] pooling preferred over mean for TSDAE (position info) (lines 11783–11795).
- `DenoisingAutoEncoderLoss` with tied encoder-decoder weights (lines 11797–11816).
- Unsupervised generally beaten by supervised; TSDAE useful for **domain adaptation** before supervised fine-tune (lines 11870–11904).
- Adaptive pretraining: TSDAE/MLM on target domain → fine-tune on in/out-domain labeled data (lines 11888–11895).

---

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Chapter opener + embedding recap | read | 10485–10559 |
| Contrastive learning theory | read | 10565–10630 |
| SBERT / bi-encoder vs cross-encoder | read | 10636–10701 |
| MNLI data + train from scratch (SoftmaxLoss) | read | 10707–10936 |
| MTEB evaluation | read | 10945–10997 |
| CosineSimilarityLoss | read | 11022–11140 |
| MNR loss + hard negatives | read | 11145–11323 |
| Supervised fine-tune (MiniLM) | read | 11325–11453 |
| Augmented SBERT | read | 11455–11683 |
| TSDAE unsupervised | read | 11685–11868 |
| TSDAE domain adaptation | read | 11870–11904 |
| Summary + footnotes ¹–¹³ | read | 11906–11979 |
| Chapter 11 opener | **deferred** | 11981+ (outside scope) |

- **Lines read:** 10485–11980 (full parent-requested range)
- **wrong_file_flag:** false
- **Amnesiac attestation:** Metrics and claims trace to line ranges in `hands_on_llms_2024.txt`

---

## pedagogy

### learning_objectives

Implicit from chapter arc:

- Explain contrastive learning and why bi-encoders beat cross-encoders at scale
- Train a sentence embedding model from scratch with sentence-transformers
- Compare Softmax, cosine similarity, and MNR losses on STSB
- Fine-tune a pretrained embedding model on domain pairs
- Apply Augmented SBERT when labeled data is scarce
- Run TSDAE for unsupervised/domain-adaptive embeddings

### worked_examples_present

**Y**

| Example | Skill taught | Anchor |
|---------|--------------|--------|
| MNLI entailment row | Positive pair structure | 10770–10778 |
| SoftmaxLoss training + STSB 0.59 | Baseline trainer setup | 10808–10935 |
| MTEB Banking77Classification | Beyond-STSB eval | 10959–10976 |
| Cosine loss label mapping | NLI → [0,1] similarity | 11062–11068 |
| MNR triplet construction | Anchor/positive/negative | 11172–11196 |
| MiniLM fine-tune 0.85 | Pretrained base advantage | 11383–11428 |
| Augmented SBERT gold/silver | Cross-encoder labeling | 11509–11673 |
| TSDAE damaged sentence pair | Unsupervised denoising | 11764–11765 |

### exercise_hooks

| ID | Prompt summary | Operator extension | Anchor |
|----|----------------|-------------------|--------|
| 10.LOSS-1 | Loss ladder replication | Reproduce softmax/cosine/MNR table on same 50k split | 10920–11269 |
| 10.MNR-1 | Batch size sweep | Increase per_device_train_batch_size; plot STSB vs batch | 11271–11277 |
| 10.HN-1 | Hard negative mining | Add semi-hard negatives via embedding retrieval; compare MNR | 11305–11320 |
| 10.ASBERT-1 | Silver quality audit | Train bi-encoder gold-only vs gold+silver; measure delta | 11677–11680 |
| 10.TSDAE-1 | Domain corpus | Run TSDAE on operator domain text → supervised fine-tune | 11870–11904 |
| 10.MTEB-1 | Task selection | Run one MTEB classification + one clustering task on final model | 10951–10976 |

---

## Operator hooks

### 1. Foundation layer (w1_foundation)

Chapter 10 is the **canon executable path for embedding model training** in cs-ai-textbook-canon:

- **Contrastive loss selection** — MNR default for pair data; cosine for graded similarity
- **STSB quick eval** — chapter's internal benchmark; MTEB for production comparison
- **Domain adaptation** — TSDAE → supervised fine-tune pipeline before RAG index rebuild
- **Pairs with Ch. 9 CLIP** — same contrastive principle, text-only depth here

### 2. MDCalc alignment

**[none]** — No clinical workflow. Pattern-portable: embedding quality gates retrieval for clinical note search; operator must validate on domain corpora separately.

### 3. Redundancy

| Overlap with | Relationship |
|--------------|--------------|
| `hands_on_llms_2024` Ch. 4 | Frozen embedding classification; Ch. 10 trains the embedder |
| `hands_on_llms_2024` Ch. 9 | CLIP multimodal contrastive; Ch. 10 text-only training |
| `ai_engineering_2025` Ch. 6 | AIE owns RAG architecture/eval; HOTL owns embedding training code |
| `ai_engineering_2025` Ch. 3 | MTEB/leaderboard overlap with AIE eval vocabulary |

**Dedup rule:** Use this ingest for **training/fine-tuning embeddings**; use AIE Ch. 6 for retrieval system design and cost.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | Strong Y — full training ladder with reported metrics |
| Exercise hooks | Operator extensions |
| Chapter boundary | Clean — ends 11979; Ch. 11 at 11981 |
| Citation density | High (SBERT, MTEB, Augmented SBERT, TSDAE, SimCSE, GPL) |
| Child-skill potential | `scholia.embedding-loss-router`, `scholia.tsdae-domain-adapt` |

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | 2024 1e |
| Author authority | **PASS** | sentence-transformers ecosystem authors |
| Primary-source citation density | **PASS** | Reimers SBERT, Muennighoff MTEB, Wang TSDAE, Thakur Augmented SBERT |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Runnable notebooks with metric table |

### Contested or oversimplified claims (not smoothed)

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Cross-encoder always better than bi-encoder | 10696–10697 | Accuracy vs speed trade-off |
| MiniLM 0.85 on 50k MNLI redundant | 11429–11433 | Demo artifact; base already saw full MNLI |
| TSDAE 0.70 "impressive" without labels | 11867–11868 | STSB-only; may not transfer to retrieval |
| Larger batch always helps MNR | 11271–11277 | GPU/memory constrained in practice |

**TEXTBOOK-Q1 chapter verdict:** **PASS** — core w1_foundation procedural ingest for embedding training.

---

## Glossary (chapter-local)

| Term | Definition per text |
|------|---------------------|
| Contrastive learning | Train embeddings so similar documents are close, dissimilar far apart |
| Cross-encoder | Model scoring two sentences jointly; no standalone embeddings |
| Bi-encoder / SBERT | Sentence-transformer producing independent embeddings per sentence |
| MNLI | Multi-Genre NLI — entailment/neutral/contradiction sentence pairs |
| STSB | Semantic Textual Similarity Benchmark — human scores 1–5 |
| MTEB | Massive Text Embedding Benchmark — multi-task embedding evaluation |
| MNR loss | Multiple negatives ranking — classify positive vs in-batch negative pairs |
| Hard negative | Similar but incorrect answer; harder than random unrelated text |
| Augmented SBERT | Cross-encoder labels silver data to expand bi-encoder training |
| TSDAE | Transformer-based Sequential Denoising Auto-Encoder for unsupervised embeddings |
| Domain adaptation | Adapt general embeddings to target-domain vocabulary via unsupervised pretrain |

---

## Reciprocal index pointers

- **Prerequisites:** Ch. 2 (word2vec), Ch. 4 (embedding classification/search), Ch. 9 (CLIP contrastive)
- **Forward:** Ch. 11 (BERT classification fine-tune, SetFit, MLM); Ch. 4 dense retrieval fine-tune (index cites)
- **External depth:** sentence-transformers loss docs; MTEB leaderboard; TSDAE paper
