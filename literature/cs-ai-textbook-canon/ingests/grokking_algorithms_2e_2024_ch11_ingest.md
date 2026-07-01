# Chapter ingest — Grokking Algorithms 2e, Chapter 11: Dynamic Programming

**slug:** `grokking_algorithms_2e_2024`  
**ingest_id:** `grokking_algorithms_2e_2024_ch11_ingest`  
**corpus:** cs-ai-textbook-canon  
**text_anchor:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/grokking_algorithms_2e_2024.txt` lines 6144–6829

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Grokking Algorithms, 2nd Edition |
| **authors** | Aditya Y. Bhargava |
| **edition** | 2e (2024) |
| **ISBN_print** | 9781633438538 [verified from text, copyright page line 156] |
| **ISBN_electronic** | not listed separately in text export; Manning liveBook edition shares print ISBN per publisher practice — operator confirm from PDF colophon if needed |
| **publisher** | Manning |
| **parent_book_title** | Grokking Algorithms |
| **chapter_number** | 11 |
| **chapter_title** | Dynamic programming |
| **page_range** | not recoverable from pdftotext/Marker export (no page markers); TOC section spans knapsack revisited → recap; text lines 6144–6829 |

**ISBN note:** `corpus_manifest.yaml` lists `9781633438531`; copyright page in text export reads `9781633438538`. Ingest follows on-disk text; operator reconcile against physical PDF.

---

## Scope

Chapter 11 introduces **dynamic programming (DP)** as an optimization technique for problems with constraints. It revisits the **0/1 knapsack problem** from chapter 10 (brute force O(2^n) vs approximate greedy), then teaches the tabular DP method via a worked grid (guitar, stereo, laptop; later iPhone). A **Knapsack FAQ** section covers row order, column order, fractional items (greedy instead), dependent items (DP fails), multi-item combinations, and unfilled knapsacks.

The chapter maps knapsack to **travel itinerary optimization** (time budget), then generalizes DP design heuristics (grid axes, cell values, subproblems). Two string problems follow: **longest common substring (LCS)** for spell-check disambiguation (`hish` → `fish` vs `vista`) and **longest common subsequence (LCSq)** to distinguish `fosh` → `fish` vs `fort`. Real-world mentions: DNA similarity / MS research, `git diff`, Levenshtein distance. Three exercises (11.1–11.3) and a recap close the chapter.

**Out of scope (explicit in text):** fractional knapsack via DP; dependent subproblems (Paris/London example); general closed-form DP recipe — author stresses experimentation (“Feynman algorithm”).

---

## Key findings [verified from text]

### DP definition and applicability

- DP solves hard problems by solving **subproblems first** and building up (lines 6148–6151, 6189–6195).
- Use DP when optimizing under a **constraint** and when subproblems are **discrete and independent** (lines 6598–6603, 6814–6818).
- Every DP solution in this chapter involves a **grid**; cell values are what you optimize; each cell is a subproblem (lines 6206–6217, 6608–6615, 6820–6825).
- **No single formula** for all DP problems — framework + experimentation (lines 6677–6693, 6827–6828).

### 0/1 knapsack (tabular DP)

- Brute force: O(2^n) — “very, very slow” (lines 6174–6177).
- Grid: **rows = items**, **columns = knapsack capacities 1…W** (lines 6210–6213).
- Per cell: compare **value if you take current item** (item value + best value for remaining weight from prior rows) vs **value if you skip** (carry forward cell above) (lines 6361–6371).
- Walkthrough result for 4 lb, items guitar (1 lb, $1500), stereo (4 lb, $3000), laptop (3 lb, $2000): **$3500 = guitar + laptop** (lines 6356–6359).
- Adding iPhone (1 lb, $2000) raises 4 lb max to **$4000** (iPhone + 3 lb subproblem) (lines 6415–6422).
- **Column values never decrease** — always store current max estimate (lines 6427–6434).
- **Row order does not change final answer** (lines 6441–6451).
- **Fractional items:** DP cannot handle; use **greedy** by value-per-pound (lines 6472–6498).
- **Dependent items** (e.g., Paris travel cost shared across sights): DP cannot model — subproblems must not depend on each other (lines 6526–6549).
- Best solution may involve **nested sub-knapsacks** (combine two at a time recursively) (lines 6551–6557).
- Knapsack need not be **fully filled** (diamond example) (lines 6561–6571).

### String DP

**Longest common substring** (`hish` vs `fish` / `vista`):

```text
if word_a[i] == word_b[j]:
  cell[i][j] = cell[i-1][j-1] + 1
else:
  cell[i][j] = 0
```
(lines 6718–6721)

- Answer is **largest value in grid**, not necessarily last cell (lines 6731–6734).
- `hish`/`fish` share substring length **3** (`ish`); `hish`/`vista` share **2** → spell-check picks `fish` (lines 6736–6740).

**Longest common subsequence** (`fosh` vs `fish` / `fort`):

```text
if word_a[i] == word_b[j]:
  cell[i][j] = cell[i-1][j-1] + 1
