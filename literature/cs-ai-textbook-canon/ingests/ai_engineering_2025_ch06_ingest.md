# Chapter ingest — AI Engineering, Chapter 6

| Field | Value |
|-------|-------|
| slug | ai_engineering_2025 |
| source_type | textbook_chapter |
| pdf_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/ai_engineering_2025.pdf |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ai_engineering_2025.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ai_engineering_2025_ch06_ingest.md |

## Bibliographic metadata

| Field | Value |
|-------|-------|
| title | AI Engineering |
| authors | Chip Huyen |
| edition | 1st Edition (2025) |
| ISBN_print | 9781098166298 [corpus manifest; errata URL cites 9781098166304 at line 96] |
| ISBN_electronic | not stated in chapter slice |
| publisher | O'Reilly Media |
| parent_book_title | AI Engineering |
| chapter_number | 6 |
| chapter_title | RAG and Agents |
| page_range | not embedded in text export [inferred mid-book from Ch.5→Ch.7 adjacency; exact print pages unverified] |

## scope

Chapter 6 is the **framework spine** for context construction beyond prompting. It splits into four major arcs within the assigned slice (lines 11402–13786):

1. **RAG** — retrieve-then-generate history (Chen et al. 2017; Lewis et al. 2020); retriever + generator architecture; term-based (TF-IDF, inverted index, BM25) vs embedding-based (vector DB, k-NN, ANN: LSH, HNSW, PQ, IVF, Annoy); hybrid search and RRF; retrieval optimization (chunking, reranking, query rewriting, contextual retrieval); evaluation metrics; multimodal RAG (CLIP); tabular RAG via text-to-SQL (Kitty Vogue `Sales` table).

2. **Agents** — definition (environment + actions/tools); RAG/SQL as agents; compound-step accuracy decay; tool inventory (knowledge augmentation, capability extension, write actions); planning decoupled from execution; FM vs RL planners with **contested** LLM planning claims; function calling; control flows (sequential, parallel, if, for); ReAct and Reflexion; tool selection ablations; failure modes (planning, tool, efficiency).

3. **Memory** — internal / short-term (context) / long-term (retrieval); FIFO and summarization strategies; overflow from context to long-term store.

4. **Chapter close** — RAG as special-case agent; security tie to Ch. 5; bridge to Ch. 7 finetuning.

Author explicitly flags the **agents section as more experimental** than the rest of the book (lines 12409–12415). [verified from text, lines 11402–13724]

## key_findings

1. **Context = per-query feature engineering** — RAG constructs query-specific context; analogous to classical ML feature engineering. Same instructions, different retrieved context per query. [verified, 11463–11470]

2. **Long context does not obsolete RAG** — Data growth outpaces context limits; long-context models may under-use distant tokens; extra tokens add cost/latency. Author predicts provider-side salience/retrieval mechanisms. Anthropic guidance: &lt;200k-token KB may skip RAG (cited). [verified, 11472–11504]

3. **RAG architecture** — Retriever (index + query) + generator; original joint training vs today's separate off-the-shelf components; end-to-end finetune can help. Document/chunk terminology unified. [verified, 11506–11547]

4. **Term-based retrieval** — TF × IDF scoring; inverted index (Elasticsearch/Lucene); BM25 length-normalized TF-IDF variant; tokenization, stop words, n-grams; n-gram overlap retrieval when query/doc lengths similar. [verified, 11566–11708]

5. **Embedding-based retrieval** — Semantic ranking; index = embed chunks; query embed + nearest neighbors; rerankers/caches in production. k-NN exact but slow; ANN libraries (FAISS, ScaNN, Annoy, Hnswlib). Algorithms: LSH, HNSW, product quantization, IVF, Annoy trees. Traditional DBs adding vector support. [verified, 11710–11849]

