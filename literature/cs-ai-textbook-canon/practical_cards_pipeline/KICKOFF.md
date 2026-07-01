# Operator kickoff — cs-ai phase 2 practical cards

**Pattern:** deai-operator-corpus split path (Piranesi plan + Scholia orchestrator + trainer gates)  
**Review loop:** PASS 2026-06-28 (`run_practical_cards_review_loop.sh`)

---

## 1. New parent chat — paste orchestrator

| Attach | Path |
|--------|------|
| **Paste only** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/prompts/ORCHESTRATOR_cs_ai_practical_cards.md` |

**Trainer:** load `/Users/dubs/.cursor/skills/trainer/SKILL.md` first.

**Do not start fan-out until you say:** `kickoff phase 2`

---

## 2. Operator gates

| Phrase | Starts | Writes? |
|--------|--------|---------|
| **`kickoff phase 2`** | Next pending wave batch (≤16 subagents) | yes — card YAML |
| **`kickoff verify`** | Re-run verify + acceptance only | no |
| **`kickoff wire`** | RAG consumer wire (local-rag-linux-setup) | consumer repo only |

**Manifest rule (fixed):** `practical_usage_required: true` only **after** cards on disk + verify PASS.

---

## 3. Preflight (run once)

```bash
bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/refresh_pipeline.sh
bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_review_loop.sh
```

---

## 4. Wave batch table (first 3 batches — start here)

| Batch ID | Route | Chapters | Dispatch prompts dir |
|----------|-------|----------|----------------------|
| `w1_foundation_fan-out_01` | fan-out | 16 | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/prompts/dispatch/` |
| `w1_foundation_fan-out_02` | fan-out | 16 | same |
| `w1_foundation_inline_01` | inline | 16 | same (parent inline — no subagent) |

Full curriculum: `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/card_curriculum.yaml`

**Totals:** 136 ingests · ~58 fan-out · ~78 inline · 102 dispatch prompts generated

---

## 5. Per-chapter subagent (fan-out)

| Role | Path |
|------|------|
| Schema | `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md` |
| Subagent packet (canonical) | `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md` |
| **Generated dispatch** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/prompts/dispatch/{slug}_ch{NN}_card_extract.md` |
| **Text slice attach** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/attachments/{slug}_ch{NN}_SLICE.txt` |
| **Write cards** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/practical_cards/{topic_slug}.yaml` |

**Pilot merge (do not delete):** `sandwich-prompt-refocus`, `quorum-read-write`, `two-phase-commit-trace`, `genai-chart-summarization-efficacy`

---

## 6. Verify (after each batch + before wire)

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon
find /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon -path '*/practical_cards/*.yaml' -print0 | xargs -0 grep -iE 'text her|text him|send this opener|copy-paste this' && echo FAIL || echo PASS
```

---

## 7. Consumer wire (`kickoff wire` after verify PASS)

| Step | Path / command |
|------|----------------|
| Kickoff doc | `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md` Phase 2B |
| Sync | `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/sync_cs_ai_corpus.sh` |
| Chunk build | `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/build_cs_ai_chunks.sh --no-sync` |
| Check | `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/check_cs_ai_rag.sh --no-sync` |
| Smoke | `bash /Users/dubs/Projects/local-rag-linux-setup/scripts/rag_query.sh "What are the steps for sandwich prompt refocus?"` |

---

## 8. Status SSOT

| Artifact | Path |
|----------|------|
| Pipeline INDEX | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/INDEX.md` |
| Live STATUS | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/STATUS.md` |
| Orchestrator status | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/plans/orchestrator_status.yaml` |
| Piranesi mirror | `/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/phase2-cs-ai/INDEX.md` |
| S4 canon | `/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/returns/scholia_practical_ingest_decision_canon_20260626.md` |

---

## Code review fixes shipped

| Bug | Fix |
|-----|-----|
| Manifest flag before cards | Reordered Phase 2A in cs-ai kickoff doc |
| RAG sync skipped practical_cards | `sync_cs_ai_corpus.sh` rsyncs `metadata/practical_cards/` |
| Chunk builder ignored YAML cards | `build_cs_ai_chunks.py` + `_practical_card_chunk.py` |
| No automated tests | `scripts/test_verify_practical_cards.py` + RAG practical-card test |
| Plan-only chats, no pipeline | deai-style `practical_cards_pipeline/` with refresh + orchestrator |

---

## Next operator action

1. Open new chat → paste **ORCHESTRATOR** path above  
2. Say **`kickoff phase 2 w1_foundation_fan-out_01`** (or `kickoff phase 2` for orchestrator-picked next batch)  
3. After all waves + verify → **`kickoff wire`**
