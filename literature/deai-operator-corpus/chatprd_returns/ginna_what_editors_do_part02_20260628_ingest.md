# Scholia SF-12 Ingest: Ginna, What Editors Do — Part II — The Editing Process

## Meta

| Field | Value |
| --- | --- |
| slug | ginna_what_editors_do |
| chapter_id | part02 |
| chapters_attested | part02 only |
| source | Peter Ginna, ed., What Editors Do: The Art, Craft, and Business of Book Editing (U Chicago Press, 2017) |
| chapters covered | Ch. 5 (Miller), Ch. 6 (Lerner), Ch. 7 (Rabiner), Ch. 8 (Norton), Ch. 9 (Witte), Ch. 10 (Saller — opening only; truncated at chunk boundary) |
| lane | both (deai_removal + tic_enrichment) |
| operator | Wei Jia · L1 Chinese · ESL fairness mandatory |
| word count target | ≤4500w |
| revision | v2 — adversarial rewrite correcting v1 coverage and claim errors |

## Iron Law Requirements

* FR-3 enforced: all claims sourced to attached Part II text only.
* Gate A: all Q-bank quotes verified verbatim against indexed chunks of attachment.
* Evidence tags: \[from-text\], \[inferred\], \[speculative\] used throughout.
* Calibration gate applied where confidence ≥80.
* No open-web research performed (closed-corpus run).

## v1 Kill List (Adversarial Review Findings)

| ID | Claim | Verdict | Explanation |
| --- | --- | --- | --- |
| C-001 | Ch. 8 (Norton) truncated at "Deploying External Reviews" | WRONG | Full chapter indexed across chunks 6-8. Sections on Conducting Market Research, Revising the Proposal, Finding the Author's Voice, Working with a Team all present. The inline attachment was truncated at 80k chars in the prompt display, but the file index contains the full content. v1 fabricated a coverage gap. |
| C-002 | Part II contains four chapters by four essayists | WRONG | Part II contains six chapters: Miller, Lerner, Rabiner, Norton, Witte, Saller. Witte (Ch. 9, line editing) and Saller (Ch. 10, copyediting) were entirely omitted from v1. Witte's essay contains the most operationally relevant content for deai_removal. |
| C-003 | "Chronology is not narrative" presented as a named diagnostic test | OVERSTATED | Rabiner uses this as a section heading introducing her argument about tables of contents. It functions as a framing assertion, not a formalized test. The transferable insight is real but the ingest elevated it beyond its textual role. Survives with weaker scope. |
| C-008 | Confidence 85 for pipeline stages "confirmed across all four essayists" | OVERSTATED | Miller alone describes the full pipeline. Other essayists discuss fragments. Convergence was asserted, not demonstrated. Downgraded to 75. |

---

## Source Discovery

Single primary source: Part II of Ginna (2017). Six essayists; six distinct vantage points.

| Essay | Author | Vantage | Key domain |
| --- | --- | --- | --- |
| Ch. 5 — "The Book's Journey" | Nancy S. Miller | Acquiring editor (trade) | Full production pipeline, dev + line editing, transmittal, schedule |
| Ch. 6 — "What Love's Got to Do with It" | Betsy Lerner | Editor turned agent turned author | Author-editor emotional dynamics, power asymmetry |
| Ch. 7 — "The Other Side of the Desk" | Susan Rabiner | Editor turned agent (nonfiction) | Conceptualization, filler, genre, table of contents |
| Ch. 8 — "Open-Heart Surgery" | Scott Norton | Developmental editor (academic/trade) | Coaching vs. modeling, external reviews, market research, voice, team work |
| Ch. 9 — "This Needs Just a Little Work" | George Witte | Line editor (trade, fiction + nonfiction) | Micro/mid-micro/macro editing taxonomy, word-level precision, sentence rhythm, transitions, war stories |
| Ch. 10 — "Toward Accuracy, Clarity, and Consistency" | Carol Fisher Saller | Copyeditor | Copyediting scope and distinction from line editing (opening only; file truncated mid-chapter) |

