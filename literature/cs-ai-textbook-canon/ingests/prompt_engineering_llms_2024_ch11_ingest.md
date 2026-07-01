# Chapter ingest — `prompt_engineering_llms_2024` · Chapter 11

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
| **chapter_number** | 11 |
| **chapter_title** | Looking Ahead |
| **page_range** | Printed page numbers absent from text export; logical span Ch. 11 opening through book Conclusion (L10542–10611); Index/colophon deferred |
| **parent_book_title** | Prompt Engineering for LLMs |

## Scope

Final chapter forecasts **multimodality**, **UX/stateful discourse**, and **intelligence trends**, then restates the book's two core lessons. Opens with logarithmic-acceleration framing (GPT-2 2019 → ChatGPT 2022 → agents/tools).

**Multimodality**: GPT-4 image-in-prompt; likely CNN embeddings + positional image vectors concatenated with text tokens through transformer (Ch. 2 callback); video via sampled frames (OpenAI cookbook). Use cases: accessibility/vision impairment; richer training data mitigating **text corpus exhaustion** and overfitting/memorization—images/video add spatial/social/physical-common-sense signal. Prompt-engineering carryover: relevant images only, textual framing, use training-familiar diagram formats not novel ones.

**User Experience and User Interface**: conversational UI momentum (200k years speech vs 40 years clicking); **artifacts / stateful objects of discourse**—pair-programming files as evolving referents vs ChatGPT rewriting functions from scratch each turn. **Anthropic Artifacts** (near publication): stateful right-pane object (SVG, HTML, mermaid, code) updated in place while transcript on left; limitations flagged: UI-level state (full rewrite not true edit), one artifact at a time, weak multi-artifact reference, no direct user edit propagation to model. Build conversational UIs deliberately—not bare gimmicks. Tools enabled action; artifacts enable talking *about* things; conversation keeps users correcting drift (Ch. 8 callback).

**Intelligence**: benchmark **saturation** (Figure 11-2)—models ace MMLU-like sets; causes: genuine improvement vs **benchmark contamination** via web duplication; responses include Open LLM Leaderboard 2 upgrades and **ARC-AGI** (non-memorizable psychometric pattern tests). **RLHF** improves visible chain-of-thought. **Knowledge distillation**: small models mimic teacher full next-token distributions—cheaper/faster slight accuracy tradeoff. **Quantization** (32→8 bit) for size/speed. Prompt-engineering implication: cost/context/smartness improve over time but **models never psychic**—missing prompt info still missing.

**Conclusion (book)**: Two lessons—(1) LLMs are text-completion engines mimicking training documents (chat/tools/artifacts as document shapes); (2) **empathize** with the model (not distracted, prompt decipherable, led explicitly, non-psychic, needs externalized monologue). Future: individualized/disposable apps, nondeterministic UX, human-AI tandem development. Terry Pratchett closing quote.

**Sections ingested:** Multimodality · UX/UI (artifacts) · Intelligence · Book Conclusion.

**Deferred:** Index (L10618+), About the Authors, Colophon—not chapter prose.

Cross-refs: Ch. 2 (transformer), Ch. 3 (RLHF), Ch. 4 (Little Red Riding Hood), Ch. 8 (course correction, tools).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Multimodality

- Image tokens embedded like text; video as sampled frames. [verified from text, lines 10334–10348]
- Multimodal training expands data beyond "entire public internet" text limit. [verified from text, lines 10357–10371]
- Include only relevant images; frame with familiar formats from training. [verified from text, lines 10373–10382]

### Artifacts and UX

- ChatGPT rewrites code objects rather than maintaining stateful referents. [verified from text, lines 10401–10412]
- Claude Artifacts: stateful side-pane object; still rewrites whole artifact internally. [verified from text, lines 10414–10451]
- Conversational UI needs investment to avoid gimmick status. [verified from text, lines 10453–10458]

### Intelligence trends

- Benchmark saturation from real gains and accidental training contamination. [verified from text, lines 10477–10498]
- Knowledge distillation and quantization continue cost/capability trends. [verified from text, lines 10510–10530]
- Models won't infer facts absent from prompt regardless of scale. [verified from text, lines 10532–10540]

### Book thesis recap

- Core: completion engines + empathy/Little Red Riding Hood + no psychic models + externalized reasoning. [verified from text, lines 10544–10596]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/prompt_engineering_llms_2024.txt` |
| **Lines read** | 10310–10611 (chapter prose); L10612–11763 scanned for boundary only |
| **Chapter boundary** | Starts `Chapter 11. Looking Ahead` (L10310); prose ends book Conclusion (L10611); Index starts L10618 |
| **Wrong-file flag** | `false` |
| **Sections deferred** | Index, author bios, colophon |
| **Figures** | Figs. 11-1–11-2 referenced |
| **Amnesiac rule** | Forward-looking claims tagged as author forecast |

## Pedagogy

### Learning objectives

1. Explain multimodal prompt design constraints (relevance, framing, familiar formats).
2. Contrast stateless chat regeneration vs artifact/stateful discourse UX.
3. Critique benchmark saturation and contamination in model selection.
4. Articulate the book's two core lessons and their prompt-engineering implications.
5. `[inferred]` Separate dated product features (Artifacts) from durable patterns (stateful referents).

### worked_examples_present

**N** (conceptual/forward-looking)—Figure 11-1 pirate SVG artifact demo described; no step-by-step lab.

### exercise_hooks

- **Instructor hooks `[inferred]`:**
  - Design artifact-aware UI mock for multi-file pair programming.
  - Audit a multimodal prompt for training-format alignment.
  - Compare ARC-AGI vs MMLU for a model-selection decision memo.

## Operator hooks

### 1. Foundation layer

Ch. 11 is **w2_systems_llm horizon/closure**—not procedural canon; use for SYNTHESIS "future tracks" and trainer session openers. Restates PE thesis for index cards; pair with **ai_engineering_2025** forward chapters on monitoring/multimodality when shipped.

### 2. MDCalc alignment

**[peripheral]** — Multimodal accessibility and artifact UX are general product patterns; no clinical deployment claims.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **hands_on_llms_2024** | Low | Multimodal tutorials may supersede dated product refs |
| **ai_engineering_2025** | Low | Eval/benchmark overlap with Ch. 4 |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Weak** — outlook chapter |
| Exercise hooks | **Inferred only** |
| Chapter boundary | **Clean** for prose; index excluded |
| Ingest suitability | **Medium** — recency-risk on product features |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** with **[RECENCY RISK]** | Artifacts/leaderboards may stale quickly |
| **Author authority** | **PASS** | Practitioner foresight |
| **Citation density** | **Moderate** | ARC-AGI, OpenAI cookbook refs; less dense than Ch. 8–10 |
| **Contested claims** | **PASS** | Artifact limitations acknowledged |
| **Worked examples** | **PARTIAL** | Conceptual figures only |

**Overall TEXTBOOK-Q1:** **PASS** — flag product-specific rows for periodic re-verify

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PE-C11-001 | LLMs remain text-completion engines under chat/tool/artifact skins | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch11_ingest.md | Conclusion |
| PE-C11-002 | Benchmark saturation mixes real gains and training contamination | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch11_ingest.md | Intelligence |
| PE-C11-003 | Artifacts enable stateful objects of discourse vs transcript-only rewrite | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch11_ingest.md | UX/UI |
| PE-C11-004 | Models cannot solve problems without prompt-contained information | compressed | Prompt Engineering for LLMs 1e | ISBN 978-1-098-15615-2 | literature/cs-ai-textbook-canon/ingests/prompt_engineering_llms_2024_ch11_ingest.md | Intelligence |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
