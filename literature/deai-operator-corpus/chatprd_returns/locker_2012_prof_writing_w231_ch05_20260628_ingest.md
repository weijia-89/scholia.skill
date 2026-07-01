# Locker 2012 — Ch05: Planning, Composing, and Revising

Slug: locker_2012_prof_writing_w231_ch05 Schema: scholia SF-12 ingest, ≤4500w Chapters attested: ch05 only Source: 06_locker_2012_prof_writing_w231_ch05_ATTACH.txt (truncated at 80K chars; items 6–10 of "Ten Ways" and later revision/editing sections partially or fully missing) Review status: Adversarial review complete (v2)

---

## 1\. Chapter Architecture

The chapter divides the writing process into four named activities, then teaches sentence- and word-level craft under a "Ten Ways to Make Your Writing Easier to Read" framework. Structure:

* Planning (brainstorming, gathering, selecting, organizing)
* Writing (drafts of all fidelities — lists through formal draft)
* Revising (re-seeing against goals; external feedback; add/delete/substitute/rearrange)
* Editing (surface: spelling, mechanics, word choice, format; proofreading)

Key structural claim: these activities are non-linear, interruptible, and scaled to document complexity. Traditional outlining is explicitly cautioned against — it "may lull writers into a false sense of confidence about their material and organization."

Time allocation heuristic: one-third planning, one-third writing, one-third revising/editing.

---

## 2\. Gate A — Verbatim Q-Bank (from this slice only)

All quotes verified present in attached text export. Gate A (closed-corpus) passed.

Q-001: "Spend only one-third of your time actually 'writing.' Spend at least another one-third of your time analyzing the situation and your audience, gathering information, and organizing what you have to say." Section anchor: USING YOUR TIME EFFECTIVELY

Q-002: "Traditional outlining may lull writers into a false sense of confidence about their material and organization, making it difficult for them to revise their content and structure if they deviate from the outline developed early in the process." Section anchor: BRAINSTORMING, PLANNING, AND ORGANIZING BUSINESS DOCUMENTS

Q-003: "Good business and administrative writing is closer to conversation and less formal than the style of writing that has traditionally earned high marks in college essays and term papers." Section anchor: WRITING GOOD BUSINESS AND ADMINISTRATIVE DOCUMENTS

Q-004: "We tend to rely on nouns rather than on verbs and deaden our style when we are under stress or feel insecure. Confident people are more direct." Section anchor: Style advice, bullet on stress/formality

Q-005: "All communication affects \[the\] bottom line. . . . When a reader, listener, viewer or member of a live audience has to take even a nanosecond to decipher what you are saying because you are making it more complicated than it needs to be, you may lose that person." Section anchor: Plain language discussion, citing Gerard Braud

Q-006: "Direct, simple writing is easier to read. One study tested two versions of a memo report. The 'high-impact' version . . . took 22% less time to read." Section anchor: TEN WAYS TO MAKE YOUR WRITING EASIER TO READ Provenance note: \[ZOMBIE\] — Locker cites an unnamed study with endnote reference. No author, year, sample size, or methodology recoverable from attached text. The 22% figure cannot be traced to a primary source.

Q-007: "Put the weight of your sentence in the verb to make your sentences more forceful and up to 25% easier to read." Section anchor: Item 4, Use verbs — not nouns Provenance note: \[ZOMBIE\] — Same issue. Locker cites an endnote. The 25% figure appears in practitioner writing guides (e.g., Instructional Solutions, HubSpot clarity guides) without traceable methodology. No primary study recovered.

Q-008: "Credit is like oxygen. When either is abundant, its presence goes unnoticed. When either is missing, that's all that is noticed." Section anchor: Warren Buffett letter examples Provenance note: Secondary quotation — Locker attributes to Buffett's 2010 letter. Multiple sources disagree on whether the quote originates in the 2007, 2008, or 2010 Berkshire Hathaway annual report. Direct fetch of the 2007, 2008, and 2010 letters (all truncated by fetch tool at 50K chars) did not surface the verbatim text. The quote is confirmed present in Locker's chapter text. Attribution year: \[unknown — unable to verify which Berkshire letter contains the verbatim quote\].

---

## 3\. Claim Registry and Verification

### Load-bearing claims

