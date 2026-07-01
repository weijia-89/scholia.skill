# ChatPRD ingest — practical cards · grokking_algorithms_2e_2024 · 10

Platform: **Opus 4.8** · Route: inline · hooks≈3
Project: `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline`

## Attach (one file only)

1. `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/attachments/grokking_algorithms_2e_2024_ch10_ATTACH.txt`

**Paste:** this prompt only. Do not upload schema or fan-out packet separately — they are referenced below and embedded in attach stable-context.

## Task

Extract **implementation cards** (`practical_usage`) from attached phase-1 ingest + text slice only.

Load-bearing rules:
- `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md`
- `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md`

Per named exercise / worked example / explicit step list in source:
- `exercise_name` — source-native hook name
- `steps` — ≥3 ordered steps when `procedure_gap: false`; paraphrase from attach; ≤12 max
- `cognitive_frame`, `observables`, `contraindications`
- `source_anchor` — prefer C-* from ingest; else `[read:body] grokking_algorithms_2e_2024_ch10_ingest.md §{section}`
- `context_tags` — include `cs-ai-foundation`, `practical-card`, plus wave tags
- `procedure_gap: true` + `steps: []` when efficacy cited but no protocol in corpus

**σ−:** no send-ready scripts; no invented steps; no pillar monikers as topic_slug.

## Output

Save YAML (one file per topic_slug; if multiple exercises, one file per topic with `cards:` list):

`/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/chatprd_returns/grokking_algorithms_2e_2024_ch10_cards.yaml`

```yaml
topic_slug: kebab-case-from-exercise-name
claim_ids: []
wire_status: pending
generated: YYYY-MM-DD
source_ingests:
  - ingests/grokking_algorithms_2e_2024_ch10_ingest.md
cards:
  - exercise_name: ...
    steps: [...]
    cognitive_frame: ...
    observables: [...]
    contraindications: [...]
    source_anchor: ...
    consumer_wire: null
    context_tags: [cs-ai-foundation, practical-card]
    procedure_gap: false
```

If zero procedural hooks: emit one gap row or empty `cards: []` with comment in save path — do not fabricate steps.

## Next steps (operator)

1. Copy or merge saved YAML into `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/practical_cards/{topic_slug}.yaml` (dedupe by exercise_name + source_anchor).
2. Run verify:
   `bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon`
3. After all waves PASS → `kickoff wire` for local-rag consumer.

**Iron law:** ChatPRD extracts only — Cursor merges + verify; no RAG re-extract.
