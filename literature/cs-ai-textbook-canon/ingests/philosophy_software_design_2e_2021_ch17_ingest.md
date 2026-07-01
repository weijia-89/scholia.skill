# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 17

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
| **chapter_number** | 17 |
| **chapter_title** | Consistency |
| **page_range** | Printed page numbers absent from text export; logical span §17.1–§17.4 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 17 treats **consistency** as a complexity-reduction tactic: similar things done in similar ways, dissimilar things in different ways. Ousterhout argues consistency yields **cognitive leverage** (learn a pattern once, reuse the mental model) and **fewer mistakes** (familiar-looking situations are safe to pattern-match). The chapter catalogs consistency at multiple levels—naming, coding style, shared interfaces, design patterns, and invariants—then turns to **how teams sustain** conventions under scale and turnover: documentation, automated enforcement, code review, and the cultural rule "when in Rome, do as the Romans do." A strong caution follows: resist one-off "improvements" that fracture established conventions unless new information and org-wide upgrade cost are both justified. §17.3 warns against **overzealous** consistency that forces genuinely dissimilar things into the same mold. The chapter closes by framing consistency as an **investment mindset** trade: upfront convention work for more obvious, faster, less buggy development.

**Sections ingested:** §17.1 Examples of consistency · §17.2 Ensuring consistency · §17.3 Taking it too far · §17.4 Conclusion.

**Cross-references in text (not ingested here):** Chapter 14 (naming); Chapter 13 (comment detail vs abstraction); Section 19.5 (design patterns).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Consistency as complexity management (intro)

- Consistency is a **powerful tool for reducing complexity** and making system behavior **more obvious**. [verified from text, lines 6354–6356]
- Consistent systems: **similar things done similarly; dissimilar things done differently**. [verified from text, lines 6356–6357]
- **Cognitive leverage:** once you learn how something is done in one place, that knowledge transfers immediately to other places using the same approach. Without consistency, developers must learn each situation separately—**more time**. [verified from text, lines 6357–6362]
- **Mistake reduction:** inconsistent systems let two situations **look the same when they differ**; developers pattern-match incorrectly. With consistency, assumptions based on familiar-looking situations are **safe**. Developers work **faster with fewer mistakes**. [verified from text, lines 6364–6370]

### Examples of consistency (§17.1)

- Consistency applies at **many levels** in a system. [verified from text, lines 6374–6375]

**Names**

- Chapter 14 already covered benefits of **using names consistently**. [verified from text, lines 6377–6378]

**Coding style**

- Development organizations commonly maintain **style guides** restricting structure beyond compiler rules: indentation, brace placement, declaration order, naming, commenting, dangerous-language-feature bans. [verified from text, lines 6380–6385]
- Style guidelines make code **easier to read** and can **reduce some kinds of errors**. [verified from text, lines 6385–6386]

**Interfaces**

- An interface with **multiple implementations** exemplifies consistency: understanding one implementation makes others easier because required features are already known. [verified from text, lines 6388–6392]

**Design patterns**

- **Design patterns** are generally accepted solutions to common problems (e.g., **model-view-controller** for UI). Reusing an existing pattern speeds implementation, increases likelihood of correctness, and makes code **more obvious to readers**. Patterns are expanded in **Section 19.5**. [verified from text, lines 6393–6398]

**Invariants**

- An **invariant** is a property of a variable or structure that is **always true** (example: each line in a text-line store ends with a newline). [verified from text, lines 6400–6403]
- Invariants **reduce special cases** in code and simplify reasoning about behavior. [verified from text, lines 6403–6405]

### Ensuring consistency (§17.2)

- Consistency is **hard to maintain** with many contributors over long timelines: groups unaware of each other's conventions; newcomers violate rules unintentionally and invent **conflicting** conventions. [verified from text, lines 6409–6413]

**Document**

- Create a document listing **most important overall conventions** (e.g., coding style); place it where developers will see it (conspicuous project Wiki spot). Encourage newcomers to read it and veterans to **review periodically**. Published Web style guides are reasonable starting points. [verified from text, lines 6416–6422]
- For **localized** conventions (e.g., invariants), document them **in code** at an appropriate spot. **Unwritten conventions are unlikely to be followed.** [verified from text, lines 6424–6426]

**Enforce**

