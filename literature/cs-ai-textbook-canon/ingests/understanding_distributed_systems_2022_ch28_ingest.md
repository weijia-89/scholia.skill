# Chapter ingest — `understanding_distributed_systems_2022` · Chapter 28

**Corpus:** cs-ai-textbook-canon · **Slug:** understanding_distributed_systems_2022 · **Wave:** w2_systems_llm  
**Ingest path:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch28_ingest.md`

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **parent_book_title** | Understanding Distributed Systems |
| **authors** | Roberto Vitillo |
| **edition** | 2e |
| **chapter_number** | 28 |
| **chapter_title** | Upstream resiliency |
| **page_range** | 261–271; lines 8328–8808 |

---

## scope

**Upstream protection** when load exceeds capacity: load shedding, load leveling, rate-limiting (single- and distributed-process algorithms), and **constant work** pattern. Slice also includes **Part IV Summary** (8729–8747) and **Part V Introduction** (8750–8808) — maintainability preview.

**Boundary note:** Part V intro is bundled in this line slice per worker assignment; ch29 begins at 8809.

---

## key_findings

### Load shedding (§28.1)

- Server can't control inbound rate; crawls before OS connection queue fills (8339–8346).
- Concurrent-request counter vs threshold → **503 Service Unavailable** (8359–8368).
- Can prioritize: drop low-priority or **oldest** requests (likely to timeout anyway) (8369–8373).
- Rejection still costs TLS + partial read (8375–8380).

### Load leveling (§28.2)

- Queue/messaging decouples arrival from processing; smooths spikes (8384–8395).
- Backlog risk (ch23); combine with **autoscaling** (8397–8410).

### Rate-limiting (§28.3)

- Quotas per user/API key/IP; **429 Too Many Requests** + `Retry-After` (8415–8439).
- Pricing tiers; partial DDoS help — not full protection; economies of scale at shared gateway (8453–8469).
- vs load shedding: **local** concurrency vs **global** quota state (8471–8481).

### Single-process rate limit (§28.3.1)

- Naive per-key timestamp lists → memory heavy.
- **Fixed buckets** + **sliding window** weighted overlap (8490–8566).
- Two counters per API key for 1-min window (8564–8566).

### Distributed rate limit (§28.3.2)

- Shared store; atomic get-and-increment; batch async flushes (8570–8605).
- Store down: prefer serve on stale state (CAP tradeoff; **static stability** ch22) over hard reject (8607–8623).

### Constant work (§28.4)

- Minimize **multi-modal behavior** under overload/config churn (8626–8634).
- KV stores in data plane vs SQL hidden modes (8636–8651).
- **Antifragile** vs resilient: perform same work under high load; periodic full config dump vs per-change push (8653–8724).
- Self-healing on corruption; pairs with cellular max-size (8706–8709).

### Part IV Summary (in slice)

- "Cruel math" — failures scale with components (8731–8734).
- Production focus shifts to fault tolerance after scale adequate (8735–8741).
- Reduce blast radius; stop crack propagation (8742–8747).

### Part V Introduction (in slice)

- Maintenance dominates cost (Kernighan quote) (8753–8763).
- Testing, safe release, monitoring, observability, runtime config (8765–8808).

---

## coverage_attestation

| Check | Status |
|-------|--------|
| **Lines read** | 8328–8808 |
| **Sections** | §28.1–28.4 · Part IV Summary · Part V Introduction |
| **Figures** | 28.1–28.5 |

---

## pedagogy

### learning_objectives

1. Contrast load shedding, leveling, and rate-limiting.
2. Implement sliding-window bucket rate limiter (single process).
3. Design distributed limiter with batched updates and stale-state fallback.
4. Apply constant-work config propagation.

### worked_examples_present

**Y** — Bucket/sliding-window figures; control-plane dump pattern.

### exercise_hooks

- 429 response contract for your public API.
- Replace per-change config push with periodic full snapshot.

---

## Operator hooks

**AIE ch.9–10** caching/gateway quotas; **UDS ch22** static stability. Part IV capstone before Part V ops chapters.

**MDCalc [high]:** Per-tenant rate limits; constant-work config for validated calculator tiers.

---

## Provenance anchors

| claim-id | claim | lines |
|----------|-------|-------|
| UDS-C28-001 | Load shedding 503 | 8365–8368 |
| UDS-C28-002 | Sliding window bucket approx | 8533–8558 |
| UDS-C28-003 | Rate-limit store down → serve stale | 8607–8623 |
| UDS-C28-004 | Constant work config dump | 8684–8698 |
| UDS-C28-005 | Part IV cruel math | 8731–8747 |

---

*Ingest · scholia · ≤4500w*
