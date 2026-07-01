# Chapter ingest — Grokking Algorithms 2e, Chapter 10

**Corpus slug:** `cs-ai-textbook-canon`  
**Ingest slug:** `grokking_algorithms_2e_2024_ch10`  
**Generated:** 2026-06-25 (sub-agent chapter fan-out)

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Greedy algorithms |
| **authors** | Bhargava, Aditya |
| **edition** | 2nd Edition (2024) |
| **ISBN_print** | 9781633438538 [verified from text, line 156] — manifest lists 9781633438531; reconcile with physical copy |
| **ISBN_electronic** | not stated in chapter slice; liveBook URL referenced in front matter (lines 600–616) |
| **chapter_number** | 10 |
| **page_range** | unverified — text export lacks page markers; TOC places ch10 between ch9 (Dijkstra) and ch11 (dynamic programming) |
| **parent_book_title** | Grokking Algorithms, Second Edition |

**Publisher:** Manning (from corpus manifest)  
**Text anchor:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/grokking_algorithms_2e_2024.txt` lines 5740–6143

---

## scope

Introductory treatment of **greedy algorithms** as a problem-solving strategy: repeatedly choose the locally optimal move and hope for a global optimum. The chapter progresses through three canonical problems of increasing difficulty:

1. **Classroom scheduling (interval scheduling)** — greedy by earliest finish time; claimed optimal.
2. **0/1 knapsack** — greedy by highest value item; shown to fail; defers exact solution to chapter 11 (dynamic programming).
3. **Set covering** — exact solution via power set is exponential; framed as **NP-hard**; greedy approximation plus full Python walkthrough using **sets** (union, intersection, difference).

Secondary topics woven in: **approximation algorithms** (speed vs optimality tradeoff), big-O for brute force O(2^n) vs greedy O(n²), and a sidebar on Python `set` operations.

**Out of scope in this slice:** formal proofs of optimality or approximation ratios; fractional knapsack; weighted set cover; linear programming relaxations; references to primary CS theory literature (appendix B mentioned only).

---

## key_findings

All claims anchored to chapter text unless tagged `[inferred]`.

### Greedy strategy (definition)

> "A greedy algorithm is simple: at each step, pick the optimal move." … "at each step, you pick the locally optimal solution, and in the end, you're left with the globally optimal solution." (lines 5804–5808)

The chapter frames greed as **easy to write** and often **fast**, but explicitly warns it does not always yield global optima (lines 5811–5812, 5850–5851).

### Classroom scheduling — greedy succeeds

**Problem:** maximize non-overlapping classes in one room given start/end times.

**Algorithm:** (1) pick the class that ends soonest; (2) among remaining classes that start after that end, again pick the one that ends soonest; repeat (lines 5774–5779).

**Worked trace:** Art (ends 10:00) → Math (after Art) → Music (after Math); three classes selected (lines 5782–5798).

**Claim:** "this simple algorithm finds the optimal solution to this scheduling problem!" (lines 5808–5809)

`[CONTESTED — not smoothed]` The chapter asserts optimality without proof or the standard "sort by finish time" precondition stated as a formal lemma. The algorithm is correct for classic interval scheduling **if** classes are considered in finish-time order at each step; readers may confuse "pick any class ending soonest among feasible" with needing a global sort. CLRS and other texts supply proof; this chapter relies on intuition and diagrams.

### Knapsack — greedy fails

**Problem:** 35 lb capacity; maximize stolen value (lines 5818–5823).

**Greedy rule:** pick most expensive item that fits, repeat (lines 5829–5832).

**Counterexample:** stereo alone → $3,000; laptop + guitar → $3,500 (lines 5839–5847).

**Takeaway:** "sometimes perfect is the enemy of good" — greedy may be "good enough" when exact methods are costly (lines 5854–5857). Exact knapsack deferred: "In the next chapter, I'll explain how to calculate the correct solution." (lines 5852–5853) → chapter 11 dynamic programming.

### Set covering — NP-hard + approximation

**Problem:** minimize radio stations covering all 50 US states (example uses 8 states) (lines 5878–5890).

**Exact approach:** enumerate power set — 2^n subsets; "O(2^n) time" (lines 5894–5906). "There's no known algorithm that solves it fast enough!" (lines 5911–5912). Classified as **NP-hard**; "check out appendix B" (lines 6129–6131).

**Greedy approximation:** (1) pick station covering the most **not-yet-covered** states (overlap OK); (2) repeat until all covered (lines 5917–5924).

**Evaluation criteria for approximations:** speed and closeness to optimal (lines 5928–5932).

`[CONTESTED — not smoothed]` Chapter says greedy "comes pretty close" (line 5917) but gives **no approximation ratio** (classic greedy set cover is O(ln n)-approximate; H_n). Runtime stated: O(n²) in number of stations (lines 5936–5937).

### Python implementation (set cover)

Setup uses `set` for `states_needed`, dict of station→coverage sets, and `final_stations` (lines 5948–5986).

Core loop (lines 6105–6115):

```python
while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states_needed & states
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered
  states_needed -= states_covered
  final_stations.add(best_station)
