# Chapter ingest — `prompt_engineering_llms_2024` · Chapter 7

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Prompt Engineering for LLMs |
| **authors** | John Berryman, Albert Ziegler |
| **edition** | 1st Edition (2025 copyright; first release 2024-11-04 per revision history) |
| **ISBN_print** | 978-1-098-15615-2 |
| **ISBN_electronic** | 978-1-098-15615-2 (single ISBN in export; O'Reilly online edition) |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 7 |
| **chapter_title** | Taming the Model |
| **page_range** | Printed page numbers absent from text export; logical span Ch. 7 opening through Conclusion (before Part III) |
| **parent_book_title** | Prompt Engineering for LLMs |

## Scope

Chapter 7 closes Part II (core prompt engineering) by shifting from prompt assembly (Ch. 5–6) to **completion control**, **logprob analytics**, **model selection**, and an **intro to fine-tuning**. It assumes the reader has distilled context into a single coherent prompt and now must ensure the model's output is parseable, cost-efficient, and trustworthy.

**Anatomy of the Ideal Completion** decomposes completions into preamble types—**structural boilerplate** (prefer deterministic prompt placement), **reasoning** (CoT preambles as virtue; long preamble can yield correct short answer), and **fluff** (RLHF verbosity; banish via format tricks like "main answer first, extras in point 2"). **Recognizable start/end** (Table 7-1) maps document structures (Markdown, YAML, JSON, code fences, numbered lists) to parse strategies; substring vs bracket-matching tradeoffs. **Postscript** control via **stop sequences** (OpenAI-style; `\n#` tip) vs **streaming + cancellation** (less savings; combine partial stop sequences like `\nclass`, `\ndef` with indentation awareness).

**Beyond the Text: Logprobs** treats logprobs as model "tone of voice": sum/average for quality; early-token probability average (Copilot insight) as predictor; application cutoffs (confidence gates, warnings, retry, model swap, Clippy avoidance); `n` completions with `temperature ≈ sqrt(n)/10` tip. **LLMs for Classification** covers yes/no and multilabel via constrained formats; **unique first-token** requirement (North America vs Northeast Asia collision example on gpt-3.5-turbo-instruct); **calibration** via logprob shifts or **logit bias**; **echo=true** for prompt surprise/typo detection (Figure 7-6); non-deterministic logprob unit-test warning (±1).

**Choosing the Model** lists decision axes (intelligence, speed, cost, ease of use, functionality, special requirements) with Figure 7-7 tradeoff examples; provider survey (OpenAI, Anthropic, Mistral, Cohere, Google, Meta); open-weight hosting caveats; **smallest model that reliably works**; prototype larger, expect price drops; **LiteLLM** for swappable APIs. **Fine-tuning primer**: full/continued pre-training vs **LoRA** vs **soft prompting** (Table 7-2); loss masking; fine-tuning as "prompt engineering by other means"; modified **Little Red Riding Hood** for fine-tuned vs original training paths.

**Sections ingested:** Anatomy of the Ideal Completion · Beyond the Text: Logprobs · Choosing the Model · Conclusion.

Cross-refs: Ch. 2 (token probabilities), Ch. 4 (CoT, Little Red Riding Hood), Ch. 5 (urgency Table 5-2), Ch. 6 (prompt patterns), Ch. 8 (advanced reasoning preambles).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Completion anatomy and parsing

- Three preamble types: structural boilerplate, reasoning, fluff—each with different cost/value tradeoffs. [verified from text, lines 6163–6210]
- CoT reasoning in preamble can be longer than answer yet improve correctness (Figure 7-2). [verified from text, lines 6183–6192]
- Table 7-1: recognizable boundaries for Markdown, YAML, JSON, code fences, numbered lists, bracket/indent languages. [verified from text, lines 6234–6246]
- Stop sequences often need leading `\n`; streaming cancellation saves less than server-side stop. [verified from text, lines 6274–6306]
- Tip: add `\nclass`, `\ndef`, `\nif` as partial stops; indented `\n\tdef` won't false-trigger. [verified from text, lines 6310–6318]

### Logprobs

- Logprob 0 = certainty; exp converts to probability (Yes/No example ~66%/33%). [verified from text, lines 6331–6337]
- Some commercial APIs disable logprobs (reverse-engineering fear). [verified from text, lines 6348–6351]
- Average logprobs or early-token probability average as quality proxy—not absolute measure. [verified from text, lines 6379–6403]
- Classification: ensure each option starts with unique token to avoid merged probabilities. [verified from text, lines 6455–6474]
- Calibration: shift logprobs by constants or use logit bias API. [verified from text, lines 6489–6512]
- echo=true surfaces prompt typos via extreme negative logprobs. [verified from text, lines 6518–6527]

### Model selection and fine-tuning

- Don't hard-code model choice; use abstraction (LiteLLM). [verified from text, lines 6568–6571]
- Six-axis selection ordered intelligence → special requirements; 2024 field "more even" vs OpenAI dominance. [verified from text, lines 6577–6647]
- Smallest reliable model; prototype slightly larger expecting price drops. [verified from text, lines 6697–6707]
- Full fine-tuning: tens of thousands examples, weeks/months, new domains. LoRA: hundreds–thousands, days, format/style/prior shifts. Soft prompting: hundreds, hours. [verified from text, lines 6751–6829]
- Fine-tuned Little Red Riding Hood: prompt should resemble fine-tune docs, not original training docs. [verified from text, lines 6834–6849]
- Chapter marks end of "core prompt-engineering techniques"; Part III covers agents/workflows. [verified from text, lines 6867–6873]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt` |
| **Lines read** | 6123–6876 (inclusive) |
| **Chapter boundary** | Starts `Chapter 7. Taming the Model` (L6123); ends before `Part III. An Expert of the Craft` / Ch. 8 (L6877) |
| **Wrong-file flag** | `false` — slug matches `prompt_engineering_llms_2024` |
| **Sections deferred** | Ch. 8+ forward refs only; fine-tuning depth beyond primer |
| **Figures** | Figs. 7-1–7-8, Tables 7-1–7-2 referenced; image data `[]` in export |
| **Amnesiac rule** | No claims from training prior; ISBN from L59 and front matter |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Classify completion preambles and choose when reasoning vs fluff is desirable.
2. Design recognizable start/end markers and stop sequences for programmatic parsing.
3. Use logprobs for quality scoring, classification calibration, and prompt anomaly detection.
4. Apply the six-axis model-selection framework and avoid baking in a single provider.
5. Compare full fine-tuning, LoRA, and soft prompting by data volume, duration, and use case.
6. Adapt the Little Red Riding Hood principle for fine-tuned models.

### worked_examples_present

**Y** — Tables, figures, classification collision example, thermostat-adjacent parsing tips, fine-tuning comparison table.

| Example | Section | Role |
|---------|---------|------|
| Figure 7-2 long vs short preamble | Preamble | CoT correctness |
| Table 7-1 start/end recognition | Recognizable Start and End | Parser design |
| Astrophysicist vs child logprob analogy | Logprobs | Confidence metaphor |
| North America / Northeast Asia / Europe | Classification | Token collision |
| Email professionalism calibration | Classification | Logit bias |
| Figure 7-6 typo logprobs | Critical Points | Prompt QA |
| Table 7-2 fine-tuning types | Choosing the Model | Method selection |
| European travel LoRA example | LoRA | Prior distribution shift |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Implement stop-sequence parser for JSON field extraction from completions.
  - Build calibrated binary classifier with logprobs + held-out threshold tuning.
  - Compare three model tiers on same prompt; record latency/token cost matrix.
  - Draft fine-tune vs prompt-engineering decision tree for a domain task.

## Operator hooks

### 1. Foundation layer

Ch. 7 is **w2_systems_llm completion-control canon** for *Prompt Engineering for LLMs*—bridges Part II prompt craft to Part III agents (Ch. 8–9) and evaluation (Ch. 10). Pairs with **ai_engineering_2025** Ch. 4 (eval/logprobs) and Ch. 7–9 (finetuning/inference) at the systems layer; **hands_on_llms_2024** for API implementation. Load before agent/workflow chapters.

### 2. MDCalc alignment

**[peripheral]** — Logprob confidence gates and classification calibration are general ML-ops patterns; no clinical claims. Useful for regulated apps needing auditable confidence thresholds on structured LLM outputs.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **ai_engineering_2025** Ch. 4 | Medium | Logprobs, eval—AIE deeper on pipeline; PE Ch. 7 on completion parsing |
| **hands_on_llms_2024** | Medium | API tutorials vs PE framework |
| **llmops_aryan_2025** | Low | Production routing/cost |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** |
| Exercise hooks | **Weak in text** |
| Chapter boundary | **Clean** |
| Ingest suitability | **High** |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2024–2025 O'Reilly; Copilot-practitioner authors |
| **Author authority** | **PASS** | GitHub Copilot founding engineers |
| **Primary-source citation density** | **PASS** | PaLM/CoT cross-refs; gpt-3.5-turbo-instruct empirical note |
| **Contested claims flagged** | **PASS** | Logprob as quality proxy limitations; model recommendations explicitly stale-prone |
| **Worked examples** | **PASS** | Tables, classification walkthrough, fine-tuning matrix |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PE-C07-001 | Three preamble types govern parse/cost tradeoffs | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch07_ingest.md | Anatomy of the Ideal Completion |
| PE-C07-002 | Unique first-token required for LLM classification options | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch07_ingest.md | LLMs for Classification |
| PE-C07-003 | Stop sequences preferred over stream cancel for cost control | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch07_ingest.md | Postscript |
| PE-C07-004 | LoRA learns format/prior within domain; full FT for new domains | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch07_ingest.md | Table 7-2 |
| PE-C07-005 | Fine-tuning modifies Little Red Riding Hood path selection | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch07_ingest.md | Conclusion |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
