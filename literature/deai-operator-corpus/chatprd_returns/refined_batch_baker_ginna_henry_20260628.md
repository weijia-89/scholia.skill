# Composer Brief — baker_ginna_henry_corpus

Status: READY FOR IMPLEMENTATION Canon: Inherit only from /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md Sources: Baker 2020 Ch 1, Ginna 2017 (full), Henry 2000 (partial)

## STOP conditions — halt and flag for operator if ANY is true

* File does not exist at the specified path
* A patch block would overwrite or delete existing content (these are APPEND operations)
* You are tempted to rephrase, summarize, or "improve" a patch block
* You encounter a conflict with the decision canon
* You want to remove an \[esl_preserve\] or \[inferred:operator_synthesis\] tag

## How to use this document

Each patch below is a fenced text block. Your job:

1. Open the target file
2. Find the appropriate section (noted in each patch header)
3. Append the patch block at the end of that section
4. Do not edit the patch text
5. Commit after each patch — one patch per commit

Do not batch patches. Do not reorder content within patches. Do not add commentary.

---

## PATCH SET A — tic.skill (5 patches)

Target file: /Users/dubs/.cursor/skills/tic/SKILL.md

### Patch A1: Register calibration pre-write check

Append to the section that governs pre-writing or drafting setup. If no such section exists, append to the end of the file.

```
### Register Calibration (Baker 2020 Ch 1)

Before drafting, name three variables:
- PURPOSE: what outcome does this text need to produce?
- AUDIENCE: who reads this, what do they already know, what register do they expect?
- CONTEXT: what channel, what constraints, what organizational norms apply?

Name the target register explicitly ("formal technical report," "casual internal update," "stakeholder-facing narrative") before writing the first sentence.

This prevents two failure modes:
- Under-formality: register too casual for the audience or stakes
- RLHF over-formality: register locked into hedged, impersonal, exhaustively qualified prose because the model defaults to "safe" tone

\[esl_preserve\] Calibrate register to the task, not to an assumed native-speaker norm. The writer adapts structure, not identity. A pre-write check that names the register target does not require performing a native register — it requires knowing what structural choices serve the purpose.

```

### Patch A2: Meaning is constructed, not transmitted

Append to the section that governs voice craft or writing principles.

```
### Meaning Is Constructed (Baker 2020 Ch 1 p. 16)

"Meaning exists in the human mind, not in words themselves."

The writer's job is not to encode meaning in word-choice and transmit it. The writer constructs conditions under which the reader builds meaning. Structure, rhythm, information placement, and pacing carry meaning independent of lexical content.

Craft implication: sentence architecture IS content, not decoration on top of content.

Compression corollary: "People manufacture information to fill in missing information" (Baker p. 16). Deliberate omission activates reader participation. Over-specification — hedging, throat-clearing, restating the same point in three ways — prevents the reader from constructing meaning. This is the primary RLHF failure mode in prose.

Guardrail: compression must be deliberate. The writer must know what is omitted and why. This principle does not justify vagueness or laziness — it justifies trusting the reader.

\[esl_preserve\] L1-influenced syntax that successfully triggers meaning-construction is a valid meaning-making path, not a defect. L1-influenced elision or compression may activate productive reader gap-filling rather than constituting "unclear" writing.

```

### Patch A3: Conflict-type triage for revision

Append to the section that governs revision or feedback handling.

```
### Conflict-Type Triage for Revision Feedback (Jehn 1997 via Baker 2020)

When receiving edit feedback, classify before responding:

- CONTENT conflict: "The argument in section 3 is wrong" — disagreement about substance. This is productive. Engage on the merits.
- PROCEDURE conflict: "You should have sent this for review before the client call" — disagreement about process. Negotiate the process separately from the content.
- RELATIONSHIP conflict: "I don't trust your judgment on this" — interpersonal friction. Do not let this contaminate your response to content feedback. Address it separately or escalate.

Classify first. Then respond to content feedback on content terms regardless of the interpersonal dynamic.

Failure mode: dismissing legitimate content feedback as relationship conflict. The taxonomy prevents ego-fusion during revision; it does not license ignoring substance.

```

### Patch A4: Authority as depth, not fluency

Append to voice-craft principles or quality self-diagnostics.

