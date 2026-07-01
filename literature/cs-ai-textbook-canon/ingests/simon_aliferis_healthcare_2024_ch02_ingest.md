# Chapter ingest — `simon_aliferis_healthcare_2024` · Chapter 2

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Artificial Intelligence and Machine Learning in Health Care |
| **authors** | Gyorgy J. Simon, Constantin Aliferis |
| **edition** | 1st Edition (2024) |
| **ISBN_print** | 978-3-031-39354-9 |
| **ISBN_electronic** | 978-3-031-39355-6 |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 2 (Part I: Foundations) |
| **chapter_title** | An Appraisal and Operating Characteristics of Major ML Methods Applicable in Healthcare and Health Science |
| **page_range** | Printed page numbers absent from text export; logical span L7262–16116 |
| **parent_book_title** | Artificial Intelligence and Machine Learning in Health Care |

## Scope

Chapter 2 is the **method-selection atlas** for biomedical ML—organized as drug-style **Method Labels** plus deep technical sections weaving classical statistics and mainstream ML.

**Analytic task taxonomy (Fig. 1).** Six tasks in two categories: **predictive modeling** (regression, classification, time-to-event) and **exploratory analysis** (density estimation, outlier detection, clustering). "Predictive" includes diagnosis, prognosis, and retroactive recognition—not only forecasting. Causal modeling deferred to Ch. 4. Outcome types: continuous (interval vs. ratio scale caution), categorical (binary/multinomial; nominal/ordinal), time-to-event (survival), sequence, structured. Temporal data types: cross-sectional (majority of ML), longitudinal, time-series—method choice depends on correlation structure of errors.

**Method Label format.** Each method/family presents: Main Use, Context of use, Secondary use, Pitfalls, Principle of operation, Theoretical properties & empirical evidence, Best practices, References—enabling at-a-glance appraisal without full algorithmic depth.

**Chapter layout (sections ingested selectively):**
- **Foundational Methods:** OLS regression (BLUE, homoscedasticity, ~10 obs/predictor rule, linear/additive limits); logistic regression; k-NN; naive Bayes; decision trees; SVMs (margin maximization, kernels, multi-class extensions).
- **Ensemble Methods:** bagging, boosting, random forests, stacked generalization—stability/variance reduction; RF vs. logistic large-scale benchmarks cited.
- **Regularization:** bias-variance perspective; Lasso/Ridge/elastic net; graphical lasso; regularization as search-space constraint; penalty coefficients **not** equivalent to statistical conditioning (Pitfall foreshadow Ch. 3).
- **Feature selection & dimensionality reduction:** filter/wrapper/embedded; Markov Boundary methods cross-ref Ch. 1/4; PCA.
- **Time-to-event:** Kaplan-Meier, Cox proportional hazards (PH), time-dependent covariates, summary survival statistics.
- **Longitudinal data:** mixed models (LMM), generalized estimating equations (GEE)—marginal vs. subject-specific effects; autocorrelated errors.
- **Brief coverage:** network medicine/network science (centrality metrics vs. predictive value caveat from Ch. 1), active learning, outlier detection ("super utilizer"), genetic algorithms (heuristic, expensive), visualization (EHR challenges, t-SNE in omics).

**Professional data scientist bar:** Beyond Method Labels, practitioners should implement, trace, prove properties, and interpret outputs for each family (seven-skill checklist L13471–13517).

**Sections ingested:** Introduction · Task taxonomy · Temporal characteristics · Method Label spec · Foundational methods · Ensembles · Regularization · Feature selection/DR · Survival · Longitudinal · Other techniques · Recommended understanding level · Classroom assignments.

Cross-refs: Ch. 1 (properties, inductive bias), Ch. 3 (protocol/stack interactions), Ch. 4 (causal), Ch. 5–6 (data prep, overfitting).

## Key findings

All claims below are **[verified from text]** unless tagged `[contested in chapter]` or `[inferred]`.

### Task taxonomy and data types

- Predictive vs. exploratory distinguished by designated outcome variable; diabetes comorbidity co-occurrence = exploratory. [verified from text, L7319–7342]
- "Predictive modeling" includes diagnosis, prognosis, past-event recognition—not only future forecasting. [verified from text, L7322–7326]
- Temperature cited as ratio scale (0°F ≠ 0°C)—modeling scale matters. `[contested in chapter—common stats pedagogy treats temperature as interval]` [verified from text, L7357–7360]
- Cross-sectional predictors can forecast future outcomes (e.g., 7-year diabetes risk). [verified from text, L7458–7461]
- Causal modeling explicitly separated—see Ch. 4. [verified from text, L7308–7310]

