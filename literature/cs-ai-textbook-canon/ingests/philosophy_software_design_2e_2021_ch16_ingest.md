# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 16

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
| **chapter_number** | 16 |
| **chapter_title** | Modifying Existing Code |
| **page_range** | Printed page numbers absent from text export; logical span §16.1–§16.6 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 16 shifts from **initial** design and implementation (earlier chapters) to **evolutionary** maintenance: how to keep complexity from creeping in as systems grow through bug fixes and new features. Ousterhout opens by restating that mature system design is determined more by incremental changes than by any upfront conception (cross-ref Ch. 1). The chapter's first half (**§16.1**) extends the **tactical vs strategic programming** distinction (Ch. 3) to code modification: resist "smallest possible change" fixes that accumulate special cases; instead refactor so each change leaves the system as if originally designed for that change. The second half (**§16.2–§16.6**) is a practical discipline for **maintaining comments** during modification—proximity to code, single source of truth, pre-commit diff review, and favoring higher-level comments that survive minor edits (cross-ref Ch. 13).

**Sections ingested:** §16.1 Stay strategic · §16.2 Maintaining comments: keep the comments near the code · §16.3 Comments belong in the code, not the commit log · §16.4 Maintaining comments: avoid duplication · §16.5 Maintaining comments: check the diffs · §16.6 Higher-level comments are easier to maintain.

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Evolutionary design context (chapter intro)

- Large systems develop through evolutionary stages adding capabilities and modifying existing modules; design is **constantly evolving**. [verified from text, lines 6114–6117]
- "It isn't possible to conceive the right design for a system at the outset"; a mature system's design is determined **more by changes made during evolution** than by initial conception. [verified from text, lines 6118–6120]
- Prior chapters addressed squeezing complexity during initial design; this chapter addresses **preventing complexity from creeping in** as the system evolves. [verified from text, lines 6121–6123]

### Stay strategic when modifying code (§16.1)

- **Tactical programming** (Ch. 3): primary goal is getting something working quickly, even at the cost of added complexity. **Strategic programming**: primary goal is great system design. Tactical approach "very quickly leads to a messy system design." [verified from text, lines 6127–6132]
- For maintainable/enhanceable systems, **"working" isn't a high enough standard**; design must be prioritized strategically—including when modifying existing code. [verified from text, lines 6132–6135]
- Typical modification mindset: **"what is the smallest possible change I can make that does what I need?"** Developers sometimes justify this because they are uncomfortable with unfamiliar code and fear larger changes introduce bugs. [verified from text, lines 6137–6142]
- Each minimal change introduces special cases, dependencies, or other complexity; **system design gets "just a bit worse"** with each evolutionary step—problems accumulate. [verified from text, lines 6143–6146]
- **Strategic modification goal:** when finished with each change, the system should have the structure it would have had if designed from the start with that change in mind. [verified from text, lines 6148–6151]
- Resist quick fixes; ask whether current design is still best given the desired change; if not, **refactor to the best possible design** so design **improves with every modification**. [verified from text, lines 6152–6156]
- **Investment mindset** (p. 15): extra refactoring time yields a cleaner system, faster subsequent development, and recouped effort. [verified from text, lines 6158–6162]
- Even when a particular change does not require refactoring, **look for design imperfections to fix while in the code**; try to improve design at least a little with every modification. [verified from text, lines 6162–6165]
- **"If you're not making the design better, you are probably making it worse."** [verified from text, lines 6165–6167]
- Investment mindset **sometimes conflicts with commercial realities** `[contested in chapter]`: e.g., three-month "right way" refactor vs two-hour quick fix under tight deadlines; or refactoring creating incompatibilities across teams. [verified from text, lines 6169–6175]
- Nonetheless, **resist compromises as much as possible**; ask whether this is the best achievable clean design under current constraints. [verified from text, lines 6177–6179]
- Seek **almost-as-clean alternatives** completable in days rather than months; or negotiate time to return after the deadline. [verified from text, lines 6180–6183]
- Every development organization should plan a **small fraction of total effort** on cleanup/refactoring; this pays for itself long-term. [verified from text, lines 6183–6186]

### Keep comments near the code (§16.2)

- Code changes often **invalidate existing comments**; developers forget to update them → stale, inaccurate comments. [verified from text, lines 6190–6192]
- Stale comments frustrate readers; many stale comments cause readers to **distrust all comments**. [verified from text, lines 6193–6195]
- **Best practice:** position comments close to the code they describe so developers see them when changing code. Farther from associated code → less likely proper update. [verified from text, lines 6199–6202]
- **Best place for a method's interface comment:** in the code file, right next to the method body—changes to the method involve that code, so interface comments are visible for update. [verified from text, lines 6203–6206]
- **C/C++ header-file placement** `[contested in chapter]`: interface comments next to declaration in `.h` are "a long way from the code"; body modifiers won't see them without extra file-switching work. [verified from text, lines 6208–6213]
- **Users should not need to read code or header files**; they should get information from tool-generated documentation (Doxygen, Javadoc) and IDE presentation (hover/type completion). Documentation should live where **developers working on the code** find it convenient. [verified from text, lines 6215–6222]
- **Implementation comments:** do not cluster all comments at the method top; **spread to the narrowest scope** covering referenced code. [verified from text, lines 6224–6227]
- **Three-phase method example:** write separate phase comments above each phase's first line; optional top-of-method strategy comment listing phases only (`// We proceed in three phases:` + phase names); details above each phase. [verified from text, lines 6227–6243]
- **Proximity–abstraction rule:** the farther a comment is from its code, the **more abstract** it should be (reduces invalidation by detail changes). [verified from text, lines 6245–6247]

