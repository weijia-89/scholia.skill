# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 5

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch05_ingest.md |
| text_lines_read | 1281–1951 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| chapter_number | 5 (+ Part I Summary + Part II Coordination intro bundled) |
| chapter_title | APIs |
| page_range | [not in text export] |

---

## Scope

Chapter 5 closes **Part I Communication** with **request-response APIs**: direct vs. indirect (message broker) communication; serialization (JSON vs. Protocol Buffers); sync vs. async (async/await); HTTP/gRPC split (public HTTP, internal gRPC). Deep **RESTful HTTP** walkthrough: message structure, HTTP/1.1 HOL blocking vs. HTTP/2 multiplexing vs. HTTP/3/QUIC on UDP, **resources/URLs**, **CRUD methods** (safe/idempotent matrix), **status codes** (2xx–5xx retry semantics), **OpenAPI** IDL example, **API evolution** (endpoint and schema compatibility, URL versioning), and **idempotency** (PUT/DELETE inherent; POST via idempotency keys, ACID atomicity, external-call complexity → Ch.13 sagas). Multi-client idempotency edge case (delete between retries; least astonishment).

**Bundled in slice:** Part I **Summary** (lines 1863–1882): respect for network complexity (sockets, certs, DNS, congestion, idempotency); "fastest network call is one you don't make." Part II **Coordination intro** (lines 1886–1951): goal of coherent distributed illusion; roadmap Ch.6–13 (models, failure detection, time, leader election, replication/CAP/PACELC, coordination avoidance, ACID, async transactions/sagas).

---

## Key findings

1. **API adapter role** (lines 1286–1306): Server adapter translates IPC messages to business logic (Figure 1.2). **Direct** communication requires both processes up; **indirect** via message broker decouples availability (Ch.23).

2. **Request-response mechanics** (lines 1308–1361): Language-agnostic serialization; JSON human-readable vs. Protobuf performant. Sync blocks threads; async via callbacks/async-await. gRPC internal; HTTP external (browser-friendly). **REST** principles: stateless requests; cacheable responses labeled.

3. **HTTP protocol** (§5.1, lines 1375–1446): Request/response messages (start line, headers, body). Stateless—all context in request. HTTPS = HTTP over TLS. HTTP/1.1 persistent connections but **head-of-line blocking** (serialized transactions); pipelining insufficient. Mitigation: multiple connections (resource cost). HTTP/2 binary multiplexing; HTTP/3 on UDP avoids TCP HOL blocking all streams on single packet loss. Book illustrates with HTTP/1.1 text format.

4. **Resources and URLs** (§5.2, lines 1449–1518): Resources (physical/abstract); URL locates resource (`/products?sort=price` example). Nested resources (`/products/42/reviews`) increase complexity—balance nesting depth. JSON representation example; content negotiation via headers.

5. **Request methods** (§5.3, lines 1522–1556): POST/GET/PUT/DELETE CRUD mapping for catalog service. **Safe** = no visible side effects, cacheable. **Idempotent** = repeated execution same effect. Matrix: POST neither; GET both; PUT idempotent not safe; DELETE idempotent not safe.

6. **Status codes** (§5.4, lines 1559–1605): 2xx success (200 OK); 3xx redirect (301); 4xx client errors (400/401/403/404)—don't retry; 5xx server errors—retry may succeed (500/502/503).

7. **OpenAPI** (§5.5, lines 1608–1707): IDL generates docs, server adapters, client SDKs. YAML spec excerpt for `/products` GET with ProductItem schema.

8. **Evolution** (§5.6, lines 1711–1743): Breaking changes at endpoint level (path rename) or message level (schema type change). URL versioning (`/v1/products/`) for breaks; prefer backward-compatible evolution.

9. **Idempotency** (§5.7, lines 1747–1861): Timeout ambiguity → client retries. PUT/DELETE inherently idempotent. POST create needs **idempotency key** (header, e.g. Stripe) stored in DB; atomic with resource creation via ACID when same DB; external calls need coordination (Ch.13). Crash after logging key but before execution blocks retries—needs atomic handler. Duplicate should return **same response** as first success (201 Created), not error. Multi-client scenario: B deletes between A's retry—original creation response less surprising (least astonishment; AWS builders library).

10. **Part I Summary** (lines 1863–1882): Network calls hide complexity; production failures from sockets, TLS expiry, DNS, congestion, non-idempotent retries.

11. **Part II intro roadmap** (lines 1893–1951): Ch.6 system models; Ch.7 failure detection; Ch.8 time/clocks; Ch.9 leader election; Ch.10 replication + CAP/PACELC; Ch.11 weaker consistency; Ch.12 ACID; Ch.13 async transactions (microservices-relevant).

---

## Pedagogy

### Learning objectives

1. Design RESTful resource URLs and CRUD method mapping.
2. Classify HTTP methods by safety and idempotency.
3. Choose retry behavior from status code class.
4. Implement POST idempotency with keys and transactional logging.
5. Contrast HTTP/1.1, HTTP/2, and HTTP/3 transport tradeoffs.
6. Articulate Part II coordination themes from intro roadmap.

### worked_examples_present

**Y** — Catalog service API throughout; OpenAPI YAML; HTTP transaction Figure 5.1; idempotency scenarios.

### exercise_hooks

1. OpenAPI spec for one internal microservice endpoint.
2. Idempotency key schema + TTL purge policy design.
3. Classify production 4xx/5xx for retry vs. no-retry runbook.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Ch.5 §5.1–5.7 | Read | lines 1281–1861 |
| Part I Summary | Read | lines 1863–1882 |
| Part II Coordination intro | Read | lines 1886–1951 |
| Ch.6+ | Deferred | line 1952 onward |

---

## Operator hooks

**IPC capstone** for w2_systems_llm Part I. Idempotency section directly supports **AI Engineering** tool-call retry design and **DDIA** ch4-style API contracts. Part II intro sets up consistency foundations for pairing with **DDIA** ch7–9.

---

## TEXTBOOK-Q1 verdict

**PASS** — Procedural HTTP/API chapter with OpenAPI example and industry refs (Stripe, Kleppmann schema evolution).

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Ch.13.2 | Sagas for external idempotency |
| Ch.2–4 | TCP/TLS/DNS under HTTP |
| Ch.6–13 | Part II coordination |

---

## Glossary

| Term | Definition |
|------|------------|
| REST | Representational state transfer design principles |
| HOL blocking | Head-of-line blocking serializing responses |
| Idempotency key | Unique client token for deduplicating POST |
| OpenAPI | IDL/spec for REST HTTP APIs |
