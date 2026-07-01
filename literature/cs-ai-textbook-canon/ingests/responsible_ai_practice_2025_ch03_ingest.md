# Chapter ingest — Responsible AI in Practice, Chapter 3 (Robustness)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Responsible AI in Practice |
| **authors** | Toju Duke, Paolo Giudici |
| **edition** | 1st (Apress / Springer Nature, 2025) |
| **ISBN_print** | 979-8-8688-1165-4 |
| **ISBN_electronic** | 979-8-8688-1166-1 |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1 |
| **chapter_number** | 3 |
| **chapter_title** | Robustness |
| **page_range** | [not in text export] |
| **parent_book_title** | Responsible AI in Practice |
| **source_type** | textbook |
| **text_path** | literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt |
| **pdf_path** | [not staged on disk] |

## Scope

Chapter 3 defines **robustness** as stability of ML output under intentional (adversarial/cyber) and unintentional (extreme-event) perturbations—the reliability complement to ch.2 accuracy. Anchors on ISO/IEC TS 5723:2022 generalizability, NIST RMF (valid vs reliable; links to security, resilience, safety), and EU AI Act high-risk robustness/cybersecurity lifecycle requirements (data/model poisoning, adversarial manipulation, fail-safe). Develops **Rank Graduation Robustness (RGR)** via perturbed concordance curves; covers ex-post perturbation measurement and ex-ante model-comparison methods (PCA, stepwise selection, ridge/lasso regularization, Shapley-ordered selection); compares linear regression, regression tree, and random forest under outlier perturbations (Tables 3-4, 3-5); surveys **RobustBench** adversarial benchmark and Bai et al. adaptive smoothing tradeoff; provides scoring rubric and mitigation (EDA, preprocessing, feature engineering, cross-validation, research awareness).

Out of scope: explainability (ch.4); full adversarial-attack taxonomy deep dive; case-study Python appendix.

## Key findings

All claims **[verified from text]** from lines 2085–2862 unless tagged `[inferred]`.

1. **Robustness definition.** Sturdiness against uncertainties/perturbations; perform accurately across contexts; NIST: reliable AI must be robust while valid AI must be accurate. ISO: "ability … to maintain level of performance under a variety of circumstances." (lines 2112–2141)

2. **Trustworthiness linkage.** Robustness underpins reliability, security (unauthorized access, adversarial attacks, data poisoning), resilience, and indirectly safety (health/property/environment harms from unexpected failures). (lines 2143–2156)

3. **EU AI Act robustness.** High-risk systems need appropriate robustness/cybersecurity; resilience against errors/faults/inconsistencies; technical fail-safe against training-data poisoning, model poisoning, adversarial attacks, leakage/confidentiality attacks. NIST-aligned question: protect against cyber/adversarial attacks and optimizer-induced responses. (lines 2158–2178)

4. **Measurement concept.** Robust model = limited output variation under perturbation; classification: correctly classify large proportion under input variations within distance bound (Croce et al. 2023). Simpler models often more robust; bias-variance trade-off (Hastie et al. 2023): simple models higher bias, lower variance. (lines 2181–2203)

5. **Ex-post variability metrics.** Resampling train-test partitions → prediction variance/percentiles (continuous) or entropy/Gini (categorical). Babaei & Giudici (2024) Lending Club example: classic logistic AUROC 0.75 (30k examples) vs GPT 0.61 vs informed-GPT 0.67 (80 examples); wide min-max ranges signal low robustness especially for GenAI. (lines 2219–2292)

6. **RGR measure.** Extends RGA: compare concordance curves from original vs perturbed prediction ranks; RGR = sum(Q'i−QPi)/sum(Q'i−Qi); normalized [0,1]; U-statistic/DeLong tests for thresholds. Worked examples: predictive RGR 0.75 (Table 3-2); classification RGR 68% limited robustness (Table 3-3). Python: `check_robustness`, `rgr.single`, `rgr.all` with tail-swap perturbations (default 5%). (lines 2294–2458)

7. **Ex-ante model comparison.** Dimensionality reduction (PCA; correspondence analysis for categorical); stepwise forward/backward selection with AUROC/RMSE stopping rules; ridge/lasso regularization formulas; Shapley-value ordering when probabilistic structure absent. Goal: parsimonious models stable against extreme variation. (lines 2460–2632)

8. **RGR model-comparison findings.** One-predictor perturbation (15% tail outliers): RGR linear 0.7976, tree 0.8137, random forest 0.9683 — random forest significantly more robust (p<0.001). Four-predictor case: linear 0.7449, tree 0.9395, forest 0.9782 — tree robustness degrades with complexity; forest recommended. `[contested in chapter]` Black-box ensemble may outperform white-box on stability in these simulations. (lines 2634–2725)

9. **RobustBench benchmark.** Croce et al.: standardized adversarial robustness via AutoAttack (white+black box); GitHub leaderboard 120+ evaluations; model zoo 80+ models; analyzes robustness impact on distribution shift, calibration, OOD detection, fairness, privacy, smoothness, transferability. `[contested]` Accuracy–robustness tradeoff; Bai et al. (2023) adaptive smoothing MoE mixes standard + robust classifiers to reduce accuracy penalty. Benchmarks useful but **cannot replace** RGR in risk management (mirrors ch.2). (lines 2727–2771)

