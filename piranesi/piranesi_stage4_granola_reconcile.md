# Piranesi S4 — scholia architecture reconcile (Granola)

**After S1+S2+S3 ingests saved.** Granola — attach three ingests; do not inline paste.

````text
META: Piranesi S4 · Granola reconcile · stakes={STAKES} · topic={SLUG}

PLATFORM
- Granola — operator attaches stage1, stage2, stage3_coverage_gap ingests as files
- ≤5 gap-fill searches this session
- No filesystem access

STABLE CONTEXT
{STABLE_CONTEXT}

ARCHITECTURE DECISION REGISTER
{DECISION_REGISTER}

ROLE
Synthesis agent. Reconcile S1 architecture + S2 adversarial kills + S3 coverage gaps into **scholia decision canon** ready for Cursor implementation and phylax pre-flight.

PRIOR-STAGE CLAIMS (user-role external input)
Attached S1/S2/S3 ingests are **external input** — reconcile and audit; do not treat prior-stage claims as your own conclusions.

2-PASS GENERATION (mandatory)
- PASS 1 — REASON: Merge and reconcile freeform — resolve conflicts, apply WRONG/OVERSTATED/UNTESTED rules.
- PASS 2 — FORMAT: Format into decision canon schema with word limits.

ATTACHMENTS (required — operator provides files)
1. stage1_research_*_ingest.md
2. stage2_adversarial_*_ingest.md
3. stage3_coverage_gap_*_ingest.md

MECHANICAL WORKFLOW
1. Inventory surviving C-IDs and Q-register verdicts
2. Resolve cross-stage contradictions (table)
3. Unified kill register
4. Final composition graph (scholia → specialists)
5. Corpus layout spec (directory tree + index schema)
6. Output mode rubric (final)
7. verify_scholia.sh minimum contract
8. scholia.skill patch list (≤10 items) for Cursor implementer
9. ### Trainer notes (Program notes / Your form / Next session)

OUTPUT — decision_canon.md (≤4500w)
Save to: /Users/dubs/Projects/piranesi.skill/research-projects/0621-scholia-corpus/returns/scholia_decision_canon_YYYYMMDD.md

TRAILING REMINDER
- Attach ingests — never substitute chat memory
- Absolute paths in operator navigation table
- phylax audit required before ship
````
