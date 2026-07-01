# SYNTHESIS — cs-ai-textbook-canon (w1_foundation + w2_systems_llm + w3_clinical_docs partial + w4_ops_governance partial closeout)

**Session:** 2026-06-25 (w1) · 2026-06-27 (w2) · 2026-06-28 (w3 partial) · 2026-06-29 (w4 partial) · **Output mode:** reference-library · **Stakes:** L3  
**Corpus root:** `literature/cs-ai-textbook-canon/`  
**Canon:** [cs_ai_textbook_canon_decision_20260625.md](/Users/dubs/Projects/piranesi.skill/research-projects/0625-textbook-canon/returns/cs_ai_textbook_canon_decision_20260625.md)

---

## Session bet

| Field | Value |
|-------|-------|
| Corpus slug | cs-ai-textbook-canon |
| Wave completed | **w1_foundation** (4 books, 56 ingests) + **w2_systems_llm** (3 books, 52 ingests) + **w3_clinical_docs partial** (2 sources, 18 ingests; doc snapshots BLOCKED) + **w4_ops_governance partial** (1 source, 10 ingests; Kästner BLOCKED) |
| Output mode | reference-library — `LITERATURE_INDEX.md` + chapter ingests + this file |
| Fan-out | Mandatory chapter sub-agents; parent never monolith-read textbooks |
| Iron laws | Amnesiac corpus; DDIA 2e only; Kästner preferred MLOps depth; no employer-stack claims |

**Wave-1 ingest tally:** 12 Grokking + 22 Ousterhout + 10 AIE + 12 Hands-On LLMs = **56/56 complete**.

**Wave-2 ingest tally:** 7 DDIA 2e (early-release partial) + 34 UDS + 11 Prompt Engineering = **52/52 complete**.

**Wave-3 ingest tally:** 6 NAM sections + 12 Simon selective chapters = **18/18 complete**.

**Wave-4 ingest tally:** 10 Responsible AI in Practice chapters = **10/10 complete** (Kästner selective chapters **0** — wrong book staged).

**Cumulative:** **136/136 w1+w2+w3 partial+w4 partial chapter/section ingests on disk** (doc snapshots + Kästner not counted — operator blockers pending).

---

## w1_foundation stack (four books)

| Track | Slug | Role in stack | Chapters |
|-------|------|---------------|----------|
| A | `grokking_algorithms_2e_2024` | Algorithms + asymptotic bedrock | 12/12 |
| A | `philosophy_software_design_2e_2021` | Complexity philosophy + design heuristics | 22/22 |
| B | `ai_engineering_2025` | AI-engineering **framework spine** (eval → prompt → RAG/agents → finetune → data → inference → architecture) | 10/10 |
| B | `hands_on_llms_2024` | **Procedural complement** — Hugging Face, LangChain, notebooks | 12/12 |

**Read-order heuristic (not strict):** Grokking ch.1–2 (search, sort, big-O) → Ousterhout ch.1–3 (complexity vocabulary) → parallel Track B: AIE ch.1–4 (landscape + eval) with HOTL ch.1–4 (tokens, transformers, classification) → AIE ch.5–6 + HOTL ch.6–8 (prompting, agents, RAG) → AIE ch.7–8 + HOTL ch.11–12 (finetune) → AIE ch.9–10 (inference + production architecture capstone).

Load-bearing anchors:

- Grokking ch.1 establishes binary search + big-O worst-case default — `ingests/grokking_algorithms_2e_2024_ch01_ingest.md` (Operator hooks: Foundation layer).
- Ousterhout ch.2 defines three symptoms / two causes of complexity — `ingests/philosophy_software_design_2e_2021_ch02_ingest.md`.
- AIE ch.4 is the eval canon (EDD, private benchmarks, leaderboard skepticism) — `ingests/ai_engineering_2025_ch04_ingest.md`.
- AIE ch.10 is the systems-integration capstone — `ingests/ai_engineering_2025_ch10_ingest.md`.
- HOTL ch.8 is the procedural RAG spine — `ingests/hands_on_llms_2024_ch08_ingest.md`.

---

## Foundation layer (prose diagram)

