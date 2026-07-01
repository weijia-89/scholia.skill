# S4 open decisions (folded from raw S3 §8)

META: re-reconcile 20260618 · source: `stage3_coverage_gap_20260618_ingest.md` §8

Merged into platform canon — operator may override via session bet.

| Decision | Recommendation | Blocking | Platform status |
|----------|----------------|----------|-----------------|
| Skill name disambiguation | `scholia-corpus-to-skill` slug | No | **SHIPPED** in research slug |
| v0.1 output modes | skill + reference-library; defer 3 | No | **v0.2 shipped** all 5 modes |
| Zotero MCP | optional_tools; cookjohn/zotero-mcp | No | **SHIPPED** zotero workflow |
| Provenance format | Flat table + relation column v0.1 | No | **SHIPPED** TROVE template |
| ref-verify | SF-06b WARN pre-filter | No | **DOC** in canon |
| Preprint policy | Tag-and-warn; no sole-support enforced gates | No | **DOC** in negative-space |
| Non-English | Supported with warnings; translations in text/ | No | **DOC** |
| Depth cap | **2** (root → ingest subagent) | **Yes** | **SHIPPED** SKILL.md |
| N>20 clustering fallback | Defer v0.2 | No | **DOC** — references/n20-clustering-fallback.md |
| Cross-stage check | Required L3+ | No | **SHIPPED** C-DG004 script |
