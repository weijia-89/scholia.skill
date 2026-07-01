# LITERATURE_INDEX — cs-ai-textbook-canon

**Session:** 2026-06-25 (w1) · 2026-06-27 (w2) · 2026-06-28 (w3 partial) · 2026-06-29 (w4 partial) · **Output mode:** reference-library · **Stakes:** L3  
**Canon:** [cs_ai_textbook_canon_decision_20260625.md](/Users/dubs/Projects/piranesi.skill/research-projects/0625-textbook-canon/returns/cs_ai_textbook_canon_decision_20260625.md)

| slug | title | track | wave | chapters ingested | role | ingest paths |
|------|-------|-------|------|-------------------|------|--------------|
| grokking_algorithms_2e_2024 | Grokking Algorithms, 2e | A | w1_foundation | 12 / 12 | core | `ingests/grokking_algorithms_2e_2024_ch{01..12}_ingest.md` |
| philosophy_software_design_2e_2021 | A Philosophy of Software Design, 2e | A | w1_foundation | 22 / 22 | core | `ingests/philosophy_software_design_2e_2021_ch{01..22}_ingest.md` |
| ai_engineering_2025 | AI Engineering | B | w1_foundation | 10 / 10 | core | `ingests/ai_engineering_2025_ch{01..10}_ingest.md` |
| hands_on_llms_2024 | Hands-On Large Language Models | B | w1_foundation | 12 / 12 | core | `ingests/hands_on_llms_2024_ch{01..12}_ingest.md` |
| understanding_distributed_systems_2022 | Understanding Distributed Systems | A | w2_systems_llm | 34 / 34 | core | `ingests/understanding_distributed_systems_2022_ch{01..34}_ingest.md` |
| ddia_2e_2026 | Designing Data-Intensive Applications, 2e | A | w2_systems_llm | 7 / 13 | core (partial) | `ingests/ddia_2e_2026_ch{01..07}_ingest.md` |
| prompt_engineering_llms_2024 | Prompt Engineering for LLMs | B | w2_systems_llm | 11 / 11 | core | `ingests/prompt_engineering_llms_2024_ch{01..11}_ingest.md` |
| nam_gen_ai_health_2025 | Generative AI in Health and Medicine (NAM) | B | w3_clinical_docs | 6 / 6 | core | `ingests/nam_gen_ai_health_2025_sec{01..06}_ingest.md` |
| simon_aliferis_healthcare_2024 | AI and ML in Health Care (Simon & Aliferis) | B | w3_clinical_docs | 12 / 12 | core (selective) | `ingests/simon_aliferis_healthcare_2024_ch{01..12}_ingest.md` |
| responsible_ai_practice_2025 | Responsible AI in Practice (Duke & Giudici) | B | w4_ops_governance | 10 / 10 | core (selective) | `ingests/responsible_ai_practice_2025_ch{01..10}_ingest.md` |

## Convergent themes

**Grokking 2e (12/12):** Track A procedural on-ramp. TEXTBOOK-Q1: ch6/10/11/12 conditional (low citation density). Export gaps: pandoc figures, ISBN 8531 vs 8538.

**Ousterhout 2e (22/22):** Complexity symptoms/causes (ch2) through tactical heuristics (deep modules, pull-complexity-down, define-errors-out, comments-first, naming/obviousness, performance tradeoffs). TEXTBOOK-Q1: ch3 conditional from batch 1; ch5–22 PASS. Recurring debate vs *Clean Code* small-function orthodoxy (ch9, ch12). MDCalc **[peripheral]** — unknown unknowns and cognitive load pattern-portable to operability.

**AI Engineering 2025 (10/10):** Framework spine — eval pipeline (ch4) → prompting/security (ch5) → RAG/agents (ch6) → finetune/PEFT (ch7) → data flywheel (ch8) → inference (ch9) → production architecture + feedback (ch10). MDCalc **[moderate]** ch4 (private eval, slice analysis), **[high relevance]** ch10 (guardrails, observability, patient-specific caching). Pair with HOTL for notebooks, not vice versa.

