# Scholia SF-12 Ingest — Ginna, What Editors Do, Ch. 15

## Meta

| Field | Value |
| --- | --- |
| slug | ginna_what_editors_do |
| chapter_id | ch15 |
| chapter_title | Dukes, Deaths, and Dragons: Editing Genre Fiction |
| author | Diana Gill |
| book | Peter Ginna (ed.), What Editors Do (2017) |
| lane | both (deai_removal + tic_enrichment) |
| chapters_attested | ch15 only |
| word_count_target | SF-12 ≤ 4500w |
| corpus_role | Part IV genre-fiction editing; bounds ch14 slice end |
| P3_status | Adversarial review complete. 14 claims audited. |

---

## Iron Law Requirements

* FR-3 enforced: every claim below derives from the attached ch15 text only. No unread chapters, no web gap-fill.
* Gate A: all Q-bank quotes verified verbatim in attached text via file_search indexing.
* Evidence tags: \[chapter-stated\] for direct textual claims; \[inferred\] for analytical extrapolations; \[verified\] for claims checked against external sources this turn; \[speculative\] for plausible but unsupported claims.

---

## Source Discovery

Single-source ingest. Primary text only.

| Source | Tier | Provenance |
| --- | --- | --- |
| Diana Gill, "Dukes, Deaths, and Dragons," in Ginna (ed.) What Editors Do, Ch. 15 | Practitioner essay in edited professional volume. Confidence ceiling: 45 (expert opinion / case study only). | Attached file: 13_ginna_what_editors_do_ch15_ATTACH.txt |

No secondary sources searched per closed-corpus rule. Gill was Executive Editor at Ace/Roc Books (Berkley, Penguin Random House) and previously at HarperCollins (Harper Voyager US). The chapter is a practitioner essay, not peer-reviewed research.

---

## Adversarial Review — Claim Registry

### Load-bearing claims identified: 14

