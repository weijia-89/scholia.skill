# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 7

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
| **chapter_number** | 7 |
| **chapter_title** | Different Layer, Different Abstraction |
| **page_range** | Printed page numbers absent from text export; logical span §7.1–§7.6 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 7 applies the **deep-module / complexity-management** framework (Ch. 4–6) to **layered systems**. Ousterhout states that well-designed systems change abstraction at each layer boundary: following one operation up or down through method calls, the abstraction should shift. **Adjacent layers with similar abstractions** are a design red flag. The chapter catalogs three failure modes—**pass-through methods**, **decorator-induced API duplication**, and **pass-through variables**—and contrasts each with legitimate cases where similar signatures are acceptable (dispatchers, polymorphic interfaces). §7.4 extends the rule inward: a class's **public interface** should differ from its **internal representation** (character-oriented text API over line-oriented storage, cross-ref Ch. 6). §7.5 develops the **context object** as the author's preferred remedy for long argument chains, while flagging its grab-bag and global-state risks. §7.6 closes by restating the net-complexity test: every interface, argument, or class must eliminate more complexity than it introduces.

**Sections ingested:** §7.1 Pass-through methods · §7.2 When is interface duplication OK? · §7.3 Decorators · §7.4 Interface versus implementation · §7.5 Pass-through variables · §7.6 Conclusion · Red Flag: Pass-Through Method · Figures 7.1–7.2 (text descriptions only; image placeholders `[]` in export).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Layered abstractions (chapter intro)

- Software systems compose in layers; higher layers use lower-layer facilities. In a well-designed system, **each layer provides a different abstraction** from layers above and below; abstractions should change with each method call along an operation's path. [verified from text, lines 2442–2447]
- **File-system layering:** top = variable-length byte file with read/write ranges; middle = fixed-size disk-block cache (frequently used blocks stay in memory); bottom = device drivers moving blocks between storage and memory. [verified from text, lines 2449–2456]
- **TCP layering:** top = reliable byte stream machine-to-machine; lower = bounded packets on best-effort delivery (loss/reordering possible). [verified from text, lines 2458–2463]
- **Red flag:** adjacent layers with **similar abstractions** suggest class-decomposition problems; chapter covers manifestations, resulting problems, and refactorings. [verified from text, lines 2465–2468]

### Pass-through methods (§7.1)

- **Pass-through method:** does little except invoke another method with a **similar or identical signature**. [verified from text, lines 2472–2475]
- **Student GUI text-editor example:** `TextDocument` delegates to `TextArea` for `getLastTypedCharacter`, `getCursorOffset`, `insertString`; only `willInsertString` adds trivial listener dispatch. **13 of 15 public methods** were pass-through. [verified from text, lines 2476–2531]
- **Red Flag: Pass-Through Method** — indicates unclear division of responsibility between classes. [verified from text, lines 2524–2529]
- Pass-through methods make classes **shallower**: increase interface complexity without increasing total system functionality; create **signature-coupling dependencies** (e.g., `TextArea.insertString` change forces `TextDocument.insertString` change). [verified from text, lines 2533–2540]
- **Design rule violated:** "The interface to a piece of functionality should be in the same class that implements the functionality." [verified from text, lines 2545–2547]
- **Diagnostic question:** "Exactly which features and abstractions is each of these classes responsible for?" — overlap in responsibility is typical. [verified from text, lines 2548–2551]
- **Refactor options (Figure 7.1):** (b) expose lower class directly to higher-level callers; (c) redistribute functionality; (d) merge entangled classes. Student collapsed `TextDocument`, `TextArea`, `TextDocumentListener` from three classes to two with clearer roles. [verified from text, lines 2553–2567]

### When interface duplication is OK (§7.2)

- Same signature is **not always bad**; each new method must contribute **significant functionality**. Pass-through methods fail because they add none. [verified from text, lines 2571–2574]
- **Dispatcher:** uses arguments to select among several methods, then passes most/all arguments through. Same signature as callees, but provides **routing/selection** functionality. [verified from text, lines 2576–2582]
- **HTTP Web server example:** dispatcher inspects URL, selects handler (static file, PHP, JavaScript, etc.) via rule matching — dispatch can be intricate. [verified from text, lines 2594–2601]
- **Multiple implementations of one interface** (e.g., disk drivers): same interface, different hardware; reduces cognitive load once one implementation is learned. These methods are **same layer**, do not invoke each other. [verified from text, lines 2603–2613]

