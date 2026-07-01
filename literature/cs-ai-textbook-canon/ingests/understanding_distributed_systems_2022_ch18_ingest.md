# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 18

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch18_ingest.md |
| text_lines_read | 5423–5851 |
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
| chapter_number | 18 |
| chapter_title | Network load balancing |
| part | Part III — Scalability |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Scale stateless app tier: availability math, LB algorithms (power-of-two choices), service discovery, health checks, watchdog; DNS, L4 TCP, L7 HTTP load balancing; sidecar service mesh.

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **Stateless scale-out** (5428–5453): Push state to DB + blob; horizontal scaling.
2. **Availability product** (5468–5499): 1−∏(1−aᵢ); nines add with caveats (LB delay, correlated failures, remaining pool overload).
3. **Algorithms** (5504–5533): RR, consistent hash, load-aware; delayed metrics oscillate; power-of-two random choices works well.
4. **Service discovery** (5542–5558): etcd/Zookeeper TTL registration; autoscaling.
5. **Health checks** (5560–5642): Passive vs active; smart LB ignores mass false failures; drain rolling deploy; watchdog restart on gray failures.
6. **DNS LB** (5646–5682): RR DNS weak failure detection; good for global multi-DC.
7. **L4 LB** (5685–5768): VIP NAT; connection hashing; direct server return; Anycast+ECMP scale-out.
8. **L7 LB** (5779–5838): HTTP demux; sticky session hotspots; TLS terminate; L4 fronts L7; sidecar mesh trade-offs.

---

## Section digest (anchored)

### Core LB features (5423–5642)

Availability math, discovery, health.

### §18.1 DNS (5646–5682)

Global multi-DC.

### §18.2 L4 (5685–5768)

Figure 18.2.

### §18.3 L7 + mesh (5779–5838)

Sticky sessions; Envoy sidecar.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Compute N-server availability.
2. Compare DNS vs L4 vs L7 LB.
3. Design health checks avoiding empty pool.
4. Evaluate mesh vs centralized LB.

### worked_examples_present

**Y** — 99%+99%→99.99%; power-of-two; AWS NLB/Azure LB refs.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **Nines math:** 3×99.9% with correlation adjustment.
2. **Health policy:** Thresholds avoiding pool wipe.
3. **Sticky hotspot:** Session affinity failure scenario.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.18 opener–health | Read | 5423–5642 |
| §18.1 DNS | Read | 5646–5682 |
| §18.2 L4 | Read | 5685–5768 |
| §18.3 L7 | Read | 5779–5838 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 5423–5851 only.

---

## Operator hooks

### 1. w2_systems_llm (Part III — Scalability)

App-tier scale for Cruder; read replicas ch19 behind LB; API gateway ch21 as L7.

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | Medium |
| **Philosophy SD ch7** | Low — layering vs sidecar sprawl |

### 4. Scholia fit

- **Worked examples:** Y (quantitative availability + layer tour).

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | AWS Well-Architected, power-of-two blog, Envoy |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Richest LB chapter |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Independent failure rates | 5487–5488 | Correlated failures common |
| Random beats delayed load metrics | 5527–5529 | Counter-intuitive |

**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Ch.19 | DB replicas behind LB |
| Ch.21 | API gateway |
| Ch.22 | Control/data plane split |

---

## Provenance notes

- Claims trace to lines 5423–5851 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| VIP | Virtual IP on L4 LB |
| Power of two choices | Pick 2 random servers; route to lighter |
| Service mesh | Sidecar LB per client |
