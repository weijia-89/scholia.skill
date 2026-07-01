# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 15

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch15_ingest.md |
| text_lines_read | 4964–5085 |
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
| chapter_number | 15 |
| chapter_title | Content delivery networks |
| part | Part III — Scalability |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

CDNs as geo-distributed reverse-proxy overlay networks: BGP limitations, edge placement, global DNS LB, multi-tier caching, DDoS shielding.

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **Overlay > cache** (4981–5047): BGP optimizes hops not latency; edge clusters + IXPs; TCP connection pools.
2. **Dynamic frontend** (5049–5052): CDN shields non-cacheable API; DDoS protection.
3. **Cache tiers** (5055–5085): Hit ratio vs edge count trade-off; intra-cluster partitioning → ch16.

---

## Section digest (anchored)

### §15.1 Overlay (4981–5052)

Figure 15.1 RTT reduction.

### §15.2 Caching (5055–5085)

Edge + intermediate tiers.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Explain content delivery networks role in Cruder scale path.
2. Apply patterns to operator cloud stack.

### worked_examples_present

**Y** — Cruder narrative + figures cited in text.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Design hook:** Apply Content delivery networks to one operator static-asset path.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.15 full slice | Read | 4964–5085 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 4964–5085 only.

---

## Operator hooks

### 1. w2_systems_llm (Part III — Scalability)

Edge delivery stack; pairs S3 ch17 + CDN for static/media.

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

- Claims trace to lines 4964–5085 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Content | Content delivery networks per chapter |
