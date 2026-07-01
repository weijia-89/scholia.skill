# Chapter ingest — Artificial Intelligence and Machine Learning in Health Care (Simon & Aliferis, 2024), Chapter 7

| Field | Value |
|-------|-------|
| slug | simon_aliferis_healthcare_2024 |
| source_type | textbook_chapter |
| pdf_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/simon_aliferis_healthcare_2024.pdf |
| text_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/simon_aliferis_healthcare_2024.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/simon_aliferis_healthcare_2024_ch07_ingest.md |

## Bibliographic metadata

| Field | Value |
|-------|-------|
| title | Artificial Intelligence and Machine Learning in Health Care and Medical Sciences |
| authors | Gyorgy J. Simon, Constantin Aliferis (eds.); Chapter 7 primary: Constantin Aliferis, Gyorgy Simon |
| edition | 1st Edition (2024) |
| ISBN_print | 978-3-031-39354-9 [verified from text export, lines 53–54] |
| ISBN_electronic | 978-3-031-39355-6 [verified from text export] |
| publisher | Springer Nature (Health Informatics series) |
| parent_book_title | Artificial Intelligence and Machine Learning in Health Care and Medical Sciences |
| chapter_number | 7 (selective canon index) |
| chapter_title | Lessons Learned from Historical Failures, Limitations and Successes of AI/ML in Healthcare and the Health Sciences |
| book_chapter_doi_suffix | _12 [text export line 37651] |
| page_range | not embedded in text export [unverified] |

## scope

Assigned text slice **lines 34537–39737** spans two book chapters. **Primary scope (selective ch07 title):** case-study-driven history of AI/ML setbacks and recoveries in health—Gartner hype cycles, AI winters, perceptron/backprop/DL/SVM/RF arcs, semantic-network and pathway semantics failures, expert/heuristic systems, disconnect from clinical workflows, Bayesian-network tractability, overfitting/overconfidence, protocol and data-design dominance over algorithm choice, causality misconceptions and scalable causal ML, genomics failures (Poti, SELDI-TOF), guideline over-generalization, literature bias (publication bias, Matthew effect), COVID-model failures, commercial cases (IBM Watson, DL vs logistic regression meta-analyses, Optum racial bias, Epic sepsis model, LLMs), theory misreadings (NFLT, OBC, UFA), equivalence classes, and limited clinical translation (RISE, TAM, ML-RCT gaps). **Secondary scope in same slice:** book ch. 13 *Characterizing, Diagnosing and Managing the Risk of Error* (lines 38553–39737)—calibration, recalibration, label-reshuffling tests, reliable decision regions, stability, equivalence-class reporting, ML debugging strategies, deployment safety toolkit.

Out of scope: detailed procedural content delegated to cross-referenced chapters (data design, lifecycle, regulatory ELSI).

## key_findings

### Historical progress and hype

1. **Non-monotonic progress** — Major health AI/ML capabilities emerged through failures, dead ends, and recoveries; systematic suboptimal practices still incur cost. [verified, 34582–34620]

2. **Gartner hype cycle** — Technology trajectories: peak inflated expectations → trough of disillusionment → slope of enlightenment → plateau of real value. [verified, 34622–34645]

3. **AI winters (USA ~1974–80, ~1987–93)** — Driven by gap between promised and actual capability; perceptron linearity limits, LISP machine collapse, expert-system limits, Fifth Generation failure; health-relevant lessons on managing expectations. [verified, 34647–34696]

4. **Perceptron → backprop → DL** — Single-layer perceptrons cannot learn arbitrary nonlinear functions; multilayer backprop and later DL (ReLUs, convolutions, pooling) recovered capability; linear models remain strong in low-sample regimes (BVDE). [verified, 34699–34736]

5. **DL limitations persist** — Causal expressiveness, overfitting theory, sample hunger, explainability, shift invariance, and inflated published performance linked to biased designs; risk of new AI winter if unmanaged. [verified, 34796–34829]

