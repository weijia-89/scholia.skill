# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 12

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch12_ingest.md |
| text_lines_read | 3812–4353 |
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
| chapter_number | 12 |
| chapter_title | Transactions |
| part | Part II — Replication (capstone) |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Chapter 12 implements **ACID transactions** for centralized and distributed data stores. Vitillo opens with microservice multi-store updates, then walks **ACID** (with explicit note that consistency in ACID is application-level, not replication consistency), **isolation anomalies** (dirty write/read, fuzzy read, phantom read), isolation levels through **serializability** and **strict serializability**, pessimistic **two-phase locking (2PL)**, optimistic **OCC**, **MVCC**, WAL-based **atomicity**, **two-phase commit (2PC)**, and **Google Spanner** as a NewSQL reference combining Paxos replication, cross-partition 2PC, MVCC+2PL, and TrueTime clock uncertainty.

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **ACID framing** (lines 3842–3896): Atomicity rolls back partial work; durability requires replication (Ch.10); author ignores confusing ACID "C" per Hellerstein.
2. **Isolation ladder** (lines 3901–3996): Stronger levels forbid more races but cost performance; default PostgreSQL is read committed; when in doubt choose strict serializability; vendor specs may diverge from formal definitions (Jepsen).
3. **2PL** (lines 3998–4026): Shared read locks, exclusive write locks, expanding/shrinking phases; strict 2PL until commit prevents cascading aborts; deadlock detection via victim abort.
4. **OCC** (lines 4027–4052): Local workspace + timestamp validation at commit; physical latches on internal structures; best for read-heavy or low-conflict writes.
5. **MVCC** (lines 4075–4103): Read-only transactions see immutable snapshots without blocking writers; write transactions use 2PL or OCC underneath.
6. **Object-level OCC** (lines 4118–4131): Version numbers + compare-and-swap for distributed conditional updates (links to leases §9.2).
7. **WAL** (lines 4141–4156): Write-ahead log enables rollback/recovery within one data store.
8. **2PC** (lines 4170–4247): Prepare then commit/abort; two points of no return; blocking if coordinator dies; uniform consensus harder than consensus; replicate roles via Raft for resilience.
9. **Spanner** (lines 4260–4353): Partitioned Paxos groups; leader lock manager; cross-partition 2PC with replicated logs; TrueTime uncertainty intervals + commit wait; CockroachDB uses hybrid logical clocks.

---

## Section digest (anchored)

### §12.1 ACID (3842–3896)

Money-transfer motivates transactions; ACID properties defined; durability needs replication.

### §12.2 Isolation (3901–3996)

Four race conditions; Figure 12.1 isolation level ladder; strict serializability adds real-time order.

### §12.2.1 Concurrency control (3998–4131)

2PL vs OCC vs MVCC trade-offs; Pavlo course recommended for implementation depth.

### §12.3 Atomicity (4134–4168)

WAL single-store; cross-bank transfer needs distributed atomicity.

### §12.3.1 Two-phase commit (4170–4247)

Figure 12.2 prepare/commit; mixed reputation (Stonebraker blog).

### §12.4 NewSQL / Spanner (4251–4353)

Figure 12.3 three partitions; TrueTime <10ms uncertainty typical.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Define ACID and map isolation levels to forbidden anomalies.
2. Compare 2PL, OCC, MVCC for workload fit.
3. Explain 2PC blocking and replication mitigations.
4. Describe Spanner's Paxos + 2PC + MVCC + clocks stack.

### worked_examples_present

**Y** — Bank transfer, 2PC figure, Spanner multi-partition diagram, CAS version example.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Isolation picker:** Given read/write ratio, pick isolation level and justify.
2. **2PC failure:** Trace participant state when coordinator crashes after all prepare OK.
3. **Clock compare:** TrueTime wait vs CockroachDB HLC for external consistency.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.12 opener | Read | 3812–3833 |
| §12.1 ACID | Read | 3842–3896 |
| §12.2 Isolation | Read | 3901–3996 |
| §12.2.1 Concurrency | Read | 3998–4131 |
| §12.3–12.3.1 Atomicity/2PC | Read | 4134–4247 |
| §12.4 Spanner | Read | 4251–4353 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 3812–4353 only.

---

## Operator hooks

### 1. w2_systems_llm (Part II — Replication (capstone))

Transaction capstone linking Part II consistency to ch19 NewSQL and **ddia_2e_2026** transaction chapters. Essential for microservice multi-store updates (pairs ch13 async patterns).

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | High — isolation, 2PC, Spanner; dedup at SYNTHESIS |
| **UDS ch13** | High — 2PC blocking motivates async txs |
| **Philosophy SD ch10** | Low — exception/rollback philosophy |

### 4. Scholia fit

- **Worked examples:** Y (figures + Spanner walkthrough).
- **Chapter boundary:** Clean end before Ch.13.

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | Jepsen, Pavlo 15-445, Spanner OSDI'12, Stonebraker 2PC blog |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Multiple figures + Spanner architecture |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Ignore ACID Consistency vs consistency models | 3862–3873 | Author explicit |
| Default strict serializability | 3968–3972 | Perf cost |
| 2PC move-on reputation | 4217–4226 | Async alt in ch13 |

**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Ch.13 | Asynchronous transactions |
| Ch.19 | NewSQL callback |
| DDIA 2e | Transaction isolation depth |

---

## Provenance notes

- Claims trace to lines 3812–4353 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Strict serializability | Serializability + real-time ordering |
| 2PL | Two-phase locking |
| 2PC | Two-phase commit |
| TrueTime | Spanner clock uncertainty intervals |