### Method Labels and selection principles

- Method Labels analogous to drug labels: primary/secondary use, pitfalls, properties at a glance. [verified from text, L7288–7292, L7501–7580]
- Classical + ML methods integrated—reflects modern practice. [verified from text, L7597–7600]
- OLS: BLUE, convex LS, Gaussian outcome assumption; ~10 observations per predictor; no automatic interaction discovery. [verified from text, L7651–7686]
- SVM for classification primary; regression secondary; **wrong causal effect estimates if used causally** (Method Label pitfall pattern). [verified from text, L7548–7555, L8281+]
- Random forests: ensemble of trees for stability; Couronné et al. large-scale RF vs. logistic benchmark. [verified from text, L9851+, refs L14027–14029]
- Regularization constrains search space; Ridge may miss grouped predictors (B and T example L10451+).
- Cox PH: seminal survival method; extensions for time-dependent covariates noted in Ch. 3 step 5.c. [verified from text, L11606+, L17021–17022]
- GEE vs. LMM: GEE for population-averaged predictions on new subjects; LMM for subject-specific effects; GEE robust to working correlation misspecification. [verified from text, L13311–13367]
- Network science metrics (diameter, path length, clustering) **do not** imply predictive/causal value—Ch. 1 property filter applies. [verified from text, L13385–13404]
- Genetic algorithms: heuristic, local optima, use when no method insight—prefer methods with known properties. [verified from text, L13421–13434]

### Pitfalls embedded in method guidance

