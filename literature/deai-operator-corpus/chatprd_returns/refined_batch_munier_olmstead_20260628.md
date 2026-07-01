# Composer Implementor Brief — munier_2016 + olmstead_1997

Save to: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/munier_olmstead_refined_20250627.md

Sources: Munier 2016, The Writer's Guide to Beginnings (Tier 3 practitioner, agent perspective, Chs 1-2 only). Olmstead 1997, Elements of the Writing Craft (Tier 3 practitioner, MFA pedagogy, full text). Neither source is empirical. No claim from either source may be tagged \[verified\] in skill files. All deai mappings are analyst inference — both authors predate AI writing.

Detection canon: Inherit only /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md. Do not re-litigate detection science.

## 1) Decision summary

* Munier's "nothing happens" bad-opening taxonomy and seven-reader-question diagnostic: ADD to both skills as practitioner diagnostics. Tag \[inferred:structural-convergence\]. These map structurally to RLHF expository defaults but Munier makes no AI connection.
* Olmstead's sentence-level craft moves: ADD six candidate deai moves and seven tic_enrichment moves. All deai mappings are \[inferred:deai-theory\] — none tested against model output.
* RLHF syntactic evidence is conflicted: Varga 2025 (scientific text, N=24) finds AI produces flatter syntax; Fredrick and Craven 2025 (essays, N=100) finds AI produces MORE subordination. Any edit referencing AI syntax must note this conflict.
* All \[esl_preserve\] tags are \[inferred:operator-context\]. Neither source discusses ESL. Preserve as operator constraints, not empirical claims.

## 2) Verbatim Q-bank

Do not paraphrase. Copy exactly. These are the anchors that prevent semantic drift.

### Munier 2016

| ID | Quote | Source |
| --- | --- | --- |
| MQ-001 | "Too many writers open with backstory or description or inner monologue—which means that nothing is happening. The opening falls flat on its face, felled by its own static weight." | Ch2 |
| MQ-002 | "Dramatization is the key. Drama is the stuff of storytelling—and it's what separates the boring beginnings from the compelling beginnings." | Ch2 |
| MQ-003 | "The most efficient and effective way to begin a story is with a scene." | Ch2 |
| MQ-004 | "Narrative thrust is the tight construction of story, line by line, beat by beat, event by event, pushing the action forward—and the reader with it." | Ch1 |
| MQ-005 | "No narrative thrust equals no sale." | Ch1 |
| MQ-006 | "If I can't say what a story is about in 50 words or less, I can't sell it." | Ch1 |
| MQ-010 | "Something happens to someone, and that someone reacts. Then the reader reacts and keeps on reading. This is the engine of story." | Ch2 |
| MQ-011 | "One of the most common complaints I hear from editors when they pass on projects is this: 'I just didn't fall in love with the protagonist.'" | Ch1 |
| MQ-015 | "For every two-hundred queries you receive, you'll only find one or two story openings compelling enough to prompt you to request the rest of the manuscript." | Ch2 (Panettieri) |

### Olmstead 1997

