# Chapter ingest — `simon_aliferis_healthcare_2024` · Selective Chapter 4

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Artificial Intelligence and Machine Learning in Health Care and Medical Sciences |
| **authors** | Gyorgy J. Simon, Constantin Aliferis (eds.); chapter authors Simon & Aliferis |
| **edition** | 1st Edition (2024, Springer Health Informatics, OA CC BY 4.0) |
| **ISBN_print** | 978-3-031-39354-9 |
| **ISBN_electronic** | 978-3-031-39355-6 |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 4 (selective ingest; book ch. 6–7) |
| **chapter_title** | Clinical-Grade Model Lifecycle (+ bundled Data Design) |
| **page_range** | Printed pages absent from text export; logical span L19484–25037 |
| **parent_book_title** | Artificial Intelligence and Machine Learning in Health Care and Medical Sciences |

## Scope

Selective ingest **04** spans book **Chapter 6** (*The Development Process and Lifecycle of Clinical Grade and Other Safety and Performance-Sensitive AI/ML Models*, L19484–22986) and book **Chapter 7** (*Data Design in Biomedical AI/ML*, L22987–25037). Primary title per wave plan: **Clinical-Grade Model Lifecycle**; Data Design is included because it falls inside the line slice and is prerequisite to lifecycle Step 2.

**Part A — Clinical-grade lifecycle (book ch. 6).** Contrasts **exploratory**, **feasibility**, **pre-clinical**, and **clinical-grade / mission-critical** AI/ML models by cost-of-error and risk assessment (ISO 14971, FDA device framing, translational spectrum T0–T4). Presents a **nine-step lifecycle** (Fig. 1): (1) performance/safety requirements; (2) data design & collection; (3) first-pass analysis; (4) model optimization & validation (metrics, uncertainty, explanation, equivalence classes); (5) IP; (6) regulatory/bias/ELSI/JEDI; (7) production conversion, workflow, sandboxing, scaling, implementation science; (8) monitoring & safeguards including **knowledge cliff**; (9) ancillary work products & documentation. Each step pairs numbered **Pitfall 6.x** / **Best Practice 6.x** entries.

Step 1 expands requirements engineering: accuracy/explainability/safety targets, stakeholder engagement (clinical experts, payers, regulators, patients, societies), **ICER** and health-economics translation, system-level vs tunnel-vision modeling, ELSI/JEDI desiderata, Open Science/HIPAA/terminology standards (OMOP CDM, SNOMED, etc.).

Step 3 introduces **RNBNFCV** (repeated nested *N*-fold cross-validation) pseudo-code for unbiased error estimation during first-pass → optimized transition; warns against overfitting across iterative rounds.

Step 4.4–4.5 is a major **interpretability & equivalence-class** block: taxonomy (inherent vs post-hoc; global vs local; model-agnostic vs specific); PDP, ICE, LIME, Anchors, permutation importance; **critique of Shapley values** (causal Markov violations, imputation bias, weak relevance); large transparent models; human surrogate explainers; **Target Information Equivalency (TIE)** and Markov-boundary equivalence classes with causal modeling errors when classes are not inferred; IP bypass via equivalent feature sets.

Steps 5–9 cover patent vs reproducibility tension, regulatory/ELSI integration, subjective vs objective production inputs, CDS workflow/sandbox/scaling, implementation-science checklist (Bauer et al.), monitoring for knowledge-boundary violations, and exhaustive documentation (model cards, provenance, checklists).

**Part B — Data design (book ch. 7, bundled).** Defines **data design** as mapping Problem Space ↔ Model Space; five problem-statement elements (outcome, exposure/intervention, predictors, target population, time period); clinical vs operational vs translational settings; **discovery / accessible / target population** validity chain; problem-type taxonomy (diagnostic, screening, risk, prognostic, treatment efficacy, biomarker discovery, operational, economic, subpopulation); **data design hierarchy** (experimental → observational: cross-sectional, cohort, case-control, nested case-control, case-cohort); inclusion/exclusion criteria; worked cohort examples (diabetes/cardiac risk); bias catalog (confounding, selection, information, confounding-by-indication, ascertainment, informed presence, non-contemporaneous controls); **Simpson's paradox**; pitfalls/best practices 7.x.

