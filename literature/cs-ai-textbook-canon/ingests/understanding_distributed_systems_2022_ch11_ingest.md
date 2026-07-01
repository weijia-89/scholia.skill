# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 11

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch11_ingest.md |
| text_lines_read | 3238–3811 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 11 |
| chapter_title | Coordination avoidance |
| page_range | [not in text export] |

---

## Scope

Chapter 11 pursues **coordination avoidance**: replication without **total order broadcast** (equivalent to consensus). Covers **broadcast protocols** (best-effort, reliable/eager, gossip probabilistic, total order), **CRDTs / strong eventual consistency** (semilattice merge, LWW and multi-value registers), **Dynamo-style quorum stores** (N/W/R, read-repair, Merkle-tree gossip anti-entropy), **CALM theorem** (monotonic programs ⇒ coordination-free consistent implementation; consistency of program output not linearizability), and **causal consistency** (weaker than strong, stronger than eventual; **COPS** causal+ with LWW registers and dependency dictionaries). Practical knob: Cosmos DB consistency levels. Closes Part II consistency foundations before Ch.12 transactions.

---

## Key findings

1. **SMR reframed** (lines 3242–3257): Needs fault-tolerant **total order broadcast** + deterministic update function. Total order ⇒ consensus bottleneck + unavailable under partition (CAP).

2. **Broadcast protocols** (§11.1, lines 3277–3345): Unicast TCP → multicast built on point-to-point. **Best-effort:** deliver if sender doesn't crash (Figure 11.1)—sender crash mid-send loses recipients. **Reliable:** eventual delivery to all non-faulty even if sender crashes; **eager** retransmit on first delivery (N² messages, Figure 11.2). **Gossip:** retransmit to random subset (Figure 11.3)—probabilistic, tunable. Reliable broadcast doesn't order messages; **total order broadcast** adds same order everywhere—requires consensus.

3. **CRDTs / strong eventual consistency** (§11.2, lines 3349–3513): Skip total order; any replica accepts writes; temporary divergence OK if **eventual delivery** + **convergence**. **Strong eventual consistency** adds **strong convergence** (same updates ⇒ same state immediately after apply). Requires **semilattice** states + **merge** = least upper bound (idempotent, commutative, associative)—**CRDTs**. Integer max-merge example. Reliable broadcast optional; **anti-entropy** periodic merge suffices. **LWW register:** Lamport timestamp + replica ID; merge max timestamp (Figure 11.5)—concurrent writes pick latest time (may be wrong semantically). **Multi-value register:** vector clock tags; merge = union of concurrent values returned to app (Figures 11.6). CRDTs compose (dict of registers → Dynamo-style).

4. **Dynamo-style stores** (§11.3, lines 3517–3592): Any replica accepts reads/writes; parallel write to N replicas, wait for **W** acks; read wait for **R** replies, return latest. **W+R>N** ⇒ quorum intersection (Figure 11.7) but not linearizability alone (partial write failure leaves inconsistency—needs atomic transaction Ch.12). W/R usually majority; tunable for read-heavy (small R) vs. consistency (W+R>N). W=R=1 max perf, weak consistency. **Read-repair:** client writes latest to stale replicas on read. **Replica sync:** background Merkle-tree gossip anti-entropy. Model = best-effort broadcast + anti-entropy.

5. **CALM theorem** (§11.4, lines 3595–3652): Program has consistent coordination-free distributed implementation **iff monotonic** (new inputs only refine output). Set union monotonic; variable assignment not. CRDTs monotonic. CALM **consistency** = same program output regardless of order/conflicts—not read/write linearizability ("Building on Quicksand"). LWW/MV make assignment monotonic via logical clocks.

6. **Causal consistency** (§11.5, lines 3655–3788): Eventual insufficient for happened-before ordering (photo upload then gallery reference). **Causal consistency:** agree on causally related order; concurrent ops may disagree. Strongest model still **available under partition** (provably). **COPS causal+:** LWW registers prevent permanent disagreement on concurrent ops. Client tracks **dependency dictionary** (key→version); writes carry dependencies; local replica applies immediately; async broadcast; receiver waits until dependencies committed locally (Figure 11.8). Replica failure OK; risk: commit locally before broadcast → acceptable data loss tradeoff for low-latency geo writes.

7. **Practical summary** (§11.6, lines 3791–3811): Consistency vs. availability/performance tradeoff universal; **Cosmos DB** five consistency levels as example knob.

---

## Pedagogy

### Learning objectives

1. Explain why total order broadcast requires consensus.
2. Contrast best-effort, reliable, gossip, and total-order broadcast.
3. State CRDT convergence conditions and compare LWW vs. MV registers.
4. Compute Dynamo quorum intersection and describe read-repair/anti-entropy.
5. Define CALM monotonicity and its consistency meaning.
6. Trace COPS dependency tracking for causal+ consistency.

### worked_examples_present

**Y** — Figures 11.1–11.8; integer max CRDT; COPS walkthrough; Cosmos DB reference.

### exercise_hooks

1. Choose W/R/N for read-heavy vs. write-heavy SLA.
2. Identify monotonic vs. non-monotonic ops in a feature spec.
3. Design causal dependency dict for two related API writes.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.11 §11.1–11.6 | Read | lines 3238–3811 |
| Ch.12+ | Deferred | line 3812 onward |

---

## Operator hooks

**Part II consistency capstone** for w2_systems_llm. Direct **DDIA** ch5/9 overlap (replication, CRDTs, Dynamo). Informs NoSQL/Cassandra/Cosmos selection and **AI Engineering** multi-region session stores.

---

## TEXTBOOK-Q1 verdict

**PASS** — Dynamo paper, COPS SOSP, CALM arXiv, Microsoft CRDT research video.

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Ch.10 | Strong consistency / CAP |
| Ch.12 | Atomic transactions for quorum writes |
| Ch.16 | Partitioning (COPS simplification) |

---

## Glossary

| Term | Definition |
|------|------------|
| Total order broadcast | Reliable + same delivery order everywhere |
| CRDT | Conflict-free replicated data type |
| Strong eventual consistency | Eventual delivery + strong convergence |
| Quorum | W/R replica ack thresholds |
| CALM | Consistency iff monotonic (coordination-free) |
| Causal consistency | Preserve happened-before order |