- Even with documentation, developers forget conventions. **Best enforcement:** a tool checking violations, with **commits blocked** until checks pass. Automated checkers work especially well for **low-level syntactic** conventions. [verified from text, lines 6428–6433]

**Line-termination case study**

- A recent Ousterhout project suffered **CRLF vs LF** cross-platform churn: Unix (newline) vs Windows (CR+LF) editors made small edits appear as **whole-file diffs**, obscuring meaningful changes. [verified from text, lines 6435–6443]
- Team adopted **newline-only** convention but could not guarantee every tool complied; each new developer triggered a **rash of line-termination problems**. [verified from text, lines 6443–6447]
- **Solution:** short **pre-commit script** aborting commits if modified files contain carriage returns; manual mode repairs files by replacing CR+LF with LF. **Instantly eliminated problems** and **trained new developers**. [verified from text, lines 6449–6455]

**Code review**

- Code reviews **enforce conventions** and **educate** newcomers. **More nit-picky reviewers** → faster team learning and cleaner code. [verified from text, lines 6457–6460]

**When in Rome**

- **Most important convention:** follow **"When in Rome, do as the Romans do."** In a new file, inspect existing structure: public-before-private ordering, alphabetical methods, camelCase vs snake_case, etc. If something **might** be a convention, **follow it**. When deciding design, ask whether a similar decision exists elsewhere; if so, **find the example and match it**. [verified from text, lines 6462–6472]

**Don't change existing conventions**

- **Resist "improving"** established conventions; a "better idea" alone is **not** sufficient to introduce inconsistency. [verified from text, lines 6474–6476]
- **Value of consistency over inconsistency** is almost always **greater** than value of one approach over another. [verified from text, lines 6476–6478]
- Before inconsistent behavior, ask: (1) **Significant new information** unavailable when the old convention was set? (2) Is the new approach **so much better** it is worth updating **all old uses**? Proceed only if the organization agrees **yes** to both—then upgrade fully so **no sign of the old convention remains**. Risk remains that others **reintroduce** the old approach unknowingly. **Reconsidering established conventions is rarely a good use of developer time.** [verified from text, lines 6478–6489]

### Taking it too far (§17.3)

- Consistency also requires **dissimilar things done differently**. Overzealous forcing of dissimilar things into the same approach—same variable name for genuinely different concepts, wrong design pattern for an ill-fitting task—creates **complexity and confusion**. [verified from text, lines 6493–6499]
- Benefits require developer confidence: **"if it looks like an x, it really is an x."** [verified from text, lines 6499–6500]

### Conclusion (§17.4)

- Consistency exemplifies the **investment mindset** (cross-ref Chapter 3): upfront work deciding conventions, building automated checkers, mimicking similar situations in new code, educating in reviews. [verified from text, lines 6504–6507]
- **Return:** code is **more obvious**; developers understand behavior **more quickly and accurately**; they work **faster with fewer bugs**. [verified from text, lines 6508–6511]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 6350–6512 (inclusive) |
| **Chapter boundary** | Starts `Chapter 17` (L6350); ends before `Chapter 18` (L6513) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; Ch. 14 naming detail, Ch. 13 comments, §19.5 patterns referenced but not read |
| **Figures** | None in chapter span |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Define consistency in Ousterhout's terms and explain cognitive leverage and mistake-reduction mechanisms.
2. Enumerate consistency layers (names, style, interfaces, patterns, invariants) and give an example of each.
3. Design a convention-maintenance program: documentation placement, automated enforcement, review discipline.
4. Apply the "when in Rome" heuristic when entering unfamiliar code.
5. Evaluate whether a proposed convention change passes the two-question upgrade gate.
6. Recognize overzealous consistency and articulate the "looks like x, really is x" trust requirement.

### worked_examples_present

**Y** — One extended narrative plus illustrative micro-examples:

| Example | Section | Role |
|---------|---------|------|
| Text-line newline invariant | §17.1 | Invariant reduces special cases |
| MVC design pattern | §17.1 | Pattern reuse for obviousness |
| CRLF/LF pre-commit script | §17.2 | Automated enforcement case study |
| camelCase vs snake_case inspection | §17.2 | "When in Rome" local convention discovery |
| Forcing wrong pattern on ill-fitting task | §17.3 | Over-consistency failure mode |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Audit a repo for three convention classes (naming, formatting, structural); map documented vs enforced vs ad hoc.
  - Write a pre-commit or CI check for one low-level syntactic rule; measure false-positive rate on legacy files.
  - Role-play code review: one reviewer nit-picks style, one proposes a "better" naming scheme—apply §17.2 upgrade gate.
  - Find a place where two modules **look** consistent but behave differently; classify as inconsistency bug vs legitimate polymorphism.
  - Draft a one-page team conventions doc with Wiki placement and onboarding checklist.

