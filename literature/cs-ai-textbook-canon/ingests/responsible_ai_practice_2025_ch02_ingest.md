# Chapter ingest — Responsible AI in Practice, Chapter 2 (Accuracy)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Responsible AI in Practice |
| **authors** | Toju Duke, Paolo Giudici |
| **edition** | 1st (Apress / Springer Nature, 2025) |
| **ISBN_print** | 979-8-8688-1165-4 |
| **ISBN_electronic** | 979-8-8688-1166-1 |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1 |
| **chapter_number** | 2 |
| **chapter_title** | Accuracy |
| **page_range** | [not in text export] |
| **parent_book_title** | Responsible AI in Practice |
| **source_type** | textbook |
| **text_path** | literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt |
| **pdf_path** | [not staged on disk] |

## Scope

Chapter 2 operationalizes **accuracy** as the first SAFE-HAI quantitative pillar. It anchors on ISO/IEC TS 5723:2022 and NIST AI RMF trustworthiness (valid/reliable distinction: accurate = valid; robust = reliable, deferred to ch.3); maps EU AI Act high-risk accuracy lifecycle requirements; develops classical metrics (ACC, confusion matrix, MSE/RMSE, ROC/AUROC with Diebold-Mariano and DeLong tests); introduces the book's signature **Rank Graduation Accuracy (RGA)** unified measure via Lorenz/concordance curves (Giudici & Raffinetti); extends to multidimensional (cosine, Levenshtein, Jaccard, embedding distances) and LLM outputs (Huang et al. toxicity/bias/alignment; hallucination index); surveys **SuperGLUE** and other NLP benchmarks; provides a scoring rubric and mitigation playbook (data volume, features, hyperparameter tuning, over/underfitting, regularization).

Out of scope: robustness measurement (ch.3); Python statistical-test appendix details; case-study application.

## Key findings

All claims **[verified from text]** from lines 1035–2084 unless tagged `[inferred]`.

1. **ISO accuracy definition.** "Closeness of results … to true values"; requires realistic use-case testing and documentation; false positive/negative consideration. (lines 1076–1086)

2. **Classification accuracy (ACC).** Correct predictions / total; tied to confusion matrix; 100% accuracy flagged as suspicious (overfitting, data leakage); >70% often recommended as practical floor. (lines 1088–1114)

3. **NIST RMF questions.** How assess accuracy? What benchmarks? How communicate? Accuracy framed as organizational (model-performance) risk before end-user harm. (lines 1147–1173)

4. **EU AI Act accuracy.** High-risk systems need appropriate accuracy in design/development, consistent lifecycle performance, declared benchmarks/metrics in instructions for use. (lines 1128–1136)

5. **Predictive accuracy (continuous).** MSE/RMSE as Euclidean distance from ground truth; finance ROE example (Table 2-1, RMSE ≈ 7.41 vs mean ROE 0.2882 — poor accuracy). Diebold-Mariano test for comparing model RMSE with p-value decision rules and risk-appetite bounds. (lines 1189–1319)

6. **Classification accuracy (binary).** FP/FN tables (Tables 2-2, 2-3); threshold dependence; ROC curve and AUROC; DeLong test for AUROC comparison. Ideal model = Y-axis (TPR=1, FPR=0). (lines 1324–1468)

