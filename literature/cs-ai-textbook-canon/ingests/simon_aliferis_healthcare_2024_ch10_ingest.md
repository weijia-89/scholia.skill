# Chapter ingest — Simon & Aliferis (2024) · Selective Ch.10 (Book Ch.16: Regulatory ELSI)

| Field | Value |
|-------|-------|
| slug | simon_aliferis_healthcare_2024 |
| source_type | textbook |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/simon_aliferis_healthcare_2024.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch10_ingest.md |
| text_lines_read | 41849–43887 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Artificial Intelligence and Machine Learning in Health Care and Medical Sciences |
| authors | Johnson, Steven G.; Simon, Gyorgy; Aliferis, Constantin |
| edition | 1st (Springer Health Informatics, 2024) |
| ISBN_print | 978-3-031-39354-9 |
| ISBN_electronic | 978-3-031-39355-6 |
| DOI | https://doi.org/10.1007/978-3-031-39355-6 |
| chapter_number | 10 (selective) / 16 (book) |
| chapter_title | Regulatory Aspects and Ethical Legal Societal Implications (ELSI) |
| page_range | [not in text export] |

---

## Scope

Book chapter 16 closes the **clinical deployment and governance** arc: how AI/ML models enter regulated care workflows (CDS Hooks, EHR execution environments), how **ISO 14971** risk management frames benefit-vs-harm tradeoffs across the device lifecycle, how **FDA** classifies clinical decision support (21st Century Cures Act → 2022 Final Guidance four non-device criteria), how **Good Machine Learning Practice (GMLP)** ten principles map to prior book chapters, and how emerging **EU AI Act** and **NIST AI RMF 1.0** frameworks sit alongside U.S. regulation. The second half pivots to **biomedical AI ethics**: measurable in-consent harms (effectiveness, equity) vs traditional out-of-consent privacy risks; NIH definitions of minority health, health equity, and health disparity; survey of fairness literature; and technical tools for bias detection—**causal-path-to-outcomes**, equivalence-class modeling, and system-level resource allocation ethics. Best Practices 16.1–16.10 codify lifecycle risk planning, non-maleficence, disparity reduction, ethics culture, data design for equity, model auditing, bias-revealing models, equitable access, and multi-model system optimization.

Out of scope in this slice: reporting standards (ch.17, selective ch.11); synthesis chapter (ch.18); appendices; index.

---

## Key findings

All claims **[verified from text]** from lines 41849–43887 unless tagged `[inferred]`.

1. **CDS deployment context** (lines 41897–41943). Model impact requires workflow integration; CDS Hooks enables vendor-agnostic external model servers. Post-deployment monitoring is mandatory—input data drift (population, terminology, documentation) and model drift (practice changes from outputs) both require eventual retraining. Performance metrics must match the clinical problem (cross-ref Evaluation chapter).

2. **ISO 14971 risk management** (lines 41945–42126). Central thesis: expected benefits must outweigh potential harms. Medical device definition encompasses AI/ML CDS. Five-step process: (i) intended use and foreseeable misuse; (ii) hazard identification and risk estimation; (iii) risk evaluation (acceptability); (iv) risk control with residual-risk iteration; (v) post-production monitoring and re-evaluation. Pitfall 16.1: ISO 14971 mandates actions but not implementation methods. Best Practice 16.1: consider risks across all lifecycle phases. Patient-specific CDS risk-benefit and pure business decisions are excluded from scope.

3. **FDA CDS regulation** (lines 42134–42289). 21st Century Cures Act (2016) created ambiguity; 2022 Final Guidance abandoned draft risk-based IMDRF approach in favor of four criteria—if **all four** met, software is non-device CDS. Criterion 1: no medical image/signal/pattern analysis. Criterion 2: displays/analyzes accepted medical information. Criterion 3: supports (not replaces) HCP recommendations; time-critical specificity triggers regulation. Criterion 4: HCP can independently review basis (six disclosure elements: intended use, inputs, population, algorithm summary, validation evidence, patient-specific context). Only ~521 AI devices FDA-approved over 25 years (mostly radiology); guidance is non-binding—enforcement TBD.

4. **GMLP ten principles** (lines 42291–42479). FDA/Health Canada/MHRA joint principles (2021) are high-level only—book cross-references each to prior chapters: multidisciplinary expertise; software engineering/security; representative data; train/test independence; reference datasets; model tailored to data and use; human-AI team performance; clinically relevant testing; clear user information (links to Reporting Standards ch.17); deployed-model monitoring and retraining risk management.

5. **Additional regulatory frameworks** (lines 42481–42542). EU AI Act: high-risk health AI, regulatory sandboxes, open-source developer obligations. NIST AI RMF 1.0: voluntary; socio-technical risk framing; govern/map/measure/manage functions. Landscape is fluid—compliance readiness required.

6. **ELSI paradigm shift** (lines 42544–42570). Traditional ELSI emphasized out-of-consent privacy breaches (hard to quantify). Health AI/ML adds **in-consent** measurable risks: under-performance, group-specific harm, interpretability and governance failures—potentially measurable and addressable via best practices.

7. **Health equity definitions** (lines 42572–42650 approx.). Minority health (OMB racial/ethnic groups); health equity as social justice in health (Whitehead: avoidable, unnecessary, unjust inequalities); health disparity as adverse differences in outcomes, care, coverage, or quality for disadvantaged populations; health determinants include SDOH intertwined with disparities.

