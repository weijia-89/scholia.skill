# Section ingest — NAM GenAI in Health and Medicine, Section 3 (Risks)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Generative Artificial Intelligence in Health and Medicine: Opportunities and Responsibilities for Transformative Innovation |
| **authors** | National Academies of Sciences, Engineering, and Medicine (NAM) |
| **year** | 2025 |
| **venue** | NAM Special Publication |
| **DOI** | https://doi.org/10.17226/28907 |
| **section** | 3 — Risks of Generative Artificial Intelligence in Health and Medicine |
| **source_type** | consensus_report |
| **pdf_path** | literature/cs-ai-textbook-canon/pdfs/nam_gen_ai_health_2025.pdf |
| **text_path** | literature/cs-ai-textbook-canon/text/nam_gen_ai_health_2025.txt |

## Scope

Section 3 enumerates primary GenAI risks in health: privacy/security, bias/equity, output limitations, algorithmic brittleness, and hallucinations/confabulations. It describes mitigation via organizational processes, federal frameworks (NIST AI RMF GenAI profile, Biden EO), multi-stakeholder collaboration, and technical tactics (dual-model comparison, prompt engineering, knowledge grounding, fact-checking).

## Key findings

All claims **[verified from text]** from lines 838–1003.

1. **Primary risk categories** (841–844): data privacy/security; bias; output limitations; algorithmic brittleness; hallucinations.

2. **Privacy/security** (846–855): vast sensitive data access; feedback loops may leak PHI into refined models; organizations must map data flows and prevent inadvertent public disclosure.

3. **Bias and equity** (857–895): non-representative training worsens care; historical data encodes systemic disparities; **AI drift** when new data or tuning degrades performance unpredictably; transparency and bias-detection validation essential.

4. **Output limitations** (897–934): generic/repetitive chatbot responses ignoring individual history erode trust; irresponsible deployment can harm patients; org processes needed to assess new AI tools, monitor safety, address challenges; NIST AI RMF and Executive Order on AI as governance foundations (NIST, 2024; White House, 2023).

5. **Algorithmic brittleness** (936–945): failure on out-of-distribution inputs; poor generalization in critical domains (Eliot, 2024).

6. **Hallucinations/confabulations** (947–969): plausible but false outputs (Farquhar, 2024); citation fabrication case study (Goddard, 2023); mitigations: dual-model discrepancy checks, prompt engineering, high-quality knowledge bases, fact-checking cross-references.

7. **Collaboration to mitigate** (982–992): multi-stakeholder engagement (providers, patients, policymakers, developers, insurers, researchers, ethicists) for intentional, coordinated, ethical deployment with fairness/transparency/effectiveness evaluation.

## Section digest

| Risk | Mechanism | Mitigation cited |
|------|-----------|------------------|
| Privacy | Training feedback loops | Data-flow mapping, PHI controls |
| Bias/drift | Skewed history, tuning | Bias detection, validation |
| Output limits | Pattern-matched replies | Dynamic personalization, feedback loops |
| Brittleness | OOD inputs | Robustness testing |
| Hallucination | Generative prediction | Dual models, RAG, fact-check |

## Coverage attestation

| Field | Value |
|-------|-------|
| **lines_read** | 838–1003 (inclusive) |
| **section_boundary** | Starts `RISKS OF GENERATIVE ARTIFICIAL` (838); ends before `APPLICATION READINESS CADENCE` (1004) |
| **deferred** | Sections 1–2, 4–6 |

## Operator hooks

### Foundation layer

**Risk taxonomy SSOT** for w3 clinical canon. Complements Simon ch.6 (overfitting/overconfidence) and ch.7 (historical failures). Engineering mitigations cross-link AIE ch.5 (security), ch.6 (RAG grounding), ch.10 (guardrails, observability).

### MDCalc alignment

**[relevant]** — highest-density governance patterns in NAM report:

- **PHI in model feedback loops** (851–852) → prohibit training on production PHI without explicit governance; log redaction; patient-data boundary controls.
- **AI drift monitoring** (887–892) → post-deploy performance tracking with revalidation triggers—algorithmovigilance (Embí, 2021 cited in sec05).
- **Hallucination controls** (964–969) → dual-model disagreement checks; grounded retrieval before clinical citations; never trust bibliographic metadata from LLM alone (Goddard case).
- **NIST AI RMF + EO alignment** (918–934) → org-level AI governance checklist for any clinical-adjacent agent.
- **Human oversight integration** (963, 916–917) → mandatory for patient-facing outputs.

Pattern-portable only; no employer production claims.

### Redundancy

| Canon | Relationship |
|-------|--------------|
| AIE ch.5/ch.10 | Security + guardrails implementation detail |
| Simon ch.6 | Statistical overconfidence vs GenAI hallucination |
| UDS ch.32 | PHI in logs/traces |

### Scholia fit

Clean bounded section; strong failure-mode cards for procedural study guides.

---

*Ingest agent: nam-ingest-sections · sec03 · lines 838–1003 · word cap ≤4500*