6. **Retriever comparison & cost** — Term-based faster/cheaper out of box; embedding can finetune ahead but may obscure exact keywords (error codes, SKUs); hybrid mitigates. Vector DB spend can reach 20–50% of model API spend. Table 6-2 + ANN-Benchmarks trade-offs (recall, QPS, build time, index size); BEIR harness. [verified, 11851–12006]

7. **RAG evaluation stack** — Component: context precision/recall, NDCG/MAP/MRR, MTEB for embeddings; end-to-end answer quality (Ch. 3–4). Production often precision-only (recall needs full-corpus labels). [verified, 11877–12016]

8. **Hybrid & RRF** — Sequential cheap→precise (term then vector); parallel ensemble; reciprocal rank fusion formula with k≈60. [verified, 12018–12065]

9. **Retrieval optimization** — Chunking: fixed units, recursive splits, overlap (e.g. 2048 chars / 20 overlap), token-aligned to generator tokenizer; size trade-offs. Reranking including time decay; context order less critical than search rank. Query rewriting for multi-turn (identity resolution risk). Contextual retrieval: metadata, Q→chunk augmentation, Anthropic situate-chunk prompt (50–100 tokens). [verified, 12067–12264]

10. **Beyond text RAG** — Multimodal: CLIP embeddings for image+text retrieval. Tabular: text-to-SQL → execute → generate (Kitty Vogue Fruity Fedora units example); table/schema selection when schemas exceed context. [verified, 12291–12389]

11. **Agent definition** — Perceives environment, acts via tools; environment↔tool dependency (SWE-agent example). ChatGPT, RAG, SQL pipelines as agents. **Compound accuracy**: 95%/step → 60% over 10 steps, 0.6% over 100. [verified, 12391–12523]

12. **Tool taxonomy** — Read (retrieve, browse, calculator, code interpreter, modality bridges) vs write (SQL mutate, email, transfers); Chameleon +11.37% ScienceQA, +17% TabMWP vs GPT-4 alone. Security: code injection, write-action trust boundaries. [verified, 12530–12691]

13. **Planning** — Decouple plan generation, validation, execution; multi-agent framing; intent classifier + IRRELEVANT bucket; human approval for risky ops. FM planner vs RL planner (merge long-term). Kitty Vogue plan-generation prompt; deferred parameters from prior tool outputs. [verified, 12693–12978]

14. **Function calling & control flow** — Tool inventory declaration; required/none/auto modes; inspect parameter values. Granularity trade-off: function names vs natural-language plans + translator. Sequential, parallel, if, for loops in AI-determined control flow. [verified, 13000–13166]

15. **Reflection** — ReAct thought/act/observation loop; Reflexion evaluator + self-reflection trajectories; latency/token cost of format-enforcing few-shots. [verified, 13168–13253]

16. **Tool selection** — Ablation, usage distributions, task/model-dependent inventories (Toolformer 5, Chameleon 13, Gorilla 1645 APIs); tool transition / Voyager skill library. [verified, 13255–13341]

17. **Agent evaluation** — Planning failures: invalid tool, bad params, goal/constraint/time misses, false completion; tool failures and missing tools; efficiency metrics vs human baselines. Book GitHub benchmark + Berkeley Function Calling Leaderboard, AgentOps, TravelPlanner cited. [verified, 13349–13478]

18. **Memory hierarchy** — Internal knowledge (training), short-term (context), long-term (RAG stores); FIFO risks losing early high-signal messages; summarization + entity tracking (Bae et al. 2022); reflection-based merge/replace (Liu et al. 2023). [verified, 13486–13665]

