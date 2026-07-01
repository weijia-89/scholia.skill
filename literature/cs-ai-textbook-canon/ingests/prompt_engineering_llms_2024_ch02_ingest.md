# prompt_engineering_llms_2024 — Chapter 02 ingest

| Field | Value |
|-------|-------|
| slug | prompt_engineering_llms_2024 |
| chapter_number | 2 |
| chapter_title | Understanding LLMs |
| parent_book_title | Prompt Engineering for LLMs |
| authors | Berryman, Johnathan; Ziegler, Albert |
| edition | 1e (2024) |
| ISBN_print | 9781098156145 (manifest) |
| source_type | textbook_chapter |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch02_ingest.md |
| text_lines_read | 757–1805 |
| page_range | not recoverable from text export |

---

## Scope

Chapter 2 is the **operational mental model** for prompt engineers: LLMs as trained document mimics, token processors, autoregressive generators, and unidirectional transformers. “Onion” structure: what LLMs are → how they see tokens → one-token-at-a-time generation → temperature/sampling → transformer attention and prompt-order implications.

Subsections: What Are LLMs? · Fine-tuning sidebar · Completing a Document · Human Thought vs LLM Processing · Hallucinations · How LLMs See the World (tokenizer differences) · Counting Tokens · One Token at a Time · Temperature and Probabilities · The Transformer Architecture · Conclusion.

Explicit bridge to Ch 3 (doubt/alignment), Ch 6 (prompt order), Ch 7 (fine-tuning), Ch 8 (tools, CoT).

---

## Key findings

All items `[verified from text]` unless tagged `[inferred]`.

1. **Core metaphor.** Ask: “How would a document starting with this prompt continue?” not “How would a person reply?” (L868–880)

2. **Training set shapes output.** TV repair example: narrative prose vs support transcripts change plausible continuations (davinci-003). (L882–945)

3. **No google/edit.** Models guess URLs, names, facts; language reflects training patterns not reality (curie-001 podcast URL). (L947–994)

4. **Hallucinations.** Indistinguishable to model from valid completions; “don’t make stuff up” weak; verify via checkable details; truth bias accepts false premises. (L996–1048)

5. **Tokenization.** LLMs use tokens not characters; deterministic tokenizers; poor at letter-level tasks (reversal, “how many Rs in strawberry”); capitalization costs extra tokens (gone vs G+ONE). Pre/post-process subtoken tasks. (L1050–1216)

6. **Token economics.** ~4 chars/token English (GPT tokenizer); worse for digits/unicode; context window = hard cap; count tokens in apps (tiktoken/HF). Pricing per token. (L1218–1277)

7. **Autoregression.** One token per forward pass; no backtrack; repetition traps; application must supply correction/backtracking. (L1279–1364)

8. **Temperature.** 0 = greedy/deterministic-ish; 0.1–0.4 light creativity; 0.5–0.7 many samples; 1 = training distribution; >1 degrades. Table 2-1 tradeoffs. Beam search noted. (L1366–1509)

9. **Transformer minibrains.** Per-token layers; attention Q&A left-to-right only; “backward-and-dumbward” limits in-layer reasoning depth; **chain-of-thought = thinking aloud** across tokens (Ch 8). (L1511–1692)

10. **Prompt order.** Word-count task fails when question after text; better when question first—order critical (Ch 6 return). Human expert test: single pass without notes? (L1694–1732)

11. **Four facts summary.** Document completion; mimic training; one token at a time; single left-to-right read. (L1734–1742)

---

## Coverage attestation

| Section | In slice (L757–1805) | Notes |
|---------|----------------------|-------|
| What Are LLMs / fine-tuning | yes | The Pile fig placeholder |
| Document completion reasoning | yes | TV examples |
| Hallucinations / truth bias | yes | Tips |
| Tokenizer differences | yes | Figs 2-4–2-8 |
| Counting tokens | yes | Context window |
| Autoregression / repetition | yes | Fig 2-10 |
| Temperature / logprobs | yes | Formula + Table 2-1 |
| Transformer / attention | yes | Figs 2-14–2-15 |
| Conclusion + footnotes ¹–¹⁵ | yes | |
| Chapter 3 opener | excluded | L1806+ |

