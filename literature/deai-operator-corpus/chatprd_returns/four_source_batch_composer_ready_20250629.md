# Composer-Ready Skill Patches — Four-Source Batch

Provenance: Ranade 2024, Locker 2012, Long 2018, Lu & Ai 2015. Two adversarial passes complete. Research audit: see git history for four_source_batch_refined_20250629.md.

Save to: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/four_source_batch_composer_ready_20250629.md

---

## How to use this document

This file contains two skill-patch blocks. Each block is a self-contained markdown section that Composer 2.5 should paste into the target SKILL.md file at the indicated location.

Implementor workflow:

1. Open the target file listed in each patch header.
2. Find the insertion point (section name given).
3. Paste the block verbatim. Do not paraphrase, reorder, or summarize.
4. Run the post-paste checklist at the bottom of this document.

---

## PATCH 1: deai.skill — AI-Signal Removal Craft Moves

Target file: /Users/dubs/.cursor/skills/deai/SKILL.md Insert under: voice-craft / signal-identification section (create if absent) Also add bibliography entries to: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md

### Detection-Bias Principle

MUST include this principle in the detection-bias section:

NNS writers face disproportionate false-positive rates from perplexity-based AI detectors. Liang et al. 2023 measured a 61.22% false-positive rate on TOEFL essays across seven detectors. The underlying linguistic variation is L1-specific (Lu & Ai 2015, N=1600, 14 syntactic measures, 7 L1 groups) — pooled NNS baselines erase these differences and create phantom-norm bias. The causal link between syntactic-complexity features and deployed detector mechanisms is undemonstrated; deployed detectors use perplexity, not syntactic-complexity measures. Tag: \[speculative — mechanism pathway unconfirmed\].

### Signal: Prompt-Formula Residue

Tag: \[inferred:detection-literature\] \[stale — derived from GPT-3 era, untested on GPT-4+/Claude 3+\]

When all seven rhetorical elements appear in sequence — audience declared, genre stated, purpose announced, subject named, context framed, exigence asserted, writer positioned — the text reads as mechanically prompted. Human writers leave several of these implicit.

How to detect: Scan for sequential mechanical completeness. If all seven elements appear within the first two paragraphs in order, flag for review.

ESL guard: Some L1-Chinese academic conventions and some disciplinary formats (regulatory filings, FDA labeling) include explicit audience and purpose statements. MUST NOT flag these as AI signals when they reflect legitimate convention.

Source: Ranade et al. 2024 prompt formula (not a detection paper — diagnostic vocabulary only).

### Signal: Genre Over-Conformity

Tag: \[inferred:detection-literature\] \[stale\]

AI outputs hit every rubric criterion for a genre template. Human writers adapt genre conventions to context and routinely deviate from textbook specs.

How to detect: Compare output against the textbook genre template. If conformity is 100%, flag. If the domain conventionally demands full conformity (regulated filings, legal briefs), this signal is invalid.

ESL guard: Genre conventions vary cross-culturally. Chinese academic memo format differs from US TPC format. Genre deviation in cross-cultural contexts is not deficiency.

### Signal: Audience Echo-Back

Tag: \[inferred:detection-literature\] \[stale\]

AI outputs explicitly declare the target audience in the opening: "This guide is for novice users." Human writers encode audience implicitly through register, vocabulary, and assumed knowledge.

How to detect: Flag opening declarations that parrot the audience specification.

ESL guard: Do not flag when explicit audience statement reflects disciplinary practice.

### Signal: Feeling-Attribution (RLHF Residue)

Tag: \[inferred:craft-transfer\]

RLHF-trained models inject feeling-prediction phrases: "I'm happy to help," "Great news!" "You'll be pleased to know." These are the same patterns that Locker (BAC 10e) tells human writers to delete because they are distancing.

How to detect: Flag any phrase that predicts or names the reader's emotional response.

Before (AI pattern): "You'll be happy to hear that your request has been approved." After (signal removed): "Your request has been approved."

