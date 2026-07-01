# prompt_engineering_llms_2024 — Chapter 03 ingest

| Field | Value |
|-------|-------|
| slug | prompt_engineering_llms_2024 |
| chapter_number | 3 |
| chapter_title | Moving to Chat |
| parent_book_title | Prompt Engineering for LLMs |
| authors | Berryman, Johnathan; Ziegler, Albert |
| edition | 1e (2024) |
| source_type | textbook_chapter |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch03_ingest.md |
| text_lines_read | 1806–2775 |
| page_range | not recoverable from text export |

---

## Scope

Chapter 3 explains **RLHF chat models** as still document completion—now on ChatML transcripts. Covers base-model limits, HHH alignment, SFT→reward→RLHF pipeline (InstructGPT/GPT-3 scale), instruct vs chat ambiguity, ChatML roles/tags, chat API (97% traffic by Jul 2023), completion API tradeoffs, tools preview, and **playwriting metaphor** (multiple playwrights: engineer, user, LLM, APIs).

Subsections: RLHF · Building RLHF models (Tables 3-3–3-4) · Chat Models / ChatML · Changing API · Chat vs Completion · Tools · Prompt Engineering as Playwriting · Conclusion.

Bridges Ch 4 (application loop), Ch 8 (tools), Ch 6 (transcript assembly).

---

## Key findings

All items `[verified from text]` unless tagged `[inferred]`.

1. **Base model behavior.** Completes arbitrary internet documents—unsafe or unhelpful (recipe vs meth steps; question lists). (L1808–1857)

2. **HHH alignment.** Helpful, honest, harmless (Anthropic 2021). (L1930–1942)

3. **RLHF stack (Table 3-3).** Base GPT-3 → SFT (~13k demos) → reward model (ranked pairs, ~33k docs) → RLHF policy (~31k). Four models, three fine-tunes. (L1944–2034)

4. **SFT lying problem.** SFT improves instruction-following but quality issues motivate reward model. (L1978–1981)

5. **Instruct ambiguity.** Mixed completion/instruct training blurs modes; need unambiguous chat format. (L2247–2260)

6. **ChatML.** `<|im_start|>{system|user|assistant}` + end tokens; system sets behavior; API strips/forges reserved tokens—users cannot inject roles. **Never put user content in system message.** (L2264–2465)

7. **Chat API dominance.** OpenAI Jul 2023: 97% chat vs completions; Python `ChatCompletion.create` example; Table 3-5 params (temperature, n, stop, stream, logprobs). (L2378–2482)

8. **Alignment tax.** Chat specialization may degrade other tasks (Stanford GPT-4 drift paper cited); chatty/refusal-heavy vs terse code extraction. Completion APIs excel at fenced code + stop=` ``` `. (L2528–2595)

9. **Tools still documents.** Tool transcripts extend ChatML; detail deferred Ch 8. (L2597–2615)

10. **Playwriting metaphor.** Parallel conversations: end-user vs app↔model transcript; Table 3-6 shows engineer fabricating context user never said. (L2617–2716)

11. **DIY exercise.** Build chat + tool calling atop completion model = 2024 Copilot interview level. (L2718–2748)

12. **Conclusion.** Assistants are documents; limited context for engineer. (L2750–2774)

---

## Coverage attestation

| Section | In slice (L1806–2775) | Notes |
|---------|------------------------|-------|
| Base vs aligned behavior | yes | Tables 3-1–3-2 |
| RLHF pipeline | yes | Tables 3-3–3-4 |
| ChatML + injection | yes | Fork bomb example |
| Chat API + params | yes | Table 3-5 |
| Chat vs completion | yes | Code fence example |
| Playwriting / Table 3-6 | yes | |
| Conclusion | yes | |
| Chapter 4 opener | excluded | L2776+ |

**wrong-file flag:** false.

---

## Pedagogy

### learning_objectives

- Diagram SFT → reward → RLHF and HHH goals. `[verified from text]`
- Explain ChatML role separation and system-message injection risk. `[verified from text]`
- Compare when completion API beats chat for parseable outputs. `[verified from text]`
- Map playwriting roles to production prompt assembly. `[verified from text]`

### worked_examples_present

**Y** — Chicken/meth completion contrast; Jeeves system message; sobriety-test temperature lab; highlighted_code Table 3-6; Chat API JSON response.

### exercise_hooks

| ID | Archetype | Scholia hook |
|----|-----------|--------------|
| PE-3.1 | System boundary | Attempt user-controlled system injection via API vs chat roles |
| PE-3.2 | Completion vs chat | Same code-gen task; compare parse effort |
| PE-3.3 | Temperature dialogue | Reproduce n=10 sobriety prompt at T=0 vs 1 |
| PE-3.4 | Playwright audit | Log which transcript lines end-user never typed |

---

## Operator hooks

### 1. Foundation layer

**w2 chat/RLHF spine** — prerequisite for PE Ch 6 sandwich prompts and AIE Ch 5 system/user splits. Pairs with HOTL Ch 6 `apply_chat_template` exercises.

### 2. MDCalc alignment

**Partial** — System-message hygiene and injection map to clinical assistant hardening; jailbreak awareness overlaps AIE Ch 5 defensive section. `[inferred]`

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| ai_engineering_2025 Ch 5 | **High** on system/user + injection | AIE adds Wallace hierarchy, PAIR; PE Ch3 explains RLHF/ChatML genesis |
| hands_on_llms_2024 Ch 6 | Partial | HOTL chat templates procedural; PE Ch3 theory + API |
| prompt_engineering_llms_2024 Ch 6 | Enables | Sandwich technique assumes ChatML from here |

**Dedup:** PE Ch3 for **RLHF pipeline + playwriting**; AIE Ch5 for **production security catalog**.

### 4. Scholia fit

- **Worked examples:** Y
- **Boundary:** Clean through Ch 4 handoff

---

## TEXTBOOK-Q1 gate

**PASS** — 2024 O'Reilly; dense primary refs (Ouyang et al. InstructGPT); contested items flagged.

### Contested claims

1. **Bing/Sydney prompt table** — Extracted by jailbreaker; overlap unconfirmed (L3840–3842 analogue in Ch5; Ch3 cites RLHF not Bing).
2. **97% chat traffic** — OpenAI 2023 statement; may date.
3. **Alignment tax magnitude** — Stanford paper cited cautiously (L2540–2546).

---

## Anchor index

| Topic | Lines |
|-------|-------|
| Chapter start | 1806 |
| RLHF / HHH | 1897–2034 |
| ChatML | 2262–2376 |
| Chat API | 2395–2517 |
| Chat vs completion | 2528–2595 |
| Playwriting | 2617–2707 |
| Conclusion | 2750–2775 |

---

## Cross-chapter dependencies

- **Requires:** Ch 2 (temperature, document completion).
- **Enables:** Ch 4–6 (loop, assembly), Ch 8 (tools).

---

*Ingest from L1806–2775. Word cap: ≤4500.*
