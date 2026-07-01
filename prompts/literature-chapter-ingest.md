# Chapter ingest — scholia textbook extension

Load when: textbook chapter fan-out, chapter-ingest, TEXTBOOK-Q1 gate.

**Owner:** scholia (not paper fan-out — peer-reviewed papers use palamedes `references/literature-corpus-fanout.md`).

## Mandatory fields (chapter-ingest)

1. title, authors, edition
2. ISBN_print, ISBN_electronic
3. chapter_number, page_range, parent_book_title
4. scope, key_findings, coverage_attestation
5. pedagogy: learning_objectives, worked_examples_present (Y/N), exercise_hooks

## TEXTBOOK-Q1 quality gate

- Edition currency (prefer ≤5 years unless classic)
- Author authority (textbook tier, not blog)
- Primary-source citation density in chapter
- Contested claims flagged, not smoothed
- Worked examples present for procedural chapters

## Output cap

≤4500 words per `{slug}_chapter_ingest.md` in `literature/ingests/`.

## Optional — practical_usage (phase 2)

When `practical_usage_required: true` in `corpus_manifest.yaml`, or the session bet includes coach / teach / operationalize / procedural output mode, attach implementation rows per `references/practical-usage-schema.md`.

**Simple chapters (≤3 exercise hooks):** extract `practical_usage` inline during phase 1 — skip per-chapter card fan-out (Piranesi S4 P1). **Complex chapters (>3 hooks):** fan-out card pass (one subagent per chapter, depth ≤2) merges topic aggregates at `literature/metadata/practical_cards/{topic_slug}.yaml` or `metadata/practical_cards/{topic_slug}.yaml` (corpus layout). Subagent reads **chapter ingest + focused text slice only** — not full chapter re-read.

Skip phase 2 for pure reference-library synthesis when no operational consumer is declared.

Efficacy-only source rows → `procedure_gap: true`; do not invent steps.

`source_anchor`: use `C-*` claim_id when present in ingest; else `[read:body] {ingest_filename} §{section}` per `references/practical-usage-schema.md`.

## Forbidden

Monolith-read of full textbook in parent agent. One chapter per sub-agent.