```
### Authority Markers (Karp in Ginna 2017 Ch 2)

Voice quality emerges from subject-matter command. Karp's markers of authority in writing:
- The voice is more assured
- The details are precise
- The momentum builds
- There is meaning between the lines
- Often there is wit, because the writer knows the material well enough to relax

Use as a self-diagnostic after drafting: does this text demonstrate command of its subject, or does it perform competence through hedging and exhaustive qualification?

\[esl_preserve\] \[inferred:operator_synthesis\] Authority markers are knowledge-depth signals, not native-register markers. An ESL writer demonstrating subject authority through precise detail meets this standard regardless of L1 syntax influence. Karp does not address ESL contexts; this application is operator inference.

```

### Patch A5: Voice is structural, not surface

Append to voice-craft principles or revision process.

```
### Voice Is Structural (Norton in Ginna 2017 Ch 8)

"An author's writing style, or voice, can be bound up in her manuscript's structural flaws."

When voice feels wrong, check structure first:
- Is the thesis clear?
- Is the argument synthesized or just listed?
- Are the key claims foregrounded or buried?
- Does the information architecture serve the reader's path through the text?

Restructuring (thesis, synthesis, foregrounding) often resolves apparent voice problems without touching sentence-level style. Development means "pushing toward describing the gist."

Guardrail: some voice problems ARE sentence-level. This principle says check structure first, not never touch sentences.

\[esl_preserve\] \[inferred:operator_synthesis\] For ESL writers, apparent "voice problems" flagged by editors may be structural (unclear thesis, insufficient synthesis) rather than sentence-level. Developmental editing that addresses structure can resolve these without touching L1-influenced syntax. Norton does not address ESL contexts; this application is operator inference.

```

---

## PATCH SET B — deai.skill (6 patches)

Target file: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md

### Patch B1: Intent-alignment editing

Append to the section on editorial theory or craft principles.

```
### Intent-Alignment Editing (Ginna 2017 Introduction)

Editing is "working through \[the book\] with close attention both to what is on the page and to the author's vision, and bringing them back together when they diverge."

The divergence target is the author's intent, not a market-median surface. An edit that makes text sound "more professional" or "smoother" while moving it away from the author's vision fails this test.

Diagnostic: before making a style edit, ask — does this change bring the text closer to what the author is trying to accomplish, or does it bring the text closer to how I think it should sound?

\[esl_preserve\] \[inferred:operator_synthesis\] An edit that removes idiosyncratic phrasing fails the intent-alignment test if the original phrasing carried author meaning. Ginna does not address ESL contexts; this protective reading is operator inference.

```

### Patch B2: Voice-imposition prohibition

```
### Voice-Imposition Prohibition (Witte in Ginna 2017 Ch 9)

"The editor should not impose a voice, a vision, a point of view, an agenda, or a too-aggressive critical approach that leaves no room for praise and disables the author's confidence and creativity."

"The line editor needs to learn what different authors need and will tolerate, rather than imposing a standard of editing that might damage the relationship with the author or even harm the author's ability to write. It's the author's book, not the editor's."

Precedent — the dialect anecdote: a southern novelist refused to lighten her characters' dialect "because then she couldn't hear them in her head." The novel succeeded as published. The editor was wrong to push for change.

Boundary: Witte also describes converting "hundreds of passive verb constructions to active forms." Clarity edits are legitimate. The prohibition is against imposing voice, not against all editorial intervention.

\[esl_preserve\] \[inferred:operator_synthesis\] Dialect preservation as voice integrity is a direct parallel to L1-influenced syntax preservation. Witte does not address ESL contexts; the parallel is operator inference.

ANTI-MODEL: Gordon Lish (discussed by Witte) practiced voice-replacing editing. This is the failure mode this prohibition exists to prevent.

```

### Patch B3: Copyedit scope boundary

