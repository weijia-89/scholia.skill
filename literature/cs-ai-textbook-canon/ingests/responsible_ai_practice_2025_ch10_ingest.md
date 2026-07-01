# Chapter ingest — `responsible_ai_practice_2025` · Chapter 10

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
| **chapter_number** | 10 |
| **chapter_title** | Case Study |
| **page_range** | Printed pages absent from text export; logical span L5394–6374 (chapter body; appendix deferred) |
| **parent_book_title** | Responsible AI in Practice |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1_10 |
| **collaborator** | Golnoosh Babaei (code/case study) |

## Scope

Chapter 10 is the **book capstone**: a high-risk **consumer credit default** classification case study applying the full SAFE-HAI metric family via the `safeaipackage` Python toolbox. It walks through logistic regression, decision trees, random forests, and neural networks on a six-predictor dataset; compares models via confusion matrices and AUROC; then runs RGA (accuracy), RGE (explainability), RGR (robustness), and RGF (fairness) modules. Closes with book-level SAFE-HAI synthesis and governance callback to Ch. 9.

**Sections ingested:** Problem framing · Dataset (Tables 10-1, 10-2) · Logistic regression (coefficients, significance, reduced model) · Tree/RF models (Fig. 10-1, 10-2) · Neural network overview · Model comparison (confusion matrix, ROC/AUROC) · SAFE-HAI assessment (`pip install safeaipackage`) · Book conclusion.

**Slice boundary:** Stops at chapter conclusion (L6374); appendix footnotes from L6375 deferred.

Cross-refs: Babaei et al.⁶⁸ (related case study); Ch. 2–7 SAFE-HAI metrics; Ch. 9 governance; prior credit examples in Ch. 4 (European SME).

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Problem and data

- **High-risk application:** credit loan grant decision via credit scoring; probability of default ∈ [0,1] linked to ordinal rating (L5416–5438).
- **Objectives:** evaluate accuracy of LR, RF, NN; explainability; fairness; robustness (L5440–5467).
- **Dataset:** binary `default` response; six predictors — interest rate, installment, log annual income, DTI, FICO, days of delay (L5477–5487).
- **Default rate:** 19.5% (L5524–5526).
- **Data-size inconsistency `[contested in chapter]`:** narrative cites n=6707 training observations (L5477–5478) but Table 10-2 `count` = 9578 for all variables (L5548–5551). Treat counts as export/OCR ambiguity; do not cite a single n without re-verifying source data.

### Logistic regression

- Fitted model (L5630–5640): log-odds(default) = −1.8327 − 0.1589·installment + 0.0570·log_income + 0.0681·dti − 0.0591·days_delay − 0.9630·FICO + 0.3008·interest_rate.
- Economic interpretation: installment, days late, FICO decrease default odds; income, DTI, interest rate increase — latter two counterintuitive; authors offer post-hoc rationales (more debt elsewhere aids repayment; higher rates incentivize timely pay) (L5642–5657).
- Table 10-3: annual income and days of delay **not significant** individually (L5707–5709).
- Table 10-4: reduced 4-variable model vs full 6-variable — deviance difference p=0.18; models statistically equivalent (L5728–5731).

### Tree models and neural networks

- Classification tree splits primarily on DTI (X4) and FICO (X5) (Fig. 10-1, L5783–5788).
- Trees unstable → random forests average B trees (L5790–5797).
- Variable importance (Fig. 10-2): FICO, days of delay, DTI most important (L5814–5815).
- Neural networks described as accurate but **black-box** / low interpretability (L5846–5847).

### Model comparison — AUROC (narrative ROC section)

| Model | AUROC | Rank |
|-------|-------|------|
| Logistic regression | 0.7612 | 3 |
| Decision tree | 0.70987 | 4 |
| Random forest | **0.8390** | **1** |
| Neural network | 0.8204 | 2 |

(L5971–6024). RF best by AUROC; NN second.

**Confusion matrix example (Table 10-6):** 150-case illustration — accuracy 105/150 = 70% (L5905–5911). Train/test split standard practice for confidentiality (L5913–5918).

