# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 10

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch10_ingest.md |
| text_lines_read | 2573–3237 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 10 |
| chapter_title | Replication |
| page_range | [not in text export] |

---

## Scope

Chapter 10 is the **consistency foundations** capstone: **Raft state machine replication** (leader log, AppendEntries, quorum commit, log completeness for elections, backtracking sync on rejection), **consensus** as write-once register / replicated log sequence, coordination services (**etcd**, **ZooKeeper**), **consistency models** (**linearizability**, **sequential consistency**, **eventual consistency**) with read-path tradeoffs, **CAP** and **PACELC** theorems (spectrum not binary; latency vs. consistency even without partitions), and **chain replication** (head/tail topology, control plane for failures, CRAQ dirty/clean reads, data plane vs. control plane split preview Ch.22). Forward: consensus-free replication in Ch.11.

---

## Key findings

1. **Why replicate** (lines 2577–2592): Availability (failover copies), scalability/performance (concurrent reads). Challenge: keep replicas consistent under failures.

2. **State machine replication** (§10.1, lines 2595–2743): Leader broadcasts deterministic ops to followers; same ordered input ⇒ same state. Example: replicated KV store with put/get. Leader elected (Ch.9); only leader mutates state via **log** entries (operation, index, term) (Figure 10.1). Append locally → AppendEntries to followers → quorum ACK → **commit** → apply to state; followers apply only after leader commit notification. Tolerates f failures with 2f+1 nodes. Leader failure: new leader must have all committed entries (vote only for ≥ up-to-date logs; compare last term then length). AppendEntries idempotent; rejected followers trigger backward search to find divergence point and overwrite suffix. Heartbeats via empty AppendEntries.

3. **Consensus** (§10.2, lines 2746–2815): SMR solves **consensus** (agreement, validity, termination). Equivalent to **write-once register** API; Raft log = sequence of consensus instances. Practical uses: leader lease, SMR itself. Don't implement from scratch (Paxos Made Live). **etcd/ZooKeeper:** fault-tolerant hierarchical KV + watches; lease via TTL key create.

4. **Consistency models intro** (§10.3, lines 2819–2876): Replicated reads don't behave like single-threaded memory—follower lag. **Consistency models** formalize observer views.

5. **Linearizability / strong consistency** (§10.3.1, lines 2879–2918): All writes/reads via leader ⇒ single-copy illusion; ops appear atomic between invocation and completion (Figure 10.4). **Real-time** guarantee = **linearizability** (strongest single-object guarantee). Leader must confirm majority leadership before serving read (may have lost leadership)—adds read latency.

6. **Sequential consistency** (§10.3.2, lines 2921–2961): Followers may serve reads; all observers see **same operation order** but not real-time visibility (Figure 10.5). Differs from linearizability by lacking real-time bound. Producer/consumer queue example.

7. **Eventual consistency** (§10.3.3, lines 2964–2988): Client may hit any follower—may see stale then earlier state. Converges when writes stop. Hard to reason; subtle bugs; OK for approximate metrics (page view counters).

8. **CAP theorem** (§10.3.4, lines 2991–3038): On **partition:** choose **availability** (reachable followers) vs. **strong consistency** (fail unreachable reads). "Pick two" really C vs. A given partition tolerance. CAP availability definition (every request eventually responds) too strict for real systems; slow = unavailable. CAP occupies one point on **spectrum**. **PACELC:** under Partition choose A or C; **Else** choose **Latency** or C—consistency vs. latency tradeoff always. Cosmos DB, Cassandra consistency knobs. Coordination amount vs. performance; move coordination off critical path.

9. **Chain replication** (§10.4, lines 3076–3231): Chain topology: writes at **head**, propagate sequentially; **tail** commits and ACK propagates back (Figure 10.6). Reads at tail ⇒ linearizable in failure-free case. **Control plane** removes failed nodes, maintains agreed topology (itself SMR/Raft—tolerates fewer control-plane failures). Failure modes: head crash (uncommitted write invisible—client retry); tail crash (promote predecessor); middle crash (sync missing updates via sequence numbers). Replace failed nodes. Simpler failure modes than quorum—committed write seen by all chain members. Higher write latency (full chain); pipelining helps; **CRAQ** dirty/clean versioning allows distributed linearizable reads with tail confirmation (Figure 10.7). Data plane leaderless on critical path; control plane leader for reconfiguration (Ch.22 pattern). Raft more write-resilient to single slow replica (majority not full chain).

10. **Forward** (lines 3229–3231): Ch.11 explores replication without consensus.

---

## Pedagogy

### Learning objectives

1. Explain Raft log replication, commit quorum, and log-matching on recovery.
2. Relate SMR to consensus and write-once registers.
3. Distinguish linearizability, sequential consistency, and eventual consistency with read routing.
4. Interpret CAP and PACELC as spectra, not binaries.
5. Compare Raft quorum vs. chain replication failure and latency profiles.

### worked_examples_present

**Y** — Replicated KV SMR; Figures 10.1–10.7; etcd/ZK lease pattern.

### exercise_hooks

1. Trace AppendEntries rejection and log backtrack on paper.
2. Pick consistency level for shopping cart vs. view counter.
3. Calculate chain vs. quorum write latency for N=5 replicas.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.10 §10.1–10.4 | Read | lines 2573–3237 |
| Ch.11+ | Deferred | line 3238 onward |

---

## Operator hooks

**Core DDIA pairing** for w2_systems_llm (replication + CAP). Essential for database selection, RAG vector store consistency tiers, and microservice read-your-writes design.

---

## TEXTBOOK-Q1 verdict

**PASS** — Raft paper, Jepsen consistency models, CAP/PACELC primary refs; dense theory with figures.

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Ch.9 | Leader election |
| Ch.11 | Weaker models without total order |
| Ch.12 | ACID transactions |
| Ch.22 | Data/control plane split |

---

## Glossary

| Term | Definition |
|------|------------|
| State machine replication | Same ordered ops on deterministic replicas |
| Quorum | Majority required for commit |
| Linearizability | Strongest single-object real-time consistency |
| Eventual consistency | Replicas converge when writes stop |
| Chain replication | Head-to-tail write pipeline; tail reads |
| PACELC | CAP + latency/consistency tradeoff without partition |