- Clustering for predictive modeling discouraged (Ch. 1 BP 2.10 echoed in method contexts).
- SVM causal misuse flagged in Method Label pitfalls.
- Regularized coefficients ≠ conditional effects—over-interpretation pitfall (Ch. 3 Pitfall 5.9).
- Visualization in multivariable EHR data can mislead. [verified from text, L13448–13451]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/simon_aliferis_healthcare_2024.txt` |
| **Lines read** | 7262–16116 (inclusive) |
| **Chapter boundary** | Starts `An Appraisal and Operating Characteristics...` (L7262); ends before Ch. 3 `Principles of Rigorous Development` (L16117) |
| **Wrong-file flag** | `false` |
| **Sections deferred** | Full algorithm pseudocode for every method; Ch. 4 causal ML (starts L14276 within file but outside ch02 span—boundary at 16116); neural network deep dive (brief mention only) |
| **Figures** | Fig. 1 task taxonomy, Method Label tables, survival/Longitudinal plots; `[]` placeholders |
| **Amnesiac rule** | Method performance claims anchored to chapter text and cited refs only |

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Classify a clinical question as predictive vs. exploratory and assign outcome type (continuous/categorical/time-to-event/sequence).
2. Read a Method Label and map entries to Table 2 properties from Ch. 1.
3. Select foundational vs. ensemble vs. regularized models given sample size, dimensionality, and interpretability needs.
4. Choose Cox PH vs. logistic for survival vs. binary endpoints; GEE vs. LMM for longitudinal goals.
5. Identify when a method is used outside its validated context (SVM for causal estimation, clustering for prediction).
6. Articulate the seven-skill professional bar for algorithm mastery.

### worked_examples_present

**Y** — Method Label tables throughout; OLS derivation; T2DM task classification in classroom assignments; GEE/LMM error-correlation panels; RF vs. logistic benchmark references.

| Example | Section | Role |
|---------|---------|------|
| Fig. 1 predictive/exploratory taxonomy | Introduction | Task routing |
| OLS Gaussian likelihood → LS | Foundational | MLE connection |
| Method Label: GEE | Longitudinal | Marginal vs. subject-specific |
| T2DM 7-year risk questions | Classroom §1 | Task type drill |
| Ridge B/T grouped variable | Regularization | Penalty limitation |

### exercise_hooks

- **Printed:** Extensive classroom assignments L13526–13872 (task classification, method selection scenarios, data representation).
- **Instructor / self-study hooks `[inferred]`:**
  - Write Method Labels for two deployed clinical models not covered explicitly (e.g., gradient boosting for readmission).
  - Given EHR cohort + question, fill Fig. 1 routing diagram and justify method family.
  - Compare interpretability vs. performance tradeoff scenarios (assignment §5g–h).

## Operator hooks

### 1. Foundation layer

Chapter 2 is **w3_clinical_docs method-selection canon**—operational bridge from Ch. 1 properties to Ch. 3 development/evaluation workflow. Method Labels should be indexed in LITERATURE_INDEX as the **lookup table** for "which algorithm for which clinical task." Prerequisite after Ch. 1; before Ch. 3 (protocol design) and Ch. 6 (overfitting). Complements **designing_ml_systems_2022** on production patterns; Simon Ch. 2 owns **health-specific method labels + survival/longitudinal** coverage.

### 2. MDCalc alignment

**[high]** — Core reference for clinical calculator and risk-model engineering:

- **Task-outcome typing**: Maps calculator outputs (probability, survival, category) to correct method family—prevents logistic-on-time-to-event class errors.
- **Method Labels as SaMD analog**: Pitfalls/best-practices blocks mirror intended-use / contraindications framing for clinical decision tools.
- **Sample size rules**: OLS 10:1 heuristic, high-dimension breakdown—relevant to rare-disease calculator validation.
- **Survival methods**: Cox PH + KM directly applicable to prognostic calculators; GEE/LMM for repeated-measures endpoints.
- **Interpretability scenarios**: Classroom prompts on "interpretable vs. best performance" mirror calculator UX/clinical acceptance tradeoffs.
- **Causal misuse warnings**: SVM/regularized coef misinterpretation—critical for treatment-effect calculators.
- **No employer-stack claims**.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **ai_engineering_2025** Ch. 4 | Low–medium | AIE eval pipeline for **generative** systems; Simon Ch. 2 is **predictive classical/ML method atlas**—minimal EDD overlap |
| **designing_ml_systems_2022** | Medium | DMS feature/training/eval chapters overlap RF, slicing; Simon adds Method Labels + survival/longitudinal health framing |
| **grokking_algorithms_2022** | Low | Decision trees briefly; Simon depth on health task taxonomy |
| **hands_on_llms_2024** | None | LLMs not method-label focus |
| **harrell_regression** (implicit via refs) | Medium | Harrell cited for survival; Simon integrates into broader label system |

**Dedup guidance:** Treat **simon_aliferis_healthcare_2024 Ch. 2** as canonical for **health ML method labels + task taxonomy + survival/longitudinal** in SYNTHESIS; reference **ai_engineering_2025 Ch. 4** only for generative/private-eval pipeline—not for repeating method-selection tables here.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — Method Labels, OLS walkthrough, longitudinal panels |
| Exercise hooks | **Strong** — multi-part classroom assignments |
| Chapter boundary quality | **Clean** — ends with professional bar + assignments before Ch. 3 |
| Ingest suitability | **High** — selective ingest captures label framework + major families; full algorithm proofs deferred appropriately |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | Springer 2024 OA |
| **Author authority** | **PASS** | Same editors; extensive peer refs (Harrell, Hastie, Breiman, Aliferis FS papers) |
| **Primary-source citation density** | **PASS** | Method sections cite foundational papers; large benchmark refs |
| **Contested claims flagged** | **PASS** | Method misuse pitfalls explicit; GA heuristic limits; network metric limitations |
| **Worked examples (procedural/conceptual)** | **PASS** | Method Labels + classroom scenarios |

**Overall TEXTBOOK-Q1:** **PASS** — selective ingest preserves label framework and major families; operator should use full chapter for algorithm-level proofs.

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| SIM-C02-001 | Method Labels provide drug-label-style at-a-glance method appraisal | compressed | AI/ML in Health Care 1e | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch02_ingest.md | Method Labels |
| SIM-C02-002 | Six analytic tasks split predictive vs. exploratory modeling | compressed | AI/ML in Health Care 1e | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch02_ingest.md | Introduction |
| SIM-C02-003 | OLS requires ~10 observations per predictor variable | compressed | AI/ML in Health Care 1e | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch02_ingest.md | OLS |
| SIM-C02-004 | GEE for population predictions; LMM for subject-specific effects | compressed | AI/ML in Health Care 1e | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch02_ingest.md | GEE Method Label |
| SIM-C02-005 | Network centrality metrics do not imply predictive clinical value | compressed | AI/ML in Health Care 1e | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch02_ingest.md | Network science |

---

*Ingest generated by scholia chapter fan-out · worker `simon-ingest-ch01-03` · corpus `cs-ai-textbook-canon` · word cap ≤4500*
