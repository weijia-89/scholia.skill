# Chapter ingest — `responsible_ai_practice_2025` · Chapter 9

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
| **chapter_number** | 9 |
| **chapter_title** | Governance Processes |
| **page_range** | Printed pages absent from text export; logical span L5094–5393 |
| **parent_book_title** | Responsible AI in Practice |
| **DOI** | https://doi.org/10.1007/979-8-8688-1166-1_9 |

## Scope

Chapter 9 is the **organizational governance capstone** of Duke & Giudici's SAFE-HAI book. It bridges Ch. 1 policy survey and Ch. 8 human-centered AI to operational governance: NIST-aligned harm taxonomy, a catalog of cross-cutting AI risks (especially foundation/open models), stakeholder roles, Table 9-1 information requirements for policy design, and a five-step governance structure (policy, team, reviews, stakeholder engagement, user feedback).

**Sections ingested:** Framing (governance vs SAFE-HAI lifecycle) · NIST three harm domains · Seven risk categories · Stakeholder map (users, civil society, policymakers) · Table 9-1 · Five governance pillars · Transition to Ch. 10 credit case study.

Cross-refs: Ch. 1 (policies, SAFE-HAI), Ch. 8 (HCAI/bitcoin example), Ch. 10 (high-risk credit application). NIST AI RMF cited throughout prior chapters.

## Key findings

All claims **[verified from text]** unless tagged `[contested in chapter]`.

### Governance framing

- AI governance = structures and processes overseeing strategy, management, and operations; fundamental given rising AI risks (L5116–5126).
- Builds on Ch. 1 governing policies and SAFE-HAI framework; adopters/developers/users must understand governance and instantiate processes (L5116–5120).
- Prior chapter (HCAI) used accuracy on neural networks and bitcoin as motivating example; this chapter deep-dives governance across the full development lifecycle (L5110–5114).

### NIST harm taxonomy (three areas)

1. **Harm to people** — civil liberties, human rights, psychological/physical safety; group harm via bias/discrimination; societal harm when democratic participation is repressed or influenced (L5143–5151).
2. **Harm to organization/enterprise** — cyber attacks, security breaches, monetary loss, reputational harm affecting technical systems and business operations (L5155–5160).
3. **Harm to a system** — financial systems, global supply chains, environmental ecosystems insufficiently robust to adverse AI impact (L5164–5169).

### Risk catalog (open/foundation-model emphasis)

| Risk | Summary | Author stance |
|------|---------|---------------|
| Disinformation / election interference | LLM incorrect but credible outputs; social-media moderation needed | High concern |
| Biorisk | Open foundation models alleged to enable bioweapon instructions | `[contested]` studies "not yet proven"; instructions often wrong; still rated high risk (L5188–5196) |
| Spear-phishing | GenAI generates targeted phishing emails | `[contested]` rated **low risk** — OS/browser security may block delivery (L5200–5211) |
| Voice-cloning scams | Short-audio impersonation; disinformation in conflict zones | High concern |
| NCII / CSAM | Text-to-image open models; nonconsensual deepfakes | High regulatory/human-rights risk (L5227–5234) |
| Authoritarian/corporate surveillance | Law enforcement and corporate use without challenge rights; false arrests, welfare penalties | High concern (L5238–5247) |
| Cyber attacks | Umbrella for scams invading privacy/data (L5251–5256) |

Risks overlap across open/closed models and domains (L5136–5139).

### Stakeholders beyond developers

- **Users** — daily-use expertise, satisfaction, pain points, feature requests; essential for governance policy design (L5271–5277).
- **Civil society** — AI education and accurate public information enable standards, research, and policy contribution (L5279–5282).
- **Policymakers** — local/international regulation; auditing, red-teaming, safety evaluations inform policy (L5284–5288).

### Table 9-1 — information for governance policies

