# cs-ai-textbook-canon — phase 2 practical cards fan-out + RAG wire kickoff

META: operator paste packet · scholia phase 2 + local-rag wire · corpus=cs-ai-textbook-canon · **WAIT FOR KICKOFF**  
Save path: `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md`

**Subagent payload (per chapter):** `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md`  
**Schema:** `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md`  
**Consumer:** `/Users/dubs/Projects/local-rag-linux-setup` (RAG LLM machine + operator study) — see `/Users/dubs/Projects/scholia.skill/references/practical-usage-consumer-bridge.md`

---

## Operator gates (read first)

| Phrase | Starts |
|--------|--------|
| **`kickoff phase 2`** | Card fan-out (scholia subagents) |
| **`kickoff wire`** or **`kickoff consumer wire`** | RAG wire (local-rag-linux-setup) — only after scholia verify PASS |

Until **`kickoff phase 2`**: plan only, no subagents, no YAML, no manifest flip.  
After phase 2 verify: **stop** unless operator also said **`kickoff wire`** or **`kickoff consumer wire`** (same message or follow-up).

---

## Kickoff (paste from here into a new Cursor chat)

````text
You are the parent orchestrator for **cs-ai-textbook-canon phase 2** — scholia practical cards + local RAG wire.

Consumer (only): local RAG LLM machine + operator learning — NOT aletheia.
- RAG project: /Users/dubs/Projects/local-rag-linux-setup
- Corpus source: /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon
- Cards output: /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/practical_cards/{topic_slug}.yaml
- RAG sync dest: /Users/dubs/Projects/local-rag-linux-setup/corpus/cs-ai-foundation/scholia/practical_cards/
- RAG chunks: /Users/dubs/Projects/local-rag-linux-setup/data/rag-chunks/cs-ai-foundation.jsonl

## IRON LAW — wait for operator

STOP after your plan. Do NOT spawn subagents, flip manifest flags, write card YAML, or patch local-rag until the operator sends the kickoff phrase(s) above.

## Load before acting (read in order)

1. /Users/dubs/Projects/scholia.skill/SKILL.md (steps 8–10)
2. /Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md
3. /Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md
4. /Users/dubs/Projects/scholia.skill/references/practical-usage-consumer-bridge.md
5. /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/corpus_manifest.yaml
6. /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/index/LITERATURE_INDEX.md
7. /Users/dubs/Projects/local-rag-linux-setup/ingest/build_cs_ai_chunks.py
8. /Users/dubs/Projects/local-rag-linux-setup/scripts/sync_cs_ai_corpus.sh
9. /Users/dubs/Projects/local-rag-linux-setup/scripts/check_cs_ai_rag.sh

## Session bet

| Field | Value |
|-------|-------|
| Phase 2A | Implementation cards (scholia fan-out) |
| Phase 2B | Wire cards into RAG chunks + Qdrant upsert |
| Corpus root | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon |
| Consumer | /Users/dubs/Projects/local-rag-linux-setup — Task 1 RAG + operator study |
| context_tags | cs-ai-foundation, distributed-systems, eval-harness, prompt-engineering, clinical-ai, practical-card |
| Pilot on disk | 4 hand cards — merge/dedupe, do not delete without operator OK |

## What to plan (before any kickoff)

**Phase 2A (cards)**
1. Count ingests with procedural content — skip pure index/bibliography.
2. Wave order (manifest w1→w4): slug · chapters · estimated topic_slugs.
3. Missing text slices.
4. Subagent count (one per procedural chapter; depth ≤2).

**Phase 2B (RAG wire)**
5. Does sync_cs_ai_corpus.sh copy metadata/practical_cards/ today? (likely no — note patch)
6. Does build_cs_ai_chunks.py index practical_cards YAML? (likely no — note patch)
7. Expected chunk shape for retrieval (one chunk per card exercise with steps embedded as text)
8. Post-wire smoke: gold-set or ad-hoc query that should hit a procedure step

Emit plan only. Wait for operator kickoff phrase(s).

---

## Phase 2A — after operator says kickoff phase 2

1. Dispatch one subagent per procedural chapter (payload: practical-usage-card-fanout.md or generated `practical_cards_pipeline/prompts/dispatch/*`)
2. Merge YAML under metadata/practical_cards/ — topic_slug kebab-case; dedupe by exercise_name + source_anchor
3. Verify scholia (must PASS before manifest flip or wire):
   bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon
   bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon
4. **Only after cards on disk and verify PASS:** set `practical_usage_required: true` in /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/corpus_manifest.yaml
5. Report card count + new topic_slugs. STOP unless operator said kickoff wire.

---

## Phase 2B — after operator says kickoff wire (and 2A verify PASS)

Work in /Users/dubs/Projects/local-rag-linux-setup. Scholia cards remain SSOT — do not re-extract steps in RAG repo.

### B1 — Sync practical_cards from scholia

Patch sync_cs_ai_corpus.sh if needed, then:

export CS_AI_CORPUS_SRC=/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon
bash /Users/dubs/Projects/local-rag-linux-setup/scripts/sync_cs_ai_corpus.sh

Confirm files under:
/Users/dubs/Projects/local-rag-linux-setup/corpus/cs-ai-foundation/scholia/practical_cards/*.yaml

### B2 — Chunk builder: index practical cards

Extend ingest/build_cs_ai_chunks.py:

- Add glob: scholia/practical_cards/*.yaml
- For each card file, emit one JSONL record per `cards[]` entry (skip procedure_gap: true with empty steps, or emit gap-only row tagged practical-card-gap)
- Record shape (minimum):
  - source_path: scholia/practical_cards/{topic_slug}.yaml
  - slug: topic_slug
  - section: exercise_name
  - text: exercise_name + numbered steps + cognitive_frame + source_anchor (plain text for embedding)
  - domain_tags: include practical-card + card context_tags + cs-ai-foundation
  - chunk_type: practical_card (new field, optional but recommended)

Do not embed send-ready scripts. Steps are procedure, not message text.

### B3 — Rebuild + validate

bash /Users/dubs/Projects/local-rag-linux-setup/scripts/build_cs_ai_chunks.sh --no-sync
bash /Users/dubs/Projects/local-rag-linux-setup/scripts/check_cs_ai_rag.sh --no-sync

Extend check_cs_ai_rag.sh assertions if needed:
- practical-card tag present when cards synced
- chunk count >= number of non-gap exercises

### B4 — Upsert (Machine A or Mac with Qdrant up)

bash /Users/dubs/Projects/local-rag-linux-setup/scripts/upsert_cs_ai.sh

Smoke query (example — pick a card you wired):

bash /Users/dubs/Projects/local-rag-linux-setup/scripts/rag_query.sh "What are the steps for sandwich prompt refocus?"

Operator confirms retrieved text includes ordered steps from scholia card, not invented prose.

### B5 — Flip wire_status on cards (optional)

In scholia card YAML, set wire_status: wired and consumer_wire: local-rag-linux-setup/ingest/build_cs_ai_chunks.py (or corpus path) after successful smoke.

---

## σ− (refuse)

- Monolith-read full textbooks in parent agent
- Invented procedures (use procedure_gap: true instead)
- Send-ready scripts in cards or RAG chunks
- Aletheia pillar_moniker / operator-self-module wiring (wrong consumer)
- Starting fan-out or wire before operator kickoff phrase
- Re-extracting steps in local-rag instead of reading scholia YAML
````

---

## Paths

| Role | Path |
|------|------|
| This kickoff | `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md` |
| Per-chapter subagent packet | `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md` |
| Scholia cards (source) | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/practical_cards/` |
| RAG sync target | `/Users/dubs/Projects/local-rag-linux-setup/corpus/cs-ai-foundation/scholia/practical_cards/` |
| Chunk builder | `/Users/dubs/Projects/local-rag-linux-setup/ingest/build_cs_ai_chunks.py` |
| Bundled JSONL | `/Users/dubs/Projects/local-rag-linux-setup/data/rag-chunks/cs-ai-foundation.jsonl` |
| Consumer bridge | `/Users/dubs/Projects/scholia.skill/references/practical-usage-consumer-bridge.md` |

## Invoke

1. New Cursor chat → paste kickoff fence above  
2. Agent emits plan (2A + 2B) → **you review**  
3. Reply **`kickoff phase 2`** → cards fan-out + scholia verify  
4. Reply **`kickoff wire`** → sync, chunk builder patch, rebuild, upsert, smoke query  
5. Or both in one message: **`kickoff phase 2`** then **`kickoff wire`** after verify PASS