else:
  cell[i][j] = max(cell[i-1][j], cell[i][j-1])
```
(lines 6781–6784)

- Subsequence allows non-contiguous matches — `fosh` closer to `fish` than substring metric alone (lines 6744–6758).

### Production / research mentions (secondary citations in chapter)

- Biologists: LCS on DNA; MS cure research cited without primary paper (lines 6793–6796).
- `git diff` uses DP (lines 6798–6800).
- Levenshtein distance uses DP; spell-check and copyright detection (lines 6802–6805).

---

## Coverage attestation

| Check | Result |
|-------|--------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/grokking_algorithms_2e_2024.txt` |
| **lines_read** | 6144–6829 (inclusive); next chapter heading `12 k-nearest neighbors` at line 6830 |
| **wrong_file_flag** | false |
| **figures** | Present as `[]` placeholders in export — grid walkthroughs described in prose only; operator may consult PDF for diagrams |
| **exercises_in_slice** | 11.1, 11.2, 11.3 present; solutions derived below where chapter gives answer or grid logic |
| **completeness** | Full chapter through Recap; no truncation before ch12 |

---

## Pedagogy

### learning_objectives

After this chapter, a reader should be able to:

1. Contrast brute-force knapsack O(2^n) with tabular DP and explain why sub-capacity columns are required.
2. Build and fill a 0/1 knapsack DP grid; apply the take-vs-skip recurrence using prior-row subproblem values.
3. State when DP **fails** (fractional items, dependent subproblems) and which alternative applies (greedy).
4. Recognize knapsack-isomorphism in scheduling (time budget vs weight capacity).
5. Design grid axes and cell semantics for a new DP problem.
6. Implement LCS substring and LCS subsequence recurrences; know answer location differs (max cell vs bottom-right).
7. Connect DP to diff, Levenshtein distance, and biological sequence alignment at a conceptual level.

### worked_examples_present

**Y** — Extensive worked examples:

- Full knapsack grid row-by-row (guitar → stereo → laptop) with dollar values (lines 6220–6359).
- iPhone row extension (lines 6380–6425).
- Travel itinerary grid setup and fill (lines 6500–6524).
- LCS substring grid + formula for `hish`/`fish` (lines 6634–6740).
- LCS subsequence grid + formula for `fish`/`fosh` (lines 6760–6788).
- FAQ walkthroughs: row reorder, necklace granularity, quinoa greedy, Paris dependency, diamond unfilled knapsack.

### exercise_hooks

| ID | Prompt (compressed) | Hook type | Suggested verification |
|----|---------------------|-----------|------------------------|
| **11.1** | Add mechanical keyboard (1 lb, $1000) to ch10 knapsack set — steal it? | extension / negative result | Fill 4th grid row; 4 lb max stays **$3500** (guitar+laptop); keyboard does not beat incumbent |
| **11.2** | 6 lb camping knapsack: Water(3,10), Book(1,3), Food(2,9), Jacket(2,5), Camera(1,6) | full DP practice | Optimal value **25**: Water + Food + Camera (or Water + Food + Book) |
| **11.3** | LCS **substring** grid for `blue` vs `clues` | string DP drill | Max substring length **3** (`lue`) |

**Scholia drill extensions (not in book):** implement bottom-up knapsack in Python; reproduce `git diff`-style LCS on two commit messages; compare greedy vs DP on fractional knapsack from FAQ.

---

## Section map (procedural index)

| Section | Text lines (approx) | Core idea |
|---------|---------------------|-----------|
| Chapter intro | 6146–6151 | DP = subproblems first |
| Knapsack revisited | 6153–6185 | O(2^n) brute force; need optimal |
| Dynamic programming | 6187–6371 | Grid construction + recurrence |
| Knapsack FAQ | 6375–6571 | Edge cases, limits of DP |
| Travel itinerary | 6500–6524 | Knapsack isomorphism |
| Dependent items | 6526–6549 | DP precondition violated |
| Multi-sub-knapsack / unfilled | 6551–6571 | Algorithm generality |
| Takeaways + tips | 6593–6615 | Grid heuristics |
| Longest common substring | 6617–6740 | 2D string grid, max in table |
| Longest common subsequence | 6742–6788 | Mismatch → max of left/top |
| Real-world uses | 6790–6805 | DNA, diff, Levenshtein |
| Exercises + recap | 6807–6828 | Consolidation |

---

## Algorithms and recurrences (reference card)

**0/1 knapsack** (columns w = 1…W, rows items i = 1…n):

- `K[i][w] = max( K[i-1][w], value_i + K[i-1][w - weight_i] )` if `weight_i ≤ w`, else `K[i-1][w]`.
- Chapter presents this via narrative grid, not this notation (lines 6361–6371).

