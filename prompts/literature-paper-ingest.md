# Paper ingest — scholia peer-reviewed fan-out

Load when: ≥3 peer-reviewed papers, paper fan-out, one agent per paper.

**Schema SSOT:** palamedes `literature-corpus-fanout` (8 fields). Scholia dispatches sub-agents; palamedes is passive schema owner.

## Mandatory fields (paper-ingest)

1. **title** — verbatim from PDF front matter
2. **authors** — list; et al. only if source uses it
3. **year** — publication year
4. **venue** — journal or proceedings
5. **DOI** — or `[preprint]` + URL; never path-only
6. **scope** — what the paper covers; 2–4 sentences
7. **key_findings** — numbered; each traceable to section anchor in text export
8. **coverage_attestation** — checklist of sections read vs deferred

## Output artifact

Write `literature/ingests/{slug}_ingest.md` (≤4500 words).

Include metadata table at top:

| Field | Value |
|-------|-------|
| pdf_path | literature/pdfs/{slug}.pdf |
| text_path | literature/text/{slug}.txt |
| source_type | peer_reviewed_article |

## Epistemic tags

- `[verified]` only with Gate A/B on DOI/abstract claims in this session
- `[preprint]` on arXiv/bioRxiv rows in provenance
- `[inferred]` for compressed summaries — chain ≤15w from quoted text
- No training-prior facts without tag

## Fan-out rules

- One paper per sub-agent (parallel; N≤16 per CLAIMS C-R004)
- Parent scholia never reads full PDF bodies at N≥5 PDFs
- Cross-paper synthesis only after all ingests + LITERATURE_INDEX roles filled

## Forbidden

- Path-only DOI column in child `references/provenance.md` (SF-06)
- Monolith single-context read of entire corpus
- P9 literal in scholia root SKILL (use paper fan-out)
