# Provenance template (CLAIMS ledger)

Use in generated child skills as `references/provenance.md`.

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| C-001 | … | quoted\|compressed\|inferred | … | … | literature/ingests/foo.md | §3.2 |

**Rules:**

- Paths relative to skill root only — no `/Users/` (SF-05)
- Preprints: tag `[preprint]` in claim column
- `[CONTRADICTION]` between ingests → block synthesis; route to operator
- Load-bearing rows require DOI/ID or explicit epistemic tag — not path-only (SF-06)

**Relation column (TROVE / C-DG005):** `quoted` (≥5 consecutive source words) · `compressed` (multi-claim condense) · `inferred` (tag in claim too) · contradicted → block + operator route