| ID | Quote | Source |
| --- | --- | --- |
| OQ-002 | "To learn to write you must master the small aspects of the craft, and to master them you must learn to read like a writer." | Introduction |
| OQ-006 | "That the car is stolen is made to be much less important than that they are fighting. ... Simply put, this information is revealed in an adjective, not in a statement of fact, as the fighting is." | Opening in Crisis (Simpson) |
| OQ-007 | "The horrifying event is made more so by the contrasting details: The bear nudged, the feathery down floated, and the coals from the fire were glowing." | Opening After a Death (Kittredge) |
| OQ-008 | "His repetition of words is like the cupping of photographs in his hands. He is seeing with his eyes closed, conjuring up the past." | Memory (Baldwin) |
| OQ-009 | "Milly does not act out her feelings. She simply nods and the reading of that nod is placed inside Jane's head." | Perceiving (Bausch) |
| OQ-010 | "The telling is straight subject-verb. In the face of this most extraordinary event, the writer has removed herself as much as possible, letting the facts speak for themselves." | High Drama in Nonfiction (Prejean) |
| OQ-016 | "she does not say how she felt, but how she didn't feel: I was not shocked ... I was not pleased. ... This is another way of being specific." | Setting by What You See (Williams) |
| OQ-017 | "When you think of voice, think of participating in what has come before, while at the same time contributing what is of your own making." | Voice (O'Brien/Hemingway) |
| OQ-018 | "His repetition of the word small is more akin to an oral tradition than to a literary one. In rewrite, one might avoid the repetition of an adjective. But to maintain the voice of a storyteller, Anderson does not make such a literary choice." | Voice of the Conjurer (Anderson) |
| OQ-019 | "O'Connor links related images, going from gold to diamond to ring to wheel. These images connect the sentence, and they add a metallic shimmer to the scene as a whole." | Language of Event (O'Connor) |
| OQ-020 | "Steinbeck does not narrate their approach, but allows them to gain ground at the edges of the scene while recounting the action of Lennie and George." | Third Person Dramatic (Steinbeck) |

## 3) Craft moves — Lane A: deai_removal

Each move: what AI does wrong, what to do instead, when it fails.

| ID | AI default (anti-pattern) | Craft intervention | When it fails | esl_preserve |
| --- | --- | --- | --- | --- |
| DEAI-01 | Opening with backstory, definition, or inner monologue — nothing happens. Example: "In today's rapidly evolving landscape..." | Test: does the opening paragraph contain an EVENT where someone acts and reacts? If no, rewrite to start with a scene. \[inferred:structural-convergence\] Anchor: MQ-001, MQ-010 | Rebecca opens with inner monologue. Some legitimate openings defer action. Scope to persuasive/narrative text only — technical docs may require definitional openings. | N/A |
| DEAI-02 | Opening answers zero of Munier's seven reader questions: (1) genre signal, (2) premise in 50 words, (3) POV clarity, (4) protagonist ID, (5) setting, (6) emotional contract, (7) narrative thrust | Quick-screen: count how many questions the opening answers. Zero = RLHF candidate. \[inferred\] Anchor: MUN-C001 | Literary openings may deliberately defer answers. Heuristic, not definitive. | Yes — tests clarity of contract, not native fluency |
| DEAI-03 | Important facts stated in topic-sentence position. All information given equal prominence. | Bury secondary-but-important facts as adjectives inside prepositional phrases. Reserve subject-verb position for primary content. \[speculative — no study tests AI sentence-level placement\] Anchor: OQ-006 | "Topic-sentence-first" as AI default is unverified. PMC salience study found LLMs have hierarchical salience in summarization but does not address sentence-level placement. | Yes — do not correct L1 Chinese topic-comment structures |
| DEAI-04 | Uniform medium-length sentences. Low sentence-length variance. (Xu and Zubiaga 2025: RLHF produces longer, less syntactically diverse output.) | Inject 2-5 word subject-verb sentences at rhythmic stress points within longer syntax. Signal is in the VARIATION pattern, not short sentences alone. \[inferred:deai-theory, conflicted evidence\] Anchor: OQ-010, OQ-012 | Varga 2025: baseline ChatGPT ALSO produces flat syntax in scientific text. Short declaratives alone are ambiguous. Must combine with irregular length variation across paragraph. | Yes — validates L2 short-sentence patterns as craft |
| DEAI-05 | AI narrates every transition and process. No white space. Completionist tendency. | Cut passages where events should happen offstage. Let major transitions occur in white space. \[inferred:deai-theory\] Anchor: OQ-020 | Untested whether AI strategically omits narration. Scope: narrative/creative text only. | Neutral |
| DEAI-06 | AI states what IS. Defaults to positive assertion ("she felt calm"). | Substitute negation-as-precision: "I was not shocked ... I was not pleased." Defining by elimination is more specific than direct statement. \[inferred:deai-theory\] Anchor: OQ-016 | Distinguish from generic hedging ("not unlike," "not without merit"). Precision-by-negation is specific; hedging-by-negation is evasion. | Yes — negation patterns natural for many ESL writers |
| DEAI-07 | AI prose has no rhythmic inheritance from any identifiable predecessor. Generic "model voice" — statistically averaged, not accumulated from reading. | Diagnostic only: if prose shows no rhythmic echo of any human writer's sentence patterns, flag as AI-default. Not a surface-level edit — requires human judgment. \[inferred:deai-theory\] Anchor: OQ-017 | Not falsifiable as a textual signal. Cannot be automated. | Yes — validates non-native writers absorbing English sentence patterns |
| DEAI-08 | AI narrates parallel action threads sequentially and explicitly. | Let one action thread advance implicitly at scene edges while narrating another in the foreground. Compress the background. \[inferred:deai-theory\] Anchor: OQ-020 | Untested. | Neutral |

### Kill-list distinguishing tests

These surface features appear in BOTH craft and AI-default writing. Use the distinguishing question.

| Surface feature | Craft version | AI-default version | Distinguishing question |
| --- | --- | --- | --- |
| Present tense | Deliberate choice for specific immediacy (Prejean execution scene) | Default tense from training data | Does switching to past tense lose something specific? If not, AI default. |
| Contrast/juxtaposition | Word-choice-level register mismatch (Kittredge: "nudged" + bear attack) | Generic thematic contrast ("hope amid despair") | Is contrast at diction level or only at theme level? |
| Short sentences | Rhythmic punctuation within longer syntax (Carver: "I knew that.") | Random short sentences, no rhythmic function | Does the short sentence follow longer ones and create specific emphasis? |
| Repetition | Functional cognitive anchoring (Baldwin memory, Anderson oral tradition) | Redundant word reuse from poor generation | Does removal damage rhythm or comprehension? If not, redundancy. |
| Negation | Precision-by-elimination ("I was not shocked") | Generic hedging ("not without merit") | Does the negation add specificity? Or is it equivocation? |

## 4) Craft moves — Lane B: tic_enrichment

Each move: what it does, how to borrow it without pastiche, when it fails.

| ID | Move | How to borrow | esl_preserve | Falsifier | Anchor |
| --- | --- | --- | --- | --- | --- |
| TIC-01 | Lead with strongest craft element | Open by deploying your strongest element (voice, premise, setting, character vulnerability) rather than balancing all equally. | Yes — natural emphasis protects non-native voice | Fails when writer cannot identify strongest element. | MUN-CM001 |
| TIC-02 | Action/reaction/reader-reaction engine | Three-beat minimum: something happens, someone reacts, reader reacts. Test every opening scene against this. | Yes — syntactically flexible across L1s | Missing any beat stalls the scene. | MQ-010 |
| TIC-03 | Emotional contract on page one | Name the target emotion and engineer it. Fear, sympathy, dark humor — not "interest." | Yes — direct emotional naming is ESL strength | Fails when emotion is stated, not evoked. | MUN-CM005 |
| TIC-04 | Circle of story | Plan opening and closing as a thematic echo pair. The echo is thematic, not lexical. | Yes — structural, any voice register | Fails when forced. Many successful works do not circle. | MQ-008 |
| TIC-05 | Two-word declarative opening | Subject-verb ignition: "We fought." Then elaborate with conditional "would." | Yes — accessible at all proficiency levels | Hemingway cosplay risk if overused. | OQ-005 |
| TIC-06 | Contrast diction | Gentle verbs for violent content. Register mismatch creates tonal dissonance. | Yes — L2 plainness can itself function as contrast | Fails when mismatch is clever, not felt. | OQ-007 |
| TIC-07 | Perception-through-other | Show Character A's interiority through B's interpretation of A's gesture, not through direct labeling. | Neutral | Standard technique. AI can produce it if prompted. | OQ-009 |
| TIC-08 | Deliberate repetition as cognitive hold | Repeat key words to hold a scene in place. Repetition enacts remembering. Borrow the principle, not specific word choices. | Yes — validates L2 repetition as craft choice | Fails when repetition is redundant, not functional. | OQ-008, OQ-018 |
| TIC-09 | Oral-tradition repetition | Choose NOT to revise away repetition when it serves a speaking voice. Anderson keeps "small" repeated — oral tradition, not literary polish. | Yes — validates L1 parallel repetition | Requires deliberate control. Unskilled repetition reads as error. | OQ-018 |
| TIC-10 | Word-chain image linking | Thread semantically related words across a sentence (gold to diamond to ring to wheel). Creates subliminal coherence. | Neutral | Fails when chain is arbitrary, not semantic-field connected. | OQ-019 |
| TIC-11 | Voice as lineage | Borrow rhythm and structure from predecessors, supply your own content. Exercise: identify 2-3 admired writers, create frame-fill exercises from their paragraphs. | Yes — validates L2 rhythm absorption | Fails when borrowing becomes pastiche (copying words, not structure). | OQ-017 |
| TIC-12 | Environmental metronome | Embed temporal cues in environmental rhythm (rocking, ticking, humming) rather than stating time jumps explicitly. | Neutral | Do not borrow a single author's specific imagery. | OLM-M013 |

## 5) Skill incorporation — atomic edit sessions

One edit session per row. Do not combine. Do not touch files from both skills in one session.

### Session 1: deai.skill / craft-theory-reference.md / ADD

Insert a new section titled "Opening Diagnostics (Munier 2016)" containing:

* The "nothing happens" binary test (DEAI-01) with MQ-001 verbatim
* The seven-question quick-screen (DEAI-02) with the seven questions listed
* Tag: \[inferred:structural-convergence — Munier 2016 predates AI; mapping is analyst inference\]
* Scope note: persuasive/narrative text only

### Session 2: deai.skill / craft-theory-reference.md / ADD

Insert a new section titled "Sentence-Level Craft Diagnostics (Olmstead 1997)" containing:

* Information burial (DEAI-03) with OQ-006 verbatim
* Short-declarative rhythm (DEAI-04) with OQ-010 verbatim
* Offstage action (DEAI-05) with OQ-020 verbatim
* Negative description (DEAI-06) with OQ-016 verbatim
* Peripheral compression (DEAI-08)
* Voice-lineage diagnostic (DEAI-07) with OQ-017 verbatim
* Tag each: \[inferred:deai-theory — not tested against model output\]
* Include falsifier per move from §3 table
* Note: RLHF syntactic evidence is conflicted — Varga 2025 vs Fredrick and Craven 2025. No unqualified claim about "AI syntax defaults."

### Session 3: deai.skill / craft-theory-reference.md / CHANGE

Add the kill-list distinguishing tests table from §3 to the existing kill-list section. These distinguish craft-use from AI-default-use of shared surface features.

### Session 4: deai.skill / detection canon refs / KEEP

Add one line citing Munier 2016 as converging practitioner source. Do not elevate to detection evidence. Do not modify detection canon.

### Session 5: tic.skill / voice-craft refs / ADD

Insert a new section titled "Distinctive Orientation Moves (Munier 2016 + Olmstead 1997)" containing:

* TIC-01 through TIC-12 from §4 table
* Each with \[esl_preserve\] tag where marked Yes
* Each with falsifier
* Tag: craft moves \[verified in source\]; esl tags \[inferred:operator-context\]

### Session 6: tic.skill / voice-craft refs / ADD

Insert a new section titled "Voice-Lineage Exercise Methodology (Olmstead 1997)" containing:

* The method: identify 2-3 admired writers, create frame-fill exercises from their paragraphs, generate own content within those frames
* OQ-017 verbatim as anchor
* Note: "borrow rhythm and structure, contribute your own content" — this IS the anti-pastiche principle stated as craft doctrine

### Session 7: tic.skill / SKILL.md / ADD

Insert three entries:

1. "Munier Opening-Engine Diagnostic" — the seven reader questions as a pre-flight check for opening scenes. Cross-reference deai.skill Session 1.
2. "Emotional Contract" — name the feeling the text should produce, test whether the opening delivers it.
3. "Frame-Fill Methodology" — Olmstead's structural-borrow-not-pastiche exercise method. Cross-reference Session 6.

## 6) Composer checklist

Implementor must verify PASS on every row before making any edit.

| Check | Instruction |
| --- | --- |
| Gate A quotes unchanged | Every Q-bank entry from §2 must appear verbatim in the target file. If any word differs, FAIL. |
| No 0628 re-litigation | No edit touches /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md. If any edit introduces a new detection-science claim, FAIL. |
| ESL tags preserved | Every esl_preserve=Yes must appear in target file. Tags are operator-context constraints, not empirical findings. If any edit removes a tag or adds native-norm polish advice, FAIL. |
| One session = one edit | Each §5 session is atomic. Do not combine sessions. Do not touch both deai.skill and tic.skill in one session. |
| No invented paths | Every file must exist before editing. Cursor does not create new files from this brief. |
| No \[verified\] promotion | No Munier or Olmstead claim may be tagged \[verified\]. Ceiling: practitioner opinion. |
| RLHF syntax conflict noted | Any reference to AI syntax must note: Varga 2025 vs Fredrick and Craven 2025. No unqualified claim. |
| Survivorship bias noted | Any added craft move must note: examples are commercially successful/canonical only. No failed applications examined. |
| Epistemic tags preserved | Every \[inferred\], \[speculative\], \[inferred:deai-theory\], \[inferred:operator-context\] tag must appear in the target file as written. Do not drop or upgrade. |

## 7) UNTESTED — defer to operator

* No craft move from these sources has been tested against RLHF output
* RLHF syntactic behavior is domain-dependent, not settled
* \[esl_preserve\] tags are operator-context inference, not empirically grounded
* Munier Chapters 3-8 are not ingested; second pass would yield additional moves
* Munier Top 11 item 9 ("all showing and no telling") may be an error — unresolved