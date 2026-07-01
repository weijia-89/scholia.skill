# Chapter ingest — `simon_aliferis_healthcare_2024` · Selective Chapter 6

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
| **chapter_number** | 6 (selective ingest; book ch. 10–11) |
| **chapter_title** | Overfitting & Overconfidence (+ bundled Human-with-Machine) |
| **page_range** | Printed pages absent from text export; logical span L30521–34536 |
| **parent_book_title** | Artificial Intelligence and Machine Learning in Health Care and Medical Sciences |

## Scope

Selective ingest **06** spans book **Chapter 10** (*Overfitting, Underfitting and General Model Overconfidence and Under-Performance Pitfalls and Best Practices*, L30521–33372) and book **Chapter 11** (*From "Human versus Machine" to "Human with Machine"*, L33373–34536). Primary title: **Overfitting & Overconfidence**; Human-with-Machine is bundled in the line slice.

**Part A — Overfitting & overconfidence (book ch. 10).** Treats **overfitting (OF)**, **underfitting (UF)**, **overconfidence (OC)**, and **under-performance (UP)** as interacting with error estimation, model selection, sampling, and reporting — especially under high dimensionality, modest *n*, and powerful learners.

**Pedagogical examples:**
1. **"Who Is the Teacher?"** — sparse high-accuracy rules (catalog-listed instructor) vs biologically plausible weak rules; illustrates capacity vs generalization.
2. **ANN training epochs** — U-shaped train/test error (Fig. 1).
3. **Rich Simon genomics gene-selection protocols** — resubstitution vs full CV vs partial CV bias (Protocol 1–3).
4. **Polynomial regression surfaces** — complexity vs sample size.

Definitions: OF model fits training/idiosyncratic patterns; extends to **methods/protocols/stacks** that systematically inflate performance estimates. UF/UP = failure to reach achievable performance. **OC** = believing model/generalization error is better than reality; asymmetric severity vs UF (OC can cause immediate harm).

**Mechanisms generating OC/UP:**
- Poor sampling / non-representative training data
- Biased error estimation (resubstitution, imputation-before-split, partial CV, preprocessing on full sample — e.g., PCA)
- **Single holdout** ≈ one NHST with inflated effective α ("Single Split Testing Known")
- **Nested CV (NCV/NFCV/RNBNFCV)** decouples training (TR) from testing (TE) — links back to ch04 lifecycle
- Selective reporting, **analysis creep**, file-drawer/publication bias
- Uncorrected multiple testing / **data dredging** (Bonferroni outdated; FDR preferred)
- Multi-team uncoordinated iteration on same benchmark data
- Non-reproducible subjective preprocessing; normalization requiring full-sample statistics
- **Spurious co-occurrence** patterns in high-D data
- Patient-specific (**N-of-1**) modeling without power/sample analysis
- Bespoke hand-crafted models skipping best-known methods

**Prevention/remediation (Best Practice 10.1 — OC/OF):** regularization; dimensionality reduction; strong feature selection; Bayesian priors/ensembles; algorithm-embedded capacity control (SVM structural risk, boosting stagewise complexity); AIC/BIC-style complexity measures; nested CV model selection; confidence/credible intervals; **unbiased estimators** (RNBNFCV, 0.632+); lock models at predefined stages; FDR control; full procedural reporting; coordinate multi-team protocols; standardized reproducible inputs; batch-safe normalization; label-reshuffling sanity tests; model stability checks.

**Best Practice 10.2 — UF/UP:** sufficient data preparation; adequate hyperparameter search; apply domain best methods per ch03; respect reference specifications; compare individualized models to population baselines; power/sample analysis extensions for ML (learning curves, causal sparsity, sensitivity analysis, simulation, domain/network priors).