```

Output example: `set(['ktwo', 'kthree', 'kone', 'kfive'])` — note multiple optimal station sets exist (lines 6119–6123).

**Set operations taught:** union `|`, intersection `&`, difference `-` with fruit/vegetable examples (lines 6038–6064).

### Recap bullets (lines 6135–6142)

- Greedy: local optimum → hoped global optimum
- NP-hard → use approximation algorithms
- Greedy approximations: easy to write, fast to run

---

## coverage_attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/grokking_algorithms_2e_2024.txt` |
| **Lines read** | 5740–6143 (inclusive) |
| **Chapter boundary** | Starts `10 Greedy algorithms` (5740); ends before `11 Dynamic programming` (6144) |
| **Wrong-file flag** | false |
| **Monolith read** | false — single chapter slice only |
| **Diagrams** | Text export shows `[]` placeholders; visual scheduling/knapsack/station maps not recoverable from text |
| **Primary-source citation density** | **Low** — no papers, no theorem citations; appendix B pointer only |

---

## pedagogy

### learning_objectives

After this chapter, a reader should be able to:

1. Define the greedy strategy (local optimum at each step).
2. Apply earliest-finish-time greedy to interval scheduling and trace a solution.
3. Recognize when greedy fails (0/1 knapsack counterexample).
4. Explain why exhaustive set cover is O(2^n) and impractical at scale.
5. Implement the greedy set-cover heuristic in Python using sets and `&` / `-` operations.
6. Distinguish exact algorithms from **approximation algorithms** on NP-hard problems.
7. Compare stated runtimes: O(2^n) exact vs O(n²) greedy for set cover.

### worked_examples_present

**Y** — Three narrative worked examples (classroom scheduling with time trace, knapsack value counterexample, radio stations with code listing). Set operations mini-tutorial with REPL-style snippets.

### exercise_hooks

| ID | Prompt (compressed) | Greedy hook | Optimal? (chapter expectation) |
|----|---------------------|-------------|-------------------------------|
| **10.1** | Truck packing: varied box sizes, maximize truck space usage | Student devises greedy (e.g., largest-first) | Student judges — likely **no** for bin packing (NP-hard) |
| **10.2** | Seven-day Europe trip; points per sight vs time cost | Student devises greedy (e.g., highest points/hour) | Student judges — likely **no** (knapsack-like) |

Both exercises mirror chapter pattern: invent greedy → ask if optimal. Useful for scholia drill cards linking to bin packing and knapsack variants.

**Forward link:** chapter 11 dynamic programming for exact knapsack (line 5852).

---

## Operator hooks

### 1. Foundation layer

Establishes **heuristic algorithm design** and **computational intractability** vocabulary for the rest of the Grokking Algorithms arc and the broader canon:

- **Greedy vs optimal** — prerequisite intuition before dynamic programming (ch11) and before recognizing when polynomial exact methods exist vs not.
- **NP-hard + approximation** — minimal exposure to "no fast exact algorithm known" and the engineering response (approximate fast). Foundation for later systems texts where optimality is traded for latency (scheduling, resource allocation) without formal proofs.
- **Set operations as algorithmic primitives** — reused anywhere coverage/union problems appear (distributed sets, feature flags, region coverage).