### Decorators (§7.3)

- **Decorator (wrapper) pattern** encourages API duplication across layers: extends an object while exposing similar/identical API, methods delegate to underlying object. [verified from text, lines 2617–2621]
- **Examples:** `BufferedInputStream` over `InputStream` (Ch. 4); `ScrollableWindow` decorating non-scrollable `Window`. [verified from text, lines 2622–2630]
- **Motivation:** separate special-purpose extensions from generic core. **Cost:** decorators tend to be **shallow** — much boilerplate for little new functionality; often many pass-through methods. Easy to overuse → **explosion of shallow classes** (Java I/O cited again). [verified from text, lines 2632–2638]
- **Alternatives before creating a decorator:** add functionality directly to underlying class (especially if general-purpose or nearly always used — `BufferedInputStream` should have been combined with `InputStream` per author); merge with particular use case; merge with existing decorator for one deeper class; implement as **stand-alone class** independent of base (scrollbars separable from window). [verified from text, lines 2640–2665]
- **Legitimate wrapper case (rare):** external class whose interface cannot be modified but must conform to a different application interface — wrapper translates. "There is usually a better alternative." [verified from text, lines 2667–2673]

### Interface versus implementation (§7.4)

- **Same rule applies inside a class:** interface abstractions should normally differ from internal representations. Similar abstractions → class probably not deep. [verified from text, lines 2677–2681]
- **Text-editor callback (Ch. 6):** teams stored text as separate lines but exposed **line-oriented APIs** (`getLine`, `putLine`). Higher UI code inserts/deletes mid-line or across lines — callers forced to split/join lines; logic duplicated across UI. [verified from text, lines 2682–2693]
- **Better design:** **character-oriented interface** — `insert` arbitrary string (including newlines) at arbitrary position; `delete` between two positions. Internal line storage unchanged. Encapsulates split/join complexity inside text class → **deeper module**, simpler higher-level code. API differs from storage mechanism; difference = valuable functionality. [verified from text, lines 2695–2705]

### Pass-through variables (§7.5)

- **Pass-through variable:** passed down a long method chain though intermediate methods do not use it. [verified from text, lines 2709–2711]
- **Datacenter service example (Figure 7.2):** CLI `cert` argument needed only by low-level `m3` (socket open); threaded through `main` → … → `m3`, appearing in every intermediate signature. [verified from text, lines 2711–2716]
- **Cost:** all intermediates must know the variable exists; adding new pass-through state (e.g., late-added certificate support) forces **large interface churn** across paths. [verified from text, lines 2718–2724]
- **Remediation options:** (b) store in **object already shared** between top and bottom (but that object may itself be a pass-through); (c) **global variable** — avoids threading but prevents multiple independent instances in one process (problematic for testing); (d) **context object** — author's most-used approach. [verified from text, lines 2726–2745]
- **Context object:** holds all application global state (config, shared subsystems, performance counters); **one context per system instance**; enables multiple instances in one process. Reference stored in major objects; passed explicitly mainly at **constructors**, reducing method-signature pollution. [verified from text, lines 2744–2773]
- **Context benefits:** unified global-state management; new variables added to context without touching unrelated code (except context ctor/dtor); convenient test configuration via context fields. [verified from text, lines 2775–2784]
- **Context limitations** `[contested in chapter]`: variables retain **most disadvantages of globals** (obscure usage, grab-bag risk, nonobvious dependencies); thread-safety concerns — **immutable context fields** preferred. Author: "I haven't found a better solution than contexts." [verified from text, lines 2786–2793]

### Conclusion (§7.6)

