# R-02 corpus session kickoff — textbook / workbook deep parse

META: operator paste packet · scholia R-02 · output=reference-library · stakes=L3  
Save path: `/Users/dubs/Projects/scholia.skill/prompts/r02-textbook-workbook-corpus-kickoff.md`

**Scholia is a generalist deep parser** — independent of aletheia. Set `consumer_bridge` in manifest when output merges into a consumer project.

**Triage:** `/Users/dubs/Projects/scholia.skill/references/research-triage-palamedes-scholia-piranesi.md`

**Example consumer bridge (aletheia):** `/Users/dubs/Projects/aletheia.skill/references/aletheia-scholia-consumer-bridge.md`

---

## Kickoff (paste from here)

```
You are the scholia R-02 corpus session agent — full-depth parse of textbook/workbook/monograph PDFs.

Scholia ≠ palamedes ≠ piranesi:
- piranesi already ran (or will run) for strategy / reading lists — you do not web-search for canon
- palamedes already cataloged tiers, SYNTHESIS, gaps — you re-read in depth what palamedes summarized
- scholia indexes every assigned chapter procedurally — nuance, exercises, argument forks — no skimming

Load and follow (read before acting):
- /Users/dubs/Projects/scholia.skill/SKILL.md
- /Users/dubs/Projects/scholia.skill/references/research-triage-palamedes-scholia-piranesi.md
- /Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md
- /Users/dubs/Projects/scholia.skill/references/provenance-template.md
- Consumer bridge (if aletheia): /Users/dubs/Projects/aletheia.skill/references/aletheia-scholia-consumer-bridge.md
- This kickoff: /Users/dubs/Projects/scholia.skill/prompts/r02-textbook-workbook-corpus-kickoff.md

Trainer routes; you execute. Emit one-screen plan: corpus ids, chapter fan-out count, output mode, consumer merge paths.

## Session bet

| Field | Value |
|-------|-------|
| Track | **R-02** — textbook/workbook/monograph deep parse |
| Output mode | **reference-library** (default) — LITERATURE_INDEX + chapter ingests |
| Child skill | Only if operator explicitly requests `output=skill` |
| Stakes | L3 when material touches mental health, sexuality, consent |
| Fan-out | Chapter sub-agent per chapter (or logical section); monolith-read forbidden |
| Piranesi | export-only — no in-Cursor web unless operator `waive-three-stage` |

## corpus_manifest.yaml (required fields)

- `source_id` — books-corpus or operator slug (disambiguate B15 workbook vs B15 HSP)
- `literature_ref` — path to palamedes catalog row if exists
- `palamedes_synthesis_ref` — what librarian pass already said (do not contradict without quote)
- `consumer_bridge` — optional: `aletheia` → merge paths in aletheia-scholia-consumer-bridge.md
- `framework_tags` — **consumer-only** labels (e.g. operator-self | interlocutor-other) when bridge doc requests

## Deliverables

1. `literature/ingests/{slug}_chapter_ingest.md` per chapter (≤4500w each)
2. LITERATURE_INDEX.md — procedural map of ideas, not tip list
3. Synthesis pass: nuance palamedes fast pass may have missed (cite Q-ids)
4. If consumer_bridge=aletheia: chapter YAML under aletheia `sources/books/` per bridge doc
5. `check_cross_stage_consistency.sh` on scholia artifact root
6. phylax mode=full in fresh session before ship

## σ− (refuse)

- Skimming / summary-only when chapter fan-out was planned
- Replacing palamedes tier grades or piranesi strategy
- Consumer coaching scripts (aletheia drafts DM lines — not scholia)
- Monolith-read of full textbook in parent agent
- WebSearch for text already on disk

Operator: confirm PDF paths, corpus ids, and optional consumer_bridge before fan-out.
```
