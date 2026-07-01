# Section ingest — NAM GenAI in Health and Medicine, Section 1 (Introduction)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Generative Artificial Intelligence in Health and Medicine: Opportunities and Responsibilities for Transformative Innovation |
| **authors** | Thomas Maddox, Dianne Babski, Peter Embí, Jackie Gerhart, Jennifer Goldsack, Ravi Parikh, Troy Sarich; Sunita Krishnan and Audrey Elliott, editors |
| **year** | 2025 |
| **venue** | NAM Special Publication / National Academies Press (Learning Health System Series) |
| **DOI** | https://doi.org/10.17226/28907 |
| **ISBN** | 978-0-309-73369-4 |
| **section** | 1 — Introduction |
| **source_type** | consensus_report |
| **pdf_path** | literature/cs-ai-textbook-canon/pdfs/nam_gen_ai_health_2025.pdf |
| **text_path** | literature/cs-ai-textbook-canon/text/nam_gen_ai_health_2025.txt |

## Scope

Section 1 defines generative AI (GenAI) and large language models (LLMs) as health-relevant content generators; surveys early promise and limited real-world evidence; names primary risk categories (hallucination, inequitable access, training-data bias); and frames trustworthy deployment through governance, diverse training data, clinician certification, workflow redesign, and periodic local validation. It anchors the report in the National Academy of Medicine (NAM) Learning Health System (LHS) and Shared Commitments trust framework, and documents provenance from the October 25–26, 2023 NAM Digital Health Action Collaborative workshop and federal follow-on meeting.

Out of scope in this slice: application-specific evidence (Section 2), detailed risk taxonomy (Section 3), readiness cadence (Section 4), path-forward recommendations (Section 5), appendix stakeholder tables.

## Key findings

All claims **[verified from text]** from lines 463–575 unless tagged `[inferred]`.

1. **GenAI/LLM definition.** GenAI produces text, imagery, and audio; LLMs specialize in language. Models train on vast text corpora and generate via prediction; users guide output with prompts and post-processing. (lines 465–472)

2. **Early health applications cited.** Drafting administrative documents; clinical documentation support; decision support; patient engagement; prior authorization summaries; evidence synthesis and drug repurposing. Evidence of real-world impact remains limited. (lines 473–487)

3. **Named risks.** Hallucinations/confabulations affecting medical decisions; inequitable access in lower-resourced settings; bias from training data or engineering choices. (lines 488–492)

4. **Trustworthy use requires hybrid governance.** Approaches overlap with and diverge from predictive/analytical AI; evolving policies needed. Accountability mechanisms include cross-organization governance frameworks; standards for testing and training on diverse datasets; clinician training and certification; workflow modification for human oversight; periodic local testing, validation, and oversight in clinical settings (Ratwani et al., 2024). (lines 521–535)

5. **LHS framing.** NAM defines a Learning Health System as aligning science, informatics, incentives, and culture for continuous improvement—with patients/families as active participants and knowledge generated as a by-product of care (NAM, n.d.). (lines 538–545)

6. **Shared Commitments.** NAM trust framework emphasizing accessible, affordable, transparent, accountable, adaptive system performance (McGinnis et al., 2024). (lines 548–550)

7. **Workshop provenance.** NAM Digital Health Action Collaborative workshop (Oct 25, 2023) plus federal agency meeting (Oct 26, 2023) to align health professionals, system leaders, developers, and agencies on LLM/GenAI implications; publication synthesizes benefits, risks, guideposts, and guardrails. (lines 551–559)

8. **Figure 1-1.** History of AI use in health care (figure placeholder in text export; pedagogical anchor for timeline cards). (lines 508–508)

## Section digest

| Subtopic | Lines (approx.) | Takeaway |
|----------|-----------------|----------|
| GenAI/LLM primer | 465–472 | Prompt-guided text generation from large corpora |
| Application vignettes | 473–485 | Admin, clinical, patient, payment, discovery |
| Evidence gap | 486–487 | Promise > demonstrated impact |
| Risk triad | 488–492 | Accuracy, equity, bias |
| Governance & oversight | 521–535 | Frameworks, standards, training, local validation |
| LHS + Shared Commitments | 538–550 | Institutional north star |
| Report origin | 551–559 | Workshop → consensus publication |

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/nam_gen_ai_health_2025.txt` |
| **lines_read** | 463–575 (inclusive) |
| **section_boundary** | Starts at `INTRODUCTION` (463); ends before `OPPORTUNITIES AND EARLY EVIDENCE` (576) |
| **wrong_file_flag** | false |
| **deferred** | Sections 2–6; appendix; references list |
| **figure_placeholders** | Figure 1-1 (508) — image not in text layer |

## Operator hooks

### Foundation layer (w3_clinical_docs)

**Clinical/regulatory spine opener** for Wave 3. Establishes vocabulary (GenAI, LLM, LHS, Shared Commitments) before Simon/Aliferis lifecycle depth and NAM sections 2–5. Pair with:

- `simon_aliferis_healthcare_2024` — rigorous development and regulatory ELSI (ch.3–4, ch.9+)
- `ai_engineering_2025_ch10_ingest.md` — production guardrails and observability (engineering complement)
- AIE ch.4 eval slice analysis — private eval before clinical-adjacent deploy

### MDCalc alignment

**[relevant]** — pattern-portable clinical AI governance (no employer claims):

- **Governance framework across organizations** (lines 528–529) → maps to multi-tier oversight: org policy + local validation + human-in-loop before patient-facing outputs.
- **Periodic local testing/validation/oversight in real-world settings** (lines 533–535) → algorithmovigilance-style post-deploy monitoring; pair with AIE ch.10 guardrails and UDS ch.31 SLO/chaos patterns.
- **Clinician training/certification on LLM use** (lines 530–531) → operator competency gate before trusting draft outputs (notes, messages, CDS).
- **Workflow modification for human oversight** (lines 532–533) → HOTL pattern: GenAI drafts; clinician accountable for sign-off.

Do not cite this section as FDA clearance criteria or MDCalc production policy.

### Redundancy

| Canon | Overlap | Distinction |
|-------|---------|-------------|
| Simon/Aliferis 2024 | Trustworthy AI, bias, lifecycle | NAM = consensus workshop synthesis; less methodological depth |
| AIE 2025 ch.10 | Guardrails, monitoring | NAM = health-system governance and equity framing |
| HOTL ch.1 | Responsible LLM development mention | NAM = domain-specific clinical guardrails |

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Anchor density | Moderate — cites Gandhi, Ratwani, McGinnis; LHS quote |
| Procedural hooks | Governance checklist derivable for study-guide cards |
| Boundary | Clean intro slice |

---

*Ingest agent: nam-ingest-sections · sec01 · lines 463–575 · word cap ≤4500*
