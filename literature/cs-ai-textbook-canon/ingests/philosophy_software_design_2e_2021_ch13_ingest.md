# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 13

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | A Philosophy of Software Design |
| **authors** | John Ousterhout |
| **edition** | 2nd Edition (v2.0, July 2021) |
| **ISBN_print** | 978-1-7321022-1-7 |
| **ISBN_electronic** | not stated separately in source text (print ISBN only; epub/mobi noted without distinct ISBN) |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 13 |
| **chapter_title** | Comments Should Describe Things that Aren't Obvious from the Code |
| **page_range** | Printed page numbers absent from text export; logical span §13.1–§13.9 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 13 argues that **comments exist because programming languages cannot capture all information in the developer's mind** at write time. The guiding principle: **comments should describe things that aren't obvious from the code**—including low-level precision (inclusive vs exclusive ranges), rationale, implicit rules, and especially **abstractions** that users must understand without reading implementation. Ousterhout prescribes **comment conventions** (interface, data-structure member, implementation, cross-module), warns against **comments that repeat the code** or mirror entity names, and distinguishes **lower-level comments** (precision on declarations) from **higher-level comments** (intuition and intent). The chapter's centerpiece is **interface documentation**: separating interface from implementation comments, with extended **IndexLookup** and **Buffer::copy** examples showing how good abstractions are documented. **Implementation comments** should explain *what* and *why*, not *how*. **Cross-module design decisions** (Status enum checklist, zombie-server protocol, experimental `designNotes` file) close the chapter. §13.9 answers which IndexLookup details belong in interface docs.

**Sections ingested:** §13.1 Pick conventions · §13.2 Don't repeat the code · §13.3 Lower-level comments add precision · §13.4 Higher-level comments enhance intuition · §13.5 Interface documentation · §13.6 Implementation comments: what and why, not how · §13.7 Cross-module design decisions · §13.8 Conclusion · §13.9 Answers to questions from Section 13.5 · red flags: Comment Repeats Code · Implementation Documentation Contaminates Interface.

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Guiding principle and abstractions (intro)

- Programming-language statements cannot capture all important information from the developer's mind; comments record it for later maintainers. [verified from text, lines 4403–4407]
- **Guiding principle:** comments describe things that aren't obvious from the code—low-level ambiguities (range inclusivity), why code exists, implicit rules ("always invoke a before b"). [verified from text, lines 4407–4417]
- **Abstractions** (cross-ref Ch. 4) carry information not visible from code alone; users should understand a module's abstraction from **externally visible declarations plus comments**, without reading implementation. [verified from text, lines 4419–4432]
- Good comments operate at a **different level of detail** than code—more detailed in some places, more abstract in others. [verified from text, lines 4434–4438]

### Pick conventions (§13.1)

- First step: decide **what** to comment and **format**; follow Javadoc (Java), Doxygen (C++), or godoc (Go) when available—none perfect, but tooling benefits outweigh imperfections. [verified from text, lines 4440–4451]
- Conventions ensure **consistency** and help ensure comments actually get written. [verified from text, lines 4453–4457]
- **Four comment categories:** (1) **Interface** — precedes module declaration; behavior, args, return, side effects, exceptions, caller preconditions; (2) **Data structure member** — field declarations; (3) **Implementation** — inside methods; (4) **Cross-module** — dependencies crossing boundaries. [verified from text, lines 4459–4478]
- **Priority:** interface and data-structure-member comments most important; every class, class variable, and method should have interface comments; comment everything rather than debating necessity; implementation comments often unnecessary (§13.6); cross-module rare but critical (§13.7). [verified from text, lines 4480–4490]

### Don't repeat the code (§13.2)

- Most unhelpful comments **repeat the code**—information deducible from adjacent lines (research-paper Python example with one-line-per-line comments). [verified from text, lines 4492–4523]
- Scroll-bar and caret-init examples show comments adding no value when code is self-explanatory or comment too vague. [verified from text, lines 4525–4550]
- **Self-test:** could someone who never saw the code write the comment from the code alone? If yes, comment is worthless. [verified from text, lines 4552–4557]
- **Name-mirroring anti-pattern:** `getNormalizedResourceNames`, `downCastParameter`, `textHorizontalPadding` comments restate identifiers without units, semantics, or array structure. [verified from text, lines 4559–4609]
- **Red flag: Comment Repeats Code** — same words as the entity name; no value without understanding the method. [verified from text, lines 4590–4602]
- **Fix:** use **different words** that add meaning—e.g., padding comment specifies pixels and both sides of each line. [verified from text, lines 4611–4631]

