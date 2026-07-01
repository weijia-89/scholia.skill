# Composer Implementor Brief — Literature Batch 2025-06-27

Save to: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/peeples_ranade_liu_terk_refined_20250627.md

Sources digested: Peeples 2003 (rhetoric anthology), Liu et al. 2024 (AI detection empirical), Terk 2010 (business writing workbook). Ranade et al. 2024 fully excluded — all claims failed kill register.

Full audit trail, verbatim Q-bank, and kill register: operator saves separately to references/audit-trail.md. This file contains only what the Composer agent needs to execute edits.

---

## 1 — Five Surviving Concepts

Each concept is one idea the agent must add to exactly one file. Nothing else from the four sources enters the skill files.

### Concept A — Summons Test (deai)

Principle: A document succeeds only if it acts in the world — summons, persuades, authorizes, compels. Surface quality (grammar, coherence, polish) is necessary but not sufficient. Text that reads well but does nothing is a failed document.

Source: Peeples 2003, Introduction p. 4.

Lane: deai_removal.

Epistemic status: The writing-craft principle is verified. The claim that RLHF-polished text routinely fails this test is speculative (Peeples predates LLMs by 20 years). Tag both in the skill file entry.

ESL: N/A.

DO example: "This memo requests budget approval for Q3 headcount. Approve by Friday or the req expires." — acts in the world.

DO-NOT example: "It is important to note that headcount planning requires careful consideration of multiple factors." — acts on nothing.

### Concept B — Situated Reasoning over Formula Import (deai)

Principle: Expert writing generates rhetorical analysis specific to the current situation rather than importing templates. Formulaic responses fail as situation complexity increases.

Source: Peeples 2003, Introduction pp. 2-3.

Lane: deai_removal.

Epistemic status: Writing-craft principle is verified. Application as "anti-AI-flattening signal" is speculative.

ESL: yes. L1-influenced reasoning sequences (explicit if-then chains, causal markers) are a form of situated reasoning. Do not smooth these into idiomatic English.

DO example: "Given that this client's renewal is 45 days out and they raised pricing concerns last QBR, the proposal leads with the usage-based tier." — situation-specific.

DO-NOT example: "Dear valued customer, we are pleased to present our competitive pricing options." — template import.

### Concept C — ESL False-Positive Warning (deai)

Principle: Vocabulary diversity and "grammatical errors" are not reliable AI tells for L2 writers. AI detectors misclassify non-native English writing as AI-generated at rates up to 61% (Liang et al. 2023, Patterns). Narrower lexical range in L2 writers is legitimate. Artificial synonym rotation to "sound diverse" is itself RLHF residue.

Source: Liu et al. 2024 (DOI 10.1007/s40979-024-00155-6), citing Liang et al. 2023 (DOI 10.1016/j.patter.2023.100779).

Lane: deai_removal.

Epistemic status: Liang 2023 is verified external (Patterns, peer-reviewed). Liu 2024 scope: GPT-3.5, rehabilitation domain, constrained checklist, n=4 reviewers, confidence capped at 60. RECENCY RISK on all Liu findings.

ESL: yes — this IS the ESL-protect entry.

NEVER: Flag vocabulary repetition as an AI tell. NEVER: Recommend synonym rotation to "humanize" text. NEVER: Treat L1-transfer syntax (article omission, preposition variation) as AI signal.

### Concept D — Key-Sentence Surfacing (tic)

Principle: After drafting, verify the main point appears in the first paragraph and a reader can identify it without re-reading. Test: could you state the key sentence to someone in three seconds?

Source: Terk 2010, Lesson 1 pp. 25-29.

Lane: tic_enrichment.

Epistemic status: Tier 3 practitioner-prescriptive. No empirical validation. Consistent with standard business-writing pedagogy.

ESL: yes. Frame as genre convention for business correspondence, not as L1 correction. L1 Chinese topic-comment structure (main point last) is legitimate in other contexts. The craft move is: surface the key sentence early for this genre.

### Concept E — Voice Through Invention and Arrangement (tic)

Principle: Voice enrichment through what you choose to argue (invention) and what order you present it in (arrangement), not just word choice and sentence rhythm (style). A writer who includes what others exclude or structures an argument in a non-template order has stronger voice signal than one with merely distinctive vocabulary.

Source: Foss/Foss/Trapp via Peeples 2003, pp. 14-15. The five canons of rhetoric (invention, arrangement, style, memory, delivery) are verified via Aristotle primary text.

Lane: tic_enrichment.

Epistemic status: The five canons are verified. The claim that LLMs over-index on style is inferred from output observation, not formally studied.

ESL: yes. Non-native writers often have strong invention and arrangement habits from L1 rhetorical traditions that differ from English belletristic norms. These are craft strengths, not deficits.

---

## 2 — Edit Blocks (literal content, copy-paste)

Each block is one atomic edit. Execute in order. Do not batch. Do not rephrase — copy the content verbatim into the target file.

### Edit 1 of 6