Tier: 1.5 (practitioner anthology from a university press; named industry professionals, not peer-reviewed). All claims are experiential/craft-based. No quantitative data; no sample sizes. \[from-text\]

---

## Confidence Scoring

| Claim cluster | Conf | Justification |
| --- | --- | --- |
| Editing pipeline stages (dev → line → copyedit → proofs) | 75 | \[c1=80, c2=70, c3=75\] Miller describes the pipeline in full. Other essayists confirm fragments. No external validation cited. FINAL=75. |
| Conceptualization as gating function (Rabiner) | 70 | \[c1=75, c2=60, c3=70\] Practitioner insight, nonfiction-specific. Rabiner's own category; no replication. FINAL=70. |
| Empathy as core editorial competency (Giroux via Miller; Lerner) | 65 | \[c1=70, c2=55, c3=65\] \[CONFIDENCE DISPUTED — c2 relies on same Giroux 1982 talk as c1; cap applied.\] FINAL=65. |
| Filler detection as editorial skill (Rabiner) | 70 | \[c1=75, c2=60, c3=70\] Practitioner insight only; no external validation. FINAL=70. |
| Coaching vs. modeling dyad (Norton) | 65 | \[c1=70, c2=55, c3=65\] Single source (four UC Press colleagues). Descriptive, not tested. FINAL=65. |
| Word-level overuse detection (Witte) | 75 | \[c1=80, c2=70, c3=75\] Witte provides concrete examples verified by 30-year editing practice. Converges with known RLHF filler-word lists \[inferred\]. FINAL=75. |
| Sentence-rhythm variation as editing scope (Witte) | 65 | \[c1=70, c2=55, c3=65\] Single practitioner; grounded in poetic craft background. FINAL=65. |

---

## Gate A — Verbatim Q-Bank

All quotes verified against indexed attachment chunks.

Q-001 Source: Miller, Ch. 5 (§ Developmental Editing) Quote: "There are three qualities that cannot be taught and without which a good editor cannot function—judgment, taste, and empathy." Attribution: Robert Giroux, 1982 talk, cited by Miller. \[verified in chunk 0\]

Q-002 Source: Rabiner, Ch. 7 Quote: "What is the story you want to tell?" Context: Basic question Rabiner found essential as agent. \[verified in chunk 4\]

Q-003 Source: Rabiner, Ch. 7 Quote: "I get why you want to write this book. Tell me why I want to read it." Context: Reframing toward reader-facing conceptualization. \[verified in chunk 4\]

Q-004 Source: Rabiner, Ch. 7 Quote: "'good writing' means compelling ideas clothed in words" Context: Content drives acquisitions more than prose fluency. \[verified in chunk 5\]

Q-005 Source: Lerner, Ch. 6 Quote: "a good editor asks the right questions, makes you better than you are, or more willing to stretch even when you resist" Context: Lerner on her third editor's method. \[verified in prompt inline text\]

Q-006 Source: Norton, Ch. 8 Quote: "significant structuring or restructuring of a manuscript's discourse" Context: Norton's definition of developmental editing. \[verified in chunk 5\]

Q-007 Source: Miller, Ch. 5 (§ Line Editing) Quote: "The editor must always respect the author's voice when making line-editing suggestions that pertain to style." Context: Constraint on line-editing scope. \[verified in chunk 0\]

Q-008 Source: Rabiner, Ch. 7 Quote: "Chronology is not narrative." Context: Section heading introducing Rabiner's argument about tables of contents. \[verified in chunk 5\]

Q-009 Source: Witte, Ch. 9 (§ Micro) Quote: "very, vague or vaguely, really, generally, mostly, nearly, pretty, pretty much, beautiful, ugly, and other words that do no work" Context: Witte's list of words to cut at the micro level. \[verified in chunk 8\]

Q-010 Source: Witte, Ch. 9 Quote: "The editor should not impose a voice, a vision, a point of view, an agenda, or a too-aggressive critical approach that leaves no room for praise and disables the author's confidence and creativity." Context: Witte's constraint on line-editing posture. \[verified in chunk 8\]