### Lower-level comments add precision (§13.3)

- Lower-level comments clarify **exact meaning** of declarations; same-level comments tend to repeat code. [verified from text, lines 4633–4645]
- Precision questions for variables: **units**, inclusive/exclusive boundaries, **null semantics**, **resource ownership** (who frees/closes), **invariants**. [verified from text, lines 4647–4662]
- "Obvious from the code" means the **declaration**, not the whole application. [verified from text, lines 4664–4670]
- Vague `offset` and `lineWidths` examples revised to specify buffer position semantics and TreeMap key/value meaning (character lengths, missing entries). [verified from text, lines 4672–4713]
- Longer variable names (`numLinesWithLength`) can reduce comment burden; "width" → "length" disambiguates units. [verified from text, lines 4707–4713]
- **Document nouns, not verbs** — describe what variable *represents*, not how code toggles it (`receivedValidHeartbeat` revision). [verified from text, lines 4715–4747]

### Higher-level comments enhance intuition (§13.4)

- Higher-level comments provide **intuition**—overall intent and structure, omitting details; used inside methods and in interface comments. [verified from text, lines 4749–4755]
- Low-level RPC-selection comment partially repeats code without explaining purpose; better: **"Try to append the current key hash onto an existing RPC…"** — enables reader to infer loop, session, LOADING state, and batch limits. [verified from text, lines 4756–4812]
- Higher-level comments harder to write; ask: what is code trying to do? simplest explanation? most important thing? [verified from text, lines 4814–4818]
- Great designers **step back from details**—same skill as abstraction; higher-level comment expresses simple conceptual framework. [verified from text, lines 4820–4831]
- Good block comment: abstract *what* plus **"how we get here"** *why* (unprocessed key hashes example). [verified from text, lines 4833–4880]

### Interface documentation (§13.5)

- Comments are the **only way to describe abstractions**; code is too low-level and leaks implementation (cross-ref Ch. 4). [verified from text, lines 4882–4891]
- **Separate interface from implementation comments** so users aren't exposed to internals; if interface comments must describe implementation, module is **shallow** (cross-ref Ch. 15). [verified from text, lines 4893–4904]
- **Class interface comment** (`Http`): capabilities, what each instance represents, limitations (single-threaded)—no method specifics. [verified from text, lines 4906–4932]
- **Method interface comment** must include: higher-level caller-visible behavior; precise per-argument and return docs with constraints and dependencies; **side effects**; exceptions; **preconditions** (minimize but document remainder). [verified from text, lines 4934–4959]
- **`Buffer::copy`** Doxygen example: complete invocation contract including partial-copy and zero-overlap cases (cross-ref Ch. 10 define-errors-out-of-existence). [verified from text, lines 4961–5015]
- **IndexLookup** distributed range-query class: usage pattern `new IndexLookup` → repeated `getNext()` until NULL; implementation complexity hidden. [verified from text, lines 5017–5062]
- Five interface-vs-implementation quiz items (message format, comparison function, server index structure, concurrency, crash handling)—answers in §13.9. [verified from text, lines 5064–5083]
- **Bad IndexLookup comment:** leaks RPC names, private config constants, obvious `#include` advice—**Red flag: Implementation Documentation Contaminates Interface**. [verified from text, lines 5084–5203]
- **Good IndexLookup comment:** client range-query abstraction, method collaboration; omits NULL and crash details appropriately delegated to method docs or invisibility to users. [verified from text, lines 5163–5197]
- **`isReady` rewrite:** removes DCFT/rule-based implementation; documents blocking semantics and that method must be invoked for progress. [verified from text, lines 5205–5276]

### Implementation comments (§13.6)

- Most short methods need **no implementation comments** given code + interface docs. [verified from text, lines 5278–5284]
- Goal: help readers know **what** code does (not how); longer methods get high-level block comments before major phases. [verified from text, lines 5286–5298]
- Loop comments at abstract level for long/complex loops only. [verified from text, lines 5299–5313]
- Also document **why** for non-obvious code (bug fixes); may reference bug tracker ID to avoid duplication (cross-ref Ch. 16). [verified from text, lines 5315–5325]
- Local variables: comment only if span is large; good short-span names need no comment. [verified from text, lines 5327–5336]