Cross-ref: tic.skill TIC-03 (feeling-attribution deletion).

### Signal: Synonym Rotation

Tag: \[speculative:symptom-overlap — Long diagnoses a human problem; RLHF is a training artifact; symptoms overlap but causes differ\]

RLHF-trained models cycle synonyms to avoid repetition: "utilize / leverage / employ / harness." Long (2018) calls the human version of this the "use once and discard" philosophy — treating words like disposable objects.

How to detect: Flag forced synonym variation within a paragraph where one word is the right word.

Remedy: Repeat the right word. Deliberate repetition enacts meaning. If the repetition makes prose call attention to its own technique rather than its content, back off.

Test: "Is it a musical sound, whether plain or ornate, or is it the interminable drone of a washing machine?" (Long, Ch 2)

ESL guard: Deliberate repetition is natural in Chinese parallel structure. MUST NOT pressure operator toward false elegant variation.

### Signal: Abstract Hedging (Conventional Received Diction)

Tag: \[speculative:symptom-overlap\]

RLHF outputs default to abstract hedging: "various factors," "it is important to note," "significant implications." Long (2018) calls the human version "conventional received diction" — language of belief and agenda rather than sensory observation.

How to detect: Revision pass. Highlight abstract/general words. Test: can you name which sense organ perceives this word?

Before: "The project has significant implications for stakeholder engagement." After: "The project lets three department heads see the same dashboard before the Monday standup."

Limit: MUST preserve abstract nouns when the subject is genuinely abstract (strategy, risk, architecture). Mechanical replacement strips conceptual argument.

ESL guard: Concreteness is language-neutral. L1-influenced syntax is preserved while swapping abstract nouns for concrete ones.

### Banned Claims — Kill List

MUST NOT appear as supported assertions in any deai skill file:

* "AI-generated text is indistinguishable from human writing" — contradicted by detection literature and by Liang 2023 (detectors achieve near-perfect accuracy on NS text).
* "Plagiarism checkers fail to detect AI work" — Turnitin launched AI detection April 4, 2023. This conflates plagiarism detection with AI-authorship detection.
* "Rhetorical prompting alleviates bias" — no evidence (Ranade 2024 aspirational claim, zero measurement).
* Any promotion of \[speculative\] or \[inferred\] tags to \[verified\] without new empirical evidence.

### Bibliography Additions for craft-theory-reference.md

Add these entries:

* Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. Patterns, 4(7), 100779. DOI: 10.1016/j.patter.2023.100779. Tier 1. 7 detectors, 91 TOEFL + 88 NS essays. 61.22% NNS false-positive rate. Perplexity-based mechanism. \[verified\]
* Lu, X., & Ai, H. (2015). Syntactic complexity in college-level English writing: Differences among writers with diverse L1 backgrounds. JSLW, 29, 16-27. Tier 1. N=1600, 14 measures, 7 L1 groups. L1-specific syntactic variation concealed by pooled benchmarks. Detection-bias implications are \[speculative\].
* Ranade, N., Saravia, M., & Johri, A. (2024). Using rhetorical strategies to design prompts. AI and Society, 40(2), 711-732. Tier 2.5 (Open Forum section). Not a detection paper. Prompt-formula framework. \[stale\] \[inferred\]
* Long, P. (2018). The Writer's Portable Mentor (2nd ed.). UNM Press. Tier 3 (practitioner pedagogy). Creative nonfiction craft. All deai mappings are \[speculative:symptom-overlap\].
* Locker, K.O., & Kienzler, D.S. (2012). Business and Administrative Communication (10th ed.). McGraw-Hill. Tier 1.5 (pedagogical canon). Prescriptive, not empirically validated.

---

## PATCH 2: tic.skill — Voice Enrichment Craft Moves

Target file: /Users/dubs/.cursor/skills/tic/SKILL.md Insert under: voice-craft section (create if absent)

### Core Principle: Non-Deficit Framing

"The use of the NS group as a comparison point does not imply a deficit orientation of L2 writing wherein any NNS departure from NS usage is construed as a problem." — Lu & Ai 2015, Section 2