### SAFE-HAI package assessment (`safeaipackage`)

Install: `pip install safeaipackage` (GitHub: GolnooshBabaei/safeaipackage) (L6036–6040).

**RGA accuracy (package output — differs from AUROC section):**

| Model | RGA |
|-------|-----|
| Logistic regression | 0.593 |
| Decision tree | 0.710 |
| Random forest | 0.731 |
| Neural network | 0.683 |

(L6054–6106). Text states RGA=AUROC for binary response (L6049–6050) yet numeric RGA values **do not match** AUROC figures above — `[contested in chapter]` likely different splits, model specs, or export error; operators must reconcile on raw code before citing ranks.

**RGE explainability (per-variable, highest = FICO across all models):**

- Logistic: FICO 0.326, installment 0.055, annual_income 0.019 (L6126–6142).
- Tree: FICO 0.338, days_of_delay 0.303 (L6155–6167).
- RF: FICO 0.200, days_of_delay 0.097 — installment least important (L6182–6200).
- NN: FICO 0.249, interest_rate 0.164 (L6213–6225).

**RGR robustness (`rgr_all()` perturb all variables):**

| Model | RGR |
|-------|-----|
| Logistic | 0.491 |
| Decision tree | **0.519** |
| Random forest | 0.475 |
| Neural network | 0.467 |

(L6237–6283). Decision tree ranked most robust despite lower AUROC.

**RGF fairness** — protected attribute: annual income (binary low/high vs mean):

| Model | RGF |
|-------|-----|
| Logistic | 0.926 |
| Decision tree | 0.922 |
| Random forest | **0.972** |
| Neural network | 0.925 |

(L6294–6337). RF highest fairness on this grouping.

### Multi-criteria conclusion tension

No single model wins all SAFE-HAI dimensions: RF best AUROC and RGF; decision tree best RGR; logistic competitive on explainability concentration. Operators must trade off per regulatory context (EU AI Act high-risk credit scoring).

### Book closing synthesis (L6339–6373)

- SAFE-HAI extends Duke (2023) framework with accuracy, security, sustainability; human rights emphasis for minority groups (L6349–6359).
- Rank Graduation metrics = novel unified measurement approach (L6357–6359).
- Governance processes (Ch. 9) required for proper development/deployment (L6361–6366).
- Responsible AI adoption must scale with AI adoption or harms proliferate (L6368–6373).

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **Lines read** | 5394–6374 (chapter body) |
| **Chapter boundary** | Starts DOI anchor ch.10 (L5394); chapter prose ends L6374; appendix L6375+ deferred |
| **wrong-file flag** | `false` |
| **Tables/figures** | Tables 10-1–10-6; Figs 10-1–10-5 (ROC curves) — alt-text in export |
| **Code blocks** | `safeaipackage` API calls for Accuracy, Explainability, Robustness, Fairness classes |
| **Sections deferred** | Appendix footnotes (L6375+); full bibliography |

## Pedagogy

### Learning objectives

1. Frame credit default scoring as a high-risk AI application under SAFE-HAI.
2. Fit and interpret logistic regression for binary default with significance testing and model reduction.
3. Compare tree, random forest, and neural network classifiers using confusion matrices and AUROC.
4. Run `safeaipackage` modules for RGA, RGE, RGR, and RGF on the same models.
5. Reconcile multi-metric trade-offs when no model dominates all principles.
6. Connect case-study workflow to Ch. 9 governance and book-level SAFE-HAI synthesis.

### worked_examples_present

**Y** — Full procedural capstone:

| Example | Section | Role |
|---------|---------|------|
| Table 10-1 sample rows | Data overview | Schema |
| Logistic coefficients + deviance test | LR application | Inference |
| Fig. 10-1 decision tree | Tree models | Splits |
| Fig. 10-3 ROC Model 1 vs 2 | ROC intro | AUROC intuition |
| Figs 10-4–10-5 per-model ROC | Model comparison | AUROC ranking |
| `check_accuracy` / `rga()` outputs | SAFE-HAI accuracy | Package walkthrough |
| `rge()`, `rgr_all()`, `rgf()` outputs | Explainability/robustness/fairness | Multi-metric assessment |