File: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md

Action: APPEND the following section at the end of the file.

```markdown
## Summons Test (Peeples 2003)

A document succeeds only if it acts in the world. Surface quality (grammar, coherence, polish) is necessary but not sufficient. If a text reads well but does nothing — summons no one, persuades no one, authorizes nothing — it has failed its rhetorical purpose regardless of surface quality.

Application to AI detection \[speculative\]: RLHF-polished text may pass product-quality checks (coherence, fluency) but fail the summons test because it lacks situated social action. This link is the operator's inference, not Peeples' claim. Peeples wrote in 2003, before LLMs existed.

Source: Peeples, T. (ed.) (2003). Professional Writing and Rhetoric. Longman. Introduction p. 4.

```

### Edit 2 of 6

File: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md

Action: APPEND the following section after the section added in Edit 1.

```markdown
## Situated Reasoning over Formula Import (Peeples 2003)

Expert writing generates rhetorical analysis specific to the current situation rather than importing generic templates. Formulaic responses fail proportionally to situation complexity. For routine genres (standard memos, acknowledgments), formulas may suffice. For novel or high-stakes situations, context-specific reasoning is required.

Application to AI detection \[speculative\]: The entire AI writing pipeline is formula import. Context-specific rhetorical reasoning cannot be templated. This link is the operator's inference.

\[esl_preserve\] L1-influenced reasoning sequences (explicit if-then chains, causal markers like "because of this, therefore") are a form of situated reasoning. Do not smooth these into idiomatic English or flag them as disfluency.

Source: Peeples 2003, Introduction pp. 2-3.

```

### Edit 3 of 6

File: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md

Action: APPEND the following section after the section added in Edit 2.

```markdown
## ESL False-Positive Warning (Liu 2024, Liang 2023)

Vocabulary diversity and "grammatical errors" are not reliable AI tells for L2 writers. AI detectors misclassify non-native English writing as AI-generated at rates up to 61% on TOEFL essays.

NEVER flag these as AI signals:
- Narrower lexical range (legitimate L2 register)
- L1-transfer syntax (article omission, preposition variation, tense marking)
- Repetitive word choice in domain-specific writing (succinctness is valid academic style)

NEVER recommend synonym rotation to "humanize" text. Artificial synonym rotation is itself RLHF residue.

Scope note: Liu et al. 2024 findings are from GPT-3.5, rehabilitation domain, constrained checklist, n=4 reviewers, confidence capped at 60. \[RECENCY RISK\] — all detector performance numbers are August 2023 snapshots.

Sources:
- Liu et al. (2024). The great detectives. Int J Educ Integrity, 20:8. DOI 10.1007/s40979-024-00155-6.
- Liang et al. (2023). GPT detectors are biased against non-native English writers. Patterns, 4(7):100779. DOI 10.1016/j.patter.2023.100779.

```

### Edit 4 of 6

File: /Users/dubs/.cursor/skills/tic/SKILL.md

Action: APPEND the following section at the end of the file, before any existing references or bibliography section.

```markdown
## Key-Sentence Surfacing (Terk 2010)

After drafting any business document, run this check:

1. Is the main point in the first paragraph?
2. Can a reader identify it without re-reading?
3. Could you state it to someone in three seconds?

If any answer is no, restructure. Move the key sentence to the first paragraph. The key sentence is the single sentence carrying the document's most important message.

\[esl_preserve\] This is a genre convention for business correspondence. L1 Chinese topic-comment structure (context first, main point last) is legitimate in other genres. The craft move is: surface the key sentence early for this specific genre, not "fix your English."

Evidence tier: Tier 3, practitioner-prescriptive, no empirical validation. Consistent with standard business-writing pedagogy (Locker, Ober, similar textbooks).

Source: Terk, N. (2010). Professional Writing Skills. Write It Well. Lesson 1, pp. 25-29.

```

### Edit 5 of 6

File: /Users/dubs/.cursor/skills/tic/SKILL.md

Action: APPEND the following section after the section added in Edit 4.

```markdown
## Voice Through Invention and Arrangement (Peeples/Foss 2003)

Most voice-enrichment work focuses on style (word choice, sentence rhythm). This is incomplete. Voice also lives in:

- Invention: what you choose to argue, what you include, what you exclude. A writer who includes what others leave out — or excludes what everyone includes — has a stronger voice signal than one with merely distinctive vocabulary.
- Arrangement: what order you present arguments in, what gets emphasis through position. Non-template structures carry voice. Template structures flatten it.

When enriching voice in a draft, ask:
1. Does the content include anything surprising or exclude anything expected? (invention)
2. Does the structure serve the argument or follow a template? (arrangement)
3. Does the register match the specific rhetorical situation? (style — but only after 1 and 2)

\[esl_preserve\] Non-native writers often have strong invention and arrangement habits from L1 rhetorical traditions that differ from English belletristic norms. These are craft strengths. Preserve them.

Evidence tier: Tier 2.5 (Foss/Foss/Trapp disciplinary survey via Peeples 2003). The five canons of rhetoric (invention, arrangement, style, memory, delivery) are verified via Aristotle primary text.

Source: Foss, Foss, & Trapp, "Perspectives on the Study of Rhetoric," in Peeples (ed.), Professional Writing and Rhetoric (2003), pp. 14-15.

```

