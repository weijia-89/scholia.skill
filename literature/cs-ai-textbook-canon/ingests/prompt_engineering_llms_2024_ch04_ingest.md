# prompt_engineering_llms_2024 — Chapter 04 ingest

| Field | Value |
|-------|-------|
| slug | prompt_engineering_llms_2024 |
| chapter_number | 4 |
| chapter_title | Designing LLM Applications |
| parent_book_title | Prompt Engineering for LLMs |
| authors | Berryman, Johnathan; Ziegler, Albert |
| edition | 1e (2024) |
| source_type | textbook_chapter |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch04_ingest.md |
| text_lines_read | 2776–3707 |
| page_range | not recoverable from text export |

---

## Scope

Chapter 4 introduces the **LLM application loop**: user problem domain ↔ text/transcript domain. One trip around the loop: problem dimensions (Table 4-1), conversion criteria (Little Red Riding Hood principle), homework travel example (Table 4-2), model selection, reverse transform, feedforward pass (retrieve → snippetize → score → assemble), complexity axes (state, RAG, CoT, tools, eval).

Gateway to Part II core techniques (Ch 5–6).

---

## Key findings

All items `[verified from text]` unless tagged `[inferred]`.

1. **Loop anatomy.** User variety vs model’s single capability—complete documents; chat/tools = specialized transcripts. Stateful single-shot vs multi-iteration travel planner. (L2797–2847)

2. **Problem dimensions (Table 4-1).** Medium, abstraction, context, statefulness—proofreading vs IT support vs travel planning. (L2854–2931)

3. **Four conversion criteria.** (1) Resemble training data. (2) Include all relevant info. (3) Condition helpful completion. (4) Natural stop / endpoint. (L2933–3040)

4. **Little Red Riding Hood principle.** Mimic training document types; ask model what formal docs exist; markdown motifs in chat user messages. (L2954–2995)

5. **Context saturation risk.** Too much loose context distracts model. (L3008–3013)

6. **GitHub im_end bug.** Suppressed end token → infinite salutations until max_tokens—stop behavior matters. (L3042–3057)

7. **Homework travel prompt (Table 4-2).** Few-shot problem/solution pattern; State Dept + news context; `## Solution 2` transition; stop=`\n#`. North Korea → discourage travel. (L3059–3163)

8. **Chat simplifies criteria 1,3,4** but engineer still owns context + shaping (L3165–3185).

9. **Model choice.** Size/cost/latency (GPT-4 20× 3.5); Codex for Copilot speed; fine-tuning for rare languages—defer Ch 7. (L3217–3250)

10. **Reverse transform.** Parse structured output; function-calling travel booking; medium shift (speech/UI); Copilot grey text vs diff. (L3252–3303)

11. **Feedforward steps (Fig 4-2).** Direct/indirect/boilerplate context; snippetize; priority tiers vs float scores; assemble under token budget; elide/summarize. (L3305–3417)

12. **State.** Chat history DB; truncate vs summarize. (L3437–3459)

13. **RAG.** Embeddings + vector store vs Elasticsearch; query spectrum (user text → LLM query → tool search). (L3461–3499)

14. **CoT.** “Think step by step” = out-loud reasoning for unidirectional model (Ch 4 preview). (L3501–3536)

15. **Tools / ReAct.** Read/write APIs; probabilistic risk on bookings. (L3538–3590)

16. **Eval.** Offline (Copilot test deletion proxy; LLM-as-judge); online telemetry—accept rate, implicit signals; evaluate full app not prompt-only. (L3592–3680)

---

## Coverage attestation

| Section | In slice (L2776–3707) | Notes |
|---------|------------------------|-------|
| Loop + Table 4-1 | yes | |
| Conversion criteria + LRH | yes | |
| Homework example | yes | Table 4-2 |
| Feedforward pass | yes | Fig 4-2 |
| State / RAG / CoT / tools | yes | |
| Eval offline/online | yes | |
| Conclusion | yes | |
| Part II / Ch 5 opener | excluded | L3708+ |

**wrong-file flag:** false.

---

## Pedagogy

### learning_objectives

- Draw the user↔model loop and four problem dimensions. `[verified from text]`
- Apply four prompt conversion criteria to a use case. `[verified from text]`
- Design feedforward: retrieve, snippetize, score, assemble. `[verified from text]`
- Plan offline/online eval metrics for an app. `[verified from text]`

### worked_examples_present

**Y** — Travel homework Table 4-2; im_end runaway; Copilot eval repos; function-call travel; Fig 4-1–4-3 placeholders.

### exercise_hooks

| ID | Archetype | Scholia hook |
|----|-----------|--------------|
| PE-4.1 | LRH doc mimic | Pick training-doc genre for domain task |
| PE-4.2 | Homework ablation | Reproduce Table 4-2 “Now You Try” five variants |
| PE-4.3 | Snippet budget | Tier priorities under fixed token cap |
| PE-4.4 | RAG query ladder | User query vs LLM-rewritten query retrieval |
| PE-4.5 | Eval proxy | Define acceptance metric for non-code app |

---

## Operator hooks

### 1. Foundation layer

**w2 application architecture** — maps to AIE Ch 6 RAG/agents at production layer; PE Ch 5–6 implement feedforward detail. DDIA/UDS workers: reference loop only at orchestration.

### 2. MDCalc alignment

**Partial** — RAG over clinical corpus; eval telemetry for safety-critical flows. `[inferred]`

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| ai_engineering_2025 Ch 5 | Partial | AIE Ch5 prompt craft; PE Ch4 **application loop + RAG/eval** |
| ai_engineering_2025 Ch 6 | **High** on RAG preview | PE Ch4 introduces RAG; AIE Ch6 depth |
| hands_on_llms_2024 Ch 6 | Low | HOTL model I/O not app loop |

**Dedup:** PE Ch4 for **loop + feedforward pipeline**; PE Ch5–6 for content/assembly; AIE for production security.

### 4. Scholia fit

- **Worked examples:** Y
- **Boundary:** Clean gateway to Part II

---

## TEXTBOOK-Q1 gate

**PASS**

### Contested claims

1. **GPT-4 20× cost** — “At time of writing” pricing (L3228–3231).
2. **Elasticsearch vs vectors** — Author bias toward debuggable lexical search (L3482–3485).

---

## Anchor index

| Topic | Lines |
|-------|-------|
| Chapter start | 2776 |
| Loop / Table 4-1 | 2797–2931 |
| Four criteria / LRH | 2933–2995 |
| Homework example | 3059–3215 |
| Feedforward | 3305–3417 |
| RAG / tools / eval | 3461–3680 |
| Conclusion | 3682–3707 |

---

## Cross-chapter dependencies

- **Requires:** Ch 2–3.
- **Enables:** Ch 5 (content), Ch 6 (assembly), Ch 8–10 (tools, eval).

---

*Ingest from L2776–3707. Word cap: ≤4500.*
