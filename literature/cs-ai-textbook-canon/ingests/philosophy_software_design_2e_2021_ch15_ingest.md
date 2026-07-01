# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 15

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | A Philosophy of Software Design |
| **authors** | John Ousterhout |
| **edition** | 2nd Edition (v2.0, July 2021) |
| **ISBN_print** | 978-1-7321022-1-7 |
| **ISBN_electronic** | not stated separately in source text (print ISBN only) |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 15 |
| **chapter_title** | Write The Comments First |
| **subtitle** | Use Comments As Part Of The Design Process |
| **page_range** | Printed page numbers absent from text export; logical span §15.1–§15.6 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 15 argues that **documentation belongs at the start of development**, not after coding and unit testing. Ousterhout diagnoses why developers delay comments (code still changing; documentation as drudge work) and catalogs the failure modes of delayed documentation: comments never written, mentally checked-out authors, comments that merely repeat code, and lost design rationale. He prescribes a **comments-first workflow** for new classes—interface comment, then public method signatures with interface comments and empty bodies, iteration, instance-variable comments, then implementation—and claims three benefits: better comments, better system design, and more enjoyable comment-writing. The chapter reframes comments as the **only way to fully capture abstractions** and as a **design diagnostic**: long or hard-to-write interface comments signal poor abstractions and shallow modules (cross-ref Chapter 4). A **Red Flag: Hard to Describe** names this heuristic. Ousterhout rebuts the rework-cost objection with a back-of-the-envelope time estimate (comments ≤5% of development time) and argues comments-first may speed coding by stabilizing abstractions earlier. The chapter closes with an invitation to try the practice and report results.

**Sections ingested:** §15.1 Delayed comments are bad comments · §15.2 Write the comments first · §15.3 Comments are a design tool · §15.4 Early comments are fun comments · §15.5 Are early comments expensive? · §15.6 Conclusion · Red Flag: Hard to Describe (§15.3).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Thesis and delayed-documentation pathology (intro, §15.1)

- Putting off documentation until after coding and unit testing is "one of the surest ways to produce poor quality documentation." The best time to write comments is **at the beginning**, as you write code—making documentation part of the design process. This produces better documentation, better designs, and makes documentation "more enjoyable." [verified from text, lines 5938–5945]
- Almost every developer Ousterhout has met delays comments. Stated reason: code still changing; rewriting docs wastes effort—better to wait until code stabilizes. He suspects an additional reason: documentation viewed as **drudge work**, deferred as long as possible. [verified from text, lines 5949–5955]
- **Negative consequences of delay:** (1) documentation often **never gets written**—delay compounds ("code will be even more stable in a few more weeks"), task grows huge and unattractive, no convenient multi-day pause, rationalization to fix bugs or add features instead; (2) even with self-discipline, comments are **poor quality**—author has "checked out mentally," wants to finish quickly, memories of design are fuzzy, comments **repeat the code**, missing non-obvious design ideas that are no longer remembered. [verified from text, lines 5957–5981]

### Comments-first workflow (§15.2)

- Ousterhout's prescribed sequence for a new class: [verified from text, lines 5985–6006]
  1. Write the **class interface comment** first.
  2. Write **interface comments and signatures** for the most important public methods; leave method bodies **empty**.
  3. **Iterate** until basic structure feels right.
  4. Write declarations and comments for the most important **class instance variables**.
  5. **Fill in method bodies**, adding implementation comments as needed.
  6. While coding bodies, discover additional methods/variables—write **interface comment before each new method body**; fill instance-variable comments at declaration time.
- When code is done, comments are done—**no backlog** of unwritten comments. [verified from text, lines 6008–6009]
- **Benefit 1 (better comments):** key design issues fresh; writing interface comment before body focuses on **abstraction and interface** without implementation distraction; problems noticed and fixed during coding/testing so comments **improve over development**. [verified from text, lines 6011–6019]

### Comments as design tool (§15.3)

