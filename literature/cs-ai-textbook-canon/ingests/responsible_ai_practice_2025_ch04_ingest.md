# Chapter ingest — `responsible_ai_practice_2025` · Chapter 4

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Responsible AI in Practice |
| **authors** | Toju Duke, Paolo Giudici |
| **edition** | 1st Edition (2025, APress/Springer Nature) |
| **ISBN_print** | 979-8-8688-1165-4 |
| **ISBN_electronic** | 979-8-8688-1166-1 |

## Chapter identification

| Field | Value |
|-------|-------|
| **chapter_number** | 4 |
| **chapter_title** | Explainability |
| **page_range** | Printed pages absent from text export; logical span L2863–3329 |
| **parent_book_title** | Responsible AI in Practice |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1_4 |

## Scope

Chapter 4 is the fourth SAFE-HAI principle in Duke & Giudici's operational Responsible AI framework. It defines explainability against regulatory baselines (NIST AI RMF, EU AI Act), surveys model-native vs post-hoc explanation methods (feature importance, Shapley values, Shapley Lorenz values), and introduces the authors' **Rank Graduation Explainability (RGE)** metric as a normalized, statistically testable alternative to standard XAI post-processing.

**Sections ingested:** Regulatory framing (NIST, EU AI Act) · XAI research landscape · Explainable-by-design vs black-box models · Shapley values & Shapley Lorenz values · Corporate credit-scoring case study (100k+ European SMEs) · Accuracy–explainability–robustness trade-offs · RGE definition, properties, worked table · Scoring rubric (Table 4-2) · Mitigation playbook · `check_explainability` Python hook (appendix ref).

Cross-refs: Ch. 2 (accuracy/AUROC, DeLong test), Ch. 3 (robustness/RGR), Ch. 5 (fairness comparison deferred), Ch. 8 (human oversight), appendix (RGE statistical test code).

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Regulatory and conceptual framing

- Explainability lacks a precise mathematical definition; literature and regulators supply operational definitions — e.g., Bracke et al. (2019): explicit understanding of factors determining ML output. [verified from text, L2887–2892]
- NIST AI RMF distinguishes **explainability** (mechanisms underlying AI) from **interpretability** (meaning of output in designed-purpose context); chapter uses "explainability" for both. [verified from text, L2894–2905]
- EU AI Act ties explainability to **transparency** for high-risk systems and to **human oversight** (Ch. 8 deferred). [verified from text, L2907–2917]
- XAI has become a major research thread (World Conference on Explainable AI cited as reference forum). [verified from text, L2919–2929]

### Model taxonomy and post-hoc methods

- **Explainable by design:** linear/logistic regression (Lasso/Ridge feature selection); tree ensembles expose feature-importance plots. [verified from text, L2931–2938]
- **Typically unexplainable:** neural networks, SVMs — addressable via permutation/reshuffling of explanatory variables. [verified from text, L2939–2943]
- **Shapley values** (Shapley 1953; Lundberg 2017): game-theoretic equitable allocation of prediction among predictors; local then global aggregation. Formula: sum over all variable combinations of marginal prediction change when variable *k* is included vs excluded. [verified from text, L2945–2983]
- **Shapley Lorenz values** (Giudici & Raffinetti 2021): replace Shapley payoff with Gini-coefficient differences (Lorenz zonoids), normalized. [verified from text, L2995–2998]
- Shapley methods are **ex post** (vs Lasso/Ridge **ex ante**); computationally explosive as variable count grows (all combinations *C*). [verified from text, L2985–3007]

### Credit-scoring case study and trade-offs

- Case: >100,000 European SME credit applications; sector default rates vary (Real Estate highest default ~17%). [verified from text, L3028–3040]
- Random-forest variable-importance plot ranks ROE, PLTax, Leverage, EBIT, TAsset, Turnover, Country, Industry. [verified from text, L3042–3071]
- Global Shapley values on logistic regression rank PLTax and EBIT highest; logistic explanations are more **concentrated** (fewer variables matter) despite lower AUROC than random forest. [verified from text, L3073–3110]
- **Three-way trade-off:** random forest wins accuracy; logistic wins explainability concentration; random forest wins robustness after DeLong-based simplification (can drop industry/country; logistic cannot). Fairness comparison deferred to Ch. 5. [verified from text, L3112–3121]

