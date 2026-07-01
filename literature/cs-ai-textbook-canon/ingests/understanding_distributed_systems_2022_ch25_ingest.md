# Chapter ingest — `understanding_distributed_systems_2022` · Chapter 25

**Corpus:** cs-ai-textbook-canon · **Slug:** understanding_distributed_systems_2022 · **Wave:** w2_systems_llm  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch25_ingest.md`

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **parent_book_title** | Understanding Distributed Systems |
| **authors** | Roberto Vitillo |
| **edition** | 2e (Version 2.0.0, March 2022) |
| **chapter_number** | 25 |
| **chapter_title** | Redundancy |
| **page_range** | 243–246; lines 7789–7918 |

---

## scope

Chapter 25 presents **redundancy** as the first-line defense against failures: replicated functionality/state so surviving nodes absorb faults. Introduces **Brooker's four prerequisites** for redundancy that actually improves availability; applies them to stateless (LB + health checks) vs stateful (replication) services; then **§25.1 Correlation** — AZs, regions, sync vs async cross-region replication.

**Out of scope:** Tactical patterns (timeouts, circuit breakers) — ch27–28.

---

## key_findings

### Brooker prerequisites `[verified]`

1. Redundancy complexity must not cost more availability than it adds.
2. Reliable healthy/unhealthy detection.
3. Degraded-mode operation.
4. Return to fully redundant mode (replace removed nodes).

### Stateless example

- LB masks node crashes via redundant pool; health checks (ch18) critical — one bad server of ten → 10% failed requests until detected (7824–7831).
- Degraded mode: remaining capacity must absorb removed nodes; must **add replacements** or pool shrinks to unsustainable (7833–7839).

### Stateful

- State replication far harder; Part III replication chapters prerequisite (7841–7845).

### Correlation (§25.1)

- Redundancy useless if nodes fail together (**correlated failures**).
- Single-DC outage correlates all servers; **multi-AZ** within region (AWS/Azure) — low enough latency for sync/partial-sync replication (Raft, chain replication) (7866–7884).
- **Multi-region**: catastrophic region loss → duplicate full stack; **async** cross-region replication due to latency; global DNS LB (7886–7892).
- Region-wide disaster probability extremely low — justify multi-region on compliance (Schrems II / EU data residency) more often than pure availability (7894–7911).

---

## coverage_attestation

| Check | Status |
|-------|--------|
| **Source file** | `literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt` |
| **Lines read** | 7789–7918 |
| **Sections** | Intro · Brooker prerequisites · §25.1 Correlation |
| **Figures** | 25.1 multi-region architecture |

---

## pedagogy

### learning_objectives

1. State Brooker's four redundancy prerequisites.
2. Contrast stateless LB redundancy vs stateful replication complexity.
3. Explain **failure correlation** and why multi-DC matters.
4. Choose sync vs async replication by AZ vs region latency.

### worked_examples_present

**Y** — Stateless pool + health checks; AZ vs region topology (Fig. 25.1).

### exercise_hooks

- Capacity model: N nodes, one fails — can remainder absorb 1/(N-1) load increase?
- Document correlation risks for your deployment (shared DC, shared dependency).

---

## Operator hooks

Pairs with **DDIA ch.5–6** replication and **AIE ch.10** gateway/fallback. Multi-region async ties to **UDS ch10** replication latency tradeoffs.

**MDCalc [medium]:** EU data residency (Schrems) as multi-region driver.

---

## TEXTBOOK-Q1

**PASS** — Brooker blog + Netflix multi-region cite; practical cloud framing.

---

## Provenance anchors

| claim-id | claim | lines |
|----------|-------|-------|
| UDS-C25-001 | Four redundancy prerequisites | 7801–7807 |
| UDS-C25-002 | Health-check detection delay → availability drop | 7827–7831 |
| UDS-C25-003 | Correlated DC outage | 7855–7862 |
| UDS-C25-004 | Cross-region async replication | 7890–7892 |

---

*Ingest · scholia · ≤4500w*