19. **Synthesis** — RAG as agent with retriever tool; both prompt-based (no weight change); memory overflow management essential; leads to Ch. 7 finetuning. [verified, 13667–13724]

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Chapter opener | read | 11402–11431 |
| RAG intro + history | read | 11432–11491 |
| Long context vs RAG + Anthropic note | read | 11472–11504 |
| RAG architecture | read | 11506–11547 |
| Retrieval algorithms overview | read | 11549–11569 |
| Sparse/dense → term vs embedding framing | read | 11571–11603 |
| Term-based (TF-IDF, BM25, tokenization) | read | 11605–11708 |
| Embedding-based + vector search algorithms | read | 11710–11849 |
| Compare algorithms + eval metrics | read | 11851–12016 |
| Hybrid search + RRF | read | 12018–12065 |
| Chunking, reranking, query rewrite, contextual retrieval | read | 12067–12264 |
| Evaluating retrieval solutions checklist | read | 12265–12289 |
| Multimodal RAG | read | 12291–12328 |
| Tabular RAG / text-to-SQL | read | 12330–12389 |
| Agents warning + overview | read | 12391–12474 |
| Kitty Vogue agent walkthrough | read | 12476–12523 |
| Tools (read/write, Chameleon) | read | 12530–12691 |
| Planning overview + decouple execute | read | 12693–12801 |
| FM planning debate + Hao et al. | read | 12827–12883 |
| FM vs RL planners | read | 12885–12901 |
| Plan generation prompt + function calling | read | 12903–13067 |
| Planning granularity + control flows | read | 13069–13166 |
| ReAct + Reflexion | read | 13168–13253 |
| Tool selection + Voyager | read | 13255–13341 |
| Failure modes + evaluation | read | 13349–13478 |
| Memory | read | 13486–13665 |
| Summary + footnotes ¹–¹⁶ | read | 13667–13786 |
| Chapter 7 opener | **deferred** | 13787+ (outside scope) |

- **Lines read:** 11402–13786 (full parent-requested range)
- **wrong_file_flag:** false
- **Amnesiac attestation:** Numbered findings trace to line ranges in `ai_engineering_2025.txt`; contested planning claims retained with source attribution

## pedagogy

### learning_objectives

Implicit from chapter arc (no numbered LO block in text):

- Distinguish RAG vs agentic context construction and when each applies
- Design retriever index/query pipelines (term, dense, hybrid)
- Choose chunking, reranking, and query-rewrite tactics for production RAG
- Evaluate retrievers component-wise and end-to-end
- Define agents by environment + tool inventory; categorize tools
- Structure plan → validate → execute with reflection and human gates
- Diagnose agent failure modes and efficiency
- Map internal / short-term / long-term memory to implementation choices

### worked_examples_present

**Y**

| Example | Skill taught | Anchor |
|---------|--------------|--------|
| Acme fancy-printer-A300 specs query | RAG motivation | 11459–11461 |
| TF-IDF / inverted index Table 6-1 | Term retrieval mechanics | 11638–11672 |
| "transformer architecture" ambiguity | Term vs semantic failure mode | 11715–11718 |
| John/Emily Doe purchase follow-up | Query rewriting | 12177–12190 |
| Anthropic contextual chunk prompt | Contextual retrieval | 12240–12255 |
| Kitty Vogue `Sales` / Fruity Fedora SQL | Text-to-SQL RAG | 12337–12373 |
| Kitty Vogue revenue projection agent steps | Multi-step agent + SQL tools | 12476–12506 |
| 199,999 ÷ 292 calculator | Tool augments model limits | 12597–12600 |
| SF→India $5k trip planning options | Plan efficiency | 12716–12729 |
| Kitty Vogue plan-generation SYSTEM PROMPT | Plan format + deferred params | 12911–12964 |
| lbs_to_kg function-calling response | Function calling API shape | 13042–13061 |
| ReAct HotpotQA trace (Fig 6-12) | Thought/Act/Observation | 13203–13214 |
| Compound accuracy 95%×N steps | Agent reliability math | 12511–12515 |

### exercise_hooks

Chapter has **no numbered end-of-chapter exercises**. Hooks below are **operator extensions** from inline examples, tips, and GitHub references.