**Part B — Human with machine (book ch. 11, bundled).** Surveys meta-analyses/systematic reviews where ML matches or exceeds clinicians (neurosurgical outcomes, oral cancer imaging, suicide prediction, etc.) — often **high-dimensional inputs** favor ML; also reviews where humans remain superior. Introduces **human heuristic biases** (availability, anchoring, etc.) vs **ML biases**; argues for **hybrid human–machine** decision making exceeding either alone; cognitive forcing functions and appropriate automation levels.

**Sections ingested:** OF/UF/OC/UP definitions · Four pedagogical examples · Bias-variance asymmetry · Error-estimation contamination · RNBNFCV cross-ref · Analysis creep/multi-team bias · Regularization & nested CV remedies · UF/UP causes · Summary pitfalls 10.1–10.2 · Human-vs-ML literature synthesis · Hybrid decision foundations (book ch. 11).

Cross-refs: ch04 lifecycle/RNBNFCV, ch05 evaluation/nested CV, ch03 methods, ch12 historical failures.

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Core concepts

- OF/UF are subtle in practice despite simple definitions; misconceptions persist from early ML era. [verified from text, L30560–30573]
- **Teacher example:** Model 9 (catalog instructor flag) achieves 100% train and generalizes to new students; biologically plausible models fail — more variables enable more overfit rules. [verified from text, L30575–30646]
- **Genomics protocols:** Resubstitution (Protocol 1) severely optimistic; **full CV feature selection** (Protocol 2 / RNBNFCV family) unbiased; partial CV (Protocol 3) still biased. [verified from text, L30669–30711]
- OF applies to models, methods, and **protocols** that systematically yield optimistic estimates. [verified from text, L30782–30790]
- **Fundamental asymmetry:** OC often more dangerous than UF because deployment proceeds on inflated confidence. [verified from text, L30828–30849]

### Error estimation and validation

- Single holdout validation behaves like a single hypothesis test with poorly controlled family-wise error when many models/hyperparameters explored — **"Single Split Testing Known"**. [verified from text, L31067–31078]
- **NCV/NFCV/RNBNFCV** approximates nested train/test separation; still biasing if feature selection uses full dataset (compare PCA-on-all-data vs selection inside folds). [verified from text, L31111–31213]
- Holdout/NCV also biased under **selective reporting** of best splits. [verified from text, L31235–31251]
- Biased protocols can be detected via **label reshuffling** (performance should collapse when labels permuted). [verified from text, L32283–32302]

### Practice pathologies

- **Analysis creep:** iterative consultant/manager loops re-analyze until desired result — related to file-drawer and publication bias. [verified from text, L31453–31489]
- Uncorrected multiple testing across features/models inflates false discoveries; terms "data dredging/fishing" often mislead non-technical audiences about intentional misconduct vs procedural flaw. [verified from text, L31383–31414]
- **Multi-team benchmark competitions** without coordinated unbiased protocols recreate analysis creep at scale. [verified from text, L31518–31537]
- Normalization requiring **entire-sample statistics** leaks test information — must use train-only or batch-safe transforms. [verified from text, L31555–31569]

### Remediation toolkit

- **Regularization** (Lasso, SVM), **dimensionality reduction**, **feature selection**, Bayesian priors, algorithmic capacity control, **nested CV**, optimism-corrected bootstrap, **FDR** (not Bonferroni), procedural locking/open-box publication, coordinated multi-team RNBNFCV, standardized pipelines. [verified from text, L31805–32157]
- UF/UP: expand hyperparameter search, use domain-appropriate methods, power/learning-curve analysis, compare N-of-1 to population models. [verified from text, L31648–31729, L32157–32267]

### Human with machine (bundled ch. 11)

