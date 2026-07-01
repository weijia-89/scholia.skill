# Synthesis operator table (ChatPRD — scholia deai-operator-corpus)

**Scope:** Closed-corpus ChatPRD synthesis only (digest → skill brief → cursor handoff). Phase 2 refine **skipped** when operator adversarially reviewed ingests.  
**Web policy:** Gate A primary for craft extraction; digest **may** web-verify load-bearing external facts (≤5 searches/window, palamedes bar). Ingest stays primary-only. Piranesi export path unchanged (Cursor export-only, no web).
**Returns folder (operator saves here; do not paste in chat tables):** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/`

---

## Iron laws (operator chat output)

1. **Current phase only** — emit one synthesis phase per response. Do not preview Phase N+1 until Phase N outputs exist on disk (see phase gate below).
2. **Columns** — `Priority` · `Window` · `Prompt` (full absolute path) · `Attachments` (bulleted list of full absolute paths).
3. **No Save to column** — operator links saves in chat; agent never prints save paths in operator tables.
4. **Full paths as visible plain text** — no `[label](/Users/…)` · no ellipses · no bare filenames. See `/Users/dubs/Projects/trainer.skill/references/operator-path-output.md` rules 7–9.
5. **Attachments column** — bulleted full paths. **Order:** `00_CORPUS_SYNTH_CONTRACT.md` first (MUST READ), then up to 7 `*_ingest.md`. Entire column = drag-upload (≤8). Digest prompt is **paste only**. Manifest (not attach): `localonly/phase3_window_manifests/{window_id}.md`.
6. **Hard limit: 1 contract + ≤7 ingests = 8 attach** — pack windows to ~7 ingests where semantically coherent; minimum 6 ChatPRD sessions for 37 ingests. Build: `python3 …/scripts/build_synth_attach_packs.py --clean`

---

## Phase gate (which table to emit)

| Active phase | Condition on disk | Prompt SSOT |
| ------------ | ----------------- | ----------- |
| **3 Evidence digest** | No `corpus_evidence_digest_*.md` for current wave; ingests on disk | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` |
| **4 Skill brief** | Digest(s) saved; operator resolved NEEDS_REVIEW; no `deai_operator_corpus_skill_brief_*.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md` |
| **5 Cursor handoff** | Skill brief saved; no `cursor_implement_brief_*.md` | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md` |

**Phase 2 Refine (skipped):** When operator adversarially reviewed each ingest, do **not** emit refine rows or per-slug `synth_attach/{slug}/` packs.

**Regenerate table:** `python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/emit_synthesis_operator_table.py`

**Build attach packs:** `python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/build_synth_attach_packs.py --clean`

**On-disk table:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/phase3_evidence_digest_operator_table.md`

---

## Table template (Phase 3 example)

```markdown
## Phase 3 — Evidence digest (current)

| Priority | Window | Prompt | Attachments |
| -------- | ------ | ------ | ----------- |
| p0_deai | 3A_deai_long_papers | /Users/dubs/Projects/.../prompts/synth_corpus_evidence_digest.md | - /Users/dubs/Projects/.../synth_attach/3A_deai_long_papers/01_long_2018_portable_mentor_part03_20260628_ingest.md<br>- ... |
```

One row per merge window. Up to 8 ingest paths bulleted in Attachments; paste Prompt separately.

---

## Merge windows (37 ingests · 6 sessions · contract + ≤7 ingests each)

| Window | Ingests | Theme |
| ------ | ------- | ----- |
| `3A_deai_craft_ethics` | 7 | Long I–IV + McKee + Jones + s00146 |
| `3A_deai_process_research` | 2 | Long V + s40979 |
| `3B_baker_ginna` | 7 | Baker ch01–07 + Ginna ch14–15 |
| `3B_workplace_rhetoric` | 7 | Ginna parts + Henry + Peeples + Terk L02 |
| `3B_skills_business_writing` | 7 | Terk L03–07 + Locker ch02–06 |
| `3B_craft_structure` | 7 | Locker ch07–08 + Munier + Olmstead |

SSOT: `scripts/build_synth_attach_packs.py` → `PHASE3_WINDOWS`.

---

## Terminology (deprecated in operator chat)

| Deprecated | Use instead |
| ---------- | ----------- |
| ingest attach / primary attach | **Attachments** — bulleted ingest copies from merge window folder |
| Save to column | Operator links in chat; folder = `chatprd_returns/` |
| Phase 2 per-slug refine rows | Skipped when ingest adversarially reviewed |

---

## Cross-links

- `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/PIPELINE.md`
- `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`
- `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/prompt_chain.py`