### Rank Graduation Explainability (RGE)

- RGE extends Rank Graduation Accuracy (RGA) from Ch. 2: compare predictions from full model vs model excluding variable *k* via Lorenz/dual-Lorenz/concordance curves on ranked predictions. [verified from text, L3125–3149]
- Formula: `sum(Q'i - QPi) / sum(Q'i - QFi)` where Q'i = dual Lorenz, QFi = Lorenz from full model ranks, QPi = concordance from reduced-model ranks. [verified from text, L3151–3159]
- Properties: normalized; RGE=1 irrelevant variable, RGE=0 variable explains all variability (text also states "RGA=0" — likely typo for RGE=0). [verified from text, L3161–3168]
- Statistical test: complement of sum of RGE values; lower sum → higher explainability; U-statistic test yields p-value vs subjective lower bound. [verified from text, L3174–3181]
- Worked example (Table 4-1, Ch. 2 predictions): RGE=0.75 for one removed variable — moderate explanation. [verified from text, L3185–3205]
- Python: `check_explainability` — per-variable RGE for classification/regression + aggregate significance test (appendix). [verified from text, L3217–3235]

### Scoring rubric and mitigation

- Table 4-2 bands: Excellent 75–90%, Good 70–75%, Fair 60–70%, Borderline 40–60%, Poor 0–40%. [verified from text, L3237–3249]
- RGE is a **collection** per feature (unlike single-statistic RGA/RGR); aggregate by ordering features by RGE and checking how many needed to reach 50% cumulative RGE — threshold is indicative/context-specific. [verified from text, L3251–3272]
- Mitigation if not explainable: (1) model selection / remove correlated features; (2) data quality (outliers, oversampling/undersampling); (3) more data, meta-analysis, synthetic data. [verified from text, L3274–3301]
- Authors claim RGE advantage over Shapley: **normalized**, interpretable as % of model accuracy due to a feature, enabling direct evaluation of mitigation — Shapley lacks this normalization/accuracy link. `[contested in chapter]` — Simon/Aliferis healthcare canon critiques Shapley for causal/clinical explanation (see simon ch04). [verified from text, L3305–3312]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **Lines read** | 2863–3329 (inclusive) |
| **Chapter boundary** | Starts DOI anchor ch.4 (L2863); ends before ch.5 Fairness (L3330) |
| **wrong-file flag** | `false` |
| **Sections deferred** | Human oversight detail (Ch. 8); full Python appendix; fairness comparison (Ch. 5) |
| **Figures** | Sector default bar chart (Fig. 4-1), variable importance (Fig. 4-2), global Shapley (Fig. 4-3) — alt-text in export |
| **Amnesiac rule** | ISBN from L11–13 text export header |

## Pedagogy

### Learning objectives

1. Distinguish explainability vs interpretability per NIST AI RMF and map both to EU AI Act transparency requirements.
2. Classify ML models as explainable-by-design vs requiring post-hoc methods.
3. Compute and interpret Shapley values and Shapley Lorenz values at local and global levels.
4. Apply RGE to quantify per-feature explainability and run the aggregate significance test.
5. Evaluate accuracy–explainability–robustness trade-offs using the corporate credit case study.
6. Use Table 4-2 rubric and mitigation steps when explainability scores are poor.

### worked_examples_present

**Y** — Credit-scoring vignette with three figures, RGE Table 4-1 numerical walkthrough, Shapley game analogy.

| Example | Section | Role |
|---------|---------|------|
| Shapley game analogy (players = predictors) | Shapley intro | Game-theory intuition |
| European SME sector defaults | Measuring explainability | Domain context |
| RF importance vs logistic Shapley | Case study | Method comparison |
| DeLong simplification (Babaei et al. 2023) | Trade-offs | Robustness link |
| Table 4-1 RGE calculation | Model explainability | Procedural numeric example |

