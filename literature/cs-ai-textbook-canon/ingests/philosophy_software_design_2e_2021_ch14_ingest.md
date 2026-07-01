# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 14

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
| **chapter_number** | 14 |
| **chapter_title** | Choosing Names |
| **page_range** | Printed page numbers absent from text export; logical span §14.1–§14.7 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 14 treats **name choice** as an underrated but high-leverage design activity. Good names are **documentation**: they clarify code, reduce other documentation needs, and help catch errors; poor names add complexity, ambiguity, and bugs. Ousterhout frames naming as another instance of **incremental complexity** (cross-ref Ch. 2): one mediocre name barely matters, but thousands of mediocre names materially harm manageability.

The chapter opens with a **six-month Sprite file-system bug** caused by reusing `block` for both physical disk blocks and logical file blocks—readers reflexively misread the variable until instrumentation proved the fault. Ousterhout argues against settling for names that are merely "reasonably close."

**§14.2** positions naming as **mental imagery**: a good name conveys what an entity *is* and *is not*, even in isolation, within a two- or three-word budget. Names are **abstractions** that highlight important aspects and omit lesser detail (cross-ref Ch. 4).

**§14.3** develops **precision** as the first pillar of good names, with a **Red Flag: Vague Name** (`getCount` vs `numActiveIndexlets`), student-project counterexamples (`x`/`y`, `blinkStatus`, `VOTED_FOR_SENTINEL_VALUE`, `result`, Linux `struct socket`/`struct sock`), loop-variable exceptions (`i`, `j`), and the **over-specific** `selection` argument case. **Red Flag: Hard to Pick Name** links naming difficulty to weak variable design.

**§14.4** adds **consistency**: one canonical name per recurring concept (`fileBlock`), never reuse that name for other purposes, and keep the named purpose narrow enough that all uses share behavior—directly replaying the Sprite bug. Distinguish similar concepts with prefixes (`srcFileBlock`, `dstFileBlock`); apply loop-variable conventions (`i` outer, `j` inner).

**§14.5** warns against **extra words** (`fileObject`, class-name repetition in fields) and **type-in-name** conventions including **Hungarian Notation**—Ousterhout no longer recommends type prefixes given modern IDE navigation.

**§14.6** presents a **contested alternative**: Go's short-name culture (Andrew Gerrand, 2014 talk). Ousterhout disputes that short names improve the `RuneCount` example, criticizes ambiguous reuse of `ch`/`d`, and argues **readability is judged by readers, not writers**—while agreeing that name length should grow with declaration-to-use distance.

**§14.7** closes by tying good naming to the **investment mindset** (Ch. 3): upfront naming effort pays off; naming skill itself is an investment that becomes nearly free with practice.

**Sections ingested:** §14.1 Example: bad names cause bugs · §14.2 Create an image · §14.3 Names should be precise · §14.4 Use names consistently · §14.5 Avoid extra words · §14.6 A different opinion: Go style guide · §14.7 Conclusion · footnote 1 (Gerrand URL).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Naming as design and documentation (intro)

- Selecting names for variables, methods, and other entities is "one of the most underrated aspects of software design." Good names document code, ease understanding, reduce other documentation, and help detect errors; poor names increase complexity and cause ambiguities leading to bugs. [verified from text, lines 5533–5538]
- Name choice exemplifies incremental complexity: one mediocre name has little impact, but systems have thousands of variables—good names across all of them significantly affect complexity and manageability. [verified from text, lines 5539–5544]

### Sprite `block` bug (§14.1)

- A single poorly named variable can have severe consequences. Ousterhout's hardest-ever bug: in the late 1980s–early 1990s **Sprite** distributed OS, files occasionally lost data (a block zeroed without user modification). [verified from text, lines 5548–5554]
- After graduate students gave up, Ousterhout spent **six months** to find a simple root cause: `block` was used for both **physical disk block numbers** and **logical file block numbers**; a logical value was used where physical was required, overwriting an unrelated disk block with zeroes. [verified from text, lines 5560–5568]
- Multiple readers (including Ousterhout) scanned the code without noticing; seeing `block` in a physical context triggered reflexive assumption of a physical value. Instrumentation pinpointed the corrupting statement before he could trace the value's origin past the "mental block" of the name. [verified from text, lines 5570–5577]
- Distinct names (`fileBlock`, `diskBlock`) would likely have prevented the error; **distinct types** for the two block kinds would make interchange impossible. [verified from text, lines 5577–5582]
- Most developers use the first reasonable name (`block` is "not a horrible name" for either meaning) rather than investing in precise, unambiguous, intuitive names—yet the Sprite case cost enormous debugging time. [verified from text, lines 5584–5593]