### Knowledge representation and early systems

6. **Semantics in graphs** — Ambiguous edge semantics in semantic networks, pathway reverse engineering, and network science lead to over-interpretation; correlation edges mistaken for causation. [verified, 34831–34892]

7. **Rule-based and heuristic AI** — Broad "hard AI" scope and expert-system knowledge elicitation failed; heuristic systems (e.g., DxPlain/INTERNIST lineage) lacked formal guarantees; modern framing: systems with vs without well-understood properties. [verified, 34894–35033]

8. **Workflow disconnect** — Early diagnostic systems (INTERNIST-I) targeted non-pressing problems, ignored sequential workups, and disrupted data entry; Hunt/Haynes and Miller "Greek Oracle" critiques; ML+EHR scale later shifted paradigm. [verified, 35034–35089]

9. **Bayesian networks** — Naïve Bayes assumptions often false clinically; BNs improved probabilistic correctness but exact/approximate inference is worst-case intractable; structure learning from data advanced field. [verified, 35091–35136]

### Overfitting, protocols, data design

10. **Overfitting/overconfidence** — Historical stepwise regression bias; modern regularized learners and nested CV (Simon et al.) help; gaps remain in education, independent-validation interpretation, hand-built models, DL theory (Zhang et al. memorization), and competition overconfidence. [verified, 35138–35293]

11. **Algorithm + data design + protocol** — Success requires tuple beyond algorithm alone; Aphinyanaphongs text-categorization benchmark: minor protocol changes dropped AUC from >0.9 to ~0.72; MAQC-II: team proficiency and protocol often dominate algorithm choice; Statnikov: RF superiority in early microarray literature was protocol artifact. [verified, 35296–35411]

12. **ML challenges limitations** — Fix data design and error estimator; toy problem statements (e.g., Kaggle stroke prediction) omit clinical context; volunteer competitor pool and few datasets limit generalizability. [verified, 35427–35492]

### Causality

13. **Correlation ≠ impossibility of causal discovery** — Fisher warns against inferring causation from correlation alone, not against non-experimental causal discovery; RCTs confirmatory, expensive, narrow, context-sensitive. [verified, 35535–35664]

14. **Scalable causal ML** — Pearl, Spirtes-Glymour-Scheines, Cooper, etc. enabled reliable discovery under assumptions; early pessimism (e.g., Ullman) overturned by local/Markov-boundary methods. [verified, 35666–35718]

15. **Predictive methods abused for causal tasks** — Large benchmarks: predictive feature selection optimal for prediction, inappropriate for causal discovery; causal feature selection yields minimal feature sets with causal accuracy. [verified, 35720–35783]

16. **Pearl's causal AI pillars** — Transparent assumptions, do-calculus, counterfactuals, external validity, missing data, causal discovery. [verified, 35785–35801]

### Genomics, guidelines, literature

17. **Genomics case studies** — Anil Poti incident: RCT insufficient if model construction flawed; IOM omics test recommendations (BP 12.7.1); Petricoin/Liotta SELDI-TOF irreproducibility; random gene signatures often match ML biomarkers (Venet et al.); NCI Biometrics branch compliance gaps. [verified, 35803–35879]

18. **Guideline risks** — Simon nested-CV guidance can be over-generalized (Statnikov histogram experiments); meta-analytic chains (Ntzani, Ioannidis) amplify misinterpretation; accreditation/reporting/reproducibility standards necessary but not sufficient for safety. [verified, 35881–36058]

19. **Literature dynamics** — Publication bias and canonization modeling (Nissen et al.); Matthew/first-mover citation effects; disconnected CS vs clinical literatures; early high-cited methods often not best performing later. [verified, 36060–36193]

### COVID, commercial, and modern cases

20. **COVID ML** — Roberts et al.: >2200 studies, none met basic clinical-readiness criteria; FDA oversight criticisms noted. [verified, 36201–36222]