**wrong-file flag:** false.

---

## Pedagogy

### learning_objectives

- Predict completions using training-set mimicry, not human reply intuition. `[verified from text]`
- Explain tokenizer pitfalls and when to pre/post-process. `[verified from text]`
- Choose temperature regimes for correctness vs diversity. `[verified from text]`
- Relate unidirectional attention to prompt ordering and CoT. `[verified from text]`

### worked_examples_present

**Y** — TV/document continuations; Acast URL confabulation; letter reversal; all-caps failure; repetition list; temperature alcohol metaphor; “One, Two, Buckle My Shoe” transformer walkthrough; word-count ordering.

### exercise_hooks

| ID | Archetype | Scholia hook |
|----|-----------|--------------|
| PE-2.1 | Mimicry probe | Same prompt, reason as human vs as document continuation |
| PE-2.2 | Token task boundary | Letter-reverse vs list-filter pre-processing split |
| PE-2.3 | Temperature sweep | List generation at 0 vs 1; measure length/repetition |
| PE-2.4 | Order ablation | Place task instruction before/after long context |
| PE-2.5 | Logprob read | Request top_logprobs; flag low-confidence spans |

---

## Operator hooks

### 1. Foundation layer

**w2 mechanics spine** — required before PE Ch 5–6 assembly and AIE Ch 5 eval hooks. Explains why HOTL Ch 6 sampling table and lost-in-middle tip have theoretical basis here.

### 2. MDCalc alignment

**Partial** — Hallucination “trust but verify” maps to clinical fact-checking; abstention not native to base LLM. `[inferred]`

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| ai_engineering_2025 Ch 5 | Partial | AIE cites NIAH/Liu; PE Ch2 derives from transformer mechanics + tokenizer |
| hands_on_llms_2024 Ch 6 | **High** on sampling | HOTL Table 6-1 temp/top_p; PE Ch2 deeper on logprobs + autoregression theory |
| hands_on_llms_2024 Ch 1–2 | Partial | HOTL transformer intro; PE Ch2 PE-oriented depth |

**Dedup:** PE Ch2 for **document-mimic + attention-order theory**; HOTL Ch6 for **executable Phi-3 sampling labs**.

### 4. Scholia fit

- **Worked examples:** Y
- **Chapter boundary:** Clean; footnotes carry nuance

---

## TEXTBOOK-Q1 gate

| Criterion | Verdict |
|-----------|---------|
| Edition currency | **PASS** |
| Author authority | **PASS** |
| Citation density | **PASS** (Liu lost-in-middle foreshadow; Illustrated Transformer ref) |
| Contested flagged | **PASS** |
| Worked examples | **PASS** |

**Overall:** **PASS**

### Contested claims

1. **Confabulation vs hallucination** — Footnote prefers confabulation label (L1767–1768).
2. **Temperature 0 deterministic** — Rounding noise caveat (L1790–1793).
3. **Strawberry R-count** — Recency-tagged “autumn 2024” model limits (L1057–1059).

---

## Anchor index

| Topic | Lines |
|-------|-------|
| Chapter start | 757 |
| Mimicry / hallucinations | 882–1048 |
| Tokenizer | 1050–1216 |
| Autoregression | 1279–1364 |
| Temperature | 1366–1509 |
| Transformer | 1511–1732 |
| Conclusion | 1734–1805 |

---

## Cross-chapter dependencies

- **Requires:** Ch 1 (GPT/PE framing).
- **Enables:** Ch 3 (alignment), Ch 4 (loop), Ch 6 (order), Ch 7–8 (CoT, tools).

---

*Ingest from L757–1805. Word cap: ≤4500.*
