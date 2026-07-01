# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 21

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
| **chapter_number** | 21 |
| **chapter_title** | Decide What Matters |
| **page_range** | Printed page numbers absent from text export; logical span §21.1–§21.5 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 21 is the **penultimate synthesis chapter** of *A Philosophy of Software Design*. Ousterhout states that one of the most important elements of good design is **separating what matters from what does not**—structuring systems around what matters, minimizing the impact of what does not, **emphasizing** the former and **hiding** the latter. He argues that many prior chapters (abstractions, naming, performance) share this separation at their core.

The chapter prescribes **how to decide** what matters (leverage, invariants, comparing alternatives, hypothesis-and-learn for inexperienced designers), **how to minimize** what matters (fewer parameters, defaults, fewer places of impact, hiding, low-level exception handling, auto-derived configuration), and **how to emphasize** what matters (prominence, repetition, centrality—with the converse heuristic that frequently seen, repeated, or structurally central ideas matter). §21.4 catalogs two failure modes: treating too much as important (clutter, shallow classes, Java I/O buffering example) and failing to recognize importance (hidden information, unavailable functionality, unknown unknowns). §21.5 extends the lens to technical writing and life philosophy, closing with **"good taste"** as the ability to distinguish important from unimportant—a capstone virtue for software designers.

**Sections ingested:** §21.1 How to decide what matters? · §21.2 Minimize what matters · §21.3 How to emphasize things that matter · §21.4 Mistakes · §21.5 Thinking more broadly.

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Core thesis (intro)

- Good design **separates what matters from what does not**; structure around what matters; minimize impact of the rest; emphasize important things, hide unimportant ones. [verified from text, lines 7471–7476]
- Prior chapters embody this separation: module interfaces reflect what matters to users; implementation hides what does not; variable names encode what matters most about a variable; performance-critical modules (§20.4) structure around performance goals with minimal method calls and special-case checks on the hot path while staying clean and obvious. [verified from text, lines 7478–7490]

### How to decide what matters (§21.1)

- **External constraints** sometimes impose importance (e.g., performance in §20.4); more often the **designer decides**; even with external constraints, the designer must determine **what matters most** in achieving them. [verified from text, lines 7494–7498]
- **Leverage** is the primary decision heuristic: solutions where fixing one problem solves many others, or where one piece of information unlocks understanding of many things. [verified from text, lines 7500–7502]
- **Text-storage example (§6.2 callback):** general-purpose insert/delete **ranges** interface solves many problems; specialized `backspace` solves only one—the general interface provides more leverage. At the text-class interface level, whether the caller pressed backspace does not matter; what matters is that text must be deleted. [verified from text, lines 7503–7510]
- **Invariants** are leverage points: knowing an invariant for a variable or structure lets you predict behavior across many situations. [verified from text, lines 7510–7513]
- **Multiple options** ease prioritization: for variable names, list related words mentally, pick the few conveying most information—an instance of the **"design it twice"** principle. [verified from text, lines 7515–7520]
- When importance is unclear (especially for **younger developers** with less experience), **hypothesize** ("I think this is what matters most"), commit, build under that assumption, then evaluate: if right, reflect on why and what clues existed; if wrong, reflect on missed clues. Either way, learning improves future choices. [verified from text, lines 7522–7532]

### Minimize what matters (§21.2)

- **Make as little matter as possible** → simpler systems. [verified from text, lines 7536–7537]
- Tactics: minimize constructor parameters or provide **defaults** reflecting common usage; for things that do matter, minimize **number of places** they matter. [verified from text, lines 7537–7540]
- Hidden module information does not matter outside the module. Exceptions handled entirely at low level do not matter to the rest of the system. Configuration computed automatically from behavior (vs manual admin choice) no longer matters to administrators. [verified from text, lines 7540–7546]

### Emphasize what matters (§21.3)

Three emphasis mechanisms plus converse diagnostic:

| Mechanism | Definition | Lines |
|-----------|------------|-------|
| **Prominence** | Important things in places more likely seen: interface docs, names, parameters of heavily used methods | 7551–7553 |
| **Repetition** | Key ideas appear over and over | 7554–7555 |
| **Centrality** | What matters most at the heart of the system, determining structure around it | 7555–7559 |

- **Centrality example:** device-driver interface in operating systems—hundreds or thousands of drivers depend on it. [verified from text, lines 7557–7559]
- **Converse heuristic:** if an idea is more likely seen, repeated, or structurally impactful, **it matters**. [verified from text, lines 7561–7563]
- **De-emphasis for unimportant things:** hide, avoid frequent encounter, avoid structural impact. [verified from text, lines 7565–7567]

### Mistakes (§21.4)

**Mistake 1 — too many things treated as important:**