| ID | Claim | Source tag | Verification result | Failure mode |
| --- | --- | --- | --- | --- |
| C-001 | Gill's boredom prohibition is a named genre-editing principle | \[chapter-stated\] | Verbatim confirmed: "for genre fiction, boredom is the true deadly sin" | Gill states this as personal editorial principle, not industry standard. No evidence it is codified elsewhere. |
| C-002 | Storytelling and writing ability are separable and storytelling is primary for genre success | \[chapter-stated\] | Verbatim confirmed: "very strong storytelling (which is very difficult to teach and is not the same as writing ability)" | Gill asserts without citation. Third-party craft sources treat them as intertwined, not cleanly separable (see hightrestlepress.com craft essay). |
| C-003 | RLHF models tend to over-explain and over-describe | \[verified\] | Confirmed by multiple papers: Singhal et al. 2023 (arxiv 2310.03716); AAAI 2025 causal lens paper; ACL Findings 2024 DPO length paper; OpenReview verbosity bias paper. All confirm RLHF length bias / verbosity as a documented pattern. | Research covers summarization/dialogue tasks; fiction-specific RLHF verbosity is \[inferred\] from these, not directly studied. |
| C-004 | Convention-violation detection has "no direct analogue in literary fiction editing" | \[speculative\] — DOWNGRADED | Writer's Digest article on literary misdirection discusses implicit contracts in literary fiction. CreativeWritingAuthority piece explicitly describes "contract" logic in both literary and genre editing. The concept has analogues; what differs is codification, not existence. | Original claim was WRONG as stated absolutely. |
| C-005 | Ancillary Justice won Hugo, Nebula, and Clarke "all in the same year" | \[verified\] — OVERSTATED | Nebula: designated 2013, ceremony May 2014. Hugo: designated 2014, ceremony Aug 2014. Clarke: designated 2014, announced May 2014. All ceremonies occurred in calendar year 2014, but the Nebula is officially the "2013 Nebula." Gill's claim is defensible as colloquial but technically imprecise. | This is Gill's claim, not the ingest's. Ingest passed it through without flagging the ambiguity. |
| C-006 | Old Man's War published 2005 | \[verified\] | Wikipedia, ISFDB, WorldCat all confirm January 2005, Tor Books. | No failure mode. |
| C-007 | "Strongest brand in publishing" is an industry characterization of Lee Child / Reacher | \[verified\] | Forbes attribution confirmed via Penguin Random House page, UEA Lee Child Archive, SearchAmelia.com. Original source: Forbes, c. 2014. | Promotional characterization by Forbes, not empirical ranking. Gill's footnote marker ("2") suggests she was citing a specific source. |
| C-008 | Romance = 29% of fiction market in 2015 per Nielsen BookScan | \[verified\] — with caveats | Bustle.com infographic confirms "29% of the U.S. fiction market in 2015." Nielsen's own 2016 report discusses romance as major segment but foregrounds e-book share (20% of e-books). PW 2015 year-end shows romance down 9% in unit sales. The 29% figure appears to be share of fiction, not growth rate. Consistent with Gill's citation. | Nielsen methodology may count differently depending on inclusion of self-pub. Jane Friedman analysis shows self-pub adds \~25% to reported totals. The 29% may undercount total romance if self-pub excluded, or overcount if methodology differs from what Gill implies. \[ZOMBIE risk: 29% appears in secondary source (Bustle) citing Nielsen; I could not find it in primary Nielsen reports accessed this turn.\] |
| C-009 | Sorcerer to the Crown won British Fantasy Award Best Newcomer | \[verified\] | Zen Cho's author site, ISFDB, Pan Macmillan, Fantastic Fiction all confirm: British Fantasy Award for Best Newcomer (Sydney J. Bounds Award), 2016. PW starred review and Fall 2015 Top Picks also confirmed. | No failure mode. |
| C-010 | Gill was editor at "Ace Books (Penguin)" | \[verified\] — OVERSTATED | Reactor (reactormag.com) confirms Gill joined Ace/Roc as Executive Editor, April 2014, under Berkley/NAL. Berkley is under Penguin Random House, not "Penguin" alone. LinkedIn confirms PRH, not Penguin as standalone entity. | Imprecise corporate attribution in original ingest. |
| C-011 | Gill provides zero failed-edit case studies | \[chapter-stated\] | Confirmed by exhaustive re-read of ch15 text. All examples (Harrison, Kadrey, Cho, Scalzi, Leckie references) are successes. Only failure-adjacent mention: "Every editor has had to pass on projects he or she loves because the market was too difficult." | Correct as stated but understates: Gill acknowledges failed acquisitions, just not failed edits. |
| C-012 | Show-don't-tell in openings is "directly applicable to de-AI passes where RLHF models front-load context and explanation" | \[inferred\] | Chain: RLHF verbosity bias is \[verified\] (C-003). Gill's Sorcerer edit move — cut preamble, start in present action — is \[chapter-stated\]. The connection (RLHF front-loading maps to narrative front-loading) is plausible but untested. No study examines RLHF creative fiction specifically. | The analogy assumes RLHF fiction output structurally resembles the pre-edit Sorcerer manuscript. This is \[speculative\], not \[inferred\], because the structural similarity is assumed, not demonstrated. DOWNGRADED. |
| C-013 | Boredom prohibition gives genre-editing "pedigree" to trimming AI-smoothed prose | \[inferred\] | Chain: Boredom prohibition is \[chapter-stated\] (C-001). AI-smoothed prose as "pleasant but inert" is a characterization, not a finding. No study measures whether RLHF prose triggers reader boredom more than non-RLHF prose. | The chain has a gap: "inert" is asserted, not measured. DOWNGRADED to \[speculative\] pending evidence that RLHF creative fiction output registers as boring to readers. |
| C-014 | Confidence scores: 85 for boredom prohibition, 90 for Sorcerer case study | \[WRONG\] | Ceiling enforcement: source is expert opinion / case study only. Maximum allowable confidence: 45. Original scores of 85 and 90 violated the ceiling. | All scores in original document exceeded appropriate ceilings. |