**Hands-On LLMs 2024 (12/12):** Procedural complement to AIE — tokens/transformers (ch1–3), classification + metrics (ch4), clustering/topics (ch5), prompting (ch6), LangChain agents/memory (ch7), dense retrieval + RAG + Ragas (ch8), multimodal CLIP/ViT (ch9), contrastive embeddings (ch10), encoder fine-tune SetFit/BERT (ch11), generative QLoRA SFT+DPO (ch12). TEXTBOOK-Q1: all 12 PASS. **Mandatory pairs:** AIE ch.6 ↔ HOTL ch.8 (RAG); AIE ch.7 ↔ HOTL ch.11–12 (finetune). MDCalc **[pattern-portable]** ch.11 NER/de-id only — not sufficient for PHI governance alone.

**Understanding Distributed Systems 2e (34/34):** Five-part distributed primer — Part I Communication (ch1–5: IPC stack, DNS, REST APIs), Part II Coordination (ch6–13: failure detection, Lamport/vector clocks, Raft, CRDTs, transactions/outbox), Part III Scalability (ch14–23: HTTP caching, CDNs, partitioning, load balancing, microservices, messaging), Part IV Resiliency (ch24–28: failure causes, redundancy, fault isolation, upstream/downstream patterns), Part V Maintainability (ch29–33: testing, CD, monitoring, observability, manageability) + epilogue ch34. TEXTBOOK-Q1: PASS all 34. **Dedup:** primary DDIA 2e pair on replication/sharding/transactions; AIE ch.10 pair on observability/resiliency (ch31–32). PDF not on disk — text-only export.

**DDIA 2e (7/13 partial):** Early-release slice only — ch1 trade-offs (OLTP/OLAP, cloud, distributed, law), ch2 NFRs, ch3 data models, ch4 **storage/index flagship for RAG** (inverted index, BM25, vector ANN/HNSW), ch5 encoding/evolution, ch6 replication, ch7 sharding. TEXTBOOK-Q1: PASS ch1–7. **Ch.8–13 deferred** — transactions, batch/stream, derived data, unbundling, consistency, consensus unavailable in text export (`[Link to Come]` in TOC). **Mandatory pairs:** ch4 ↔ AIE ch.6 + HOTL ch.8; ch6–7 ↔ UDS ch.10/16.

**Prompt Engineering for LLMs 2024 (11/11):** w2 LLM-application depth — GPT lineage + PE-as-engineering (ch1), document-mimic/tokenization (ch2), RLHF/chat/ChatML (ch3), application loop + feedforward (ch4), static/dynamic content + RAG (ch5), Valley of Meh + knapsack assembly (ch6), model control (ch7), conversational agency (ch8), LLM workflows (ch9), **eval canon** (ch10), looking ahead (ch11). TEXTBOOK-Q1: PASS all 11. **Mandatory pairs:** PE ch.10 ↔ AIE ch.4 (eval); PE ch.5–6 ↔ AIE ch.5–6 + HOTL ch.6/8 (RAG/PE). Copilot-author authority.

**NAM GenAI in Health and Medicine 2025 (6/6):** w3 governance spine — LHS + Shared Commitments (sec01), early evidence with mixed results (sec02), risk taxonomy PHI/bias/drift/hallucination (sec03), **near/mid/long-term readiness cadence** (sec04), algorithmovigilance + local EHR validation + accountability Tables 5-1–5-4 (sec05), stakeholder implementation matrices (sec06). TEXTBOOK-Q1: PASS all 6. **Mandatory pairs:** sec04 ↔ Simon ch.4 (lifecycle gates); sec05 ↔ Simon ch.10 (regulatory ELSI). MDCalc **[relevant]** all sections — pattern-portable governance; no employer claims.

