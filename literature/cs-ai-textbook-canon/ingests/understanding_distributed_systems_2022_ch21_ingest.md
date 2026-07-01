# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 21

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch21_ingest.md |
| text_lines_read | 6376–6771 |
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
| chapter_number | 21 |
| chapter_title | Microservices |
| part | Part III — Scalability |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Functional decomposition into microservices: monolith pain, team topology, caveats, API gateway (routing, composition, GraphQL, JWT auth, cross-cutting).

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **Decomposition** (6407–6445): Independent deployable services; small teams; per-service data stores; deep APIs not micro-sized.
2. **Caveats** (6449–6551): Stack standardization; remote call complexity; distributed monolith; ops/testing/observability; eventual consistency; **monolith first** (Fowler MicroservicePremium).
3. **API gateway** (6559–6771): Routing map; composition reduces client calls (availability product); GraphQL; auth at gateway, authz in services; JWT vs opaque; gateway bottleneck — managed APIM.

---

## Section digest (anchored)

### §21.1 Caveats (6449–6551)

Fowler + Ousterhout cites.

### §21.2 API gateway (6559–6771)

Figures 21.1–21.3; JWT; GraphQL.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Apply monolith-first criteria.
2. Design gateway routing/composition.
3. Separate authn vs authz.
4. Spot distributed monolith smells.

### worked_examples_present

**Y** — Cruder decomposition figures; JWT/API keys.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Peel order:** First service to extract from monolith.
2. **Composed SLA:** Availability of N internal calls.
3. **Token choice:** JWT vs opaque internal.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Monolith→services (6380–6445) | Read | 6380–6445 |
| §21.1 Caveats | Read | 6449–6551 |
| §21.2 Gateway | Read | 6559–6771 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 6376–6771 only.

---

## Operator hooks

### 1. w2_systems_llm (Part III — Scalability)

Organizational scale; ch13 outbox/sagas across services; ch22 splits gateway planes.

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **Philosophy SD** | High — Ousterhout deep modules cite |
| **DDIA 2e** | Medium — data across services |

### 4. Scholia fit

- **Worked examples:** Y (gateway responsibilities table).

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | Fowler MicroservicePremium, GraphQL, JWT.io |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Fowler + gateway depth |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Monolith first | 6546–6551 | Team-size dependent |
| Micro name misleading | 6440–6444 | Services should be substantial |

**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Ch.22 | Control/data plane |
| Ch.23 | Messaging |

---

## Provenance notes

- Claims trace to lines 6376–6771 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Distributed monolith | Microservices with monolith coupling |
| API gateway | Public facade reverse proxy |