| ID | Prompt summary | Operator extension | Anchor |
|----|----------------|-------------------|--------|
| 6.RAG-1 | Acme printer spec retrieval | Build minimal BM25 + embedding hybrid on 10-doc corpus; measure context precision | 11459–11461, 12018–12039 |
| 6.RAG-2 | Chunk "I left my wife a note" | Sweep chunk size/overlap; plot recall@k on boundary-sensitive Qs | 12103–12110 |
| 6.RAG-3 | Transformer query disambiguation | Compare BM25-only vs vector-only vs hybrid+RRF on ambiguous term | 12031–12035, 12047–12065 |
| 6.RAG-4 | Emily Doe follow-up | Implement LLM query rewrite with conversation buffer; fail closed on unknown "his wife" | 12177–12210 |
| 6.RAG-5 | Fruity Fedora 7-day units | Text-to-SQL with schema-in-context; log invalid SQL rate | 12351–12373 |
| 6.AG-1 | Kitty Vogue product planner | Implement plan-validate-execute loop with 3 tools; count plans-to-valid | 12903–12978, 13408–13416 |
| 6.AG-2 | 40 lbs → kg tool call | Log and assert parameter values on every function call | 13042–13067 |
| 6.AG-3 | Tool inventory ablation | Remove one tool at a time; plot task success delta (Chameleon-style) | 13277–13293 |
| 6.AG-4 | SF→Hanoi $5k constraint | Eval goal failure when budget/city violated | 13387–13393 |
| 6.MEM-1 | Long chat FIFO vs summary | Compare FIFO truncation vs rolling summary on early-purpose messages | 13623–13649 |
| 6.EVAL-1 | Book GitHub agent benchmark | Run author's failure-mode benchmark; map to planning/tool/efficiency taxonomy | 13360–13364, 13408–13431 |

## Operator hooks

### 1. Foundation layer (w1_foundation)

Chapter 6 is the **canon reference for production context construction** in the cs-ai-textbook-canon stack:

- **RAG pipeline vocabulary** — retriever indexing/querying, hybrid search, chunking, contextual retrieval — operationalizes Ch. 5 prompting with external memory
- **Agent loop** — plan/validate/execute/reflect — composes Ch. 2–4 eval, structured outputs, and Ch. 5 defensive prompting for tool use
- **Memory model** — bridges short context to long-term stores; prerequisite for multi-turn agent skills and observability (what to log: tool calls, plans, memory evictions)

Treat as **framework spine, not tutorial** per corpus manifest `ingest_note`. Pair with **hands_on_llms_2024** for implementation notebooks and **philosophy_software_design_2e_2021** Ch. 4–7 for API/tool-surface depth when reviewing agent middleware.

### 2. MDCalc alignment

**[none]** — No clinical deployment, regulated workflow, or MDCalc-specific content. Pattern-portable only: retrieval precision/recall framing, human-in-the-loop before write actions, eval harness discipline.

### 3. Redundancy

| Overlap with | Relationship |
|--------------|--------------|
| `hands_on_llms_2024` | HOTL likely supersedes on embedding/RAG code paths; keep AIE Ch.6 for architecture, cost, and eval framing |
| `grokking_algorithms_2e_2024` Ch.12 | k-NN intuition cited here for vector search (11762–11775); AIE adds ANN, hybrid, production cost |
| `philosophy_software_design_2e_2021` | Tool inventory / shallow wrappers (Ch. 7); write-action trust (Ch. 10 errors); comments-as-contract for tool schemas (Ch. 13–15) |
| `ddia_2e_2026` | Vector indexing and retrieval at storage layer; AIE focuses application RAG, not replication |
| Ch. 3–5 (same book) | Embeddings (Ch.3), eval metrics (Ch.3–4), defensive prompting for tools (Ch.5) — prerequisites, not re-ingested |