### Create an image (§14.2)

- Naming goal: create a **mental image** of the entity's nature—what it is and what it is not. Test: if someone sees the name alone, without declaration, documentation, or use sites, how well can they guess the referent? Is a clearer name available? [verified from text, lines 5597–5604]
- Practical limit: more than two or three words makes names unwieldy—find few words capturing the most important aspects. [verified from text, lines 5605–5608]
- Names are **abstractions** providing simplified views; best names focus on what matters most and omit less important detail. [verified from text, lines 5610–5614]

### Precision (§14.3)

- Good names have **precision** and **consistency**; precision failures are most common—names too generic or vague invite wrong assumptions (as in the `block` bug). [verified from text, lines 5618–5622]
- **`IndexletManager::getCount()`**: "count" is too generic; `numActiveIndexlets` lets many readers guess the return value without documentation. [verified from text, lines 5623–5637]
- **Red Flag: Vague Name** — if a name could refer to many things, it conveys little and misuse is more likely. [verified from text, lines 5639–5643]

**Student-project examples:**

| Bad name | Problem | Better alternative | Lines |
|----------|---------|-------------------|-------|
| `x`, `y` (text editor) | Could mean screen pixels or file position | `charIndex`, `lineIndex` | 5648–5655 |
| `blinkStatus` | "status" vague for boolean; "blink" unclear what blinks | `cursorVisible` (boolean as predicate) | 5657–5680 |
| `VOTED_FOR_SENTINEL_VALUE` | Special but meaning opaque | `NOT_YET_VOTED` | 5682–5693 |
| `result` in void method | Implies return value; no semantic content | `mergedLine`, `totalChars`; `result` OK when actually returned | 5695–5705 |
| `struct socket` / `struct sock` | Too similar; subclass relationship unclear | e.g. `sock_base`, `inet_sock` | 5707–5713 |

- **Exception:** generic `i`, `j` for short loop spans where meaning is obvious from visible code (e.g. iterating lines). Long loops or obscure iteration semantics need descriptive names. [verified from text, lines 5715–5731]
- **Over-specific names:** `delete(Range selection)` suggests UI-selected text only; method deletes any range—`range` is better. [verified from text, lines 5733–5741]
- **Red Flag: Hard to Pick Name** — difficulty finding a precise, intuitive, short name suggests the variable lacks clear definition or purpose; consider refactoring (e.g. split one variable representing several things). Choosing names can **improve design** by exposing weaknesses. [verified from text, lines 5743–5757]

### Consistency (§14.4)

- Second pillar: **consistency**. For repeatedly manipulated concepts (e.g. block numbers in a file system), pick one canonical name (`fileBlock` for index within a file) and use it everywhere—like reusing a common class, it lets readers transfer knowledge across contexts. [verified from text, lines 5761–5770]
- Three consistency requirements: (1) always use the common name for that purpose; (2) never use it for anything else; (3) keep the purpose narrow enough that all variables with that name share behavior. The Sprite bug violated (3) by using `block` for two behaviors. [verified from text, lines 5772–5780]
- Multiple variables of the same kind: common name plus distinguishing prefix (`srcFileBlock`, `dstFileBlock`). [verified from text, lines 5782–5786]
- Loop convention: `i` outermost, `j` nested—readers make safe instant assumptions. [verified from text, lines 5788–5792]

### Avoid extra words (§14.5)

- Every word should add information; clutter causes wrapping without clarity. `fileObject` — "Object" likely adds nothing. [verified from text, lines 5796–5801]
- **Type-in-name** (`filePtr`) and **Hungarian Notation** (e.g. `arru8NumberList` = array of unsigned 8-bit integers) were common at Microsoft for C; Ousterhout **no longer recommends** type information in names—modern IDEs navigate to declarations or show types inline. [verified from text, lines 5803–5813]
- Instance variables repeating class name (`fileBlock` in class `File`) add no information when context is obvious; use `block` unless multiple block types coexist. [verified from text, lines 5815–5820]

