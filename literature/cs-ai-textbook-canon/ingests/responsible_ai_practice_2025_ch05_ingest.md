# Chapter ingest — `responsible_ai_practice_2025` · Chapter 5

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
| **chapter_number** | 5 |
| **chapter_title** | Fairness and Human Rights |
| **page_range** | Printed pages absent from text export; logical span L3330–3763 |
| **parent_book_title** | Responsible AI in Practice |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1_5 |

## Scope

Chapter 5 covers the fifth SAFE-HAI principle: **fairness** in relation to **human rights** (non-discrimination). It surveys competing fairness notions in ML literature (group, individual, counterfactual), applies corporate and consumer credit case studies, exposes **Simpson's paradox** in marginal vs conditional fairness assessments, and introduces **Rank Graduation Fairness (RGF)** as the authors' normalized, statistically testable fairness metric (parallel to RGE/RGA family).

**Sections ingested:** Motivation (AI harms, discrimination) · Literature survey (Teodorescu 2021, Horesh et al. 2020, Karimi/FairMatch 2022, Grabowicz 2022, Jiang & Nachum 2024) · Corporate SME fairness (Shapley Lorenz Lorenz curves, conditional vs marginal) · HMDA consumer lending case (157k NY 2017 applications) · Simpson's paradox · RGF definition, properties, Table 5-1 · Scoring rubric (Table 5-2) · Mitigation · `check_fairness` Python hook · Generative-AI extension note.

Cross-refs: Ch. 4 (RGE, Shapley Lorenz, corporate credit dataset), Ch. 2 (Table 2-6 classifications, DeLong test), Ch. 6 (privacy next).

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Fairness landscape and human-rights framing

- Responsible AI aims to mitigate harms to individuals, organizations, environment — including **human-rights violations** (non-discrimination, privacy). This chapter focuses on **discrimination/fairness**. [verified from text, L3355–3362]
- **No universal fairness measure**; multiple notions coexist in literature. [verified from text, L3364–3367]
- **Group fairness** (Teodorescu 2021): statistical fairness on imbalanced credit data; typical ML models cannot satisfy more than one fairness criterion when multiple protected variables present — requires human trade-off decisions. [verified from text, L3369–3384]
- **Individual fairness** (Horesh et al. 2020): paired consistency score without explicit protected variable; implicit discriminatory correlates. [verified from text, L3386–3397]
- **Counterfactual/FairMatch** (Karimi et al. 2022): PSM matching for similar/dissimilar individuals; improves individual and group fairness on four datasets. [verified from text, L3399–3408]
- **Fairness–explainability link:** Grabowicz et al. (2022) combine both; Jiang & Nachum (2024) on bias removal — authors follow similar integrated approach. [verified from text, L3410–3416]

### Corporate credit — conditional vs marginal fairness

- Same >100k European SME dataset as Ch. 4; 3D scatter of leverage/EBIT/P-L by country (Italy, France, Spain, Germany). [verified from text, L3426–3445]
- **Conditional fairness:** ML fair when explanatory variable (e.g., leverage) has **same effect on output** across groups — linked to individual fairness. [verified from text, L3465–3472]
- **Marginal (unconditional) fairness:** same **output** across population groups — group-based fairness. [verified from text, L3468–3472]
- Shapley Lorenz Lorenz curve (Fig. 5-2): real case near maximum fairness line; country-level accuracy trends (Fig. 5-3) also similar — but structural differences (e.g., fewer German firms in sample due to reporting rules) mean lower accuracy ≠ bias; conditional Shapley analysis reveals small leverage bias. Model deemed **conditionally fair**. [verified from text, L3490–3502]

### Consumer lending — HMDA and Simpson's paradox

- **HMDA 2017 New York:** 157,269 loan applications; target `declined_loan` = 1 if GSE/FHA requirements met but lender still rejected. [verified from text, L3511–3525]
- Protected variable: race (African American=1, White=0); controls include gender, income, loan amount, purpose, lien, FHA/GSE type. [verified from text, L3527–3537]
- ~8% African American; race highly correlated with loan amount → **Simpson's paradox**: fair marginally, unfair conditionally on loan amount. [verified from text, L3539–3561]
- Agarwal et al. (2023) + Shapley Lorenz: RF more fair than logistic **marginally**; authors extend with conditional split by mean loan amount. [verified from text, L3563–3590]
- **High loan amount subsample:** race ranks **1st** of six variables, explains **91%** of declined loans (RF). **Low amount:** race 5th, ~1%. Combined: race explains ~3% — marginal appearance of fairness masks conditional unfairness. [verified from text, L3581–3596]
- RGF proposed as **conditional** metric avoiding paradox; easier to compute than full Shapley workflow. [verified from text, L3598–3600]

### Rank Graduation Fairness (RGF)

- Extends RGA: compare predictions from full model vs model **excluding protected variable** via Lorenz curves on ranks. [verified from text, L3604–3624]
- Formula: `sum(Q'i - QPi) / sum(Q'i - QFi)` — same structural form as RGE but semantic focus on protected attribute removal. [verified from text, L3626–3633]
- Properties: RGF=0 **unfair** (protected variable reverses ranks); RGF=1 **fair** (no rank change); 0<RGF<1 intermediate. [verified from text, L3637–3641]
- Binary response: statistical test coincides with **DeLong's test**; general case uses U-statistics. Higher RGF → higher predictive accuracy; smaller p-value → significant vs lower bound. [verified from text, L3647–3653]
- Worked example (Table 5-1, Ch. 2 classifications, gender/race/nationality removed): RGF=68% — "attention" level. [verified from text, L3657–3667]
- Python: `check_fairness` for classification/regression; extensible to generative AI by identifying words/sentences associated with protected attributes. [verified from text, L3682–3701]

