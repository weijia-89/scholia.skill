# Chapter ingest — Responsible AI in Practice, Chapter 1 (Responsible AI and AI Governance)

## Bibliographic metadata

| Field | Value |
|-------|-------|
| **title** | Responsible AI in Practice |
| **authors** | Toju Duke, Paolo Giudici |
| **edition** | 1st (Apress / Springer Nature, 2025) |
| **ISBN_print** | 979-8-8688-1165-4 |
| **ISBN_electronic** | 979-8-8688-1166-1 |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1 |
| **chapter_number** | 1 |
| **chapter_title** | Responsible AI and AI Governance |
| **page_range** | [not in text export] |
| **parent_book_title** | Responsible AI in Practice |
| **source_type** | textbook |
| **text_path** | literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt |
| **pdf_path** | [not staged on disk] |

## Scope

Chapter 1 establishes the book's governance and measurement spine. It defines Responsible AI within ethical AI (governance, social, societal, legal dimensions); traces philosophical roots to the 1950s; documents GenAI-era harms (LAION-5B copyright/privacy/CSAM, Replika companion risks); surveys global AI regulation (UNESCO 2021 Recommendation, UN 2023 advisory principles, US Executive Order Oct 2023, EU AI Act, UK AI bill Nov 2023, plus China/Japan/Canada/Australia/Korea/Singapore); and introduces the **SAFE-HAI** framework (Secure, Accurate, Fair, Explainable Human-Centered AI) with Lorenz-curve / Gini-index extensions for quantitative compliance metrics (RGA, RGR, RGE, RGF, RGP, RGS, RGH preview). Sequel to Duke (2023) *Building Responsible AI Algorithms*.

Out of scope in this slice: procedural measurement of SAFE metrics (ch.2–8); governance processes (ch.9); case study (ch.10); Python appendix.

## Key findings

All claims **[verified from text]** from lines 194–1034 unless tagged `[inferred]`.

1. **Responsible AI definition.** Body of work ensuring development, deployment, and use of AI with minimal risks/harms across race, gender, belief, sexual orientation, age, and ability; overlaps with but is not identical to "ethical AI." (lines 212–233)

2. **Historical framing.** Principles (fairness, transparency, accountability, privacy, safety, explainability, inclusivity, sustainability) trace to 1950s academic philosophy; GenAI/transformer era (post-2017) accelerated adoption and harm surface. (lines 235–261)

3. **Documented harms.** LAION-5B: copyright disputes, private medical images in training data, Stanford finding of >1000 CSAM images (Dec 2023). Replika: depression reports, 2021 UK incident (Chail). Authors frame these as drivers for regulatory action. (lines 284–329)

4. **UNESCO / UN governance.** UNESCO 2021 global AI ethics standard (human rights, transparency, fairness, human oversight). UN 2023 advisory body: five principles—inclusive governance, public interest, data-governance alignment, stakeholder collaboration, UN Charter/HR law/SDG grounding. (lines 342–439)

5. **US Executive Order (Oct 2023).** Eight principles: safe/secure; responsible innovation/competition; worker support; anti-discrimination; consumer protection; privacy/HR protection; federal workforce/infrastructure; international collaboration. `[contested in chapter]` Skepticism noted: revocability, limited power without congressional law, funding gaps, innovation slowdown concerns. (lines 444–597)

6. **EU AI Act.** High-risk criteria: significant health/safety/rights risk; third-party conformity assessment products; profiling (e.g., CCTV). Non-high-risk exemptions for narrow procedural tasks, human-activity improvement, pattern detection without replacing human review, preparatory assessment tasks. Transition from Aug 2024; `[contested]` innovation-stifle and private-sector accountability critiques. (lines 599–682)

7. **UK AI bill (Nov 2023).** Risk assessment/monitoring; five principles (safety/security/robustness, transparency/explainability, fairness, accountability/governance, contestability/redress); transparency, testing, data-protection, equality, inclusivity requirements for developers/deployers. (lines 684–736)

8. **Regulatory gap theme.** Global convergence on privacy/fairness/transparency/robustness/safety themes, but implementation speed, standards, workforce literacy, and GenAI pace raise open questions. (lines 742–772)

9. **SAFE-HAI framework.** SAFE = Security (robustness to perturbations), Accuracy (ground-truth consistency), Fairness (absence of group bias), Explainability (human-understandable causes). HAI extensions = qualitative: privacy, environmental sustainability, human-in-the-loop. Metrics agnostic to underlying ML architecture; inspired by Basel financial risk measurement (Giudici & Raffinetti 2023 financial-sector precursor). (lines 777–863)

10. **Lorenz/Gini methodology preview.** Extend Lorenz curve and Gini index from income inequality to AI output concentration; seven Rank Graduation measures planned across book chapters (RGA accuracy, RGR robustness, RGE explainability, RGF fairness, RGP privacy, RGS sustainability, RGH human oversight). Python code deferred to later chapters and case study. (lines 888–1013)

## Chapter digest