```
### Copyedit Scope Boundary (Saller in Ginna 2017 Ch 10)

"The opportunity to improve someone else's prose is not an invitation to make it one's own. Copyediting means stifling one's own voice in favor of the writer's and honoring the type and purpose of the document."

Saller's five copyediting categories: spelling/grammar/style, accuracy, structure, logic, elegance. Elegance (voice, rhythm, tone monitoring) is the highest level — "a level that many projects don't allow time and money for."

Scope boundary: elegance-level monitoring is opt-in, not default. If a text needs rewriting, the copyeditor escalates to the author or assigning editor rather than exceeding the copyedit mandate.

\[esl_preserve\] \[inferred:operator_synthesis\] A copyeditor who "corrects" L1-influenced syntax to match a native register is exceeding scope unless specifically authorized to edit at the elegance level. Saller does not address ESL contexts; this application is operator inference.

```

### Patch B4: Do-no-harm principle

```
### Do-No-Harm Principle (Ferber in Ginna 2017 Ch 19)

"First, do no harm. ... it seems to me the first and foremost responsibility of an editor is to not inflict damage while improving the health of a body of scholarly writing. ... Overly simplifying, or 'dumbing down,' the author's text may ultimately result in alienating its core audience without realistically replacing it with a wider one."

Simplification is editorial harm when it destroys the text's fit with its actual audience. The "harm" threshold is about audience-fit destruction, not about all simplification.

Guardrail: this principle does not apply when genuine comprehension failure occurs. If a reader cannot parse the sentence, the edit is warranted.

\[esl_preserve\] \[inferred:operator_synthesis\] For ESL academic writers, simplifying L1-influenced academic prose to match trade-book register can alienate the author's specialist audience. Ferber does not address ESL contexts; this parallel is operator inference.

```

### Patch B5: Communicative packaging diagnostic

```
### Communicative Packaging Diagnostic (Henry 2000, via Crowley 1998)

"Pernicious was the reduction of writing to something akin to communicative packaging, as most students learned it and as most workers exercised it."

Communicative packaging = formally correct text with no rhetorical position. The text displays competence rather than commanding assent or rejection. It is content poured into a formal container: correct grammar, hedged claims, topic-sentence-then-support structure, no first person, no situated voice.

Use as a detection diagnostic: if a draft reads as communicative packaging, it likely exhibits RLHF residue or corporate-tone flattening.

\[inferred:craft-transfer\] Henry wrote in 2000, pre-AI. His critique of current-traditional rhetoric (Crowley's "theory of graphic display") maps structurally onto RLHF-optimized output: both optimize for surface compliance at the expense of genuine rhetorical position. The analogy is structural, not causal.

Scope: this diagnostic applies to knowledge-work writing. Boilerplate, compliance documentation, and standardized operational communication may legitimately use Taylorized prose.

\[esl_preserve\] ESL writers who prioritize meaning density over surface polish are resisting communicative packaging. Surface correctness is not the goal of good writing.

```

### Patch B6: Implied-author specificity test

```
### Implied-Author Specificity Test (Henry 2000, via Prince 1987 / Booth 1961)

Every text constructs an "implicit image of an author ... responsible for its design and for the values and cultural norms it adheres to."

Revision diagnostic: after drafting, ask — if the byline were removed, could a reader who knows the author identify them from the text alone? If the implied author is indistinguishable from any other text in the genre, the voice is under-specified.

AI-generated text typically constructs an implied author who is: unfailingly polite, comprehensive but shallow, structurally predictable. These are testable markers of voice vacancy.

Prior applications: the implied-author concept has been applied to workplace and technical writing since 1982 (ERIC ED228641; Jameson 2004 in JBCA).

\[esl_preserve\] An L1-influenced implied author is a specific implied author. Specificity is the goal.

```

---

## Implementation sequence

Execute in this order. One commit per patch.

1. Patch A1 (register calibration)
2. Patch A2 (meaning is constructed)
3. Patch A3 (conflict triage)
4. Patch A4 (authority as depth)
5. Patch A5 (voice is structural)
6. Patch B1 (intent-alignment)
7. Patch B2 (voice-imposition prohibition)
8. Patch B3 (copyedit scope)
9. Patch B4 (do-no-harm)
10. Patch B5 (communicative packaging)
11. Patch B6 (implied-author test)

## After implementation

* Run `refresh_attach_packs.sh`
* Update manifest.yaml: `ingest_status: implemented` for baker_ginna_henry_corpus
* Do not modify the decision canon
* Do not re-read the v1 ingest files (Baker v1, Ginna v1, Henry v1) — v2 governs for all three sources