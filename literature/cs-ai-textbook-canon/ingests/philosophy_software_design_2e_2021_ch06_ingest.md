# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 6

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
| **chapter_number** | 6 |
| **chapter_title** | General-Purpose Modules are Deeper |
| **page_range** | Printed page numbers absent from text export; logical span §6.1–§6.9 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |
| **corpus_slug** | philosophy_software_design_2e_2021 |
| **wave / track** | w1_foundation · track A |

## Scope

Chapter 6 argues that **unnecessary specialization**—in class APIs, method design, and control-flow special cases—is a primary driver of software complexity, and that **somewhat general-purpose** modules yield **deeper**, simpler interfaces with better **information hiding**. Ousterhout grounds the claim in teaching experience (student GUI text-editor projects) and extends it with an operating-system device-driver pattern (specialization pushed downward) and a refactored **undo/redo** architecture (`History` + `Action` interface). The chapter operationalizes generality through three self-check questions, distinguishes **false abstractions** (e.g., `backspace` hiding behavior the UI must know anyway), and closes with **eliminating special cases in method bodies** (empty selection represented as zero-width range). Specialization cannot be eliminated entirely; the design task is to **separate** specialized code from general-purpose mechanisms and place each at the correct layer.

**Sections ingested (text lines 1956–2437):**

| Section | Lines | Focus |
|---------|-------|-------|
| Chapter intro | 1956–1981 | Generality vs specialization; link to deep APIs and Ch. 20 |
| §6.1 Somewhat general-purpose classes | 1983–2027 | Sweet spot: current functionality, general interface |
| §6.2 Example: editor text storage (specialized) | 2029–2084 | Student `backspace`/`delete`/`deleteSelection` APIs |
| §6.3 General-purpose text API | 2086–2149 | `insert`/`delete`/`changePosition`/`findNext` |
| §6.4 Information hiding | 2151–2174 | False abstraction; who needs to know what |
| §6.5 Design questions | 2176–2211 | Three heuristics; single-char API counterexample |
| §6.6 Push specialization up/down | 2213–2250 | UI upward; device drivers downward |
| §6.7 Undo mechanism | 2252–2386 | `History` class extraction; fences; layering note |
| §6.8 Eliminate special cases | 2388–2426 | Empty selection; Ch. 10 forward ref |
| §6.9 Conclusion | 2428–2436 | Synthesis |

