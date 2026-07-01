# Practical-usage card fan-out — subagent paste packet

Load when: phase-2 implementation-card pass after chapter ingests exist; one subagent per chapter (depth ≤2).

**Parent reads:** `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md`  
**Do not** monolith-read the corpus in the parent agent.

---

## Subagent payload (paste per chapter)

````text
SUB-AGENT: practical_usage card extract · {slug} · chapter {NN}

Read only:
- /Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md
- {corpus_root}/ingests/{slug}_ch{NN}_ingest.md
- Text slice cited in that ingest (lines or section from coverage_attestation only)

Write / merge:
- {corpus_root}/metadata/practical_cards/{topic_slug}.yaml
  (or literature/metadata/practical_cards/ per corpus layout)

Rules:
1. Extract named procedures from exercise_hooks, worked examples, or explicit step lists in source text.
2. ≥3 ordered steps when procedure_gap: false; **≤12** max; paraphrase from ingest — no invented steps.
3. source_anchor: prefer C-* claim_id; else "[read:body] {ingest_path} §{section}".
4. Efficacy-only → procedure_gap: true; steps: []; quality_level: procedure_gap.
5. cognitive_frame, observables, contraindications per schema.
6. consumer_wire: null unless session bet names consumer bridge path.
7. context_tags from session bet.
8. topic_slug: kebab-case from exercise_name (not pillar monikers).
9. quality_level: full | partial | procedure_gap on every card.
10. Merge: dedupe by exercise_name + source_anchor.

Forbidden:
- Send-ready scripts ("text her", opener banks)
- Steps not traceable to ingest or text slice
- Monolith-read of full book text
````

---

## Parent orchestrator checklist

1. Confirm phase 1 ingests exist for target chapters.
2. Dispatch one subagent per complex chapter (>3 hooks); inline extract for simple chapters.
3. Merge cards under metadata/practical_cards/ (or literature/metadata/practical_cards/).
4. **Only after cards exist:** set `practical_usage_required: true` in corpus manifest.
5. Track B: run sync_banter_r02_practical_cards_mirror.sh after writing aletheia SSOT cards.
6. Verify:
   bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh {verify_root}
   bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh {verify_root}

## Paths

| Role | Path |
|------|------|
| Schema SSOT | `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md` |
| Consumer bridge (example) | `/Users/dubs/Projects/scholia.skill/references/practical-usage-consumer-bridge.md` |
| Verify | `/Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh` |
