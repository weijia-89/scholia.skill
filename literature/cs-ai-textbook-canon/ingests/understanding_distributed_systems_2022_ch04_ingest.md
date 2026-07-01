# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 4

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch04_ingest.md |
| text_lines_read | 1154–1280 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 4 |
| chapter_title | Discovery |
| page_range | [not in text export] |

---

## Scope

Chapter 4 covers **DNS** as the internet's name-to-IP discovery layer: a **distributed, hierarchical, eventually consistent key-value store**. Walks through browser resolution of `www.example.com` (local cache → resolver → root NS → TLD NS → authoritative NS; Figure 4.1). Discusses DNS-over-TLS, **TTL** tradeoffs, cache misbehavior, DNS as **single point of failure** (Dyn 2016 DDoS), and **static stability** idea (serve stale on NS failure vs. treating TTL as hard expiry). Forward reference to resiliency part.

---

## Key findings

1. **DNS purpose** (lines 1159–1173): Before TLS connect, client must discover IP. DNS = phone book; hierarchical distributed eventually consistent KV store.

2. **Resolution steps** (lines 1175–1216): (1) Browser cache hit or ISP resolver; (2) resolver cache or iterative query; (3) root NS maps TLD; (4) TLD NS maps domain; (5) authoritative NS returns hostname IP. Subdomains may require extra hop.

3. **Security evolution** (lines 1218–1221): Original DNS plain-text over UDP; industry moved to **DNS over TLS** (DoT) to prevent snooping.

4. **Caching and TTL** (lines 1223–1255): Worst-case multi-hop slow; caching at browser/OS/resolver essential. **TTL** defines record validity; clients may ignore TTL. **Tradeoff:** long TTL → slow propagation of changes; short TTL → higher NS load and latency. Small TTL + NS outage → more clients impacted.

5. **Failure and static stability** (lines 1257–1273): DNS outage prevents clients reaching application (massive outages possible). **Static stability** proposal: serve **stale** entries when NS unreachable rather than failing—entries rarely change; more robust than strict TTL expiry. Forward to resiliency part.

---

## Pedagogy

### Learning objectives

1. Recite iterative DNS resolution from browser to authoritative NS.
2. Explain TTL tradeoffs for operators changing records.
3. Describe why DNS is an availability bottleneck.
4. Define static stability in DNS context.

### worked_examples_present

**Y** — Full `www.example.com` walkthrough (Figure 4.1).

### exercise_hooks

1. Plan a zero-downtime DNS migration with TTL strategy.
2. Incident postmortem template for authoritative NS failure.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.4 Discovery (full) | Read | lines 1154–1280 |
| Ch.5+ | Deferred | line 1281 onward |

---

## Operator hooks

First **eventual consistency** taste in UDS (line 1164); foreshadows Ch.10–11 consistency models. Pair **DDIA** service discovery chapters. Critical for any multi-service/LLM gateway deployment.

---

## TEXTBOOK-Q1 verdict

**PASS**

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Ch.10 | Consistency models |
| Part IV | Resiliency / static stability |
| Ch.5 | HTTP after DNS+TLS |

---

## Glossary

| Term | Definition |
|------|------------|
| DNS | Domain Name System |
| TTL | Time to live for cached DNS records |
| Authoritative NS | Server holding canonical records for zone |
| Static stability | Continue serving stale data when dependency impaired |
