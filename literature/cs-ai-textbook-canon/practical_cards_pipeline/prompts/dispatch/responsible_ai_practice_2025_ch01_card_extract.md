# SUB-AGENT: practical_usage card extract · responsible_ai_practice_2025 · 01

**Route:** fan-out · hooks≈4

Read only:
- /Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md
- /Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md
- /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch01_ingest.md
- Text slice: /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/attachments/responsible_ai_practice_2025_ch01_SLICE.txt

Write / merge:
- /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/practical_cards/{topic_slug}.yaml

Rules (from fan-out packet):
1. ≥3 steps when procedure_gap: false; ≤12 max; no invented steps.
2. source_anchor: prefer C-*; else "[read:body] responsible_ai_practice_2025_ch01_ingest.md §{section}".
3. Efficacy-only → procedure_gap: true; steps: []; quality_level: procedure_gap.
4. context_tags: cs-ai-foundation, practical-card (+ session tags from wave).
5. topic_slug: kebab-case from exercise_name — not pillar monikers.
6. Merge/dedupe by exercise_name + source_anchor.

Forbidden: send-ready scripts; monolith-read; steps not in ingest/slice.
