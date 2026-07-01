# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 9

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
| **chapter_number** | 9 |
| **chapter_title** | Better Together Or Better Apart? |
| **page_range** | Printed page numbers absent from text export; logical span intro–§9.9 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 9 addresses the **fundamental decomposition question**: given two pieces of functionality, should they live together or be separated? The scope spans **functions, methods, classes, and services**. Ousterhout frames the decision as minimizing **overall system complexity** and improving **modularity**, not maximizing the count of small components—subdivision itself introduces cost (more interfaces, management code, physical separation, duplication).

The chapter gives **four indicators of relatedness** that favor combining code (shared information, bidirectional co-use, conceptual overlap, mutual unintelligibility), then four **bring-together rules** (§9.1–§9.3) and one **separation rule** (§9.4). Two extended **GUI-editor and logging examples** (§9.5–§9.6) show when apparent relatedness misleads. §9.7 extends the analysis to **method splitting and joining**, with Figure 9.3 distinguishing subtask extraction from public API fission. §9.8 **contests Clean Code's length-based function splitting** in favor of depth over brevity. §9.9 concludes: choose structure for best information hiding, fewest dependencies, deepest interfaces.

**Sections ingested:** intro · §9.1 Bring together if information is shared · §9.2 Bring together if it will simplify the interface · §9.3 Bring together to eliminate duplication · §9.4 Separate general-purpose and special-purpose code · §9.5 Example: insertion cursor and selection · §9.6 Example: separate class for logging · §9.7 Splitting and joining methods · §9.8 A different opinion: Clean Code · §9.9 Conclusion · footnote 1 (Clean Code citation).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Framing: combine vs separate (intro)

- The central design question applies at every granularity: e.g., buffering with stream I/O vs separate class; HTTP parsing in one method vs many. [verified from text, lines 2953–2961]
- Goal: reduce **complexity of the system as a whole** and improve modularity—not "smallest possible components." Subdivision adds complexity absent before: (1) more components and interfaces to track; (2) management/orchestration code; (3) **separation**—good when components are independent (focus without distraction), bad when dependent (developers flip between sites or miss dependencies → bugs); (4) **duplication** across subdivided pieces. [verified from text, lines 2966–3000]
- **Relatedness indicators** favoring combination: shared information; **bidirectional** co-use (counter-example: block caches almost always use hash tables, but hash tables have many non-cache uses → keep separate); conceptual overlap under a higher category; one piece hard to understand without the other. [verified from text, lines 3002–3023]

### §9.1 — Bring together if information is shared

- Cross-ref §5.4 HTTP server: initial design split **read** (socket → string) and **parse** (string → components) across classes. Reader needed parsing knowledge to find request end (header parsing for content-length). Shared HTTP-format knowledge → combine read+parse in one place; code became **shorter and simpler**. [verified from text, lines 3029–3045]

### §9.2 — Bring together if it will simplify the interface

- Merging modules can yield a **simpler or easier-to-use** interface than the originals, especially when each implemented part of one solution. HTTP merge eliminated passing the request string between methods. [verified from text, lines 3047–3056]
- **Java I/O** (cross-ref Ch. 4): combining `FileInputStream` + `BufferedInputStream` with default buffering would hide buffering from most users; disable/replace methods available for the minority. [verified from text, lines 3058–3066]

### §9.3 — Bring together to eliminate duplication

- Repeated code patterns: factor into a method (best when snippet is long and replacement signature is simple); or refactor so snippet executes **once** (error-path cleanup example, Figures 9.1–9.2). [verified from text, lines 3068–3092]
- **`goto` for cleanup** `[contested in chapter]`: generally bad and can produce indecipherable code, but useful to escape nested structures and centralize cleanup before multiple error returns. [verified from text, lines 3086–3092]
- **Red flag: Repetition** — same (or nearly same) code appearing repeatedly signals missing abstractions. [verified from text, lines 3111–3115]

### §9.4 — Separate general-purpose and special-purpose code

- A module with a reusable mechanism should expose **only the general-purpose mechanism**—not specializations for particular uses, nor unrelated general mechanisms. Special-purpose code belongs elsewhere (typically with the use case). [verified from text, lines 3094–3109]
- **GUI editor (Ch. 6):** `Text` class holds general text ops; UI-specific ops (e.g., delete selection) in UI module—eliminated information leakage and extra interfaces vs specialized ops in `Text`. [verified from text, lines 3102–3109]
- **Red flag: Special-General Mixture** — specialized code inside a general mechanism complicates the mechanism and leaks information; future use-case changes drag mechanism changes. [verified from text, lines 3184–3190]

### §9.5 — Example: insertion cursor and selection (separate)

