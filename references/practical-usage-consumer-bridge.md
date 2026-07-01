# practical_usage — consumer bridge (scholia → downstream)

**Owner:** consumer project. Scholia owns extract + verify only.

## Scholia output

```
{corpus_root}/metadata/practical_cards/{topic_slug}.yaml
# or
{corpus_root}/literature/metadata/practical_cards/{topic_slug}.yaml
```

Card fields: `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md`

## Wiring contract

| Card field | Consumer action |
|------------|-----------------|
| `consumer_wire` | Optional path in consumer repo (often null until wired) |
| `wire_status` | Scholia ships `pending`; consumer sets `wired` after merge |
| `context_tags` | Consumer retrieval filters (e.g. `eval-harness`, `distributed-systems`) |
| `procedure_gap` | Consumer must not invent steps; surface gap honestly |

---

## Primary consumer: local RAG LLM machine (cs-ai-textbook-canon)

**Project:** `/Users/dubs/Projects/local-rag-linux-setup`  
**Use:** Task 1 RAG (`cs-ai-foundation` Qdrant collection) + operator study from retrieved procedures  
**Corpus source:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon`

### What is wired today

| Layer | Status |
|-------|--------|
| Chapter ingests → RAG chunks | **Wired** — `build_cs_ai_chunks.py` / bundled JSONL |
| Study guide → RAG chunks | **Wired** |
| Practical cards → RAG chunks | **Not wired yet** — cards exist on scholia disk only |

### Operator flow (after phase 2 fan-out)

1. Scholia writes/verifies cards under `metadata/practical_cards/`.
2. Sync scholia → local-rag: `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/sync_cs_ai_corpus.sh`
3. Rebuild chunks: `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/build_cs_ai_chunks.sh`
4. Upsert: `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/upsert_cs_ai.sh`

**Remaining consumer work:** extend `ingest/build_cs_ai_chunks.py` to index `metadata/practical_cards/*.yaml` as a distinct chunk type (procedure steps retrievable by `topic_slug` / `exercise_name`). Until then, operator can read YAML directly for study.

### Session bet tags

Use `context_tags` on cards: `cs-ai-foundation`, `distributed-systems`, `eval-harness`, `prompt-engineering`, `clinical-ai`.

---

## Reference consumer: aletheia R-02 (not cs-ai)

**Corpus:** `/Users/dubs/Projects/aletheia.skill/research/scholia/banter-r02-corpus/`  
**Status:** **Wired** 2026-06-26 — loader + verify pass; coaching runtime only.

Docs:

- `/Users/dubs/Projects/aletheia.skill/references/architecture/practical-cards-runtime.md`
- `/Users/dubs/Projects/aletheia.skill/references/architecture/claim-bridge.md` § R-02 practical wire table

Verify:

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /Users/dubs/Projects/aletheia.skill/research/scholia/banter-r02-corpus
python3 /Users/dubs/Projects/aletheia.skill/scripts/harness/test_load_practical_card.py -v
```

---

## Phase 2 kickoff (cs-ai)

**Wait for operator.** Paste:

`/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md`

| Phrase | Action |
|--------|--------|
| **`kickoff phase 2`** | Scholia card fan-out + verify |
| **`kickoff wire`** | Sync cards → chunk builder → Qdrant upsert + smoke query |

Full wire spec is in that kickoff (Phase 2B).

## σ−

Scholia refuses send-ready scripts in cards. RAG consumer must not treat steps as copy-paste message text.