**Sections ingested:** Lifecycle model taxonomy · Steps 1–9 with pitfalls/BPs · RNBNFCV · XAI taxonomy & Shapley critique · Equivalence classes/TIE · IP/regulatory/implementation/monitoring/knowledge cliff · Data design overview · Problem statement · Validity/generalizability · Design hierarchy · Cohort/case-control examples · Biases · Summary pitfalls/BPs (both book chapters).

Cross-refs: book ch. 3 (rigorous development), ch. 5 (methods appraisal), ch. 8–10 (data prep, evaluation, overfitting), ch. 16 (ELSI).

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Model taxonomy and risk framing

- Biomedical AI/ML differs from low-stakes recommendation/spam systems by **high cost of wrong decisions** across diagnosis, treatment, drug-target discovery, and health-system interventions. [verified from text, L19531–19593]
- Four model classes: exploratory (hypothesis test, no critical decisions linked); feasibility (constructibility test); pre-clinical (feasibility for future critical models); **clinical-grade/mission-critical** (performance allows safe patient/population/system decisions). [verified from text, L19601–19617]
- Delineation is fundamentally **risk assessment**; ISO 14971 and FDA criteria apply; T0–T1 ≈ exploratory/feasibility, T2+ ≈ clinical-grade. [verified from text, L19619–19633]
- **Pitfall 6.1.1:** treating clinical-grade development like exploratory/feasibility work. **BP 6.1.1:** explicitly define goals/process by model class. [verified from text, L19662–19677]

### Nine-step lifecycle (high level)

- Lifecycle parallels method-development process but targets **model** (not algorithm) development for existing/new methods on available data. [verified from text, L19695–19708]
- **Step 1:** meaningful performance targets in real-use context; stakeholder engagement; **ICER** links predictivity to value; system-level interactions (e.g., sepsis alert + existing workflows); relax requirements for feasibility models. [verified from text, L19733–20110]
- **Step 2:** rigorous data design as important as modeling for high-stakes models; convenience-design limits must be acknowledged for feasibility work. [verified from text, L20116–20168]
- **Step 3:** first-pass modeling must be rigorous; transition pitfalls include ignoring literature reproduction and **overfitting across iterations**; **RNBNFCV** provides unbiased outer-loop accuracy averaging with stratified splits. [verified from text, L20170–20358]
- **Step 4:** optimization covers data/algorithms/protocols, metrics vs targets, uncertainty, explanation, **equivalence classes**; omitting steps is Pitfall 6.2.4.4. [verified from text, L20358–21186]
- **Steps 5–9:** IP must not block reproducibility yet must resist equivalence-class bypass; ELSI/JEDI throughout; production models favor **objective inputs**; sandbox pre-deployment; implementation-science dimensions; monitoring for **knowledge cliff** (models acting outside training distribution); ancillary datasets and documentation. [verified from text, L21186–21653]

### Interpretability and Shapley critique `[contested in chapter]`

- Prefer interpretable models when accuracy tradeoff acceptable; standardized coefficients for linear models; feature selection before surrogate explanation; LIME/global surrogates/local surrogates/human surrogates each need fidelity evaluation. [verified from text, L20853–20888]
- **Shapley values** adopted uncritically for ML explanation exhibit: improper feature relevance; failure under causal dependence; imputation-based SVs ≠ de novo model SVs; violation of causal Markov condition. Authors recommend against SV-based explanation for causal/clinical interpretation. [verified from text, L20665–20891]

### Equivalence classes

