# CS + AI Foundation Study Guide

**Program:** cs-ai-textbook-canon wave-1 (2 weeks, 10 weekdays)  
**Primary sources:** Grokking Algorithms 2e · A Philosophy of Software Design 2e · AI Engineering (Huyen 2025)  
**Quote policy:** Passages marked **[verified from text]** come from `/literature/cs-ai-textbook-canon/text/*.txt` exports. Contested claims are flagged, not smoothed.

---

## Part 1 — Algorithms and growth rates (Grokking Algorithms 2e)

> **Memory anchors for Part 1 — Algorithms.** Pick one room of a familiar space (kitchen, childhood bedroom, office). For each chunk below, choose a locus and a vivid image you will never forget. Spend two minutes building it now; walk it again tonight before sleep.
>
> - **Binary search halving:** a phone book ripped in half each guess
> - **Big O vs wall clock:** NASA counting down vs Bob multiplying guesses
> - **Hash collision:** two fruits fighting for the same alphabet slot
> - **BFS layers:** ripples in a pond from one stone
> - **Dijkstra cheapest:** toll booths on a highway map
> - **Greedy trap vs DP table:** vending machine that steals change vs spreadsheet grid
>
> See Appendix D.2 for the build-your-own framework and fallback palace.

### 1.1 Binary search and sorted preconditions

Binary search is the first algorithm in Grokking because it teaches the habit of **eliminating half the search space** each step.