For **CLRS 4e** (optional canon): this chapter is a shallow intuitive layer; CLRS supplies proofs and tighter bounds.

### 2. MDCalc alignment

**[none]**

No agents, trace/eval observability, clinical AI safety, or regulated deployment content. Pattern-portable at most: "pick good-enough fast heuristic when exact optimization is exponential" applies generically to ops problems but is not discussed in those domains here.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **grokking_algorithms_2e_2024 ch11** | Direct continuation — exact knapsack via DP |
| **clrs_4e_2022** | Greedy algorithms chapter (proofs, activity selection, Huffman, matroids) — **deeper, redundant** if both ingested |
| **ai_engineering_2025 / hands_on_llms_2024** | No substantive overlap |
| **ddia_2e_2026 / understanding_distributed_systems_2022** | No overlap |
| **kaestner_ml_production_2025** | Tangential — resource scheduling in production may use heuristics; not covered here |

Unique value in canon: **most accessible** greedy + NP-hard + approximation narrative with runnable Python.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Y** — strong; scheduling trace, knapsack counterexample, full code |
| Exercise hooks | **Y** — 10.1, 10.2 plus implicit set-cover coding exercise |
| Chapter boundary quality | **Clean** — self-contained arc scheduling → knapsack fail → set cover + code; recap closes slice |

**Scholia extraction candidates:** flashcards on greedy definition; interval scheduling trace; knapsack counterexample numbers; set-cover loop invariant (`states_needed` shrinks); set ops `&` `|` `-`; NP-hard vs approximation decision tree.

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| **Edition currency** | **PASS** | 2e 2024; ≤5 years |
| **Author authority** | **PASS** | Manning textbook tier; pedagogical CS intro, not blog |
| **Primary-source citation density** | **FAIL (chapter-level)** | No research citations; appendix B only; claims about NP-hardness and optimality unsubstantiated in-chapter |
| **Contested claims flagged** | **PASS** | Scheduling optimality unproven here; set-cover approximation ratio unstated; knapsack failure shown honestly |
| **Worked examples (procedural)** | **PASS** | Multiple traces + executable Python |

**Gate summary:** **CONDITIONAL PASS** — suitable as intro/heuristic reference; pair with CLRS or theory appendix for proofs and approximation bounds. Do not treat approximation quality claims ("comes pretty close") as quantified without appendix B or external source.

---

## Provenance hooks (selected)

| claim-id | claim | relation | section-anchor |
|----------|-------|----------|----------------|
| C-GA10-001 | Greedy = locally optimal each step | quoted | §Greedy strategy |
| C-GA10-002 | Interval scheduling earliest-finish greedy optimal | compressed | §Classroom scheduling — `[CONTESTED]` |
| C-GA10-003 | 0/1 knapsack value-greedy yields $3000 vs $3500 optimal combo | quoted | §Knapsack |
| C-GA10-004 | Set cover exact O(2^n); NP-hard | quoted | §Set-covering |
| C-GA10-005 | Greedy set cover O(n²) | quoted | §Approximation algorithms |
| C-GA10-006 | Set ops `&` `\|` `-` semantics | quoted | §Sets sidebar |

**Ingest path (relative):** `literature/cs-ai-textbook-canon/ingests/grokking_algorithms_2e_2024_ch10_ingest.md`

---

## Cross-chapter links (within book)

| Direction | Link |
|-----------|------|
| Back | Chapter 9 Dijkstra — also greedy-like local choices (mentioned in TOC; not in slice) |
| Forward | Chapter 11 dynamic programming — exact knapsack (line 5852) |
| Appendix | Appendix B — NP-hard problems (lines 6130–6131) |

---

## Gaps for parent SYNTHESIS

1. **Approximation guarantee missing** for set-cover greedy — flag if canon needs operational SLAs on heuristic quality.
2. **Page range** absent from export — operator may annotate from PDF for citation cards.
3. **ISBN mismatch** manifest vs text — verify single canonical ISBN in index.
4. **Diagram-dependent steps** (`[]` placeholders) — scheduling and station maps need PDF figures for full self-study offline.
