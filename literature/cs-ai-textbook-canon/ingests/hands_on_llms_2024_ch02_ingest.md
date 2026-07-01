# Chapter ingest — Hands-On Large Language Models, Chapter 2

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Tokens and Embeddings |
| **authors** | Jay Alammar, Maarten Grootendorst |
| **edition** | 1st Edition (2024) |
| **ISBN_print** | 9781098150952 |
| **ISBN_electronic** | not stated in chapter slice |
| **chapter_number** | 2 |
| **page_range** | not marked in text export; chapter spans lines 1599–3122 (chapter 3 begins line 3123) |
| **parent_book_title** | Hands-On Large Language Models |
| **publisher** | O'Reilly Media |
| **year** | 2024 |

## Scope

Chapter 2 is the book’s **tokenization and embedding mechanics** chapter. It explains how LLMs see **token IDs** (not raw strings), tours **real pretrained tokenizers** (BERT uncased/cased, GPT-2, Flan-T5, GPT-4, StarCoder2, Galactica, Phi-3/Llama 2), and covers design axes: **BPE**, **WordPiece**, **SentencePiece**; vocabulary size; special tokens; domain-specific training data (code, science).

It links tokenizers to **embedding matrices** inside models, **contextualized token embeddings** (DeBERTa v3 example), **sentence/document text embeddings** (`sentence-transformers`), **word2vec** (skip-gram, negative sampling, contrastive framing), and a **playlist Word2Vec recommender** (Gensim on Cornell radio playlists).

Out of scope: full Transformer forward pass (ch.3), classification pipelines (ch.4), contrastive training depth (ch.10), RAG (ch.8).

## Key findings

All quotes **[verified from text]** from lines 1599–3122.

### Tokenization pipeline

- Models generate **one token at a time**; prompts are tokenized first. (lines 1624–1632)
- `input_ids` are integer sequences referencing tokenizer vocabulary; decode per-id shows subword splits (e.g., `apolog` + `izing`). (lines 1680–1779)
- Three tokenizer determinants: **method** (BPE, WordPiece), **design choices** (vocab size, special tokens), **training corpus**. (lines 1841–1859)

### Token granularity

- Schemes: **word**, **subword** (dominant), **character**, **byte** / tokenization-free (CANINE, ByT5). Subword ~3 chars/token → ~3× more text in 1K context vs character. (lines 1870–1937)
- GPT-2/RoBERTa include bytes as fallback but are not fully byte-level. (lines 1931–1937)

### Tokenizer tour (canonical test string)

Shared probe text exercises capitalization, emoji, CJK, Python `elif`/whitespace, numbers (lines 1954–1966). Highlights:

| Tokenizer | Notable behavior (from text) |
|-----------|------------------------------|
| BERT uncased | Lowercase; newlines dropped; `##` subwords; UNK for emoji/CJK |
| BERT cased | `CAPITALIZATION` → 8 subtokens |
| GPT-2 | Newlines kept; emoji via multi-byte tokens; whitespace matters for code |
| Flan-T5 | No newline/whitespace tokens; UNK emoji/CJK |
| GPT-4 | Whitespace runs up to 83 chars as single tokens; `elif` token; ~100K vocab |
| StarCoder2 | Per-digit tokens (`600` → `6 0 0`); repo/filename special tokens |
| Galactica | Citation/reasoning special tokens (`[START_REF]`, `<work>`) |
| Phi-3 / Llama 2 | Chat role tokens `<|user|>`, `<|assistant|>`, `<|system|>` |

> "A model that uses a single token to represent four consecutive whitespace characters is more tuned to a Python code dataset." (lines 2144–2150)

### Embeddings

- Model holds **vocab_size × embedding_dim** matrix; tokenizer and model are **paired** — cannot swap without retraining. (lines 2568–2587)
- **Contextualized** embeddings: DeBERTa v3 on "Hello world" → shape `[1, 4, 384]` with [CLS]/[SEP]. (lines 2612–2694)
- **Text embeddings:** `SentenceTransformer("all-mpnet-base-v2")` → 768-d vector per sentence. (lines 2699–2750)
- **word2vec:** skip-gram sliding window + **negative sampling** (noise-contrastive estimation); bridges to ch.10 contrastive training and ch.9 multimodal image–caption pairing. (lines 2798–2906)

### Recommendation system example

- Playlists as "sentences," songs as "tokens"; Gensim `Word2Vec` on Cornell YES Complete dataset; `vector_size=32`, `window=20`, `negative=50`. (lines 2914–3068)
- Demonstrates embeddings beyond NLP (nearest-neighbor recommendations for Billie Jean, 2Pac, Metallica).

### Factuality caveat