| ID | Claim | Tag | Source / Evidence | Failure mode |
| --- | --- | --- | --- | --- |
| C-001 | Locker's four-activity writing process model (plan/write/revise/edit) is non-linear and interruptible | \[verified\] | Verbatim in attached text (Q-002 context). Consistent with Flower & Hayes (1981) cognitive process model. | Locker's version is simplified from Flower & Hayes; non-linearity claim is textbook-level, not research-level |
| C-002 | One-third time allocation heuristic (plan/write/revise) | \[verified\] | Verbatim in attached text (Q-001). | Prescriptive, not empirically derived. Locker provides no study backing this ratio |
| C-003 | "High-impact" memo took 22% less time to read | \[speculative — ZOMBIE\] | Locker cites unnamed study via endnote. No primary source recoverable. | The 22% figure may be fabricated, misremembered, or from an unpublished/proprietary study |
| C-004 | Verb-forward sentences are "up to 25% easier to read" | \[speculative — ZOMBIE\] | Same as C-003. Appears in practitioner sources without methodology. | Practitioner echo chamber — the number circulates without attribution |
| C-005 | RLHF-trained models default to passive hedging ("It should be noted that...") | \[WRONG — falsified\] | PMC 11874169 / arxiv 2410.16107: GPT-4o uses agentless passive voice at roughly HALF the human rate. Instruction-tuned models show REDUCED passive voice, not increased. | The ingest v1 claim reversed the direction of the effect |
| C-006 | RLHF-trained models over-nominalize ("provide an explanation" instead of "explain") | \[verified\] | PMC 11874169 / arxiv 2410.16107: instruction-tuned LLMs show nominalizations at \~1.5–2.1x human rate (GPT-4o \~2.1x). Methodology: 66 Biber features, paired Wilcoxon with Bonferroni correction, open code/data. \[c1=80, c2=70, c3=75; FINAL=75\] | Single research group; replication pending; effect sizes vary by model family |
| C-007 | Passive voice is acceptable for emphasis, coherence, or tact (Locker's 3-case framework) | \[verified\] | Verbatim in attached text with examples. Standard composition pedagogy. | Pedagogical consensus, not empirical finding |
| C-008 | Buffett "credit is like oxygen" quote appears in 2010 Berkshire letter | \[unknown\] | Quote present in Locker's text. Year attribution could not be confirmed — fetches of 2007, 2008, 2010 letters were all truncated before reaching the relevant section. Secondary sources disagree (some cite 2007, some 2008, one cites 2010). | Misattributed year would not affect the ingest's craft-move extraction but undermines provenance accuracy |
| C-009 | Seven half-truths are commonly taught as absolutes | \[verified\] | All seven present verbatim in attached text with Locker's contextual qualifications | "Commonly taught" is Locker's assertion; the claim that RLHF encodes them as absolutes (C-011) is separate |
| C-010 | Plain Writing Act of 2010 requires federal agencies to use clear prose | \[verified\] | Public Law 111-274, confirmed via congress.gov fetch (200 OK, full text). PlainLanguage.gov confirmed active. | None — straightforward legislative fact |
| C-011 | RLHF training encodes half-truths as absolutes (especially #1, #6, #7) | \[speculative\] | No empirical study tests whether RLHF models enforce these specific writing rules. Plausible given mode-collapse literature (ICLR 2024) but unverified for these specific rules. | Would require corpus analysis of model outputs against each half-truth |
| C-012 | A writer's selective violation of half-truths is a voice signature worth preserving | \[inferred\] | Derived from: (a) Locker's framework that rules are context-dependent \[verified in text\], (b) Sommers 1980 finding that expert revision involves rhetorical choices beyond surface compliance \[verified via JSTOR/ERIC\]. Chain: if rules are contextual AND expert writers make deliberate violations AND voice is constituted by habitual choices, then violations can be signatures. | The inference assumes violations are deliberate, not accidental. For ESL writers, some "violations" may be L1 transfer patterns, which is precisely what \[esl_preserve\] addresses |

### Calibration gate (C-006, the only claim at conf ≥80 before review)

* c1 (source quality + tier convergence): 80 — peer-reviewed, open methodology, but single research group
* c2 (effect size + replication): 70 — strong effect sizes (Cohen's d reported), but no independent replication yet
* c3 (recency + adversarial counter-argument): 75 — published 2024, within window; counter-argument is that effect may be model-family-specific (Llama variants showed different patterns from GPT-4o)
* max-min = 10 (below 20 threshold)
* FINAL = 75

---

## 4\. Kill List

| ID | Verdict | Sentence |
| --- | --- | --- |
| C-003 | UNTESTED | The 22% reading-time reduction figure traces to an unnamed study in Locker's endnotes; no primary source with described methodology was recovered. |
| C-004 | UNTESTED | The 25% readability figure circulates in practitioner guides without attribution; no primary study was found. |
| C-005 | WRONG | Empirical evidence shows instruction-tuned LLMs use LESS agentless passive voice than humans (roughly half the rate), directly contradicting the claim that RLHF models "default to passive hedging." |
| C-008 | OVERSTATED | The Buffett quote exists and Locker cites it, but the year attribution (2010) could not be confirmed; sources disagree on whether it originates in 2007, 2008, or 2010. |
| C-011 | UNTESTED | No empirical study tests RLHF encoding of these specific half-truths; the claim cannot appear as load-bearing in synthesis. |

---

## 5\. Hostile Expert Objections

Objection 1: The ingest treats a survey textbook as a source of craft moves without distinguishing empirically grounded claims from pedagogical convention.

Response: Accepted. Locker's chapter is pedagogical, not empirical. The four-activity model, time allocation heuristic, and half-truths framework are teaching tools, not research findings. The ingest now tags each claim's evidentiary basis. The craft moves remain useful as heuristics for de-AI and voice work, but none should be treated as empirically validated writing rules.

Objection 2: The "RLHF residue" applications are inferences layered onto Locker's content — Locker wrote in 2012 and says nothing about language models. The deai_removal and tic_enrichment applications are the ingest author's additions, not Locker's claims.

Response: Accepted and now explicit. All lane-tagged applications are marked as operator inference, not textbook content. The Locker source provides the craft heuristic; the lane application is an analytical overlay. This distinction was insufficiently clear in v1.

Objection 3: The passive-voice claim (C-005) was not merely wrong but reversed the direction of the effect, which should have triggered skepticism about the other RLHF claims.

Response: Accepted. C-005 is killed. The remaining RLHF claim (C-006, nominalization) survives because it has independent empirical support, but the error in C-005 warrants a general caution: the ingest author's intuitions about RLHF stylistic effects should not be trusted without empirical verification. Craft move 3b has been rewritten to remove the falsified passive-voice claim.

---

## 6\. Overconfidence Check

Pre-review, no claims scored 80+, so mandatory downward-pressure pass is not triggered. Post-review, the highest-confidence claim (C-006) scores 75 after calibration gate. Distribution is appropriate: 1 claim at 75, 4 verified at pedagogical-consensus level (not scored on empirical confidence scale), 2 zombie, 1 wrong, 1 unknown, 1 speculative, 1 inferred.

---

## 7\. Core Craft Moves — Extraction and Lane Tagging (Post-Review)

### 7a. Verb-heavy sentences over nominalization \[lane: both\]

Locker's item 4: nouns ending in -ment, -ion, -al often hide verbs.

| Nominalized (weak) | Verb-forward (better) |
| --- | --- |
| make an adjustment | adjust |
| make a decision | decide |
| reach a conclusion | conclude |
| take into consideration | consider |
| provide assistance | assist |

Craft move: When revising, scan for "make/perform/provide + noun" patterns — collapse to the verb.

deai_removal application \[operator inference, not Locker\]: Instruction-tuned LLMs nominalize at \~2x human rate \[C-006, verified\]. This craft move directly targets that residue.

tic_enrichment application \[operator inference\]: Verb-forward prose compresses sentence length and increases directness — structural borrow for voice priming.

Zombie-stat caveat: Locker's claim that verb-forward sentences are "up to 25% easier to read" (Q-007) cannot be traced to a primary source \[C-004, UNTESTED\]. The craft move stands on compositional logic, not on the quantitative claim.

### 7b. Active voice as default, passive as deliberate tool \[lane: both\]

Three situations where passive is acceptable:

1. Emphasize the object receiving the action ("Your order was shipped November 15")
2. Provide paragraph coherence by keeping old information as subject
3. Avoid assigning blame ("The order was damaged during shipment")

Craft move: Passive is not banned — it is reserved. The distinction matters for de-AI work because blanket "use active voice" rules produce mechanical rewrites. Locker's framework gives a principled test: does the passive serve emphasis, coherence, or tact?

deai_removal application \[CORRECTED\]: The v1 claim that "RLHF models default to passive hedging" is falsified \[C-005, WRONG\]. Empirical evidence shows instruction-tuned models use LESS agentless passive voice than humans (PMC 11874169). The de-AI application is therefore different from what v1 stated: when editing AI-generated text, the editor should expect FEWER passives than in human writing, not more. The Locker framework remains useful not for stripping AI passive (which is already rare) but for evaluating whether to ADD passive voice back in where it serves coherence or tact — restoring a human-like range of voice choices that AI text lacks.

### 7c. Connotation awareness and ethical word choice \[lane: tic_enrichment\]

Locker's positive/negative word pairs:

| Positive | Negative |
| --- | --- |
| assume | guess |
| curious | nosy |
| cautious | fearful |
| firm | obstinate |
| flexible | wishy-washy |

Craft move: Word choice carries attitude. The same behavior described with different connotation words produces different appraisals.

tic_enrichment application \[operator inference\]: Voice priming requires conscious connotation selection. When building a writer's word palette, map their habitual connotation choices — these are fingerprint-level voice markers.

### 7d. Eliminate wordiness — three strategies \[lane: deai_removal\]

Locker's condensation methods:

1. Eliminate words that add nothing ("Keep this information on file for future reference" → "File this information")
2. Combine sentences to eliminate redundancy
3. Put meaning into subject and verb to cut word count

Craft move: Wordiness is not length — concise writing can be long if packed with ideas. The test is whether the same idea can be expressed in fewer words.

deai_removal application \[operator inference\]: RLHF residue frequently manifests as filler phrases ("It is important to note that," "In order to," "It should be mentioned that"). Locker's condensation strategies provide a systematic method for stripping these without flattening content. Note: The filler-phrase claim is practitioner consensus \[speculative\], not empirically verified for specific phrases.

### 7e. Half-truths as nuanced craft rules \[lane: both\]

Locker identifies seven "half-truths" commonly taught as absolutes:

1. "Write as you talk" — OK for first draft, not final
2. "Never use I" — use it when describing your actions; avoid when self-centered
3. "Never use you" — fine for familiar audiences, benefits, sales; avoid in formal reports
4. "Never begin a sentence with And or But" — And as afterthought is weak; But as gear-shift is fine
5. "Never end a sentence with a preposition" — avoid in formal contexts, OK elsewhere
6. "Big words impress people" — they distance you and risk miscommunication
7. "Never have a sentence with more than 20 words, or a paragraph with more than 8 lines" — parallel clauses and bulleted lists can be clear at length

Craft move: Rules are context-dependent. Audience, purpose, and situation override mechanical prescriptions.

deai_removal application \[operator inference\]: The claim that RLHF encodes these half-truths as absolutes is \[speculative — C-011, UNTESTED\]. The framework remains useful as a heuristic for recognizing when a style "correction" is a genuine error versus a contextually appropriate choice.

tic_enrichment application \[operator inference\]: A writer's selective violation of these half-truths can be a voice signature \[C-012, inferred\]. Preserve it. \[esl_preserve\]: L1-influenced syntax that violates half-truth #4 or #7 is not an error requiring correction — it may be a legitimate structural choice.

### 7f. Style levels as audience-calibrated registers \[lane: tic_enrichment\]

Locker's three-register model (Figure 5.1):

| Feature | Conversational | Good business | Traditional term paper |
| --- | --- | --- | --- |
| Tone | Highly informal | Sounds like a real person | More formal, retains human voice |
| Contractions | Many | Occasional OK | Few if any |
| Pronouns | First/second person | First/second person | Minimized |
| Friendliness | Friendly | Friendly | No effort to be friendly |
| Words | Short, simple, slang | Short, simple, no slang | Abstract, scholarly |
| Sentences | Incomplete, short | Short sentences and paragraphs | Longer sentences and paragraphs |
| Grammar | Can be ungrammatical | Standard English | More formal standard English |

Craft move: "Good business style" is the target register for most workplace writing. Individual variation is expected and desirable.

---

## 8\. Coverage Attestation

Chapters attested: ch05 only.

Sections fully covered from attached export:

* Planning, Composing, and Revising (process overview)
* Using Your Time Effectively
* Brainstorming, Planning, and Organizing Business Documents
* Writing Good Business and Administrative Documents (style levels, Buffett example)
* Half-Truths about Business Writing (all 7)
* Ten Ways to Make Your Writing Easier to Read (items 1–5)

Sections not covered due to 80K truncation:

* Ten Ways items 6–10 \[speculative content excluded from Q-bank and craft moves\]
* Organizational patterns section
* Revising, editing, and proofreading detailed treatment
* Document design and visuals
* Summary and exercises

FR-3 enforced: No claims made from unread sections.

---

## 9\. Skill Incorporation Table (Post-Review)

| Skill / Move | Action | Lane | Rationale |
| --- | --- | --- | --- |
| Verb-forward sentence revision (collapse nominalizations) | KEEP | deai_removal | Targets verified RLHF nominalization habit (C-006, conf 75). Zombie-stat caveat on 25% claim noted |
| Passive voice: principled 3-case exception framework | KEEP | both | Locker's framework survives. The deai application is REVERSED from v1: AI text already underuses passive; the framework helps editors restore human-range passive where it serves coherence/tact |
| Connotation-pair mapping for voice fingerprinting | ADD | tic_enrichment | Locker's pairs provide a template for mapping writer-specific connotation habits |
| Three-register calibration model | KEEP | tic_enrichment | Aligns with existing register-awareness guidance |
| Wordiness condensation: 3-strategy method | KEEP | deai_removal | Reinforces filler-stripping guidance; "put meaning into subject+verb" is a specific technique. Filler-phrase targeting is practitioner consensus, not empirically verified |
| Half-truths as contextual rules | ADD | both | Permits selective violation as voice signature. RLHF-encoding claim is untested — use as heuristic only |
| Traditional outlining caution | CHANGE | both | Outlines are scaffolds, not contracts |
| \[esl_preserve\] Half-truth violations as legitimate L1 syntax | ADD | tic_enrichment | Some "violations" may reflect L1 transfer patterns; do not correct unless RLHF-corroborated |

---

## 10\. What Could Not Be Verified

* The 22% and 25% quantitative claims (C-003, C-004): would require access to Locker's endnotes and the original studies cited therein.
* The year of Buffett's "credit is like oxygen" quote (C-008): would require full-text search of all Berkshire Hathaway annual letters 2007–2010. Fetch tool truncated all four letters before the relevant section.
* Whether RLHF models encode specific half-truths as absolutes (C-011): would require a corpus analysis comparing model outputs against each half-truth rule.
* Whether RLHF filler phrases ("It is important to note that") are elevated relative to human writing: would require a controlled corpus study. The PMC study analyzed 66 Biber features but did not isolate these specific phrases.

Evidence that would change the assessment:

* A replication of the PMC nominalization study on Claude/Anthropic models (the study covered GPT-4o and Llama 3 only)
* Access to Locker's endnotes for the primary sources behind the 22% and 25% claims
* A full-text search confirming the Buffett quote location

---

## 11\. Downstream Handoff Notes

For Cursor implementation (implementor only — does not author ingests):

* Verb-forward revision: implement as a lint rule flagging "make/perform/provide + noun" patterns. Low ambiguity, high automation potential. Empirically grounded (C-006).
* Passive voice: do NOT implement as a blanket flag. Do NOT assume AI text overuses passive — the opposite is true. Implement as a contextual check: when passive is present, does it serve emphasis, coherence, or tact? If none, flag. Also flag passages that LACK passive where coherence or tact would benefit from it.
* Connotation mapping: requires human-in-the-loop. Cannot be automated without writer profile.
* Half-truth awareness: encode as a "rule override" system. When a style rule triggers, check whether the violation is a voice signature or an error. Requires writer profile context. The RLHF-encoding hypothesis (C-011) is untested — do not build automation on it.
* Truncation remediation: before implementing items 6–10, operator must supply full chapter export.