- **TIE:** variables A, A' carry identical information about target T; modeling without inferring equivalence classes yields random Markov-boundary members, suboptimal deployment models, and **IP bypass**. [verified from text, L20911–21171]
- Causal errors include discarding true causes for information-equivalent non-causes and over-interpreting algorithm-selected variables as biologically primary. [verified from text, L21051–21131]

### Data design (bundled book ch. 7)

- Data design specifies what data are modeled and Problem↔Model mapping; differs from classical study design by reliance on **pre-existing digital repositories**, automation, rich representations (text, graphs), and ML-specific evaluation. [verified from text, L23006–23018]
- Five elements refine rough questions: outcome, exposure/intervention, predictors, target population, time period; settings = clinical, operational, translational. [verified from text, L23100–23221]
- Validity requires **target ⊇ accessible ⊇ discovery** representativeness; failure → Pitfall 7.2.1. [verified from text, L23549–23652]
- Design hierarchy: prefer simplest adequate design; cross-sectional only when temporal gap absent; cohort for incidence/prevalence/time gaps; case-control for rare outcomes; nested designs merge cohort + case-control benefits with shared limitations. [verified from text, L23779–24289]
- Biases: confounding, selection, information, confounding-by-indication, ascertainment, informed presence, non-contemporaneous controls; **Simpson's paradox** — BP 7.4.1: check aggregation when effect direction surprises. [verified from text, L24291–24466]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/simon_aliferis_healthcare_2024.txt` |
| **Lines read** | 19484–25037 (inclusive) |
| **Chapter boundary** | Starts book ch. 6 abstract (L19484); ends before book ch. 8 Data Preparation (L25038); includes full book ch. 7 Data Design |
| **Wrong-file flag** | `false` |
| **Sections deferred** | Forward refs to ELSI ch. 16, overfitting ch. 10, evaluation ch. 9 (named only); classroom assignments summarized not reproduced |
| **Figures** | Lifecycle flow (Fig. 1–2), interpretation taxonomy (Fig. 3), equivalence-class tree (Fig. 5), data-design flows — alt-text/placeholders in export |
| **Amnesiac rule** | ISBN/edition from L53–57 and corpus manifest |

## Pedagogy

### Learning objectives

1. Distinguish exploratory, feasibility, pre-clinical, and clinical-grade models and apply risk-based development rigor.
2. Walk through the **nine-step clinical-grade lifecycle** and map project activities to each step.
3. Specify performance targets with stakeholders and translate predictivity into **ICER/value** framing.
4. Explain **RNBNFCV** purpose in first-pass → optimized transitions.
5. Critique Shapley-value and feature-importance explanations for clinical models.
6. Define **TIE/equivalence classes** and list predictive/causal/IP consequences of ignoring them.
7. Construct a **data design** (five elements, hierarchy choice, inclusion/exclusion) for an observational ML problem.

### worked_examples_present

**Y** — Multiple pedagogical scenarios, pseudo-code, and vignettes:

| Example | Section | Role |
|---------|---------|------|
| Low- vs high-stakes AI domains | Model taxonomy | Cost-of-error framing |
| Sepsis alert system-level evaluation | Step 1.4 | Tunnel vision vs system goals |
| RNBNFCV pseudo-code | Step 3 | Unbiased error estimation |
| Melanoma dermoscopy + LIME table | Step 4.4 | Local explanation |
| Causal DAG + equivalence tree | Step 4.5 | TIE / Markov boundary |
| Diabetes early-treatment (Ex 7.2.1) | Data design | Five-element problem statement |
| Cohort risk model (Ex 7.3.1) | Data design | Index date, I/E criteria |
| Drug mortality cohort (Ex 7.3.2–3) | Data design | Confounding, exposure windows |
| ICER hospital budget vignettes | Classroom | Health economics (lifecycle tail) |

### exercise_hooks