### Comments in code, not commit logs (§16.3)

- **Common mistake:** detailed change information in the **commit message** but not in the code. [verified from text, lines 6251–6252]
- Commit logs are browsable but developers needing the information are **unlikely to scan the repository log**; even if they do, finding the right message is tedious. [verified from text, lines 6253–6257]
- **Commit-message test:** ask whether developers will need this information in the future; if yes, **document in the code**. [verified from text, lines 6259–6260]
- **Worked example:** commit describing a subtle problem motivating a change—without in-code documentation, a later developer might undo the change and **re-create the bug**. [verified from text, lines 6261–6263]
- Including the same information in the commit message is fine, but **the code is the primary location**. [verified from text, lines 6264–6266]
- Illustrates placing documentation **where developers are most likely to see it**; the commit log rarely qualifies. [verified from text, lines 6267–6268]

### Avoid duplication (§16.4)

- **Second maintenance technique:** avoid duplicated documentation—harder to find and update all copies. [verified from text, lines 6273–6275]
- **Document each design decision exactly once.** If multiple code places are affected, don't repeat at each; find the **most obvious single place**. [verified from text, lines 6275–6278]
- **Variable-behavior example:** tricky behavior affecting multiple uses → document in comment next to the **variable's declaration** (natural lookup point). [verified from text, lines 6279–6284]
- If no obvious single place: use a **`designNotes` file** (§13.7) or pick the best available place and add **short cross-references** elsewhere (`See the comment in xyz…`). [verified from text, lines 6286–6290]
- **Stale reference is self-evident** if master comment moved/deleted; duplicated stale copies give **no indication** readers use outdated information. [verified from text, lines 6291–6298]
- **Don't redocument one module's decisions in another**—e.g., don't explain called-method behavior before a call; readers should use interface comments (IDEs often surface these on hover/selection). [verified from text, lines 6300–6308]
- If information exists **outside the program** (HTTP spec on the web, user manual), don't repeat it—**reference externally** (URL or short pointer). [verified from text, lines 6310–6315]
- **Command-method example:** `// Implements the Foo command; see the user manual for details.` [verified from text, lines 6317–6324]
- Readers must easily find all needed documentation, but **you don't have to write all of it**. [verified from text, lines 6326–6328]

### Check the diffs (§16.5)

- Before committing, **scan all changes** in the revision-control diff; ensure each change is **properly reflected in documentation**. [verified from text, lines 6332–6335]
- Pre-commit scans also catch **debugging code left in** and **unfixed TODO items**. [verified from text, lines 6335–6337]

### Higher-level comments easier to maintain (§16.6)