## Operator hooks

### 1. Foundation layer

Chapter 17 operationalizes themes from earlier canon chapters: **investment mindset** (Ch. 3), **naming discipline** (Ch. 14), and **comment abstraction** (Ch. 13, referenced only at chapter boundary). It sits in the book's tactical-design arc after comments (Ch. 16) and before **obviousness** (Ch. 18)—consistency is presented as a prerequisite for code that reads predictably. For **w1_foundation**, this chapter supplies team-process vocabulary (document, enforce, review, don't unilaterally "improve") that complements structural heuristics from deep modules (Ch. 4) and information hiding (Ch. 5). It does not introduce new decomposition theory; it explains **how conventions scale** when many hands touch one codebase over years.

### 2. MDCalc alignment

**[peripheral]** — No clinical AI, agent orchestration, or regulated-deployment content. Portable lessons: **consistent tool/agent API shapes** across a product surface; **automated linting** for prompt-template or schema conventions; **invariants** on eval/trace payloads (e.g., required metadata fields always present). No production or employer-stack claims.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 14** | High (internal) | Naming consistency cited; ingest Ch. 14 for naming detail, Ch. 17 for cross-cutting consistency frame |
| **philosophy_software_design_2e_2021 Ch. 3** | Medium (internal) | Investment mindset echoed in §17.4 conclusion |
| **philosophy_software_design_2e_2021 §19.5** | Forward ref | Design patterns named here; full pattern discussion deferred |
| **Clean Code / style-guide culture** | Medium | Aligns on readability; Ousterhout adds **org-wide upgrade gate** and **anti-"better idea"** rule as distinctive emphasis |
| **ai_engineering_2025** | Low | Pipeline/config consistency analogs only |

**Dedup guidance:** Treat Ch. 17 as the **canonical consistency-and-conventions** reference in SYNTHESIS; point naming specifics to Ch. 14 and pattern catalog to §19.5 rather than duplicating.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Moderate** — one strong CRLF narrative; other examples are brief |
| Exercise hooks | **Weak in text** — no printed exercises; hooks require external labs |
| Chapter boundary quality | **Clean** — self-contained §17.1–§17.4 |
| Ingest suitability | **High** — actionable team practices with anchorable claims and clear failure modes (over-consistency, unilateral convention breaks) |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; design-principles canon still current |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press; author bio at end of source file |
| **Primary-source citation density** | **PASS (low density flagged)** | Argument-and-anecdote chapter; no per-section bibliography—appropriate for manifesto style |
| **Contested claims flagged** | **PASS** | "Consistency > marginal approach improvement" and "rarely good use of time to revisit conventions" are strong prescriptive claims—preserved, not smoothed |
| **Worked examples (procedural/conceptual)** | **PASS** | CRLF pre-commit case study is procedural; invariant/MVC examples conceptual |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C17-001 | Consistency reduces complexity and makes behavior more obvious | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | intro |
| PSD2E-C17-002 | Cognitive leverage: learn once, apply elsewhere | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | intro |
| PSD2E-C17-003 | Inconsistent systems invite unsafe pattern-matching and mistakes | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | intro |
| PSD2E-C17-004 | Invariants are always-true properties that reduce special cases | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.1 |
| PSD2E-C17-005 | Unwritten conventions are unlikely to be followed | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.2 |
| PSD2E-C17-006 | Best enforcement: checker tool blocking commits until pass | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.2 |
| PSD2E-C17-007 | Pre-commit CRLF check eliminated line-termination churn | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.2 |
| PSD2E-C17-008 | When in Rome: follow apparent local conventions in existing code | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.2 |
| PSD2E-C17-009 | Value of consistency usually exceeds value of a better isolated approach | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.2 |
| PSD2E-C17-010 | Overzealous consistency forces dissimilar things into same mold | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.3 |
| PSD2E-C17-011 | Benefits require: if it looks like x, it really is x | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.3 |
| PSD2E-C17-012 | Consistency is investment mindset: upfront convention work, faster fewer-bug development | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch17_ingest.md | §17.4 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
