# Section ingest — NAM GenAI in Health and Medicine, Section 5 (The Path Forward)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Generative Artificial Intelligence in Health and Medicine: Opportunities and Responsibilities for Transformative Innovation |
| **authors** | National Academies of Sciences, Engineering, and Medicine (NAM) |
| **year** | 2025 |
| **venue** | NAM Special Publication |
| **DOI** | https://doi.org/10.17226/28907 |
| **section** | 5 — The Path Forward (+ References + Author Information) |
| **source_type** | consensus_report |
| **pdf_path** | literature/cs-ai-textbook-canon/pdfs/nam_gen_ai_health_2025.pdf |
| **text_path** | literature/cs-ai-textbook-canon/text/nam_gen_ai_health_2025.txt |

## Scope

Section 5 prescribes foundational activities for responsible GenAI integration: workforce skill generation; model training, implementation, and monitoring (including Tables 5-1/5-2 comparing generative vs predictive AI oversight); resources/infrastructure; standardized oversight and guidelines; cross-sector collaboration (Table 5-3 life-cycle phases; Table 5-4 RACI-style responsibility matrix); and a concluding synthesis. The slice also includes the full reference bibliography (lines 1879–2205) and contributor biographies with conflict disclosures (2222–2358).

## Key findings

All substantive claims **[verified from text]** from lines 1229–1868; bibliography and author rows from 1879–2361.

### Foundational activities (1231–1234)

Skill generation; model testing/implementation/monitoring; resources/infrastructure; standardized oversight/guidelines.

### Skill generation (1236–1258)

- Clinicians must interpret GenAI outputs as possible, not certain—never supplanting judgment (1241–1243).
- Expand clinician AI literacy curricula; continuous education; patient/consumer education for rights and trust (1247–1258).

### Model training, implementation, monitoring (1272–1350)

- Sociotechnical governance web: regulators, vendors, health systems, providers (1275–1281).
- **Algorithmovigilance** for GenAI despite black-box opacity (Embí, 2021; lines 1285–1289).
- Tables 5-1 (1322–1345) — **similarities**: bias/fairness checks; performance drift; ethical/societal impact; regulatory compliance; user feedback loops.
- Tables 5-2 (1377–1420) — **differences**: GenAI monitors subjective coherence, hallucinations, content misuse; predictive AI tracks accuracy/precision/recall on fixed parameters.
- OMB M-24-10: test conditions must mirror deployment (1300–1302); **local validation** on local population and EHR software; Classen et al. EHR safety program used by 3,000+ hospitals annually (1304–1306).
- Privacy/ethics require domain experts, ethicists, stakeholders throughout lifecycle (1307–1350).

### Resources and infrastructure (1352–1436)

- Many organizations lack expertise, budget, IT for LLM deployment (1354–1357).
- EHR integration costly; trust-building with frontline clinicians resource-intensive (1358–1365).
- Digital divide may worsen access if patients lack connectivity/devices (1433–1436).

### Standardized oversight and guidelines (1438–1499)

- FDA, ASTP/ONC, and other regulators need clear GenAI evaluation standards (1444–1448).
- Many AI-enabled solutions will **not** be FDA-regulated yet used for summarization, CDS, patient chatbots (1453–1459).
- OCR nondiscrimination responsibilities for provider AI use (1464–1464).
- Flexible reimbursement/regulatory models; new evaluation metrics beyond traditional methods; real-world local validation and benchmarks (1490–1499).
- Shared responsibility between developers and health systems (Ratwani et al., 2024).

### Collaboration (1501–1837)

- Table 5-3 (1514–1626): collaboration opportunities across life-cycle phases—prioritizing problems, data creation, model development/evaluation/standards, implementation/diffusion, monitoring/maintenance (including red-teaming, adversarial testing, version management).
- High development costs drive shared data assets and standards (AAMI software lifecycle reference, 1521–1522).
- Table 5-4 (1692–1795): **health care professionals accountably (A) responsible (R)** for prioritization, evaluation fit-for-purpose, implementation, and ongoing monitoring—bearing decision risk despite developer work.
- Policy makers/regulators accountable for model standards; developers accountable for data assurance and model build.
- Patient/community consultation required across all phases (1681–1837).
- RACI key (1806–1832): Accountable (one), Responsible (do work), Consulted (two-way), Informed (one-way updates).

