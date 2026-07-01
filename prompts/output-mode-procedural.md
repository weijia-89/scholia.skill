# Output mode: procedural — scholia prep → palamedes handoff

**Owner:** scholia sets `layout_mode: flat` in manifest; **palamedes** renders via `procedural-guide-site.md`. No `literature/ingests/` fan-out required (C-DG007 W02×W05).

## When to use

Operator bet: "how do I fix X", "setup guide", "install walkthrough", "reassembly steps", "procedural HTML", single how-to corpus (not exam cram).

## Corpus layout (flat)

Set in `literature/metadata/corpus_manifest.yaml`:

```yaml
layout_mode: flat  # skips ingests/ requirement; PDFs → text/ exports only
```

Minimum tree:

```
literature/
  pdfs/           # operator-supplied
  text/           # Marker / pdftotext exports (required for ingest)
  metadata/corpus_manifest.yaml
references/       # optional provenance for load-bearing specs
```

**Not required:** `literature/ingests/` fan-out, LITERATURE_INDEX, SYNTHESIS (unless operator also wants reference-library).

## Scholia prep (before handoff)

1. Confirm `layout_mode: flat` in manifest.
2. Export readable text to `literature/text/{slug}/` (Marker for equation-heavy).
3. Capture operator goal + success criteria in session bet.
4. Run verify on staging dir — monolith/ingest gates N/A when flat + no ingests/.
5. If corpus has chapter ingests and operational output: phase-2 cards per `prompts/practical-usage-card-fanout.md` + `references/practical-usage-schema.md`.

## Handoff payload schema

```yaml
handoff: scholia → palamedes/procedural-guide-site
output_mode: procedural
layout_mode: flat

paths:
  corpus_manifest: literature/metadata/corpus_manifest.yaml
  text_sources:
    - literature/text/{slug}/{slug}.md   # one or more primary exports
  pdf_sources:                          # optional reference only
    - literature/pdfs/{author}_{year}_{slug}.pdf

session_bet:
  subject: string          # e.g. "2015 Forester A/C clutch shim"
  slug: string             # output filename stem
  output_dir: string       # operator-chosen write path (outside scholia repo OK)
  stakes: L2-L4            # physical repair / prod config → L3+

load_bearing_specs:        # tier-tagged in palamedes P1
  - spec: string           # torque, gap, version pin, security setting
    source_path: string    # relative text/ path or DOI
    tier: verified|inferred|priors-only

constraints:
  single_file_html: true   # default: inline CSS, file:// friendly
  amnesiac: true
```

## Palamedes invocation

Trigger: "fix guide" / "procedural guide" / "setup guide" + handoff payload.

**Consumer spec:** `/Users/dubs/Projects/palamedes/skill/references/procedural-guide-site.md`

Palamedes owns: single-file HTML, mandatory section IDs (`#start-here`, `#walkthrough`, `#verify`, etc.). Scholia does **not** ship HTML templates.

## Verify before ship

| Check | Owner |
|-------|-------|
| text/ exports present | scholia operator workflow |
| layout_mode flat | corpus_manifest.yaml |
| Load-bearing specs tier-tagged | palamedes P1→P4 |
| Guide opens offline | operator spot-check |

## Failure modes

| Failure | Route |
|---------|-------|
| No text layer | Block; operator runs Marker/pdftotext |
| layout_mode full but procedural bet | Coach: switch to flat or use study-guide mode |
| Unreadable PDF | Set drm/unreadable in manifest; operator judgment |