8. **Literature synthesis on fairness** (lines 42700–42894). Multiple authors converge: engage marginalized communities; collect audit data on protected groups; report intersectional performance; set disparity thresholds; post-market surveillance (e.g., [32]); diverse teams and preanalysis plans (Chen et al.); avoid over-automation and biased training data (Gianfrancesco); critique "neutral" equal-output models when biology justifies differences (McCradden)—focus on downstream patient effects not metrics alone.

9. **Causal-Path-to-Outcomes Principle** (lines 42896–42979). Paradigmatic example: race → differential healthcare access → treatment intensity → outcomes creates spurious past-expenditure predictors; purely predictive models may drop race yet embed bias. **Rule:** causal paths from race/minority indicators to medical decisions affecting outcomes without medical justification indicate unethical bias requiring remediation in modeling and/or practice.

10. **Equivalence classes and Pitfall 16.3** (lines 42981–43011). Predictively optimal model families may swap race for information-equivalent proxies—collinearity insufficient for detection. System-level ethics (lines 43013–43078): locally optimal ICU admission models may collectively exceed capacity; solutions include operations-research integration, ground-up multi-objective design, or hybrid approaches (Best Practice 16.10).

11. **Best Practices 16.3–16.10** (lines 43150–43260). Non-maleficence; disparity reduction mandate; ethics-equity culture (training, community engagement, accountability); data design supporting equity (SDOH collection, adequate minority representation); model development/evaluation equity audits with interpretable/causal methods; use AI to **reveal** bias (do not "sterilize" bias-capturing audit models); equitable access; system-level multi-model optimization.

---

## Pedagogy

### Learning objectives

1. Map ISO 14971 lifecycle steps to a clinical ML model deployment plan.
2. Apply FDA four-criterion test to classify CDS as device vs non-device.
3. Cross-reference GMLP principles to concrete book chapters for implementation.
4. Distinguish traditional privacy ELSI from in-consent performance/equity harms.
5. Apply Causal-Path-to-Outcomes and equivalence-class reasoning to bias audits.
6. Recognize system-level resource conflicts across multiple deployed models.

### worked_examples_present

**Y** — Causal diagrams for racial bias in treatment allocation (Figs. 2–4); ISO 14971 walkthrough; FDA criterion examples (ECG patterns, heart-failure scores, sepsis alerts); pulmonary ICU capacity scenario.

### exercise_hooks

1. Draft risk management plan outline for a sepsis prediction CDS.
2. Classify three hypothetical CDS products under FDA four criteria.
3. Build causal graph for a disparity scenario and identify spurious predictors.
4. Exercise 7: surrogate model for provider decision bias (lines 43551–43594).

---

## Coverage attestation

| Field | Value |
|-------|-------|
| source_path | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/simon_aliferis_healthcare_2024.txt` |
| lines_read | 41849–43887 (inclusive) |
| section_boundary | Starts `Regulatory Aspects and Ethical Legal Societal Implications`; ends before `Reporting Standards, Certification/Accreditation, and Reproducibility` (43888) |
| wrong_file_flag | false |
| deferred | Book ch.17–18; appendices A–C; index |
| book_chapter_map | Selective ch.10 = book ch.16 |

---

## Operator hooks

**w3_clinical_docs regulatory spine.** Pair with NAM sec03 (risks) and sec04 (readiness) for governance framing; AIE ch.10 for production guardrails. **MDCalc `[relevant]`:** FDA CDS classification and GMLP monitoring map to algorithmovigilance and HOTL disclosure patterns—do not cite as clearance policy.

### Redundancy

| Canon | Overlap | Distinction |
|-------|---------|-------------|
| NAM GenAI 2025 | Governance, equity, bias | Simon = technical depth on FDA/ISO/causal bias detection |
| responsible_ai_practice_2025 | Fairness frameworks | Simon = health-specific causal-path principle |

---

## TEXTBOOK-Q1 verdict

**PASS** — Primary-source regulatory citations (ISO 14971, FDA Final Guidance, GMLP, EU AI Act, NIST AI RMF); contested fairness claims flagged (race-in-model heuristics, neutral-model critique); worked causal examples; Pitfalls 16.1–16.3 explicit.

---

## Cross-references

| Reference | Topic |
|-----------|-------|
| Book ch.4 | Clinical-grade lifecycle |
| Book ch.7 | Evaluation, decision curves |
| Book ch.8 | Lessons learned / historical bias |
| Selective ch.11 | Reporting Standards (TRIPOD, GMLP principle 9) |
| NAM sec01–06 | Consensus governance complement |

---

## Glossary

| Term | Definition |
|------|------------|
| CDS Hooks | Vendor-agnostic FHIR-based CDS integration standard |
| ISO 14971 | Medical device risk management lifecycle standard |
| GMLP | FDA/Health Canada/MHRA Good Machine Learning Practice principles |
| Health disparity | Adverse health difference for disadvantaged populations |
| Causal-Path-to-Outcomes | Bias signal when race causally affects decisions without medical justification |
| Equivalence class | Set of predictively equivalent models that may hide proxy bias |

---

*Ingest agent: simon-ingest-ch10-12 · selective ch10 · lines 41849–43887 · word cap ≤4500*