Q-011 Source: Witte, Ch. 9 (§ Mid-Micro) Quote: "Prose writers, especially young ones, often fall into habitual sentence structures that can have a cumulatively soporific effect." Context: Sentence-rhythm variation as editing target. \[verified in chunk 8\]

---

## Core Concepts Extracted

### 1\. The editing pipeline as staged transformation

Miller maps: developmental editing → line editing → editorial letter exchange → transmittal manuscript → copyediting → setting copy → page proofs → press/e-book. Each stage has distinct scope. \[from-text\]

Lane: \[both\] — stage boundaries matter for distinguishing structural de-AI (dev-edit scope) from sentence-level de-AI (line-edit scope).

Miller herself notes these stages "often overlap" in practice. The pipeline is a conceptual ordering, not a strict workflow. \[from-text\]

### 2\. Developmental editing as "bones" work

Miller: the editor "tackles such big-picture matters as structure, focus, pacing, plotting, shaping an argument, gaps in the narrative." Norton operationalizes this as "significant structuring or restructuring of a manuscript's discourse." \[from-text\]

Lane: \[both\] — de-AI revision that reorganizes paragraph order, cuts hedging preambles, or restructures argument flow operates at dev-edit scope. \[inferred\]

### 3\. Line editing as voice-respecting sentence work

Miller's checklist: word choice, syntax, phrasing, transitions, chronology checks, dialogue truth-testing. Bounded by the constraint that "the editor must always respect the author's voice." \[from-text\]

Witte expands this with operational specificity Miller lacks (see Concept 11).

Lane: \[deai_removal\] + \[esl_preserve\] — do not flatten L1-influenced syntax that is not itself RLHF-generated.

### 4\. Conceptualization as gating function (Rabiner)

Central claim: publishability turns on conceptualization — "the value added by the author to what is essentially a set of facts, stories, and commentary in search of a larger meaning." \[from-text\]

Transfer to de-AI: RLHF-trained models produce text missing conceptualization by definition — they generate plausible prose without authorial intent. But the diagnostic ("Why do you want to write this book?") targets a human author's intentionality. It does not apply to AI output, which has no intent. The concept transfers as a test for whether human-authored text survived AI revision with its conceptual core intact. \[inferred\]

### 5\. Filler: the anti-pattern (Rabiner)

Rabiner: filler is "proposal material that is very nicely written but devoid of real content. It's there because the author is trying to write his way out of the fact that he doesn't yet know what he wants to say." \[from-text\]

Lane: \[deai_removal\] — RLHF prose produces surface-similar filler (fluent, content-light). The etiology differs: human filler arises from authorial uncertainty; RLHF filler arises from helpfulness optimization. The symptom presentation overlaps; the cure does not. Human filler: force thinking. RLHF filler: delete and replace. \[inferred\]

### 6\. Chronology-is-not-narrative (Rabiner)

Rabiner: sequential ordering does not create story. "The reader needs to gain a sense of momentum, almost of inevitability, as the book moves toward a conclusion." \[from-text\]

This is a framing assertion introducing her argument about tables of contents, not a named diagnostic test. Useful as a heuristic but should not be treated as a formalized protocol. \[from-text, scope corrected from v1\]

Lane: \[both\] — diagnoses RLHF outputs that present information sequentially without building momentum.

### 7\. Genre as subconscious editorial filter (Rabiner)

Editors subconsciously evaluate whether "the author truly understands what readers who read this type of book want" and "how they want their stories told." Mismatch produces "systemic problems" that "can't be resolved through editing." \[from-text\]

Lane: \[tic_enrichment\] — voice priming must respect genre expectations.

### 8\. Coaching vs. modeling (Norton)

Coaching: summary feedback without working solutions in text. Modeling: editor rewrites sample passages. Roessner "plays ghostwriter in Track Changes" for a few sentences, then says "Please do more of this." \[from-text\]

