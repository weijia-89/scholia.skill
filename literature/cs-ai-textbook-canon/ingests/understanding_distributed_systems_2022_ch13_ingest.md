# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 13

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch13_ingest.md |
| text_lines_read | 4354–4816 |
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
| chapter_number | 13 |
| chapter_title | Asynchronous transactions |
| part | Part II capstone + Part III intro |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Chapter 13 replaces blocking **2PC** with asynchronous atomic patterns: **transactional outbox**, **sagas** with compensating transactions, and **semantic locks**. Uses cashier's-check analogy for atomic-but-not-isolated transfers. Closes Part II (coordination is expensive) and opens **Part III Scalability** with Cruder journey roadmap for Ch.14–23.

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **2PC critique** (4359–4376): Blocking + lock holding; unsuitable for long-lived or cross-org transactions.
2. **Cashier's check analogy** (4378–4393): Async atomic transfer; inconsistent intermediate state; not isolated.
3. **Outbox pattern** (4402–4481): Dual-write RDB + Elasticsearch; XA/2PC impractical; local tx writes outbox row; relay (Debezium) publishes to Kafka; at-least-once + idempotency key (Ch.5.7); resembles SMR log.
4. **Sagas** (4485–4591): Local txs T₁…Tₙ + compensations Cᵢ; orchestrator state machine with durable checkpoints; duplicate messages require idempotent participants; AWS Step Functions / Azure Durable Functions.
5. **Semantic locks** (4599–4603): Dirty flag on saga-touched data until completion.
6. **Part II summary** (4616–4652): Failures unavoidable; reduce coordination via off-critical-path design, apologize (sagas), CRDTs.
7. **Part III intro** (4653–4812): Cruder PoC → scale-out journey; Bill Baker "cattle not pets"; functional decomposition, partitioning, replication; previews ch14 HTTP cache through ch23 messaging.

---

## Section digest (anchored)

### §13.1 Outbox (4402–4481)

Catalog + search index; eventual consistency OK.

### §13.2 Sagas (4485–4591)

Travel booking Figure 13.1 workflow.

### §13.3 Isolation (4594–4603)

Semantic dirty flags.

### Part II summary + Part III intro (4616–4812)

Roadmap for scalability chapters.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Contrast 2PC with outbox and sagas.
2. Design outbox relay with idempotent consumers.
3. Model orchestrated saga with compensations.
4. State Part III scalability patterns preview.

### worked_examples_present

**Y** — Product catalog outbox; travel saga figure; Part III Cruder architecture figures.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Outbox relay:** Crash after publish-before-delete recovery plan.
2. **Saga extension:** Add payment step with C₂ compensation.
3. **Semantic lock:** Define reader behavior on dirty records.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.13 opener | Read | 4354–4399 |
| §13.1 Outbox | Read | 4402–4481 |
| §13.2 Sagas | Read | 4485–4591 |
| §13.3 Semantic locks | Read | 4594–4603 |
| Part II summary | Read | 4616–4652 |
| Part III intro | Read | 4653–4812 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 4354–4816 only.

---

## Operator hooks

### 1. w2_systems_llm (Part II capstone + Part III intro)

Bridges dual-write (search/RAG index sync) to ch23 messaging. Part III intro sets Cruder narrative for ch14–23 worker scope.

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | High — outbox, sagas |
| **AIE RAG** | Medium — index sync = outbox port |
| **UDS ch23** | High — outbox → Kafka |

### 4. Scholia fit

- **Bundled slice:** Part III intro included by line contract (4812 end).
- **Worked examples:** Y.

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | Microservices.io outbox, Garcia-Molina sagas, Debezium |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Two full patterns + Part III roadmap |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Async atomic but not isolated | 4391–4393 | Explicit trade-off |
| Eventual consistency OK for search | 4434–4436 | Use-case dependent |

**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Ch.14–23 | Part III scalability |
| Ch.23 | Message channels detail |

---

## Provenance notes

- Claims trace to lines 4354–4816 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Transactional outbox | Events in same DB tx as domain write |
| Saga | Compensating local transaction chain |
| Semantic lock | Dirty flag during saga |
