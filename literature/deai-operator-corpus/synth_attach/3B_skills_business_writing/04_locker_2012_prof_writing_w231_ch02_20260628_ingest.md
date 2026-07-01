# Ingest: Locker 2012 — Ch02 Adapting Your Message to Your Audience

slug: locker_2012_prof_writing_w231_ch02 schema: scholia SF-12 chapter ingest chapters_attested: ch02 only lane: tic_enrichment (primary), deai_removal (secondary) operator: Wei Jia · L1 Chinese · ESL fairness mandatory stakes: L3 source: Locker, Kitty O. Business and Administrative Communication, 10th ed. McGraw-Hill, 2012. Chapter 2. corpus: deai-operator-corpus truncation_note: Attachment truncated at 80,000 chars. Coverage based on visible text only; sections after truncation point are marked \[TRUNCATED — NOT ATTESTED\]. review_status: ADVERSARIAL REVIEW COMPLETE — 2026-06-28

---

## Iron Law Requirements

* FR-3 enforced: all claims sourced from attached ch02 text only; no external chapter content used.
* Gate A: all verbatim quotes verified against attached export.
* Two-lane tags applied to every craft move.
* Canon inherited; not re-litigated.
* ESL preserve rules active.

---

## Source Discovery

Single source, closed corpus:

| Field | Value |
| --- | --- |
| Source | Locker 2012, Business and Administrative Communication, 10e, Ch02 |
| Tier | Tier 1.5 — established business communication textbook, widely adopted in US undergraduate/MBA programs |
| Provenance | Attached chapter export: 06_locker_2012_prof_writing_w231_ch02.txt |
| Coverage | pp. 29–42+ (truncated mid-page \~42); major sections on audience taxonomy, analysis methods, channel selection, six adaptation questions, audience analysis examples |
| Gaps | Post-truncation content (likely: audience benefits detail, summary exercises, chapter-end cases) — marked \[TRUNCATED — NOT ATTESTED\] |

---

## Adversarial Review: Claim Register

### Load-Bearing Claims

C-001: Locker's audience taxonomy contains 5 types (gatekeeper, primary, secondary, auxiliary, watchdog). Tag: \[verified\] — confirmed against attached text and Locker BAC 12e instructor manual \[renrendoc.com\]. The Scribd-hosted BAC notes add "initial audience" as a sixth term; the attached ch02 text does not define "initial audience" as a separate named type in the truncated portion. However, my original document header listed "5 types" while the body text listed 6 terms including "initial." REVISION: The attached text references someone who first receives the message (consistent with "initial audience" in other editions), but the visible text defines five named roles: gatekeeper, primary, secondary, auxiliary, watchdog. I count what the attached text explicitly names. Failure mode: The truncated portion may contain an explicit "initial audience" definition. If so, the count becomes 6.

C-002: MBTI validity is contested in I/O psychology. Tag: \[verified\] — Pittenger 2005, Consulting Psychology Journal 57(3):210 \[doi.org/10.1037/1065-9293.57.3.210, Gate A: 200 OK via doi.org redirect; Gate B: abstract confirms "cautionary comments" and psychometric limitations\]. Also confirmed by Randall 2017 systematic review \[gwern.net/doc/psychology/personality/2017-randall.pdf, Gate A: 200 OK; Gate B: reports "satisfactory reliability for 3 of 4 subscales" but "limited samples" and "caution warranted"\]. Also 25-year synthesis \[doi.org/10.1002/jcad.70006, Gate A: 200 OK; Gate B: "aggregate evidence since 1999 is less supportive... than the manual suggested"\]. Failure mode: MBTI defenders could argue reliability is adequate for developmental (non-selection) use. This does not change the finding that Locker presents MBTI uncritically.

C-003: The "discourse community" concept originates from Swales (1990), not Locker. Tag: \[verified\] — Swales 1990, Genre Analysis, Cambridge UP. Six defining characteristics confirmed \[mjreiff.com/uploads Swales PDF, Gate A: 200 OK; Gate B: six characteristics listed verbatim\]. Locker's definition (Q-003) is a simplified pedagogical adaptation of Swales. Locker does not cite Swales in the visible text. Failure mode: None material. Attribution is clear.