Norton's full chapter (now confirmed present) adds substantial operational detail: "Revising the Proposal" section describes thesis development; "Finding the Author's Voice" describes synthesis calibration; "Working with a Team" describes outsourcing to freelance DEs. \[from-text\]

Lane: \[tic_enrichment\] — craft-move banks need both coaching (describe move) and modeling (show move in situ).

### 9\. Witte's micro/mid-micro/macro editing taxonomy (NEW — omitted from v1)

Witte provides the most operationally specific editing framework in Part II:

* Micro (diction): identify overused words, imprecise adjectives, cliches. His filler-word list (Q-009) directly overlaps known RLHF padding markers.
* Mid-micro (sentences): vary sentence length and structure. "Habitual sentence structures that can have a cumulatively soporific effect." Diagnoses RLHF's tendency toward uniform sentence cadence.
* Macro (structure): beginnings/endings of books and chapters; transitions; paragraph-level purpose test ("What did this paragraph just do? Did it do anything?").

Lane: \[deai_removal\] — Witte's micro level is the most directly applicable content in Part II. His word list is a ready-made detection lexicon for RLHF residue. His paragraph purpose test ("Did it do anything?") operationalizes Rabiner's filler concept at paragraph granularity.

### 10\. The paragraph purpose test (Witte)

"When editing, if I find myself bored or confused, I pause to ask myself: What did this paragraph just do? Did it do anything? If not, why not?" \[from-text\]

This is more operationally useful than Rabiner's filler concept because it works at paragraph level (actionable) rather than proposal level (diagnostic). \[inferred\]

Lane: \[deai_removal\] — apply during line-edit-scope de-AI passes.

### 11\. Voice imposition as editorial failure (Witte)

"The editor should not impose a voice, a vision, a point of view, an agenda, or a too-aggressive critical approach that leaves no room for praise and disables the author's confidence and creativity." \[from-text\]

Converges with Miller's Q-007 but adds specificity: the failure mode is not just "disrespecting voice" but actively imposing the editor's voice. \[from-text\]

Lane: \[esl_preserve\] + \[deai_removal\] — de-AI passes that replace RLHF prose with the reviser's preferred idiom commit this error. The goal is to reveal the author's voice underneath, not substitute a new one.

### 12\. Transitions as momentum architecture (Witte)

"If a chapter begins on an irresolute note—with no connection to the previous chapter's end and no sense of dramatic promise—then the line editor might suggest adding a sentence (or two) that establishes direction." Witte's cop-scene example concretizes: cut stage business between dramatic beats; "We don't need to see routine to-and-fro taking up space and sapping momentum." \[from-text\]

Lane: \[both\] — RLHF models generate false transitions ("Let's dive in," "Now let's explore") that mimic momentum without creating it. Witte's framework identifies what real transitions do: connect the previous section's end to the next section's promise.

---

## Skill Incorporation Table