### Edit 6 of 6

File: /Users/dubs/.cursor/skills/tic/SKILL.md

Action: APPEND the following section after the section added in Edit 5.

```markdown
## Category-Based Organization (Terk 2010)

For documents longer than 3 paragraphs, organize bottom-up:

1. Brainstorm all points.
2. Group into 3-5 categories.
3. Write one summary sentence per category (names the topic + says why it matters).
4. Each category becomes one paragraph, opened by its summary sentence.
5. Let the content determine the categories — do not impose a pre-set outline template.

\[esl_preserve\] This organizational method is language-neutral. Category labels and summary sentences work regardless of L1 influence on syntax.

Evidence tier: Tier 3, practitioner-prescriptive, no empirical validation.

Source: Terk, N. (2010). Professional Writing Skills. Write It Well. Lesson 1, pp. 38-46.

```

---

## 3 — Anti-Patterns (NEVER DO)

The agent must not do any of the following during or after executing the edit blocks above.

1. NEVER reference Ranade et al. 2024 in any skill file. All claims from that paper are WRONG or ZOMBIE. If any reference to Ranade, "rhetorical prompt-formula," or "Prompt = (audience + genre + purpose + subject + context + exigence + writer)" appears in a skill file after edits, the edit session has failed.

2. NEVER modify /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md. This file is inherited. No re-litigation.

3. NEVER create files not listed in the edit blocks above. Only two files are touched: craft-theory-reference.md and tic/SKILL.md.

4. NEVER remove existing content from either file. All edits are APPEND operations.

5. NEVER rephrase the edit block content. Copy verbatim. The epistemic tags (\[speculative\], \[esl_preserve\], \[RECENCY RISK\], evidence tiers) are part of the content, not metadata to strip.

6. NEVER recommend "increasing vocabulary diversity" or "fixing grammar for professional tone" anywhere in any file touched by these edits. These are ESL-hostile moves that this batch explicitly kills.

---

## 4 — Verification Checklist

After executing all 6 edits, verify each row. If any row is FAIL, halt and escalate to operator.

| Check | How to verify | PASS/FAIL |
| --- | --- | --- |
| Edit 1 content verbatim in craft-theory-reference.md | Search for "Summons Test (Peeples 2003)" — must match Edit 1 exactly |  |
| Edit 2 content verbatim in craft-theory-reference.md | Search for "Situated Reasoning over Formula Import" — must match Edit 2 exactly |  |
| Edit 3 content verbatim in craft-theory-reference.md | Search for "ESL False-Positive Warning" — must match Edit 3 exactly |  |
| Edit 4 content verbatim in tic/SKILL.md | Search for "Key-Sentence Surfacing (Terk 2010)" — must match Edit 4 exactly |  |
| Edit 5 content verbatim in tic/SKILL.md | Search for "Voice Through Invention and Arrangement" — must match Edit 5 exactly |  |
| Edit 6 content verbatim in tic/SKILL.md | Search for "Category-Based Organization (Terk 2010)" — must match Edit 6 exactly |  |
| No Ranade references anywhere | Search both files for "Ranade" — zero results required |  |
| No modifications to decision canon | Verify /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md is untouched |  |

---

## 5 — What is NOT in this brief (operator reference)

The following were in the full digest but are excluded from Composer scope because they require operator judgment, not agent execution:

* Peeples ethics-as-textual-feature (CM-D03): Entirely speculative for AI application. Operator can promote if empirical evidence emerges.
* Peeples three-binary diagnostic (CM-D04): Useful as operator-level analytical framework but too abstract for a skill file instruction. A low-thinking model cannot execute "diagnose which binary the draft collapses."
* Liu et al. redundancy-across-sections (CM-D05): RECENCY RISK too high — GPT-4+ partially addresses this. Operator should re-evaluate after testing against current models.
* Liu et al. evidence-anchoring (CM-D06): Partially addressed by RAG pipelines. Operator should assess whether existing guidance already covers this.
* Terk reader-first planning gate: Standard pre-writing advice that any model already knows. Adding it to a skill file would increase context load without adding capability delta.
* Terk probability discourse: Too abstract for a skill file instruction ("handle uncertainty through calibrated epistemic markers"). Needs concrete examples to be actionable — operator should develop these.
* Co-inquiry register (Peeples): Downgraded to context-only. No mechanism or falsifier available.
* Grammar-as-credibility (Terk): SPLIT — proofread high-stakes externals is pragmatic (operator already knows this); blanket prescriptivism is accent erasure (killed).
* Full audit trail, verbatim Q-bank, kill register with confidence scores, adversarial review: Save separately to references/ for future ingest cycles.