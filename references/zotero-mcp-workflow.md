# Zotero MCP — optional corpus_manifest pre-fill

**Status:** optional operator workflow. Scholia does **not** auto-download PDFs or require Zotero MCP for verify.

**MCP gate:** Before invoking zotero-mcp in session, load `@wintermute` and route policy approval through **form-check** (blast radius, data leaving device).

## When to use

- Operator has Zotero library with metadata + linked PDFs
- Session bet includes many papers and manual manifest entry is tedious
- Operator still supplies PDF files on disk under `literature/pdfs/`

## When NOT to use

- No Zotero installed or MCP unavailable → **manual manifest** from `references/corpus-manifest-template.yaml`
- Cloud-only PDFs without local export → operator downloads first
- PHI/ITAR/no-TDM corpora → refuse per `references/negative-space.md`

## Prerequisites

1. Zotero desktop running with library accessible
2. MCP server configured (e.g. nealcaren/mcp-zotero or BirdInTheTree/zotero-mcp)
3. Operator confirms which collection maps to this scholia session

## Workflow (operator + agent)

```
Operator: "populate manifest from Zotero collection {name}"
Agent:
  1. form-check: MCP scope approved for this session
  2. get_collections → find collection by name
  3. get_collection_items(collection_key) → item_keys[]
  4. For each item_key:
     a. get_item(item_key) → title, creators, date, DOI, itemType
     b. Map to corpus_manifest.yaml entry:
        - doi: {DOI or empty}
        - title: {title}
        - authors: {creators joined}
        - year: {date.year}
        - source_type: {journal_article|book_chapter|review} from itemType
        - pdf_path: literature/pdfs/{firstauthor}_{year}_{slug}.pdf
        - ingest_status: pending
        - text_quality: unknown
        - legal_status: unknown
        - drm: none
        - layout_mode: full
  5. find_duplicates → warn operator
  6. Write literature/metadata/corpus_manifest.yaml
  7. Report: "{N} items imported, {M} duplicates flagged, {K} missing local PDFs"
```

## PDF path resolution

Zotero MCP returns metadata only unless RAG/index tools enabled. Agent must:

1. Check if PDF exists at mapped `pdf_path`
2. If missing: list item in report; operator copies PDF manually
3. Never silently fetch PDFs from network without operator explicit step

## Failure modes

| Failure | Fallback |
|---------|----------|
| MCP timeout / auth error | Manual manifest from template |
| Missing DOI | Leave empty; tag in provenance at ingest |
| Duplicate items | Operator merges in Zotero or dedupes manifest |
| Collection not found | Operator renames or picks alternate collection |

## Verify impact

**None.** `verify_scholia.sh` does not call Zotero MCP. Manifest fields validated separately when corpus layout exists.

## Negative space

- zotero-mcp is **optional** — failure mode = manual manifest
- No new cloud dependencies in verify script
- Scholia parent platform does not bundle MCP server code

## References

- Canon: `piranesi.skill/research-projects/0621-scholia-corpus/returns/stage3b_coverage_gap_deep_20260618_ingest.md` § C-DG006
- Template: `references/corpus-manifest-template.yaml`
- MCP policy: `/Users/dubs/Projects/wintermute.skill/SKILL.md`