### Go style guide dissent (§14.6) `[contested in chapter]`

- Not everyone agrees. **Go** developers (Andrew Gerrand) argue names should be very short, often single-character: "long names obscure what the code does." [verified from text, lines 5824–5827]
- Gerrand's `RuneCount` with `i`, `n` vs longer `buffer`, `index`, `count` — Ousterhout finds the longer version **no harder** to read; `count` clarifies `n`. Short `n` forced him to read through code; if `n` were system-wide convention for counts only, short form might work for others. [verified from text, lines 5856–5891]
- Go culture reuses short names for different concepts (`ch` = character or channel; `d` = data, difference, distance)—Ousterhout sees **ambiguous names** as confusion/error-prone like `block`. [verified from text, lines 5893–5896]
- **Readability is determined by readers, not writers** — short names fine if readers understand; switch to longer names on cryptic-code complaints (web search "go language short names"); Ousterhout would shorten if long names drew complaints. [verified from text, lines 5898–5905]
- **Agreement:** longer names when declaration-to-use **distance** is greater (loop `i`/`j` example). [verified from text, lines 5907–5910]

### Conclusion (§14.7)

- Well-chosen names make code **obvious**: first encounter yields a correct low-effort guess about behavior. [verified from text, lines 5914–5916]
- Good naming exemplifies **investment mindset** (Ch. 3): small upfront time eases future work and reduces bugs. Naming skill is itself an investment—initial frustration gives way to ease until good names cost almost no extra time ("benefits almost for free"). [verified from text, lines 5917–5926]

### Footnote 1

- Andrew Gerrand, "What's in a name?" Go talk: `https://talks.golang.org/2014/names.slide#1` [verified from text, lines 5930–5930]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 5529–5931 (inclusive) |
| **Chapter boundary** | Starts `Chapter 14` (L5529); ends before `Chapter 15` (L5932) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; adjacent Ch. 15 not read |
| **Figures** | None in chapter span |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Explain why naming is a design activity with system-wide incremental-complexity effects, not a cosmetic afterthought.
2. Apply the **isolation test**: evaluate whether a name conveys correct mental imagery without surrounding context.
3. Diagnose **vague**, **over-specific**, and **hard-to-name** variables; map each to refactoring or red-flag responses.
4. Enforce **three-part consistency** (canonical name, exclusive use, narrow shared behavior) for recurring domain concepts.
5. Trim **extra words** and justify when type-in-name conventions are unnecessary given IDE affordances.
6. Compare Ousterhout's precision/consistency doctrine with Go short-name culture and articulate the **reader-judged readability** criterion.

### worked_examples_present

**Y** — Multiple worked examples with code or incident detail:

| Example | Section | Role |
|---------|---------|------|
| Sprite `block` zeroing bug | §14.1 | Canonical naming-failure incident |
| `getCount` / `numActiveIndexlets` | §14.3 | Vague method name |
| GUI editor `x`/`y`, `blinkStatus` | §14.3 | Student-project renames |
| Consensus `VOTED_FOR_SENTINEL_VALUE` | §14.3 | Opaque sentinel |
| `result` in void method | §14.3 | Misleading local name |
| Linux `socket` / `sock` | §14.3 | Indistinguishable type names |
| `i` loop vs long loop | §14.3 | Precision exception |
| `delete(Range selection)` | §14.3 | Over-specific parameter |
| `srcFileBlock` / `dstFileBlock` | §14.4 | Consistent distinguished names |
| `fileObject`, Hungarian `arru8NumberList` | §14.5 | Clutter and deprecated style |
| Go `RuneCount` short vs long | §14.6 | Contested readability debate |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - **Name audit:** pick one module; list variables failing the isolation test; propose renames and note any design splits revealed.
  - **Sprite replay:** given a domain with two similar quantities (e.g. token index vs byte offset in a parser), write code that compiles with one shared name and refactor to distinct names/types; discuss bug class prevented.
  - **Consistency charter:** for a recurring concept in a codebase (user ID, request ID, shard key), draft a one-line naming convention satisfying all three consistency requirements.
  - **Go debate:** side-by-side review of a real Go file vs idiomatic longer-name refactor; collect reader comprehension timings or blind guesses (methodology external).
  - **Red-flag drill:** classify names as vague, hard-to-pick, or over-specific; pair each with a design action beyond rename-only.