| Subtopic | Lines (approx.) | Takeaway |
|----------|-----------------|----------|
| RAI definition & history | 212–261 | Ethical-AI subset; GenAI harm acceleration |
| Harm vignettes | 284–329 | LAION-5B, Replika as regulatory catalysts |
| UNESCO / UN | 342–439 | Global ethics + five governance principles |
| US EO 2023 | 444–597 | Eight trust principles; enforcement limits noted |
| EU AI Act | 599–682 | High-risk taxonomy; contested private-sector balance |
| UK + other jurisdictions | 684–740 | Principle-based bill; synthetic-data/privacy focus |
| SAFE-HAI intro | 777–1013 | Quantitative Lorenz metrics + qualitative HAI pillars |

## Pedagogy

### Learning objectives

1. Distinguish Responsible AI from ethical AI and name core principle categories.
2. Map major 2023–2024 regulatory instruments (UNESCO, UN, US EO, EU AIA, UK) to overlapping trust themes.
3. Explain SAFE vs HAI components and why authors adopt financial-sector risk-measurement analogy.
4. Identify contested claims in regulatory reception (innovation vs safety tradeoffs).
5. Preview how Lorenz-curve metrics unify accuracy/robustness/fairness measurement.

### worked_examples_present

**Y** — LAION-5B and Replika harm narratives; EU high-risk vs non-high-risk decision tree; Lorenz income example (preview); SAFE-HAI diagram placeholders.

### exercise_hooks

1. Map NIST AI RMF trust characteristics to SAFE-HAI pillars (forward to ch.2–8).
2. Classify a hypothetical clinical CDS under EU AI Act high-risk criteria.
3. Compare US EO principle 4 (non-discrimination) with UK fairness principle—gaps and overlaps.
4. Draft org-level AI governance checklist from UNESCO + UN principles.

## Coverage attestation

| Field | Value |
|-------|-------|
| **source_path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **lines_read** | 194–1034 (inclusive) |
| **section_boundary** | Starts at Ch.1 heading (196); ends before Ch.2 `Accuracy` (1037) |
| **wrong_file_flag** | false |
| **deferred** | Ch.2–10; Python appendix; references list |
| **figure_placeholders** | SAFE-HAI governance cube (793–799); seven-aspect diagram (933–938) |

## Operator hooks

### Foundation layer (w4_ops_governance)

**Governance + measurement spine opener** for Wave 4. Establishes SAFE-HAI vocabulary and global policy map before technical chapters. Pair with:

- `nam_gen_ai_health_2025_sec05_ingest.md` — health-system guardrails (mandatory pair per wave card)
- `simon_aliferis_healthcare_2024_ch10_ingest.md` — FDA/ISO 14971 regulatory depth
- `ai_engineering_2025_ch10_ingest.md` — production guardrails complement

### MDCalc alignment

**[relevant]** — pattern-portable governance (no employer claims):

- **Eight US EO principles + EU high-risk taxonomy** (lines 457–663) → tiered risk classification before patient-facing deploy; map to org policy + local validation.
- **Human oversight emphasis** (UNESCO lines 351–355; SAFE-HAI HITL preview lines 831–832, 998–1000) → HOTL: AI drafts; clinician accountable for sign-off.
- **Post-deployment monitoring** (US EO lines 472–474) → algorithmovigilance-style ongoing performance checks.
- **Consumer protection in healthcare** (lines 532–536) → sensitive-domain safeguards for CDS and documentation tools.

Do not cite this chapter as FDA clearance criteria or MDCalc production policy.

### Redundancy

| Canon | Overlap | Distinction |
|-------|---------|-------------|
| NAM GenAI 2025 sec01 | Governance, bias, local validation | RAI = global regulation survey + quantitative SAFE-HAI metrics program |
| Simon/Aliferis ch10 | EU AI Act, NIST RMF, fairness | RAI = cross-sector textbook; less health-specific causal bias depth |
| AIE 2025 ch10 | Guardrails, monitoring | RAI = statistical compliance metrics (Lorenz/Gini), not MLOps pipeline |
| Duke 2023 (prior book) | RAI framework precursor | This book adds measurable SAFE-HAI statistics + Python |

### Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Anchor density | Moderate — cites UNESCO, UN, US EO, EU AIA, Giudici & Raffinetti 2023, Basel analogy |
| Procedural hooks | Governance checklist + high-risk classifier derivable for study-guide cards |
| Boundary | Clean intro/governance slice; measurement deferred to ch.2+ |
| Contested claims | Flagged — EO revocability, EU innovation critique, regulation pace vs GenAI |

## TEXTBOOK-Q1 verdict

**PASS** — 2025 edition; author authority (Duke: Google RAI PM; Giudici: 200+ pubs, EU regulatory projects); primary-source policy citations; contested regulatory reception not smoothed; worked harm/regulatory examples present.

---

*Ingest agent: rai-ingest-ch01-03 · ch01 · lines 194–1034 · word cap ≤4500*
