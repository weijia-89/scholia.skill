# Ingest: Terk Professional Writing Skills — Lesson 3

slug: terk_prof_writing_skills chapter_id: lesson03 chapters_attested: lesson03 only source: source_exports/chapters/08_terk_prof_writing_skills_lesson03.txt schema: scholia SF-12 ≤4500w lane_tags: deai_removal, tic_enrichment, both, esl_preserve

---

## 1\. Chapter Summary

Lesson 3 teaches concise language through three mechanics: (a) collapsing multi-word phrases into single words, (b) eliminating redundant doublings, and (c) cutting wasteful possessives, relative clauses, and existential-there constructions. The pedagogy is exercise-heavy — roughly 60% of the chapter is practice + revision pairs. The theory is thin but operationally precise: every technique maps to a mechanical deletion or substitution rule, not a judgment call.

---

## 2\. Gate A — Verbatim Q-Bank (lesson03 only)

All quotations below appear verbatim in the attached chapter text.

Q-001 | "Unnecessary words are obstacles to good business writing. They clutter up your sentences and slow your readers down. They can also make your documents boring." anchor: INTRODUCTION, p.101

Q-002 | "at a time prior to simply means before. The longer phrase is dull and bulky. The single word does the same job more efficiently." anchor: USE ONE WORD FOR A ONE-WORD IDEA, p.102

Q-003 | "We are in agreement with you about the contract terms." → "We agree with you about the contract terms." anchor: USE ONE WORD FOR A ONE-WORD IDEA, p.102

Q-004 | "She solved the problem in a clever way." → "She solved the problem cleverly." anchor: USE ONE WORD FOR A ONE-WORD IDEA, p.102

Q-005 | "A crisis is always serious, plans are always for the future, and ten a.m. doesn't happen at night. These unnecessary words waste your readers' time." anchor: AVOID REPETITION, p.104

Q-006 | "Their assumption is that the company should always come first." → "They assume the company should always come first." anchor: ELIMINATE WASTEFUL POSSESSIVES, CLAUSES, AND THERE IS PHRASES, p.105

Q-007 | "There is a new package on your desk." → "A new package is on your desk." anchor: ELIMINATE WASTEFUL POSSESSIVES, CLAUSES, AND THERE IS PHRASES, p.105

Q-008 | "There may be several applicants who have the necessary background for this position." → "Several applicants may have the necessary background for this position." anchor: ELIMINATE WASTEFUL POSSESSIVES, CLAUSES, AND THERE IS PHRASES, p.105

Q-009 | "The broker who works in Chicago sent the file that is incomplete to the home office." → "The Chicago broker sent the incomplete file to the home office." anchor: ELIMINATE WASTEFUL POSSESSIVES, CLAUSES, AND THERE IS PHRASES, p.105

Q-010 | Review fill-in: "\________\_ words are obstacles to good business writing." (answer: Unnecessary) anchor: REVIEW, p.113

Q-011 | Review fill-in: "Sometimes you can collapse several words or a long phrase into \____\_ that conveys your message quickly and clearly" (answer: one word) anchor: REVIEW, p.113

---

## 3\. Core Techniques Extracted

### 3a. Phrase-to-word collapse \[both\]

The chapter identifies two sub-patterns:

* Nominalization reversal: convert noun-phrase back to verb. "are in agreement" → "agree"; "made an offer" → "offered"; "made a study" → "studied"; "made an improvement" → "improve"; "are of the opinion" → "believe"
* Prepositional-phrase-to-adverb: "in a reckless manner" → "recklessly"; "in a clever way" → "cleverly"; "in a hasty manner" → "hastily"; "in a prompt way" → "soon"

### 3b. Redundancy elimination \[both\]

Tautological doublings where one word already encodes the other:

| Redundant phrase | Survivor | Why redundant |
| --- | --- | --- |
| alternative choices | alternatives OR choices | "alternative" already implies choice |
| basic fundamentals | fundamentals | fundamentals are inherently basic |
| serious crisis | crisis | crisis implies severity |
| final outcome | outcome | outcome implies finality |
| past experience | experience | experience is inherently past |
| future plans | plans | plans are inherently future |
| advance warning | warning | warning is inherently advance |
| end result | result | result implies endpoint |
| ten a.m. in the morning | ten a.m. | a.m. already means morning |
| equally as effective as | as effective as | "equally" and "as...as" duplicate |
| urban residents of the city | urban residents OR city residents | urban = of the city |
| subterranean garage, located underground | subterranean garage | subterranean = underground |

### 3c. Structural trimming \[both\]