| \# | Skill / Move | Source | Action | Lane | Rationale |
| --- | --- | --- | --- | --- | --- |
| 1 | Filler detection heuristic | Rabiner Ch. 7 | KEEP | deai_removal | "Can you articulate what the author wants to say?" test identifies RLHF padding. Already implicit; now named. |
| 2 | Conceptualization-before-prose ordering | Rabiner Ch. 7 | ADD | both | Does the passage have a point, or is it writing-in-search-of-a-point? Pre-check before line editing. |
| 3 | Voice-respect constraint at line-edit scope | Miller Ch. 5, Witte Ch. 9 | KEEP | deai_removal + esl_preserve | Miller's formulation + Witte's anti-imposition constraint reinforce: line edits that flatten voice violate the constraint. |
| 4 | Stage-scope discipline (dev vs. line vs. copy) | Miller Ch. 5 | ADD | both | Label each de-AI pass by editing scope. Prevents scope creep. |
| 5 | Coaching/modeling dual deployment | Norton Ch. 8 | CHANGE | tic_enrichment | Craft-move banks currently coaching-only. Add modeling examples (before/after rewrites) to each move entry. |
| 6 | Genre-fit filter for voice priming | Rabiner Ch. 7 | ADD | tic_enrichment | Before borrowing structural moves, verify genre compatibility. Mismatch = systemic problems. |
| 7 | Witte's filler-word detection list | Witte Ch. 9 (§Micro) | ADD | deai_removal | "very, vague or vaguely, really, generally, mostly, nearly, pretty, pretty much" — ready-made lexicon for RLHF residue detection. Cross-reference with existing de-AI signal lists. |
| 8 | Paragraph purpose test | Witte Ch. 9 (§Macro) | ADD | deai_removal | "What did this paragraph just do? Did it do anything?" — paragraph-level operationalization of filler detection. Apply during line-edit-scope passes. |
| 9 | Sentence-rhythm variation check | Witte Ch. 9 (§Mid-Micro) | ADD | both | Diagnose uniform sentence cadence (RLHF signature). Vary length and structure to break soporific monotony. |
| 10 | Transition architecture (not false transitions) | Witte Ch. 9 | ADD | both | Cut stage business; connect previous ending to next promise. Distinguish from RLHF false transitions ("Let's explore"). |
| 11 | Editorial letter structure (praise → dev → line) | Miller Ch. 5, Lerner Ch. 6 | KEEP | both | Confirms existing practice. |

---

## Adversarial Self-Review (Integrated)

### Three strongest objections a hostile domain expert would raise

Objection 1: The filler analogy is a false equivalence. Rabiner describes filler produced by humans who don't know what to say. RLHF filler is produced by models optimizing for perceived helpfulness. The surface presentation overlaps (fluent, content-light); the causal mechanism does not. Therefore the detection heuristic may transfer but the explanatory framework is misleading.

Assessment: This objection succeeds. The document now marks the etiological distinction explicitly in Concept 5 and does not claim causal equivalence.

Objection 2: All six essayists describe human-to-human editing. Mapping their lessons to human-AI revision is analogical, not empirical. No essayist anticipated or discussed AI-generated text. Transfer is this ingest's construction, not the source's claim.

Assessment: This objection succeeds. Every \[inferred\] tag in the transfer claims acknowledges this. The document does not attribute AI-applicability to the essayists.

Objection 3: Survivorship bias. All six essayists are successful, established professionals. Their practices may not represent what most editors do, only what worked for these particular practitioners under their particular conditions.

Assessment: This objection succeeds but has limited operational impact. The ingest borrows structural moves (editing taxonomies, detection heuristics), not success recipes. Survivorship bias matters more for claims like "empathy is the most crucial quality" (which depends on whether empathetic editors differentially succeed) than for taxonomic categories (which are descriptive).

### Overconfidence check

v1 had 2 of 5 scores at 80+. After correction, 0 of 7 scores exceed 80. No downward-pressure pass needed.

### What could not be verified

* Whether Witte's filler-word list actually overlaps with empirically validated RLHF marker lists. Stated as \[inferred\] from known de-AI practice, not verified against a specific published list.
* Saller's full chapter (Ch. 10) — only the opening section is in the indexed file. Unknown whether remaining content contains transferable craft moves.
* The Giroux 1982 talk is cited by Miller with a footnote marker but no full citation is available in the text export. Cannot verify the quote against the primary speech. \[from-text, secondary citation only\]
* No chapter in Part II discusses editing in languages other than English. Applicability to L1-Chinese ESL contexts is assumed via the \[esl_preserve\] framework, not demonstrated by the source.

---

## Coverage Attestation

chapters_attested: part02 only

Chapters read: Ch. 5 (Miller, complete), Ch. 6 (Lerner, complete), Ch. 7 (Rabiner, complete), Ch. 8 (Norton, complete — v1 error corrected), Ch. 9 (Witte, complete), Ch. 10 (Saller, opening section only — file truncated at chunk boundary).

Chapters NOT read: Parts I, III, IV, and any chapters outside Part II. No claims from unread material.