- Unimportant things clutter design, add complexity, increase cognitive load. [verified from text, lines 7572–7574]
- Examples: method arguments **irrelevant to most callers**; **Java I/O interface** (page 26) forcing awareness of buffered vs unbuffered I/O when developers almost always want buffering and should not waste time requesting it explicitly. [verified from text, lines 7574–7579]
- **Shallow classes** often result from treating too many things as important. [verified from text, lines 7580–7581]

**Mistake 2 — failing to recognize importance:**

- Important information hidden or important functionality unavailable → developers continually recreate it; impedes productivity; leads to **unknown unknowns**. [verified from text, lines 7583–7587]

### Thinking more broadly (§21.5)

- Same focus applies to **technical writing:** identify few key concepts at start, structure remainder around them; tie details back to overall concepts. [verified from text, lines 7591–7596]
- **Life philosophy extension:** identify few things that matter most personally; spend energy there; avoid frittering time on unimportant or unrewarding activities. `[contested in chapter]` — normative life advice beyond software scope; pedagogically illustrative but not empirically grounded in chapter. [verified from text, lines 7598–7601]
- **"Good taste"** = ability to distinguish important from unimportant; essential part of being a good software designer. [verified from text, lines 7603–7605]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 7467–7606 (inclusive) |
| **Chapter boundary** | Starts `Chapter 21` (L7467); ends before `Chapter 22` (L7607) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; adjacent Ch. 22 not read |
| **Cross-chapter refs cited (not re-ingested)** | §6.2 text storage; §20.4 performance-critical path; page 26 Java I/O |
| **Figures** | None in this chapter span |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. State the chapter's organizing principle—separate, emphasize, and hide—and relate it to abstractions, naming, and performance from earlier chapters.
2. Apply **leverage** and **invariants** as heuristics for deciding what matters in an interface or module design.
3. Use the **hypothesis-commit-evaluate** loop when importance is ambiguous, extracting clues from both successes and failures.
4. List tactics to **minimize what matters** (defaults, hiding, localized exception handling, auto-derived configuration).
5. Distinguish **prominence, repetition, and centrality** as emphasis tools and apply the converse diagnostic (visibility/structure ⇒ importance).
6. Diagnose the two mistake classes: over-importance (clutter, shallow classes) vs under-importance (hidden capability, unknown unknowns).
7. Transfer the framing to technical writing structure and recognize "good taste" as prioritization judgment, not aesthetics alone.

### worked_examples_present

**N** — No new in-chapter walkthrough or figure. The chapter is **conceptual synthesis** with **callbacks** to prior material:

| Referenced example | Source in book | Role in Ch. 21 |
|--------------------|----------------|----------------|
| Text insert/delete vs `backspace` | §6.2 | Leverage / general vs specialized API |
| Performance-critical path design | §20.4 | External constraint + structural emphasis |
| Java buffered vs unbuffered I/O | p. 26 | Over-emphasis mistake |
| OS device-driver interface | §21.3 (brief) | Centrality |
| Variable naming word-list procedure | §21.1 | "Design it twice" micro-procedure |

Operators should pair this chapter with ingests for §6.2, Ch. 20, and early Java I/O discussion for full worked context.

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - **Leverage audit:** For one public API, list specialized methods vs one general operation; score leverage and propose consolidation.
  - **Matter map:** Draw prominence/repetition/centrality for a subsystem (e.g., auth middleware); mark what should be de-emphasized.
  - **Hypothesis sprint:** Pick an ambiguous design choice; write a one-sentence "what matters" hypothesis; implement minimally; retrospective on clues.
  - **Mistake classification:** Find a shallow class or bloated method signature in a codebase; argue mistake type 1 vs 2 and remediation.
  - **Writing transfer:** Outline a design doc with 3 key concepts upfront; tie each detail section back—evaluate readability vs a detail-first draft.
  - **Defaults lab:** Reduce constructor parameters on a config object using sensible defaults; count call-site simplification vs hidden surprise risk.

## Operator hooks

### 1. Foundation layer

Chapter 21 is the **meta-heuristic capstone** immediately before the book's Conclusion (Ch. 22). It does not introduce new tactical design patterns; it **names and unifies** the prioritization logic implicit across the text—abstraction boundaries (Ch. 4+), information hiding, deep modules (Ch. 7), naming, performance critical paths (Ch. 20). Position in **w1_foundation** as the **"triage and taste"** chapter: what to make obvious vs invisible.

Bridges to:

- **Philosophy PSD2E Ch. 2–3** — complexity symptoms/causes; Ch. 21 explains *why* clutter accumulates when too much "matters."
- **Philosophy PSD2E Ch. 6** — text-storage leverage example is the chapter's strongest concrete anchor; cite Ch. 21 for *decision rationale*, Ch. 6 for *interface design*.
- **Philosophy PSD2E Ch. 20** — performance as externally imposed "what matters"; Ch. 21 generalizes to all design dimensions.
- **Clean Code / APOSD-adjacent craft texts** — naming and API surface discipline; Ousterhout frames as **importance allocation**, not style rules.
- **AI Engineering 2025 / agent orchestration** — tool schemas, system prompts, and middleware stacks suffer both mistake types: over-exposed config knobs (mistake 1) vs hidden capabilities developers reinvent (mistake 2). Chapter is pattern-portable, not LLM-specific.

**Prerequisite established:** familiarity with modules, interfaces, and at least one prior "deep vs shallow" or performance chapter so callbacks land.

### 2. MDCalc alignment

**[peripheral]**

No clinical AI, regulated deployment, trace/eval observability, or HIPAA/FDA content. Portable patterns for health-tech engineering:

- **API surface for clinical calculators** — expose what clinicians need (inputs, outputs, unit semantics); hide buffering, caching, and transport details (Java I/O analogy).
- **Agent tool design** — few high-leverage tools with general parameters beat many single-purpose tools; minimizes what matters to integrators.
- **Documentation** — Ch. 21's technical-writing parallel supports operator runbooks structured around few key concepts (dosing logic, contraindication checks) with details tied back.

No MDCalc production-stack claims. Do not cite this chapter as authority on clinical validation or monitoring requirements.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **Philosophy PSD2E Ch. 4, Ch. 7** | High (internal) | Abstraction depth and shallow-class diagnosis—Ch. 21 states the *why*; earlier chapters show *how* |
| **Philosophy PSD2E Ch. 6** | Medium (internal) | Text API leverage example owned by Ch. 6; Ch. 21 cites for heuristic only |
| **Philosophy PSD2E Ch. 20** | Medium (internal) | Performance-as-constraint example; dedup measurement tactics to Ch. 20 |
| **Philosophy PSD2E Ch. 2** | Medium (internal) | Cognitive load and unknown unknowns—Ch. 21 mistake taxonomy connects |
| **Clean Code (Martin)** | Low–medium | Naming emphasis overlaps; Ousterhout is systems/module-scale, not line-level style |
| **The Pragmatic Programmer** | Low | "Good taste" and tradeoff thinking; different example set |

**Dedup guidance:** Treat Ch. 21 as **canonical importance-allocation framing** for SYNTHESIS; link to Ch. 6/20 for worked examples rather than duplicating walkthroughs. Use Ch. 21 when teaching *prioritization mistakes* and *emphasis mechanics*.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Weak in-chapter** — relies on prior-chapter callbacks; strong as integrator if paired |
| Exercise hooks | **Weak in text** — conceptual drills inferable from heuristics |
| Chapter boundary quality | **Clean** — self-contained §21.1–21.5; short, cohesive |
| Ingest suitability | **High** — capstone vocabulary ("leverage," "good taste," mistake taxonomy) useful for cross-corpus tagging; few contested universals |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e published July 2021; meta-design heuristics age slowly; Java I/O example remains illustrative |
| **Author authority** | **PASS** | John Ousterhout, Stanford; textbook from Yaknyam Press; synthesizes own prior chapters |
| **Primary-source citation density** | **PASS (low density flagged)** | No bibliography; heuristics and examples from author's design experience and earlier book sections |
| **Contested claims flagged** | **PASS** | "Good taste" and life-philosophy extension are normative, not empirically tested; leverage heuristic stated without counterexamples where specialization wins |
| **Worked examples (procedural/conceptual)** | **PASS (by reference)** | Procedural depth lives in §6.2, §20.4, p. 26; this chapter is appropriately conceptual for a synthesis penultimate |

**Overall TEXTBOOK-Q1:** **PASS** — suitable foundation-track ingest as **prioritization meta-chapter**; operator should bundle with Ch. 6 and Ch. 20 ingests for example-backed teaching.

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C21-001 | Separate what matters from what doesn't; structure around what matters, hide the rest | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | intro |
| PSD2E-C21-002 | Decide importance via leverage and invariants | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.1 |
| PSD2E-C21-003 | General-purpose text range API beats specialized backspace for leverage | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.1 |
| PSD2E-C21-004 | Hypothesize what matters, build, learn from success or failure | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.1 |
| PSD2E-C21-005 | Minimize what matters: defaults, hiding, fewer impact sites, auto config | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.2 |
| PSD2E-C21-006 | Emphasize via prominence, repetition, centrality; de-emphasize the converse | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.3 |
| PSD2E-C21-007 | Mistake: too much matters → clutter, shallow classes, Java I/O buffering | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.4 |
| PSD2E-C21-008 | Mistake: too little recognized → hidden info, unavailable functionality, unknown unknowns | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.4 |
| PSD2E-C21-009 | Good taste = distinguishing important from unimportant | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch21_ingest.md | §21.5 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