- **Benefit 2 (most important): improves system design.** Comments provide the **only way to fully capture abstractions**; good abstractions are fundamental to good design. Writing abstraction comments at the beginning enables **review and tuning before implementation code**. [verified from text, lines 6023–6027]
- To write a good comment you must identify the **essence** of a variable or code unit—most important aspects—**early**; otherwise you are "just hacking code." [verified from text, lines 6028–6031]
- Comments are a **"canary in the coal mine of complexity."** A method or variable requiring a **long comment** is a red flag for a poor abstraction. [verified from text, lines 6033–6035]
- **Depth heuristic via comments** (cross-ref Ch. 4): best classes have simple interfaces and powerful functions. Judge interface complexity from **comments describing it**. Short, simple interface comment that fully enables use → simple interface. No complete description without long, complicated comment → complex interface. Compare interface comment to implementation: if comment must describe all major implementation features → **shallow method**. Same for variables: long comment to fully describe → possible wrong decomposition. Writing comments enables **early evaluation** of design decisions. [verified from text, lines 6035–6050]
- **Red Flag: Hard to Describe** — interface comment for a method or variable should be **simple yet complete**; difficulty writing such a comment indicates a **design problem**. [verified from text, lines 6052–6057]
- Caveat: comments indicate complexity only if **complete and clear**; incomplete or cryptic comments do not measure depth. [verified from text, lines 6059–6063]

### Enjoyment and cost (§15.4–§15.5)

- **Benefit 3:** early comment-writing is **more fun**. Ousterhout enjoys the early design phase—fleshing abstractions and structure; comments record and test design quality. Goal: design expressible **completely and clearly in the fewest words**; simpler comments → pride. Under **strategic programming** (main goal = great design, not merely working code), comment-writing should be fun because it identifies best designs. [verified from text, lines 6067–6078]
- **Rework-cost rebuttal (§15.5):** delaying comments saves little. Estimate fraction of development time typing code **and** comments (including revisions)—unlikely >**10%** of total dev time. Even if half of lines are comments, comment-writing probably ≤**5%** of total time. Delaying saves only a fraction of that. [verified from text, lines 6082–6091]
- Comments-first **stabilizes abstractions before coding**, likely saving coding time. Code-first lets abstractions evolve during coding, requiring **more code revisions** than comments-first. Net: comments-first **might be faster overall**. [verified from text, lines 6093–6099]

### Conclusion (§15.6)

- Invitation: try comments-first, stick with it until habituated, reflect on comment quality, design quality, and enjoyment; report whether experience matches author's. [verified from text, lines 6103–6108]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 5932–6109 (inclusive) |
| **Chapter boundary** | Starts `Chapter 15` (L5932); ends before `Chapter 16` (L6110) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; adjacent Ch. 16 not read |
| **Figures** | None in chapter span |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Explain why delaying documentation until post-coding produces poor or absent comments.
2. Execute Ousterhout's **comments-first** class-development sequence (interface → method stubs → variables → bodies).
3. Use interface-comment length and clarity as a **design diagnostic** for abstraction quality and module depth.
4. Apply the **Hard to Describe** red flag when a method or variable resists simple, complete documentation.
5. Counter the "comments will need rewriting" objection with the author's time-fraction argument.
6. Relate comment-first practice to **strategic programming** and Chapter 4's deep-module heuristic.

### worked_examples_present

**N** — No standalone code listings or multi-step system walkthroughs. The chapter is **procedural and argumentative**: a numbered workflow (§15.2) and qualitative heuristics (comment length vs depth) serve as the primary instructional content.

| Example type | Section | Role |
|--------------|---------|------|
| Comments-first class workflow | §15.2 | Step-by-step design process |
| Interface-comment depth test | §15.3 | Qualitative shallow-vs-deep judgment |
| Time-fraction rework argument | §15.5 | Quantitative objection handling |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Implement one new class using comments-first; compare resulting interface comments to a code-first control on the same spec.
  - Audit an existing module: for each public method, draft the "simple yet complete" interface comment Ousterhout demands; flag **Hard to Describe** cases and propose refactors.
  - Measure team time on comment-writing vs total sprint time; test whether Ousterhout's ≤5% estimate holds locally.
  - Pair with Ch. 4 ingest: classify methods as deep/shallow using **comment-vs-implementation** rubric from §15.3.
  - Agent/skill authoring hook: write tool `description` and parameter docs **before** implementation; treat verbose or ambiguous docs as API design debt.

