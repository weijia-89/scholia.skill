# STATUS — cs-ai practical cards phase 2

**Updated:** 2026-07-01T18:20:22 UTC
**Corpus:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon`
**Pipeline:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline`

| Metric | Count |
|--------|-------|
| Chapter ingests | 136 |
| Fan-out (>3 hooks) | 58 |
| Inline (≤3 hooks) | 44 |
| Skip (0 hooks) | 34 |
| Dispatch batches (≤16) | 10 |
| Pilot cards on disk | see `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/practical_cards/` |

## Commands

| Step | Command |
|------|---------|
| Regenerate curriculum | `python3 /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/plan_card_waves.py` |
| Build dispatch prompts | `python3 /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/build_card_dispatch_prompts.py` |
| Build attach slices | `python3 /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/build_attach_slices.py` |
| Verify preflight | `bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh --self-test` |
| Review loop | `bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_review_loop.sh` |
| Orchestrator | paste `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/prompts/ORCHESTRATOR_cs_ai_practical_cards.md` |

## Operator gates

| Phrase | Action |
| **`kickoff phase 2`** | Run next pending wave batch (subagents) |
| **`kickoff verify`** | Re-run verify only |
| **`kickoff wire`** | RAG consumer wire (after verify PASS) |

## Piranesi mirror

`/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/phase2-cs-ai/STATUS.md`