---

## Kill List

| ID | Verdict | Sentence |
| --- | --- | --- |
| C-004 | OVERSTATED — survives with weaker scope | Literary fiction does have analogues to convention-violation detection (implicit reader contracts around interiority, ambiguity, epiphany); what differs is the degree of codification, not the existence of the skill. Retagged \[speculative\]. |
| C-005 | OVERSTATED — survives with annotation | Gill's "same year" is defensible colloquially (all ceremonies in 2014) but the Nebula is officially designated 2013. Ingest now annotates the ambiguity rather than passing through uncritically. |
| C-010 | OVERSTATED — survives with correction | "Ace Books (Penguin)" corrected to "Ace/Roc Books (Berkley, Penguin Random House)." |
| C-012 | OVERSTATED — survives as \[speculative\] | Downgraded from \[inferred\] to \[speculative\]. The RLHF-to-narrative-preamble analogy is plausible but structurally untested. |
| C-013 | OVERSTATED — survives as \[speculative\] | Downgraded from \[inferred\] to \[speculative\]. "Pleasant but inert" is a characterization, not a measured effect. |
| C-014 | WRONG — falsified | Original confidence scores (85, 90) violated the confidence ceiling for expert opinion / case study sources (max 45). All scores recalibrated. |

---

## Three Strongest Objections a Hostile Domain Expert Would Raise

1. Survivorship bias is structural, not incidental. Every craft prescription in this chapter derives from books that succeeded. Gill provides no analysis of books where she applied the same principles and they failed. The ingest treated this as a footnote; it should be a top-level epistemic limitation that qualifies every skill-incorporation recommendation. Accepted. Elevated.

2. The de-AI / RLHF bridge claims are the ingest author's analytical overlay, not Gill's. Gill says nothing about AI, RLHF, or machine-generated prose. The connections (iceberg principle maps to RLHF over-description; boredom prohibition maps to AI-smoothed flatness) are the ingest's extrapolations. These should be tagged \[speculative\] throughout, not \[inferred\], because the structural similarity between RLHF fiction output and the pre-edit manuscripts Gill describes has not been demonstrated. Accepted. All de-AI bridge claims downgraded to \[speculative\].

3. The "storytelling vs. writing ability" distinction (C-002) is presented as a discovery when it is actually a contested position. Gill asserts it without evidence. A hostile expert would cite counter-examples (Cormac McCarthy, Ursula Le Guin) where prose quality is inseparable from storytelling power, and argue Gill's framing privileges commercial genre aesthetics over craft. The ingest's original adversarial section noted this but did not downgrade the claim. Accepted. Claim retained as \[chapter-stated\] (it is what Gill says) but flagged as contested and not promoted to a skill-incorporation principle.

---

## Recalibrated Confidence Scoring

Ceiling enforced: all scores capped at 45 (expert opinion / case study only).

| Claim cluster | Score | Justification |
| --- | --- | --- |
| Boredom prohibition as genre prime directive | 40 | Single practitioner assertion. Consistent with genre-editing consensus \[speculative — no survey data\]. Ceiling 45; no replication. |
| Storytelling vs. writing ability distinction | 30 | Asserted without citation. Contested in literary-fiction discourse. Consistent with some practitioner opinion but no empirical basis. |
| Iceberg principle for world building | 40 | Well-established craft concept predating Gill. She applies it to genre editing specifically. No counter-evidence but no empirical test either. |
| Series-weighted market claim | 35 | Supported by 2015 Nielsen data cited in chapter. Market structure has shifted since 2015. \[RECENCY RISK\] |
| Convention/community engagement as differentiator | 35 | Practitioner observation. Consistent with industry knowledge but not empirically validated. Genre vs. literary community engagement differences are assumed, not measured. |
| Sorcerer case study editorial moves | 45 | First-person practitioner account of her own editing. High credibility for process claims (she did what she says she did). But survivorship bias: we see only the successful outcome. |
| RLHF verbosity bias (external claim) | 40 | Multiple papers confirm length bias in RLHF. However, all studies cover summarization/dialogue, not fiction. Fiction-specific RLHF verbosity is \[inferred\], not directly demonstrated. Ceiling 45 for cross-domain extrapolation. |