- Every design element (interface, argument, function, class, definition) adds complexity developers must learn; it must **eliminate more complexity than it adds** or should be omitted. [verified from text, lines 2797–2805]
- **"Different layer, different abstraction"** instantiates this: same-abstraction layers (pass-through methods, decorators) likely fail the net-benefit test; pass-through arguments add awareness cost without functionality. [verified from text, lines 2807–2813]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 2438–2814 (inclusive) |
| **Chapter boundary** | Starts `Chapter 7` (L2438); ends before `Chapter 8` (L2815) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; Ch. 8 not read |
| **Figures** | Fig. 7.1 (pass-through refactor options), Fig. 7.2 (pass-through variable remedies) — textual captions only; `[]` image placeholders in export |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from same file front matter (L5–29) |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. State the **different layer, different abstraction** rule and recognize adjacent layers with similar abstractions as a decomposition red flag.
2. Define **pass-through methods** and **pass-through variables**; quantify their complexity cost (interface bloat, coupling, signature churn).
3. Apply refactor strategies for pass-through methods: direct exposure, redistribution, merge (Figure 7.1).
4. Distinguish illegitimate API duplication from **dispatchers** and **same-layer polymorphic interfaces**.
5. Critique **decorator/wrapper** usage using depth/shallowness criteria; enumerate alternatives before adding wrapper classes.
6. Explain why a class's **public API** should differ from its internal representation, using the line-storage / character-API text example.
7. Compare pass-through-variable remedies (shared object, globals, context) and articulate context-object trade-offs for testing and multi-instance deployment.

### worked_examples_present

**Y** — Multiple concrete scenarios with code or architecture detail:

| Example | Section | Role |
|---------|---------|------|
| File-system three-layer stack | Intro | Layer abstraction shifts (file → block cache → drivers) |
| TCP reliable stream over packets | Intro | Network layering |
| `TextDocument` / `TextArea` pass-through | §7.1 | 13/15 pass-through methods; listener-only logic |
| Figure 7.1 refactor paths (a–d) | §7.1 | Eliminate pass-through between C1/C2 |
| HTTP URL dispatcher | §7.2 | Legitimate same-signature routing |
| Disk driver common interface | §7.2 | Same-layer polymorphism |
| `BufferedInputStream`, `ScrollableWindow` | §7.3 | Shallow decorator critique |
| Text line API vs character API | §7.4 | Interface ≠ implementation (Ch. 6 callback) |
| Datacenter `cert` pass-through chain | §7.5 | Figure 7.2 (a–d) remediation comparison |
| Context object pattern | §7.5 | Constructor-threaded global state |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Audit a service codebase: count pass-through methods (one-line delegates); map to Figure 7.1 refactor option.
  - Trace a configuration flag (API key, TLS cert, trace ID) from entrypoint to socket/client; classify as pass-through variable; sketch context-object migration.
  - Given an agent/tool framework with wrapper classes per provider, apply §7.3 checklist: merge, standalone, or deep single decorator?
  - Revisit Ch. 6 text-module design: document line-internal vs character-external API as depth case study.
  - Red-team: defend decorator pattern (Gang of Four orthodoxy) against Ousterhout's shallow-class critique; identify when dispatchers vs pass-through methods differ only by intent.
  - Testing hook: demonstrate why globals block two parallel test instances; implement dual contexts in one process.

## Operator hooks

### 1. Foundation layer

Chapter 7 is the **layering and API-surface hygiene** companion to Ch. 4 (depth) and Ch. 6 (information hiding in the text editor). It operationalizes "each abstraction boundary must earn its keep" for **multi-class and multi-layer systems**—directly relevant when designing agent pipelines, middleware stacks, and SDK wrappers in the **w1_foundation** track. Pass-through methods map to **thin facade services** that add no policy; pass-through variables map to **observability context, auth tokens, and config** threaded through call stacks. The **context object** pattern anticipates **request-scoped dependency injection** and test doubles without endorsing a specific framework. Cross-canon: reinforces **understanding_distributed_systems_2022** layering discussions and **ddia_2e_2026** boundary design; contrasts with **ai_engineering_2025** tool/agent wrapper proliferation—apply §7.3 before adding per-vendor adapter classes.

### 2. MDCalc alignment

**[peripheral — pattern portable]** — No clinical AI, trace/eval product, or regulated-deployment content. Portable patterns for operator stacks:

- **Trace/eval context:** treat trace IDs, eval run config, and preview flags as context fields rather than pass-through parameters through every handler (§7.5).
- **Agent/tool interfaces:** prefer **dispatchers** (route by intent/URL analog) over pass-through wrappers; merge shallow provider decorators where behavior is universal (§7.2–7.3).
- **Informal contracts:** character-vs-line API lesson applies to **document/chunk abstractions** in RAG pipelines—external API should match caller mental model, not storage layout (§7.4).

