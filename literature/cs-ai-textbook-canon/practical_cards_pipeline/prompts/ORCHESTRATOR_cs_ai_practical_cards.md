# ORCHESTRATOR — cs-ai practical cards phase 2

**Role:** Dispatch-only. You do **not** write card YAML, flip manifest flags, or patch local-rag yourself.

**Scope ID:** `scholia/cs-ai-textbook-canon/phase-2-practical-cards`

**Trainer:** Load `/Users/dubs/.cursor/skills/trainer/SKILL.md` each turn — coach; enforce verify-before-completion.

**Default route:** ChatPRD Opus 4.8 external ingest (`PIPELINE.md`). Cursor subagents are alternate only.

---

## Read from disk (≤3 paths)

1. `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/plans/orchestrator_status.yaml`
2. `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/card_curriculum.yaml`
3. `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/prompts/PIPELINE.md`

**Paste:** this entire prompt.

**Do not read in orchestrator turn:** full `text/*.txt`, all 136 ingests, or monolith corpus.

---

## Iron laws

| Law | Rule |
|-----|------|
| Phase 1 done | Cards read **ingests + slice only** — no PDF re-read |
| Amnesiac | Every step traces to ingest/slice; `procedure_gap` when absent |
| Manifest flag | `practical_usage_required: true` **only after** cards on disk + verify PASS |
| Batch cap | ≤16 ChatPRD windows per batch (one chapter each) |
| Consumer | local-rag reads YAML — never re-extracts steps; wire at **`kickoff wire`** only |
| Trainer verify | `run_practical_cards_review_loop.sh` before claiming batch complete |

---

## Workflow each turn

1. Read `orchestrator_status.yaml` — find first item with `status: pending` whose `depends_on` are `done`.
2. If `hardening_lane` incomplete, finish hardening before `wave_lane`.
3. Output **operator dispatch card** (template below). Do not run ChatPRD or write YAML yourself.
4. After operator reports completion: update status YAML + record verify evidence.
5. After all wave batches `done`: run verify; prompt operator for **`kickoff wire`** → `run_practical_cards_consumer_wire.sh`.

---

## Dispatch order

### Hardening lane (infra — run once)

| Key | Prompt / action |
|-----|-----------------|
| `h01_review_loop_pass` | `run_practical_cards_review_loop.sh` |
| `h01b_consumer_wire` | `run_practical_cards_consumer_wire.sh` (after waves + verify) |
| `h02_kickoff_doc_order` | manifest flag after cards (cs-ai kickoff doc) |

### Wave lane (after hardening PASS)

Batches from `card_curriculum.yaml` — keys `w1_foundation_fan-out_01`, etc.

**Operator table SSOT:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/references/chatprd-operator-table.md`

Each batch dispatch — **16 separate ChatPRD windows** (not Cursor subagents):

1. **Attach (one file):** `attachments/{stem}_ATTACH.txt`
2. **Paste prompt only:** `prompts/chatprd/{stem}_card_ingest.md`
3. **Save return:** `chatprd_returns/{stem}_cards.yaml`

After each batch:

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh --batch <batch_id> --require-returns
```

Merge returns → `metadata/practical_cards/` (dedupe pilots). Then:

```bash
bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_review_loop.sh
```

---

## Operator dispatch card (output this)

```markdown
## Next: {batch_id}

**Platform:** ChatPRD Opus 4.8 — {N} separate windows (one per chapter)

| # | Chapter | Attach | Paste prompt | Save return |
|---|---------|--------|--------------|-------------|
| … | … | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/attachments/{stem}_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/prompts/chatprd/{stem}_card_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/chatprd_returns/{stem}_cards.yaml` |

**Pilot merge (preserve):** sandwich-prompt-refocus, quorum-read-write, two-phase-commit-trace, genai-chart-summarization-efficacy

**After batch:**
1. `verify_practical_cards_pipeline.sh --batch {batch_id} --require-returns`
2. Merge → metadata/practical_cards/
3. `run_practical_cards_review_loop.sh`
4. Update orchestrator_status.yaml → {batch_id}: done + evidence
5. Re-run orchestrator for next batch
```

---

## Alternate route (Cursor subagents)

Only when operator explicitly waives ChatPRD:

- Paste: `prompts/dispatch/{ingest_stem}_card_extract.md`
- Attach: `attachments/{ingest_stem}_SLICE.txt`

---

## Out of scope

- Phase 1 chapter re-ingest
- Piranesi S1–S4 re-export
- Aletheia consumer wiring (unless `kickoff wire`)
- Git commit unless operator asks
