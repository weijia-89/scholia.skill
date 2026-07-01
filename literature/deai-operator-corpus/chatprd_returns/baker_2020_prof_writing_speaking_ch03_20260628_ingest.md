# Baker 2020 — Professional Writing and Speaking (5e) — Ch03 Composing Business Messages

Slug: baker_2020_prof_writing_speaking Chapter: ch03 Lane: tic_enrichment (primary), deai_removal (secondary) Operator: Wei Jia · ESL fairness mandatory · stakes L3 Schema: scholia SF-12 ingest (≤4500w) chapters_attested: ch03 only Truncation note: Attached export truncated at \~80k chars. Full coverage confirmed through Easy Persuasion Messages. Difficult Persuasion and Bad News sections available only from Table 3.5 summary rows; detailed prose for those two categories is NOT attested. Flagged as \[TRUNCATION GAP\].

---

## Iron Law Requirements

* Closed-corpus: all claims from attached ch03 export only. No open-web gap-fill performed on primary text content.
* Gate A: every Q-bank quote checked against inline attachment text. One OCR-induced mismatch flagged (Q-004).
* Two-lane tags applied per craft move.
* Canon inherited; not re-litigated.
* Adversarial review completed this turn per search policy. External verification applied to structural claims about source type and framework provenance.

---

## Source Discovery

| Factor | Assessment |
| --- | --- |
| Source type | Tier 3 — undergraduate textbook (practitioner pedagogy, not peer-reviewed research) \[verified — RedShelf listing: Baker, William H., Matthew J. Baker, and Vincent D. Robles. Professional Writing and Speaking, 5th ed. Noun Publishing, 2020. ISBN 9781735184302\] |
| Methodology | Prescriptive; no empirical data cited for effectiveness claims |
| Conflicts of interest | None detected; standard academic publisher (Noun Publishing, small press) |
| Survivorship bias | N/A — pedagogical framework, not outcome study |
| Recency | 2020 (5th edition); structural writing advice is non-perishable \[verified — teachtowrite.com authors page confirms 5th ed. published 2020\] |
| Specificity | High on technique, low on evidence base |
| Replication | Five C's and OABC frameworks appear across multiple biz-comm textbooks and university writing centers \[verified — UNC Writing Center uses OABC; Cal Poly Pomona uses 10 C's variant; multiple writing pedagogy sites reproduce Five C's with variations\] |

---

## Confidence Scoring

Overall source utility for deai/tic craft: 58/100 \[c1=50, c2=55, c3=68; FINAL=55, rounded to 58 after qualitative adjustment\]

* c1 (source quality): Undergraduate textbook from a small publisher; no primary research; no peer review. Tier convergence with standard biz-comm canon, but Baker's specific formulations (CLOUD, OABC with four agenda types) appear to originate with Baker, not with the broader field. 50.
* c2 (effect size / replication): Prescriptive frameworks; no measured effect sizes. The underlying concepts (topic sentences, active voice, audience analysis) are consensus pedagogy, but the specific mnemonic packaging is Baker-original and unreplicated as a system. 55.
* c3 (recency / adversarial counter): Writing-structure advice is durable. Counter-argument: textbook treats "considerate" writing with euphemism framing that can conflict with ESL-preserve mandate. Additional counter: the RLHF-mapping claims in the skill incorporation table are analogies drawn by the ingest author, not by Baker. 68.

Post-downward-pressure revision: Initial score was 62. Strongest argument for 10-point reduction: the primary value proposition (these frameworks fix RLHF patterns) is an ingest-author inference, not a source claim. Baker never discusses LLMs. The score reflects source utility, not the inferential claims built on top of it. Reduced to 58.

\[CONFIDENCE DISPUTED on c1-c2 spread\]: c1=50, c2=55, c3=68. max-min=18 (<20 threshold). Not disputed, but close. The c3 score is driven by durability of writing advice generally, not by Baker specifically.

---

## Load-Bearing Claims Registry