Overconfidence check: 0 of 7 scores are 80+. No downward-pressure pass required.

---

## Revised Concept Extraction

### C-01. The Boredom Prohibition (genre prime directive)

* "for genre fiction, boredom is the true deadly sin" \[chapter-stated\]
* Genre competes against all entertainment forms; the editor's first test is whether she cannot put the manuscript down \[chapter-stated\]
* De-AI connection: RLHF-smoothed prose may tend toward flatness that would fail the boredom test. \[speculative — no direct evidence that RLHF fiction output triggers reader boredom; the structural analogy is untested\]

### C-02. Storytelling vs. Writing Ability (contested distinction)

* Gill explicitly separates them: "very strong storytelling (which is very difficult to teach and is not the same as writing ability)" \[chapter-stated\]
* This is Gill's assertion, not an established finding. Counter-examples exist where prose quality and storytelling are inseparable. \[chapter-stated but contested\]
* Not promoted to skill-incorporation principle. Retained as context.

### C-03. Convention Literacy

* Each genre has "rules, or at least expectations" forming an implicit reader contract \[chapter-stated\]
* The editor must know "which ones must be kept and which can be broken" \[chapter-stated\]
* Innovation operates within convention: Scalzi's Old Man's War (2005, Tor Books \[verified\]) succeeded by referencing Heinlein while being accessible to new readers \[chapter-stated\]
* Convention-violation detection exists in literary fiction editing too (implicit contracts around interiority, epiphany, ambiguity) \[verified via external sources\]. What differs is degree of codification, not existence. \[speculative\]

### C-04. The Iceberg Principle (world building)

* "Genre editors work with their authors to avoid showing the dreaded 'iceberg'" \[chapter-stated\]
* World building "must serve the story" \[chapter-stated\]
* De-AI connection: RLHF models exhibit documented length/verbosity bias \[verified, multiple papers\]. Whether this maps structurally to narrative over-exposition in fiction is \[speculative\].

### C-05. Series Architecture

* Genre fiction "typically published in series" \[chapter-stated\]
* Stand-alone novels work but market "very strongly weighted toward series or linked novels" \[chapter-stated\]
* Lee Child / Reacher: "the strongest brand in publishing" — attributed to Forbes, c. 2014 \[verified\]
* Editor's series duties: continuity of story, world, character evolution \[chapter-stated\]

### C-06. Case Study: Sorcerer to the Crown (Zen Cho)

Editorial moves documented (all \[chapter-stated\], high credibility for process claims):

| Move | Description |
| --- | --- |
| Opening tightening | "sharpening the opening chapters so that the story started more quickly, showing the hero's predicament rather than telling it in numerous conversations" |
| Heroine intro cut | Cut introductory chapter that was "more preamble and in the past" so present-timeline introduction had "more impact" |
| Character motivation work | Developed heroine's "goals and motivations throughout the story" |
| Relationship development | "narrative space we gained was used to more fully develop the main relationship" |
| Hero arc development | Hero's "motives and issues were more fully developed within the story arc" |
| Edit level | "more on the level of story/concept/characters/pacing than line-by-line revision" |

External verification: PW starred review confirmed \[verified\]. British Fantasy Award Best Newcomer (Sydney J. Bounds Award, 2016) confirmed \[verified\]. Published by Ace/Berkley (Penguin Random House), Sept 2015 \[verified\].

Survivorship caveat: this is a success story. No data on how often these same editorial moves fail to produce commercially or critically successful outcomes.

### C-07. Ancillary Justice Awards

