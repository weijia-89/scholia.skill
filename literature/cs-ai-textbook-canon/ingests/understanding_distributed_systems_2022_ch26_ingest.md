# Chapter ingest — `understanding_distributed_systems_2022` · Chapter 26

**Corpus:** cs-ai-textbook-canon · **Slug:** understanding_distributed_systems_2022 · **Wave:** w2_systems_llm  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch26_ingest.md`

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **parent_book_title** | Understanding Distributed Systems |
| **authors** | Roberto Vitillo |
| **edition** | 2e |
| **chapter_number** | 26 |
| **chapter_title** | Fault isolation |
| **page_range** | 247–251; lines 7919–8044 |

---

## scope

Redundancy fails for **highly correlated** faults (same bug everywhere, poison-pill user). Chapter covers **blast-radius reduction** via partitioning: bulkhead pattern, **shuffle sharding**, and **cellular architecture** (full-stack cells + gateway routing). Links to ch16 partitioning for scale.

---

## key_findings

### Poison pills & noisy neighbors

- User malformed requests crash all replicas if requests land anywhere — redundancy doesn't help (7928–7934).
- Resource-heavy user degrades everyone (**noisy neighbor**) (7936–7938).
- **Partition by user** limits blast radius (7940–7950).

### Bulkhead pattern

- Ship-hull compartments metaphor; partition limits fault spread (7963–7966).
- Example: 6 instances, 3 partitions → bad user affects ~33% (7952–7956).

### Shuffle sharding (§26.1)

- **Virtual partitions** = random permanent subsets of instances.
- 6 instances, groups of 2 → C(6,2)=15 virtual partitions vs 3 physical — much lower collision probability (7986–7998).
- Partitions overlap (Fig. 26.2); combine with LB removing bad instances + client retries (8001–8003).

### Cellular architecture (§26.2)

- Partition **entire stack** (LB, compute, storage) into independent **cells**; gateway routes to correct cell (8014–8019).
- Azure Storage example: stamp = cell (8021–8024).
- **Max cell capacity** enables predictable benchmarking; scale by adding cells not enlarging cells (8039–8044).

---

## coverage_attestation

| Check | Status |
|-------|--------|
| **Lines read** | 7919–8044 |
| **Sections** | Intro · §26.1 Shuffle sharding · §26.2 Cellular architecture |
| **Figures** | 26.1–26.3 |

---

## pedagogy

### learning_objectives

1. Explain when redundancy fails (correlated software bugs, poison pills).
2. Apply bulkhead partitioning to cap blast radius.
3. Compute shuffle-shard collision reduction vs physical partitions.
4. Describe cellular architecture and capacity ceiling benefits.

### worked_examples_present

**Y** — 6-instance partition math; Azure Storage cells.

### exercise_hooks

- Design shuffle-shard assignment for your service instance count.
- Define max cell size and add-cell trigger.

---

## Operator hooks

**AIE ch.10** multi-tenant guardrails; **DDIA** sharding. Cellular pattern matches large SaaS ops (New Relic cite).

**MDCalc [low-medium]:** Tenant isolation for hospital-system partitions.

---

## Provenance anchors

| claim-id | claim | lines |
|----------|-------|-------|
| UDS-C26-001 | Poison pill defeats redundancy | 7928–7934 |
| UDS-C26-002 | Shuffle sharding 15 vs 3 partitions | 7986–7998 |
| UDS-C26-003 | Cell max size → predictable benchmark | 8039–8044 |

---

*Ingest · scholia · ≤4500w*
