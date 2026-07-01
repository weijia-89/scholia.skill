# Chapter ingest — `philosophy_software_design_2e_2021` · Chapter 5

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
| **chapter_number** | 5 |
| **chapter_title** | Information Hiding (and Leakage) |
| **page_range** | Printed page numbers absent from text export; logical span §5.1–§5.10 |
| **parent_book_title** | A Philosophy of Software Design, 2nd Edition |

## Scope

Chapter 5 presents **information hiding** as the primary technique for building the **deep modules** introduced in Chapter 4. Following David Parnas's classic formulation, each module should encapsulate a few **design decisions** in its implementation while keeping them off the interface. Ousterhout catalogs hidden knowledge (data structures, algorithms, page sizes, workload assumptions) and explains how hiding reduces complexity by simplifying interfaces and localizing change. He distinguishes **private visibility** from true information hiding—getters/setters can leak representation—and treats **partial hiding** as worthwhile when rare features are segregated behind separate methods.

The chapter's counter-theme is **information leakage**: the same design decision reflected in multiple modules, including **back-door leakage** (shared knowledge without interface exposure). **Temporal decomposition**—structuring code by execution order—is named as a common leakage cause; the remedy is to organize by **knowledge needed**, not task sequence. A multi-section **HTTP server course-project** walkthrough illustrates leakage, shallow APIs, sensible defaults, and when merging classes increases depth. The chapter closes with intra-class hiding, limits on over-hiding, and a restatement of the deep-module link.

**Sections ingested:** §5.1 Information hiding · §5.2 Information leakage · §5.3 Temporal decomposition · §5.4 Example: HTTP server · §5.5 Example: too many classes · §5.6 Example: HTTP parameter handling · §5.7 Example: defaults in HTTP responses · §5.8 Information hiding within a class · §5.9 Taking it too far · §5.10 Conclusion · footnote 1 (Parnas 1972).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Information hiding (§5.1)

- **Information hiding** (Parnas¹) is "one of the most important techniques for achieving deep modules." Each module encapsulates a few pieces of knowledge representing **design decisions**; knowledge lives in implementation, not interface. [verified from text, lines 1583–1590]
- Examples of hideable knowledge: B-tree storage/access, logical-to-physical disk mapping, TCP implementation, multi-core thread scheduling, JSON parsing—including data structures, algorithms, low-level details (page size), and higher-level assumptions (most files are small). [verified from text, lines 1592–1611]
- Hiding reduces complexity **two ways**: (1) simpler, more abstract interfaces lower cognitive load for callers; (2) hidden information has no external dependencies, so related design changes touch **one module** (e.g., TCP congestion-control change affects implementation only, not higher-level send/receive code). [verified from text, lines 1613–1626]
- When designing modules, ask what can be hidden; more hiding enables simpler interfaces and **deeper** modules. [verified from text, lines 1628–1631]
- **`private` ≠ information hiding:** private fields help, but public getters/setters expose variable nature and usage as fully as public fields. [verified from text, lines 1633–1639]
- **Best hiding** is total irrelevance to users; **partial hiding** also helps—features needed by few users, accessed via separate methods invisible in common cases, create fewer dependencies than universally visible information. [verified from text, lines 1641–1649]

### Information leakage (§5.2)

- **Information leakage** is the opposite: a design decision reflected in **multiple modules**, creating coupled change surfaces. Information in an interface is leaked **by definition**; simpler interfaces correlate with better hiding. [verified from text, lines 1651–1659]
- **Back-door leakage:** two classes share knowledge (e.g., file format for read vs write) without interface exposure—"more pernicious than leakage through an interface, because it isn't obvious." [verified from text, lines 1660–1666]
- Leakage is "one of the most important red flags"; designers should develop sensitivity and ask how to confine knowledge to **one class**. Remedies: **merge** small closely tied classes, or **extract** a new encapsulating class—effective only if the new class offers a **simple abstraction**; otherwise back-door leakage becomes interface leakage with little gain. [verified from text, lines 1668–1681]

### Temporal decomposition (§5.3)

- **Temporal decomposition:** system structure mirrors **time order** of operations. Read-modify-write file app split into reader, modifier, writer duplicates file-format knowledge → leakage. Fix: combine read/write mechanisms in one class used in both phases. [verified from text, lines 1683–1701]
- **Red flag: Information Leakage** — same knowledge in multiple places (e.g., two classes understanding a file format). [verified from text, lines 1703–1707]
- Order matters in applications but **should not drive module structure** unless consistent with information hiding (stages using totally different information). Design by **knowledge per task**, not execution order. [verified from text, lines 1709–1714]

### HTTP server examples (§5.4–§5.7)