> "generation models alone aren't reliable search engines. This led to the rise of retrieval-augmented generation (RAG)" (lines 2563–2566)

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/hands_on_llms_2024.txt` |
| **lines_read** | 1599–3122 (inclusive) |
| **chapter_boundary** | Starts line 1599; ends line 3122 (footnote ¹ Sentence-BERT before ch.3 at 3123) |
| **wrong_file_flag** | false |
| **adjacent_chapter_bleed** | none |
| **figure_placeholders** | Multiple `[]`; tokenizer comparison table preserved in prose |

## Pedagogy

### learning_objectives

Implicit from chapter opening and summary (lines 1612–1620, 3070–3118):

1. Explain tokenization as mandatory pre/post-processing for LLM I/O.
2. Compare word/subword/character/byte schemes and tradeoffs for context length.
3. Interpret differences among production tokenizers (English, code, multilingual).
4. Relate tokenizer vocabulary to model embedding matrix.
5. Generate contextual token embeddings and sentence embeddings in code.
6. Describe word2vec skip-gram + negative sampling and transfer idea to recommenders.

### worked_examples_present

**Y**

| Example | Lines (approx.) | Role |
|---------|-----------------|------|
| Phi-3 email prompt → `input_ids` tensor + per-token decode | 1662–1826 | Token I/O loop |
| `show_tokens()` colored tokenizer tour | 1993–2438 | Comparative tokenizer lab |
| DeBERTa contextual embeddings `output.shape` | 2616–2694 | Encoder representations |
| `SentenceTransformer.encode` | 2729–2746 | Text embeddings |
| Gensim GloVe `most_similar('king')` | 2769–2796 | Static embeddings |
| word2vec Dune sentence sliding window | 2806–2864 | Training intuition |
| Playlist Word2Vec + `print_recommendations` | 2930–3068 | Cross-domain embeddings |

### exercise_hooks

| ID | Prompt (derived) | Scholía hook |
|----|------------------|--------------|
| hotl-ch02-1 | Tokenize a Python snippet with BERT vs GPT-4 tokenizer IDs (conceptual) | Code-tokenization literacy |
| hotl-ch02-2 | Estimate tokens for a 2K-word doc at ~3 chars/token vs character-level | Context budget |
| hotl-ch02-3 | Embed two paraphrases; compare cosine similarity | Embedding quality probe |
| hotl-ch02-4 | Improve zero-shot label strings exercise foreshadowed in ch.4 tip | Cross-chapter |
| hotl-ch02-5 | Train toy Word2Vec on custom "playlists" | Contrastive/recommender pattern |

Forward refs: ch.3 internals, ch.4 embedding model choice, ch.8 RAG, ch.9 multimodal, ch.10 contrastive, ch.11 fine-tuning tokenizers.

## Operator hooks

### Foundation layer

**Core w1_foundation implementation chapter** for token unit literacy (pairs with AIE ch.1 GPT-4 tokenization example). Establishes:

- **Token ≠ word** and **subword** as default for modern LLMs.
- **Tokenizer–model coupling** — production pitfall when swapping tokenizers.
- **Embedding types:** static (word2vec), contextual (encoder), document (sentence-transformers).
- **Code/science tokenizer specialization** — prerequisite for evaluating codegen and doc-ingest pipelines.

Feeds DDIA/RAG chapters (embedding search) and all Hands-on application parts.

### MDCalc alignment

**[none]**

Technical NLP/embeddings only. No clinical AI, agents, or observability. Peripheral: embedding APIs (Cohere/OpenAI mentioned in ch.4 tip) for CPU-only pipelines.

### Redundancy

| Canon title | Overlap | Gap / distinction |
|-------------|---------|-------------------|
| **AI Engineering 2025** | Tokenization mentioned ch.1 | AIE one example; Hands-on ch.2 is exhaustive tokenizer lab |
| **Grokking Algorithms 2e** | None | — |
| **Philosophy of Software Design 2e** | None | — |
| **Prompt Engineering for LLMs 2024** | Token budget implicit | PE focuses prompts not tokenizer internals |
| **DDIA 2e** | Vector/search concepts distant | DDIA not tokenizer-focused |

**Verdict:** Low redundancy — **canonical tokenizer + embedding** slot for canon.

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| **Worked examples** | Y — extensive code + 8-tokenizer comparison |
| **Exercise hooks** | Strong implicit labs (tips, HF course refs) |
| **Chapter boundary** | Clean |
| **Anchor density** | Very high — model names, vocab sizes, special tokens, shapes |
| **Ingest suitability** | Excellent reference ingest for tokenizer cheat sheet |

## TEXTBOOK-Q1 gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | GPT-4, StarCoder2, Phi-3 tokenizers (2023–2024) |
| **Author authority** | **PASS** | O'Reilly; authors known for visual ML/NLP pedagogy |
| **Primary-source citation density** | **PASS** | BPE, WordPiece, SentencePiece, DeBERTaV3, Sentence-BERT, NCE papers cited |
| **Contested claims flagged** | **PASS** | "Google killer" / factuality limits → RAG; tokenizer "open source" nuance deferred to ch.1 |
| **Worked examples** | **PASS** | Multiple executable blocks |

**TEXTBOOK-Q1 overall: PASS**

---

*Ingest agent: hotl-ingest-ch01-04 · hands_on_llms_2024 ch02 · lines 1599–3122 · word cap ≤4500*