```
[L0  asymptotics + search intuition]
        grokking_algorithms_2e_2024 (ch1–12)
              │
              ▼
[L1  structural complexity + module design]
        philosophy_software_design_2e_2021 (ch1–22)
              │
              ├──────────────────────────────┐
              ▼                              ▼
[L2a  AI framework spine]          [L2b  executable LLM stack]
        ai_engineering_2025                 hands_on_llms_2024
        ch1 landscape                       ch1–2 tokens/embeddings
        ch2–3 model + eval metrics          ch3 transformer internals
        ch4 EDD + eval pipeline ◄──────────► ch4 classification metrics
        ch5 prompting + security            ch5–6 prompting + sampling
        ch6 RAG + agents ◄─────────────────► ch7–8 agents + dense/RAG pipeline
        ch7 finetune decision + PEFT ◄──────► ch11–12 encoder + generative FT
        ch8 data flywheel                     ch9–10 multimodal + contrastive embed
        ch9 inference economics
        ch10 architecture + feedback flywheel
              │
              ▼
[L3  w2_systems_llm — ingested 2026-06-27]
        understanding_distributed_systems_2022 (34/34) · ddia_2e_2026 (7/13 early release) · prompt_engineering_llms_2024 (11/11)
              │
              ▼
[L4  w3_clinical_docs — partial 2026-06-28]
        nam_gen_ai_health_2025 (6/6 sections) · simon_aliferis_healthcare_2024 (12/12 selective)
        langsmith/langfuse/langgraph snapshots — BLOCKED (operator export)
              │
              ▼
[L5  w4_ops_governance — partial 2026-06-29]
        responsible_ai_practice_2025 (10/10) — SAFE-HAI + Rank Graduation metrics + governance + case study
        kaestner_ml_production_2025 — BLOCKED (Andrew Kelleher ≠ Christian Kästner)
```

**Cross-track coupling:** Track A supplies *why* complexity and coupling hurt (change amplification, unknown unknowns); Track B supplies *what to build* (RAG, agents, eval, finetune) and HOTL supplies *how to run it in code*. Ousterhout's "pull complexity downward" (ch index via `philosophy_software_design_2e_2021_ch22_ingest.md`) ports to adapter boundaries and deep modules in agent tool layers — pattern only, no production claims.

---

## w2_systems_llm stack (three books)

| Track | Slug | Role in stack | Chapters |
|-------|------|---------------|----------|
| A | `understanding_distributed_systems_2022` | **Distributed-systems primer** — communication → coordination → scalability → resiliency → maintainability | 34/34 |
| A | `ddia_2e_2026` | **Data-systems depth** — trade-offs, NFRs, storage/index internals, replication, sharding (early-release slice) | 7/13 |
| B | `prompt_engineering_llms_2024` | **LLM application + PE depth** — chat/RLHF, app loop, RAG content/assembly, tools/agency, eval | 11/11 |

**Read-order heuristic (not strict):** UDS ch.1–5 (IPC + APIs) → DDIA ch.1–2 (architectural trade-offs + NFRs) → parallel PE ch.1–3 (PE framing + chat) with DDIA ch.3–4 (data models + storage/index) → PE ch.4–6 (app loop + RAG assembly) paired with AIE ch.6 + HOTL ch.8 (w1 RAG pair) and DDIA ch.4 (index internals) → UDS ch.10–11 + DDIA ch.6–7 (replication + sharding) → PE ch.7–10 (model control, agency, workflows, eval) → UDS ch.24–32 (failure + observability) as ops capstone.

Load-bearing anchors:

- UDS ch.1 defines five challenge domains and ports-and-adapters anatomy — `ingests/understanding_distributed_systems_2022_ch01_ingest.md`.
- DDIA ch.4 is the **RAG index canon** (inverted index, BM25 lineage, vector ANN/HNSW) — `ingests/ddia_2e_2026_ch04_ingest.md`.
- DDIA ch.6–7 cover replication and sharding trade-offs — `ingests/ddia_2e_2026_ch06_ingest.md`, `ingests/ddia_2e_2026_ch07_ingest.md`.
- PE ch.4 introduces the application loop + feedforward pipeline — `ingests/prompt_engineering_llms_2024_ch04_ingest.md`.
- PE ch.5–6 own static/dynamic content + prompt assembly (Valley of Meh, sandwich, knapsack crafters) — `ingests/prompt_engineering_llms_2024_ch05_ingest.md`, `ingests/prompt_engineering_llms_2024_ch06_ingest.md`.
- PE ch.10 is the w2 eval canon (SOMA, example suites) — `ingests/prompt_engineering_llms_2024_ch10_ingest.md`.

**DDIA ch.8–13 deferred:** Early-release text export terminates at line 12807 after ch.7 (Sharding). TOC lists ch.8–13 as `[Link to Come]` — transactions, batch/stream processing, derived data, unbundling, consistency, consensus not yet available. Re-ingest when O'Reilly ships full 2e text; until then w2 DDIA coverage is **selective partial (7/13)** per manifest `ingest_scope: selective`.

---

## Redundancy map

### AIE ↔ Hands-On LLMs (RAG + finetune)