### Scoring rubric and mitigation

- Table 5-2 bands (same numeric bands as explainability ch4): Excellent 75–90%, Good 70–75%, Fair 60–70%, Borderline 40–60%, Poor 0–40%. Section header erroneously says "robustness" — content is fairness. [verified from text, L3703–3715]
- Mitigation: (1) apply RGE/explainability to locate unfair drivers; (2) resample/oversample underrepresented groups; (3) synthetic data for underrepresented groups. [verified from text, L3717–3750]

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **Lines read** | 3330–3763 (inclusive) |
| **Chapter boundary** | Starts ch.5 DOI (L3330); ends before ch.6 Privacy (L3764) |
| **wrong-file flag** | `false` |
| **Sections deferred** | Chen et al. full citation; generative-AI fairness procedures (named only) |
| **Figures** | 3D SME scatter (Fig. 5-1), Lorenz fairness curves (Fig. 5-2), country accuracy trends (Fig. 5-3) |
| **Amnesiac rule** | ISBN from L11–13 header |

## Pedagogy

### Learning objectives

1. Relate fairness requirements to human-rights non-discrimination in Responsible AI framing.
2. Contrast group, individual, and counterfactual fairness approaches and their literature limitations.
3. Distinguish **marginal** vs **conditional** fairness and diagnose **Simpson's paradox** in lending decisions.
4. Apply Shapley Lorenz and RGF to corporate and HMDA credit cases.
5. Interpret RGF properties, DeLong linkage, and Table 5-2 scoring bands.
6. Select mitigation paths linking explainability (RGE) and dataset rebalancing.

### worked_examples_present

**Y** — Dual case studies (SME corporate + HMDA consumer), RGF Table 5-1, Simpson's paradox walkthrough.

| Example | Section | Role |
|---------|---------|------|
| European SME 3D financial plot | Org fairness | Conditional fairness intuition |
| Lorenz curve near max fairness | Org fairness | Shapley Lorenz visualization |
| HMDA race × loan amount split | Individual fairness | Simpson's paradox |
| Table 5-1 RGF=68% | Model fairness | Numeric procedure |

### exercise_hooks

- No formal end-of-chapter exercises.
- **Instructor hooks `[inferred]`:**
  - Replicate HMDA marginal vs conditional Shapley ranking on a public fair-lending dataset.
  - Compute RGF after removing a protected attribute; compare to DeLong test outcome.
  - Map Teodorescu multi-criterion impossibility to a two-protected-variable scenario.
  - Pair with **simon ch10 ELSI** for health-equity framing of conditional fairness.

## Operator hooks

### 1. w4_ops_governance — SAFE-HAI fairness canon

**Mandatory pair:** **simon_aliferis_healthcare_2024 ch10** (ELSI/regulatory fairness). This chapter supplies **RGF metric + Simpson's paradox guardrail** for credit/lending; Simon supplies health-equity and causal-path principles. Also pairs **nam_gen_ai_health_2025 sec03** (risk) at wave level.

### 2. MDCalc / clinical-adjacent alignment

**[medium-high]** — HMDA lending is high-stakes consumer finance; methodology transfers to equitable allocation questions:

- **Simpson's paradox check** essential before declaring a model "fair" on aggregated metrics.
- **Conditional RGF** preferred over marginal Shapley summaries for audit defensibility.
- Corporate SME case less clinical; no HIPAA/clinical endpoints.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **simon_aliferis_healthcare_2024 ch04/10** | Medium–high | Simpson's paradox (Simon data design); ELSI fairness |
| **responsible_ai_practice_2025 ch04** | High | Same credit datasets, Shapley Lorenz lineage |
| **nam_gen_ai_health_2025 sec03** | Medium | Discrimination/bias risk taxonomy |

**Dedup:** Canonical for **RGF + conditional fairness / Simpson's paradox** in w4 RAI track.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Strong** — dual case studies + Table 5-1 |
| Exercise hooks | **Moderate** — inferred |
| Chapter boundary | **Clean** |
| Ingest suitability | **High** — contested marginal-vs-conditional fairness preserved |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2025; w4 wave |
| **Author authority** | **PASS** | Duke/Giudici; Giudici fairness/Lorenz research |
| **Primary-source citation density** | **PASS** | Teodorescu 2021, Horesh 2020, Karimi 2022, Grabowicz 2022, Jiang & Nachum 2024, Agarwal 2023, Chen et al., Giudici & Raffinetti 2021 |
| **Contested claims flagged** | **PASS** | No universal fairness measure; RF "fair" marginally but unfair conditionally; rubric header typo |
| **Worked examples** | **PASS** | HMDA paradox, Table 5-1, Lorenz curves |

**Overall TEXTBOOK-Q1:** **PASS**

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| RAI-C05-001 | No universal ML fairness measure; multiple incompatible notions | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch05_ingest.md | Fairness landscape |
| RAI-C05-002 | Conditional fairness: same variable effect on output; marginal: same output across groups | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch05_ingest.md | Org fairness |
| RAI-C05-003 | HMDA RF appears marginally fair on race but unfair for high loan amounts (91% Shapley share) | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch05_ingest.md | Simpson's paradox |
| RAI-C05-004 | RGF=0 unfair (rank reversal); RGF=1 fair (no change) | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch05_ingest.md | RGF |
| RAI-C05-005 | Binary RGF test coincides with DeLong's test | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch05_ingest.md | RGF test |
| RAI-C05-006 | Explainability (RGE) mitigation can surface fairness failure modes | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch05_ingest.md | Mitigation |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `rai-ingest-ch04-06` · word cap ≤4500*