21. **IBM Watson Health** — Heuristic, non-purpose-built, Jeopardy-scale evaluation mismatch, human patching behind scenes, inferior benchmarks, strategic failure (2021 wind-down). [verified, 36237–36284]

22. **DL vs logistic regression** — Meta-analyses (~300 primary studies): at low risk of bias, ML/DL often matches or loses to LR; high bias inflates ML advantage (Christodoulou et al. logit AUC difference ~0 at low bias). [verified, 36286–36373]

23. **Marcus hybrid AI critique** — Pure DL lacks symbolic knowledge, arithmetic, verification; recommends hybrid symbolic-connectionist approaches (BP 12.11.2). [verified, 36377–36449]

24. **Optum racial bias** — Model trained on costs as proxy for need; systemic cost disparities induced prioritization bias. [verified, 36451–36474]

25. **Health apps evidence** — Systematic reviews: very weak RCT evidence for prescribability. [verified, 36476–36491]

26. **Epic Sepsis Model** — External validation AUC 0.63 vs developer claims; low sensitivity, alert fatigue. [verified, 36493–36513]

27. **LLMs (ChatGPT/LaMDA)** — USMLE-passing headlines vs reasoning failures, harmful advice examples, fabricated citations; unlimited-scope vs focused systems tradeoff. [verified, 36515–36639]

28. **Commercial vs academic NLP** — Aphinyanaphongs: Google Prediction API and other commercial tools underperformed libSVM-scale academic stacks on 229 text tasks. [verified, 36641–36700]

29. **Google Flu Trends** — Big-data hubris, unstable features, lack of baselines (CDC lagged reports), opacity. [verified, 36773–36826]

30. **AI error amplification** — ChatGPT-generated misinformation recycled by search without warnings. [verified, 36829–36856]

### Theory and equivalence classes

31. **NFLT misread** — No Free Lunch does not invalidate CV, independent validation, or choosing best empirical models in skewed real-world priors. [verified, 36858–36908]

32. **OBC and UFA** — Bayes optimality and universal approximation do not guarantee tractable learning or practical superiority. [verified, 36910–36955]

33. **Equivalence classes** — Astronomical numbers of equally accurate predictors, feature sets, and causal models; ignoring classes causes over-interpretation, IP weakness, and false fairness audits (Table 2); use TIE*/GLL-MB, GLL-PC, ODLP* (BP 12.13.1). [verified, 36957–37110]

### Translation and conclusions

34. **Limited clinical adoption** — Yin et al.: few real-world AI implementations with rigorous designs; RISE barriers; Plana et al.: 41 ML RCTs, poor CONSORT-AI adherence; RCTs must be final verification after rigorous development. [verified, 37114–37209]

35. **Chapter conclusion** — Identify limitations scientifically; apply best practices to avoid large-scale harm and another AI winter. [verified, 37211–37243]

### Embedded ch. 13 (lines 38553–39737): model risk characterization

36. **Calibration essential** — Perfect calibration ≠ perfect accuracy; binning and sigmoid mapping convert scores to probabilities; measure calibration regions. [verified, 38655–38692]

37. **Label reshuffling test (LRT)** — Tests significance vs null model and protocol overfitting propensity. [verified, 38632–38641]

38. **Reliable/unreliable decision regions** — Invert calibration logic to define deployable output ranges. [verified, 38703–38711]

39. **Stability ≠ unreliability** — High parameter instability may reflect equivalence classes, not poor generalization. [verified, 38723–38743]

40. **ML debugging harder than code debugging** — Functionals, infinite optimal models, stochasticity, data-design coupling; seven-strategy debug checklist (BP 13.7). [verified, 38824–39031]

41. **Deployment toolkit (BP 13.8)** — Outlier detection, reliable regions, distribution-shift monitoring, credible intervals, QC alerts, population transfer checks, missing-input policy, ancillary DSS for validity drift. [verified, 39102–39241]

