# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 19

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch19_ingest.md |
| text_lines_read | 5852–6192 |
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
| chapter_number | 19 |
| chapter_title | Data storage |
| part | Part III — Scalability |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Scale relational DB via leader-follower replication, partitioning limits, NoSQL access-pattern modeling (DynamoDB single-table, GSI), NewSQL trend (CockroachDB, Spanner callback).

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **Replication** (5865–5941): Leader WAL → followers; read replicas + LB; async fast but lossy; sync fragile; mixed sync follower for failover; scales reads not writes.
2. **Partitioning pain** (5954–5970): App-layer sharding + 2PC + replication combo is daunting.
3. **NoSQL** (5998–6032): Bigtable/Dynamo lineage; relaxed consistency; denormalized key-value/documents.
4. **DynamoDB** (6056–6144): PK/SK; 3 replicas; W=2 ack; single-table entity mixing (Jon Snow orders); GSI eventually consistent.
5. **Access patterns upfront** (6146–6157): NoSQL less flexible than SQL when misused.
6. **NewSQL** (6159–6192): CockroachDB, Spanner; consistency over partition availability.

---

## Section digest (anchored)

### §19.1 Replication (5865–5941)

Figure 19.1 leader-follower.

### §19.2 Partitioning (5954–5970)

App-layer complexity.

### §19.3 NoSQL/DynamoDB (5998–6192)

Single-table example; NewSQL.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Configure leader-follower for read scale.
2. Explain app-layer partitioning cost.
3. Model DynamoDB for dominant queries.
4. Contrast NoSQL/NewSQL/RDB.

### worked_examples_present

**Y** — Jon Snow orders table; RDS failover; DeBrie DynamoDB Book ref.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Sync policy:** 1 sync + N async for RPO target.
2. **DynamoDB model:** PK/SK + GSI for second query.
3. **Store picker:** NoSQL vs NewSQL vs RDB.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| §19.1 | Read | 5865–5941 |
| §19.2 | Read | 5954–5970 |
| §19.3 | Read | 5998–6192 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 5852–6192 only.

---

## Operator hooks

### 1. w2_systems_llm (Part III — Scalability)

Primary w2 data-layer ingest; pair **ddia_2e_2026** replication/partitioning; links ch12.4 Spanner.

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | High — primary overlap |
| **UDS ch12** | High — Spanner/NewSQL |
| **AIE** | Low — vector store different layer |

### 4. Scholia fit

- **Worked examples:** Y (concrete DynamoDB rows).

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | Bigtable, DynamoDB re:Invent, DeBrie, Pavlo NewSQL |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | DynamoDB + replication depth |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|
| NoSQL flexibility myth | 6146–6151 | Author inversion |
| NewSQL availability cost | 6164–6178 | Pavlo contested |

**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Ch.20 | Cache DB reads |
| DDIA 2e | SYNTHESIS dedup |

---

## Provenance notes

- Claims trace to lines 5852–6192 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Read replica | Follower serving reads |
| Single-table design | Multiple entities same PK |
| NewSQL | Distributed SQL/ACID |