**Out of scope for this ingest:** Chapters 1–5 (complexity, strategy, modules, information hiding); Ch. 10 (exceptions), Ch. 20 (efficiency)—referenced only.

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[author experience]`.

### KF-1 — Over-specialization as complexity root cause

Teaching software design shifted Ousterhout's view toward generality:

> "I now think that over-specialization may be the single greatest cause of complexity in software." (lines 1964–1966)

Converse claim: general-purpose code is "simpler, cleaner, and easier to understand" (lines 1966–1967). Principle applies at class/method level (deep APIs via general-purpose interfaces → more information hiding) and in method bodies (eliminate special cases so common path handles edge cases; efficiency tie-in deferred to Ch. 20, lines 1975–1976).

### KF-2 — "Somewhat general-purpose" sweet spot (§6.1)

Tension between **investment mindset** (Ch. 3: build reusable mechanisms) and **incremental delivery** (specialize now, refactor later). Author initially favored special-purpose; student-project review reversed the preference: general-purpose classes were "almost always better," with **simpler, deeper interfaces** and **less implementation code**—even when used only once (lines 2007–2018).

**Operational definition:**

> "the module's functionality should reflect your current needs, but its interface should not." (lines 2021–2023)

Interface must support multiple uses without being tied to today's needs; avoid over-generalization that harms current usability (lines 2025–2027).

### KF-3 — Specialized text API anti-pattern (§6.2)

Student GUI editor projects mirrored UI operations in the text layer: `backspace(Cursor)`, `delete(Cursor)`, `deleteSelection(Selection)`—types `Cursor` and `Selection` leak UI concepts (lines 2053–2063). Costs:

- Large number of **shallow methods**, many invoked once (lines 2070–2074).
- **Information leakage** between UI and text modules; new UI ops require text-class changes (lines 2076–2084).
- Violates independent class development goal (lines 2082–2084).

### KF-4 — General-purpose text API (§6.3)

Replacement surface: `insert(Position, String)`, `delete(Position start, Position end)`, `changePosition(Position, int numChars)` (lines 2093–2105). UI key handlers compose generically:

```text
text.delete(cursor, text.changePosition(cursor, 1));           // delete key
text.delete(text.changePosition(cursor, -1), cursor);         // backspace
```

(lines 2115–2119)

Tradeoff: UI call sites slightly longer but **behavior obvious** without reading text-class docs (lines 2121–2128). **Less total code** than many special-purpose methods (lines 2129–2132). Reuse for batch find-replace needs only `findNext(Position, String)` added (lines 2134–2146).

### KF-5 — False abstraction and information hiding (§6.4)

`backspace` in the specialized text class is a **false abstraction**: it purports to hide which characters are deleted, but UI developers must know anyway and will read implementation (lines 2163–2168). Design rule:

> "One of the most important elements of software design is determining who needs to know what, and when." (lines 2169–2170)

When details matter, make them explicit in the layer that needs them rather than obscuring behind a mismatched interface (lines 2171–2174).

### KF-6 — Three interface balance questions (§6.5)

1. **Simplest interface covering all current needs?** Fewer methods with same capability → more general-purpose; caveat if arguments balloon (lines 2183–2192).
2. **How many situations will this method be used?** Single-use methods (e.g., `backspace`) are red flags (lines 2194–2197).
3. **Easy to use for current needs?** Over-generalization red flag: single-character `insert`/`delete` is simple and general but forces loops and inefficiency for range edits (lines 2199–2211).

### KF-7 — Push specialization up or down (§6.6)

Applications must have specialized top-level features, but specialization need not **percolate down** (lines 2215–2232). **Upward push:** editor UI owns backspace/delete composition; text class stays generic.

**Downward push:** OS **device drivers** implement general block read/write interface using device-specific commands; core OS stays device-agnostic; new devices plug in without OS changes (lines 2234–2250).

### KF-8 — Undo: extract general-purpose `History` (§6.7)

Student mistake: entire undo in text class, including selection/cursor/view changes with callbacks—awkward coupling, information leakage, text class changes for new undoable entities (lines 2263–2289).

Refactor separates three concerns (lines 2348–2365):

| Layer | Responsibility | Location |
|-------|----------------|----------|
| General undo engine | List management, undo/redo traversal, grouping | `History` class |
| Action specifics | Per-operation `undo()`/`redo()` | `History.Action` implementors (`UndoableInsert`, `UndoableSelection`, …) |
| Grouping policy | When one user undo spans multiple actions | High-level UI via `History.addFence()` |

`History` knows nothing about action payloads (lines 2316–2326). **Fences** delimit action groups; `undo()` walks back to next fence (lines 2339–2346).

**Important nuance:** separation applies **per mechanism**. Text class may hold **special-purpose undo code for text** alongside **general-purpose text operations**—combine special-purpose undo-for-text with text management, not with general `History` infrastructure (lines 2373–2386).

### KF-9 — Eliminate special cases in code bodies (§6.8)

Selection "no selection" state variable caused pervasive `if` checks. **Fix:** always maintain a selection; empty UI selection = zero-width range (same start/end positions) (lines 2408–2412). Copy/delete on empty selection becomes no-op via normal logic—e.g., delete concatenation regenerates original line when range empty (lines 2413–2422). Forward reference: Ch. 10 on exception special cases (lines 2424–2426).

### KF-10 — Conclusion (§6.9)

Unnecessary specialization in classes, methods, or control flow significantly contributes to complexity. Good design **reduces and separates** specialized from general-purpose code → deeper classes, better information hiding, simpler obvious code (lines 2430–2436).

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 1956–2437 (inclusive) |
| **Chapter boundary** | Starts `Chapter 6` (L1956); ends §6.9 conclusion (L2436); L2437 blank before later chapters |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections complete** | §6.1–§6.9 + chapter intro — all present in slice |
| **Figures** | None in slice |
| **Code blocks** | Java-style API signatures and `History` class sketch present as plain text |
| **Deferred** | Page numbers; Ch. 10 exception handling; Ch. 20 efficiency argument for special-case elimination |
| **Amnesiac rule** | No claims drawn from training prior; ISBN from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. **Contrast** special-purpose vs somewhat general-purpose module design and articulate the "functionality narrow, interface broad" rule.
2. **Refactor** a UI-mirroring API into a small set of composable primitive operations (text editor pattern).
3. **Diagnose** false abstractions where purported hiding forces callers to inspect implementation anyway.
4. **Apply** the three balance questions when designing or reviewing interfaces.
5. **Place** specialized code correctly by pushing specialization **up** (application/UI) or **down** (drivers/adapters).
6. **Extract** a general-purpose mechanism (command/history pattern) from entangled special-purpose handlers.
7. **Eliminate** boolean/state special cases by normalizing edge conditions into the common data model (empty selection).

### worked_examples_present

**Y** — Multiple worked examples with code or architectural detail:

| Example | Section | Role |
|---------|---------|------|
| Student specialized text API | §6.2 | Anti-pattern: UI-shaped methods |
| General-purpose `insert`/`delete`/`changePosition` | §6.3 | Composable primitives; backspace/delete composition |
| Find-replace extension | §6.3 | Reuse without `backspace`/`delete` methods |
| `backspace` as false abstraction | §6.4 | Information-hiding failure mode |
| Single-character API counterexample | §6.5 | Over-generalization that harms usability |
| Editor UI vs text layering | §6.6 | Push specialization upward |
| OS device drivers | §6.6 | Push specialization downward |
| Monolithic undo in text class | §6.7 | Coupling anti-pattern |
| `History` + `Action` + fences | §6.7 | Command pattern; three-layer separation |
| Text undo in text class (nuance) | §6.7 | Per-mechanism separation rule |
| Empty selection as zero-width range | §6.8 | Special-case elimination in bodies |

### exercise_hooks

| Hook | Type | Prompt sketch |
|------|------|---------------|
| **E-6.1 API audit** | refactor lab | Given a CRUD or agent-tool API mirroring UI screens, list methods used in only one call site; redesign with ≤3 composable primitives. |
| **E-6.2 False abstraction hunt** | code review | Find methods whose names encode caller context (e.g., `onSubmit`, `handleBackspace` in domain layer); who actually needs the hidden detail? |
| **E-6.3 Three questions** | design review | For a new module, answer §6.5 questions in writing before implementation; flag single-use methods. |
| **E-6.4 Layer placement** | architecture | Map specialization in a RAG pipeline: what belongs in orchestration (up) vs provider adapters (down)? |
| **E-6.5 History extraction** | implementation | Refactor coupled undo/state into `History` + `Action`; define fence policy for multi-step user operations. |
| **E-6.6 Empty state** | bug-prevention | Identify nullable/optional state variables that force `if (!x)` branches; normalize to sentinel values or zero-width ranges. |
| **E-6.7 Cross-canon** | synthesis | Compare Ousterhout generality heuristic with DDIA 2e bounded-context boundaries: where does "general interface" become wrong abstraction across domains? |

No end-of-chapter problem sets in source text.

## Operator hooks

### 1. Foundation layer

Chapter 6 is the **operational complement** to Chapter 4's deep-module heuristic and Chapter 5's information-hiding discipline: it shows *how* to deepen modules in practice—prefer general primitives, push UI/product specialization upward, push hardware/provider specialization downward. For **w1_foundation**, this chapter is essential before later Ousterhout material on naming, comments, and performance (Ch. 20 special-case efficiency link).

Bridges:

- **Ch. 3 (strategic investment)** — somewhat general-purpose design is the module-level expression of upfront interface investment (line 1992 cross-ref).
- **Ch. 4–5** — generality increases depth and reduces leakage; false `backspace` abstraction is a concrete leakage/false-abstraction case.
- **AI Engineering 2025 / agent stacks** — tool interfaces that mirror one UI flow or one prompt template reproduce §6.2 shallow-API pathology; `History`/`Action` pattern maps to auditable agent action logs and reversible tool batches.
- **DDIA 2e** — device-driver downward specialization parallels storage-engine adapters behind uniform APIs; upward specialization parallels application-specific orchestration over generic data primitives.

**Prerequisite established:** deep modules + information hiding + generality/specialization placement.

### 2. MDCalc alignment

**[peripheral]**

Chapter is general software-design pedagogy, not clinical AI, agents, trace/eval observability, or regulated deployment. Portable patterns:

- **Agent/tool registries** should expose composable primitives (read/write/search) not screen-shaped method names—reduces coupling when UI or workflow changes.
- **Undo/audit trails** for clinician-facing edits map directly to `History` + `Action` + fences; grouping policy belongs in application layer, not buried in storage class.
- **False abstraction** risk when "helpful" wrapper APIs hide behavior reviewers must verify (safety-relevant in any high-stakes UI, but chapter does not discuss clinical validation).

No MDCalc production-stack or HIPAA/FDA claims. Do not treat student-project anecdotes as health-tech evidence.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4–5** | High (intentional) | Ch. 6 applies depth + hiding via generality; ingest separately, cross-link |
| **Gang of Four Command pattern** | Medium | `History`/`Action` is textbook Command; Ousterhout frames via specialization separation |
| **Clean Code / UI-driven APIs** | Tension | Mirrors-class-to-UI is common in rapid prototyping; Ousterhout argues against |
| **understanding_distributed_systems_2022** | Low | Driver adapter pattern echoes OS example |
| **ai_engineering_2025** | Low–medium | Tool design and agent action logging; no duplicate walkthrough needed |

**Dedup guidance:** Treat §6.3 text API and §6.7 `History` as **canonical scholia examples** for general-purpose interfaces and undo extraction; other ingests should cite this ingest rather than re-derive.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| **Worked examples** | **Strong** — two multi-section code/architecture narratives plus OS pattern |
| **Exercise hooks** | **Strong** — refactor and extraction labs natural from material |
| **Chapter boundary quality** | **Excellent** — self-contained; clean handoffs to Ch. 10/20 via forward refs only |
| **Anchor density** | High for pedagogical claims; **low for external citations** |
| **Ingest suitability** | **High** — procedural design chapter with falsifiable before/after comparisons |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; ≤5 years from operator date (2026); active design-principles canon |
| **Author authority** | **PASS** | John Ousterhout — Stanford CS; Yaknyam Press textbook; teaching-grounded examples |
| **Primary-source citation density** | **PASS (low density flagged)** | No formal citations, footnotes, or bibliography in lines 1956–2437. Evidence: author teaching experience, recurring student-project patterns, standard OS device-driver narrative. Appropriate for manifesto-style textbook chapter but **not citation-heavy** |
| **Contested claims flagged** | **PASS** | Strong universals flagged below—not smoothed |
| **Worked examples (procedural)** | **PASS** | Extended text API and undo refactor with code; special-case elimination walkthrough |

**Overall TEXTBOOK-Q1:** **PASS** (with low citation-density flag; qualify universals in downstream synthesis)

### Contested / strong claims (not smoothed)

| claim | issue | anchor |
|-------|-------|--------|
| Over-specialization may be **single greatest** complexity cause | Superlative; no comparative study | lines 1964–1966 |
| General-purpose **always** better than special-purpose in student projects | `[author experience]`; selection bias in classroom | lines 2009–2018 |
| General-purpose better **even without reuse** | Assertive; counterexamples (YAGNI extremists) not explored | lines 2017–2018 |
| Device-driver pattern description | Standard CS pedagogy; no primary OS paper cited | lines 2234–2250 |

### Claims ledger (load-bearing)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C06-001 | Over-specialization may be the single greatest cause of software complexity | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | intro |
| PSD2E-C06-002 | Sweet spot: functionality for current needs, interface general enough for multiple uses | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.1 |
| PSD2E-C06-003 | Specialized text API leaks UI concepts and creates shallow single-use methods | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.2 |
| PSD2E-C06-004 | General-purpose insert/delete/changePosition composes UI operations with less total code | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.3 |
| PSD2E-C06-005 | backspace method is false abstraction when UI must know deleted characters | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.4 |
| PSD2E-C06-006 | Push specialization up (UI) or down (device drivers) to isolate general-purpose core | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.6 |
| PSD2E-C06-007 | History class separates general undo engine from Action specializations and UI fence policy | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.7 |
| PSD2E-C06-008 | Represent no selection as empty zero-width range to eliminate special-case branches | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md | §6.8 |

## Cross-links (within book)

- **Depends on:** Ch. 3 — investment mindset for somewhat general-purpose upfront cost (line 1992); Ch. 4 — deep modules; Ch. 5 — information hiding and leakage.
- **Forward references:** Ch. 10 — exceptions as special cases (lines 2424–2426); Ch. 20 — eliminating special cases can improve efficiency (lines 1975–1976).

## Provenance

| Field | Value |
|-------|-------|
| **ingest_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch06_ingest.md` |
| **ingest_agent** | sub-agent chapter ingest |
| **source_text** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **DOI/URL/ISBN** | ISBN 978-1-7321022-1-7 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