| ID | Claim | Tag | Source / Chain | Failure Mode |
| --- | --- | --- | --- | --- |
| C-001 | Baker 2020 is a real textbook, 5th edition, published 2020 | \[verified\] | RedShelf listing (ISBN 9781735184302); VitalSource listing; teachtowrite.com authors page | Book could be misattributed to wrong year — but three independent retailer listings agree on 2020 |
| C-002 | Ch03 covers Five C's (Clear, Complete, Correct, Considerate, Convincing), CLOUD, and OABC | \[verified\] | Attachment text, cross-checked against teachtowrite.com sample pages summary | Misread of OCR'd text could map wrong content to wrong section |
| C-003 | Five C's frameworks are widely used in biz-comm pedagogy | \[verified\] | Cal Poly Pomona 10 C's guide; UK Writing Courses 5 C's; legalknowledgebase.com variants | Baker's specific five (with "Convincing" replacing common "Concise") may be less standard than implied |
| C-004 | OABC is used beyond Baker's textbook | \[verified\] | UNC Writing Center; skillnation.in; teachtowrite.com 3-levels PDF | OABC may originate with Baker and be adopted downstream rather than being independently developed |
| C-005 | Baker's concision heuristics (5 tips) directly target RLHF verbosity patterns | \[inferred\] | Chain: RLHF models exhibit verbosity bias \[verified — Singhal et al. 2023 arxiv 2310.10076; Shen et al. 2023 arxiv 2310.03716\]; Baker's tips reduce wordcount → inference that they address same surface problem | Analogy, not causal link. Baker wrote for human writers in 2020. The tips address human verbosity, not RLHF-specific patterns. RLHF verbosity has distinct mechanisms (reward-model length bias) that Baker's tips do not address at the generative level |
| C-006 | RLHF models default to inappropriately indirect approach | \[speculative\] | No source cited. Plausible from practitioner observation but untested in this review | Would require systematic analysis of LLM output approach patterns across message types |
| C-007 | "Underdeveloped paragraphs are an RLHF residue pattern" | \[speculative\] | No source. Anecdotal practitioner observation | RLHF models more commonly over-develop (verbose) than under-develop. This claim may be wrong for the dominant failure mode |
| C-008 | RLHF outputs "often fail on chunking (wall-of-text)" | \[speculative\] | No source. LLMs frequently use headers and bullet lists (arguably over-chunk). Claim direction may be inverted | Would require content analysis of LLM outputs vs. Baker's chunking standard |
| C-009 | Table 3.1 logic fallacies are standard informal-logic taxonomy | \[verified\] | Standard names (ad hominem, straw man, false causality, bandwagon, slippery slope, etc.) match any introductory logic textbook | Baker's examples are business-contextualized but the taxonomy is not novel |
| C-010 | Table 3.3 cohesion taxonomy (9 types) can replace generic LLM connectives | \[inferred\] | Chain: LLM outputs use generic connectives like "additionally" and "moreover" \[speculative — practitioner observation\]; Baker's taxonomy provides more semantically precise alternatives → inference that substitution improves specificity | "Generic connectives" claim is unverified. Some LLM outputs use varied connectives. The improvement claim is plausible but untested |
| C-011 | "You attitude" concept is standard biz-comm pedagogy, not Baker-unique | \[verified\] | Kitty O. Locker (GVSU handout); ThoughtCo; Miami Farmer School; UBC handout — all discuss you-attitude independently | N/A — this is a provenance claim, not an effectiveness claim |
| C-012 | Euphemism guidance in "Considerate" section conflicts with ESL-preserve mandate | \[inferred\] | Chain: Baker advises euphemisms for social sensitivity ("employment was terminated" vs "was fired") \[verified — attachment text §Considerate\]; ESL-preserve mandate prohibits erasing L1-influenced directness \[verified — operator instructions\]; L1-Chinese speakers tend toward direct phrasing \[speculative — linguistic generalization\] → inference of conflict | The conflict exists only if the operator's natural phrasing would trigger euphemism correction. Not all Baker euphemism advice targets L1-influenced patterns |
| C-013 | Q-bank entries Q-001 through Q-012 are verbatim from ch03 | \[inferred\] | Checked against OCR'd attachment text. OCR artifacts make strict "verbatim" uncertain — the attachment is an OCR scan with character-level errors throughout | Q-004 contains "gives adequately answers" which appears to be OCR error for "gives adequate answers." The quote may not be verbatim from the actual printed text |
| C-014 | "Negative tone is almost never appropriate" reflects positivity bias parallel to RLHF | \[inferred\] | Chain: Baker states negative tone is "almost never appropriate" \[verified — attachment text\]; RLHF models exhibit positivity bias \[speculative — practitioner claim, not cited to research this turn\] → inference of parallel | The parallel is suggestive but superficial. Baker's advice is pragmatic (negative tone damages relationships); RLHF positivity bias has a different mechanism (reward model optimization). Calling this a "parallel" overstates the connection |
| C-015 | Textbook is Tier 3 source quality | \[inferred\] | Chain: it is an undergraduate textbook \[verified\]; undergraduate textbooks rank below peer-reviewed and institutional research in standard evidence hierarchies → Tier 3 | Could argue Tier 2.5 if the textbook were widely adopted at major institutions. BYU adoption confirmed but breadth unknown |
| C-016 | Six message categories cover the main business message types | \[verified\] | Attachment text Table 3.5 lists all six with OABC guidelines | This is a claim about Baker's categorization, not about exhaustiveness. Baker may omit categories (e.g., crisis communication, cross-cultural messages) |
| C-017 | Cohesion taxonomy is more useful than generic LLM connectives for tic_enrichment | \[speculative\] | No comparative evidence. The taxonomy provides more options, but "more useful" requires demonstrated improvement in output quality | Would need A/B testing of outputs using Baker's cohesion types vs. default LLM connectives |
| C-018 | CLOUD mnemonic uses Cohesion (not Coherence) as the C | \[verified\] | Attachment text: "remember the attributes of cohesion, length, organization, unity, and development (remembered as CLOUD)" — Baker distinguishes cohesion (micro) from coherence (macro) in the text | Some external sources list CLOUD as "Coherence, Length, Organization, Unity, Development" (abbreviations.com). Baker's version uses Cohesion. This is a Baker-specific usage |
| C-019 | Direct approach is default; indirect only for bad news / difficult persuasion | \[verified\] | Attachment text Table 3.5 and §Opening: four of six categories use direct approach; two (difficult persuasion, bad news) use indirect | This is Baker's prescription. Other biz-comm texts may differ on where to draw the line |
| C-020 | Emoji guidance should be dropped (S-12) | \[inferred\] | Chain: Baker includes emoji guidance for informal electronic messages \[verified — attachment text\]; operator's use case is craft-move bank for deai/tic \[verified — prompt meta\]; emoji guidance is irrelevant to that use case → DROP | If operator later works on informal messaging craft, this DROP would need revisiting |
| C-021 | Truncation gap covers the highest-value material for deai work | \[speculative\] | Difficult Persuasion and Bad News sections use indirect approach, which is where RLHF-default behavior concentrates \[speculative — C-006\]. If C-006 is wrong, the truncation gap is less critical | Testable: process full export and evaluate whether indirect-approach detailed prose adds craft moves not available from Table 3.5 summary |

