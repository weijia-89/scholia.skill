# Output mode: study-guide — scholia prep → palamedes handoff

**Owner:** scholia prepares corpus; **palamedes** renders via `study-guide-site.md`. Scholia does **not** embed HTML templates (route-don't-duplicate).

## When to use

Operator session bet includes: "study guide", "exam prep", "cram program", "certification site", "memory palace", "pedagogy appendix", or textbook-heavy corpus with daily cadence.

## Scholia prep (before handoff)

1. Run paper/chapter fan-out per routing tree (≥3 papers or ≥5 PDFs → mandatory fan-out).
2. Produce `literature/index/LITERATURE_INDEX.md` (or `literature/ingests/LITERATURE_INDEX.md`) with operator-question roles.
3. Produce `literature/ingests/SYNTHESIS.md` — load-bearing claims trace to ingests via `references/provenance.md`.
4. Run C-DG004: `bash scripts/check_cross_stage_consistency.sh <child-or-staging-dir>`.
5. Run `bash scripts/verify_scholia.sh` on staging corpus layout.

## Handoff payload schema

Emit this block to operator or paste into a **fresh palamedes chat**:

```yaml
handoff: scholia → palamedes/study-guide-site
output_mode: study-guide
stakes: L2-L4  # exam/cert → L3+

paths:  # relative to corpus root unless operator supplies absolute
  index_path: literature/index/LITERATURE_INDEX.md
  synthesis_path: literature/ingests/SYNTHESIS.md
  provenance_path: references/provenance.md  # optional if child skill not yet generated
  ingests_glob: literature/ingests/*_ingest.md

operator_questions:
  - role: string       # e.g. "exam domain", "weak area", "must-memorize"
    question: string   # verbatim operator question from session bet

session_bet:
  subject: string      # e.g. "ISC2 CC", "bar exam torts"
  cadence_days: integer  # study program length
  pedagogy: full|partial|skip  # full = memory palace + Appendix D for exam sites

constraints:
  amnesiac: true       # palamedes must not use training priors for load-bearing claims
  cite_ingests: true   # every load-bearing claim traces to ingest path or DOI
```

## Palamedes invocation

Load palamedes with stakes from session bet. Trigger: "build me a study guide" + attach handoff payload.

**Consumer spec:** `/Users/dubs/Projects/palamedes/skill/references/study-guide-site.md`

Palamedes owns: HTML site, pedagogy appendix, Anki optional, render scripts. Scholia does **not** patch palamedes templates.

## Verify before ship

| Check | Owner |
|-------|-------|
| Corpus fan-out complete | scholia verify |
| C-DG004 structure | check_cross_stage_consistency.sh |
| Semantic consistency | phylax mode=full |
| Study site renders | palamedes + operator spot-check |

## Failure modes

| Failure | Route |
|---------|-------|
| Missing SYNTHESIS or index | Block handoff; complete scholia pipeline |
| CONTRADICTED (phylax) | Block; operator resolves ingests |
| Sparse corpus | piranesi export-only (not in-Cursor web) |