## Operator hooks

### 1. Foundation layer

Chapter 14 is the book's dedicated **naming** chapter, cross-linked from **Chapter 7 (Different Layer, Different Abstraction)** and **Chapter 18 (Comments Should Describe Things Not Obvious from the Code)** in the wider text (not ingested here). It operationalizes earlier themes: **incremental complexity** (Ch. 2), **strategic investment** (Ch. 3), and **abstraction via names** (Ch. 4). For **w1_foundation**, it complements modular-depth guidance with local readability tactics every maintainer applies daily. The Sprite anecdote anchors systems thinking: naming errors can corrupt persistent state silently.

### 2. MDCalc alignment

**[peripheral]** — No clinical AI, agent orchestration, or regulated-deployment content. Portable lessons: prefer **precise domain terms** in tool schemas and trace field names (avoid generic `result`, `data`, `status`); enforce **consistent identifiers** across eval pipelines so analysts do not confuse logically distinct IDs; treat ambiguous short names in shared libraries as incident precursors. No employer-stack claims.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4** | Medium | Names as abstractions; omit unimportant detail |
| **philosophy_software_design_2e_2021 Ch. 7** | Medium | Book explicitly cross-refs Ch. 14 for naming elsewhere |
| **philosophy_software_design_2e_2021 Ch. 18** | Medium | Comments vs names as documentation; Ch. 14 defers some doc burden to names |
| **Clean Code (Martin)** | High conceptual | Both stress meaningful names; Ousterhout adds consistency rules, red flags, Go counterargument |
| **Go official style / Effective Go** | Direct tension | §14.6 cites Gerrand; preserve `[contested]` tag in SYNTHESIS |
| **ai_engineering_2025 / agent frameworks** | Low | Schema and variable naming in pipelines; pattern-portable only |

**Dedup guidance:** Treat this ingest as the **canonical Ousterhout naming** reference; other PSD ingests should link here for `block`-bug and three-part consistency rather than re-telling Sprite.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — incident narrative plus many before/after renames |
| Exercise hooks | **Weak in text** — no printed exercises; hooks require external labs |
| Chapter boundary quality | **Clean** — self-contained §14.1–14.7; footnote is Gerrand URL |
| Ingest suitability | **High** — actionable heuristics, explicit red flags, preserved dissent |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; ≤5 years from session date (Jun 2025) with margin |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press textbook |
| **Primary-source citation density** | **PASS (low density flagged)** | One external talk footnote (Gerrand 2014); chapter is anecdote-and-example driven like rest of book |
| **Contested claims flagged** | **PASS** | Go short-name culture, Hungarian notation deprecation, reader-vs-writer readability flagged—not smoothed |
| **Worked examples (procedural/conceptual)** | **PASS** | Sprite bug, multiple rename tables, Go `RuneCount` comparison |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C14-001 | Sprite bug: `block` conflated physical and logical block numbers; six-month debug | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.1 |
| PSD2E-C14-002 | Good names are documentation; poor names increase complexity and bugs | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | intro |
| PSD2E-C14-003 | Names are abstractions focusing on important aspects | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.2 |
| PSD2E-C14-004 | Red Flag: Vague Name — broad names invite misuse | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.3 |
| PSD2E-C14-005 | Red Flag: Hard to Pick Name — signals weak variable design | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.3 |
| PSD2E-C14-006 | Consistency: one name per purpose; never dual-purpose; narrow behavior scope | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.4 |
| PSD2E-C14-007 | No longer recommend Hungarian Notation / type-in-name with modern IDEs | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.5 |
| PSD2E-C14-008 | Readability judged by readers not writers; Go short names contested | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.6 |
| PSD2E-C14-009 | Good naming is investment mindset; skill becomes nearly free with practice | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch14_ingest.md | §14.7 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