- **§5.4 Context:** HTTP request/response textual format over TCP; Figure 5.1 POST example (initial line, headers, body, URL parameters). Course assignment: classes for servers to receive requests and send responses. [verified from text, lines 1716–1752]
- **Red flag: Temporal Decomposition** — execution order in code structure; same knowledge at different times encoded in multiple places → leakage. [verified from text, lines 1734–1740]
- **§5.5 Too many shallow classes:** common student mistake. Separate "read request to string" and "parse string" classes = temporal decomposition; both need HTTP structure (e.g., `Content-Length` for body size) → duplicated parsing, two ordered calls for callers. **Merge** into one read-and-parse class: better hiding, simpler single-method interface, **deeper** module. General theme: hiding often improves by making a class **slightly larger**—consolidate capability-related code and raise interface level (one method for full computation). Caveat: extremes possible; Ch. 9 covers when to split. [verified from text, lines 1754–1795]
- **§5.6 Parameter handling — good choices:** hide header-vs-body parameter location (merge into one namespace); hide URL encoding (return decoded values like `"What a cute baby!"`). **Bad choice:** `getParams()` returning internal `Map` reference—shallow, exposes representation, couples callers to storage changes, forces two-step access, risks caller mutating internal state. **Better:** `getParameter(String)`, `getIntParameter(String)` (and typed variants)—deeper, hides representation and conversion mechanics; exceptions on missing/invalid params (omitted in excerpt). [verified from text, lines 1797–1865]
- **§5.7 Response defaults:** mistake = requiring explicit HTTP version on response when version must match request already passed at send time → leakage risk and caller burden. Library should default version and **Date** header. Defaults embody **common-case simplicity** and **partial information hiding**; override via special methods when rare. Classes should "do the right thing" without being asked (negative contrast: Java I/O buffering on p. 26—should be automatic). **Red flag: Overexposure** — API for common features forces learning rarely used features. [verified from text, lines 1867–1903]

### Intra-class hiding and limits (§5.8–§5.9)

- **§5.8:** Hiding applies inside classes too—private methods should encapsulate knowledge; **minimize places each instance variable is used** to reduce intra-class dependencies. [verified from text, lines 1905–1916]
- **§5.9 Taking it too far:** do not hide information **needed outside** the module (e.g., performance-tuning configuration parameters for different callers). Goal: minimize external information needs; auto-configuration beats exposed knobs when possible—but required external knowledge must be **exposed**. [verified from text, lines 1918–1931]

### Conclusion (§5.10)

- Information hiding and deep modules are **closely related**: much hidden information → more functionality, smaller interface → deeper; little hiding → shallow (little functionality or complex interface). [verified from text, lines 1933–1940]
- Decompose by **pieces of knowledge**, not runtime operation order (avoids temporal decomposition, leakage, shallowness). [verified from text, lines 1942–1949]

### Footnote 1

