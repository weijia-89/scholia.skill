# Output harness contract (scholia skills)

**Scope:** mechanical verification of **generated artifacts** — not skill metadata lint (see `skill-fitness`) and not semantic phylax.

## Problem

Skills that emit files (ingests, cards, prompts, operator tables) fail in operator loops when agents hand-copy paths, skip sections, or ship YAML that does not match schema. Doc-only iron laws do not catch this until merge/verify — too late.

## Pattern

| Layer | What | When |
|-------|------|------|
| **Generator** | `refresh_*.sh` / build scripts | produces artifacts from SSOT (curriculum, manifest) |
| **Harness** | `verify_*.py` + `verify_*.sh` | deterministic oracles on disk output |
| **Self-test** | `--self-test` + `test_verify_*.py` | regression fixtures without corpus |
| **Gate** | review loop / refresh tail / `kickoff verify` | exit 2 blocks ship |

**Loop circuit breakers** (`scripts/lib/review_loop_guard.sh`): **min 2 successful phases** (never exit after first pass) · max 8 attempts · 900s wall clock · stuck signature abort (2× same failure on one phase). Success deepens `REVIEW_LOOP_ITER`; failure retries the same phase.

**Gates:**
- Scholia only: `run_practical_cards_verify_gate.sh` (single pass)
- Bounded loop: `run_practical_cards_review_loop.sh`
- Consumer (`kickoff wire`): `run_practical_cards_consumer_wire.sh`

**Iron law:** every generator that writes operator-facing output must have a paired harness invoked at refresh tail or review loop.

## Oracle naming

- **SF-*** — scholia.skill root / child skill (`verify_scholia.sh`)
- **PS-*** — pressure scenarios (`verify_scholia.sh --pressure`)
- **PC-*** — practical card YAML (`verify_practical_cards.py`)
- **PC-P*** — practical cards **pipeline** artifacts (`verify_pipeline.py`)

## cs-ai practical cards (reference implementation)

**SSOT:** `literature/cs-ai-textbook-canon/practical_cards_pipeline/card_curriculum.yaml`

**Generators:** `refresh_pipeline.sh` → attach, ChatPRD prompts, operator table

**Harness:**

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh --batch w1_foundation_fan-out_01
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh --summary
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh --batch w1_foundation_fan-out_01 --require-returns
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh --self-test
```

| ID | Check |
|----|-------|
| PC-P01 | `card_curriculum.yaml` loads |
| PC-P02 | `attachments/{stem}_ATTACH.txt` exists per non-skip chapter |
| PC-P03 | `prompts/chatprd/{stem}_card_ingest.md` exists |
| PC-P04 | attach has STABLE-CONTEXT, PHASE-1-INGEST, TEXT-SLICE |
| PC-P05 | attach has no `[MISSING` markers |
| PC-P06 | prompt references resolvable attach absolute path |
| PC-P07 | prompt save path matches `chatprd_returns/{stem}_cards.yaml` |
| PC-P08 | operator table rows match curriculum |
| PC-P09 | operator table attach/prompt paths resolve |
| PC-P10 | return YAML validates (`verify_practical_cards.validate_card_file`) |
| PC-P11 | no README/MANIFEST in upload dirs |
| PC-P12 | phase-1 ingest exists on disk |
| PC-P13 | prompt does not reference `prompts/dispatch/` (wrong route) |
| PC-P14 | `--batch` / `--route` scope resolves ≥1 chapter |

**After ChatPRD batch:** run `--batch <id> --require-returns` before merge.

**After merge:** `verify_practical_cards.sh` on corpus root (PC-* on `metadata/practical_cards/`).

## Adding harnesses to new skills

1. Name oracles (`XX-###`) in a `references/*-harness.md` table.
2. Implement `scripts/verify_<artifact>.py` with `--self-test` using `tempfile` fixtures.
3. Add `scripts/verify_<artifact>.sh` wrapper (exit 0/2).
4. Add `scripts/test_verify_<artifact>.py` (unittest).
5. Wire tail of generator script + review loop / `kickoff verify`.
6. Register in parent `SKILL.md` references table.

**Reuse:** import shared validators (e.g. `verify_practical_cards.validate_card_file`) instead of duplicating parsers.

## Exit codes

- `0` — all FAIL-tier oracles pass (WARN allowed)
- `2` — one or more FAIL; Stop hook / review loop blocks
