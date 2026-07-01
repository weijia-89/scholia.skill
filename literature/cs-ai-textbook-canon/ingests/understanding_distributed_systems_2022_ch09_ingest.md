# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 9

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch09_ingest.md |
| text_lines_read | 2353–2572 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 9 |
| chapter_title | Leader election |
| page_range | [not in text export] |

---

## Scope

Chapter 9 covers **leader election**: one process with special powers until relinquish or failure. Requirements: **safety** (at most one leader) and **liveness** (election completes despite failures). **Raft leader election** as state machine (follower/candidate/leader; election terms as logical timestamps; heartbeat timeout → candidacy → majority vote → leader heartbeats; split vote with random timeouts). **Practical alternative:** linearizable **compare-and-swap with TTL** lease on fault-tolerant KV store (etcd/ZooKeeper)—rarely implement Raft from scratch. **Lease pitfalls:** GC pause / network delay can expire lease before write completes—fencing via **version numbers** on conditional writes; CAS on file store or accept occasional dual leaders if idempotent. Leader = scalability bottleneck and SPOF; mitigate with **partition leaders**; minimize leader work; tolerate occasional multiple leaders. Fault-tolerant lease store requires **replication** (Ch.10).

---

## Key findings

1. **Leader election purpose** (lines 2359–2377): Privileged ops (shared resource, work assignment). Safety + liveness as general distributed algorithm properties.

2. **Raft algorithm** (§9.1, lines 2381–2441): Three states (Figure 9.1). **Terms** numbered; start as followers expecting leader heartbeats with term. Missing heartbeat → timeout → increment term, candidate, self-vote, RequestVote RPCs. Outcomes: (a) majority → leader + heartbeats; (b) discover higher-term leader → follower; (c) **split vote** → random election timeout → retry.

3. **Practical CAS lease pattern** (§9.2, lines 2444–2498): Use external fault-tolerant store with linearizable CAS + TTL instead of custom Raft. CAS(K, V_old, V_new) atomic. First successful lease holder = leader; renew until stop. Client-side expiration (DynamoDB lock client) more complex.

4. **Lease mutual exclusion failure** (lines 2500–2546): Process may lose lease before finishing critical section (preemption, clock skew, in-flight delay). Local clock check insufficient. **Version-number fencing:** read version, compute, conditional write incrementing version via CAS. Without conditional writes, accept occasional races if updates idempotent.

5. **Leader downsides** (lines 2552–2565): Bottleneck; large blast radius; partition-level leaders add complexity (common in distributed DBs).

6. **Rule of thumb** (lines 2563–2565): Minimize leader work; prepare for occasional multiple leaders.

7. **Forward link** (lines 2566–2572): Fault-tolerant lease store needs replicated state → Ch.10.

---

## Pedagogy

### Learning objectives

1. Define safety and liveness for leader election.
2. Trace Raft follower→candidate→leader flow including split vote.
3. Implement leader lock with CAS+TTL and articulate failure modes.
4. Explain version-number fencing against stale lease holders.
5. List scalability/reliability tradeoffs of centralized leadership.

### worked_examples_present

**Y** — Raft state machine Figure 9.1; Python pseudocode lease critical section; DynamoDB lock client ref.

### exercise_hooks

1. Simulate split vote with fixed vs. random election timeouts.
2. Design fencing tokens for a distributed cron job.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.9 §9.1–9.2 | Read | lines 2353–2572 |
| Ch.10+ | Deferred | line 2573 onward |

---

## Operator hooks

Raft/etcd/ZK knowledge for **any coordinated microservice**. Pairs **DDIA** leader/fencing content. LLM agent orchestrators using leader election for single-writer pipelines.

---

## TEXTBOOK-Q1 verdict

**PASS** — Raft paper + production patterns (AWS DynamoDB lock).

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Ch.10 | Replication for fault-tolerant coordination store |
| §10.3.1 | Linearizability definition |
| Ch.22 | Control plane patterns |

---

## Glossary

| Term | Definition |
|------|------------|
| Safety | Nothing bad happens (≤1 leader) |
| Liveness | Something good eventually happens (election completes) |
| Election term | Raft logical epoch number |
| Fencing | Version check preventing stale leader writes |