Three sub-patterns:

* Possessive deflation: "Their assumption is that..." → "They assume that..." (convert possessive + nominalization back to subject + verb)
* Relative-clause absorption: "The broker who works in Chicago" → "The Chicago broker"; "the file that is incomplete" → "the incomplete file"; "employees who want to" → "employees wanting to" \[inferred extension\]
* Existential-there deletion: "There is X on Y" → "X is on Y"; "There are several employees who..." → "Several employees..."

---

## 4\. Craft-Move Extraction

### Move L3-01: Nominalization-to-verb reversal \[deai_removal\]

Pattern: {light verb} + {nominalized noun} → {root verb}

* "make a decision" → "decide"
* "conduct a survey" → "survey"
* "make an offer" → "offer"
* "will have the capability of processing" → "can process"

Operational rule: when editing AI output, search for "make/made a," "conduct/conducted a," "perform/performed a," "provide/provided a" + noun. Replace with the verb form of the noun.

RLHF relevance: RLHF drives verbosity via length bias in reward models \[verified — Singhal et al. 2023, arxiv 2310.03716\]. Light-verb + nominalization constructions are a plausible verbosity vehicle, but no study has measured their specific frequency in RLHF-trained output vs. base models. \[speculative — C-001\] The claim that this is the "single highest-yield de-AI move" is operator observation, not measured. \[speculative — C-002\]

\[c1=70, c2=55, c3=65\] FINAL=65

### Move L3-02: Prepositional-phrase-to-adverb \[deai_removal\]

Pattern: "in a {adj} manner/way/fashion" → "{adj}-ly"

* "in a reckless manner" → "recklessly"
* "in a prompt way" → "promptly" / "soon"

RLHF relevance: same inference gap as L3-01. The pattern is mechanically clear and low-ambiguity, making it useful regardless of whether RLHF specifically drives it. \[speculative — C-003\]

\[c1=70, c2=60, c3=65\] FINAL=65

### Move L3-03: Tautological-doubling removal \[deai_removal\]

The chapter's redundancy list (Section 3b) encodes real semantic knowledge. These doublings overlap with AI-writing patterns documented in practitioner tools (blader/humanizer Pattern 23), but no study measures tautological-doubling frequency specifically in RLHF output. \[speculative — C-004\]

Operational rule: maintain a tautology watchlist. On de-AI pass, search-and-delete the redundant modifier.

\[c1=65, c2=55, c3=60\] FINAL=60

### Move L3-04: Existential-there deletion \[deai_removal\]

"There is/are/may be" constructions defer the subject, creating softer openings. RLHF drives hedging and softening \[inferred from verified RLHF verbosity/hedging data — C-005\]. Terk's fix: promote the real subject to sentence-initial position.

Guard required: existential-there is not always clutter. Halliday & Matthiessen (2014) analyze it as a Textual Theme that introduces hearer-new information \[verified — C-006, via Collins 2001 ALS proceedings; Jiang & Zhang 2022 Frontiers in Psychology\]. Delete when the subject is already given/known. Preserve when introducing a genuinely novel entity into discourse.

\[c1=68, c2=62, c3=60\] FINAL=62

### Move L3-05: Relative-clause absorption \[both\]

"The broker who works in Chicago" → "The Chicago broker." Collapses a relative clause into a pre-nominal modifier.

Dual-lane value: cleanup of over-generated relative clauses + rhythm tightening for voice. Guard against over-absorption of complex clauses where a single adjective cannot encode the information.

\[c1=70, c2=65, c3=62\] FINAL=65

### Move L3-06: Possessive-nominalization deflation \[deai_removal\]

"Their assumption is that..." → "They assume that..." Same nominalization-reversal as L3-01 but triggered by possessive + copula + nominalization. Inherits the same evidence gaps as L3-01.

\[c1=68, c2=60, c3=62\] FINAL=62

### Move L3-07: Filler-phrase deletion \[deai_removal\]

The chapter's extended revision exercise (pp.107-110) reveals a category of pure filler:

* "I would like to take this opportunity to inform you that" → (delete entirely)
* "On the basis of your recent letter" → "Thank you for your recent letter" or delete
* "At this point in time" → "Now" or delete
* "for the purpose of" → "to"
* "in order to" → "to"
* "with regard to" → "about" / "regarding"
* "due to the fact that" → "because" / "since"
* "as to whether" → "whether"
* "in regard to" → "about"

