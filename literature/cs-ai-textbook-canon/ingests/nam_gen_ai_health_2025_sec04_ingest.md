# Section ingest — NAM GenAI in Health and Medicine, Section 4 (Application Readiness Cadence)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Generative Artificial Intelligence in Health and Medicine: Opportunities and Responsibilities for Transformative Innovation |
| **authors** | National Academies of Sciences, Engineering, and Medicine (NAM) |
| **year** | 2025 |
| **venue** | NAM Special Publication |
| **DOI** | https://doi.org/10.17226/28907 |
| **section** | 4 — Application Readiness Cadence |
| **source_type** | consensus_report |
| **pdf_path** | literature/cs-ai-textbook-canon/pdfs/nam_gen_ai_health_2025.pdf |
| **text_path** | literature/cs-ai-textbook-canon/text/nam_gen_ai_health_2025.txt |

## Scope

Section 4 organizes LLM health applications into near-, mid-, and long-term readiness tiers (Figure 4-1), balancing opportunity against patient/clinician/system risk. Near-term emphasizes lower-risk admin and education tasks; mid-term precision medicine and documentation coding; long-term higher-autonomy virtual assistants, surveillance, and synthetic medical education.

## Key findings

All claims **[verified from text]** from lines 1004–1228.

### Framing (1006–1015)

- Lower-risk apps (ambient ambulatory scribing) closer to deployment than higher-risk virtual health assistants (Tierney et al., 2024).
- Figure 4-1 maps opportunities vs risks across time horizons.

### Near-term (1017–1071)

**Patient education/engagement:** LLM chatbots for mental health showed depression/distress reductions in prospective studies (Li et al., 2023); tailored culturally appropriate responses; informed-consent readability gains but bias reinforcement risk if unchecked (Decker et al., 2023; Omiye et al., 2023).

**Information synthesis:** EHR summarization reducing admin burden (Van Veen et al., 2024); vendor integrations (Goodman et al., 2024); cohort retrieval for trials and retrospective studies (Jin et al., 2023); real-time literature review with hallucination risk without careful question tailoring (Tang et al., 2023).

### Mid-term (1084–1166)

**Precision medicine:** Multimodal prognostic synthesis (Wilhelm et al., 2023) with confusing/incorrect recommendations; precision oncology LLMs lack clinician-useful evidence (Benary et al., 2023); may need neurosymbolic reasoning for interpretability.

**Rare diseases:** GenAI linking mechanisms to therapeutics; in silico trials (ISTs) and digital twins (DTs) for underpowered trials (Rees et al., 2019; Kolla et al., 2021; Moingeon et al., 2023; Bartlett et al., 2019; Cosmas et al., 2024); LLM foundation models enabling cross-disease twins.

**Documentation/coding:** NLU note generation and billing codes (Yang et al., 2023); SDOH extraction from unstructured text (Guevara et al., 2024); ChatGPT diagnosis-code accuracy varies—high for common, poor for rare (Hadi et al., 2024; Harada et al., 2024).

**Genome mining:** DNA language models for variant effect prediction augmenting GWAS.

### Long-term (1168–1211)

**Virtual health assistants:** Symptom assessment, triage, remote consult after validation (Sezgin, 2024; Tadesse et al., 2023).

**Disease surveillance:** Multi-source outbreak detection—limited by real-time reliable data access.

**Medical education:** Synthetic cases/images for representative curricula when data and domain knowledge adequate (Safranek et al., 2023).

## Section digest (readiness tiers)

| Tier | Example applications | Primary gating risks |
|------|---------------------|----------------------|
| Near | Ambient scribe, chart summary, patient education drafts | Hallucination, bias in consent/education |
| Mid | Precision oncology CDS, billing codes, digital twins | Wrong recommendations, code inaccuracy |
| Long | Autonomous triage, outbreak AI, synthetic training | Safety, data latency, representation |

## Coverage attestation

| Field | Value |
|-------|-------|
| **lines_read** | 1004–1228 (inclusive) |
| **section_boundary** | Starts `APPLICATION READINESS CADENCE` (1004); ends before `THE PATH FORWARD` (1229) |
| **figure_placeholders** | Figure 4-1 (1049) |
| **deferred** | Sections 1–3, 5–6 |

## Operator hooks

### Foundation layer

**Deployment sequencing reference** for w3. Use before enabling high-autonomy features in any clinical-adjacent stack. Pair Simon ch.4 (clinical-grade lifecycle) for gate criteria translating tiers into validation requirements.

### MDCalc alignment

**[relevant]**:

- **Risk-tiered rollout** (1010–1012) → ship admin/summary features with stricter eval than patient-autonomous triage; maps to guardrail tiering (read vs write vs autonomous).
- **Local validation before tier promotion** `[inferred from sec01 + 1010]` → near-term ≠ zero risk; Atrium mixed results (sec02) justify cohort-specific eval.
- **Billing/code GenAI** (1144–1155) → high financial/compliance blast radius; require accuracy benchmarks on rare-code slices before automation.
- **Bias in patient-education chatbots** (1053–1054) → slice eval by demographic before patient-facing deploy.

No MDCalc employer claims.

### Redundancy

| Source | Note |
|--------|------|
| sec02 application list | sec04 adds temporal risk stratification |
| AIE ch.10 | Production architecture for near-term deploy |
| Simon ch.4 | Lifecycle gates for mid/long-term |

### Scholia fit

Figure 4-1 + tier table → strong procedural routing card ("which app class am I building?").

---

*Ingest agent: nam-ingest-sections · sec04 · lines 1004–1228 · word cap ≤4500*