---

## Gate A — Verbatim Q-Bank (from ch03 only)

All quotes checked against the OCR'd attachment text inline. OCR artifacts present throughout the source — character substitutions, merged words, spacing errors. Quotes below are best-reconstruction from OCR. One mismatch flagged.

Q-001 \[Five C's definition\] "strive to make your writing clear, complete, correct, considerate, and convincing" — §Five C's of Effective Documents \[OCR-match confirmed\]

Q-002 \[Clarity — chunking\] "Break the text into small bite-size chunks. Large masses of text are overwhelming and difficult to process. Small chunks are much easier." — §Clear, item 1 \[OCR-match confirmed\]

Q-003 \[Clarity — appropriate words\] "Use appropriate words. Choose words that the audience will understand and words that have an appropriate level of precision." — §Clear, item 3 \[OCR-match confirmed\]

Q-004 \[Completeness — 5W2H\] "Make sure the text gives adequate answers to all relevant 5W2H questions — who, what, when, where, why, how, and how much." — §Complete \[FLAG: OCR text reads "gives adequately answers" — likely OCR error for "gives adequate answers" or "adequately answers." The quote as rendered in the ingest may not match the printed page exactly. Tagged \[OCR UNCERTAIN\].\]

Q-005 \[Correctness — weasel words\] "avoid the use of weasel words — words that give a vague or ambiguous claim that misleads" — §Correct \[OCR-match confirmed\]

Q-006 \[Considerate — you attitude\] "Messages that have a you attitude focus on meeting the reader's needs, not just on the writer's." — §Considerate \[OCR-match confirmed\]

Q-007 \[CLOUD acronym\] "remember the attributes of cohesion, length, organization, unity, and development (remembered as CLOUD)" — §CLOUD Paragraph Structure \[OCR-match confirmed\]

Q-008 \[Concision — active voice\] "a. No: Customer-service training was given by Collette to 13 people. \[10 words\] b. Yes: Collette gave customer-service training to 13 people. \[8 words\]" — §Length, tip 1 \[OCR-match confirmed\]

Q-009 \[OABC definition\] "OABC is a message pattern that can be used in many writing situations. OABC stands for opening, agenda, body, and closing." — §OABC Message Pattern \[OCR-match confirmed\]

Q-010 \[Agenda — four types\] "choose from the following four types — quantify, identify, organize, and symbolize" — §Agenda \[OCR-match confirmed\]

Q-011 \[Opening — direct approach rationale\] "Professionals are busy people, and they want you to get to the point quickly and then to give appropriate details." — §Opening \[OCR-match confirmed\]

Q-012 \[Logic fallacies — false causality\] "Arguing that because two items occur together, one must be causing the other." — Table 3.1, False causality row \[OCR-match confirmed\]

---

## Key Concepts Extracted

### Five C's Framework \[lane: tic_enrichment\]

| Attribute | Core Principle | Craft Relevance |
| --- | --- | --- |
| Clear | Chunk content; coherent flow; appropriate word choice; visual signposts | Maps to deai: address verbosity and under-chunking. Note: C-008 flags that LLMs may over-chunk rather than under-chunk — direction of fix is context-dependent \[speculative\] |
| Complete | 5W2H coverage; anticipate audience questions; avoid TMI | Relevant to tic: complete without padding. Anti-RLHF-filler is plausible but unverified as a systematic pattern \[speculative\] |
| Correct | No logic fallacies; no weasel words; proper citation; no defamation | Table 3.1 logic fallacies are a standard taxonomy \[verified — C-009\]. Useful as audit checklist for any generated reasoning |
| Considerate | Formality calibration; tone (positive/neutral/negative); you-attitude vs me-attitude | \[esl_preserve\] tension: euphemism framing can erase L1-influenced directness \[inferred — C-012\]. Borrow formality calibration; reject euphemism-as-rule |
| Convincing | Logical + emotional appeals; positive/negative framing; evidence use | Maps to persuasion message categories. No novel contribution beyond standard rhetoric |

### CLOUD Paragraph Model \[lane: tic_enrichment\]

| Attribute | Principle | Craft Application |
| --- | --- | --- |
| Development | Use 5W2H; methods: applications, evaluations, explanations, instances, authority (Table 3.2) | Development checks catch underdeveloped support for claims. Note: C-007 flags that RLHF's dominant failure mode may be over-development (verbosity), not under-development |
| Unity | All sentences pertain to paragraph topic | Unity check is a useful edit pass regardless of whether the writer is human or LLM |
| Organization | Topic sentence leads (direct) or culminates (indirect); skimmability | Direct approach = topic sentence first. Baker's prescription aligns with standard biz-comm consensus \[verified — C-019\] |
| Length | Trust your eyes; one-sentence paragraphs acceptable in professional writing | Concision heuristics (5 tips): active voice, eliminate redundancy, reduce inflated phrases, omit empty subjects, reduce clutter. These target human verbosity; mapping to RLHF verbosity is analogical \[inferred — C-005\] |
| Cohesion | Micro-level connective tissue: reference preceding text, forecast upcoming text, show relationships | Table 3.3 cohesion types: comparison, condition, consequence, extension, forecasting, location, numeration, reference, sequence. Baker distinguishes cohesion (micro) from coherence (macro) \[verified — C-018\] |

### OABC Message Pattern \[lane: tic_enrichment\]

* Opening: Key point or main message first (direct) or background-first (indirect for bad news). Critical info goes here because readers skim after first sentence.
* Agenda: Preview/forecast of body. Four types: quantify (how many sections), identify (label sections), organize (describe sequence), symbolize (metaphor). Short messages may omit.
* Body: Content matching the agenda forecast. Structure mirrors outline.
* Closing: Summarize, conclude, recommend action, or provide cordial sign-off.

Pattern confirmed in use at UNC Writing Center and multiple pedagogy sites \[verified — C-004\]. Origin appears to be Baker (or Baker's institution), adopted downstream.

### Six Message Categories \[lane: tic_enrichment\]

| Category | Audience State | Approach | OABC Notes |
| --- | --- | --- | --- |
| Relationship building | Receptive | Direct | Opening = main point; no agenda needed; body = additional thoughts; close as appropriate |
| Good news | Receptive | Direct | Opening = good news; agenda as needed; body = relevant details; close = cordial reference to good news |
| Informative | Generally receptive | Usually direct | Opening = main point; agenda as appropriate; body = details consistent with agenda; close = forward-looking |
| Easy persuasion | Uncontested to interested | Direct or slightly indirect | Opening = background + main point; agenda as appropriate; body = positive info, logical/emotional persuasion; close = desired action |
| Difficult persuasion | Displeased to agreeable | Indirect | Opening = frame issue without main point; agenda = general identity; body = reasoning then main point, highlight positives, minimize negatives; close = reinforce positives, request action |
| Bad news | Shocked/disappointed | Indirect | Opening = related content without bad news; agenda = general identity; body = reasoning leading to de-emphasized bad news; close = options or mildly positive content |

\[TRUNCATION GAP\]: Detailed prose for Difficult Persuasion and Bad News categories not attested in available export. Table 3.5 summary rows are attested. Do not cite detailed examples from these sections.

---

## Skill Incorporation Table

| ID | Skill / Pattern | Action | Lane | Rationale |
| --- | --- | --- | --- | --- |
| S-01 | OABC message scaffolding | KEEP | tic_enrichment | Structural pattern for message composition. Confirmed in external biz-comm pedagogy \[C-004\]. Not author-voice pastiche — pure structure. |
| S-02 | Five C's as edit-pass checklist | KEEP | both | After drafting, run a five-pass audit. Useful for catching vagueness, over-hedging, TMI. Baker's specific variant (with "Convincing") is somewhat idiosyncratic — standard variants use "Concise" \[C-003\]. Borrow the checklist concept; do not treat Baker's exact five as canonical. |
| S-03 | CLOUD paragraph self-check | KEEP | tic_enrichment | Unity and organization checks are universally applicable edit passes. Development check direction depends on failure mode: check for under-development in terse outputs, over-development in verbose ones \[revised per C-007\]. |
| S-04 | Concision heuristics (5 tips) | KEEP | deai_removal | Active voice, eliminate redundancy, reduce inflated phrases, omit empty subjects, reduce clutter. These are standard concision advice \[C-005 — OVERSTATED from "directly target RLHF" to "address surface verbosity patterns applicable to any verbose text, including RLHF output"\]. |
| S-05 | Logic fallacy table (Table 3.1) | KEEP | both | 11 named fallacies with examples. Standard informal-logic taxonomy \[C-009\]. Useful as audit layer, not a Baker-original contribution. |
| S-06 | Euphemism-as-rule framing in "Considerate" section | CHANGE | esl_preserve | Borrow formality-calibration principle; reject blanket euphemism rule. Tag: \[esl_preserve\] — never use euphemism guidance to "smooth" an ESL operator's natural directness. This CHANGE survives adversarial review \[C-012 — conflict is real, though narrower than initially stated\]. |
| S-07 | You-attitude vs me-attitude | KEEP | tic_enrichment | Reader-centered framing. Standard biz-comm concept \[C-011\]. Does not conflict with ESL voice preservation. |
| S-08 | Agenda types (quantify, identify, organize, symbolize) | KEEP | tic_enrichment | Granular preview taxonomy. "Identify" agendas map well to structured deliverables. Four-type taxonomy may be Baker-specific packaging of a common idea \[C-004\]. |
| S-09 | Tone calibration (positive/neutral/negative) | KEEP with caution | tic_enrichment | Three-level model is oversimplified. Baker's claim that "negative tone is almost never appropriate" parallels positivity bias in both human pedagogy and RLHF, but the mechanisms differ \[C-014 — OVERSTATED\]. Borrow the calibration principle; do not borrow the positivity default. |
| S-10 | Cohesion word taxonomy (Table 3.3) | ADD | tic_enrichment | Nine cohesion types. Claim that these replace "generic LLM connectives" is speculative \[C-017 — UNTESTED\]. Value is in providing a richer vocabulary of connective strategies. Utility must be assessed empirically in actual tic outputs. |
| S-11 | Direct vs indirect approach selection | KEEP | both | Direct = default for receptive audiences. Indirect = bad news, difficult persuasion \[C-019\]. Claim that RLHF defaults to inappropriate indirectness is speculative \[C-006\]. Borrow the selection framework; test the RLHF-mapping claim separately. |
| S-12 | Emoji/emoticon guidance | DROP | — | Dated and context-inappropriate for operator's use case \[C-020\]. |

---

## Adversarial Review

### Hostile Expert Objections

Objection 1: No empirical validation for any framework. The Five C's, CLOUD, and OABC are pedagogical mnemonics. No study cited — by Baker or by this ingest — demonstrates that applying these frameworks improves writing quality by any measurable metric. Response: Correct. These are heuristic tools, not evidence-based interventions. The ingest does not claim empirical backing. Source confidence score reflects this (58/100). Downstream use should treat these as structural scaffolds to be validated through operator experience, not as proven methods.

Objection 2: Craft-move mapping to RLHF is analogical, not demonstrated. Every claim that a Baker technique "fixes" an RLHF pattern (C-005, C-006, C-007, C-008, C-014) is an inference drawn by the ingest author. Baker wrote for undergraduate human writers in 2020. He never discusses LLMs, RLHF, or AI-generated text. The mapping assumes surface similarity between human writing errors and LLM output errors, which may not hold — RLHF verbosity has distinct generative mechanisms (reward-model length bias per Singhal et al. 2023, Shen et al. 2023). Response: Accepted. All RLHF-mapping claims are now tagged \[speculative\] or \[inferred\] with the analogical chain made explicit. No RLHF-mapping claim appears as \[verified\]. Downstream craft-move adoption should test these mappings empirically before treating them as established.

Objection 3: CLOUD and Five C's are not unique to Baker. The underlying concepts (topic sentences, unity, coherence, active voice, audience analysis) appear in every introductory writing textbook. Baker's contribution is mnemonic packaging, not conceptual novelty. Treating Baker as a "source" for these ideas overstates his authorship. Response: Partially accepted. The ingest now notes where concepts are standard (C-003, C-009, C-011) and where Baker's specific packaging may be original (OABC four agenda types, CLOUD with Cohesion vs Coherence distinction). The skill incorporation table attributes borrowable value to the mnemonic structures while noting they are not Baker-original ideas.

### Kill List

| ID | Verdict | Note |
| --- | --- | --- |
| C-005 | OVERSTATED | Concision heuristics "directly target RLHF verbosity patterns" → revised to "address surface verbosity applicable to any verbose text." The causal specificity to RLHF is an unsupported inference. |
| C-007 | OVERSTATED | "Underdeveloped paragraphs are an RLHF residue pattern" → RLHF's dominant verbosity failure mode suggests over-development is more common. Under-development is possible but not the typical pattern. Scope narrowed. |
| C-008 | OVERSTATED | "RLHF outputs often fail on chunking (wall-of-text)" → LLMs frequently over-chunk with excessive headers and bullets. Direction of failure is context-dependent, not unidirectional. Scope narrowed. |
| C-014 | OVERSTATED | "Negative tone" advice parallels RLHF positivity bias → the parallel is superficial. Baker's advice is pragmatic (about human relationship maintenance); RLHF positivity bias is mechanistic (reward model optimization). The word "parallel" survives; "reflects" was too strong. |
| C-017 | UNTESTED | Cohesion taxonomy is "more useful" than generic LLM connectives → no comparative evidence exists. May not appear as load-bearing in synthesis. |
| C-006 | UNTESTED | RLHF models default to inappropriately indirect approach → practitioner intuition, untested. May not appear as load-bearing in synthesis. |

No claims WRONG (falsified). All survive with scope reductions or tag downgrades.

### Overconfidence Check

Confidence scores in document: overall 58/100. No individual score at 80+. Check passes. No downward-pressure needed beyond the overall reduction from 62 to 58 already applied.

### Unverifiable Items and Evidence Gaps

* Whether Baker's OABC originates with Baker or was adopted from an earlier source — origin tracing not completed
* Whether CLOUD uses "Cohesion" uniquely in Baker vs "Coherence" in earlier editions — would require edition comparison
* Full text of Difficult Persuasion and Bad News prose sections — requires processing untruncated export
* Whether LLM outputs systematically exhibit the specific failure modes mapped in the skill incorporation table — requires content analysis study
* Whether Baker's Five C's variant (with "Convincing" instead of "Concise") has pedagogical advantages over standard variants — no comparative study exists
* Q-004 exact wording in printed text vs OCR — requires access to physical or properly rendered digital copy
* The arxiv 2411.07858 paper referenced in the template is titled "Demystify Verbosity Compensation Behavior" (later "Veracity"), not "Verbosity≠Veracity" — the template's shorthand is imprecise but directionally correct

---

## Synthesis (post-review)

Five borrowable patterns survive adversarial review. All RLHF-mapping claims are inferential or speculative; none should be treated as established in downstream craft-move implementation.

1. OABC as tic scaffold \[tic_enrichment\] — confirmed as standard biz-comm pedagogy. Borrowable as message architecture. Not voice, not style. \[C-004 verified\]

2. Concision heuristics as deai checklist \[deai_removal\] — five actionable tips that reduce wordcount in any verbose text. Mapping to RLHF-specific verbosity is analogical, not demonstrated \[C-005 OVERSTATED → scoped\]. Still useful for surface-level deai passes.

3. Logic fallacy table as reasoning-audit tool \[both\] — 11 standard named fallacies. Not a Baker contribution; a standard informal-logic taxonomy recontextualized for business writing \[C-009 verified\]. Value is in the business-specific examples, not the taxonomy itself.

4. Cohesion taxonomy as sentence-craft vocabulary \[tic_enrichment\] — nine types provide more semantic precision than default connective habits. Utility claim is speculative \[C-017 UNTESTED\]. Worth testing in tic outputs; do not assume improvement without evidence.

5. Direct/indirect approach selector \[both\] — principled framework for when to lead with conclusion vs build toward it. RLHF-mapping claim (models default to inappropriate indirectness) is speculative \[C-006 UNTESTED\]. The selector itself is a sound structural tool independent of the RLHF claim.

Not borrowable: emoji guidance (dropped), euphemism-as-rule (changed to borrow formality calibration only), positivity-bias in tone model (flagged, not adopted as default).

Action required: Process full export to close truncation gap on Difficult Persuasion and Bad News sections. These sections cover indirect approach in detail — the highest-value material for deai work if C-006 (RLHF defaults to inappropriate indirectness) is eventually confirmed.