### Cross-module design decisions (§13.7)

- Not all design decisions fit one class; protocol senders/receivers, shared invariants need documentation. [verified from text, lines 5338–5346]
- **RAMCloud `Status` enum:** inline checklist of seven files/places to update when adding a status—placed at end where editors look. [verified from text, lines 5348–5419]
- **Zombie servers:** no obvious central doc location; duplication vs single misplaced doc both fail. [verified from text, lines 5421–5433]
- **Experimental `designNotes` file:** labeled sections (e.g., "Zombies"); code references `// See "Zombies" in designNotes.` — single copy, discoverability vs proximity tradeoff `[contested in chapter]` (author experimenting). [verified from text, lines 5435–5474]

### Conclusion (§13.8)

- Goal: structure and behavior **obvious** so readers find info and modify confidently. [verified from text, lines 5476–5484]
- **"Obvious"** = first-time reader, not author; if reviewer says unclear, **don't argue**—improve comments or code. [verified from text, lines 5486–5495]

### Answers (§13.9)

| Question | Belongs in interface? |
|----------|----------------------|
| Message formats to servers | **No** — implementation detail |
| Comparison function for range | **Yes** — users need to know |
| Server-side index data structure | **No** — encapsulated on servers |
| Concurrent multi-server requests | **Possibly** — high-level perf info if special techniques |
| Server crash mechanism | **No** for RAMCloud (auto-recovery invisible); **yes** for manifestation if visible to apps |

[verified from text, lines 5497–5527]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 4399–5528 (inclusive) |
| **Chapter boundary** | Starts `Chapter 13` (L4399); ends before `Chapter 14` (L5529) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; adjacent Ch. 14 not read |
| **Figures** | No figures in chapter; code tables rendered as ASCII in export |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. State the guiding principle for comments and explain why abstractions require comment supplementation.
2. Classify comments into interface, data-structure-member, implementation, and cross-module categories.
3. Detect and eliminate comments that repeat code or mirror entity names.
4. Write lower-level comments addressing units, boundaries, null semantics, ownership, and invariants.
5. Write higher-level comments that convey intent, structure, and "how we get here" rationale.
6. Separate interface from implementation documentation and apply the IndexLookup interface quiz.
7. Place cross-module documentation where developers will discover it (enum anchor, designNotes pattern).

### worked_examples_present

**Y** — Extensive before/after comment rewrites and production-style API examples:

| Example | Section | Role |
|---------|---------|------|
| Research-paper line-by-line comments | §13.2 | Anti-pattern: repeat code |
| Scroll bars / caret init | §13.2 | Trivial or vague comments |
| `getNormalizedResourceNames` / padding | §13.2 | Name-mirroring vs informative |
| `offset` / `lineWidths` TreeMap | §13.3 | Precision on declarations |
| `receivedValidHeartbeat` | §13.3 | Nouns not verbs |
| RPC append selection loop | §13.4 | Low vs high level |
| Unprocessed PKHashes block | §13.4 | What + why ("how we get here") |
| `Http` class interface | §13.5 | Class-level abstraction doc |
| `Buffer::copy` Doxygen | §13.5 | Complete method contract |
| IndexLookup bad vs good class doc | §13.5 | Interface vs implementation |
| `isReady` bad vs good | §13.5 | Implementation contamination |
| Phase / loop implementation comments | §13.6 | Navigation comments |
| RAMCloud `Status` enum checklist | §13.7 | Cross-module at discovery point |
| `designNotes` / Zombies | §13.7 | Central cross-module file |

### exercise_hooks

- No end-of-chapter problem sets in source text (§13.5 embeds a self-quiz answered in §13.9).
- **Instructor / self-study hooks `[inferred]`:**
  - Audit an open-source module: classify comments; flag repeat-code and implementation-in-interface violations.
  - Rewrite a shallow getter's interface comment using Ousterhout's precision checklist.
  - Given an agent-tool or RAG-client API, draft interface comments that hide orchestration (IndexLookup pattern).
  - Design a cross-module checklist for a shared error-code enum in your codebase.
  - Peer review: apply the "first-time reader" obviousness test from §13.8.

## Operator hooks

### 1. Foundation layer