| Topic | Canonical framework (AIE) | Canonical procedural (HOTL) | Dedup rule |
|-------|---------------------------|----------------------------|------------|
| **RAG architecture** | `ai_engineering_2025_ch06_ingest.md` — retriever/generator split, hybrid RRF, agent planning debates, long-context vs RAG | `hands_on_llms_2024_ch08_ingest.md` — dense→rerank→RAG, Cohere/LangChain/FAISS notebooks, Ragas eval | **AIE for design; HOTL for reproduction.** Do not duplicate AIE architecture prose in HOTL-derived skills. |
| **Agents + memory** | AIE ch.6 — tool taxonomy, ReAct/Reflexion, failure modes | HOTL ch.7 — LangChain chains, ReAct tutorial | HOTL owns notebook paths; AIE owns failure-mode checklists. |
| **Finetune / PEFT** | `ai_engineering_2025_ch07_ingest.md` — when-to-finetune, LoRA/QLoRA theory, "form vs facts", Ovadia RAG-vs-FT tables | `hands_on_llms_2024_ch12_ingest.md` — TinyLlama QLoRA SFT + DPO; ch.11 encoder SetFit/BERT | **Mandatory pair:** AIE ch.7 before HOTL ch.12 for go/no-go; HOTL ch.11 for encoder path only. |
| **Embeddings** | AIE ch.3–6 embedding framing | HOTL ch.10 contrastive training | HOTL owns training code; AIE owns retrieval architecture. |
| **Eval** | AIE ch.4 EDD + private eval | HOTL ch.4 sklearn metrics + ch.8 MAP/nDCG/Ragas | AIE for pipeline design; HOTL for metric implementation drills. |

Contested claims preserved in ingests (not smoothed): RAG-vs-finetune heuristic (`ai_engineering_2025_ch07_ingest.md`); RAG does not eliminate hallucinations (`hands_on_llms_2024_ch08_ingest.md`).

### Grokking ↔ Ousterhout

| Dimension | Grokking 2e | Philosophy of Software Design 2e |
|-----------|-------------|----------------------------------|
| **Core question** | *How fast / scalable is this algorithm?* | *How hard is this system to understand and change?* |
| **Overlap** | Low direct content overlap — `grokking_algorithms_2e_2024_ch01_ingest.md` Operator hooks: Redundancy table marks Ousterhout as tangential on asymptotics | `philosophy_software_design_2e_2021_ch02_ingest.md`: Grokking listed as **complementary not redundant** |
| **Shared meta-theme** | Worst-case / growth-rate thinking → latency SLO intuition | Unknown unknowns + cognitive load → operability and silent-failure risk |
| **Dedup rule** | **Do not substitute** Grokking for Ousterhout or vice versa. Grokking is the designated intro-complexity + algorithms slot; Ousterhout is the designated design-philosophy slot. CLRS optional for formal depth. |

### Other w1 redundancies (indexed, not re-derived)

| Pair | Notes | Source |
|------|-------|--------|
| AIE ↔ DMLS 2022 | Slice eval overlap; point to DMLS for ML-system slicing, AIE ch.4 for LLM eval | `ai_engineering_2025_ch04_ingest.md` |
| HOTL ↔ `prompt_engineering_llms_2024` | RAG prompt templates; HOTL integrated tutorial wins for w1 | `hands_on_llms_2024_ch08_ingest.md` |
| AIE ch.10 internal | Guardrails/observability/feedback — cross-link ch.5–9 ingests, do not re-derive | `ai_engineering_2025_ch10_ingest.md` |

### w2 ↔ w1 (AIE RAG, HOTL, Ousterhout)

| Topic | w1 canonical | w2 canonical | Dedup rule |
|-------|--------------|--------------|------------|
| **RAG retrieval stack** | AIE ch.6 architecture + HOTL ch.8 FAISS/LangChain notebooks | DDIA ch.4 index internals (BM25, HNSW, OLTP/OLAP); PE ch.5 lexical+neural RAG + FAISS walkthrough | **DDIA for why indexes work; AIE for production RAG design; HOTL for notebooks; PE for content sourcing + assembly.** |
| **Prompt engineering** | AIE ch.5 defensive PE + versioning; HOTL ch.6 Phi-3 labs | PE ch.1–6 app loop, chat/RLHF, Valley of Meh, knapsack crafters | **AIE owns security spine; PE owns application loop + assembly algorithms; HOTL owns runnable exercises.** |
| **Eval pipelines** | AIE ch.4 EDD + private benchmarks | PE ch.10 SOMA/example suites, offline eval tree | **Mandatory pair:** AIE ch.4 for criteria buckets; PE ch.10 for Copilot-first example suites. |
| **Agents + tools** | AIE ch.6 tool taxonomy; HOTL ch.7 LangChain ReAct | PE ch.8 conversational agency; PE ch.9 LLM workflows | AIE for failure modes; PE for agency/workflow patterns; HOTL for notebook paths. |
| **Complexity / coupling** | Ousterhout ch.2 symptoms + ch.22 deep modules | UDS ch.1 five domains; DDIA ch.1 trade-off lens | **Ousterhout for design vocabulary; UDS for distributed failure/time/consensus; DDIA for data-system trade-offs.** Do not substitute one for another. |
| **Observability + resiliency** | AIE ch.10 guardrails/feedback flywheel | UDS ch.24–32 failure causes, redundancy, monitoring/observability | UDS for distributed ops patterns; AIE ch.10 for LLM-specific production architecture. |