C-004: "Some 75% of US managers are judging" (Locker's claim, Q-004). Tag: \[speculative — ZOMBIE STAT\] — I could not trace this to an independent primary source with described methodology. The closest match is DeWald 1986 (n=30 paired executives, single organization) showing \~73-79% Judging among Type A executives \[scholarworks.wmich.edu, Gate A: 200 OK; Gate B: "About 80% of both military and civilian executives were Thinking-Judgers"\]. Gardner & Martinko 1996 literature review notes TJ types are "overrepresented" among managers but provides no single 75% figure \[sagepub.com, Gate A: 200 OK; Gate B: describes overrepresentation without specific percentage\]. The 75% figure likely originates from CPP/Myers-Briggs Company publisher data, which has COI (publisher reporting its own instrument's results). Cannot verify independently. Failure mode: The stat may exist in MBTI manual normative tables (not publicly accessible), but those tables are publisher-produced with no independent replication at this sample claim level. \[ZOMBIE\] — appears only in secondary/textbook sources.

C-005: "Nearly 80% of U.S. managers who are thinking types" (Locker's claim, Q-005). Tag: \[speculative — ZOMBIE STAT\] — Same provenance problem as C-004. DeWald 1986 reports \~80% TJ but n=30 in a single military/civilian org. The Freeman library review notes "many studies had limited TF variability (most managers were Ts)" but this is a methodological artifact, not a population parameter. No independent large-sample study confirms "nearly 80%." Failure mode: Same as C-004.

C-006: RLHF filler phrases ("certainly," "great question," "I'd be happy to") function as credibility-damaging signals for sophisticated readers. Tag: \[verified\] — Wu et al. 2026, "The Rise of Verbal Tics in Large Language Models," arXiv:2604.19139 \[Gate A: 200 OK; Gate B: abstract names "sycophantic openers (That's a great question!, Awesome!)" and "pseudo-empathetic affirmations" explicitly; reports r = -0.87 between sycophancy and perceived naturalness, p < 0.001, N=120\]. Also confirmed by practitioner tools (unslop GitHub, CleanTextTools) codifying removal of these exact phrases. \[RECENCY RISK — paper is April 2026, within 12 months of training cutoff.\] Failure mode: The Wu et al. study's human evaluation sample is small (N=120) and the paper is unreplicated as of this review. Confidence ceiling: single study, unreplicated → max 70.

C-007: RLHF residue constitutes a "discourse community violation" per Swales/Locker framework. Tag: \[inferred\] — Chain: (a) Swales defines discourse communities by shared genre norms \[C-003, verified\]; (b) RLHF-trained models produce a uniform "helpful assistant" register regardless of target genre \[C-006, verified\]; (c) therefore RLHF output violates genre norms of most target discourse communities. Also supported by dspace.mic.ul.ie study showing "register/genre violations as predictors of underperformance in writing assessments" \[Gate A: 200 OK; Gate B: confirms "potential register/genre violations as predictors of underperformance"\]. Failure mode: The inference equates "writing that sounds AI-generated" with "discourse community violation." These overlap but are not identical. A discourse community that has normalized AI-assisted writing would not treat RLHF register as a violation. The claim assumes the target community rejects AI register — which is true for the operator's use case but not universal. SCOPE RESTRICTION APPLIED.

C-008: Face-saving is a strength area for L1 Chinese writers, not a deficit. Tag: \[verified\] — Lee 2018, "Chinese Culture, Language, and L1 and L2 Speech Act Production" \[Springer, link.springer.com/chapter/10.1007/978-981-10-8980-0_3, Gate A: 200 OK; Gate B: confirms "Face-saving (miànzi) as a central driver in pragmatic decisions and polite behavior in Chinese communication"\]. Also: 2025 study on transfer effects \[doi.org/10.54254/2753-7048/2025.nd24829, Gate A: 200 OK; Gate B: confirms "Chinese facework considerations (face-saving sensitivity) positively transfer to English pragmatic choices" — positive pragmatic transfer, not deficit\]. Failure mode: Individual variation among L1 Chinese speakers is high. "L1 Chinese = strong at face-saving" is a population-level generalization. The esl_preserve tag correctly prevents treating this as universal.

C-009: Locker's "discourse community" concept provides theoretical grounding for why RLHF residue sounds wrong. Tag: \[inferred\] — Chain: C-003 (Swales concept verified) + C-007 (RLHF as genre violation, inferred with scope restriction). This is an analogy, not a verified theoretical mapping. Locker's textbook was written in 2012; it does not address AI-generated text. The bridge is constructed by this ingest, not found in the source. Failure mode: The analogy is productive but could overstate Locker's relevance. Locker provides vocabulary (discourse community, genre norms) that can be applied to the RLHF problem, but Locker did not theorize this application. Reframed accordingly.

C-010: The six adaptation questions (Figure 2.3) have pedagogical utility as a pre-writing checklist. Tag: \[speculative\] — No empirical validation of this specific checklist as a unit was found. Each individual question is defensible on face validity, but the composite has not been tested. Textbook adoption is not evidence of effectiveness. Failure mode: Widely adopted ≠ empirically validated. Confidence ceiling: expert opinion / case study only → max 45.

C-011: Locker's channel selection framework (written for complex data, oral for emotion/consensus) reflects sound principles. Tag: \[speculative\] — This is practitioner conventional wisdom. No citation to empirical media-richness research (e.g., Daft & Lengel 1986) appears in the visible text. The principles are directionally plausible but the specific claims are not source-traced. Failure mode: Media richness theory itself has mixed empirical support. Locker's simplified version lacks nuance about synchronous digital channels.

C-012: NAAL found 30 million US adults at "below basic" prose literacy. Tag: \[verified\] — NCES Commissioner's remarks, Dec 15 2005 \[nces.ed.gov/whatsnew/commissioner/remarks2005/12_15_2005.asp, Gate A: 200 OK; Gate B: "30 million U.S. adults had Below Basic prose literacy"\]. Data is from 2003 NAAL, published 2006. Locker's attribution is accurate. Failure mode: Data is from 2003. Current literacy levels may differ. \[RECENCY RISK\] already flagged.

C-013: Generational stereotypes (Figure 2.2) are oversimplified. Tag: \[inferred\] — Based on the general methodological critique that generational cohort research suffers from confounding age, period, and cohort effects. No specific falsification test run against Locker's Figure 2.2 claims. The recommendation to DROP specifics while keeping the meta-principle is conservative and defensible. Failure mode: Some generational differences in communication preferences may be real (e.g., channel preferences). The DROP recommendation may be too aggressive for channel-specific claims.

C-014: Locker's red-flag words principle can be inverted to apply to RLHF filler. Tag: \[inferred\] — Chain: Locker says avoid words that "create an immediate negative response" (Q-bank, §5b); RLHF filler creates negative credibility response in sophisticated readers \[C-006, verified\]. The structural parallel holds. The inversion is a novel application constructed by this ingest. Failure mode: Locker's red-flag principle targets emotional valence (political/ideological triggers). RLHF filler triggers credibility/authenticity concerns, a different mechanism. The analogy holds structurally (both are audience-alienating word choices) but the psychological mechanisms differ. SCOPE NOTE added.

---

## Kill List

| Claim | Verdict | Disposition |
| --- | --- | --- |
| C-001 original: "5 types" with 6 terms listed | OVERSTATED | Body text corrected: 5 explicitly named types in visible text (gatekeeper, primary, secondary, auxiliary, watchdog). "Initial audience" appears in other editions but is not separately defined in the truncated portion. |
| C-004: 75% of US managers are judging | OVERSTATED | Zombie stat. Traceable only to MBTI publisher data and small-n studies. Retained as "Locker's textbook claim" with \[ZOMBIE STAT\] flag; not usable as independent evidence. |
| C-005: \~80% of US managers are thinking types | OVERSTATED | Same disposition as C-004. |
| C-009 original framing: discourse community "provides theoretical grounding" for RLHF problem | OVERSTATED | Reframed: discourse community provides useful vocabulary and a productive analogy. It does not provide theoretical grounding — Locker's 2012 textbook predates the RLHF phenomenon. |
| C-010 original confidence 80 | OVERSTATED | Dropped to 45. No empirical validation of the six-question checklist as a unit. |
| C-011 original confidence 70 | OVERSTATED | Dropped to 40. No source-traced empirical support in visible text. |

---

## Hostile Expert Objections

Objection 1: "You're retrofitting a 2012 business-writing textbook onto a 2025+ AI-writing problem. The theoretical connection is forced."

Response: Partially accepted. The discourse-community concept (Swales 1990, adapted by Locker) predates AI writing by decades, but it describes a real phenomenon: genre norms vary by community, and violations are detectable and penalized. RLHF register is a specific modern instance of genre-norm violation. The connection is an analogy, not a derivation. All craft moves now carry explicit scope tags distinguishing "structural borrow from Locker" versus "novel application to RLHF." No claim that Locker anticipated or theorized about AI writing.

Objection 2: "The ESL-preserve claims about L1 Chinese face-saving are essentializing. Not all L1 Chinese speakers share the same pragmatic competence."

Response: Accepted as a valid concern. C-008 is verified at the population level (Lee 2018; positive pragmatic transfer research), but individual variation is high. The esl_preserve tag already prevents universalizing. Added explicit caveat: "population-level generalization; individual assessment required." The craft move (CM-T3) is framed as "validate existing competence if present" not "assume competence because L1 Chinese."

Objection 3: "Your MBTI confidence score of 55 was too generous. The instrument's construct validity is weak, and Locker's uncritical presentation should be flagged harder."

Response: Accepted. Downgraded from 55 to 40. The 25-year psychometric synthesis \[doi.org/10.1002/jcad.70006\] found "aggregate evidence since 1999 is less supportive of MBTI-M psychometrics than the manual suggested." Convergent validity effect sizes are small-to-moderate (r ≤ \~0.30). The S-02 row already recommended CHANGE (extract meta-principle, drop MBTI as instrument). Confidence score now reflects this more accurately.

---

## Overconfidence Check

Original scores 80+: Audience taxonomy (85), Six adaptation questions (80). Post-review: 2 of 5 original scores were 80+. This is 40%, below the 50% trigger. However, I run the downward-pressure pass anyway because both scores relied on "widely adopted" as evidence, which is not empirical validation.

Audience taxonomy (85 → 75): Strongest argument for -10: The taxonomy is a pedagogical heuristic, not derived from empirical communication research. It organizes common sense into categories. Its value is mnemonic, not predictive. Other biz-comm textbooks use different audience categorizations (e.g., Bovee & Thill use a different schema). Argument succeeds partially — the taxonomy is useful but not uniquely validated. Score: 75.

Six adaptation questions (80 → 45): Strongest argument for -10 (applied -35): No empirical study validates these six questions as a unit. The checklist has face validity only. Other checklists with different questions could serve equally well. Confidence ceiling for expert opinion: max 45. Applied.

---

## Confidence Scoring (post-review)

| Claim domain | Confidence | Justification |
| --- | --- | --- |
| Audience taxonomy (5 named types) | 75 \[c1=80, c2=70, c3=75\] | Standard taxonomy; consistent across Locker editions; no empirical validation as a unit; other textbooks use different schemas. Pedagogical heuristic, not predictive model. |
| Myers-Briggs as audience analysis tool | 40 \[c1=35, c2=40, c3=45\] | MBTI convergent validity weak (r ≤ 0.30 per 25-year synthesis). Locker's specific manager percentages (75% J, 80% T) are zombie stats. Heuristic value of "adapt to processing style" survives; MBTI as instrument does not. |
| Six adaptation questions (Figure 2.3) | 45 \[c1=50, c2=40, c3=45\] | Face validity only. No empirical test of this specific checklist. Confidence ceiling: expert opinion → max 45. |
| Channel selection framework | 40 \[c1=45, c2=35, c3=40\] | Practitioner conventional wisdom. No citation to media-richness literature in visible text. Dated examples. Structural logic is plausible but unsourced. |
| NAAL literacy statistics | 65 \[c1=70, c2=60, c3=65\] | Verified against NCES primary source. Data from 2003. \[RECENCY RISK\]. |
| RLHF filler as credibility signal | 65 \[c1=70, c2=55, c3=70\] | Wu et al. 2026 (N=120, r=-0.87). Single study, unreplicated. Confidence ceiling: 70. Reduced to 65 for small N. \[RECENCY RISK\]. |
| Face-saving as L1 Chinese strength | 60 \[c1=65, c2=55, c3=60\] | Multiple cross-cultural pragmatics sources confirm positive pragmatic transfer. Population-level; individual variation high. |

---

## Trustworthiness Assessment

| Factor | Assessment |
| --- | --- |
| Source type | Tier 1.5 — widely adopted textbook; pedagogical authority, not original research |
| Methodology | Textbook synthesis; cites primary sources (NAAL, Myers-Briggs, WSJ articles) but does not conduct original studies |
| Conflicts of interest | Standard textbook commercial incentive; no unusual conflicts |
| Survivorship bias | Success examples (Amazon, Nintendo Wii, Zappos) are all winners; no failed audience-analysis cases presented |
| Recency | 2012 publication; many examples from 2007–2011. Channel/technology examples are significantly dated. Structural principles have indeterminate shelf life. |
| Specificity | Good — provides concrete checklists, taxonomies, and named examples |
| Replication | Core frameworks appear across multiple biz-comm textbooks but are not empirically replicated in the scientific sense |

---

## Chapter Structure Map

1. Audience taxonomy — 5 named types: gatekeeper, primary, secondary, auxiliary, watchdog
2. Ways to analyze your audience
  * Analyzing individuals (Myers-Briggs framework)
  * Analyzing members of groups (demographics, psychographics)
  * Analyzing organizational culture and discourse community
3. Choosing channels to reach your audience (written vs. oral; creative channels)
4. Using audience analysis to adapt your message — 6 questions (Figure 2.3)
  * Initial reaction
  * Information needs
  * Obstacles
  * Positive aspects
  * Expectations (language, content, organization)
  * Document use conditions
5. Audience analysis works — success examples
6. \[TRUNCATED — NOT ATTESTED\] — likely audience benefits, summary, exercises

---

## Gate A — Verbatim Q-Bank (ch02 only)

Q-001: "Empathy is the ability to put yourself in someone else's shoes, to feel with that person." (§ Ways to Analyze Your Audience, p. 29)

Q-002: "Organizational culture is a set of values, attitudes, and philosophies." (§ Analyzing the Organizational Culture and the Discourse Community, p. 32)

Q-003: "A discourse community is a group of people who share assumptions about what channels, formats, and styles to use for communication, what topics to discuss and how to discuss them, and what constitutes evidence." (§ Analyzing the Organizational Culture, p. 32)

Q-004: "Putting the main point up front satisfies the needs of judging types, and some 75% of US managers are judging." (§ Analyzing Individuals, p. 30) \[ZOMBIE STAT — see C-004\]

Q-005: "Giving logical reasons satisfies the needs of the nearly 80% of U.S. managers who are thinking types." (§ Analyzing Individuals, p. 30) \[ZOMBIE STAT — see C-005\]

Q-006: "Demographic characteristics are measurable features that can be counted objectively: age, sex, race, religion, education level, income, and so on." (§ Analyzing Members of Groups, p. 30)

Q-007: "Psychographic characteristics are qualitative rather than quantitative: values, beliefs, goals, and lifestyles." (§ Analyzing Members of Groups, p. 31)

Q-008: "A communication channel is the means by which you convey your message." (§ Choosing Channels, p. 33)

Q-009: "If you know your audience well and if you use words well, much of your audience analysis and adaptation will be unconscious." (§ Using Audience Analysis to Adapt Your Message, p. 36)

Q-010: "People who have already made up their minds are highly resistant to change." (§ Obstacles, p. 39)

---

## Skill Incorporation Table

| ID | Locker Principle | Operator Skill Mapping | Action | Lane | Notes |
| --- | --- | --- | --- | --- | --- |
| S-01 | Audience taxonomy: 5 named types | Map to voice-register switching: different audiences require different register calibration, not different "personalities" | KEEP | tic_enrichment | Useful framing for multi-audience documents. Operator already does implicit register-switching; this gives it vocabulary. |
| S-02 | Myers-Briggs personality adaptation (Figure 2.1) | CHANGE: Extract the structural move (adapt to receiver processing style) while dropping MBTI as instrument | CHANGE | tic_enrichment | MBTI validity weak \[verified, C-002\]. Specific manager percentages are zombie stats \[C-004, C-005\]. The meta-principle "match message structure to audience processing" is sound independent of MBTI. Decouple completely. |
| S-03 | Discourse community analysis | Map to deai_removal: RLHF register violates most real discourse communities by defaulting to "helpful assistant" genre regardless of target norms. This is a productive analogy, not a derivation — Locker predates the RLHF phenomenon. | ADD | both | Vocabulary borrow, not theoretical derivation. Swales (1990) is the primary theorist; Locker simplifies for pedagogy. |
| S-04 | "As you know" / subordinate clause technique | Structural borrow: presupposition framing controls information hierarchy without condescension | KEEP | tic_enrichment | \[esl_preserve\] — L1 Chinese writers may use different presupposition markers; don't force English-native phrasing. Structural principle transfers cross-linguistically. |
| S-05 | "Red flag" words avoidance | Map to deai_removal: RLHF filler triggers credibility concerns via a different mechanism (authenticity, not political valence) but the structural parallel holds — both are audience-alienating word choices. | ADD | deai_removal | Analogy, not identity. Locker's mechanism: emotional valence. RLHF mechanism: authenticity/credibility. Both result in audience rejection. |
| S-06 | Channel selection: written for complex data, oral for emotion | KEEP as background knowledge for voice-register decisions | KEEP | tic_enrichment | Empirical basis is weak \[C-011, confidence 40\] but the heuristic is non-harmful as a starting orientation. |
| S-07 | Organizational culture diagnostic questions | Map to tic_enrichment: voice priming should account for organizational register | ADD | tic_enrichment | Practical: diagnose org culture before calibrating voice. |
| S-08 | Six adaptation questions (Figure 2.3) as pre-writing checklist | KEEP as diagnostic heuristic; no empirical validation \[C-010\]. Adapt for deai pre-pass: ask "who is the audience and what register do they expect?" before removing AI signals. | KEEP | both | Prevents over-correction. Face validity only — treat as heuristic, not validated instrument. |
| S-09 | Generational communication preferences (Figure 2.2) | DROP specific generational stereotypes (dated, methodologically weak). KEEP meta-principle: audience cohort affects channel/formality expectations. | DROP (specifics) / KEEP (meta) | tic_enrichment | Cohort-period-age confounding undermines specific claims. |
| S-10 | Face-saving when correcting audience knowledge | High-value structural borrow. \[esl_preserve\] — aligns with L1 Chinese face-management norms at population level; individual assessment required. Frame as validation of existing competence, not deficit remediation. | KEEP | tic_enrichment | \[verified, C-008\] Positive pragmatic transfer confirmed. Population-level generalization; do not universalize. |

---

## Craft Moves Extracted

### Lane A: deai_removal

CM-D1: Red-flag inversion (analogy, not identity) Locker warns against words triggering negative audience reaction. RLHF filler ("certainly," "great question," "I'd be happy to") triggers negative credibility response in readers who detect AI register \[verified, C-006, Wu et al. 2026: r=-0.87 sycophancy-naturalness\]. The structural parallel: both are audience-alienating word choices. The mechanisms differ (Locker: emotional/political valence; RLHF: authenticity/credibility). Scope: this analogy is constructed by the ingest, not found in Locker.

CM-D2: Discourse community violation detection (analogy) RLHF register can be characterized as a discourse-community genre violation using Swales/Locker vocabulary. The AI writes in "helpful assistant" register regardless of target community norms. Locker's diagnostic questions (What channels/formats/styles are preferred? What constitutes evidence?) can identify where AI defaults clash with community expectations. Scope: Locker did not theorize about AI writing. This is a vocabulary borrow applied to a novel domain.

CM-D3: Audience-aware removal calibration Before stripping AI signals, run Figure 2.3's six questions against the target audience. Some "AI-sounding" formality may be appropriate for the audience (e.g., formal government reports). Deai_removal must be audience-contingent, not blanket. Note: the six questions are a face-validity heuristic \[C-010, confidence 45\], not a validated instrument.

### Lane B: tic_enrichment

CM-T1: Register switching by audience type Locker's five audience types each require different register calibration. Voice priming should specify which audience type the document primarily serves, then adjust formality, detail density, and tone.

CM-T2: Structural presupposition framing \[esl_preserve\] "As you know" / subordinate-clause technique for shared information. Use presupposition markers to signal epistemic status without condescension. L1 Chinese writers have native pragmatic resources for this; preserve existing patterns rather than imposing English-specific phrasing.

CM-T3: Face-saving as voice architecture \[esl_preserve\] When a document must correct audience beliefs, build face-saving structures: acknowledge initial understanding, attribute change to circumstances rather than audience error. Aligns with L1 Chinese face-management norms at population level \[verified, C-008\]. Individual assessment required — do not essentialize. Frame as validation of existing competence if present, not assumption of competence based on L1.

CM-T4: Organizational register calibration Before priming voice, diagnose organizational culture: tall/flat hierarchy, formality norms, reward structures. "Natural" voice is context-dependent. Voice priming must be context-specific.

CM-T5: Channel-dependent voice Written voice for complex data; oral/conversational voice for consensus. Voice priming should specify channel, then calibrate. "Write like you talk" is bad advice if the channel is a formal report. Empirical basis for the written/oral distinction is weak \[C-011\] but the heuristic is directionally useful.

### Lane C: both

CM-B1: Audience analysis as pre-pass diagnostic Run Locker's six adaptation questions before any deai or tic pass. Prevents both over-removal (stripping formality the audience expects) and under-priming (failing to match register expectations). Treat as heuristic, not validated protocol \[C-010\].

---

## What Could Not Be Verified

1. Whether the truncated portion of ch02 contains an explicit "initial audience" definition that would make the taxonomy 6 types rather than 5.
2. Whether the truncated portion contains audience-benefits content (intrinsic/extrinsic) that would affect the skill incorporation table.
3. The primary source for Locker's 75% J / 80% T manager statistics. These appear to derive from MBTI manual normative tables, which are publisher-controlled and not independently replicated at the specific claim level.
4. Empirical validation of Figure 2.3's six questions as a composite instrument. No study was found testing this specific checklist.
5. Whether Locker cites Daft & Lengel or other media-richness research in portions not visible in the truncated text.

Evidence that would change the assessment:

* An independent large-sample (n > 500) study of MBTI type distribution among US managers would either confirm or kill C-004/C-005.
* A replication of Wu et al. 2026 would raise C-006 confidence from 65 toward 80.
* An empirical test of Locker's Figure 2.3 checklist against communication outcomes would resolve C-010.

---

## Coverage Attestation

chapters_attested: ch02 only

Sections verified present in attached text:

* Audience taxonomy (5 named types) — verified
* Ways to analyze (individuals, groups, org culture, discourse community) — verified
* Choosing channels — verified
* Six adaptation questions (Figure 2.3) — verified (all 6 questions with sub-bullets)
* Audience analysis works (examples) — partially verified (truncation occurs mid-section \~p.42)

Sections NOT attested (likely in truncated portion):

* Audience benefits detail (intrinsic/extrinsic)
* You-attitude extended discussion
* Chapter summary
* Exercises and cases
* Any content after p.42
* Possible "initial audience" formal definition

---

## Operator Notes

1. Primary value for tic_enrichment: the discourse community vocabulary (Q-003, CM-D2, S-03). This gives productive language for describing why RLHF register sounds wrong in specific contexts — it violates community genre norms. This is an analogy constructed by the ingest, not a theoretical derivation found in Locker. Locker predates the RLHF phenomenon.

2. Primary value for deai_removal: the red-flag inversion analogy (CM-D1, S-05). RLHF filler triggers credibility concerns through a different mechanism than Locker's political/emotional red flags, but the structural form (audience-alienating word choice → remove) is shared. Empirical support from Wu et al. 2026 (r=-0.87) is strong but unreplicated.

3. ESL preserve note: face-saving (CM-T3, S-10) and presupposition framing (CM-T2, S-04) align with L1 Chinese pragmatic norms at the population level. Positive pragmatic transfer is confirmed (Lee 2018; 2025 transfer study). Do not essentialize — individual assessment required. Frame as validation if applicable, not assumption.

4. MBTI: strip completely as an instrument. The meta-principle "adapt message structure to how the audience processes information" survives independent of MBTI. Locker's specific percentage claims (75% J, 80% T) are zombie stats that should not appear in downstream skill files.

5. Truncation impact: moderate. Core frameworks are attested. Missing content is likely exercises and extended examples. If audience-benefits detail (intrinsic/extrinsic) is needed, a follow-up ingest from the full export is required.

---

## Save Path

Target: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/locker_2012_prof_writing_w231_ch02_20260628_ingest.md

Optional refinement: prompts/synth_refine_per_source.md → locker_2012_prof_writing_w231_ch02_refined_20260628.md

Cursor implement: only from agent handoff prompts — never patch skills from raw ingest.