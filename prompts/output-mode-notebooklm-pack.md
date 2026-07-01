# Output mode: notebooklm-pack — scholia prep → notebooklm-prep handoff

**Owner:** scholia curates corpus artifacts; **notebooklm-prep** owns `.sources` manifest, upload curation, and NotebookLM bootstrap. Scholia does **not** duplicate upload lists or CE templates.

## When to use

Operator bet includes: "NotebookLM", "audio overview", "HM prep notebook", "notebook refresh", or opt-in cloud upload from closed corpus.

## Scholia prep (before handoff)

1. Complete fan-out → ingests → LITERATURE_INDEX → SYNTHESIS (same as study-guide prep).
2. Write `references/provenance.md` with DOI/tag discipline (SF-06).
3. Export operator-facing summary if needed (decision canon, not raw Piranesi dumps).
4. **Do not** auto-upload PDFs — operator explicitly opts in to NotebookLM.

## Handoff payload schema

```yaml
handoff: scholia → notebooklm-prep
output_mode: notebooklm-pack

paths:
  slug: string                    # application or corpus slug
  scope: string                   # e.g. hm-prep, takehome, research
  index_path: literature/index/LITERATURE_INDEX.md
  synthesis_path: literature/ingests/SYNTHESIS.md
  ingests_glob: literature/ingests/*_ingest.md
  provenance_path: references/provenance.md
  corpus_manifest: literature/metadata/corpus_manifest.yaml

sources_candidates:             # notebooklm-prep reads bodies before add
  - path: string                 # relative path; scan-before-add required
    reason: string               # why this source belongs in notebook
    drop_if: string              # optional dedup rule

operator_questions:
  - question: string
    role: string

limits:                           # consumer defaults (notebooklm-prep SSOT)
  max_sources: 50                 # sidebar budget; defer overflow to operator
  max_tokens_hint: 500000         # soft ceiling; prep skill enforces curation
  flat_md_only: true              # ii.{stage}/nblm_uploads/ flat *.md policy

constraints:
  amnesiac: true                  # NotebookLM has zero knowledge outside uploads
  scan_before_add: true           # never path-only .sources edits
  piranesi_canon_over_raw: true   # prefer S4 decision canon over S1-S3 ingests
```

## notebooklm-prep invocation

Load: `/Users/dubs/Projects/.cursor/skills/notebooklm-prep/SKILL.md`

Trigger: "create notebook" / "notebook refresh" + handoff payload.

notebooklm-prep owns: `.sources` edit with scan-before-add, `copypasteURLs.txt`, Custom Experience, Phase A/B bootstrap, upload curation per `notebooklm_upload_curation.md`.

Scholia does **not** patch notebooklm-prep templates or toren application paths unless operator colocates corpus under `applications/<slug>/`.

## Verify before ship

| Check | Owner |
|-------|-------|
| Corpus complete on disk | scholia verify |
| C-DG004 structure | check_cross_stage_consistency.sh |
| `.sources` scan-before-add | notebooklm-prep checklist |
| validate_prep_layout_v2 (if toren slug) | applications scripts |

## Failure modes

| Failure | Route |
|---------|-------|
| >50 sources | notebooklm-prep dedup + operator triage |
| Path-only .sources add | Block; run scan-before-add |
| Sparse corpus | piranesi export → ingest → retry handoff |
| MCP in session | @wintermute → form-check before zotero/notebook MCP |