* Gill: "won the Hugo, Nebula, and Arthur C. Clarke Awards all in the same year" \[chapter-stated\]
* Technically: Nebula designated 2013 (ceremony May 2014), Hugo designated 2014 (ceremony Aug 2014), Clarke designated 2014 (announced May 2014). All ceremonies in calendar year 2014. "Same year" is colloquially defensible but officially the Nebula is the 2013 award. \[verified with annotation\]

---

## Gate A — Verbatim Q-Bank

All quotes verified present in attached ch15 text via file_search.

| ID | Quote | Section anchor | Verified |
| --- | --- | --- | --- |
| Q-001 | "for genre fiction, boredom is the true deadly sin" | Opening section | Yes |
| Q-002 | "very strong storytelling (which is very difficult to teach and is not the same as writing ability)" | Opening section | Yes |
| Q-003 | "Genre editors work with their authors to avoid showing the dreaded 'iceberg'" | World building section | Yes |
| Q-004 | "which ones must be kept and which can be broken" | Convention literacy section | Yes |
| Q-005 | "sharpening the opening chapters so that the story started more quickly, showing the hero's predicament rather than telling it in numerous conversations" | Sorcerer case study | Yes |
| Q-006 | "more on the level of story/concept/characters/pacing than line-by-line revision, as the writing was very strong to start" | Sorcerer case study | Yes |
| Q-007 | "if you as an editor are being paid to read a submission and do not love it . . . how can you convince the rest of the house to love it" | Acquiring section | Yes |
| Q-008 | "the strongest brand in publishing" | Series / Lee Child section | Yes |

---

## Revised Skill Incorporation Table

Survivorship bias caveat applies to all KEEP and ADD rows: these skills derive from success-only evidence.

| Skill / Principle | Action | Lane | Rationale | Epistemic status |
| --- | --- | --- | --- | --- |
| Iceberg principle — cut over-explained world-building | KEEP | deai_removal | Named craft principle for trimming over-description. Predates Gill; she provides genre-editing application. Connection to RLHF over-description is \[speculative\], not \[inferred\]. | \[chapter-stated\] principle; \[speculative\] de-AI bridge |
| Show-don't-tell in openings (Sorcerer case) | KEEP | both | Concrete before/after from genre editing. Cut preamble, start in present action. Analogy to RLHF front-loading is \[speculative\]. | \[chapter-stated\] principle; \[speculative\] de-AI bridge |
| Convention-violation detection | CHANGE (was ADD) | tic_enrichment | Not new — literary fiction has analogous implicit-contract editing. What Gill adds: genre conventions are more codified, making violation detection more systematic. Useful for voice work where operator decides which reader expectations to honor vs. subvert. | \[chapter-stated\] genre version; \[verified\] that literary analogue exists |
| Boredom-as-deadly-sin test | KEEP | both | Useful as a named test during revision passes. Single-practitioner assertion, consistent with genre consensus. | \[chapter-stated\]; no empirical basis |
| Voice-overrides-preference (Sandman Slim anecdote) | KEEP | tic_enrichment | Reframed for revision: test whether a convention violation is load-bearing before removing it. Maps to \[esl_preserve\] logic. | \[chapter-stated\] anecdote |
| Series continuity tracking | DROP | n/a | Mechanical skill for multi-book projects. Outside current scope. | n/a |
| Community engagement / marketing | DROP | n/a | Outside prose-level craft scope. | n/a |
| Trend-timing market analysis | DROP | n/a | Acquisition skill, not editing skill. | n/a |

---

## Epistemic Rigor

### Survivorship Bias Audit — ELEVATED TO STRUCTURAL LIMITATION

Every craft prescription in this chapter derives from books that succeeded commercially or critically. Gill provides no analysis of:

* Books where she applied these same principles and they failed
* Base rates for genre acquisition success
* How often "iceberg" cuts, preamble removal, or convention-breaking produce worse outcomes

This is not a minor footnote. It means every skill-incorporation recommendation carries an implicit "conditional on having selected the right manuscript in the first place." The editorial moves may be necessary but not sufficient, or they may be incidental to success driven by other factors (market timing, author platform, luck).