### DDIA ↔ UDS (w2 internal)

| Topic | DDIA 2e (ch1–7) | UDS 2e | Dedup rule |
|-------|-----------------|--------|------------|
| **Replication** | DDIA ch.6 — leader/follower, sync/async, quorum | UDS ch.10 — Raft SMR, CAP/PACELC | DDIA for storage-engine replication detail; UDS for consensus protocol walkthrough. |
| **Partitioning / sharding** | DDIA ch.7 — sharding strategies, rebalancing | UDS ch.16 — partitioning + consistent hashing | Pair for scale-out RAG/vector stores; DDIA owns rebalancing semantics. |
| **Transactions / consistency** | ch.8–13 **deferred** (not in export) | UDS ch.12–13 — transactions, async/outbox | UDS fills gap until DDIA ch.8+ ships. |
| **Messaging / async** | ch.8–13 **deferred** | UDS ch.23 — brokers, DLQ, exactly-once illusion | UDS owns until DDIA batch/stream chapters available. |
| **Storage / indexes** | DDIA ch.4 — flagship for RAG | UDS ch.19 — data storage overview | **DDIA owns index internals**; UDS light touch. |

Contested claims preserved in ingests (not smoothed): approximate ANN recall risk (DDIA ch.4); exactly-once messaging illusion (UDS ch.23); PE lost-in-middle vs HOTL ch.6 exercise overlap flagged per ingest.

---

## w3_clinical_docs stack (partial — textbooks complete, doc snapshots BLOCKED)

| Track | Slug | Role in stack | Units |
|-------|------|---------------|-------|
| B | `nam_gen_ai_health_2025` | **Governance + readiness cadence** — LHS framing, risk taxonomy, near/mid/long-term deployment tiers, algorithmovigilance, stakeholder RACI | 6/6 sections |
| B | `simon_aliferis_healthcare_2024` | **Clinical ML rigor** — formal properties, eight-step development workflow, nine-step clinical-grade lifecycle, regulatory ELSI, reporting standards | 12/12 selective |
| B | `langsmith_docs_snapshot` | Trace + eval tooling (outside-input) | **BLOCKED** |
| B | `langfuse_docs_snapshot` | Observability + eval tooling (outside-input) | **BLOCKED** |
| B | `langgraph_fault_tolerance_snapshot` | Agent fault tolerance (outside-input) | **BLOCKED** |

**Read-order heuristic (not strict):** NAM sec01 (vocabulary + LHS/Shared Commitments) → Simon ch.1 (formal property framework) → Simon ch.2 (method appraisal) → Simon ch.3 (eight-step rigorous development) → parallel NAM sec02–03 (opportunities + risks) with Simon ch.4 (clinical-grade lifecycle + data design) → NAM sec04 (readiness cadence tiers) → Simon ch.5–6 (evaluation + overfitting) → Simon ch.7 (historical failures) → Simon ch.8–9 (NLP + imaging specialties) → NAM sec05–06 (path forward + stakeholder matrices) with Simon ch.10–11 (regulatory ELSI + TRIPOD reporting) → Simon ch.12 (BP taxonomy capstone).

Load-bearing anchors:

- NAM sec01 establishes GenAI/LLM vocabulary and hybrid governance (frameworks, diverse training data, clinician certification, local validation) — `ingests/nam_gen_ai_health_2025_sec01_ingest.md`.
- NAM sec04 is the **readiness cadence canon** — near/mid/long-term risk tiers (ambient scribe → precision CDS → autonomous triage) — `ingests/nam_gen_ai_health_2025_sec04_ingest.md`.
- NAM sec05 owns algorithmovigilance, drift monitoring, local EHR validation, Table 5-4 accountability — `ingests/nam_gen_ai_health_2025_sec05_ingest.md`.
- Simon ch.1 Table 2 eleven property dimensions + heuristic-vs-formal continuum — `ingests/simon_aliferis_healthcare_2024_ch01_ingest.md`.
- Simon ch.3 eight-step development workflow (problem definition → controlled testing → benchmarks) — `ingests/simon_aliferis_healthcare_2024_ch03_ingest.md`.
- Simon ch.4 nine-step clinical-grade lifecycle + RNBNFCV + Shapley critique — `ingests/simon_aliferis_healthcare_2024_ch04_ingest.md`.
- Simon ch.10 FDA CDS / GMLP regulatory spine — `ingests/simon_aliferis_healthcare_2024_ch10_ingest.md`.
- Simon ch.12 BP maturity/impact taxonomy capstone — `ingests/simon_aliferis_healthcare_2024_ch12_ingest.md`.

### NAM governance cadence

NAM frames trustworthy GenAI deployment through **Learning Health System (LHS)** alignment and **Shared Commitments** (accessible, affordable, transparent, accountable, adaptive). Operational governance spans six sections:

| Section | Governance function | Load-bearing content |
|---------|---------------------|----------------------|
| sec01 | Vocabulary + institutional north star | LHS, Shared Commitments, hybrid governance checklist |
| sec02 | Evidence realism | Mixed preliminary results; adoption outpacing evidence (ambient scribe) |
| sec03 | Risk taxonomy | Hallucination, PHI leakage, bias/drift, NIST AI RMF alignment |
| sec04 | **Deployment cadence** | Near/mid/long-term tiers; risk gates before tier promotion |
| sec05 | **Operational RACI** | Algorithmovigilance, local EHR validation (OMB M-24-10), Tables 5-1–5-4 |
| sec06 | Stakeholder matrices | Provider/payer/regulator/patient implementation strategies |

**Cadence rule:** NAM sec04 tiers sequence *when* to deploy; NAM sec05 defines *who validates what* post-deploy; Simon ch.4 defines *how* to validate clinical-grade models. Pair sec04 + ch.4 before enabling any clinical-adjacent agent feature.

### Simon clinical ML rigor

Simon/Aliferis supplies the **property-based appraisal spine** that w1–w2 engineering texts lack:

| Layer | Chapters | Rigor contribution |
|-------|----------|-------------------|
| Formal foundations | ch.1–2 | Table 2 properties; method labels; heuristic = pre-scientific/high-risk |
| Development process | ch.3 | Eight-step workflow; protocol/data design can dominate algorithm choice (BP 5.5) |
| Clinical lifecycle | ch.4 | Nine-step lifecycle; exploratory → clinical-grade taxonomy; ISO 14971/FDA framing |
| Evaluation + failure | ch.5–7 | Nested CV, net benefit, historical failure catalog, knowledge cliff |
| Specialties + regulation | ch.8–11 | NLP/imaging cautions; FDA CDS; TRIPOD+ reporting |
| Capstone | ch.12 | BP maturity/impact routing index |

**Mandatory pairs (w3 internal):** Simon ch.3 ↔ AIE ch.4 (EDD vs health BP 5.7 workflow — AIE for generative eval design, Simon for property-based clinical appraisal); Simon ch.4 ↔ NAM sec04 (lifecycle gates ↔ readiness tiers); Simon ch.10 ↔ NAM sec03+sec05 (regulatory ELSI ↔ algorithmovigilance).

**Deferred slices:** Simon appendices A–C + index (L45491–52845) not ingested — BP tables in appendix 3 referenced from ch.12 only.

### Doc-snapshot BLOCKED gap

Three w3 slugs remain **`ingest_status: none`** — operator must export markdown snapshots to `text/`:

| Slug | Expected path | Blocks |
|------|---------------|--------|
| `langsmith_docs_snapshot` | `text/langsmith_docs_snapshot.md` | Trace + eval implementation layer |
| `langfuse_docs_snapshot` | `text/langfuse_docs_snapshot.md` | Observability + eval implementation layer |
| `langgraph_fault_tolerance_snapshot` | `text/langgraph_fault_tolerance_snapshot.md` | Agent fault-tolerance patterns |

Until supplied, w3 trace/eval tooling coverage is **pattern-portable only** via AIE ch.10 + UDS ch.31–32 + MDCalc canon cross-links — not vendor-specific runbooks.

### w3 ↔ w1/w2 redundancy map

| Topic | w1+w2 canonical | w3 canonical | Dedup rule |
|-------|-----------------|--------------|------------|
| **Eval pipelines** | AIE ch.4 EDD; PE ch.10 SOMA | Simon ch.3 Steps 6–7; ch.5 nested CV | **Simon for clinical property gates; AIE/PE for generative eval design.** |
| **Production guardrails** | AIE ch.10 architecture | NAM sec03 PHI/drift; Simon ch.4 Step 8 monitoring | NAM for governance policy; Simon for clinical monitoring; AIE for engineering patterns. |
| **RAG retrieval** | DDIA ch.4 + AIE ch.6 + HOTL ch.8 | Simon ch.8 NLP specialty | Engineering stack from w1+w2; Simon for clinical NLP deployment cautions only. |
| **Observability** | UDS ch.31–32; AIE ch.10 | Doc snapshots (BLOCKED) | UDS/AIE until operator exports LangSmith/Langfuse/LangGraph. |
| **PHI / de-id** | HOTL ch.11 pattern-portable | NAM sec03; Simon ch.5 phenotypes | HOTL insufficient alone; NAM + Simon own governance depth. |

### w4_ops_governance stack (partial — RAI complete, Kästner BLOCKED)

| Track | Slug | Role in stack | Units |
|-------|------|---------------|-------|
| B | `responsible_ai_practice_2025` | **Quantitative RAI spine** — SAFE-HAI framework, Rank Graduation metric family, governance processes, credit + bitcoin case studies | 10/10 |
| B | `kaestner_ml_production_2025` | **Preferred MLOps depth** — production ML systems rigor (deferred from w1 AIE ch.8–10) | **BLOCKED** |

