# KICKOFF — Corpus extraction wave (superset + trainer gates)

**Scope ID:** `deai-corpus-extraction-wave-20260627`

**Role:** Orchestrator — dispatch-only. You coordinate waves; you do **not** implement skill patches or author ChatPRD ingests unless explicitly assigned a worker slot.

**Trainer:** Load `/Users/dubs/.cursor/skills/trainer/SKILL.md` + `/Users/dubs/Projects/trainer.skill/references/trainer-dispatch-gates.md`. Coach on scope; dispatch graph before spawn.

**Superset:** Load `/Users/dubs/.cursor/skills/superset/SKILL.md`. Daily log SSOT required before parallel dispatch.

---

## Project root

`/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`

## Read from disk (orchestrator — ≤4 paths)

1. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/ingest_inventory.yaml`
2. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chapter_curriculum.yaml`
3. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/daily/2026-06-27.md`
4. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md`

**Paste:** this entire prompt.

---

## Iron laws

| Law | Rule |
| --- | ---- |
| ChatPRD authors | Ingests + synthesis (`synth_*` prompts) |
| Cursor implements | Workers read ≤4 paths from disk; no @-attach |
| Trainer gate | Review manifest + adversarial pass before each wave |
| Verify loop | Re-run split/build/pytest until PASS; no "done" without evidence |
| Long deai priority | **Part III (sentence/paragraph)** > Parts I, IV > Part II > **Part V (process)** |
| Terk lesson07 | Pattern slice at body offset ~276983 — not 196512 cross-ref |
| No skill patches | From raw ingests until refine + evidence digest gate |
| Prompt SSOT | `CORPUS_SYNTH_CONTRACT.md` + `prompt_chain.py`; regen via `rewrite_chatprd_prompts.py` + `generate_chapter_prompts.py` |
| Prompt SSOT | `CORPUS_SYNTH_CONTRACT.md` + `prompt_chain.py`; regen via `rewrite_chatprd_prompts.py` + `generate_chapter_prompts.py` |

---

## Wave manifest (superset daily log)

**Artifact:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/daily/2026-06-27.md`

Operator signs manifest before spawning agents. Each agent updates `status` in YAML front-matter.

### Phase 0 — Pipeline rebuild (serial)

| Agent | owned_paths | produces | verify |
| ----- | ----------- | -------- | ------ |
| `pipeline_rebuild` | `scripts/split_*.py`, `chapter_curriculum.yaml` | chapter slices + attaches | `wc -c` lesson07 + long part03; no truncation note on lesson07 |

Commands (operator or agent):

```bash
python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/split_epub_chapters.py
python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/split_chapters.py
python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/build_attach_uploads.py
python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/generate_chapter_prompts.py
```

**Trainer review checkpoint:** curriculum diff + slice char counts + Terk lesson07 opens with email lesson body.

### Phase 1 — ChatPRD ingests (parallel where independent)

| Agent | target | priority | prompt |
| ----- | ------ | -------- | ------ |
| `ingest_terk_l07` | terk lesson07 | P0 | `prompts/08_terk_prof_writing_skills_lesson07_ingest.md` |
| `ingest_long_p03` | Long Part III sentence/paragraph | **P0 deai** | `prompts/11_long_2018_portable_mentor_part03_ingest.md` |
| `ingest_long_p01` | Long Part I | P1 deai | `prompts/11_long_2018_portable_mentor_part01_ingest.md` |
| `ingest_long_p04` | Long Part IV | P1 | `prompts/11_long_2018_portable_mentor_part04_ingest.md` |
| `ingest_long_p02` | Long Part II (truncation aware) | P2 | `prompts/11_long_2018_portable_mentor_part02_ingest.md` |
| `ingest_long_p05` | Long Part V revision process | P3 low deai | `prompts/11_long_2018_portable_mentor_part05_ingest.md` |

**Do not drop part05** — ingest after I–IV or in parallel if windows allow.

**Trainer review checkpoint:** ingest coverage attestation matches single chapter_id; Gate A quotes from attach.

### Phase 2 — Refine (per source) — **SKIPPED this wave**

Operator adversarially reviewed each ingest return. **Do not** run per-source refine ChatPRD windows or emit `synth_attach/{slug}/` packs. Proceed to Phase 3 merge windows with raw `*_ingest.md` attaches.

Legacy path (unreviewed ingests only): `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md` + saved ingest + Gate A ATTACH.

**Orchestrator default:** emit **current synthesis phase only** — ChatPRD table with columns `Priority | Window | Prompt | Attachments` (bulleted full paths). **No Save to column** in operator chat. Spec: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/references/synthesis-operator-table.md` · regen: `python3 …/scripts/emit_synthesis_operator_table.py`

