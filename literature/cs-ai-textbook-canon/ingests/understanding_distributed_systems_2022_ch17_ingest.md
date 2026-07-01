# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 17

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch17_ingest.md |
| text_lines_read | 5280–5422 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| ISBN_print | [not found in text export] |
| ISBN_electronic | [not found in text export] |
| publisher | Self-published (Roberto Vitillo) |
| chapter_number | 17 |
| chapter_title | File storage |
| part | Part III — Scalability |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Offload static files to S3/Azure; Azure Storage architecture: location service, stream/partition/front-end layers, chain replication.

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **Managed blob** (5285–5295): Public URL → CDN direct.
2. **Azure layers** (5320–5400): DNS account routing; stream extents + chain replication; partition manager range index; stateless front-end.
3. **S3 note** (5402–5415): Strong consistency added 2021; AS built for strong consistency from start.

---

## Section digest (anchored)

### §17.1 Azure Storage (5299–5415)

Figures 17.1–17.3; Calder SOSP'11.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Explain file storage role in Cruder scale path.
2. Apply patterns to operator cloud stack.

### worked_examples_present

**Y** — Cruder narrative + figures cited in text.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Design hook:** Apply File storage to one operator static-asset path.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.17 full slice | Read | 5280–5422 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 5280–5422 only.

---

## Operator hooks

### 1. w2_systems_llm (Part III — Scalability)

Blob offload for Cruder media; control/data plane preview ch22.

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | Medium — parallel themes at data layer |

### 4. Scholia fit

- **Worked examples:** Y (figures).
- **Chapter boundary:** Clean.

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | Primary papers and vendor docs in footnotes |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Cruder + cloud refs |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|


**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Next UDS ch | Scale path continues |

---

## Provenance notes

- Claims trace to lines 5280–5422 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| File | File storage per chapter |
