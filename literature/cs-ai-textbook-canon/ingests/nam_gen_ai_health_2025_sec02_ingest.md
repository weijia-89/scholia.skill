# Section ingest — NAM GenAI in Health and Medicine, Section 2 (Opportunities and Early Evidence)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Generative Artificial Intelligence in Health and Medicine: Opportunities and Responsibilities for Transformative Innovation |
| **authors** | National Academies of Sciences, Engineering, and Medicine (NAM) |
| **year** | 2025 |
| **venue** | NAM Special Publication |
| **DOI** | https://doi.org/10.17226/28907 |
| **section** | 2 — Opportunities and Early Evidence for Generative Artificial Intelligence in Health and Medicine |
| **source_type** | consensus_report |
| **pdf_path** | literature/cs-ai-textbook-canon/pdfs/nam_gen_ai_health_2025.pdf |
| **text_path** | literature/cs-ai-textbook-canon/text/nam_gen_ai_health_2025.txt |

## Scope

Section 2 catalogs early GenAI use cases across clinical operations, research, discovery, equity, and patient engagement. Each subsection cites published or vendor-reported evaluations with explicit mixed or preliminary results. The section repeatedly flags need for ongoing assessment, human oversight, and validation—especially where adoption is outpacing evidence (ambient scribing, patient messaging).

## Key findings

All claims **[verified from text]** from lines 576–837.

### Chart summarization (587–598)

- Clinicians take ~7 minutes to summarize a chart; LLMs faster (Van Veen et al., 2024).
- Clinicians preferred GenAI summaries >50% of the time vs clinician-written.
- GenAI summaries comparable on completeness, correctness, trustworthiness (Schoonbeek et al., 2024).

### Ambient note documentation (600–631)

- Ambient visit recording → templated encounter notes; favorable Permanente experience, reduced documentation time (Tierney et al., 2024).
- Atrium Health longitudinal study: no overall EHR/financial metric differences; small benefits for low-volume users, high utilizers, family medicine (Liu, Hetherington, Dharod, et al., 2024).
- Rapid adoption despite mixed results (Epic, 2024); continual value assessment required.

### Patient messaging (633–645)

- UC San Diego: empathetic drafts reduce cognitive burden but increase read time and reply length (Tai-Seale et al., 2024).
- Mayo Clinic nurses saved ~30 s/message (Cacciaglia, 2024).
- Human input still necessary; large improvements needed.

### Population health and research (647–670)

- Conversational prompts → data queries (Epic, 2024).
- Literature synthesis for evidence-based practice—subject to hallucinations; mitigation required.

### Prior authorization and insurance (672–681)

- Draft appeal letters by abstracting chart data (Kirby, 2024).

### Clinical decision support (683–691)

- Nascent role due to error/bias concerns (Ratwani et al., 2024).
- Emerging: explainable CDS creation and alert optimization via LLMs (Liu, McCoy, Peterson, et al., 2024; Liu, McCoy, Wright, et al., 2024).

### Clinical trials (693–703)

- Trial design, evidence summarization, regulatory compliance, recruitment/enrollment diversity (Carroll and Anderson, 2024; Gangwal et al., 2024; Merk et al., 2018; Ng, 2024).
- Unstructured note standardization; multilingual patient education.

### Drug discovery and repositioning (717–723)

- Novel molecular structures, antibody design (Marinov et al., 2024); repurposing (Yan et al., 2024).

### Diagnostics and monitoring (725–733)

- Dementia differentiation (Xue et al., 2024); differential diagnosis support (Kanjee et al., 2023); hypertension engagement (Andreadis et al., 2024).

### Health equity (735–785)

- Potential: increased clinician availability via burden reduction; multilingual/culturally tailored materials; prior auth/reimbursement assistance; scheduling chatbots (Clark and Bailey, 2024).
- Disparity illumination via large-dataset analysis.
- **Caveat:** could worsen equity with non-representative data or inequitable deployment; empiric equity impact evidence currently absent.

### Patient and support network engagement (787–826)

- Personalized education, 24/7 chatbots, caregiver resources, community connection.
- Chatbots require ongoing clinical oversight and monitoring (lines 818–820).

## Section digest

| Application domain | Evidence quality signal | Human oversight note |
|--------------------|-------------------------|----------------------|
| Chart summarization | Comparative studies favorable | Clinician review implied |
| Ambient scribing | Mixed system-level outcomes | Rapid adoption → monitor |
| Patient messaging | Time tradeoffs | Draft + edit |
| Literature synthesis | Hallucination risk | Fact-checking required |
| CDS | Early/experimental | Error/bias concerns |
| Equity tools | Promise > validation | Monitor for harm |

## Coverage attestation

| Field | Value |
|-------|-------|
| **lines_read** | 576–837 (inclusive) |
| **section_boundary** | Starts `OPPORTUNITIES AND EARLY EVIDENCE` (576); ends before `RISKS OF GENERATIVE ARTIFICIAL INTELLIGENCE` (838) |
| **deferred** | Sections 1, 3–6 |

## Operator hooks

### Foundation layer

Primary **use-case catalog** for w3 clinical procedural guides. Maps 1:1 to Simon/Aliferis lifecycle gates (data prep ch.5, overfitting ch.6, reporting ch.10–11). Cross-link AIE ch.6 RAG for literature synthesis and ch.10 for ambient-scribe observability.

### MDCalc alignment

**[relevant]** — clinical AI governance patterns:

- **Draft-then-verify workflows** (chart summaries, messages, prior auth) → treat LLM output as provisional; clinician/accountable human signs off before patient-visible or billing actions.
- **Mixed ROI evidence on ambient scribing** → deploy with local eval slices (low-volume vs high-utilizer cohorts) before org-wide rollout—mirrors AIE ch.4 slice analysis.
- **Patient-facing chatbots** (818–820) → mandatory ongoing clinical oversight; maps to guardrail + escalation tiers (AIE ch.10).
- **Equity monitoring** (777–780) → representative eval datasets before production; `[inferred]` tie to Simon ch.5 data governance.

No MDCalc product or employer-stack claims.

### Redundancy

| Source | Overlap |
|--------|---------|
| AIE ch.6/ch.10 | RAG summarization, production monitoring |
| HOTL ch.8 | Retrieval quality for evidence synthesis |
| Simon ch.7 | Historical failure lessons complement mixed Atrium results |

### Scholia fit

High anchor density (15+ cited studies); suitable for application-matrix study cards and "evidence vs adoption" debate prompts.

---

*Ingest agent: nam-ingest-sections · sec02 · lines 576–837 · word cap ≤4500*