**Read-order heuristic (not strict):** RAI ch.1 (SAFE-HAI + regulation survey) → ch.2–3 (RGA accuracy + RGR robustness) → ch.4–6 (RGE explainability, RGF fairness, RGP privacy) → ch.7 (RGS sustainability/ESG) → ch.8 (HCAI three-step oversight loop) → ch.9 (five-pillar governance) → ch.10 (credit default SAFE-HAI capstone via `safeaipackage`).

Load-bearing anchors:

- RAI ch.1 establishes **SAFE-HAI** (Secure, Accurate, Fair, Explainable Human-Centered AI) and previews the **Rank Graduation** metric family (RGA, RGR, RGE, RGF, RGP, RGS, RGH) — `ingests/responsible_ai_practice_2025_ch01_ingest.md`.
- RAI ch.2 is the **accuracy canon** — ISO 5723/NIST/EU AIA mapping, classical metrics, **Rank Graduation Accuracy (RGA)** via Lorenz/concordance curves — `ingests/responsible_ai_practice_2025_ch02_ingest.md`.
- RAI ch.3 defines **Rank Graduation Robustness (RGR)** — perturbation stability, RobustBench, ex-ante model comparison — `ingests/responsible_ai_practice_2025_ch03_ingest.md`.
- RAI ch.4 introduces **Rank Graduation Explainability (RGE)** — Shapley vs Shapley Lorenz, SME credit trade-offs — `ingests/responsible_ai_practice_2025_ch04_ingest.md`.
- RAI ch.5 covers **Rank Graduation Fairness (RGF)** — Simpson's paradox, HMDA conditional vs marginal fairness — `ingests/responsible_ai_practice_2025_ch05_ingest.md`.
- RAI ch.6 defines **Rank Graduation Privacy (RGP)** — four-step forget-set protocol, employee salary case — `ingests/responsible_ai_practice_2025_ch06_ingest.md`.
- RAI ch.7 extends to **Rank Graduation Sustainability (RGS)** — ESG ensemble finance, Table 7-1 rubric — `ingests/responsible_ai_practice_2025_ch07_ingest.md`.
- RAI ch.8 is the **HCAI oversight canon** — three-step evaluate/assess/improve loop, bitcoin FFNN→GRU remediation — `ingests/responsible_ai_practice_2025_ch08_ingest.md`.
- RAI ch.9 is the **governance process canon** — NIST harm taxonomy, seven risk categories, Table 9-1, five-pillar org structure — `ingests/responsible_ai_practice_2025_ch09_ingest.md`.
- RAI ch.10 is the **procedural capstone** — consumer credit default classification, full SAFE-HAI four-metric matrix via `safeaipackage` — `ingests/responsible_ai_practice_2025_ch10_ingest.md`.

### SAFE-HAI and Rank Graduation metrics

Duke & Giudici operationalize Responsible AI through **SAFE-HAI**: measurable Secure/Accurate/Fair/Explainable properties under **human-centered oversight** (ch.8). Each SAFE pillar maps to a **Rank Graduation** metric derived from Lorenz/concordance curves on ranked predictions — unified family enabling cross-dimension comparison and statistical testing (`safeaipackage` / `check_*` hooks).