- David Parnas, "On the Criteria to be Used in Decomposing Systems into Modules," *Communications of the ACM*, December 1972. [verified from text, lines 1953–1954]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/philosophy_software_design_2e_2021.txt` |
| **Lines read** | 1576–1955 (inclusive) |
| **Chapter boundary** | Starts `Chapter 5` (L1576); ends before Ch. 6 (L1956+) |
| **Wrong-file flag** | `false` — slug matches `philosophy_software_design_2e_2021` |
| **Sections deferred** | None within chapter; Ch. 4 prerequisite cited in opening; Ch. 9 split guidance forward-referenced only |
| **Figures** | Fig. 5.1 HTTP POST request described in text; image placeholder `[]` in export |
| **Amnesiac rule** | No claims drawn from training prior; ISBN/edition from L5–29 of same file |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Define information hiding per Parnas/Ousterhout and distinguish it from `private` access modifiers.
2. Explain how hiding simplifies interfaces and localizes design change.
3. Detect **information leakage** and **back-door leakage**; apply merge-or-extract remediation criteria.
4. Recognize **temporal decomposition** and redesign around shared knowledge rather than execution order.
5. Evaluate API methods (e.g., `getParams` vs `getParameter`) for representation exposure and depth.
6. Apply **defaults** and **partial hiding** to optimize the common case without blocking rare overrides.
7. Balance hiding against legitimate need to expose configuration or tuning parameters.

### worked_examples_present

**Y** — Sustained worked example thread plus supporting cases:

| Example | Section | Role |
|---------|---------|------|
| B-tree, TCP, JSON, etc. | §5.1 | Catalog of hideable mechanisms |
| Read-modify-write file app | §5.3 | Temporal decomposition anti-pattern |
| HTTP POST (Fig. 5.1) | §5.4 | Protocol context for course project |
| Read-then-parse HTTP classes | §5.5 | Leakage via shallow split; merge remedy |
| Parameter merge + URL decode | §5.6 | Good hiding choices |
| `getParams()` vs typed getters | §5.6 | Shallow vs deep parameter API |
| Response version/Date defaults | §5.7 | Defaults as partial hiding |
| Java I/O buffering (p. 26) | §5.7 | Negative default example |
| Private methods / field usage | §5.8 | Intra-class hiding |
| Exposed tuning parameters | §5.9 | When not to hide |

### exercise_hooks

- No end-of-chapter problem sets in source text.
- **Instructor / self-study hooks `[inferred]`:**
  - Audit an HTTP or REST handler library: map knowledge duplicated across classes; propose merge or extract refactor.
  - Red-team a codebase for temporal decomposition (pipeline stages mirroring runtime order).
  - Refactor a `getAllX()` returning internal collection to deep per-item accessors; document migration cost.
  - Design defaults for an LLM tool schema (model name, timeout, retry) using partial-hiding principles; identify what must remain configurable.
  - Trace a Parnas 1972 module-boundary paper excerpt against one student HTTP design from the chapter.

## Operator hooks

### 1. Foundation layer

Chapter 5 operationalizes **deep modules** (Ch. 4) with **information hiding** as the central tactic and **leakage detection** as the primary diagnostic. It belongs in the **w1_foundation** wave immediately after Ch. 4 and before tactical chapters on naming, comments, and error handling. For agent/LLM pipeline design, the HTTP walkthrough is directly portable: hide encoding, transport, and parsing behind one deep "request" abstraction; avoid staged micro-classes that mirror ingest→parse→route order when they share format knowledge. Cross-ref **understanding_distributed_systems_2022** (cites Ousterhout on depth) and **ddia_2e_2026** (boundary design in distributed systems)—this chapter supplies the **leakage vocabulary** those texts assume. Forward pointer: Ch. 9 when **larger** merged classes should be split again.

### 2. MDCalc alignment

**[peripheral]** — No clinical AI, trace/eval, or regulated-deployment content. Portable patterns for MDCalc-style stacks: **deep tool interfaces** that hide HTTP/JSON/schema details from clinical logic; **defaults** for observability headers and API versions so application code cannot leak protocol coupling; **red-flag review** for temporal pipelines (retrieve → parse → score → render) that duplicate document-format knowledge across stages. No production or employer-stack claims.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **philosophy_software_design_2e_2021 Ch. 4** | High | Direct prerequisite; depth heuristic applied here via hiding |
| **understanding_distributed_systems_2022** | Medium | Shared Ousterhout lineage; cite Ch. 5 for leakage/temporal decomposition, not re-derive |
| **ddia_2e_2026** | Low–medium | Module boundaries in data systems; different domain, same hide-knowledge theme |
| **ai_engineering_2025** | Low | LLM pipeline staging risks temporal decomposition if format knowledge duplicates |
| **Parnas 1972 (primary)** | Source | Footnote only in chapter; full paper not ingested here |

**Dedup guidance:** Treat this ingest as the **canonical leakage + temporal decomposition** reference in SYNTHESIS; HTTP `getParams` anti-pattern is the anchor example for representation exposure.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — unified HTTP course-project thread with code snippets |
| Exercise hooks | **Weak in text** — no printed exercises; labs inferred from examples |
| Chapter boundary quality | **Clean** — §5.1–5.10 self-contained; Ch. 4/9 cross-refs only |
| Ingest suitability | **High** — actionable red flags, primary citation (Parnas), contested-adjacent API critique preserved |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2e July 2021; within ≤5-year window from session date (Jun 2025); design-principles canon remains current |
| **Author authority** | **PASS** | John Ousterhout, Stanford; Yaknyam Press textbook; author bio in source file (L8147+) |
| **Primary-source citation density** | **PASS (moderate)** | One foundational footnote (Parnas 1972); chapter is pedagogy-by-example rather than literature survey—appropriate for technique chapter |
| **Contested claims flagged** | **PASS** | "Larger classes deepen modules" vs Ch. 9 split guidance noted; Java I/O buffering critique flagged as negative example `[contested in chapter]` relative to platform defaults culture |
| **Worked examples (procedural/conceptual)** | **PASS** | Extended HTTP implementation critique with before/after interfaces |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| PSD2E-C05-001 | Information hiding encapsulates design decisions not visible in module interface | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.1 |
| PSD2E-C05-002 | Hiding reduces complexity via simpler interfaces and localized change | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.1 |
| PSD2E-C05-003 | Private fields with public getters/setters do not constitute full information hiding | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.1 |
| PSD2E-C05-004 | Back-door leakage: shared knowledge without interface exposure | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.2 |
| PSD2E-C05-005 | Temporal decomposition structures modules by execution order, causing leakage | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.3 |
| PSD2E-C05-006 | Merging read-and-parse HTTP classes yields deeper module than temporal split | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.5 |
| PSD2E-C05-007 | getParams() exposing internal Map is shallow; getParameter hides representation | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.6 |
| PSD2E-C05-008 | Defaults embody common-case simplicity and partial information hiding | compressed | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | §5.7 |
| PSD2E-C05-009 | Parnas 1972: criteria for decomposing systems into modules | quoted | A Philosophy of Software Design 2e | ISBN 978-1-7321022-1-7 | literature/cs-ai-textbook-canon/ingests/philosophy_software_design_2e_2021_ch05_ingest.md | footnote 1 |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · word cap ≤4500*