### exercise_hooks

- No formal end-of-chapter problem set.
- **Operator drill ideas `[inferred]`:**
  - Reproduce AUROC and RGA on one public credit dataset; document why ranks may diverge.
  - Run SAFE-HAI four-metric matrix; pick model under EU AI Act explainability vs accuracy priority.
  - Audit DTI/interest-rate coefficient signs against domain experts — challenge post-hoc rationales.
  - Map Ch. 10 workflow to NAM sec05 local validation + algorithmovigilance checklist.
  - Extend fairness analysis beyond income binary split (intersectional protected attributes).

## Operator hooks

### 1. w4_ops_governance — SAFE-HAI procedural capstone

Integrates **ch02–07 metrics** into one runnable pipeline. Pairs naturally with:

| Canon | Relationship |
|-------|--------------|
| **RAI ch09** | Governance structure precedes case-study measurement |
| **RAI ch04** | RGE explainability theory; ch10 applies `check_explainability` |
| **RAI ch02** | RGA/AUROC theory; ch10 applies `check_accuracy` |
| **NAM sec05** | Post-deploy monitoring + local validation after model selection |
| **simon_aliferis_healthcare_2024 ch03–06** | Rigorous clinical ML evaluation contrast (nested CV, net benefit) |

**Not a clinical ingest** — consumer credit domain; methodology portable to risk scoring with domain re-validation.

### 2. MDCalc / clinical-adjacent alignment

**[medium]** — Pattern-portable, not clinical case study:

- **High-risk scoring template** — multi-metric gate before deploy maps to clinical decision support diligence.
- **No single winner** — reinforces Simon/NAM requirement for fit-for-purpose metric selection, not AUROC-only.
- **Fairness on income proxy** — illustrates protected-attribute testing; clinical fairness needs richer attributes.
- **`safeaipackage`** — executable hook for phylax provenance rows; verify package version and data n before production claims.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **RAI ch02–07** | High | ch10 applies prior-chapter metrics |
| **RAI ch04** | High | European SME credit + RGE theory |
| **simon ch05–06** | Medium | Evaluation rigor; Simon adds clinical metrics |
| **ai_engineering_2025 ch04** | Low–medium | Eval pipeline; different stack |

**Dedup:** Canonical for **end-to-end SAFE-HAI `safeaipackage` walkthrough** on credit data.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — full ML + SAFE-HAI code outputs |
| Exercise hooks | **Strong** — multi-metric trade-off drills |
| Chapter boundary | **Clean** — case study + book close; appendix excluded |
| Ingest suitability | **High** — w4 capstone with executable package hook |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2025 Springer/Apress |
| **Author authority** | **PASS** | Duke + Giudici + Babaei (`safeaipackage` SSRN line) |
| **Primary-source citation density** | **PASS** | Babaei et al.⁶⁸; Lorenz/Gini lineage; logistic/tree/ROC standard refs in appendix |
| **Contested claims flagged** | **PASS** | n=6707 vs 9578; AUROC vs RGA rank mismatch; counterintuitive LR coefficients |
| **Worked examples** | **PASS** | Full credit case + package API |

**Overall TEXTBOOK-Q1:** **PASS** — suitable w4 capstone; operators must reconcile metric discrepancies on source code.

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| RAI-C10-001 | Credit default case applies SAFE-HAI via safeaipackage | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch10_ingest.md | Framing |
| RAI-C10-002 | Random forest AUROC 0.8390 best among four classifiers | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch10_ingest.md | AUROC comparison |
| RAI-C10-003 | Reduced logistic model equivalent to full (p=0.18) | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch10_ingest.md | Model reduction |
| RAI-C10-004 | FICO highest RGE across all models | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch10_ingest.md | Explainability |
| RAI-C10-005 | Decision tree highest RGR; RF highest RGF on income split | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch10_ingest.md | Robustness/fairness |
| RAI-C10-006 | safeaipackage installable via pip from GolnooshBabaei repo | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch10_ingest.md | Package |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `rai-ingest-ch09-10` · word cap ≤4500*