No employer-stack or production claims made.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4** | High | Shallow modules, Java I/O, `BufferedInputStream` — Ch. 7 applies same depth heuristic to layers/decorators |
| **philosophy_software_design_2e_2021 Ch. 6** | High | Text line vs character API reprised in §7.4 — cross-link, do not duplicate full Ch. 6 ingest |
| **understanding_distributed_systems_2022** | Medium | Layering, pass-through config in services; cite Ousterhout context pattern at SYNTHESIS |
| **ddia_2e_2026** | Low–medium | System boundaries and abstraction shifts at storage/query layers |
| **ai_engineering_2025** | Low | Tool wrappers and agent middleware; apply Ch. 7 red flags when reviewing adapter depth |
| **Gang of Four / decorator pattern literature** | Conceptual tension | Ousterhout contests decorator overuse `[contested in chapter]` |

**Dedup guidance:** Canonical reference for **pass-through method/variable** terminology and **context object** trade-offs in SYNTHESIS; Ch. 4 remains canonical for **depth metric**; Ch. 6 for **information hiding** narrative of text API.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — student code, HTTP dispatch, Java I/O, datacenter cert chain, text API |
| Exercise hooks | **Weak in text** — no printed exercises; hooks require external codebase audits |
| Chapter boundary quality | **Clean** — self-contained §7.1–7.6; figures described in prose |
| Ingest suitability | **High** — actionable red flags, explicit contested opinions (context, decorators), ties prior chapters |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; within ≤5-year window relative to session (Jun 2025–2026); design-principles canon remains current |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press textbook; author bio in source file (L8147+) |
| **Primary-source citation density** | **PASS (low density flagged)** | Chapter is argument-and-example driven; references Gang of Four decorator pattern and prior-chapter examples by name only—**no section bibliography or external citations**. Appropriate for manifesto-style design text but not citation-heavy |
| **Contested claims flagged** | **PASS** | Decorator overuse critique, Java I/O merge recommendation, context-as-least-bad-global-state, "haven't found a better solution" — preserved above, not smoothed |
| **Worked examples (procedural/conceptual)** | **PASS** | Code extracts, layering walkthroughs, architectural figures (textual), refactor decision tree |

**Overall TEXTBOOK-Q1:** **PASS**

## Cross-canon synthesis notes

- **Net-complexity test (load-bearing):** Every layer, class, argument, or wrapper must remove more complexity than it adds; pass-through artifacts fail by construction (§7.6).
- **Legitimate duplication triad:** (1) dispatcher adds routing; (2) same-layer polymorphic implementations; (3) interface intentionally simpler than representation (§7.2, §7.4)—distinct from pass-through delegation.
- **Context pattern:** Prefer constructor-threaded context over signature threading; treat fields as immutable where possible; expect grab-bag discipline debt (§7.5).
- **Agent-stack heuristic `[inferred]`:** Before adding a provider wrapper class, run §7.3 four-question checklist; before threading `trace_id` through ten functions, use context.

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C07-001 | Each layer in a well-designed system should provide a different abstraction | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | intro |
| PSD2E-C07-002 | Pass-through methods increase interface complexity without increasing functionality | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.1 |
| PSD2E-C07-003 | Interface to functionality should live in the class that implements it | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.1 |
| PSD2E-C07-004 | Dispatchers provide useful functionality despite same signatures as callees | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.2 |
| PSD2E-C07-005 | Decorators tend shallow; Java I/O cited as shallow-class explosion | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.3 |
| PSD2E-C07-006 | Class interface should differ from internal representation for depth | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.4 |
| PSD2E-C07-007 | Context object is preferred pass-through-variable remedy; immutable fields; not ideal | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.5 |
| PSD2E-C07-008 | Different layer same abstraction likely fails net complexity benefit test | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch07_ingest.md | §7.6 |

## σ− (ingest boundaries)

- Figure 7.1/7.2 node-level diagrams not recoverable from `[]` placeholders — refactor options taken from captions only.
- Page numbers unavailable from text export; PDF required for print citation.
- No formal exercises or end-of-chapter summary bullets in slice (chapter ends at §7.6 prose).
- Do not infer MDCalc production architecture from pattern-portable hooks.
- Ch. 8+ not read; do not attribute pull-through generalizations beyond §7.6.

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