### Phase 3 — Evidence digest + skill brief (serial ChatPRD merge windows)

Build packs: `python3 …/scripts/build_synth_attach_packs.py --clean` → `synth_attach/3A_*`, `synth_attach/3B_*`.

1. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` — attach up to 8 `*_ingest.md` per window (ingests OK; Phase 2 skipped)
2. Operator resolves NEEDS_REVIEW rows
3. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` — deduped implement brief
4. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` — Composer handoff

**Trainer review checkpoint:** no implement until elicitation PASS + brief checklist green.

### Phase 4 — Cursor implement (existing orchestrator)

`/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md`

---

## Autonomous bug-fix loop

After each phase, agent runs verify and fixes until PASS:

| Check | Command / criterion |
| ----- | ------------------- |
| Terk L07 slice | `wc -c` ~28–40k; head contains "E-mail is a vital" |
| Long Part III | `wc -c` ~90–100k; title sentence/paragraph |
| lesson07 attach | no `NOTE: Chapter slice truncated` |
| Manifest chapter_attaches | lists new Long parts + terk L07 |
| Prompts exist | `prompts/11_long_2018_portable_mentor_part0{1,3,4}_ingest.md` |

On FAIL: fix curriculum/scripts → re-run pipeline → re-verify. Max 3 loops then escalate to operator.

---

## Operator dispatch card (template)

**Default orchestrator output (mandatory):** After Phase 0 PASS (or at kickoff when pipeline already green), the orchestrator **always** emits a **ChatPRD attach table** — one row per ChatPRD window. Operator drags **Prompt** + **Attach** into each ChatPRD session (≤8 files per window). Full absolute paths only; no `@`-attach in Cursor.

Columns: `Priority | Slug | Prompt | Attachments` — full absolute paths; Attachments = bulleted list. **No Save to** in chat handoffs.

```markdown
## Next wave: {phase_id}

**Daily log:** /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/daily/2026-06-27.md

**Trainer gate:** {checkpoint description}

**Verify before close:** {commands}

### ChatPRD attach table

| Priority | Window | Agent | Prompt | Attach | Save to | Notes |
| -------- | ------ | ----- | ------ | ------ | ------- | ----- |
| {P0} | {parallel label} | {agent_name} | {absolute prompt path} | {absolute attach path} | {chatprd_returns slug} | {truncation / chapter_id} |
```

Populate rows from daily-log manifest `prompt` + `attach` fields (or derive from `ingest_inventory.yaml` + `attachments/`). Group parallel windows by priority; do not omit part05.

### Phase 1 — live table (2026-06-27 wave)

| Priority | Window | Agent | Prompt | Attach | Save to | Notes |
| -------- | ------ | ----- | ------ | ------ | ------- | ----- |
| P0 | parallel | `ingest_terk_l07` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/08_terk_prof_writing_skills_lesson07_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/08_terk_prof_writing_skills_lesson07_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/terk_prof_writing_skills_lesson07_YYYYMMDD_ingest.md` | `chapter_id: lesson07`; slice @276983 |
| P0 | parallel | `ingest_long_p03` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/11_long_2018_portable_mentor_part03_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part03_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part03_YYYYMMDD_ingest.md` | **P0 deai** — sentence/paragraph |
| P1 | parallel | `ingest_long_p01` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/11_long_2018_portable_mentor_part01_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part01_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part01_YYYYMMDD_ingest.md` | `chapter_id: part01` |
| P1 | parallel | `ingest_long_p04` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/11_long_2018_portable_mentor_part04_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part04_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part04_YYYYMMDD_ingest.md` | `chapter_id: part04` |
| P2 | serial | `ingest_long_p02` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/11_long_2018_portable_mentor_part02_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part02_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part02_YYYYMMDD_ingest.md` | attach truncates @119k; full slice on disk |
| P3 | serial | `ingest_long_p05` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/11_long_2018_portable_mentor_part05_ingest.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part05_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part05_YYYYMMDD_ingest.md` | low deai; keep after I–IV |

**Phase 2+ rows:** Prompt = synth prompt path; Attach = saved ingest(s) from Phase 1 (+ optional chapter ATTACH + optional `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`); Save to = `chatprd_returns/{slug}_refined_YYYYMMDD.md` or digest/brief paths per `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md`.

### Phase 2 — refine table (wave 2 ingests on disk) — **SUPERSEDED; do not run**

Historical example only. Current operator table: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/phase3_evidence_digest_operator_table.md`