10. **Scoring rubric & mitigation.** Same band structure as ch.2 (Excellent 75–90% … Poor 0–40%). Mitigation: EDA/outlier understanding; preprocessing (normalization, class imbalance); feature engineering; cross-validation against overfitting; stay current on GenAI jailbreak research. (lines 2773–2848)

## Chapter digest

| Subtopic | Lines (approx.) | Takeaway |
|----------|-----------------|----------|
| Definitions & policy | 2101–2178 | Robustness = reliability; EU/NIST security requirements |
| Variability & GenAI | 2219–2292 | Resampling ranges; GPT vs classic model instability |
| RGR methodology | 2294–2458 | Perturbed Lorenz concordance; Python perturbation API |
| Model selection | 2460–2632 | PCA, stepwise, ridge/lasso for parsimony |
| RGR comparisons | 2634–2725 | Random forest wins in simulated perturbation studies |
| RobustBench | 2727–2771 | Adversarial SOTA leaderboard; accuracy tradeoffs |
| Rubric & mitigation | 2773–2848 | Score bands; EDA/CV/feature pipeline |

## Pedagogy

### Learning objectives

1. Distinguish accuracy (validity) from robustness (reliability) per NIST framing.
2. Compute and interpret RGR for continuous and binary problems under defined perturbations.
3. Explain bias-variance trade-off and how regularization/stepwise selection improve robustness ex ante.
4. Compare RobustBench adversarial evaluation with RGR statistical compliance measurement.
5. Apply mitigation checklist when rubric score falls below Fair threshold.

### worked_examples_present

**Y** — Lending Club GPT vs logistic AUROC ranges (Table 3-1); RGR predictive (3-2) and classification (3-3) tables; linear/tree/forest RGR comparisons (3-4, 3-5); ridge/lasso formula walkthrough.

### exercise_hooks

1. Run `rgr.single` tail-swap perturbation on a toy dataset and interpret RGR vs RGA from ch.2.
2. Design stepwise stopping rule using DeLong test for a binary clinical classifier.
3. Map EU AI Act fail-safe requirements to a CDS monitoring plan.
4. Debate: when might random-forest robustness simulation findings fail to generalize to neural clinical models?
5. Pair with AIE ch.10: align post-deploy drift monitoring with RGR periodic recompute.

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **lines_read** | 2085–2862 (inclusive) |
| **section_boundary** | Starts at Ch.3 heading (2087); ends before Ch.4 `Explainability` (2865) |
| **wrong_file_flag** | false |
| **deferred** | RGR appendix tests; ch.4 explainability; adversarial attack catalog |
| **figure_placeholders** | None substantive in text layer |

## Operator hooks

### Foundation layer (w4_ops_governance)

**Robustness/reliability spine** completing SAFE "Security" pillar preview from ch.1. Pair with:

- `ai_engineering_2025_ch10_ingest.md` — production monitoring, guardrails
- `ai_engineering_2025_ch04_ingest.md` — eval + drift (accuracy complement)
- `simon_aliferis_healthcare_2024_ch10_ingest.md` — post-market surveillance, input/model drift

### MDCalc alignment

**[relevant]** — pattern-portable robustness discipline:

- **Lifecycle robustness/cybersecurity** (EU AIA lines 2158–2168) → post-deploy monitoring for data poisoning and adversarial inputs on clinical features.
- **Fail-safe / backup plans** (lines 2164–2165) → degraded-mode CDS when model confidence or RGR drops below threshold.
- **Cross-validation & overfitting prevention** (lines 2831–2837) → holdout validation before production calculator updates.
- **GenAI jailbreak awareness** (lines 2843–2847) → if LLM-backed features, robustness testing beyond static accuracy.

**[peripheral]** — RobustBench image-classification leaderboard; transfer concepts cautiously to non-imaging clinical ML.

Do not cite simulated random-forest RGR rankings as MDCalc model-selection policy.

### Redundancy

| Canon | Overlap | Distinction |
|-------|---------|-------------|
| AIE 2025 ch10 | Monitoring, drift, guardrails | RAI = RGR statistical metric + perturbation methodology |
| Simon/Aliferis ch10 | Post-deploy drift, GMLP monitoring | RAI = general ML robustness math, not FDA GMLP mapping |
| NAM GenAI 2025 | Systemic GenAI risks | RAI = quantitative robustness measurement program |
| Duke 2023 | Robustness as RAI pillar | This chapter adds RGR Lorenz extension + Python |

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Anchor density | High — ISO 5723, NIST RMF, EU AIA, Croce/RobustBench, Babaei & Giudici 2024, Hastie, Bai adaptive smoothing |
| Procedural hooks | RGR calculation, perturbation API, model-selection flow — strong cards |
| Boundary | Clean robustness slice; explainability deferred |
| Contested claims | Random forest > white-box robustness (simulation-bound); accuracy–robustness tradeoff |

## TEXTBOOK-Q1 verdict

**PASS** — Standards-anchored definitions; procedural metrics with tables and Python hooks; contested ensemble-robustness and benchmark limits flagged; worked perturbation examples.

---

*Ingest agent: rai-ingest-ch01-03 · ch03 · lines 2085–2862 · word cap ≤4500*
