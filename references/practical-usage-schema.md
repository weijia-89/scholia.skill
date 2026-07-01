# practical_usage — scholia ingest schema extension

**Owner:** scholia (all corpora)  
**Status:** v2 · 2026-06-26  
**Parent schema:** `prompts/literature-chapter-ingest.md` mandatory fields + `deep_read_v2` claim rows

## Purpose

Phase 1 ingest (`deep_read_v2`) condenses **claims and evidence**. Phase 2 extracts **implementation cards** when the session bet or corpus manifest requires operational content — named exercises, ordered steps, cognitive frames, observables — for any consumer skill (coaching, exam prep, procedural guides, reference libraries).

**Failure mode this fixes:** citing "ACT is effective for social anxiety" without extracting how the source says to run defusion, exposure, or values work.

## When to run phase 2

Set in `corpus_manifest.yaml`:

```yaml
practical_usage_required: true
```

Or declare in session bet: coach / teach / operationalize / procedural output mode.

Skip phase 2 when the consumer only needs bibliographic synthesis (pure reference-library index).

## Optional block (chapter ingest or card fan-out output)

Attach zero or more `practical_usage` rows per exercise hook extracted from a chapter ingest:

```yaml
practical_usage:
  - exercise_name: string       # source-native name, e.g. "Thank You Mind"
    steps: [string]             # ordered; paraphrase OK; no invented steps
    cognitive_frame: string     # operator-internal stance while doing it
    observables: [string]       # third-party-visible behavior
    contraindications: [string] # σ−, DEFER, clinical routing
    source_anchor: string       # claim_id or [read:body] section anchor
    consumer_wire: string       # optional path in consumer skill (relative)
    context_tags: [string]        # from session bet — domain-specific, not hardcoded
    procedure_gap: false        # true when source cites efficacy but prescribes no steps
    quality_level: full          # full | partial | procedure_gap
```

`quality_level` rules:
- **full** — ≥3 source-anchored steps extracted
- **partial** — named exercise or frame without full step list (source incomplete)
- **procedure_gap** — efficacy-only or meta-analysis; no protocol in corpus (must match `procedure_gap: true`)

## Field rules

| Field | Rule |
|-------|------|
| `exercise_name` | Source hook name or workbook exercise title; no invented branding |
| `steps` | ≥3 ordered steps when `procedure_gap: false`; **≤12** max; paraphrase from ingest or source text |
| `cognitive_frame` | Operator-internal stance; not interlocutor-facing script |
| `observables` | Third-party-visible behavior; mark observable vs inferred where relevant |
| `contraindications` | Consumer σ− gates when known; default scholia refusals (no invented clinical advice) |
| `source_anchor` | `C-*` claim_id when ingest has claim rows; else `[read:body] {ingest_path} §{section}` (see below) |
| `consumer_wire` | Optional; consumer skill documents its own bridge |
| `context_tags` | Session-defined (e.g. `clinical`, `distributed-systems`, `eval-harness`) |
| `procedure_gap` | Honest tag when meta-analysis / review row has no procedure in corpus |
| `quality_level` | `full` \| `partial` \| `procedure_gap`; required when manifest flag set — distinguishes honest gap from silent failure |

## source_anchor (until claim rows exist)

Textbook ingests without `deep_read_v2` claim_ids use section anchors:

```
[read:body] prompt_engineering_llms_2024_ch06_ingest.md §Sandwich / refocus
```

When claim rows land in ingest, prefer `C-{BOOK}_CH{NN}-{seq}` and list in card `claim_ids: []`.

## Iron laws

1. **Amnesiac corpus** — every step traces to ingested source or tagged epistemic row.
2. **No invented procedures** — efficacy without protocol → `procedure_gap: true`, not fabricated steps.
3. **No send-ready scripts** — unless source is an explicit quoted template and consumer σ− allows.
4. **Fan-out not monolith** — one subagent per chapter for card extraction; depth ≤2.
5. **Simple chapters (≤3 exercise hooks):** inline single-pass `practical_usage` in chapter ingest — skip card fan-out (Piranesi S4 P1).

## Phase-2 empty-result rollback

When manifest `practical_usage_required: true` but phase 2 yields zero cards after an honest pass:

1. Set manifest annotation `procedure_gap_corpus: true` (or per-chapter note in ingest).
2. Do **not** ship an empty `practical_cards/` directory as success.
3. Log extraction metadata (chapters attempted, hooks found, gaps tagged).

See `references/corpus-manifest-template.yaml`.

## Card file shape (topic aggregate)

```
literature/metadata/practical_cards/{topic_slug}.yaml
```

Corpus layouts without a `literature/` prefix may use `metadata/practical_cards/{topic_slug}.yaml` instead (e.g. `cs-ai-textbook-canon`). Verify script auto-detects both.

`topic_slug` = kebab-case from exercise name or index role (not pillar monikers).

```yaml
topic_slug: thank-you-mind
claim_ids: [C-B03_CH04-001]
wire_status: pending          # pending | wired (consumer updates)
generated: YYYY-MM-DD
source_ingests: [relative paths under literature/ingests/]
cards:
  - exercise_name: Thank You Mind
    steps: [...]
    cognitive_frame: ...
    source_anchor: C-B03_CH04-001
    consumer_wire: null
    procedure_gap: false
```

## Routing (SKILL.md)

After `deep_read_v2` claim extraction:

1. Check manifest `practical_usage_required` or session bet.
2. Fan-out implementation-card pass per chapter.
3. Merge into `literature/metadata/practical_cards/`.
4. Run `verify_practical_cards.sh` before ship.

## Verify gate

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh --self-test
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /path/to/corpus/root
```

Fails when: manifest requires cards but none exist; card has `<3` steps with `procedure_gap: false`; card has `>12` steps; step missing `source_anchor`; missing `quality_level` when manifest flag set; banned send-script patterns.

## References

- Strategy prompt: `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-ingest-strategy.md`
- **Implementation kickoff:** `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-implement-kickoff.md`  
**cs-ai deai-style pipeline:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/KICKOFF.md`
- Fan-out subagent packet: `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md`
- Consumer bridge: `/Users/dubs/Projects/scholia.skill/references/practical-usage-consumer-bridge.md`
- Piranesi architecture review: `/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/returns/scholia_practical_ingest_decision_canon_20260626.md`
