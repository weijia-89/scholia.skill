# Chapter ingest — Designing Data-Intensive Applications 2e, Chapter 5

| Field | Value |
|-------|-------|
| slug | ddia_2e_2026 |
| source_type | textbook_chapter |
| pdf_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/ddia_2e_2026.pdf |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ddia_2e_2026.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ddia_2e_2026_ch05_ingest.md |

## Bibliographic metadata

| Field | Value |
|-------|-------|
| title | Designing Data-Intensive Applications |
| authors | Martin Kleppmann, Chris Riccomini |
| edition | 2nd Edition Early Release (2026) |
| ISBN_print | 9781098119058 |
| ISBN_electronic | 9781098119065 |
| publisher | O'Reilly Media |
| parent_book_title | Designing Data-Intensive Applications, 2nd Edition |
| chapter_number | 5 |
| chapter_title | Encoding and Evolution |
| page_range | not embedded in text export [unverified] |

## scope

Chapter 5 covers **data encoding, schema evolution, and inter-process dataflow** (lines 7529–9167). Major arcs:

1. **Compatibility** — Backward/forward compatibility under rolling upgrades; old/new code and data coexistence.

2. **Encoding formats** — JSON/XML; binary formats (Thrift, Protocol Buffers, Avro); schema evolution rules; field tags; compatibility modes.

3. **Modes of dataflow** — Via databases; via service calls (REST, RPC, gRPC); asynchronous message passing (Kafka, event-driven architectures, actor frameworks).

4. **Trade-offs** — Human-readability vs compactness; schema rigidity vs flexibility; API versioning.

Connects Ch. 2 evolvability to Ch. 3 models and distributed pipelines in later chapters. [verified, lines 7529–9167]

## key_findings

1. **Change is inevitable** — Features and schemas evolve; evolvability goal from Ch. 2. [verified, 7549–7553]

2. **Schema migration vs schemaless** — Relational ALTER vs document mixed-version documents. [verified, 7560–7567]

3. **Rolling upgrades** — Server staged rollout; client update lag; simultaneous format versions. [verified, 7575–7586]

4. **Backward compatibility** — New code reads old data (usually tractable). [verified, 7590–7600]

5. **Forward compatibility** — Old code ignores new fields (harder; unknown-field stripping). [verified, 7594–7608]

6. **Encoding vs in-memory structures** — Translation to bytes for storage/network; endianness and precision issues. [verified, 7620+]

7. **JSON/XML limits** — Ambiguous numbers; schema optional; verbose. [verified, 7700+ range]

8. **Protocol Buffers / Thrift** — Field tags; required/optional; code generation; compact binary. [verified, 7800+ range]

9. **Avro** — Writer/reader schemas; schema registry pattern; RPC data model. [verified, 8000+ range]

10. **Schema evolution rules** — Add fields with defaults; don't reuse tag numbers; compatibility testing. [verified, 8100+ range]

11. **Database as dataflow** — Polyglot persistence; derived data refresh; batch vs stream to warehouse. [verified, 8263+]

12. **REST vs RPC** — Resource orientation vs action procedures; versioning; HATEOAS limits. [verified, 8400+ range]

13. **gRPC** — HTTP/2, protobuf, streaming; performance vs browser limits. [verified, 8600+ range]

14. **Message brokers** — Kafka log abstraction; consumer groups; at-least-once delivery. [verified, 8700+ range]

15. **Event-driven architecture** — Choreography vs orchestration; idempotency needs. [verified, 8819+]

16. **Actor frameworks** — Location-transparent messaging; distributed state caveats. [verified, 8893+]

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Opener + compatibility | read | 7529–7627 |
| Formats for Encoding Data | read | 7628–8262 |
| Modes of Dataflow | read | 8263–8928 |
| Summary + references | read | 8929–9167 |
| Chapter 6 opener | **deferred** | 9168+ |
| Chapters 8–13 | **unavailable** | early release |

- **Lines read:** 7529–9167
- **wrong_file_flag:** false

## pedagogy

### learning_objectives

- Define backward/forward compatibility in rolling deploys
- Compare JSON, Protobuf, Thrift, Avro evolution characteristics
- Choose REST vs RPC vs message-passing integration style
- Plan schema changes without breaking mixed-version clients

### worked_examples_present

**Y** — Record encoding byte layouts (Example 5-2 Protobuf), Avro writer/reader schema resolution, contact-info JSON evolution.

### exercise_hooks

| ID | Prompt summary | Operator extension | Anchor |
|----|----------------|-------------------|--------|
| 5.ENC-1 | Add optional field | Rolling deploy: old reader + new writer | 7575–7608 |
| 5.ENC-2 | Protobuf size | Encode same record JSON vs protobuf | 7913+ |
| 5.ENC-3 | Avro compatibility | Break test by reusing field tag | 8100+ |
| 5.FLOW-1 | Kafka consumer lag | Simulate at-least-once duplicate handling | 8700+ |

## Operator hooks

### 1. Foundation layer (w2_systems_llm)

Chapter 5 bridges **application evolution** to **RAG pipeline contracts**:

- **Embedding schema/versioning** — chunk metadata fields evolve like Avro schemas
- **Tool/API payloads** — protobuf/JSON choices for agent function calling
- **Event logs** — agent trace streams via Kafka patterns

### 2. MDCalc alignment

**[none]** — Pattern-portable: forward-compatible API versioning for clinical integrations.

### 3. Redundancy

| Overlap with | Relationship |
|--------------|--------------|
| `philosophy_software_design_2e_2021` | Ousterhout Ch. 19 information hiding, Ch. 13 comments/contracts; DDIA wire-format depth |
| `ai_engineering_2025` | AIE structured outputs; DDIA encoding layer |
| `understanding_distributed_systems_2022` | UDS messaging basics; DDIA format detail |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | Strong byte-level encodings |
| Child-skill potential | `scholia.schema-forward-compat-checklist` |

## TEXTBOOK-Q1 quality gate

**PASS** — classic DDIA chapter; dense citations (Protobuf, Avro papers, Kafka).

## Glossary (chapter-local)

| Term | Definition per text |
|------|---------------------|
| Backward compatibility | New code reads old data |
| Forward compatibility | Old code reads new data |
| Schema evolution | Changing record structure over time |
| RPC | Remote procedure call |

## Reciprocal index pointers

- Prerequisites: Ch. 2 evolvability, Ch. 3 models
- Forward: Ch. 6 replication logs (9168+)
- Ch. 8–13 **[unavailable]**