### De-AI Bridge Claims — ALL DOWNGRADED TO \[SPECULATIVE\]

The ingest's highest-value claims for the operator are the connections between Gill's craft principles and RLHF residue patterns. These connections are the ingest author's analytical overlay. Gill says nothing about AI or machine-generated prose. The structural analogies (RLHF over-description maps to iceberg violations; RLHF front-loading maps to narrative preambles) are plausible but:

* No study examines RLHF creative fiction output specifically
* The verbosity bias literature covers summarization and dialogue tasks
* Whether RLHF fiction registers as "boring" to readers is unmeasured

These claims may be promoted to \[inferred\] if future research demonstrates RLHF fiction-specific verbosity patterns. Until then: \[speculative\].

### Contested Claims Flagged

* Storytelling vs. writing ability: Gill's binary is a practitioner assertion, not a finding. Not incorporated as a skill principle.
* "No direct analogue in literary fiction": Falsified. Literary fiction has implicit-contract editing. Claim corrected.

### Gaps / Unknowns

* No discussion of developmental editing mechanics (edit letter format, inline comment practices)
* No editor-agent dynamic analysis specific to genre
* Line editing explicitly deemphasized — no line-level craft moves extractable
* Self-publishing impact on editing standards mentioned only as acquisition signal
* No data on what percentage of genre acquisitions succeed commercially
* No evidence on whether Gill's editorial moves are replicable by other editors on other manuscripts

### What Would Change the Assessment

* A study of RLHF verbosity in creative fiction tasks (not summarization) would promote C-003's fiction applicability from \[speculative\] to \[inferred\]
* A reader-response study measuring boredom in RLHF-generated fiction vs. human fiction would promote C-013 from \[speculative\] to \[inferred\]
* Failed-edit case studies from Gill or comparable genre editors would allow assessment of base rates and whether these moves are necessary/sufficient
* Replication of Gill's editorial process by a different editor on a different manuscript with documented outcomes would raise the Sorcerer case study from N=1

---

## Post-Review Synthesis

Usable findings, restricted to \[verified\] and post-test \[speculative\]-with-explicit-caveats:

### For deai_removal lane

1. The iceberg principle is a named, source-backed craft principle for cutting over-description. It predates Gill and has genre-editing pedigree. Its connection to RLHF over-description is \[speculative\] — the structural analogy is plausible but undemonstrated in fiction contexts. Operator should use the principle on its own merits, not as AI-specific authority.

2. The boredom prohibition names a test: does the prose sustain engagement? This is Gill's practitioner standard, not an empirical threshold. It can function as a revision heuristic without claiming special authority over AI-generated text.

### For tic_enrichment lane

1. Convention-violation detection is a systematic genre-editing skill that has looser analogues in literary fiction editing. Gill's contribution: genre conventions are codified enough that violation detection can be proceduralized — identify the convention, assess whether the violation is intentional and load-bearing, decide whether to keep or cut. This proceduralization (not the concept itself) is the borrowable skill.

2. Voice-overrides-preference (Sandman Slim): when a strong voice violates the editor's default preferences, test whether the violation serves the work before removing it. Maps to \[esl_preserve\] logic — L1-influenced syntax may violate "standard" conventions but serve voice.

### For both lanes

1. Sorcerer to the Crown case study provides a concrete editorial sequence: tighten openings by showing not telling, cut preamble chapters, develop character motivation into vacated space. These are individually unremarkable craft moves; their value is the documented sequence and the principle that structural editing can create space for character work. Survivorship-biased.

2. The storytelling-vs-writing distinction is Gill's assertion, not a skill. It warns against over-polishing at the sentence level at the expense of narrative-level qualities, but the binary framing is too crude for skill incorporation.

---

## Coverage Attestation

chapters_attested: ch15 only

No claims in this ingest derive from chapters 1-14 or 16-18+ of What Editors Do. Chapter 16 (Weiland) and Chapter 17 (Siscoe) text appears in the attached file but is excluded per FR-3.