- End-of-chapter **classroom assignments** present for both book ch. 6 and 7 (proposal review, BN incomplete evidence, model equivalence, data-design scenarios).
- **Instructor hooks `[inferred]`:**
  - Classify three published health-AI papers by model tier and list missing lifecycle steps.
  - Draft Step 1 requirements doc with ICER threshold for a screening test.
  - Red-team a Shapley-based feature ranking for a causal clinical variable set.
  - Design cohort vs case-control for a rare oncology outcome; document bias risks.

## Operator hooks

### 1. w3_clinical_docs — lifecycle canon

This selective chapter is the **operational spine** for clinical-grade ML engineering in the cs-ai-textbook-canon w3 track: model-class gating before method work, requirements-before-modeling (pairs with **ai_engineering_2025** EDD at pattern level), and explicit monitoring/knowledge-cliff vocabulary. **RNBNFCV** cross-links **simon ch06** (overfitting) and **simon ch05** (evaluation/error estimation). Bundled **Data Design** is prerequisite reading before data-prep ingest ch05.

### 2. MDCalc / clinical-adjacent alignment

**[high]** — Directly on-point for regulated clinical ML without product claims:

- **Risk-tiered rigor:** Exploratory notebook ≠ clinical-grade pipeline; ISO 14971/FDA framing portable to SaMD planning.
- **Value translation:** ICER/minimum performance thresholds before deployment decisions.
- **Explanation skepticism:** Shapley/feature-importance not sufficient for causal clinical narrative.
- **Validity chain:** Target/accessible/discovery populations — essential for EHR-derived models.
- No employer-stack or specific vendor APIs cited.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **designing_ml_systems_2022** | Medium | Production ML lifecycle; Simon adds clinical risk tiers, ICER, regulatory |
| **ai_engineering_2025** | Low–medium | Eval pipeline patterns; Simon is clinical/regulatory depth |
| **responsible_ai_practice_2025** | Medium | ELSI/JEDI overlap; Simon ch. 16 deferred for regulatory detail |
| **ddia_2e_2026** | Low | Data modeling at systems layer; Simon data design is study-design layer |

**Dedup:** Treat this ingest as canonical for **clinical-grade lifecycle + health data design hierarchy** in w3 SYNTHESIS.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — lifecycle steps, RNBNFCV, cohort designs, XAI taxonomy |
| Exercise hooks | **Strong in text** — extensive classroom sections both book chapters |
| Chapter boundary | **Bundled** — selective slice spans two book chapters by design |
| Ingest suitability | **High** — numbered pitfalls/BPs, citation-backed, contested Shapley claims preserved |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2024 Springer OA; w3_clinical_docs wave |
| **Author authority** | **PASS** | UMN Institute for Health Informatics editors; forewords (Chapman, Demiris); decades clinical ML practice |
| **Primary-source citation density** | **PASS** | ISO 14971, FDA, Murdock XAI survey, Ma & Tourani Shapley critique, OHDSI/OMOP, Pearl Simpson's paradox |
| **Contested claims flagged** | **PASS** | Shapley explanation limits, IP vs openness, equivalence-class IP bypass |
| **Worked examples** | **PASS** | Nine-step lifecycle, RNBNFCV, cohort/case-control walkthroughs |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| SIM-C04-001 | Clinical-grade vs exploratory model classes differ by linked decision risk | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | Model taxonomy |
| SIM-C04-002 | Nine-step lifecycle spans requirements through monitoring | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | Lifecycle |
| SIM-C04-003 | RNBNFCV for unbiased error estimation in model optimization | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | Step 3 |
| SIM-C04-004 | Shapley values have severe shortcomings for ML/causal explanation | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | Shapley pitfalls |
| SIM-C04-005 | Equivalence-class ignorance yields random Markov-boundary models and IP bypass | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | TIE |
| SIM-C04-006 | Data design maps Problem Space to Model Space via five problem elements | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | Data design |
| SIM-C04-007 | Discovery sample must represent accessible and target populations | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch04_ingest.md | Validity |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `simon-ingest-ch04-06` · word cap ≤4500*