All voice-craft guidance below treats NNS syntactic departures as variation, not deviation. No move in this section prescribes convergence toward native-speaker norms. \[esl_preserve\]

### Move: Subject-Slot Swap

When announcing outcomes, deliverables, or status updates, put the reader's benefit or the outcome in the subject position. This is an information-architecture move, not pronoun counting.

Before: "We have completed the quarterly analysis and are pleased to share the results." After: "The quarterly analysis covers three new revenue streams. Full results are attached."

MUST NOT mechanically maximize "you" — over-insertion sounds manipulative. The move is: foreground what the reader gets, background what the writer did.

ESL guard: L1 Chinese topic-comment structure ("Regarding X, the situation is Y") is compatible with this move. Recommend "put the reader's benefit in subject position," not "sound more natural." \[esl_preserve\]

Source: Locker, BAC 10e, you-attitude framework (prescriptive pedagogy, not empirically validated on reception).

### Move: Negative-Context Passive/Impersonal

When delivering bad news, identifying errors, or stating constraints: replace second-person agent with impersonal subject or passive construction. This OVERRIDES "prefer active voice" specifically in face-threatening contexts.

Before: "You made no allowance for inflation in your estimate." After (impersonal): "This estimate makes no allowance for inflation." After (passive): "No allowance for inflation has been made in this estimate."

When to apply: Only when face-threat is present. Over-use of passive in non-negative contexts produces bureaucratic prose.

ESL guard: L1 Chinese rhetorical convention favors indirectness and passive/impersonal construction in face-threatening situations. This move validates rather than overrides L1 preference. Passive voice in negative contexts is a face-saving strategy with cross-cultural support, not a fluency deficit. \[esl_preserve\]

Source: Locker, BAC 10e, Ch 3 — you-attitude guideline 5.

### Move: Feeling-Attribution Deletion

MUST NOT predict or name the reader's emotional response. State the fact. Let the reader supply their own reaction.

"It's distancing to have others tell us how we feel — especially if they are wrong." — Locker, BAC 10e, Ch 3

Before: "You'll be happy to hear that your scholarship has been renewed." After: "Your scholarship has been renewed."

Before: "Great news! The deployment succeeded." After: "The deployment succeeded. Zero errors in the smoke test."

Scope: Delete the prediction, not the warmth. In genuine congratulatory contexts (awards, promotions), a brief warm phrase is fine — cut the presumption about how the reader feels.

RLHF cross-ref: This pattern overlaps with RLHF residue ("I'm happy to help," "Great news!"). See deai.skill signal: feeling-attribution.

ESL guard: L1 Chinese business rhetoric omits feeling-prediction naturally. MUST preserve this tendency rather than adding Anglo warmth fillers. \[esl_preserve\]

### Move: Organization-Resistance Calibration

Planning-stage decision. Before drafting any persuasive or request document, assess expected audience resistance.

* Low resistance or busy reader who expects your message: Lead with the ask or the news (direct pattern).
* High resistance or unsolicited outreach: Establish shared problem first, present solution, then make the ask (indirect/problem-solving pattern).

Direct and indirect are co-equal strategies selected by resistance level. MUST NOT frame direct as professional default and indirect as exception.

ESL guard: L1 Chinese rhetorical preference for context-first is an asset in unsolicited and high-resistance communication, not a deficit to correct. \[esl_preserve\]

Limit: In time-urgent internal communication to known-receptive audiences, indirect organization wastes reader time. Match to actual resistance, not to L1 default.

Source: Locker, BAC 10e, persuasion chapter.

### Move: Deliberate Repetition

When a word is the right word, repeat it. Do not rotate synonyms for false variety.

"Poor writers, timid writers, average writers, many teachers including writing teachers, and some editors despise a repeated word. Their philosophy is: use once and discard. To them words are like dental floss, toilet paper, chewing gum." — Long, Ch 2

