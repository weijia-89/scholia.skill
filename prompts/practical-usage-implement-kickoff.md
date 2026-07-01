# Scholia practical-usage ingest — implementation kickoff

META: operator paste packet · scholia phase 2 · S4 canon SSOT · **WAIT FOR KICKOFF**

**Architecture SSOT:** `/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/returns/scholia_practical_ingest_decision_canon_20260626.md`

**Subagent payload:** `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md`

---

## Operator gates

| Phrase | Starts | Writes? |
|--------|--------|---------|
| **`kickoff phase 2`** | Card extraction (inline or fan-out) | yes |
| **`kickoff verify`** | Re-run verify + acceptance checklist only | **no** |
| **`kickoff consumer wire`** | Consumer bridge (after scholia verify PASS) | consumer repo only |

Until **`kickoff phase 2`**: plan only — no subagents, no card YAML, no manifest flip.

---

## Corpus tracks

| Track | Ingest SSOT (`corpus_root`) | Card write path | Scholia verify path |
|-------|----------------------------|-----------------|---------------------|
| **A — cs-ai** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon` | same `/metadata/practical_cards/` | same |
| **B — banter R-02** | `/Users/dubs/Projects/aletheia.skill/research/scholia/banter-r02-corpus` | `…/literature/metadata/practical_cards/` | `/Users/dubs/Projects/scholia.skill/literature/banter-r02-corpus` (mirror) |
| **C — custom** | operator `{corpus_root}` | `{corpus_root}/metadata/practical_cards/` or `literature/metadata/practical_cards/` | same as write root |

**Track B post-write:** `bash /Users/dubs/Projects/scholia.skill/scripts/sync_banter_r02_practical_cards_mirror.sh` (aletheia SSOT → scholia mirror).

**Consumer wire (separate session):**
- A → `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md` Phase 2B
- B → `/Users/dubs/Projects/aletheia.skill/references/architecture/aletheia-scholia-consumer-bridge.md`
- C → `/Users/dubs/Projects/scholia.skill/references/practical-usage-consumer-bridge.md`

---

## Kickoff (paste into new Cursor chat)

````text
You are the parent orchestrator for scholia phase 2 practical-usage implementation.

Verdict (Piranesi S4): SHIP WITH REVISIONS — two-phase ingest is correct.
Scholia owns procedural INDEXING (YAML) + extract + verify. Palamedes owns HTML rendering. Consumers own consumer_wire.

## IRON LAW

STOP after your plan. Do NOT spawn subagents, write card YAML, flip manifest flags, or patch consumer repos until the operator sends an explicit kickoff phrase.

| Phrase | Action |
| kickoff phase 2 | extract / merge cards |
| kickoff verify | verify scripts + checklist ONLY — no writes |
| kickoff consumer wire | consumer bridge — only after scholia verify PASS |

## Load (read in order)

1. /Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/returns/scholia_practical_ingest_decision_canon_20260626.md
2. /Users/dubs/Projects/scholia.skill/SKILL.md (steps 8–10)
3. /Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md
4. /Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md
5. /Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md
6. Track B only: /Users/dubs/Projects/scholia.skill/literature/banter-r02-corpus/CONSUMER_MIRROR.md
7. {corpus_root}/metadata/corpus_manifest.yaml OR literature/metadata/corpus_manifest.yaml
8. {corpus_root}/index/LITERATURE_INDEX.md (if present)

## Session bet (operator fills)

| Field | Value |
| Track | A | B | C |
| corpus_root | absolute path to ingest SSOT |
| card_write_root | absolute path for practical_cards/ (may differ on track B) |
| verify_root | absolute path for verify_practical_cards.sh |
| consumer | absolute path or none |
| context_tags | domain tags from session bet |
| Goal | fan-out | expand cards | verify-only |

## Plan (before kickoff phase 2)

1. Inventory chapter ingests with exercise_hooks / worked examples / step lists.
2. Skip index/bibliography/front-matter chapters.
3. Per chapter: count hooks — ≤3 inline single-pass; >3 fan-out subagent (S4 P1).
4. Plan procedure_gap rows for efficacy-only sources.
5. List existing topic_slugs; plan merge/dedupe (exercise_name + source_anchor).
6. Wave batches ≤16 parallel subagents.
7. Preflight: bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh --self-test

Emit: chapter · hooks · route (inline|fan-out) · expected topic_slug(s).

WAIT for kickoff phase 2.

---

## Phase 2 — kickoff phase 2

| Rule | Requirement |
| Subagent input | chapter ingest + focused text slice only |
| steps | ≥3 when procedure_gap:false; ≤12 max |
| source_anchor | required (C-* or [read:body] …) |
| quality_level | full | partial | procedure_gap on every card when manifest flag set |
| efficacy-only | procedure_gap:true; steps:[]; quality_level:procedure_gap |
| topic_slug | kebab-case from exercise_name — not pillar monikers |
| consumer_wire | null unless operator names consumer path in session bet |
| forbidden | send scripts; invented steps; monolith multi-chapter read; palamedes HTML |

Execution:
1. ≤3 hooks: inline practical_usage in ingest OR write card YAML — no subagent.
2. >3 hooks: one subagent/chapter via practical-usage-card-fanout.md (depth ≤2).
3. Write to {card_write_root}/metadata/practical_cards/ or …/literature/metadata/practical_cards/.
4. Track B: sync mirror after writes (script above).
5. Set practical_usage_required:true only after cards exist on disk.
6. Zero cards after honest pass: procedure_gap_corpus:true — do not treat empty dir as success.

Verify (must PASS):

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh {verify_root}
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh {verify_root}
find {verify_root} -path '*/practical_cards/*.yaml' -print0 | xargs -0 grep -iE 'text her|text him|send this opener|copy-paste this' && echo FAIL || echo PASS
```

Acceptance (S4 §7):
- ≥3 card YAMLs with ≥3 steps each (track B: maintain ≥17)
- verify exit 0
- ≥1 procedure_gap:true row
- quality_level on every card when manifest flag set
- manifest flag only after cards on disk

Report: card count · topic_slugs · procedure_gap count · verify output. STOP unless kickoff consumer wire.

---

## kickoff verify only

Re-run verify commands and acceptance checklist. No YAML writes. No manifest changes. No subagents.

---

## kickoff consumer wire

Scholia cards are SSOT. Consumer session links only — no re-extraction. See track table above.

Out of scope: harness copy, send-ready coaching text, palamedes HTML.

Kill list: single-pass parity claim; SDK depth-cap removal; scholia HTML rendering; unmeasured token-cost quotes.

TRAILING REMINDER: Amnesiac corpus; provenance on every step; fan-out not monolith.
````

---

## Attach (minimum)

1. `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-implement-kickoff.md`
2. `/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/returns/scholia_practical_ingest_decision_canon_20260626.md`

Optional: track kickoff (cs-ai) or R-02 pillar canon (track B expand).

## Quick start

1. New chat → paste Kickoff block or attach files.
2. Declare track + paths.
3. Review plan → **`kickoff phase 2`**.
4. After verify PASS → **`kickoff consumer wire`** if needed.