| Priority | Window | Agent | Prompt | Attach | Save to | Notes |
| -------- | ------ | ----- | ------ | ------ | ------- | ----- |
| P0 deai | 2A | `refine_long_p02` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part02_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/11_long_2018_portable_mentor_part02_ATTACH.txt` + optional `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/long_2018_portable_mentor_part02_refined_20260628.md` | attach truncates @119k |
| P0 deai | 2A | `refine_corpus_3375627` | same refine prompt | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/corpus_3375627_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/01_corpus_3375627_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/corpus_3375627_refined_20260628.md` | ethics paper |
| P1 | 2A | `refine_ginna_ch14` | same | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/ginna_what_editors_do_ch14_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/13_ginna_what_editors_do_ch14_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/ginna_what_editors_do_ch14_refined_20260628.md` | |
| P1 | 2A | `refine_ginna_ch15` | same | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/ginna_what_editors_do_ch15_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/13_ginna_what_editors_do_ch15_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/ginna_what_editors_do_ch15_refined_20260628.md` | |
| P1 | 2B | `refine_baker_ch01` | same | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/baker_2020_prof_writing_speaking_ch01_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/05_baker_2020_prof_writing_speaking_ch01_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/baker_2020_prof_writing_speaking_ch01_refined_20260628.md` | |
| P1 | 2B | `refine_baker_ch03` | same | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/baker_2020_prof_writing_speaking_ch03_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/05_baker_2020_prof_writing_speaking_ch03_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/baker_2020_prof_writing_speaking_ch03_refined_20260628.md` | |
| P1 | 2B | `refine_locker_ch03` | same | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/locker_2012_prof_writing_w231_ch03_20260628_ingest.md` + `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/06_locker_2012_prof_writing_w231_ch03_ATTACH.txt` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/locker_2012_prof_writing_w231_ch03_refined_20260628.md` | |

### Phase 3 — evidence digest + skill brief (6 merge windows)

| Window | Ingests | Notes |
| ------ | ------- | ----- |
| 3A_deai_craft_ethics | 7 | Long I–IV + corpus + jones + s00146 · attach contract first |
| 3A_deai_process_research | 2 | part05 + s40979 |
| 3B_baker_ginna | 7 | Baker + Ginna ch14–15 |
| 3B_workplace_rhetoric | 7 | Ginna parts + Henry + Peeples + Terk L02 |
| 3B_skills_business_writing | 7 | Terk L03–07 + Locker ch02–06 |
| 3B_craft_structure | 7 | Locker ch07–08 + Munier + Olmstead |

Prompt (paste): `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md`

| Step | Prompt | Attach |
| ---- | ------ | ------ |
| 3C skill brief | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` | approved digest(s) only |
| 3D cursor | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` | skill brief only |

---

## Long Parts I–IV rationale (deai lane)

Part V (`part05`) covers revision **process** (submission, literary vs commercial). Parts I–IV hold **prose craft** — especially Part III (sentence + paragraph mechanics). Prioritize ChatPRD ingests:

1. `part03` — P0 deai
2. `part01`, `part04` — P1
3. `part02` — P2 (large; attach truncates)
4. `part05` — P3 (keep; lower deai value)

---

## Related prompts

| Step | Path |
| ---- | ---- |
| Pipeline | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md` |
| Evidence digest | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` |
| Per-source refine | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_refine_per_source.md` |
| Skill brief | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` |
| Contract | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` |
| Cursor handoff | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` |