7. **RGA unified measure.** Lorenz curve (Qi), dual Lorenz (Q'i), concordance curve (Ci from prediction ranks); RGA = sum(Q'i−Ci)/sum(Q'i−Qi); normalized [0,1] with 0.5 = random; binary case RGA = AUROC; U-statistic test generalizes DeLong. Worked examples: high RGA 0.90 (Table 2-5), low RGA 0.06 (Table 2-6), binary RGA 0.83 (Table 2-7). Python: `check_accuracy` / `rga(y, yhat)`. (lines 1477–1747)

8. **Multidimensional & textual accuracy.** Document/image vector distances (cosine, Levenshtein, Jaccard, Euclidean on TF-IDF/embeddings); RGA applicable to summary distances. LLMs without ground truth: Huang et al. toxicity/bias/value-alignment; Mann-Whitney ≡ AUROC ≡ RGA; hallucination index as mean AUROC on Q-evidence-answer triples. TrustGPT benchmark cited for unstructured LLM distance. (lines 1749–1862)

9. **Benchmarks vs risk management.** SuperGLUE eight tasks (BoolQ, CB, COPA, MultiRC, ReCoRD, RTE, WIC, WSC); also HELM, LM Evaluation Harness, PromptBench, Chatbot Arena, SQuAD, IMDB. `[contested in chapter]` Benchmarks useful for compliance checking but **cannot substitute** for statistical metrics (RGA) in formal risk management. LLM issues: hallucination, jailbreaks, unsafe/biased outputs. (lines 1864–1989)

10. **Communication & rubric.** Transparency via papers, conferences, product disclosure. Scoring rubric: Excellent 75–90%, Good 70–75%, Fair 60–70%, Borderline 40–60%, Poor 0–40%. (lines 1991–2013)

11. **Mitigation.** More training data (cost caveat/synthetic data); more variables/feature processing; hyperparameter tuning; underfitting → increase flexibility/reduce regularization; overfitting → reduce flexibility/increase regularization. Fraud-detection failure example for business/regulatory consequences. (lines 2015–2072)

## Chapter digest

| Subtopic | Lines (approx.) | Takeaway |
|----------|-----------------|----------|
| Definitions & RMF | 1051–1173 | ISO + NIST + EU AIA accuracy requirements |
| RMSE / Diebold-Mariano | 1189–1319 | Continuous prediction distance + hypothesis tests |
| ROC / AUROC / DeLong | 1324–1468 | Threshold-independent binary accuracy |
| RGA methodology | 1477–1747 | Lorenz-concordance unified rank metric + Python hook |
| Multimodal / LLM | 1749–1862 | Distance metrics; subjective LLM eval; RGA unification claim |
| Benchmarks | 1864–1989 | SuperGLUE et al.; benchmarks ≠ risk-management metrics |
| Rubric & mitigation | 1991–2072 | Performance bands; data/model tuning playbook |

## Pedagogy

### Learning objectives

1. Apply ISO and NIST definitions of accuracy vs reliability (robustness).
2. Compute and interpret RMSE, AUROC, and RGA with appropriate statistical tests.
3. Explain why threshold choice affects FP/FN and why AUROC/RGA normalize comparisons.
4. Distinguish benchmark leaderboard evaluation from RGA-based compliance risk measurement.
5. Select mitigation strategies for underfitting vs overfitting given rubric score.

### worked_examples_present

**Y** — ROE MSE table (2-1); credit-default FP/FN tables (2-2, 2-3); Lorenz income Gini walkthrough (2-4); RGA concordance examples (2-5–2-7); ROC figure (2-1).

### exercise_hooks

1. Calculate RGA by hand for a five-row prediction set (Tables 2-5 pattern).
2. Compare two classifiers with DeLong test given AUROC values and sample size.
3. Map SuperGLUE task list to a clinical NLP use case (documentation QA).
4. Apply scoring rubric to a model with ACC=0.68 and document mitigation plan.
5. Pair exercise: contrast RGA approach with AIE ch.4 private eval pipeline design.

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **lines_read** | 1035–2084 (inclusive) |
| **section_boundary** | Starts at Ch.2 heading (1037); ends before Ch.3 `Robustness` (2087) |
| **wrong_file_flag** | false |
| **deferred** | RGA statistical-test appendix; ch.3 robustness; case study |
| **figure_placeholders** | ROC curve Model 1 vs 2 (1415–1429); concordance curves (1568–1575) |

## Operator hooks

### Foundation layer (w4_ops_governance)

**Quantitative accuracy spine** for SAFE-HAI. Mandatory pair with `ai_engineering_2025_ch04_ingest.md` (evaluation-driven development, private benchmarks, contamination). Complements `nam_gen_ai_health_2025` accuracy/hallucination risk framing with measurable statistics.

### MDCalc alignment

**[relevant]** — pattern-portable eval discipline (no employer claims):

- **Declared accuracy metrics in instructions for use** (EU AIA lines 1134–1136) → model cards / release notes for any clinical-adjacent tool.
- **Realistic use-case testing** (ISO lines 1084–1086) → eval slices matching production documentation or CDS context.
- **NIST communicate-accuracy question** (lines 1162–1164) → transparent performance disclosure to clinical users.
- **Fraud-detection analogy** (lines 2023–2029) → false-positive harm in triage/CDS contexts.

**[peripheral]** — SuperGLUE/HELM leaderboard patterns; not clinical-benchmark specific.

Do not cite RGA thresholds as MDCalc acceptance criteria without local validation.

### Redundancy

| Canon | Overlap | Distinction |
|-------|---------|-------------|
| AIE 2025 ch04 | Benchmarks, hallucination, eval pipelines | RAI = Lorenz/RGA statistical compliance metric; less MLOps workflow |
| Simon/Aliferis ch03–04 | Model evaluation, metrics | RAI = cross-domain finance examples; unified RGA theory |
| NAM GenAI 2025 | Hallucination/accuracy risks | RAI = procedural measurement + Python hooks |

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Anchor density | High — ISO 5723, NIST RMF, EU AIA, Diebold-Mariano, DeLong, Giudici & Raffinetti, Wang et al. SuperGLUE |
| Procedural hooks | RGA calculation, rubric bands, mitigation checklist — strong study-guide material |
| Boundary | Clean accuracy-only slice |
| Contested claims | 100%-accuracy suspicion; benchmarks insufficient for risk management |

## TEXTBOOK-Q1 verdict

**PASS** — Primary-source standards citations; procedural chapter with tables, formulas, Python function names; contested benchmark-vs-RM distinction explicit; worked numerical examples throughout.

---

*Ingest agent: rai-ingest-ch01-03 · ch02 · lines 1035–2084 · word cap ≤4500*