**Simon & Aliferis Healthcare 2024 (12/12 selective):** w3 clinical ML rigor — formal property framework Table 2 (ch1), method appraisal labels (ch2), eight-step rigorous development workflow (ch3), nine-step clinical-grade lifecycle + data design hierarchy (ch4), evaluation + OMOP phenotypes (ch5), overfitting/overconfidence protocols (ch6), historical failures + knowledge cliff (ch7), NLP specialty cautions (ch8), dermatology imaging deployment (ch9), FDA CDS/GMLP regulatory ELSI (ch10), TRIPOD+ reporting standards (ch11), BP maturity/impact capstone (ch12). TEXTBOOK-Q1: PASS all 12. **Mandatory pairs:** ch.3 ↔ AIE ch.4 (property gates vs generative EDD); ch.4 ↔ NAM sec04; ch.10 ↔ NAM sec03+sec05. MDCalc **[high]** ch.3–4, ch.7, ch.10. Appendices A–C deferred (L45491–52845).

**Responsible AI in Practice 2025 (10/10):** w4 quantitative RAI spine — SAFE-HAI framework + regulation survey (ch1), **Rank Graduation Accuracy (RGA)** + ISO/NIST/EU AIA accuracy (ch2), **RGR** robustness + RobustBench (ch3), **RGE** explainability + Shapley Lorenz SME credit (ch4), **RGF** fairness + Simpson's paradox HMDA (ch5), **RGP** privacy + forget-set protocol (ch6), **RGS** sustainability/ESG (ch7), HCAI three-step oversight + bitcoin case (ch8), five-pillar governance + Table 9-1 (ch9), credit default **`safeaipackage`** capstone (ch10). TEXTBOOK-Q1: PASS all 10. **Mandatory pairs:** ch.1/ch.9 ↔ NAM sec05; ch.5/ch.8 ↔ Simon ch.10 ELSI; ch.2–4 ↔ AIE ch.4/ch.10. MDCalc **[relevant]** ch.2–3 eval/robustness, ch.9 governance — pattern-portable; no employer claims. Ch.10 appendix deferred (L6375+).

**Wave progress:** **136/136 partial w4** — w1: 56 (Grokking + Ousterhout + AIE + HOTL) · w2: 52 (UDS 34 + DDIA 7 + PE 11) · w3: 18 (NAM 6 + Simon 12) · w4: 10 (RAI 10). **Kästner BLOCKED** — wrong book staged; selective ingests pending operator replace. **Doc snapshots pending** — langsmith, langfuse, langgraph remain `ingest_status: none`. DDIA full-book target 13 chapters pending O'Reilly release of ch.8–13.

## Preflight (2026-06-25)

**Status:** UNBLOCKED — operator ebooks symlinked + text exported via pandoc/pdftotext.

**Wave 1 fan-out:** **complete** (56/56 ingests on disk). SYNTHESIS.md shipped at w1 closeout.

**Wave 2 fan-out:** **complete** (52/52 ingests on disk). SYNTHESIS.md extended at w2 closeout 2026-06-27. DDIA selective partial 7/13 (early release).

### Operator mismatches (action required)

| slug | issue |
|------|-------|
| `kaestner_ml_production_2025` | Staged **Andrew Kelleher** epub — NOT Christian Kästner (MIT Press 2025 OA). Replace or waive. |
| `fsa_2e_2025` | Folder title "Fundamentals of Software Architecture" — verify 2e vs 1e before indexing. |
| `responsible_ai_practice_2025` | Staged **Toju Duke** — manifest lists Duke/Giudici Springer 2025; **ingested 10/10** (verified same title). |
| `se_modern_approach_2024` | Not supplied |
| Doc snapshots | `langsmith_docs_snapshot.md`, `langfuse_docs_snapshot.md`, `langgraph_fault_tolerance_snapshot.md` — not supplied |

**DDIA:** epub metadata confirms **2e** — Kleppmann + Riccomini, ISBN 9781098119065 (ebook).
