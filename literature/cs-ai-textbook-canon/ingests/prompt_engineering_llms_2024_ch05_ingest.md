# prompt_engineering_llms_2024 — Chapter 05 ingest

| Field | Value |
|-------|-------|
| slug | prompt_engineering_llms_2024 |
| chapter_number | 5 |
| chapter_title | Prompt Content |
| parent_book_title | Prompt Engineering for LLMs |
| authors | Berryman, Johnathan; Ziegler, Albert |
| edition | 1e (2024) |
| source_type | textbook_chapter |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch05_ingest.md |
| text_lines_read | 3708–5096 |
| page_range | not recoverable from text export |

---

## Scope

Chapter 5 catalogs **what goes into prompts**: **static** (clarifications, few-shot examples) vs **dynamic** (per-user context). Covers explicit/implicit instructions, few-shot benefits and three drawbacks (scale, anchoring, spurious patterns), dynamic sources, lexical retrieval (Jaccard, TF-IDF/BM25), neural RAG (embeddings, FAISS, snippetizing), full book-rating RAG code walkthrough, lexical vs neural tradeoffs.

Part II core—pairs with Ch 6 assembly.

---

## Key findings

All items `[verified from text]` unless tagged `[inferred]`.

1. **LLM value prop.** Messy text + commonsense beats pure collaborative filtering for recommendations when rich user context supplied (Fig 5-1). (L3708–3744)

2. **Static vs dynamic.** Static clarifies task; dynamic details instance (user, session). Boundary fuzzy (self-help rule vs user preference). (L3754–3807)

3. **Clarification + consistency.** Programmatic queries fail silently on ambiguity; explicit lists (Bing/Sydney Table 5-1—unconfirmed extract). Tips: positives over negatives, reasons, avoid absolutes. System message for RLHF models. (L3814–3933)

4. **Few-shot prompting.** Pattern continuation; zero-shot = no examples; implicit often beats explicit rules; persona via examples. (L3938–4015)

5. **Drawback 1 — context scale.** Long per-user JSON personas blow window; attention confusion among similar sections; shorten examples or few-shot format-only. (L4020–4086)

6. **Drawback 2 — anchoring.** Example distributions bias outputs (name era Fig 5-4; star-rating uniformity Fig 5-5); include representative + edge cases. (L4088–4156)

7. **Drawback 3 — spurious patterns.** Ascending/descending order (Fig 5-6); “happy path first” pessimism (Fig 5-7); shuffle/eval subsets; DSPy optimization. (L4161–4214)

8. **Dynamic content sources.** User input, files, DB, APIs, search—gather broadly then filter in Ch 6. (L4234+ region)

9. **Lexical retrieval.** Stop words, stemming, Jaccard similarity—fast, Copilot open-tab use; search string as mini-prompt. TF-IDF/BM25 for term weighting. (L4488–4543)

10. **Neural retrieval.** Embedding vectors, offline index (snippetize → embed → store), online k-NN; contrastive-trained embedders; tiny vs LLM cost. (L4549–4674)

11. **Snippetizing.** Token limits, one idea per chunk, prompt-fit size; sliding window vs paragraph boundaries; code class context augmentation. (L4592–4643)

12. **RAG walkthrough (Fig 5-12).** FAISS + OpenAI embeddings; `predict_rating` static+dynamic prompt; The Beach → rating 2 from backpacking-hating reviews. (L4692–4864)

13. **Lexical vs neural.** Lexical debuggable, field boosts; neural semantic typos/synonyms; hybrid often best. (L4866–4899)

---

## Coverage attestation

| Section | In slice (L3708–5096) | Notes |
|---------|------------------------|-------|
| Static/dynamic framing | yes | |
| Clarification / Table 5-1 | yes | Unconfirmed Bing extract |
| Few-shot + 3 drawbacks | yes | Figs 5-2–5-7 |
| Dynamic sources | yes | L4234–4487 region |
| Lexical + neural retrieval | yes | RAG code |
| Conclusion | yes | L5055–5085 |
| Chapter 6 opener | excluded | L5097+ |

**wrong-file flag:** false.

---

## Pedagogy

### learning_objectives

- Classify prompt fragments as static vs dynamic for an app. `[verified from text]`
- Design few-shot sets avoiding anchoring and spurious order bias. `[verified from text]`
- Implement lexical vs neural retrieval tradeoff for a corpus. `[verified from text]`
- Walk through FAISS RAG indexing + rating prompt assembly. `[verified from text]`

### worked_examples_present

**Y** — Book recommendation Fig 5-1; review-rating few-shot Figs 5-3/5-5; full Python RAG (index_reviews, retrieve_reviews, predict_rating).

### exercise_hooks

| ID | Archetype | Scholia hook |
|----|-----------|--------------|
| PE-5.1 | Static/dynamic sort | Tag fields in a production prompt template |
| PE-5.2 | Few-shot shuffle | Measure metric vs ordered “happy path first” |
| PE-5.3 | Jaccard vs embed | Same query on IDE snippets; compare recall |
| PE-5.4 | RAG replicate | Run book-rating pipeline on local review JSON |
| PE-5.5 | Snippet window | Ablate overlap stride on one long doc |

---

## Operator hooks

### 1. Foundation layer

**w2 content spine** — implements Ch 4 feedforward “retrieve”; feeds Ch 6 prioritization. Pairs with AIE Ch 6 RAG and HOTL Ch 7 LangChain memory.

### 2. MDCalc alignment

**Partial** — Dynamic patient context + static clinical scope boundaries mirror static/dynamic split. `[inferred]`

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| ai_engineering_2025 Ch 5 | **High** on few-shot/CoT mention | AIE Ch5 **defensive PE + prompt ops**; PE Ch5 **content sourcing + RAG code** |
| ai_engineering_2025 Ch 6 | Partial | Both RAG; PE Ch5 FAISS tutorial more hands-on |
| hands_on_llms_2024 Ch 6 | Partial | HOTL few-shot/CoT labs; PE Ch5 retrieval theory + anchoring |

**Dedup:** PE Ch5 for **static/dynamic taxonomy + RAG walkthrough**; AIE Ch5 for **security/versioning/DSPy warnings**.

### 4. Scholia fit

- **Worked examples:** Y (runnable RAG)
- **Boundary:** Ends pointing to Ch 6 assembly

---

## TEXTBOOK-Q1 gate

**PASS**

### Contested claims

1. **Table 5-1 Bing prompt** — Jailbreaker extract; overlap unconfirmed (L3840–3842).
2. **Few-shot always worth it** — Author hedges after three drawbacks (L4216–4219).
3. **Neural > lexical** — Chapter argues lexical debuggability (L4870–4888).

---

## Anchor index

| Topic | Lines |
|-------|-------|
| Chapter start | 3708 |
| Static/dynamic | 3754–3807 |
| Few-shot | 3938–4219 |
| Dynamic content | 4234 |
| Lexical retrieval | 4488–4543 |
| Neural RAG code | 4692–4864 |
| Conclusion | 5055–5096 |

---

## Cross-chapter dependencies

- **Requires:** Ch 4 loop, Ch 2 attention (few-shot scale).
- **Enables:** Ch 6 assembly; Ch 8 advanced RAG.

---

*Ingest from L3708–5096. Word cap: ≤4500.*
