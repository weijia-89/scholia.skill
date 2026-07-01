# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 7

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch07_ingest.md |
| text_lines_read | 2065–2118 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 7 |
| chapter_title | Failure detection |
| page_range | [not in text export] |

---

## Scope

Short chapter on **failure detection** when client-server communication fails ambiguously: slow server vs. crash vs. network loss (Figure 7.1). Clients use **timeouts** after no response—cannot build a **perfect** failure detector (too short → false positives; too long → wasted wait). **Proactive** detection via **pings** (request/response with timeout, continued probing for recovery) and **heartbeats** (receiver times out missing beats). Used when frequent interaction requires immediate action; otherwise detect-on-communicate suffices.

---

## Key findings

1. **Ambiguous silence** (lines 2069–2088): No response could mean slow, crashed, or undelivered message. Client configures timeout; on fire, marks server unavailable (error or retry). **Perfect failure detection impossible**—timeout tuning is heuristic.

2. **Pings** (lines 2103–2108): Periodic request expecting timely response; timeout → unavailable; keep pinging for recovery detection.

3. **Heartbeats** (lines 2109–2113): Sender periodically signals liveness; receiver timeout on missing heartbeat → unavailable; resumes when heartbeats return.

4. **When to use** (lines 2114–2118): Pings/heartbeats for tight coupling needing fast reaction; lazy detection at communication time otherwise sufficient.

---

## Pedagogy

### Learning objectives

1. Explain why timeout-based failure detection is inherently imperfect.
2. Contrast ping-based vs. heartbeat-based proactive detection.
3. Choose detection strategy based on interaction frequency and blast radius.

### worked_examples_present

**Y** — Figure 7.1 ambiguity diagram; ping/heartbeat definitions.

### exercise_hooks

1. Set timeout policy given p99 latency SLA and false-positive budget.
2. Compare health checks vs. heartbeats in your orchestrator.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.7 Failure detection (full) | Read | lines 2065–2118 |
| Ch.8+ | Deferred | line 2119 onward |

---

## Operator hooks

Foundation for **Raft leader election** (Ch.9 heartbeats) and **load balancer** health checks. Pair **DDIA** unreliability of networks.

---

## TEXTBOOK-Q1 verdict

**PASS** — Concise procedural chapter.

---

## Glossary

| Term | Definition |
|------|------------|
| Failure detector | Mechanism inferring process unavailability |
| Ping | Active probe expecting response |
| Heartbeat | Passive liveness signal from sender |
