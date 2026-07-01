# Chapter ingest — `responsible_ai_practice_2025` · Chapter 6

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
| **chapter_number** | 6 |
| **chapter_title** | Privacy |
| **page_range** | Printed pages absent from text export; logical span L3764–4126 |
| **parent_book_title** | Responsible AI in Practice |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1_6 |

## Scope

Chapter 6 addresses **privacy** as a SAFE-HAI principle: preserving individual privacy in ML datasets and supporting **right-to-be-forgotten** style erasure tests. It extends the Rank Graduation metric family to **Rank Graduation Privacy (RGP)**, walks through a four-step train/remove/retrain/compare protocol, applies an employee salary case study (473 bank employees, `stima` R package), and surveys standard privacy-preserving ML techniques (differential privacy, federated learning, homomorphic encryption, adversarial training, MPC).

**Sections ingested:** NIST RMF privacy independence principle · RGP derivation and four-step procedure · Properties and Table 6-1 worked example · Employee dataset classification (salary doubling) and regression (salary growth) · RGP interpretation paradox (high score + significant test) · Scoring rubric (Table 6-2) · Mitigation techniques · `check_privacy` Python hook (Babaei et al. 2024).

Cross-refs: Ch. 2 (Table 2-3 predictions), Ch. 4–5 (RGE/RGF parallel metrics), Ch. 7 (sustainability next), EU AI Act high-risk payroll automation note.

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Privacy framing (NIST / SAFE-HAI)

- ML privacy aims to safeguard sensitive data during development and deployment. [verified from text, L3780–3785]
- NIST AI RMF: AI output should be **as independent as possible from individual observations** — removing one individual (or set) should not materially change output. [verified from text, L3787–3796]
- RGP extends RGA: compare predictions from model trained on **all data** vs model trained **excluding m observations** to be "forgotten." [verified from text, L3798–3807]

### Four-step RGP protocol

1. Fit model on full training set (*N* observations).
2. Predict on test set (*n* observations).
3. Remove *m* observations (*m* < *N*); retrain on *N−m*.
4. Predict on same test set with reduced model.

Compare Ŷ (full) vs Ŷ(−m) (reduced); reorder full-model predictions by ranks of reduced-model predictions (*r*^{−m}). Build Lorenz Q from full ranks *r*, dual Lorenz Q′, concordance QPi from *r*^{−m}. [verified from text, L3821–3853]

### RGP definition and properties

- Formula: `sum(Q'i - QPi) / sum(Q'i - Qi)` — parallel to RGE/RGF structure. [verified from text, L3855–3862]
- RGP=0: removed data **irrelevant**; RGP=1: removed data of **absolute importance**; 0<RGP<1 intermediate. [verified from text, L3866–3869]
- Statistical test: higher RGP → higher value of removed data; smaller p-value → significant vs lower bound (subjective threshold). [verified from text, L3875–3880]
- Table 6-1 (Ch. 2 predictions, data removed): RGP=0.75 → removing training rows reduces model accuracy ~25%. [verified from text, L3884–3905]
- Repeat for multiple forget-sets; average RGP vs subjective compliance threshold. Babaei et al. (2024) implements test in `check_privacy`. [verified from text, L3907–3922]

### Employee salary case study

- **Dataset:** 473 bank employees (`stima` R package); gender, age, education, job category, tenure, minority status, starting/current salary. [verified from text, L3929–3946]
- **Classification:** binary `doubling_salary` (growth rate ≥2); RandomForestClassifier; **EU AI Act high-risk** payroll automation context. [verified from text, L3959–3963]
- Removing obs 10: RGP≈0.944; obs 12: RGP≈0.930 — obs 12 **more valuable** to model (lower RGP). [verified from text, L3976–3986]
- **Interpretation nuance:** High RGP suggests removal barely changes predictions; but p-value for obs 10 = 0.003418 → **reject null** → ranks significantly differ → model **not privacy-compliant** by RGP test. Small dataset (473) makes compliance difficult. [verified from text, L3988–3999]
- **Regression:** salary growth (continuous), RandomForestRegressor; RGP≈0.996 (obs 10) and ≈0.997 (obs 12) — near 1 suggests minimal prediction change from removal, yet p-value for obs 12 = 1.65×10⁻⁸ → again **reject** → not compliant. Both models fail privacy criterion due to limited data. [verified from text, L4001–4034]

### Scoring rubric and mitigation

- Table 6-2 bands (**stricter than prior chapters**): Excellent 95–100%, Good 90–95%, Fair 80–90%, Borderline 70–80%, Poor 0–70%. [verified from text, L4036–4048]
- Mitigation techniques (survey level):
  1. **Differential privacy** — noise/perturbation for aggregate release without PII leakage.
  2. **Federated learning** — local training, aggregated updates without raw data sharing.
  3. **Homomorphic encryption** — compute on encrypted data.
  4. **Adversarial training** — robustness vs privacy/security attacks.
  5. **Secure multi-party computation (MPC)** — joint computation without revealing inputs.
  - Apple, Google, IBM cited as adopters. [verified from text, L4050–4117]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **Lines read** | 3764–4126 (inclusive) |