RLHF relevance: These items overlap substantially with filler patterns documented in AI-writing detection tools. The blader/humanizer project (Pattern 23, SKILL.md lines 354-390) lists identical mappings: "In order to"→"To", "Due to the fact that"→"Because", "At this point in time"→"Now" \[verified — Gate A: HTTP 200; Gate B: claim matches source\]. Leap AI and Metric37 articles confirm these as characteristic AI-writing markers. However, these patterns also appear in pre-RLHF training data; isolating the RLHF contribution specifically is not possible from available evidence. \[inferred — C-008\]

\[c1=78, c2=70, c3=72\] FINAL=72

---

## 5\. Skill Incorporation Table

| ID | Terk Move | Action | Lane | Rationale |
| --- | --- | --- | --- | --- |
| L3-01 | Nominalization-to-verb | KEEP | deai_removal | High-yield candidate for RLHF verbosity cleanup \[speculative re: RLHF-specific frequency\]. Mechanically clear regardless of causal mechanism. |
| L3-02 | Prep-phrase-to-adverb | KEEP | deai_removal | Low ambiguity, mechanical fix. Useful for automated lint checklist. |
| L3-03 | Tautological doubling | KEEP | deai_removal | Useful as a deletion dictionary. No measured frequency data for RLHF-specific overproduction. |
| L3-04 | Existential-there deletion | CHANGE | deai_removal | Apply with information-structure guard: delete only when subject is given/known, not when introducing genuinely new referent \[verified — Halliday & Matthiessen 2014; Collins 2001\]. Terk oversimplifies by treating all existential-there as clutter. |
| L3-05 | Relative-clause absorption | KEEP | both | Dual-lane value: de-AI cleanup + rhythm tightening. Guard against over-absorption of complex clauses. |
| L3-06 | Possessive-nominalization deflation | KEEP | deai_removal | Sub-pattern of L3-01 with distinct trigger; worth separate lint rule. |
| L3-07 | Filler-phrase deletion | KEEP | deai_removal | Strongest overlap with documented AI-writing filler patterns \[inferred from blader/humanizer, Leap AI, Metric37\]. Directly transferable to de-AI pass dictionary. |
| L3-08 | "One word for one-word idea" (general principle) | KEEP | both | Meta-principle governing L3-01 through L3-06. Editorial heuristic, not a mechanical rule. |
| L3-09 | AI-specific tautology extensions | ADD | deai_removal | Extend Terk's static list with observed AI tautologies: "completely eliminate," "actively engage," "carefully consider," "clearly demonstrate." \[speculative — based on practitioner observation, no frequency study\] |
| L3-10 | \[esl_preserve\] guard on concision moves | ADD | esl_preserve | L1-Chinese existential-there overproduction is documented \[verified — Jiang & Zhang 2022, Frontiers in Psychology: 80.8% production rate at elementary level vs. 63.5% native\]. Concision rules must not flag L1-transfer patterns in operator prose as "clutter." The specific mapping of Chinese doubled-emphasis (重要的关键 → "important essentials") is constructed, not attested in SLA literature. \[speculative — C-009\] |
| L3-11 | Exercise-based self-audit | DROP | — | The chapter's assignment format is pedagogically fine but not operationally useful for automated de-AI passes. The craft moves themselves (L3-01–L3-07) transfer; the format does not. |

---

## 6\. Adversarial Review

### Claim Registry

| ID | Claim | Tag | Source | Failure mode |
| --- | --- | --- | --- | --- |
| C-001 | RLHF over-produces nominalizations | \[speculative\] | No direct measurement exists | Could be base-model frequency, not RLHF-amplified |
| C-002 | Nominalization-to-verb is "single highest-yield" de-AI move | \[speculative\] | Operator judgment | Other patterns (filler phrases) may have higher frequency |
| C-003 | AI prefers prepositional phrases over adverbs | \[speculative\] | Inferred from length bias | No per-pattern frequency data |
| C-004 | RLHF models produce tautological doublings | \[speculative\] | No measurement | May be training-data frequency, not RLHF-specific |
| C-005 | Existential-there is RLHF-frequent due to hedging function | \[inferred\] | Chain: RLHF→hedging (verified) + there-as-hedging (established) | Frequency of this specific construction unmeasured |
| C-006 | Existential-there has legitimate information-structure function | \[verified\] | Collins 2001; Halliday & Matthiessen 2014; Jiang & Zhang 2022 | None identified |
| C-007 | L1-Chinese speakers overproduce existential-there | \[verified\] | Jiang & Zhang 2022 (N=320, GLMM, p<0.001) | Study is Chinese university students; may not generalize to all L1-Chinese populations |
| C-008 | Every L3-07 filler item is RLHF-frequent | \[inferred\] | blader/humanizer Pattern 23; Leap AI; Metric37 | Items also in pre-training data; RLHF amplification not isolated |
| C-009 | Chinese 重要的关键 maps to "important essentials" | \[speculative\] | Constructed example | No SLA attestation found |
| C-010 | RLHF reward models exhibit length bias | \[verified\] | Singhal et al. 2023 (arxiv 2310.03716): 70-90% of reward gain = length | Tested on Llama-7B with 3 datasets; generalization to larger models uncertain |
| C-011 | The chapter's mechanical specificity is excellent | \[verified\] | Direct observation of source text | Pedagogical quality ≠ empirical validity |

