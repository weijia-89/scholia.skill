# Chapter ingest — Designing Data-Intensive Applications 2e, Chapter 3

| Field | Value |
|-------|-------|
| slug | ddia_2e_2026 |
| source_type | textbook_chapter |
| pdf_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/ddia_2e_2026.pdf |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/ddia_2e_2026.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/ddia_2e_2026_ch03_ingest.md |

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
| chapter_number | 3 |
| chapter_title | Data Models and Query Languages |
| page_range | not embedded in text export [unverified] |

## scope

Chapter 3 compares **data models and query languages** across the application-to-storage stack (lines 3157–5477). Major arcs:

1. **Declarative vs imperative** — SQL/Cypher/SPARQL/Datalog vs application loops; query optimization.

2. **Relational vs document** — Normalization, joins, many-to-one; schema-on-read; polymorphism; ID references; relational-document hybrids (JSON in SQL).

3. **Graph models** — Property graphs, Cypher; triple-stores/RDF/SPARQL; GraphQL limits and adoption costs; Datalog recursion.

4. **Event sourcing and CQRS** — Append-only events; materialized views; advantages and operational complexity.

5. **Dataframes/matrices** — Pandas/R, columnar analytics, TileDB/ArcticDB; science/finance time series.

Bridge to Ch. 4 storage engines explicit. [verified, lines 3157–5477]

## key_findings

1. **Data model centrality** — Shapes code and problem cognition; layered abstractions from app → DB → bytes → hardware. [verified, 3177–3213]

2. **Model comparison goal** — No one-size-fits-all; expressiveness vs convenience trade-offs. [verified, 3215–3221]

3. **Declarative queries** — Specify what not how; optimizer chooses plans; MapReduce contrast for large scans. [verified, 3223–3245]

4. **Relational foundations** — Codds model; SQL ubiquity; normalization reduces duplication. [verified, 3247+]

5. **Document model** — JSON aggregates; schema flexibility; poor join support; update locality. [verified, 3500+]

6. **Many-to-one relationships** — Weak in pure document without references; drives hybrid SQL+JSON. [verified, 3600+ range]

7. **Schema-on-read** — Not schemaless; implicit schema at read time; migration still needed. [verified, 3842+]

8. **Graph property model** — Vertices/edges; Cypher pattern matching; index-free adjacency concept. [verified, 4025+]

9. **RDF/SPARQL** — Triple stores; semantic web baggage; good for data integration. [verified, 4200+ range]

10. **Graph in SQL** — Recursive CTEs; performance limits vs native graph DBs. [verified, 4298+]

11. **GraphQL** — Client-driven selection; N+1 and backend complexity; not a database model. [verified, 4736–4858]

12. **Event sourcing** — Immutable event log as source of truth; snapshots/projections; auditability. [verified, 4858+]

13. **CQRS** — Separate read/write models; pairs with event sourcing; consistency challenges. [verified, 4940+]

14. **Dataframes** — Column-oriented in-memory analytics; vectorized ops; bridge to ML pipelines. [verified, 5033+]

15. **Query language spectrum** — Declarative SQL family vs imperative application code boundaries. [verified, summary 5122+]

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Opener + layered models | read | 3157–3221 |
| Declarative Query Languages | read | 3223–3246 |
| Relational vs Document | read | 3247–4024 |
| Graph-Like Data Models | read | 4025–4735 |
| GraphQL | read | 4736–4857 |
| Event Sourcing and CQRS | read | 4858–5032 |
| Dataframes, Matrices, Arrays | read | 5033–5121 |
| Summary + references | read | 5122–5477 |
| Chapter 4 opener | **deferred** | 5478+ |
| Chapters 8–13 | **unavailable** | early release |

- **Lines read:** 3157–5477
- **wrong_file_flag:** false

## pedagogy

### learning_objectives

- Map application concepts to relational, document, and graph representations
- Choose normalization vs denormalization with join/update trade-offs
- Explain declarative query benefits and optimizer role
- Contrast event sourcing/CQRS with CRUD state storage
- Position dataframes for analytics/ML adjacent workloads

### worked_examples_present

**Y** — LinkedIn/Facebook/Twitter schema comparisons, Cypher patterns, GraphQL query example, event-sourced account balance.

### exercise_hooks

| ID | Prompt summary | Operator extension | Anchor |
|----|----------------|-------------------|--------|
| 3.DM-1 | User/org many-to-one | Model same domain in SQL vs JSON; count update sites | 3247–3600 |
| 3.DM-2 | Graph vs SQL traversal | Same 3-hop query in Cypher vs recursive CTE | 4025–4350 |
| 3.DM-3 | Event sourcing ledger | Rebuild balance from events; compare to mutable row | 4858+ |
| 3.DM-4 | GraphQL N+1 audit | Trace resolver fan-out on nested query | 4736+ |

## Operator hooks

### 1. Foundation layer (w2_systems_llm)

Chapter 3 is the **data modeling spine** before storage (Ch. 4) and distribution (Ch. 6–7):

- **Document vs relational** — shapes RAG metadata schemas and tool-record shapes
- **Graph** — knowledge-graph RAG adjacency
- **Event sourcing** — audit logs for agent actions

### 2. MDCalc alignment

**[none]** — Pattern-portable: immutable audit trails (event sourcing), schema evolution for regulated fields.

### 3. Redundancy

| Overlap with | Relationship |
|--------------|--------------|
| `ai_engineering_2025` | AIE uses JSON/docs in prompts; DDIA explains underlying model trade-offs |
| `hands_on_llms_2024` | HOTL Ch. 7 LangChain data structures; DDIA deeper on persistence models |
| `philosophy_software_design_2e_2021` | Ousterhout Ch. 5–6 deep classes vs DDIA persistence model choice |
| `understanding_distributed_systems_2022` | Minimal overlap; UDS not model-focused |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | Strong multi-paradigm comparisons |
| Citation density | High (Codd, semantic web, CQRS patterns) |
| Child-skill potential | `scholia.relational-vs-document-rag-schema` |

## TEXTBOOK-Q1 quality gate

| Criterion | Result |
|-----------|--------|
| Edition currency | **PASS** |
| Author authority | **PASS** |
| Citation density | **PASS** |
| Contested claims | **PASS** — GraphQL criticism cited [Bessey 2024] |
| Worked examples | **PASS** |

**TEXTBOOK-Q1 verdict:** **PASS**

## Glossary (chapter-local)

| Term | Definition per text |
|------|---------------------|
| Declarative query | Specify result shape/conditions; DB plans execution |
| Normalization | Factor repeated data into referenced tables |
| Schema-on-read | Structure interpreted at read time |
| Event sourcing | State changes stored as append-only events |
| CQRS | Command/query responsibility segregation |

## Reciprocal index pointers

- Forward: Ch. 4 storage (5478+)
- Ch. 8–13 **[unavailable]**
