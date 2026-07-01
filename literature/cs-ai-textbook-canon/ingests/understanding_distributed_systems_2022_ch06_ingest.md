# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 6

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch06_ingest.md |
| text_lines_read | 1952–2064 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 6 |
| chapter_title | System models |
| page_range | [not in text export] |

---

## Scope

Chapter 6 introduces **formal system models** for reasoning about distributed algorithms by abstracting implementation. Three dimensions: **communication links** (fair-loss, reliable, authenticated reliable—with TCP/TLS as real implementations), **process failures** (Byzantine/arbitrary up to f of 3f+1 tolerance, crash-recovery, crash-stop), and **timing** (synchronous, asynchronous, partially synchronous). Book default: **fair-loss links + crash-recovery processes + partial synchrony**. Emphasizes models are wrong but useful; question assumptions against production reality.

---

## Key findings

1. **Communication link models** (lines 1963–1985): **Fair-loss:** messages may be lost/duplicated; retransmit eventually delivers. **Reliable:** exactly-once delivery; implement via dedup on fair-loss. **Authenticated reliable:** reliable + sender authentication. TCP ≈ reliable; TLS ≈ authentication layer.

2. **Process failure models** (lines 1987–2011): **Arbitrary/Byzantine:** any deviation; tolerates up to ⌊(n-1)/3⌋ faulty (Lamport); for safety-critical/untrusted parties (aircraft, Bitcoin)—**out of book scope**. **Crash-recovery:** correct algorithm but crash loses in-memory state; **book default**. **Crash-stop:** no recovery after crash; models hardware/permanent failure; simpler algorithms.

3. **Timing models** (lines 2013–2040): **Synchronous:** bounded message/operation time—unrealistic (GC pauses, network delays). **Asynchronous:** unbounded time—many problems unsolvable (infinite stall). **Partially synchronous:** mostly synchronous—representative of real systems.

4. **Default model** (lines 2041–2051): Fair-loss + crash-recovery + partial synchrony for remainder. Deeper theory: Cachin et al. "Introduction to Reliable and Secure Distributed Programming."

5. **Models vs. reality** (lines 2048–2051): "All models are wrong"—operators must imagine breakage modes when assumptions fail.

---

## Pedagogy

### Learning objectives

1. Define fair-loss, reliable, and authenticated reliable links.
2. Contrast Byzantine, crash-recovery, and crash-stop process models.
3. Explain why asynchronous models limit solvable problems.
4. State the book's default system model triple.

### worked_examples_present

**N** — Conceptual taxonomy only; maps to prior TCP/TLS chapters.

### exercise_hooks

1. Map a production outage to which model assumption broke.
2. Decide whether Byzantine model applies to a given multi-tenant SaaS.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.6 System models (full) | Read | lines 1952–2064 |
| Ch.7+ | Deferred | line 2065 onward |

---

## Operator hooks

Theoretical foundation for **Part II Coordination**; aligns with **DDIA** fault-tolerance framing. Essential before Raft/CAP chapters.

---

## TEXTBOOK-Q1 verdict

**PASS** — Classic distributed-systems taxonomy with primary refs (Lamport Byzantine, Chandra failure detectors).

---

## Glossary

| Term | Definition |
|------|------------|
| Fair-loss link | May lose/duplicate; eventual delivery if sender retries |
| Crash-recovery | Process may crash and restart losing RAM state |
| Partial synchrony | System synchronous most of the time |
| Byzantine fault | Arbitrary process misbehavior |
