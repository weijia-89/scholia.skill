# wc-to-token approximation (gap #11)

META: Canon gap #11 · SF-03 line-count proxy · `[inferred]`

## Rule

`verify_scholia.sh` SF-03 counts **body lines**, not tokens. For rough budgeting when comparing prose to vendor compaction limits:

| Approximation | Value | Source |
|---------------|-------|--------|
| English prose | ~0.75 tokens per word | Industry heuristic; not vendor-specified |
| Inverse | ~1.33 words per token | Derived |

## Platform use

- **SF-12** enforces **4500 words** per ingest file (word count via `wc -w`).
- **Vendor 5k/25k** (K-03, C-DG001) refers to Claude skill body compaction — do not equate 500 lines ≈ 5k tokens without measurement.
- Child skills approaching SF-03 line cap: split templates to `references/` (C-DG008).

## Verification

No mechanical gate. phylax semantic review may flag load-bearing claims that assume exact token equivalence.

**Status:** OPEN research gap — acceptable for v0.2.1; document approximation only.