## Operator hooks

### 1. Foundation layer

Chapter 15 operationalizes themes from **Chapter 4 (deep modules)** and **Chapter 3 (strategic vs tactical programming)** into a concrete **design-time practice**: write interface documentation before implementation. It sits in the book's middle "how to design" arc after naming complexity (Ch. 2), choosing investment strategy (Ch. 3), and modular depth (Ch. 4), and before **Chapter 16 (Modifying Existing Code)**—which likely addresses comment maintenance on legacy code (not read in this ingest). For **w1_foundation**, this chapter is the canonical **comments-as-design** reference: it gives agents and humans a falsifiable heuristic (short complete interface comment = good abstraction) rather than generic "write more docs" advice. Prerequisite: Ch. 4 depth vocabulary. Complements **ai_engineering_2025** and agent-skill canon where **tool schemas and skill frontmatter** are the programmer-facing "interface comments."

### 2. MDCalc alignment

**[peripheral]** — No clinical AI, trace/eval, or regulated-deployment content. Portable pattern: define **informal contracts in prose before code**—analogous to documenting agent tool behavior, eval rubrics, or human-in-the-loop gates before pipeline implementation. The **Hard to Describe** red flag maps to oversized tool descriptions or skills that cannot state invocation preconditions in one short paragraph.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4** | High (internal) | §15.3 explicitly cross-references deep modules; dedup depth rubric—point here for comment-first workflow, Ch. 4 for module theory |
| **philosophy_software_design_2e_2021 Ch. 3** | Medium (internal) | Strategic programming cited in §15.4; link enjoyment of early design to strategic investment |
| **Clean Code / "self-documenting code"** | Conceptual tension | Ousterhout argues comments capture abstractions code cannot; `[contested in chapter]` vs minimal-comment cultures |
| **ai_engineering_2025** | Low–medium | Prompt/spec-before-code parallels; different domain |
| **grokking_algorithms_2e_2024** | None | No overlap in this chapter |

**Dedup guidance:** Treat Ch. 15 as the **canonical comments-first process** in SYNTHESIS; other ingests should reference this workflow rather than restating the six-step class sequence.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Weak** — process description and heuristics, no code artifacts |
| Exercise hooks | **Weak in text** — no printed exercises; strong external lab potential |
| Chapter boundary quality | **Clean** — self-contained §15.1–§15.6 |
| Ingest suitability | **High** — dense prescriptive chapter with anchorable claims, explicit red flag, and cross-chapter links |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; design-principles canon still current |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press |
| **Primary-source citation density** | **PASS (low density flagged)** | No bibliography, footnotes, or external citations in chapter—argument and personal practice only |
| **Contested claims flagged** | **PASS** | Universal "almost every developer" delay claim, 5–10% time fractions, and tension with minimal-documentation orthodoxy preserved—not smoothed |
| **Worked examples (procedural/conceptual)** | **CONDITIONAL PASS** | Strong procedural workflow; no code examples |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C15-001 | Best time to write comments is at the beginning of development, as you write code | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | intro |
| PSD2E-C15-002 | Delaying documentation often means it never gets written at all | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | §15.1 |
| PSD2E-C15-003 | Comments-first: class interface comment, then public method interface comments with empty bodies, iterate, then instance variables, then bodies | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | §15.2 |
| PSD2E-C15-004 | Comments provide the only way to fully capture abstractions | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | §15.3 |
| PSD2E-C15-005 | Red Flag Hard to Describe: difficulty writing simple complete interface comment indicates design problem | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | §15.3 |
| PSD2E-C15-006 | Writing comments probably accounts for ≤5% of total development time | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | §15.5 |
| PSD2E-C15-007 | Comments-first may be faster overall by stabilizing abstractions before coding | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch15_ingest.md | §15.5 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