**Dedup rule:** Use this ingest for **system design and failure-mode checklists**; defer hands-on vector-DB setup to HOTL unless operator requests AIE-only path.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | Strong Y — SQL, prompts, function-call payloads, ReAct trace |
| Exercise hooks | Operator extensions only (no textbook exercises) |
| Chapter boundary | Clean — ends 13724 summary; Ch.7 at 13787 |
| Citation density | High (IR classics + 2020–2024 agent papers) |
| Child-skill potential | `scholia.rag-hybrid-eval`, `scholia.agent-plan-validate`, `scholia.memory-fifo-vs-summary` reference cards |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | 2025 1e; within ≤5-year preference |
| Author authority | **PASS** | O'Reilly textbook; practitioner pedigree (Stanford MLSys, Cloudera, NVIDIA, Snorkel); forewords from ChatGPT cocreator, enterprise AI leaders |
| Primary-source citation density | **PASS** | Dense: Chen 2017, Lewis 2020, Robertson BM25, FAISS/ScaNN papers, ReAct, Reflexion, Chameleon, Anthropic 2024 contextual retrieval, MTEB, BEIR, ANN-Benchmarks |
| Contested claims flagged | **PASS** | See table below |
| Worked examples (procedural chapter) | **PASS** | Multiple stepped pipelines with prompts and SQL |

### Contested or oversimplified claims (not smoothed)

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Long context will not kill RAG | 11474–11489 | Author opinion; contested by "just stuff KB in prompt" camp — Anthropic 200k caveat noted |
| Claude &lt;200k tokens → skip RAG | 11499–11504 | Vendor-specific guidance; may not generalize |
| Term vs embedding categorization preferred over sparse/dense | 11573–11603 | Pedagogical choice; SPLADE edge case acknowledged |
| 95% per-step → 0.6% @100 steps | 12511–12515 | Independence assumption; steps may correlate |
| LeCun: autoregressive LLMs can't plan | 12831–12833 | Active debate; author presents counterarguments |
| Kambhampati: LLMs confuse planning knowledge vs executable plans | 12833–12839 | Contested; Hao et al. world-model planning cited as alternative |
| Self-driving car trust anecdote | 12668–12684 | Rhetorical; not empirical safety claim |
| Vector DB = 20–50% of API spend | 11935–11936 | Anecdotal industry observation |
| Agents section "more experimental" | 12409–12415 | Author self-flag — frameworks evolving |
| FIFO memory "fatally wrong" for early messages | 13630–13634 | Use-case dependent |
| RAG as special-case agent | 13696–13698 | Definitional stretch useful for unification but not universal |

**TEXTBOOK-Q1 chapter verdict:** **PASS** — flagship w1_foundation ingest for RAG/agents; flag agent-planning debate and vendor-specific retrieval guidance when cross-linking.

## Glossary (chapter-local)

| Term | Definition per text |
|------|---------------------|
| RAG | Retrieve relevant external information, then generate with it |
| Retriever | Indexes and queries external memory; quality dominates RAG success |
| Generator | Model producing final response from retrieved context |
| Term-based retrieval | Lexical matching (TF-IDF, BM25, inverted index) |
| Embedding-based retrieval | Semantic similarity via dense vectors + vector search |
| Hybrid search | Combined term + embedding retrieval |
| RRF | Reciprocal rank fusion across ranked lists |
| Chunk | Sub-document unit for indexing (also called document in IR sense) |
| Contextual retrieval | Augment chunks with metadata or situating context before index |
| Agent | Entity perceiving environment and acting through tools |
| Tool inventory | Declared set of functions/APIs available to agent |
| Function calling | Model API pattern selecting tools and parameters |
| Plan | Sequence of actions to accomplish a task |
| ReAct | Interleaved reasoning (thought) and action with observations |
| Context precision / recall | Fraction of retrieved docs relevant; fraction of relevant docs retrieved |
| Internal / short-term / long-term memory | Trained weights; current context; persisted external retrieval |

## Reciprocal index pointers

Text export lacks a reliable print index slice for Ch. 6 within the read range. Cross-chapter pointers from body text:

- Prerequisites: Ch. 3 (embeddings, context efficiency), Ch. 4 (eval), Ch. 5 (defensive prompting, code injection)
- Forward: Ch. 7 finetuning (13787+)
- External depth: book GitHub repo (IR resources, agent failure benchmark)