## coverage_attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| Abstract, hype, AI winters | read | 34554–34696 |
| Perceptron, DL, semantics, expert/heuristic AI | read | 34699–35033 |
| Workflow disconnect, Bayes/BNs | read | 35034–35136 |
| Overfitting, protocols, MAQC-II, challenges | read | 35138–35492 |
| Causality, genomics, guidelines, literature | read | 35527–36193 |
| COVID, Watson, DL meta-analyses, commercial cases | read | 36201–36856 |
| Theory misinterpretation, equivalence classes | read | 36858–37110 |
| Translation, conclusions, assignments | read | 37114–37641 |
| Ch. 13 model diagnostics (embedded slice) | read | 38553–39737 |
| Ch. 13 references | read | 39633–39731 |
| Book ch. 14 NLP opener | **deferred** | 39738+ |

- **Lines read:** 34537–39737 (full assigned range)
- **wrong_file_flag:** false
- **Amnesiac attestation:** Numbered findings trace to line ranges in `simon_aliferis_healthcare_2024.txt`

## pedagogy

### learning_objectives

- Map historical AI failures to enduring health-AI pitfalls (hype, semantics, workflow, protocol, causality)
- Explain why algorithm choice often matters less than data design and error-estimation protocol
- Critique commercial and literature hype using cited case studies (Watson, ESM, COVID reviews)
- Distinguish predictive from causal ML misuse and equivalence-class over-interpretation
- Apply post-hoc model diagnostics (calibration, LRT, reliable regions) before deployment

### worked_examples_present

**Y** — Extensive case studies and benchmark citations; Statnikov histogram figure for guideline generality; Table 2 equivalence-class language; calibration binning workflow figures in embedded ch. 13.

### exercise_hooks

| ID | Prompt summary | Anchor |
|----|----------------|--------|
| 7.PE-1 | Map case-study table (12.1–12.14) to prior-chapter pitfalls/BPs | 37425–37600 |
| 7.PE-2 | Classify cases as historical-solved vs enduring-open | 37606–37637 |
| 7.PE-3 | Design label-reshuffling test for a clinical risk model | 38632–38641 |
| 7.PE-4 | Audit a published DL paper for LR comparator + bias tools | 36286–36373 |
| 7.PE-5 | List deployment safeguards from BP 13.8 for sepsis-like alerting | 39102–39241 |

## Operator hooks

### 1. w3_clinical_docs

Primary **failure-mode and anti-pattern canon** for clinical ML: pairs with NAM risk sections, lifecycle chapters elsewhere in Simon, and operator due-diligence checklists before trusting vendor AI.

### 2. MDCalc alignment

**[pattern-portable]** — Comparator discipline (LR baselines), external validation skepticism, and deployment calibration directly apply to clinical decision calculators and risk scores.

### 3. Redundancy

| Canon title | Relationship |
|-------------|--------------|
| `nam_gen_ai_health_2025` | Policy/risk framing; Simon ch07 empirical case depth |
| `hands_on_llms_2024` | LLM pitfalls cross-reference Watson/ChatGPT sections |
| Earlier Simon selective ch01–06 | Prerequisites for BVDE, lifecycle, overfitting vocabulary |

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Citation density | Very high (meta-analyses, MAQC-II, Obermeyer, Wong ESM) |
| Contested claims | Authors flag DL hype, guideline overreach, LLM early evidence |
| Slice quirk | Lines 38553–39737 are book ch. 13—documented as secondary scope |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | 2024 OA Springer |
| Author authority | **PASS** | Senior health-informatics faculty, consensus-grade citations |
| Primary-source citation density | **PASS** | Hundreds of anchored references |
| Contested claims flagged | **PASS** | DL vs LR, guidelines, LLMs explicitly qualified |
| Worked examples | **PASS** | Case-study pedagogy; embedded ch. 13 procedural diagnostics |

**TEXTBOOK-Q1 chapter verdict:** **PASS** — essential w3_clinical_docs historical and risk-characterization ingest.