| Category | Requirements |
|----------|--------------|
| Capability | Tasks trained on, datasets, error rates, FP/FN — misuse potential |
| Controllability | Intentional/unintentional behavior, toxicity, alignment with developer/user intent |
| Model impact | Representational harms, disinformation, false content, workforce displacement |
| New/emerging information | Verify developer claims via testing and risk assessment |
| Uncovering new information | Developers often test accuracy/privacy only — miss robustness, security, fairness, sustainability, data ethics (L5293–5304) |

Scrutiny, testing, investigation, and reporting of risks underpin governance process creation (L5306–5308).

### Five-step governance structure

1. **Define AI policy** — with legal and stakeholders; align to AI principles and strategy; publicize to engineering; clear, concise, accessible (L5314–5322).
2. **Establish AI governance team** — multidisciplinary working group (researchers, engineers, product, legal); oversees safe/trustworthy AI design, development, deployment (L5326–5335).
3. **Regular reviews and risk assessments** — ongoing evaluation of datasets, models, ML applications; escalation paths and remediation (L5339–5348).
4. **Stakeholder engagement** — regular meetings with users, civil society, policymakers to inform design and organizational learning (L5352–5361).
5. **Incorporate user feedback** — thumbs up/down and similar mechanisms; processes to fine-tune datasets, models, and applications (L5365–5374).

Closing: risks too grave to ignore; SAFE-HAI framework measurement reduces harms (L5378–5381). Next chapter: credit-lending case study applying SAFE-HAI (L5383–5389).

## Coverage attestation