| **Chapter boundary** | Starts ch.6 DOI (L3764); ends before ch.7 Sustainability (L4127) |
| **wrong-file flag** | `false` |
| **Sections deferred** | Full Babaei 2024 notebook/GitHub details; footnote 46–47 full text |
| **Figures** | None beyond tables in export slice |
| **Amnesiac rule** | ISBN from L11–13 header |

## Pedagogy

### Learning objectives

1. State NIST AI RMF independence-from-individuals privacy principle.
2. Execute the four-step RGP protocol for leave-one-out (or leave-m-out) erasure tests.
3. Interpret RGP magnitude vs p-value tension on small-sample models.
4. Apply Table 6-2 privacy rubric (note stricter bands vs ch4–5).
5. Name five privacy-preserving ML techniques and their deployment trade-offs.
6. Connect payroll automation example to EU AI Act high-risk classification.

### worked_examples_present

**Y** — Table 6-1 numeric RGP, employee dataset classification + regression with specific observation removals.

| Example | Section | Role |
|---------|---------|------|
| Table 6-1 RGP=0.75 | RGP definition | Procedural walkthrough |
| Obs 10 vs 12 removal (classification) | Employee case | RGP + p-value paradox |
| Salary growth regression | Employee case | Continuous-target RGP |

### exercise_hooks

- No formal end-of-chapter exercises.
- **Instructor hooks `[inferred]`:**
  - Run leave-one-out RGP on a small UCI dataset; plot RGP vs p-value for each row.
  - Compare RGP compliance threshold to differential-privacy ε budget concept (external reading).
  - Draft erasure-test protocol for an HR analytics model citing EU AI Act high-risk language from text.
  - Evaluate when federated learning vs MPC fits a multi-hospital vs multi-bank scenario.

## Operator hooks

### 1. w4_ops_governance — SAFE-HAI privacy canon

Completes the **Rank Graduation metric quartet** (RGA ch2, RGR ch3, RGE ch4, RGF ch5, **RGP ch6**) for w4 operational governance. Pairs **responsible_ai_practice_2025 ch09** (governance processes) at wave level; privacy **human-rights link** from ch5 intro carries forward.

### 2. MDCalc / clinical-adjacent alignment

**[medium]** — Employee payroll not clinical, but patterns apply to **small-N health ML**:

- **RGP erasure test** as operational right-to-be-forgotten check before deployment.
- **High RGP + significant p-value** paradox — auditors must use both, not RGP alone.
- Small cohort warning (473 employees ≈ small clinic dataset) directly relevant to EHR models.
- Differential privacy / federated learning named for multi-site health data — no implementation detail.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **responsible_ai_practice_2025 ch04–05** | High | Same RGA/Lorenz metric family |
| **simon_aliferis_healthcare_2024** | Low | HIPAA/de-identification not covered here |
| **nam_gen_ai_health_2025 sec03** | Medium | Privacy risk in gen-AI health |

**Dedup:** Canonical for **RGP metric + erasure-test protocol + privacy rubric** in w4 RAI track.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — employee case with explicit RGP values |
| Exercise hooks | **Moderate** — inferred |
| Chapter boundary | **Clean** |
| Ingest suitability | **High** — RGP/p-value tension preserved, mitigation survey |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2025; w4 wave |
| **Author authority** | **PASS** | Duke/Giudici; Babaei et al. 2024 code line |
| **Primary-source citation density** | **PASS** | NIST AI RMF, Babaei et al. 2024, footnotes 46–47, industry DP/FL/MPC refs |
| **Contested claims flagged** | **PASS** | RGP magnitude vs p-value interpretation on small N; rubric bands differ from ch4–5 |
| **Worked examples** | **PASS** | Table 6-1, employee classification/regression |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| RAI-C06-001 | NIST privacy: output should be independent of individual observations | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch06_ingest.md | Privacy framing |
| RAI-C06-002 | RGP compares full-data vs reduced-data model predictions via Lorenz ranks | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch06_ingest.md | RGP protocol |
| RAI-C06-003 | RGP=0 irrelevant data; RGP=1 absolutely important data | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch06_ingest.md | RGP properties |
| RAI-C06-004 | High RGP with significant p-value still fails privacy compliance (small N) | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch06_ingest.md | Employee case |
| RAI-C06-005 | Privacy rubric Excellent 95–100% (stricter than explainability/fairness) | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch06_ingest.md | Scoring rubric |
| RAI-C06-006 | Mitigation: DP, federated learning, homomorphic encryption, adversarial training, MPC | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch06_ingest.md | Mitigation |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `rai-ingest-ch04-06` · word cap ≤4500*