Chapter 13 operationalizes **abstraction documentation** introduced in Chapter 4 (modules, deep vs shallow) and foreshadows Chapter 15's claim that **writing comments exposes design quality** (shallow modules force implementation into interface docs). It pairs with Chapter 10's "define errors out of existence" via `Buffer::copy` and Chapter 16's comment-duplication discipline. For **w1_foundation**, this chapter is the canon reference for **what belongs in interface docs vs code**—prerequisite for reading API-heavy titles (**ai_engineering_2025**, **hands_on_llms_2024** tool schemas) and for **LangSmith/Langfuse doc snapshots** (w3) where informal contracts dominate formal types. It does not replace dedicated style guides (Google Java Style, etc.) but supplies the **design rationale** behind them.

### 2. MDCalc alignment

**[peripheral]** — No direct coverage of agents, trace/eval observability, clinical AI safety, or regulated deployment. Pattern-portable lessons:

- **Agent/tool interfaces** should document side effects, preconditions, and performance-relevant concurrency at abstraction level—analogous to IndexLookup hiding RPC choreography.
- **Informal contracts** (ordering, crash visibility, comparison semantics for clinical calculators) mirror Ousterhout's argument that formal types are insufficient.
- **Cross-module invariants** (e.g., status-code propagation across services) parallel RAMCloud `Status` checklist—relevant to regulated multi-service health stacks only as a documentation pattern, not as clinical authority.

No employer-stack or production claims made.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4** | High | Abstractions; Ch. 13 extends "comments complete declarations" |
| **philosophy_software_design_2e_2021 Ch. 15** | Forward link | Shallow design revealed by comment difficulty [not ingested in this slice] |
| **Clean Code / Code Complete** | Medium | Comment hygiene overlaps; Ousterhout is more abstraction- and interface-centric |
| **ai_engineering_2025 / prompt_engineering_llms_2024** | Low–medium | Prompt/schema docs as informal interfaces; different medium, shared "hide complexity" goal |
| **langsmith_docs_snapshot / langfuse_docs_snapshot** | Low | Observability API docs; procedural reference, not design philosophy |
| **ddia_2e_2026** | Low | Distributed IndexLookup example is RAMCloud-specific; DDIA covers distributed design not comment craft |

**Dedup guidance:** Treat Ousterhout Ch. 13 as **canonical interface-comment vs implementation-comment** reference; other ingests should link here rather than re-deriving IndexLookup rewrite walkthrough.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — many before/after comment pairs with real systems code |
| Exercise hooks | **Moderate** — §13.5 quiz + §13.9 answers; no printed exercises |
| Chapter boundary quality | **Clean** — self-contained §13.1–13.9; §13.9 belongs to §13.5 |
| Ingest suitability | **High** — dense procedural guidance with anchorable red flags and extended case study |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; within classic/design-principles window for 2026 session |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press textbook; RAMCloud/HTTP examples from author systems work |
| **Primary-source citation density** | **PASS (low density flagged)** | Chapter cites Javadoc/Doxygen/godoc and internal cross-refs; one research-paper anti-example; no bibliography—appropriate for craft chapter |
| **Contested claims flagged** | **PASS** | `designNotes` approach labeled experimental; "comment everything" vs rare exceptions stated; reviewer-obviousness norm preserved |
| **Worked examples (procedural/conceptual)** | **PASS** | Multiple rewrite exercises with production C++/Java samples |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C13-001 | Comments should describe things that aren't obvious from the code | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | intro |
| PSD2E-C13-002 | Developers should understand abstractions without reading implementation code | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | intro |
| PSD2E-C13-003 | Four comment categories: interface, data structure member, implementation, cross-module | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.1 |
| PSD2E-C13-004 | Red flag: comment repeats code or entity name words | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.2 |
| PSD2E-C13-005 | Variable comments: units, boundaries, null, ownership, invariants | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.3 |
| PSD2E-C13-006 | Higher-level comments express intent; lower-level add precision | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.3–§13.4 |
| PSD2E-C13-007 | Interface comments must be separable from implementation; else module is shallow | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.5 |
| PSD2E-C13-008 | Red flag: implementation documentation contaminates interface | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.5 |
| PSD2E-C13-009 | Implementation comments: what and why, not how | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.6 |
| PSD2E-C13-010 | Cross-module docs at natural discovery points (Status enum) or central designNotes | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.7 |
| PSD2E-C13-011 | "Obvious" means obvious to first-time reader, not author | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch13_ingest.md | §13.8 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