| Metric | Pillar | Chapter | Definition sketch | Scoring rubric |
|--------|--------|---------|-------------------|----------------|
| **RGA** | Accuracy | ch.2 | Concordance between full-model and reduced-model ranked predictions | Table 2 bands (Excellent 75–90%) |
| **RGR** | Robustness | ch.3 | Stability under perturbation (adversarial + extreme-event) | Table 3 bands |
| **RGE** | Explainability | ch.4 | Per-feature contribution to model accuracy via Lorenz ranks | Table 4-2; aggregate cumulative RGE |
| **RGF** | Fairness | ch.5 | Conditional fairness on protected variables (Simpson's paradox guard) | Table 5-2 |
| **RGP** | Privacy | ch.6 | Sensitivity to train-set row removal (right-to-be-forgotten test) | Table 6-2 |
| **RGS** | Sustainability | ch.7 | E/S/G feature contribution to model output (parallel RGE structure) | Table 7-1 |
| **RGH** | Human oversight | ch.8 | Probability × severity risk matrix + improvement rubric (Table 8-1) | ch.8 three-step loop |

**Measurement workflow:** ch.2–7 supply per-pillar metrics → ch.8 wraps them in human-gated evaluate/assess/improve → ch.9 institutionalizes governance → ch.10 demonstrates end-to-end on credit data. No single model wins all dimensions (ch.10: RF best AUROC/RGF; decision tree best RGR; logistic competitive on explainability concentration).

Contested claims preserved in ingests (not smoothed): benchmarks ≠ risk-management metrics (ch.2); Shapley causal limits vs Simon ch.4 critique (ch.4); Simpson's paradox in HMDA fairness (ch.5); RGP high-score + significant-test paradox (ch.6); greenwashing/ESG provider heterogeneity (ch.7); trading-volume as RGF protected variable (ch.8); biorisk/spear-phishing severity in governance taxonomy (ch.9); n=6707 vs 9578 sample sizes, AUROC vs RGA rank mismatch (ch.10).

### Governance processes (RAI ch.9)

RAI ch.9 bridges ch.1 policy survey and ch.8 HCAI to **operational governance**:

| Pillar | Function |
|--------|----------|
| 1. Governance policy | Risk assessment, monitoring, reporting requirements |
| 2. AI governance team | Multidisciplinary working group (research, engineering, product, legal) |
| 3. Regular assessments | Scrutiny, testing, investigation of risks across lifecycle |
| 4. Stakeholder engagement | Users, civil society, policymakers — Table 9-1 information requirements |
| 5. User feedback | Continuous improvement loop from daily-use expertise |

**Cadence rule:** RAI ch.9 five-pillar structure supplies domain-agnostic org playbook; **NAM sec05** Tables 5-1–5-4 supply health-sector RACI/accountability detail. Pair before enabling clinical-adjacent or high-risk credit features.

### Case studies (RAI ch.8 + ch.10)

| Case | Chapter | Domain | Models | SAFE-HAI dimensions exercised |
|------|---------|--------|--------|-------------------------------|
| Bitcoin price direction | ch.8 | Financial time-series | FFNN baseline → NNAR/LSTM/GRU | RGA, RGR, RGE, RGF + Table 8-1 improvement |
| Consumer credit default | ch.10 | High-risk classification (EU AI Act) | Logistic, tree, RF, NN on six-predictor dataset | Full four-metric matrix via `pip install safeaipackage` |

Ch.10 appendix (L6375+) deferred — body ends at chapter conclusion L6374.

### Kästner BLOCKED gap

`kaestner_ml_production_2025` remains **`ingest_status: none`** with **`text_quality: mismatch`** — staged epub is Andrew Kelleher, not Christian Kästner (MIT Press 2025 OA, ISBN 9780262049726). Operator must replace at `pdfs/kaestner_ml_production_2025.pdf` + export `text/kaestner_ml_production_2025.txt` before selective chapter fan-out. Until supplied, MLOps production depth remains **pattern-portable only** via AIE ch.8–10 + w2 UDS observability — not Kästner-preferred single-text depth.

### w3 doc snapshots still pending

Three w3 slugs remain **`ingest_status: none`** — unchanged from w3 partial closeout. Operator must export markdown snapshots to `text/`:

| Slug | Expected path | Blocks |
|------|---------------|--------|
| `langsmith_docs_snapshot` | `text/langsmith_docs_snapshot.md` | Trace + eval implementation layer |
| `langfuse_docs_snapshot` | `text/langfuse_docs_snapshot.md` | Observability + eval implementation layer |
| `langgraph_fault_tolerance_snapshot` | `text/langgraph_fault_tolerance_snapshot.md` | Agent fault-tolerance patterns |

Until supplied, trace/eval tooling coverage is **pattern-portable only** via AIE ch.10 + UDS ch.31–32 + RAI ch.9 governance — not vendor-specific runbooks.

### w4 ↔ w1/w2/w3 redundancy map

| Topic | w1–w3 canonical | w4 canonical | Dedup rule |
|-------|-----------------|--------------|------------|
| **Eval pipelines** | AIE ch.4 EDD; PE ch.10 SOMA; Simon ch.3 Steps 6–7 | RAI ch.2 RGA + ch.3 RGR | **AIE/PE for generative eval design; RAI for unified Rank Graduation compliance metrics; Simon for clinical property gates.** |
| **Explainability** | Simon ch.4 Shapley critique | RAI ch.4 RGE + Shapley Lorenz | **Simon for clinical causal limits; RAI for normalized statistical explainability testing.** |
| **Fairness / ELSI** | Simon ch.10 FDA CDS; NAM sec03 bias | RAI ch.5 RGF + Simpson's paradox | **Simon for regulatory ELSI; RAI for quantitative fairness measurement.** |
| **Privacy / PHI** | NAM sec03; HOTL ch.11 pattern-portable | RAI ch.6 RGP forget-set protocol | **NAM for governance policy; RAI for model-level privacy testing.** |
| **Production guardrails** | AIE ch.10 architecture | RAI ch.9 five-pillar governance | **AIE for engineering patterns; RAI for org governance process; NAM sec05 for health RACI.** |
| **MLOps depth** | AIE ch.8–10 flywheel | Kästner (BLOCKED) | AIE until operator stages correct Kästner text. |
| **Observability tooling** | UDS ch.31–32; doc snapshots (BLOCKED) | RAI ch.9 risk taxonomy | UDS/AIE/RAI until operator exports LangSmith/Langfuse/LangGraph. |

**Mandatory pairs (w4 internal + cross-wave):** RAI ch.1/ch.9 ↔ NAM sec05 (governance + algorithmovigilance); RAI ch.5/ch.8 ↔ Simon ch.10 (fairness + HCAI ↔ ELSI); RAI ch.2–4 ↔ AIE ch.4/ch.10 (RGA/RGR/RGE ↔ EDD + observability); RAI ch.10 ↔ ch.2–7 (capstone applies full metric stack).

### Remaining gaps (post-w4 partial)

| Gap | w1–w4 coverage | Target |
|-----|----------------|--------|
| **Trace observability tooling** | AIE ch.10 + UDS ch.31–32 + RAI ch.9 pattern-portable | Doc snapshots (BLOCKED) |
| **DDIA transactions/consensus** | UDS ch.10–13 partial fill | DDIA ch.8–13 when full 2e text ships |
| **MLOps depth** | AIE ch.8–10 flywheel; RAI governance metrics | Kästner (BLOCKED) |
| **Simon appendices** | ch.12 references only | Optional on-demand ingest |
| **CLRS formal proofs** | Grokking intuition only | Optional on-demand per manifest |
| **RAI ch.10 appendix** | Body complete L6374 | Optional on-demand (L6375+) |

**TEXTBOOK-Q1 conditionals (w1):** Grokking ch.6/10/11/12 conditional low citation density — `LITERATURE_INDEX.md` convergent themes.

---

## MDCalc agent-monitoring canon (pattern-portable cross-links)

**Source canon (external):** `/Users/dubs/Projects/piranesi.skill/research-projects/0623-mdcalc-agent-monitoring/returns/mdcalc_agent_monitoring_decision_canon_20260625.md`  
**Constraint:** Pattern-portable only — no MDCalc production-stack or employer claims.

| MDCalc prevention control | w1 textbook pattern | Ingest anchor |
|---------------------------|---------------------|---------------|
| **P0 adapter contract** (tool raises or typed error — never success-shaped error string) | Deep modules + define-errors-out-of-existence; guardrail tier for write actions | Ousterhout index principles via `philosophy_software_design_2e_2021_ch22_ingest.md`; AIE ch.10 write-action guardrails — `ai_engineering_2025_ch10_ingest.md` |
| **P0.5 semantic evaluator on tool spans** (inspect content, not span status) | Eval-before-build; failure-mode metrics over vanity scores; per-component RAG relevance | AIE ch.4 EDD + slice analysis — `ai_engineering_2025_ch04_ingest.md`; ch.10 observability + metric design — `ai_engineering_2025_ch10_ingest.md` |
| **P1 retry fingerprint / circuit breaker** | Agent compound-step accuracy decay; routing after N identical tool failures | AIE ch.6 agent failure modes — `ai_engineering_2025_ch06_ingest.md` |
| **P1 trace-to-dataset / regression** | Data flywheel + user feedback as training signal; pin prompt_version + model_id | AIE ch.8 + ch.10 feedback loop warnings — `ai_engineering_2025_ch10_ingest.md` |
| **P2 task-outcome eval** (e.g., citations present) | RAG citation precision/recall; Ragas faithfulness | HOTL ch.8 Ragas axes — `hands_on_llms_2024_ch08_ingest.md` |
| **Silent semantic failure class** | Unknown unknowns in coupled systems | Ousterhout ch.2 symptoms — `philosophy_software_design_2e_2021_ch02_ingest.md` |

**w3 doc snapshots** (`langsmith_docs_snapshot`, `langfuse_docs_snapshot`, `langgraph_fault_tolerance_snapshot`) remain **BLOCKED** — operator export pending. NAM sec05 + Simon ch.3–4 supply governance/process canon until snapshots land.

**Clinical-adjacent pattern (no clinical claims):** HOTL ch.11 NER/de-identification cites anonymization use case — `[pattern-portable]` only; SetFit few-shot insufficient alone for PHI — `hands_on_llms_2024_ch11_ingest.md`.

---

## Operator blockers

| Slug | Issue |
|------|-------|
| `kaestner_ml_production_2025` | Wrong book staged (Andrew Kelleher ≠ Christian Kästner) — blocks w4 |
| Doc snapshots | LangSmith, Langfuse, LangGraph exports not supplied — w3 partial |
| `se_modern_approach_2024` | Not supplied |

---

## Next steps

1. **Kästner staging** — operator replace wrong epub with Christian Kästner *Machine Learning in Production* (MIT Press OA); export text; selective chapter fan-out.
2. **w3 doc snapshots** — operator export `langsmith_docs_snapshot.md`, `langfuse_docs_snapshot.md`, `langgraph_fault_tolerance_snapshot.md` to `text/`; re-run verify.
3. **DDIA ch.8–13** — re-ingest when O'Reilly early-release export includes full Part II tail.
4. **phylax mode=full** — fresh session (`context:fork`) before shipping reference-library as child skill.
5. **Child skill** — only if operator explicitly requests `output=skill` after reference-library ships.