Forms: anaphora (She broke... she broke... she broke...), polyptoton (trouble/troubled/troublemaker), simple re-use for bearing down on meaning.

Test: Does the repetition make the sentence perform its meaning, or is it accidental? If accidental, vary. If deliberate, keep.

Calibration: In professional prose, one or two strategic repetitions per paragraph. This is not literary-fiction density.

ESL guard: Deliberate repetition is natural in many L1 rhetorical traditions including Chinese parallel structure. MUST NOT pressure toward false elegant variation. \[esl_preserve\] \[inferred:craft-transfer — Long does not discuss ESL\]

### Move: Before/After Paragraph Revision Drill

Procedure (register-agnostic):

1. Copy one paragraph from current work.
2. Label it "before."
3. Apply one craft technique from this skill file (subject-slot swap, passive/impersonal, feeling-deletion, repetition, concreteness).
4. Read the revised version aloud until it sounds right to your ear.
5. Type the "after" version back into the document.
6. Compare. Keep whichever is stronger.

One technique per pass. The read-aloud step is the feedback loop that prevents mechanical rule-application from producing robotic prose. The ear is the final arbiter, not the rule.

ESL guard: "Your ear" develops iteratively through exposure and practice. The L2 ear is a legitimate ear, not a deficient one. Reading aloud in L2 builds prosodic competence without requiring L1 norms. \[esl_preserve\] \[inferred:craft-transfer — Long does not discuss ESL\]

Source: Long, How to Use This Book + Ch 2 (one worked example: Munter paragraph). Effectiveness is anecdotal — adopt the procedure, not an efficacy claim.

### Move: L1-Chinese Syntactic Signature as Voice Resource

Population-level finding (Lu & Ai 2015, N=1600, cross-sectional, confidence capped at 58):

* Chinese-L1 writers show phrasal sophistication ahead of clausal complexity: dense noun phrases with fewer dependent clauses, producing compressed, information-dense style.
* Chinese-L1 writers show conjunction-free clause coordination (lower T/S): independent clauses joined by punctuation without conjunctions. This is a documented L1 structural transfer, not always a "comma splice."

MUST NOT "correct" operator toward NS subordination norms. If operator's natural pattern favors dense noun phrases and fewer subordinate clauses, treat this as a voice resource — a compressed, information-dense register — not as a deficiency requiring remediation.

SHOULD NOT prescribe this pattern for individual operators. Population-level finding; individual variation exists. If operator's natural pattern includes high subordination, do not force reduction.

Conjunction-free clause coordination can be deliberately deployed as asyndeton in English prose when the context supports compressed, paratactic style.

Source: Lu, X., & Ai, H. (2015). JSLW, 29, 16-27. \[esl_preserve\]

### Move: Lexicon Practice (Enrichment Drill)

Procedure:

1. Maintain a domain-specific word collection: one word per entry, include etymology and sound groupings.
2. For each major project, create a word trap: list 50-100 concrete, sensory-perceivable terms from the project's domain before drafting.
3. During revision, check whether the piece uses words from the trap or defaults to generic vocabulary.

This is a vocabulary-building drill, not a style prescription. The goal is to expand the operator's active vocabulary from sensory observation, not from frequency lists or "native-sounding" idiom guides.

Source: Long, Ch 2, Lexicon Practice + Word Trap. Effectiveness is anecdotal (instructor self-report; no controlled study). Adopt the procedure, not an efficacy claim. \[inferred:craft-transfer — Long does not discuss ESL or professional writing\]

### Kill List — Patterns to Reject

MUST NOT adopt as craft guidance:

* Locker's pronoun-you maximization as absolute rule. "Use you more often than I" oversimplifies. Over-use of "you" in positive contexts can read as aggressive in cross-cultural settings. Use strategically, not reflexively.
* Locker's specific memo/letter templates. Borrow structural logic; do not copy 2012 genre templates.
* Long's notebook romanticism (dawn, silence, cat, nightgown). Borrow the practice; reject the aesthetic framing.
* Long's handwriting-superiority claim. The underlying neuroscience (James & Engelhardt 2012) tested preliterate 5-year-olds, not adult writers. Adult studies show null results. Treat handwriting as personal preference.
* Any framing of indirect organization as a deficit or exception. Direct and indirect are co-equal strategies.
* Any recommendation to "sound more natural" — prescribe structural moves, not nativeness.

