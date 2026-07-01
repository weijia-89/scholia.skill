# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 2

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus] |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch02_ingest.md |
| text_lines_read | 733–978 |
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
| chapter_number | 2 |
| chapter_title | Reliable links |
| page_range | [not in text export] |

---

## Scope

Chapter 2 explains how **TCP** builds a reliable byte-stream channel on top of unreliable **IP** (BGP routing, no delivery guarantee). Covers reliability mechanisms (segments, sequence numbers, ACKs, retransmit timers, checksums), **connection lifecycle** (three-way handshake, TIME_WAIT, connection pools), **flow control** (receive buffer, receiver-advertised window), **congestion control** (congestion window, slow start, loss reaction, bandwidth-delay product formula), and **UDP** as a lean alternative for custom protocols (multiplayer games example). Recurring theme: RTT and geographic proximity affect cold-start and bandwidth utilization.

---

## Key findings

1. **IP addressing and routing** (lines 738–749): IPv6 128-bit space; routers use local tables (BGP builds/propagates routes). IP does not guarantee delivery—overloaded routers drop packets.

2. **TCP reliability illusion** (§2.1, lines 770–778): Byte stream partitioned into numbered **segments**; each sent segment ACKed; timeout → retransmit; receiver **checksum** verifies integrity.

3. **Connection lifecycle** (§2.2, lines 782–846): OS manages socket state (opening/established/closing simplification). Server must listen before connect. **Three-way handshake** (SYN → SYN/ACK → ACK + first data) costs full RTT before application data (Figure 2.1). Low RTT reduces cold-start penalty → servers near clients. Close involves multiple RTTs; keep-alive avoids repeated handshake tax. **TIME_WAIT** (minutes) prevents delayed segments attaching to new connections; rapid open/close exhausts socket limit → **connection pools**.

4. **Flow control** (§2.3, lines 850–880): Sender must not overwhelm receiver **receive buffer** (Figure 2.2); buffer size advertised in ACK headers (Figure 2.3). Analogous to connection-level rate limiting (cf. §28.3).

5. **Congestion control** (§2.4, lines 884–939): **Congestion window** caps unacked bytes in flight. New connections start at default window, grow exponentially per ACK until limit (Figure 2.4)—cannot use full bandwidth immediately. Packet loss → **congestion avoidance** shrinks window. **Bandwidth = WinSize / RTT** (bandwidth-delay product); TCP optimizes window, not RTT → again, proximity matters.

6. **UDP and custom protocols** (§2.5, lines 942–978): Dropping TCP reliability/stability yields **UDP**—connectionless datagrams, no sequencing/ACK/flow/congestion control. Used to bootstrap custom protocols (HTTP/3 later). **Multiplayer games:** stale snapshots not worth retransmitting; TCP retransmission would harm real-time experience.

---

## Section digest (anchored)

### Opening (lines 733–767)

IP + BGP for routing; TCP for reliability and stability patterns.

### §2.1–2.5

Progression from segment-level reliability → connection economics → receiver protection → network protection → when to abandon TCP guarantees.

---

## Pedagogy

### Learning objectives

1. Explain what IP guarantees vs. what TCP adds.
2. Walk through the three-way handshake and articulate cold-start cost.
3. Describe TIME_WAIT and why connection pools exist.
4. Contrast flow control and congestion control.
5. State the bandwidth-delay product relationship.
6. Identify workloads where UDP outperforms TCP.

### worked_examples_present

**Y** — Multiplayer game UDP vs. TCP (lines 969–978); Figures 2.1–2.4.

### exercise_hooks

1. Estimate max throughput given RTT=50ms and window=64KB.
2. Diagnose "cannot open new connections" under high churn (TIME_WAIT).
3. Decide TCP vs. UDP for a telemetry stream vs. file transfer.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.2 Reliable links §2.1–2.5 | Read | lines 733–978 |
| Ch.3+ | Deferred | line 979 onward |

**Attestation:** Lines 733–978 only; boundary before Chapter 3 at line 979.

---

## Operator hooks

### 1. Foundation layer

Core **Part I Communication** mechanics. Essential for debugging latency, connection exhaustion, and "network is fine but app slow" incidents. Pairs with **DDIA** networking assumptions and **AI Engineering** tool-call timeout design.

### 2. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | Less TCP depth; Vitillo fills transport layer |
| **SE Modern Approach** | Possible networking chapter overlap |

### 3. Scholia fit

**Clean chapter boundary.** Procedural transport content with RFC anchors.

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result |
|-----------|--------|
| Edition currency | **PASS** |
| Author authority | **PASS** |
| Citation density | **PASS** (RFC 793, 4271, 768, CUBIC paper) |
| Contested claims | **PASS** — bandwidth formula idealized |
| Worked examples | **PASS** |

**Verdict:** **PASS**

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Ch.3 | TLS on TCP |
| Ch.5 / HTTP 3 | UDP-based HTTP |
| §28.3 | Service-level rate limiting |

---

## Glossary

| Term | Definition |
|------|------------|
| Segment | TCP discrete packet of byte stream |
| RTT | Round-trip time |
| Congestion window | Max unacked bytes in flight |
| TIME_WAIT | Post-close wait state for stray segments |
| UDP | Connectionless datagram transport |