### exercise_hooks

- No formal end-of-chapter exercises in text.
- **Instructor hooks `[inferred]`:**
  - Reproduce variable-importance and Shapley rankings on a public credit dataset; compare concentration vs AUROC.
  - Implement RGE for one held-out variable on Ch. 2 Table 2-3 predictions; interpret vs Table 4-1.
  - Debate RGE vs Shapley for a high-stakes decision system — cite Simon Shapley critique.
  - Draft EU AI Act transparency paragraph for a high-risk scoring model using this chapter's rubric.

## Operator hooks

### 1. w4_ops_governance — SAFE-HAI explainability canon

This chapter is the **operational XAI measurement layer** for w4: pairs with **responsible_ai_practice_2025 ch02–03** (RGA/RGR family) and forward-links **ch05** fairness. Cross-corpus: **ai_engineering_2025** eval chapters (mandatory pair per wave plan); **simon_aliferis_healthcare_2024 ch04** Shapley critique is adversarial counterweight — do not treat Shapley as sufficient for clinical/causal narrative.

### 2. MDCalc / clinical-adjacent alignment

**[medium]** — Methodology portable; domain is corporate credit not clinical:

- **Normalized explainability metric (RGE)** usable wherever rank-based model comparison is acceptable.
- **Three-way trade-off** (accuracy/explainability/robustness) applies to clinical risk models but case study is financial.
- **Regulatory hooks:** NIST RMF + EU AI Act transparency language directly quotable for governance docs.
- No employer-stack APIs cited.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **simon_aliferis_healthcare_2024 ch04** | High (XAI) | Simon critiques Shapley; RAI promotes Shapley + proposes RGE |
| **ai_engineering_2025** | Medium | Eval/monitoring patterns; RAI adds SAFE-HAI RGE rubric |
| **nam_gen_ai_health_2025 sec03** | Low–medium | Risk framing; RAI is procedural measurement |

**Dedup:** Treat this ingest as canonical for **RGE explainability metric + SAFE-HAI ch4 rubric** in w4.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — credit case, Table 4-1, Shapley analogy |
| Exercise hooks | **Moderate** — inferred from case + rubric |
| Chapter boundary | **Clean** — single book chapter |
| Ingest suitability | **High** — procedural metric with scoring rubric and code hook |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2025 Springer/Apress; w4_ops_governance wave |
| **Author authority** | **PASS** | Duke (Bedrock AI); Giudici (Univ. Pavia, Lorenz/RGE research line) |
| **Primary-source citation density** | **PASS** | NIST RMF, EU AI Act, Bracke 2019, Shapley 1953, Lundberg 2017, Giudici & Raffinetti 2021, Saranya & Subhashini 2023, Babaei et al. 2023 |
| **Contested claims flagged** | **PASS** | RGE vs Shapley superiority; RGE=0/RGA typo in properties list flagged |
| **Worked examples** | **PASS** | Credit-scoring figures, Table 4-1 RGE walkthrough |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| RAI-C04-001 | NIST distinguishes explainability (mechanisms) from interpretability (output meaning) | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch04_ingest.md | Regulatory framing |
| RAI-C04-002 | Shapley values allocate prediction credit across all predictor combinations | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch04_ingest.md | Shapley values |
| RAI-C04-003 | Logistic regression more concentrated explanations than RF despite lower AUROC | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch04_ingest.md | Trade-offs |
| RAI-C04-004 | RGE compares full vs leave-one-out model predictions via Lorenz curves | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch04_ingest.md | RGE |
| RAI-C04-005 | Explainability rubric bands 75–90% Excellent through 0–40% Poor | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch04_ingest.md | Scoring rubric |
| RAI-C04-006 | RGE normalized and linked to predictive accuracy unlike Shapley | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch04_ingest.md | Mitigation |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `rai-ingest-ch04-06` · word cap ≤4500*