### Kill List

* C-001: OVERSTATED. No study measures nominalization frequency in RLHF vs. base output. Retagged \[speculative\]. Confidence dropped from 88 to 65.
* C-002: OVERSTATED. Yield ranking is operator observation. Retagged \[speculative\]. Removed "single highest-yield" claim.
* C-003: OVERSTATED. Causal claim about "thorough" removed. Retagged \[speculative\]. Confidence dropped from 82 to 65.
* C-004: OVERSTATED. No frequency data for tautological doublings in RLHF output. Retagged \[speculative\]. Confidence dropped from 78 to 60.
* C-008: OVERSTATED. "Every item is RLHF-frequent" → "items overlap substantially with documented AI-writing filler patterns." Retagged \[inferred\]. Confidence dropped from 90 to 72.
* C-009: UNTESTED. The 重要的关键 example is constructed. May not appear as load-bearing in synthesis.

### Overconfidence Check

Original document: 6 of 7 craft-move scores were 78+. After adversarial review, all scores reduced. New distribution: 60, 62, 62, 65, 65, 65, 72. Zero scores above 80. Overconfidence pattern resolved.

### Three Strongest Hostile-Expert Objections

1. The RLHF-to-specific-pattern causal chain is unsupported. RLHF drives length (verified). But the jump from "length bias" to "RLHF causes nominalizations / prepositional phrases / tautological doublings specifically" has no empirical basis. The document now marks this gap explicitly on every affected craft move.

2. Terk's advice predates LLMs entirely. The original document repeatedly frames Terk's concision rules as "de-AI" tools without acknowledging that these are general plain-language principles that happen to overlap with AI-writing patterns. The overlap is real but the framing implies Terk was designed for de-AI work, which is false. Addressed by reframing: the moves are useful for de-AI work because verbosity patterns overlap, not because Terk anticipated RLHF.

3. The ESL guard (L3-10) rests partly on a constructed example. The underlying principle (L1-Chinese topic-comment transfer affects existential-there usage) is verified. But the specific 重要的关键 → "important essentials" mapping is speculative and should not be cited as evidence in downstream implementations without SLA attestation. Addressed by flagging.

### What Could Not Be Verified

* Whether any specific syntactic pattern (nominalization, prepositional phrase, tautological doubling) is more frequent in RLHF-trained output than in base-model output. This is the central gap. A comparative corpus study (RLHF vs. SFT output, annotated for these patterns) would resolve it.
* Whether Terk's redundancy list generalizes beyond business English to technical writing.
* Whether the "Write It Well" series has empirical validation against readability metrics.
* How Terk handles concision vs. register in later chapters.

---

## 7\. Coverage Attestation

chapters_attested: lesson03 only. No claims derived from lessons 1, 2, or 4+. All Q-bank entries verified against attached text. FR-3 enforced.

---

## 8\. Synthesis

What survives adversarial review:

* Terk's seven craft moves (L3-01 through L3-07) are mechanically precise and operationally transferable to de-AI editing passes. This is the chapter's primary value.
* The filler-phrase list (L3-07) has the strongest external corroboration: identical items appear in the blader/humanizer Pattern 23 library and in multiple AI-writing detection articles. Confidence: 72 (highest surviving score).
* The existential-there guard (L3-04 CHANGE action) is the document's most evidence-backed correction to Terk: information-structure theory and SLA data both confirm that blanket deletion of existential-there is wrong.
* The ESL guard (L3-10) is operationally necessary: L1-Chinese existential-there overproduction is empirically documented, and flagging these patterns as "clutter" in operator prose would violate \[esl_preserve\].
* RLHF drives verbosity through length bias in reward models. This is the verified anchor for the entire de-AI lane. But the specific claim that RLHF amplifies nominalizations, prepositional phrases, or tautological doublings over base rates is speculative. The craft moves remain useful for verbosity reduction regardless of whether the causal mechanism is RLHF-specific or general writing-quality improvement.