### Conclusion (1839–1868)

Transformative potential requires managing privacy, bias, transparency, infrastructure limits via cross-stakeholder collaboration, federal/organizational oversight, standardized guidelines, continuous education.

### References (1879–2205) — attestation only

~60 numbered references spanning ambient scribing (Tierney, Van Veen, Liu NEJM AI), hallucination (Farquhar, Goddard), governance (NIST AI.600-1, White House EO, OMB M-24-10), equity (Omiye), CDS (Liu JAMIA), digital twins, drug repurposing (Yan), WHO AI ethics guidance. Full list in source text; not reproduced here (provenance via DOI 10.17226/28907).

### Author information (2222–2358)

Contributors include NLM leadership (Babski—GenAI pilot), Vanderbilt informatics chair Embí (algorithmovigilance author), and other workshop authors; **Conflict disclosures: None** stated for sampled bios (Babski, Embí).

## Section digest

| Pillar | Core obligation | Named artifact |
|--------|-----------------|----------------|
| Skills | Clinician + patient AI literacy | Curricula, CME |
| Monitoring | GenAI ≠ predictive-only metrics | Tables 5-1, 5-2 |
| Local proof | Mirror deployment conditions | OMB M-24-10, Classen EHR safety |
| Governance | Shared dev/provider responsibility | Ratwani; Table 5-4 |
| Collaboration | Life-cycle stakeholder map | Tables 5-3, 5-4 |

## Coverage attestation

| Field | Value |
|-------|-------|
| **lines_read** | 1229–2361 (inclusive) |
| **section_boundary** | Path Forward (1229) through Author Information; ends before APPENDIX (2362) |
| **tables_ingested** | 5-1, 5-2, 5-3, 5-4 (structured summaries) |
| **references** | Bibliography scanned in full; individual entries not duplicated (SF-12 word budget) |
| **deferred** | Appendix (sec06); Sections 1–4 |

## Operator hooks

### Foundation layer

**Governance and RACI SSOT** for w3 clinical canon—primary handoff to Simon ch.9 (regulatory ELSI) and ch.10–11 (reporting). Cross-link AIE ch.4 (eval design), ch.10 (observability), Shah et al. 2023 nationwide health AI assurance labs (reference list).

### MDCalc alignment

**[relevant]** — densest operational governance content:

- **Algorithmovigilance + drift** (1285–1333) → post-deploy monitoring with revalidation; GenAI adds subjective quality and hallucination checks beyond accuracy metrics.
- **Local validation on local EHR** (1302–1306) → mandatory before trusting vendor demos; 3,000-hospital EHR safety precedent.
- **Table 5-4 accountability** → health professionals remain **Accountable** for implementation/monitoring even when developers are Responsible for build—maps to human-in-loop and sign-off gates for any clinical-adjacent agent output.
- **Red-teaming / adversarial testing** (Table 5-3, 1574–1575) → pre-ship robustness for biased/adversarial inputs.
- **Non-FDA-regulated GenAI** (1453–1459) → org policy must cover summarization and chatbots even without device clearance.
- **Version management + retraining triggers** (Table 5-3 monitoring rows) → model registry and change control.

Pattern-portable; no MDCalc production-stack claims.

### Redundancy

| Canon | Relationship |
|-------|--------------|
| Simon ch.4, ch.9 | Lifecycle + regulatory detail |
| AIE ch.10 | Engineering controls for Table 5-2 monitoring |
| sec03 risks | sec05 operationalizes mitigation |

### Scholia fit

Tables 5-3/5-4 → procedural RACI worksheets; reference list anchors phylax provenance rows for cross-cited studies.

---

*Ingest agent: nam-ingest-sections · sec05 · lines 1229–2361 · word cap ≤4500*