> **Binary search is an algorithm; its input is a sorted list of elements** (I'll explain later why it needs to be sorted). If an element you're looking for is in that list, binary search returns the position where it's located. Otherwise, binary search returns null.  
> — Grokking ch1 **[verified from text]**

**Worked example (phone book):** 240,000 names → at most ~18 halvings (log₂ 240k). The book's number-guessing demo caps at **7 guesses for 1–100** because log₂ 100 ≈ 6.6.

**Simple search vs binary search:** guessing 1, 2, 3… eliminates one candidate per try. Binary search eliminates **half** the remaining space.

**Big O trap (Bob vs NASA):** Bob says binary search is "15× faster" at 1B entries because 1B/240k ≈ 4000 and log only doubles a bit. That confuses **multiplicative speedup** with **growth rate**. log₂(1B) ≈ 32 steps vs 1B steps for simple search — the ratio explodes at scale, but O(log n) is about **how cost grows**, not a fixed multiplier.

| Notation | Name | Typical examples |
|----------|------|------------------|
| O(1) | Constant | Hash lookup (average) |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Simple search, one pass |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Nested loops, naive sorts |

**Figure note:** EPUB/PDF shows halving diagrams; text export has `[]` placeholders — open the book for visuals.

### 1.2 Arrays, linked lists, and selection sort

- **Arrays:** O(1) random access; O(n) insert in middle (shift elements).
- **Linked lists:** O(n) access by index; O(1) insert at head if you have the pointer.
- **Selection sort:** find smallest, swap, repeat — O(n²). Fine for tiny n; not for large datasets.

**Design link (preview):** picking array vs list is an **interface / performance tradeoff** Ousterhout returns to as hidden cost in abstractions.

### 1.3 Recursion and the call stack

Recursion needs:
1. **Base case** (stop)
2. **Recursive case** (smaller subproblem)

The **call stack** holds unfinished frames. Stack overflow = too deep without base case.

**Classic:** sum(list) = first + sum(rest); factorial; Euclidean GCD (ingest flags: full proof deferred in text).

### 1.4 Divide and conquer: quicksort and merge sort

**Quicksort:** pick pivot, partition smaller/larger, recurse. Average O(n log n); worst O(n²) on adversarial/poor pivot order. Random pivot helps average case.

**Merge sort:** split in half, sort halves, merge — stable O(n log n) but needs extra memory.

**When to pick which:** in-memory, average-case speed → quicksort variants; stability or guaranteed bound → merge sort.

### 1.5 Hash tables and collisions

Hash maps underpin dicts, caches, and dedup sets.

> **First, I've been telling you a white lie. I told you that a hash function always maps different keys to different slots in the array.**  
> — Grokking ch5 **[verified from text]**

**Collisions:** two keys land in same slot → chaining or open addressing. **Load factor** triggers resize/rehash.

**Applications:** dedup, caches, routing tables, inverted indexes (preview for RAG).

### 1.6 Graphs: BFS and shortest unweighted paths

Model relationships as **nodes + edges**. BFS explores **layer by layer** → fewest hops on unweighted graphs. Use a **queue**.

**Seen set** prevents cycles from looping forever.

### 1.7 Trees and binary search trees

Trees are acyclic connected graphs. **BST:** left < parent < right; in-order traversal yields sorted order. Imbalance degrades to linked-list performance → balanced trees (red-black, AVL) in other books (CLRS optional in canon).

### 1.8 Dijkstra and weighted graphs

For **non-negative** edge weights, Dijkstra greedily settles the cheapest unvisited node. Differs from BFS when edge weights differ.

**Ingest flag:** Grokking sometimes says Dijkstra requires "no cycles"; with non-negative weights, cycles do not break correctness — revisit with CLRS if you need proof.

### 1.9 Greedy, NP-complete, dynamic programming

**Greedy:** locally optimal choices. Works for some problems (Huffman, activity selection with proof); fails for 0/1 knapsack.

**NP-complete:** no known fast exact algorithm for worst case; approximation or exponential DP often used.

**DP:** optimal substructure + overlapping subproblems → table or memoization. Classic: knapsack, longest common subsequence.

### 1.10 k-NN and where ML fits

k-nearest neighbors: classify by majority vote of nearby training points. Grokking ch12 introduces ML lightly — **ingest flags oversimplifications**; pair with AIE for production reality.

---

## Part 2 — Managing complexity in software (Ousterhout 2e)

> **Memory anchors for Part 2 — Software design.** Pick a second room (or a second route through the same home). Anchor:
>
> - **Complexity definition:** fog on a windshield while driving
> - **Change amplification:** one domino knocks over twenty
> - **Deep module:** five Unix syscalls hiding a filesystem
> - **Information hiding:** restaurant kitchen behind a menu
> - **Strategic vs tactical:** patching a tire daily vs aligning wheels once
>
> See Appendix D.2.

### 2.1 What complexity is (and is not)

> **Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system.**  
> — Ousterhout ch1 **[verified from text]**

Large feature-rich systems can be **simple** if easy to change; small systems can be **complex** if every tweak is scary.

**Weighted complexity:** isolate rare complex parts that nobody touches — they barely raise C = Σ tₚ cₚ.

### 2.2 Three symptoms

1. **Change amplification** — small logical change touches many files.
2. **Cognitive load** — how much you must hold in head to be safe.
3. **Unknown unknowns** — surprises you did not know to look for (worst symptom).

### 2.3 Strategic vs tactical programming

**Tactical:** ship the fastest patch now. **Strategic:** invest in design so future changes stay cheap. Ousterhout argues **0% strategic** eventually drowns in complexity debt; ch3 investment curves are **[conditional — anecdotal in ingest]**.

### 2.4 Deep modules vs shallow modules

> **The best modules are deep: they have a lot of functionality hidden behind a simple interface. A deep module is a good abstraction because only a small fraction of its internal complexity is visible to its users.**  
> — Ousterhout ch4 **[verified from text]**

**Unix I/O:** `open/read/write/lseek/close` — enormous behavior, tiny surface.

**Shallow module / classitis:** many tiny classes with pass-through methods — high interface cost, low benefit.

### 2.5 Information hiding and leakage

**Parnas:** hide design decisions likely to change. **Leakage:** interface exposes internals callers should not need (e.g., file format details in method names).

**Pull complexity downward:** module should absorb pain, not export config knobs for every edge case.

### 2.6 Layers and pass-through methods

Each layer should add value. **Pass-through method** only forwards calls — sign of shallow layering. Prefer **different abstractions** per layer, not 1:1 wrappers.

### 2.7 Debates you should know

- **Clean Code small functions:** Ousterhout ch9/ch12 — splitting can **increase** total complexity if interfaces multiply without depth.
- **Test-driven development:** useful but not a substitute for deep modules (ch8).

### 2.8 Capstone: principles and red flags (ch22)

**16 design principles** (sample): define errors out of existence; pull complexity down; separate general from special; design it twice; comments describe what code cannot; etc.

**14 red flags** (sample): shallow module; information leakage; pass-through method; overexposure of internals; special-general mixture; conjoined implementations.

**Day 5 mock** expects you to recite any 3 principles + 3 red flags from memory, then verify against ch22.

---

## Part 3 — AI engineering framing (AIE ch1–2)

> **Memory anchors for Part 3 — AI stack.** Pick a third room. Anchor:
>
> - **Scale post-2020:** power lines feeding a stadium-sized GPU hall
> - **Foundation model:** iceberg — API tip, training underwater
> - **Three layers:** app / model dev / infrastructure cake tiers
> - **Sampling randomness:** dice cup over next-token choice
>
> See Appendix D.2.

### 3.1 Scale and AI engineering

> **If I could use only one word to describe AI post-2020, it'd be scale.**  
> — AIE ch1 **[verified from text]**

Consequences: (1) more capable models → more applications; (2) only a few orgs train at frontier → **model-as-a-service** for everyone else.

> **AI engineering—the process of building applications on top of readily available models—** into one of the fastest-growing engineering disciplines.  
> — AIE ch1 **[verified from text]**

### 3.2 From language models to foundation models

**Self-supervision** infers labels from raw text (next-token prediction), unlocking web-scale training data.

**Foundation model:** large pretrained model adapted via prompt engineering, RAG, finetuning.

### 3.3 AI vs traditional ML engineering

| Traditional ML eng | AI engineering |
|--------------------|----------------|
| Train custom models | Mostly adapt existing FMs |
| Feature pipelines | Context construction |
| Batch inference focus | Interactive latency + streaming |
| Tabular metrics | Open-ended generation eval |

### 3.4 Use-case patterns and limits

Successful patterns: coding assistants, search/synthesis, translation, classification with instructions. Limits: factual drift, tool misuse, inconsistent sampling, cost at scale.

### 3.5 Crawl-Walk-Run deployment

Microsoft framing cited in AIE: start **human-in-loop**, increase automation as eval confidence grows. Pair with guardrails before unsupervised actions.

### 3.6 Model internals you must respect (ch2 skim)

**Autoregressive LMs** predict next token. **Attention** mixes prior tokens. **Scaling laws / Chinchilla:** model size and data should scale together for compute-optimal training.

**Hallucination:** fluent but false — not a bug you "unit test away"; manage with retrieval, constraints, eval.

**Sampling:** temperature and top-p increase diversity → **non-determinism** is a product requirement, not an accident.

---

## Part 4 — Evaluation, prompts, RAG, agents (AIE ch3–6)

> **Memory anchors for Part 4 — Eval and context.** Fourth room. Anchor:
>
> - **AI-as-judge bias:** referee wearing your team's jersey
> - **EDD buckets:** four clipboards on a wall
> - **RAG pipeline:** librarian hands book pages to writer
> - **Compound accuracy:** chain of leaky buckets
>
> See Appendix D.2.

### 4.1 Why FM evaluation is hard (ch3)

Structural difficulties include: open-ended outputs, no single correct answer, judge cost, distribution shift, rapid model churn, sensitivity to prompt phrasing.

**Perplexity:** useful on training-like text; weak post-SFT product proxy.

**Functional correctness:** pass@k for code — tests, not vibes.

**AI-as-judge biases:** position bias, verbosity bias, self-preference. Mitigate with swap order, rubrics, human calibration.

### 4.2 Evaluation-driven development (ch4)

Build eval sets **before** chasing leaderboard scores. Four buckets: domain accuracy, generation quality, instruction-following, cost/latency.

**Leaderboards** ≠ your product decision — different data, prompts, and risk tolerance.

### 4.3 Prompt engineering (ch5)

Techniques: instructions, few-shot ICL, chain-of-thought (when appropriate), structured output formats.

**Prompt injection:** untrusted content hijacks instructions — direct (user) vs indirect (retrieved doc). Defenses: separation of trusted system vs untrusted data, output filtering, tool permission boundaries — not one silver bullet.

### 4.4 RAG pattern (ch6)

> **Two dominating patterns for context construction are RAG, or retrieval-augmented generation, and agents.**  
> — AIE ch6 **[verified from text]**

**RAG:** retrieve relevant chunks → condition generation. Persists because:
- Context windows still bounded economically
- Fresh/private corpora not in weights
- Attribution and update without retrain

**Hybrid search:** BM25 (lexical) + embeddings (semantic) fused (e.g., RRF).

### 4.5 Agents and compound accuracy

Agents loop: perceive → plan → act with tools. **Compound accuracy:** 0.95¹⁰ ≈ 0.60 for ten independent 95% steps — multi-step autonomy needs human checkpoints or narrow tools.

**ReAct:** interleave reasoning traces with tool calls.

**Experimental warning (ingest):** agent frameworks evolve quickly — eval before production autonomy.

### 4.6 Finetune vs RAG heuristic

**Facts** → RAG / knowledge base. **Form** (tone, format, tool style) → finetune / preference tuning. Many products need both.

---

## Part 5 — Adaptation, data, inference, architecture (AIE ch7–10)

> **Memory anchors for Part 5 — Production.** Fifth room or revisit room 1 with new stickers. Anchor:
>
> - **LoRA/QLoRA:** small adapter backpack on a giant model
> - **TTFT vs TPOT:** door opening vs items on a conveyor
> - **Guardrails layer:** bouncer before and after the model
> - **Feedback loop risk:** amplifier squeal when mic hears speaker
>
> See Appendix D.2.

### 5.1 Finetuning and PEFT (ch7)

**Full finetune** updates all weights — expensive. **LoRA:** low-rank adapters on attention layers. **QLoRA:** quantized base + adapters for consumer GPUs.

When to finetune: stable style/format, proprietary workflow, after RAG ceiling — not as first move for changing facts.

### 5.2 Dataset engineering (ch8)

Dimensions: relevance, diversity, correctness, toxicity/safety, format consistency. **Data iteration** often beats architecture churn.

### 5.3 Inference and cost (ch9)

**TTFT** (time to first token) dominates perceived chat latency. **TPOT** (time per output token) dominates long completions.

**KV cache** stores attention state during decode — critical for throughput.

Batching, quantization, speculative decoding — know names; Hands-On LLMs week covers labs.

### 5.4 Architecture stack (ch10)

Typical request path:

1. **Guardrails / policy** (input)
2. **Router** (model selection)
3. **Semantic cache** (repeat queries)
4. **Context builder** (RAG / memory)
5. **Model call**
6. **Guardrails** (output)
7. **Logging / tracing**

**Observability triad:** metrics (aggregates), logs (events), traces (request journeys). Essential for debugging nondeterministic failures.

### 5.5 Feedback loops and safety

User thumbs-up/down, implicit signals, RLHF-style training can improve quality but also **sycophancy** and **reward hacking**. Regulated-adjacent deployments: human escalation, PHI out of caches, audit trails — pattern-portable ideas from ch10 without employer-specific claims.

---

## Appendix A — Chapter map and ingest status

| Book | Chapters in program | Ingest path |
|------|---------------------|-------------|
| Grokking 2e | 1–12 | `ingests/grokking_algorithms_2e_2024_ch*_ingest.md` |
| Ousterhout 2e | 1–5, 7–8, 9, 20–22 | `ingests/philosophy_software_design_2e_2021_ch*_ingest.md` |
| AIE 2025 | 1–10 | `ingests/ai_engineering_2025_ch*_ingest.md` |

**Not in 2-week sprint:** Hands-On LLMs labs (follow-on week).

---

## Appendix B — High-frequency miss patterns

> **Memory anchors for Appendix B miss patterns.** Walk the rooms you already built (D.2). At each existing locus, add ONE small sticker for the trap — do not invent new loci.

### Miss pattern 1: Big O as speed multiplier

> **Anchor this trap.** Pick an image separating "growth rate" from "× faster on my laptop."

Bob's NASA mistake: O(log n) describes scaling, not a constant factor speedup.

### Miss pattern 2: Hash O(1) always

> **Anchor this trap.** Two avocados in the same alphabet slot.

Collisions and load factor break the white lie.

### Miss pattern 3: BFS vs Dijkstra

> **Anchor this trap.** Counting stops vs counting tolls.

BFS = unweighted hops. Dijkstra = sum of non-negative weights.

### Miss pattern 4: Shallow = small file

> **Anchor this trap.** Tiny interface, huge hidden kitchen.

Depth = benefit/cost of interface, not LOC.

### Miss pattern 5: Pass-through "layering"

> **Anchor this trap.** Echo hallway that only repeats your words.

Layers must add semantics, not forwarding.

### Miss pattern 6: Perplexity as product metric

> **Anchor this trap.** Textbook difficulty score on customer support replies.

Good for LM training diagnostics; weak alone for task success.

### Miss pattern 7: Leaderboard = ship decision

> **Anchor this trap.** Trophy shelf from a different sport.

Your data, prompts, and risk profile differ.

### Miss pattern 8: Long context kills RAG

> **Anchor this trap.** Entire library on desk vs index cards.

Economics, freshness, and attribution keep RAG relevant.

### Miss pattern 9: Agent step accuracy multiplies

> **Anchor this trap.** Ten locks, each 95% — how many open?

Multiply probabilities; add human gates.

### Miss pattern 10: Finetune for fresh facts

> **Anchor this trap.** Tattoo vs pocket notebook.

Changing knowledge → retrieval; changing voice → finetune.

---

## Appendix C — Completion checklist (Day 10)

- [ ] Mock B scored ≥ 75% open-book
- [ ] Palace walk under 5 minutes, all five rooms
- [ ] Glossary: 40+ terms self-defined without looking
- [ ] One-page "crawl-walk-run" plan for a hypothetical FM app
- [ ] List 3 Ousterhout red flags you have actually seen in code
- [ ] Sketch AIE ch10 architecture stack from memory
- [ ] Export browser notes if using static hosting
- [ ] Schedule Hands-On LLMs follow-on week for labs

**Sleep target:** 7–8 hours before heavy mock days (D5, D10).

---

## Appendix D — Pedagogy and memory systems

### D.1 Evidence summary

1. **Retrieval practice** `[T1-verified, read:body]` — testing beats re-reading for delayed recall (Serra et al. 2025). **Practical:** daily drills in PRACTICE_EXAMS.md and mock exams.
2. **Transfer-appropriate processing** `[T1-verified, read:body]` — practice in the form you'll be tested in (Morris et al. 1977). **Practical:** open-book mocks with trace/paper exercises, not flashcards alone.
3. **Spaced repetition** `[T2-verified]` — expanding intervals (Ebbinghaus; modern meta-analyses). **Practical:** Anki deck from glossary (optional build).
4. **Method of loci** `[T1-verified, read:body]` — spatial serial recall d≈0.42–0.88 immediate (Ondrej et al. 2025). **Practical:** five-room map across Parts 1–5.

**Compounders:** dual coding (image + word), interleaving algorithm + design questions, generation effect (write traces before reading solutions).

### D.2 Build-your-own memory palace

1. **Pick your space** — current home recommended.
2. **Map five rooms** to Parts 1–5 in walk order.
3. **5–7 loci per room** — max ~2 items per locus.
4. **Vivid images** — yours, not this document's.

**Locus patterns:** bookshelf for ordered lists; stove burners for intensity scales; spice rack for equivalent options.

**Fallback (under 90 seconds):** use kitchen → bedroom → office route; sticky notes on fridge, bedpost, monitor for the five Part titles only — replace with personal images by Day 3.

### D.3 Mnemonic quick reference

| Domain | Mnemonic | Expands to |
|--------|----------|------------|
| Sorting growth | "1 log n square" | O(1), O(log n), O(n), O(n log n), O(n²) |
| Ousterhout symptoms | "ACC" | Amplification, Cognitive load, Unknown unknowns |
| Unix I/O depth | "ORWLC" | open, read, write, lseek, close |
| EDD buckets | "DGIC" | Domain, Generation, Instruction, Cost/latency |
| RAG stages | "RIG" | Retrieve, Inject context, Generate |
| Latency pair | "First Per" | TTFT first token, TPOT per token |

### D.4 Daily integration schedule

| Day | Memory work (15–30 min evening) | New technique |
|-----|----------------------------------|---------------|
| D1 | Build room 1 (Algorithms); drill binary search | Retrieval: end-of-day recap without book |
| D2 | Room 1 loci for sort/recursion | Generation: write partition trace |
| D3 | Room 2 (Design) + hash collision image | Interleave one algo + one design question |
| D4 | Room 2 depth/leakage stickers | Dual coding: sketch Unix I/O diagram |
| D5 | Full walk rooms 1–2; **Mock A** | TAP: timed mock form |
| D6 | Room 3 (AI framing) | Spaced review D1 flash terms |
| D7 | Room 4 (Eval) | AI-as-judge bias list from memory |
| D8 | Room 4 RAG/agent loci | Compound accuracy calculation |
| D9 | Room 5 (Production) | Finetune vs RAG decision writeup |
| D10 | Full five-room walk; **Mock B** | No new material; sleep |

### D.5 Honest caveats

1. **Mocks beat palace** for exam-like checks (MoL GRADE low–low).
2. Mnemonics are pointers, not understanding.
3. **TAP:** timed mocks > passive re-read.
4. ~2 items per locus max.
5. Sleep beats one more chapter.
6. Cross-domain chains in this guide are `[inferred]` pedagogical links, not author claims.
7. **Abort rule:** if Day 2 palace recall <30%, rebuild with simpler space before adding rooms.
8. Figures require EPUB/PDF — exports lack diagrams.

### D.6 Sources

- Ondrej J. et al. (2025). Method of loci meta-analysis. PMC12514325.
- Serra M.J. et al. (2025). Retrieval practice in health professions. PMC12292765.
- Roediger H.L., Karpicke J.D. (2006). Test-enhanced learning.
- Morris C.D. et al. (1977). Transfer appropriate processing.
- Paivio A. (1971). Imagery and Verbal Processes.
- Bjork R.A. (1994). Desirable difficulties.