---

## Implementation Checklist

Composer 2.5 MUST verify each row before committing edits.

| Check | How to verify |
| --- | --- |
| Quotes are verbatim | Every quoted passage in the patches above appears exactly as written. Do not paraphrase, condense, or "improve" wording. |
| No 0628 re-litigation | No edit re-derives detection thresholds or classifier evaluations. Detection science inherits from /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md only. |
| ESL guards intact | Every \[esl_preserve\] tag is retained. No "sound more natural" language added. No "correct toward NS norms." |
| Tags preserved | Every \[inferred:detection-literature\], \[inferred:craft-transfer\], \[speculative:symptom-overlap\], and \[stale\] tag is retained exactly. Do not promote to \[verified\]. |
| Lane separation | deai_removal content goes in deai.skill files. tic_enrichment content goes in tic.skill files. Cross-references are inline notes, not section merges. |
| Kill-list items excluded | No WRONG/ZOMBIE/OVERSTATED claim from the kill lists appears as a supported assertion. |
| File paths exist | Verify every target path exists on disk before editing. If absent, create the file with a header first. |
| One patch per commit | Apply PATCH 1 (deai), commit. Then apply PATCH 2 (tic), commit. Do not batch across skill boundaries. |

---

## Provenance (for operator audit trail only — do not paste into skill files)

| Source | Tier | What survives | What was killed |
| --- | --- | --- | --- |
| Lu & Ai 2015 (JSLW) | 1 | Pooling-conceals-variation (LA-C001). Chinese phrasal > clausal pattern (LA-C003). Punctuation coordination (LA-C004). Non-deficit framing (LA-C010). | Detection-feature overlap with AI detectors (downgraded to \[speculative\] — deployed detectors use perplexity, not syntactic measures). |
| Liang et al. 2023 (Patterns) | 1 | 61.22% NNS false-positive rate. Perplexity mechanism. | Added in Pass 2 to replace the broken NLI-detection inference chain. |
| Locker 2012 (BAC 10e) | 1.5 | Subject-slot swap. Negative-context passive. Feeling-attribution deletion. Organization-resistance calibration. | Pronoun-you maximization as absolute rule. Anglo-American directness as professional default. All specific templates. |
| Long 2018 (Portable Mentor) | 3 | Concrete-over-abstract audit. Deliberate repetition. Before/after drill. Lexicon Practice procedure. | Handwriting superiority. Leonardo 9,000-word claim (ZOMBIE). Notebook romanticism. Lexicon effectiveness claim (UNTESTED). All RLHF mappings downgraded to \[speculative:symptom-overlap\]. |
| Ranade 2024 (AI and Society) | 2.5 | Prompt-formula residue vocabulary (7-element decomposition). Genre over-conformity. Audience echo-back. | All 7 empirical claims (WRONG or OVERSTATED). "Universal formula." "Indistinguishable." "Bias alleviation." Entire paper is \[stale\] for detection purposes. |

### Duplicate ingest resolution (operator action required)

* Two Locker ingests exist with overlapping content, different chapter numbering. Keep the ingest with absolute file paths (/Users/dubs/...). Deprecate the other.
* Two Long ingests exist covering the same slice. Keep the ingest with the explicit falsifying-tests-run table. Deprecate the other.

### Unread chapters (follow-up ingest priorities)

1. Long Part III, Chs 11-21 (sentence craft) — highest-value gap; blocks sentence-variety moves
2. Locker Ch 7 (Delivering Negative Messages) — buffer/reasons/refusal pattern; high priority for \[esl_preserve\]
3. Long Ch 24 (Revision) — transferable revision methodology
4. Locker Ch 5 (Planning, Composing, Revising) — revision checklist