- GUI editor: blinking insertion cursor + highlighted selection (copy/delete); cursor always at one end of selection when selection exists; manipulated together (click-drag, insert deletes selection first). One team combined into single object (two positions + booleans). [verified from text, lines 3129–3154]
- Combined object **awkward**: higher-level code still treated selection and cursor as distinct, invoking separate methods; implementation **more complex** (boolean for which selection end is cursor, indirect cursor retrieval). **Not closely enough related** to combine. [verified from text, lines 3156–3171]
- Revision: separate selection and cursor; introduced **`Position`** (line + character)—selection = two Positions, cursor = one; simpler usage and implementation; Positions reused elsewhere. Demonstrates lower-level general-purpose interface (Ch. 6). [verified from text, lines 3172–3182]

### §9.6 — Example: logging class (bring together / inline)

- Student RPC project: `try/catch` at error site called `NetworkErrorLogger.logRpcOpenError(...)` in a nested static class with methods like `logRpcSendError`, `logRpcReceiveError`. [verified from text, lines 3192–3257]
- Separation **added complexity without benefit**: methods **shallow** (often one line) but heavily documented; each invoked **once**; highly dependent on call site—readers flip between invocation and logger. **Better:** inline logging at detection; easier to read; eliminates logger interfaces. [verified from text, lines 3259–3272]

### §9.7 — Splitting and joining methods

- Length alone is **rarely** a good split justification; developers tend to **split too much**. Splitting adds interfaces and separates related code. Rigid student rules (e.g., split >20 lines) criticized. [verified from text, lines 3274–3291]
- Long methods acceptable when blocks are relatively independent (read sequentially) or **interdependent** (keeping together lets readers see interactions). Hundreds of lines fine if **deep**: simple signature, easy to read. [verified from text, lines 3293–3304]
- Design goal per method: **one thing, completely**; simple interface; **deep** (interface ≪ implementation). Length secondary if those hold. [verified from text, lines 3312–3318]
- **Figure 9.3 patterns:**
  - **(b) Extract subtask** (preferred): child holds subtask; parent retains original interface and calls child. Valid when child reader needs no parent context and parent reader need not know child implementation; child is **general-purpose** / reusable. Flipping between parent and child to understand → **Conjoined Methods** red flag. [verified from text, lines 3320–3337]
  - **(c) Split into two public methods:** when original had overly complex interface doing **unrelated** things; each new interface simpler; ideal if most callers need only one. Risk: callers must invoke both and pass state → shallow methods (9.3d). [verified from text, lines 3339–3362]
- **Joining methods** can simplify: two shallow → one deep; eliminate duplication, inter-method dependencies, intermediate structures; improve encapsulation; simpler interface (§9.2). [verified from text, lines 3364–3371]
- **Red flag: Conjoined Methods** — cannot understand one method without the other; applies when physically separated code is mutually unintelligible. [verified from text, lines 3373–3380]

### §9.8 — A different opinion: Clean Code

- Robert C. Martin (*Clean Code*, 2009): functions should be **extremely short**; even 10 lines too long; if/else/while blocks should be one line (often a function call); indent level ≤1–2. [verified from text, lines 3382–3395]
- Ousterhout **partial agreement** `[contested in chapter]`: shorter generally easier, but below a few dozen lines further shrinkage unlikely to help readability. Key test: does splitting reduce **overall system complexity**? More functions → more interfaces; too-small functions become **conjoined**. **Depth before length**; don't sacrifice depth for brevity. [verified from text, lines 3397–3410]

### §9.9 — Conclusion

- Split or join modules based on **complexity**; prefer best **information hiding**, **fewest dependencies**, **deepest interfaces**. [verified from text, lines 3412–3416]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 2949–3421 (inclusive) |
| **Chapter boundary** | Starts `Chapter 9` (L2949); ends before `Chapter 10` (L3422) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; adjacent Ch. 10 not read |
| **Figures** | Fig. 9.1–9.3 referenced; image data `[]` placeholder only in export |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. State the costs and benefits of subdividing code at any modular granularity.
2. Apply the four **relatedness** heuristics and recognize when bidirectional co-use fails.
3. Decide when to combine modules for **shared information**, **simpler interfaces**, or **duplication removal**.
4. Separate **general-purpose mechanisms** from **special-purpose** consumers without information leakage.
5. Evaluate real examples (cursor/selection, inline vs extracted logging) against combine/separate rules.
6. Split or join **methods** using subtask extraction vs public API fission—and detect **conjoined methods**.
7. Contrast Ousterhout's **depth-over-length** position with Clean Code's small-function orthodoxy.

### worked_examples_present

**Y** — Multiple worked examples with code or scenario detail:

| Example | Section | Role |
|---------|---------|------|
| Buffering with stream I/O vs separate | intro | Granularity of decomposition question |
| Hash table vs block cache | intro | Bidirectional co-use counter-example |
| HTTP read + parse merge | §9.1 | Shared information |
| HTTP interface elimination | §9.2 | Simpler combined interface |
| Java default buffering | §9.2 | Auto behavior for common case |
| Packet-type LOG duplication + goto cleanup | §9.3 | Duplication elimination (Figs. 9.1–9.2) |
| Text class vs UI module (Ch. 6) | §9.4 | General vs special-purpose |
| Insertion cursor + selection | §9.5 | When **not** to combine |
| `Position` class | §9.5 | General-purpose lower-level abstraction |
| `NetworkErrorLogger` | §9.6 | When **not** to separate |
| Method split patterns | §9.7 | Figure 9.3 (a)–(d) |
| Clean Code function-size rules | §9.8 | Contested alternative |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Given a microservice or agent-tool boundary, score relatedness on all four intro indicators; argue combine vs separate.
  - Refactor a shallow `*ErrorLogger` or `*Helper` with single-call-site methods into inlined or deep-module form.
  - Audit a codebase for **Repetition**, **Special-General Mixture**, and **Conjoined Methods** red flags.
  - Split a long method using 9.3(b) subtask extraction; if readers must flip between parent and child, revert and justify.
  - Debate: defend or refute Clean Code's 10-line function rule using Ousterhout's complexity metric.

## Operator hooks

### 1. Foundation layer

Chapter 9 operationalizes **modular decomposition tactics** introduced in Ch. 4 (depth), Ch. 5 (information hiding / HTTP), and Ch. 6 (general-purpose interfaces). It is the canon's primary reference for **when to merge vs split** modules and methods—a prerequisite for tactical chapters on comments, naming, and performance that assume stable boundaries. Pairs directly with **philosophy_software_design_2e_2021 Ch. 4** (depth heuristic) and **Ch. 5** (information leakage); avoid re-ingesting the full HTTP or GUI-editor stories elsewhere—cross-link §9.1/§9.5 instead.

### 2. MDCalc alignment

**[peripheral]** — No clinical AI, agents, or regulated-deployment content. Portable patterns: prefer **one deep agent/tool call** over multi-step shallow helpers callers must chain; inline observability at failure sites when logger wrappers are single-use and force context-switching; separate **generic retrieval/RAG plumbing** from **domain-specific post-processing**.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4–6** | High | Same HTTP, Java I/O, GUI-editor examples; Ch. 9 adds combine/split decision rules |
| **philosophy_software_design_2e_2021 Ch. 5** | Medium | §9.1 cites §5.4 HTTP decomposition |
| **Clean Code (Martin, 2009)** | Direct tension | §9.8 names and quotes opposing guidance |
| **grokking_algorithms_2e_2024** | Low | Hash-table example touches shared CS structures |
| **ai_engineering_2025** | Low | Tool/pipeline boundary design; no duplicate examples |

**Dedup guidance:** Treat Ch. 9 as the **canonical combine-vs-separate** and **method split/join** reference; Ch. 4/6 ingests should point here for decomposition decisions rather than re-deriving cursor/selection or logging examples.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — HTTP, GUI, logging, method figures |
| Exercise hooks | **Weak in text** — no printed exercises; lab hooks inferred |
| Chapter boundary quality | **Clean** — self-contained §9.1–9.9; footnote 1 at chapter end |
| Ingest suitability | **High** — actionable heuristics, red flags, and explicit contestation of Clean Code |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; ≤5 years from session date (Jun 2025); design-principles canon remains current |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press textbook |
| **Primary-source citation density** | **PASS (low density flagged)** | Argument-and-example driven; one footnote citing *Clean Code* (2009); cross-refs to earlier chapters—not bibliography-heavy |
| **Contested claims flagged** | **PASS** | `goto` for cleanup, Clean Code function length, student "20-line" rules, default buffering—all preserved as contested |
| **Worked examples (procedural/conceptual)** | **PASS** | Multiple code scenarios and Figure 9.3 decision patterns |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C09-001 | Subdivision adds interfaces, separation cost, and duplication risk | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | intro |
| PSD2E-C09-002 | Combine when pieces share information (HTTP read+parse) | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.1 |
| PSD2E-C09-003 | Combine when merge simplifies interface or enables default behavior | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.2 |
| PSD2E-C09-004 | Separate general-purpose mechanisms from special-purpose use code | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.4 |
| PSD2E-C09-005 | Cursor and selection better separated via Position abstraction | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.5 |
| PSD2E-C09-006 | Single-use shallow loggers should be inlined at detection site | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.6 |
| PSD2E-C09-007 | Method length alone rarely justifies split; prefer subtask extraction | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.7 |
| PSD2E-C09-008 | Depth more important than length; contests Clean Code small functions | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch09_ingest.md | §9.8 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