**LCS substring:** match extends diagonal; mismatch → 0.

**LCS subsequence:** match extends diagonal; mismatch → `max(left, top)`.

**Contested / simplified claims (flagged, not smoothed):**

- “LCS being used to find a cure for multiple sclerosis” — author assertion without citation (line 6796); treat as motivational, not evidence.
- “Diff uses dynamic programming” — standard and correct at high level; chapter does not specify algorithm variant (Myers vs classic LCS).
- Feynman algorithm joke — pedagogy about trial-and-error, not a real algorithm (lines 6675–6687).

---

## Operator hooks

### 1. Foundation layer

Chapter 11 is the **canonical optimization capstone** for Track A wave-1 (`grokking_algorithms_2e_2024`). It formalizes techniques foreshadowed in ch10 (greedy knapsack approximation) and depends on ch2–3 (recursion), ch4–5 (divide/conquer intuition), and ch10 (greedy, approximation). It directly prepares **ch12 k-NN** and **ch13 ML overview** (distance/similarity, feature tradeoffs) and underpins later canon topics: sequence alignment in bio/clinical NLP, edit distance in eval harnesses, and DP-flavored parsing in compiler/LLM tooling. For **CLRS** on-demand reads, this chapter maps to introductory DP (not replacement for CLRS depth).

### 2. MDCalc alignment

**[none]** — No agents, trace/eval observability, clinical AI safety, or regulated deployment content. String similarity mentions (spell-check, copyright) are generic CS; DNA/MS reference is biology motivation only. Pattern-portable at most: edit-distance metrics could inform fuzzy clinical string matching, but chapter does not discuss healthcare.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **grokking ch10** | Same knapsack story; ch11 gives exact DP where ch10 gave greedy ~2 approximation |
| **CLRS 4e** | DP, LCS, knapsack treated rigorously with pseudocode and proofs — Grokking is intuitive grid-only |
| **AI Engineering / Hands-On LLMs** | No direct overlap; distant link via diff/Levenshtein for eval text comparison |
| **DDIA / distributed** | none |
| **Philosophy of Software Design** | none |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — multiple full grids |
| Exercise hooks | **Three** numbered exercises; 11.2 is best standalone lab |
| Chapter boundary | **Clean** — ends at recap; ch12 starts k-NN at line 6830 |
| Diagram dependency | **Medium** — grids are central; text export loses figures (`[]`) |
| Procedural skill yield | **High** for knapsack + LCS templates |

---

## TEXTBOOK-Q1 quality gate

| Criterion | Pass/Fail | Notes |
|-----------|-----------|-------|
| **Edition currency** | **PASS** | 2e 2024; ≤5 years; foundational algorithms text |
| **Author authority** | **PASS** | Manning textbook tier; foreword Daniel Zingaro; not blog content |
| **Primary-source citation density** | **FAIL (low)** | Chapter cites no papers, RFCs, or textbooks for DP origin; real-world bullets (DNA, MS, diff, Levenshtein) are assertive without references |
| **Contested claims flagged** | **PASS** | MS cure, diff internals, ISBN mismatch flagged in this ingest |
| **Worked examples (procedural chapter)** | **PASS** | Multiple full grid walkthroughs + pseudocode for both string problems |

**TEXTBOOK-Q1 overall:** **CONDITIONAL PASS** — pedagogically strong for procedural DP introduction; weak on primary citations. Suitable as **intuition layer** in reference-library; pair with CLRS or similar for proofs and citation-backed treatment.

---

## Provenance rows (sample)

| claim-id | claim | relation | source | anchor |
|----------|-------|----------|--------|--------|
| GA2E11-C01 | 0/1 knapsack DP max for 4 lb guitar/stereo/laptop is $3500 | quoted | Grokking Algorithms 2e ch11 | text L6356–6359 |
| GA2E11-C02 | Brute-force knapsack is O(2^n) | quoted | Grokking Algorithms 2e ch11 | text L6174–6177 |
| GA2E11-C03 | DP cannot handle fractional knapsack; use greedy | quoted | Grokking Algorithms 2e ch11 | text L6478–6485 |
| GA2E11-C04 | LCS substring mismatch cell = 0 | quoted | Grokking Algorithms 2e ch11 | text L6718–6721 |
| GA2E11-C05 | LCS subsequence mismatch cell = max(left, top) | quoted | Grokking Algorithms 2e ch11 | text L6781–6784 |
| GA2E11-C06 | LCS used in MS cure research | compressed | Grokking Algorithms 2e ch11 | text L6793–6796; **uncited — low confidence** |

---

## Paths

| Role | Path |
|------|------|
| Ingest | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/grokking_algorithms_2e_2024_ch11_ingest.md` |
| Text export | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/grokking_algorithms_2e_2024.txt` |
| PDF | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/grokking_algorithms_2e_2024.pdf` |
| Manifest | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/corpus_manifest.yaml` |
| Chapter schema | `/Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md` |