- Comments are easier to maintain when **higher-level and more abstract** than the code—they don't mirror implementation details, so **minor code changes don't invalidate** them; only overall behavior changes do. [verified from text, lines 6341–6345]
- Cross-ref Ch. 13: some comments must be detailed and precise. [verified from text, lines 6345–6346]
- In general, the **most useful comments** (those that don't simply repeat the code) are also the **easiest to maintain**. [verified from text, lines 6346–6348]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 6110–6349 (inclusive) |
| **Chapter boundary** | Starts `Chapter 16` (L6110); ends before `Chapter 17` (L6350) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; adjacent Ch. 17 not read |
| **Figures** | None in chapter span |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Explain why evolutionary modification—not initial design—dominates mature system structure.
2. Contrast tactical "smallest change" fixes with strategic refactor-on-touch modification.
3. Apply the investment mindset when weighing quick fixes against refactoring under deadline pressure.
4. Place interface and implementation comments using proximity, scope-narrowing, and abstraction-distance rules.
5. Decide whether documentation belongs in code vs commit messages vs external references.
6. Maintain single-source documentation with cross-references and pre-commit diff review.

### worked_examples_present

**Y** — Multiple worked examples with concrete guidance:

| Example | Section | Role |
|---------|---------|------|
| Smallest-change bug fix mindset | §16.1 | Tactical accumulation of complexity |
| 3-month refactor vs 2-hour fix | §16.1 | Commercial constraint tradeoff |
| Method interface comment in `.c` vs `.h` | §16.2 | Proximity beats header convention |
| Three-phase method comments | §16.2 | Scope-narrowed implementation comments |
| Subtle-bug motivation in commit only | §16.3 | Risk of reintroducing fixed bugs |
| Tricky variable behavior | §16.4 | Single canonical comment location |
| Cross-reference to moved master comment | §16.4 | Self-evident stale refs vs silent duplication |
| HTTP protocol / user-manual commands | §16.4 | External doc by reference |
| Pre-commit diff scan | §16.5 | Documentation + TODO/debug catch |
| Abstract vs detail-level comments | §16.6 | Maintenance durability |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Audit a recent PR: classify each change as tactical vs strategic; identify accumulated special cases.
  - Pick one stale-comment hotspot; relocate comments per §16.2 proximity rules; measure diff noise.
  - Find commit-message-only rationale in repo history; migrate load-bearing rationale into code comments.
  - Deduplicate repeated design explanations; add `designNotes` entry or cross-refs per §16.4.
  - Add a pre-commit hook or checklist mirroring §16.5 diff scan.
  - Rewrite low-level comments as higher-level behavioral statements (§16.6) without losing precision where Ch. 13 requires it.

## Operator hooks

### 1. Foundation layer

Chapter 16 is the book's **maintenance-and-evolution** capstone for complexity control: it connects Ch. 1's incremental-development thesis and Ch. 3's strategic/investment mindset to day-to-day modification work. It directly precedes **Chapter 17 (Consistency)**—comment discipline here sets up consistency-of-documentation patterns; Ch. 13's `designNotes` and comment-style guidance are assumed background. For **w1_foundation** canon, this chapter operationalizes "don't let complexity creep back in" after modular-design chapters (4–15). It is prerequisite context for any ingest discussing **technical debt paydown**, **refactor-on-touch culture**, or **living documentation** in agent/LLM codebases—without duplicating those domains' specifics.

### 2. MDCalc alignment

**[peripheral]** — No clinical AI, trace/eval, or regulated-deployment content. Portable patterns only: **document invariant rationale in code** (not commit-only) before agents or juniors rewrite "mysterious" guards; **single-source comments** reduce drift when multiple services touch shared contracts; **strategic small refactors** when extending eval harnesses or tool schemas beat layered special cases. No production or employer-stack claims.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 3** | High | Tactical/strategic and investment mindset—Ch. 16 applies same frame to modifications; cross-link, don't re-derive |
| **philosophy_software_design_2e_2021 Ch. 13** | High | Comment style, `designNotes` (§13.7)—Ch. 16 is maintenance-focused extension |
| **philosophy_software_design_2e_2021 Ch. 1** | Medium | Iterative/incremental development framing |
| **Clean Code / "boy scout rule"** | Medium | Overlapping "leave code better" ethos; Ousterhout emphasizes **design structure**, not just local cleanliness |
| **ai_engineering_2025** | Low | Prompt/schema iteration analogs `[inferred]` only—no text overlap |
| **kaestner_ml_production_2025** | Low | Production refactor/debt themes; different domain |

**Dedup guidance:** Treat Ousterhout Ch. 16 as the **canonical strategic-modification + comment-maintenance** reference for SYNTHESIS; point Ch. 3 for mindset origin and Ch. 13 for comment authoring rules.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Moderate** — procedural examples and code-comment snippets, no large code listings |
| Exercise hooks | **Weak in text** — no printed exercises; hooks require repo/PR labs |
| Chapter boundary quality | **Clean** — self-contained §16.1–§16.6; full chapter within assigned lines |
| Ingest suitability | **High** — actionable maintenance discipline with anchorable claims and explicit commercial-tradeoff caveats |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; current for design-principles canon |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press textbook |
| **Primary-source citation density** | **PASS (low density flagged)** | Argument-and-practice chapter; cross-refs to Ch. 1, 3, 13; no per-section bibliography |
| **Contested claims flagged** | **PASS** | Commercial refactor compromises, C header comment placement flagged—not smoothed |
| **Worked examples (procedural/conceptual)** | **PASS** | Multiple comment-placement and modification-discipline scenarios |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C16-001 | Mature system design determined more by evolutionary changes than initial conception | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | intro |
| PSD2E-C16-002 | Smallest-possible-change mindset during modifications is tactical programming | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.1 |
| PSD2E-C16-003 | Strategic goal: after each change, structure as if originally designed for that change | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.1 |
| PSD2E-C16-004 | If you're not making the design better, you are probably making it worse | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.1 |
| PSD2E-C16-005 | Organizations should allocate a small fraction of effort to cleanup/refactoring | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.1 |
| PSD2E-C16-006 | Best place for method interface comment is next to method body in code file | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.2 |
| PSD2E-C16-007 | Farther a comment is from code, the more abstract it should be | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.2 |
| PSD2E-C16-008 | Load-bearing change rationale belongs in code, not only commit messages | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.3 |
| PSD2E-C16-009 | Document each design decision exactly once; avoid duplicated comments | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.4 |
| PSD2E-C16-010 | Pre-commit diff scan should verify documentation matches each change | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.5 |
| PSD2E-C16-011 | Higher-level comments that don't repeat code are easiest to maintain | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch16_ingest.md | §16.6 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