- Meta-analyses across neurosurgery, oral cancer, depression, vascular surgery, suicide risk, chest pain, and imaging show ML often **outperforms logistic regression and clinical scores**; high-dimensional inputs favor machines. [verified from text, L33408–33469]
- **Grove et al. (2000):** mechanical prediction equaled or beat clinicians in 84–94% of studies; early CADx abdominal pain 71.6% → 91.8% with tool. [verified from text, L33499–33510]
- **Pitfall 11.1:** Lab-level expert parity does **not** imply deployability, in-practice performance, or clinically meaningful metrics. [verified from text, L33520–33530]
- Human biases: reconstructive memory (not storage), context/order effects, prospect-theory deviations from MEU, heuristics (representativeness, law of small numbers, availability, anchoring). [verified from text, L33565–33700+]
- ML biases arise from data design, inductive bias mismatch, and protocol OC — **fundamentally different** and differently controllable. [verified from text, L33562–33564, L33800+]
- **Error-domain complementarity:** three scenarios — independent errors (routable), perfect overlap (uncorrectable), partial overlap — motivate hybrid routing. [verified from text, L33900–33919]
- Combination mechanisms: weak-learner ensembles, target-function regional human knowledge, **ROC convex hull**, **stacking** (base learners include human or human-mimic models). [verified from text, L33921–33980]
- **Table 2 strategies S1–S10:** modeled hybrids S1–S8 (S5/S6/S7/S8 **FIRST** priority for predictive optimality); pure computer S9 / pure human S10 **THIRD**; blinding/randomization mitigates automation bias and gaming risk. [verified from text, L33982–34086]
- **Human risks in hybrid CDS:** automation bias (rubber-stamping), alert fatigue, decision fatigue, workflow/context sensitivity — harder to control than ML-only deployment. [verified from text, L34088–34160]
- Empirical hybrid gains: CADe skin-lesion study 66% expert → 72.1% with AI; Haynes CDS reviews show provider-performance improvements (patient outcomes mixed). [verified from text, L34107–34125]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/simon_aliferis_healthcare_2024.txt` |
| **Lines read** | 30521–34536 (inclusive) |
| **Chapter boundary** | Starts book ch. 10 abstract (L30521); includes full book ch. 11; L34535–34536 = ch. 12 header only (deferred to simon-ingest-ch07-09 worker) |
| **Wrong-file flag** | `false` |
| **Sections deferred** | Book ch. 12 opening (historical failures) — 2 lines at slice tail; deep cognitive-bias catalog in ch. 11 summarized |
| **Figures** | ANN error curve, genomics protocol schematic, regression surfaces — placeholders |
| **Amnesiac rule** | ISBN from manifest |

## Pedagogy

### Learning objectives

1. Distinguish OF, UF, OC, and UP at model, method, and protocol levels.
2. Explain the **teacher thought experiment** and genomics **Protocol 1–3** bias hierarchy.
3. Diagnose **CV contamination** from preprocessing, feature selection, and imputation leakage.
4. Articulate why **single holdout** is insufficient for model selection under multiple comparisons.
5. Deploy **RNBNFCV/FDR/regularization** as coordinated OC-prevention stack.
6. Recognize **analysis creep** and multi-team benchmark failure modes.
7. Summarize evidence on **ML vs human** performance and hybrid decision rationale.

### worked_examples_present

**Y** — Canonical pedagogical demonstrations:

| Example | Section | Role |
|---------|---------|------|
| Who Is the Teacher? table | Intro Ex 1 | Overfit vs generalizable rules |
| ANN epoch error curve (Fig. 1) | Intro Ex 2 | Training duration OF |
| Genomics Protocol 1–3 | Intro Ex 3 | Feature-selection CV bias |
| Polynomial regression surfaces | Intro Ex 4 | Model complexity |
| PCA-on-full-data vs nested | CV contamination | Preprocessing leakage |
| Label reshuffling test | Detection | Sanity check for signal |
| Consultant analysis-creep vignette | Classroom | Sequential p-hacking analog |
| COVID temporal shift assignment | Classroom | Distribution shift OC |

### exercise_hooks

- Large **classroom assignment** set (Rich Simon protocol variants, reshuffling, COVID OF/UP, capacity-control combinations, active learning bias, exploratory vs confirmatory modeling).
- **Instructor hooks `[inferred]`:**
  - Reproduce Protocol 1 vs 2 error bias on synthetic high-D classification.
  - Run label-reshuffling test on a teammate's published pipeline.
  - Audit a Kaggle medical competition for multi-team analysis creep.
  - Debate hybrid vs full automation for one diagnostic pathway using ch. 11 evidence.

## Operator hooks

### 1. w3_clinical_docs — overfitting/OC canon

Selective ch06 is the **w3 falsifiability gate**: pairs with **simon ch05** error estimation and **simon ch04** RNBNFCV lifecycle mandate. Essential before trusting any clinical ML generalization claim. **Label reshuffling** and **nested CV** are operator-checklist items for chart-review ML and EHR models.

### 2. MDCalc / clinical-adjacent alignment

**[high]** — Directly addresses clinical ML failure modes:

- **Never ship on resubstitution or single split** when feature selection/tuning occurred.
- **OC > UF risk:** inflated AUC on convenience samples → harmful deployment.
- **Temporal shift** (COVID assignment): monitoring requirement for production clinical scores.
- **Human–machine hybrid:** supports human-in-the-loop guardrails without rejecting automation.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **ai_engineering_2025 ch04** | Medium | Eval contamination, slice analysis; Simon adds genomics protocols + NHST analogy |
| **designing_ml_systems_2022** | Medium | Train/serve skew; Simon adds multi-team creep |
| **grokking_algorithms_2e_2024** | Low | No OF depth |
| **responsible_ai_practice_2025** | Low–medium | Hybrid human-AI governance |

**Dedup:** Canonical w3 reference for **OC/OF mechanisms + RNBNFCV + analysis creep**; ch. 11 bundled for human–ML synthesis only.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — four intro experiments + contamination traces |
| Exercise hooks | **Strong** — advanced classroom set |
| Chapter boundary | **Bundled** — ch. 11 + 2 lines of ch. 12 header |
| Ingest suitability | **High** — prescriptive BPs, empirical protocols cited |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2024 clinical ML |
| **Author authority** | **PASS** | Primary genomics OF protocols (Simon et al.); Harrell/Braga-Neto citations |
| **Primary-source citation density** | **PASS** | Simon genomics CV paper, Benjamini-Hochberg FDR, Ghassemi reproducibility, Steyerberg |
| **Contested claims flagged** | **PASS** | Bonferroni deprecated; single-split NHST analogy; ML-vs-human meta-analysis limits noted |
| **Worked examples** | **PASS** | Four introductory experiments + detection tests |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| SIM-C06-001 | Full CV feature selection required for unbiased genomics error estimates | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Protocol 1–3 |
| SIM-C06-002 | Overconfidence poses greater deployment risk than underfitting | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | OC vs UF |
| SIM-C06-003 | Single holdout under multiple model comparisons inflates effective alpha | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Single split testing |
| SIM-C06-004 | Preprocessing on full data (e.g., PCA) contaminates CV error estimates | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | CV contamination |
| SIM-C06-005 | RNBNFCV is recommended iterative modeling protocol | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Remediation |
| SIM-C06-006 | Label reshuffling should collapse performance if signal is real | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Detection |
| SIM-C06-007 | Hybrid human–machine can exceed either alone in high-D clinical tasks | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39354-9 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Human with machine |
| SIM-C06-008 | Lab performance parity does not guarantee clinical deployability (Pitfall 11.1) | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39355-6 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Pitfall 11.1 |
| SIM-C06-009 | S5–S8 hybrid strategies prioritized over pure human or pure ML (Table 2) | compressed | Simon/Aliferis 2024 | ISBN 978-3-031-39355-6 | literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch06_ingest.md | Hybrid strategies |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `simon-ingest-ch04-06` · word cap ≤4500*