| Check | Status |
|-------|--------|
| **Source path** | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/responsible_ai_practice_2025.txt` |
| **Lines read** | 5094–5393 (inclusive) |
| **Chapter boundary** | Starts DOI anchor ch.9 (L5094); ends copyright before ch.10 (L5391–5393) |
| **wrong-file flag** | `false` |
| **Tables ingested** | Table 9-1 (structured summary) |
| **Footnotes** | NIST harm citation (⁶⁵), biorisk (⁶⁶), spear-phishing (⁶⁷) — appendix deferred |
| **Sections deferred** | Full footnote bibliography (appendix from L6375) |

## Pedagogy

### Learning objectives

1. Map AI harms to NIST's three domains (people, organization, system).
2. Enumerate major cross-cutting AI risks and distinguish contested vs settled severity claims.
3. Identify governance-relevant stakeholders beyond engineering (users, civil society, policymakers).
4. Apply Table 9-1 information categories when drafting organizational AI policy.
5. Design a five-pillar governance structure: policy, team, assessments, engagement, feedback.
6. Connect governance processes to SAFE-HAI measurement from prior chapters.

### worked_examples_present

**N** — Conceptual/process chapter; bitcoin/HCAI example referenced from Ch. 8 only. Table 9-1 is a requirements checklist, not a numeric walkthrough.

### exercise_hooks

- No formal end-of-chapter exercises in text.
- **Operator drill ideas `[inferred]`:**
  - Draft Table 9-1 completion worksheet for one production model (capability through ethics tests).
  - Map your org's current RACI against the five governance pillars; gap-list missing roles.
  - Red-team catalog: which Ch. 9 risks apply to your deployment (GenAI vs predictive)?
  - Design stakeholder engagement cadence (users, civil society, policy) with escalation paths.
  - Pair with NAM sec05 Table 5-4 — reconcile health-professional accountability with internal governance team charter.

## Operator hooks

### 1. w4_ops_governance — governance process canon

**Mandatory pair: RAI ch9 ↔ NAM sec05** (`nam_gen_ai_health_2025_sec05_ingest.md`).

| RAI ch9 | NAM sec05 complement |
|---------|----------------------|
| Five-pillar org governance structure | Foundational activities + Tables 5-1/5-2 monitoring |
| Table 9-1 information requirements | Local validation, OMB M-24-10 mirror-deployment testing |
| Stakeholder map (users, civil society, policymakers) | Table 5-3 life-cycle collaboration + Table 5-4 RACI |
| Red-teaming for policymakers (L5285–5287) | Adversarial testing / red-teaming in monitoring rows |
| User feedback mechanisms (L5367–5374) | User feedback loops in Tables 5-1/5-3 |
| Developer testing gaps (accuracy/privacy only) | Algorithmovigilance + GenAI-specific drift/hallucination metrics |

**Read-order:** RAI ch1 (policy landscape) → ch9 (org process) **in parallel with** NAM sec05 (health-sector operational RACI). NAM sec05 is denser on post-deploy accountability; RAI ch9 is domain-agnostic org playbook.

**Upstream:** RAI ch1, ch8. **Downstream:** RAI ch10 (SAFE-HAI measurement case study).

### 2. MDCalc / clinical-adjacent alignment

**[high relevance]** — Governance patterns portable to clinical-adjacent AI:

- **Five-pillar structure** maps to model registry, change control, clinical safety officer sign-off.
- **Table 9-1** → pre-deploy dossier checklist (capability, controllability, impact, independent verification).
- **Stakeholder engagement** → clinician + patient/community consultation (NAM Table 5-3 parallel).
- **User feedback** → thumbs/report mechanisms on CDS outputs; not sufficient alone for algorithmovigilance.
- Risk catalog includes surveillance false-arrest precedent — relevant to biased clinical decision support.

No employer-stack APIs cited.

### 3. Redundancy

| Canon title | Overlap | Notes |
|-------------|---------|-------|
| **nam_gen_ai_health_2025 sec05** | **High (mandatory pair)** | sec05 operationalizes what ch9 structures generically |
| **responsible_ai_practice_2025 ch01** | High | Policy survey; ch9 is implementation layer |
| **simon_aliferis_healthcare_2024 ch10** | Medium | Regulatory ELSI; Simon is FDA/GMLP depth |
| **ai_engineering_2025 ch10** | Medium | Engineering guardrails/observability; RAI is governance process |

**Dedup:** Treat ch9 as canonical for **domain-agnostic five-pillar governance playbook**; defer RACI/accountability detail to NAM sec05 Table 5-4.

### 4. Scholia fit

| Criterion | Assessment |
|-----------|------------|
| Worked examples | **Weak** — checklist and process steps only |
| Exercise hooks | **Moderate** — inferred drills + NAM pair |
| Chapter boundary | **Clean** — single governance chapter |
| Ingest suitability | **High** — w4 governance spine; mandatory NAM sec05 pair |

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **Edition currency** | **PASS** | 2025 Springer/Apress |
| **Author authority** | **PASS** | Duke (ex-Google Responsible AI PM, Bedrock AI); Giudici (Univ. Pavia, regulatory/statistical AI) |
| **Primary-source citation density** | **PASS** | NIST AI RMF harm taxonomy (⁶⁵); biorisk/phishing footnotes |
| **Contested claims flagged** | **PASS** | Biorisk unproven but high-rated; spear-phishing downgraded to low risk |
| **Worked examples** | **N/A** | Process chapter — Table 9-1 checklist suffices |

**Overall TEXTBOOK-Q1:** **PASS** — suitable w4 governance ingest; pair with NAM sec05 for operational RACI.

## Provenance (load-bearing claims)

| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| RAI-C09-001 | NIST categorizes AI harms to people, organizations, and systems | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch09_ingest.md | NIST harm taxonomy |
| RAI-C09-002 | Five governance pillars: policy, team, reviews, stakeholders, feedback | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch09_ingest.md | Governance structure |
| RAI-C09-003 | Table 9-1 requires capability, controllability, impact, verification, ethics testing | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch09_ingest.md | Table 9-1 |
| RAI-C09-004 | Developers often test accuracy/privacy only, omitting fairness/robustness/ethics | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch09_ingest.md | Uncovering new information |
| RAI-C09-005 | Policymakers informed by auditing, red-teaming, safety evaluations | compressed | Duke/Giudici 2025 | ISBN 979-8-8688-1166-1 | literature/cs-ai-textbook-canon/ingests/responsible_ai_practice_2025_ch09_ingest.md | Stakeholders |

---

*Ingest generated by scholia chapter fan-out · corpus `cs-ai-textbook-canon` · worker `rai-ingest-ch09-10` · word cap ≤4500*
