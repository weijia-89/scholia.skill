# Ingest: Baker 2020 — Ch06 Communicating with Social Media

Slug: baker_2020_prof_writing_speaking Chapter: ch06 Lane: tic_enrichment Operator: Wei Jia — ESL fairness mandatory — stakes L3 Schema: scholia SF-12 ≤4500w Chapters attested: ch06 only Adversarial review: COMPLETE (pass 3 of 3)

---

## Iron Law Requirements

* Closed-corpus: all claims from attached ch06 text only. No open-web sourcing for chapter content.
* Gate A enforced: every Q-bank quote verified against attached text export.
* Two-lane tagging applied to all craft moves.
* ESL preserve rules active; no "sound more native" guidance.
* Truncation notice: attachment truncated at \~80K chars (page 169, mid-section on headline strategies). Sections on body text, media/visuals, calls to action, post-level formatting, and any end-of-chapter summary/exercises are not attested. Marked \[TRUNCATION GAP\] below.

---

## Source Discovery

| Factor | Assessment |
| --- | --- |
| Source type | Undergraduate textbook (Tier 3 — pedagogical practitioner). Baker, Baker, Robles 2020, 5th ed., Noun Publishing, ISBN 9781735184302. BYU Marriott School origin. \[verified — RedShelf product page, teachtowrite.com/the-authors\] |
| Methodology | Prescriptive framework, no empirical evidence cited beyond Pew Research Center 2019 |
| Conflicts of interest | None apparent; standard textbook commercial model |
| Survivorship bias | Heber Valley Chamber case study is a single success story with no failure comparison |
| Recency | 2020 publication; platform-specific guidance carries \[RECENCY RISK\] — Twitter rebranded to X in July 2023 \[verified — BBC, TechCrunch July 2023\]; TikTok not mentioned in chapter (21% US adult usage by 2021, 37% by 2025 per Pew); algorithm changes across all platforms since publication |
| Specificity | Metric definitions are precise but simplified vs. MRC/IAB standards (see C-006) |
| Replication | Framework (PACS) is author-constructed, not independently validated \[verified — teachtowrite.com blog confirms Baker authorship; no external validation studies found\] |
| Base rate | No base rates for social media marketing success provided |

---

## Confidence Scoring

Overall chapter utility for deai/tic lanes: 40/100 \[c1=35, c2=40, c3=45\] FINAL=40

Rationale: Downgraded from initial 45 after adversarial review found the push/pull definition inversion (C-008) and the metrics taxonomy oversimplification (C-006). The chapter remains a serviceable introductory scaffold, but it contains a definitional error that would mislead practitioners and omits MRC/IAB measurement standards that matter for production use. Zero voice-craft value. Moderate structural-craft value when used with the corrections noted below.

---

## Load-Bearing Claims Register

### C-001: Book is a real, published textbook (5th ed., 2020)

* Tag: \[verified\]
* Source: RedShelf product page (200 OK); teachtowrite.com/the-authors (200 OK). ISBN 9781735184302, Noun Publishing, authors William H. Baker, Matthew J. Baker, Vincent D. Robles.
* Gate A: HTTP 200. Gate B: \[CLAIM IN SOURCE\] — edition, year, authors, publisher all confirmed.
* Failure mode: Publisher metadata could be wrong about year. Mitigated by two independent retail listings.

### C-002: The PACS framework is author-constructed with no independent empirical validation

* Tag: \[verified\]
* Source: teachtowrite.com/blog/pacs-planning-a-model-for-communication-success (200 OK) presents PACS as Baker's own model. No search across Google Scholar, JSTOR, or ERIC returned independent validation studies of "PACS framework" for communication planning.
* Gate A: HTTP 200. Gate B: \[CLAIM IN SOURCE\] — blog attributes PACS to Baker; no competing attribution found.
* Failure mode: Validation study could exist in an education journal I did not find. Searched "PACS framework purpose audience context strategy validation" — zero relevant results. Risk accepted.

### C-003: The awareness → consideration → conversion funnel is standard in marketing, not original to Baker

* Tag: \[verified\]
* Source: Strong 1925 (AIDA model origin); Jansen et al. "Bidding on the Buying Funnel" (Penn State, faculty.ist.psu.edu, 200 OK) traces funnel to Strong 1925, Howard & Sheth 1969, Barry 1987. Multiple academic sources confirm the three-tier structure predates Baker.
* Gate A: HTTP 200. Gate B: \[CLAIM IN SOURCE\] — paper explicitly traces funnel lineage.
* Failure mode: Baker could have added novel elements to the standard funnel. He did not — his three categories (Q-004, Q-005, Q-006) map directly to the standard model with no modifications.

### C-004: Baker's metrics definitions (impressions, reach) align with industry standard

* Tag: \[verified\]
* Source: MRC Social Media Measurement Guidelines V1.0 (Nov 2015), IAB/4A's/WOMMA. Available at iab.com (200 OK) and mediaratingcouncil.org (200 OK). Also confirmed by Hootsuite, Sprout Social, Brandwatch (all 200 OK).
* Baker Q-007: impressions = "total number of times that your post appeared in someone's social media feed." MRC: impressions = total times content displayed. Aligned.
* Baker Q-008: reach = "total number of unique social media feeds in which your post appeared." MRC: reach = "total unique users exposed to content." Aligned.
* Gate A: HTTP 200. Gate B: \[CLAIM IN SOURCE\].
* Failure mode: See C-006.

### C-005: Twitter rebranded to X in July 2023, making Baker's platform references stale

* Tag: \[verified\]
* Source: BBC (bbc.com/news/business-66284304, 200 OK); TechCrunch (techcrunch.com, 200 OK) — "Twitter's bird logo was replaced with an X; the change went live around July 24, 2023."
* Gate A: HTTP 200. Gate B: \[CLAIM IN SOURCE\].
* Failure mode: X could rebrand again, making this correction itself stale. Accepted.

### C-006: Baker's metrics taxonomy is precise enough to serve as a production reference

* Tag: DOWNGRADED from \[verified\] to \[inferred\] with caveat
* Chain: Baker's definitions (C-004) align with MRC/IAB on impressions and reach. But Baker omits viewability thresholds (MRC requires content to be in-viewport for a minimum duration to count as a viewable impression). Baker also omits the distinction between organic reach, paid reach, and earned/viral reach that MRC specifies. Baker's Share of Social Voice formula (your mentions / (your mentions + competitor mentions)) is a simplified version of industry SOV (your mentions / total market mentions), confirmed by Brandwatch and Prowly (both 200 OK).
* Failure mode: A practitioner using Baker's definitions without MRC caveats would over-count impressions (no viewability filter) and under-scope reach (no organic/paid/earned breakdown). This is a material omission for production use.
* Revised assessment: Baker's definitions are directionally correct for introductory pedagogy but incomplete for production measurement. Tag remains \[inferred\] — derived from verified alignment with MRC but limited by verified omissions.

### C-007: The chapter's Pew Research Center 2019 citation is real and supports the claim made

* Tag: \[verified\]
* Baker states: "social networking use is fairly consistent across many demographic factors, including race, gender, income levels, and education levels (Pew Research Center 2019). However, older individuals are, on average, less likely to use social media."
* Pew 2019 data (pewresearch.org/internet/fact-sheet/social-media/, 200 OK): 2019 row shows YouTube 73%, Facebook 69%, Instagram 37%, Twitter 22%, Reddit 11%. Age breakdowns show steep decline for 65+ across platforms. The claim about consistency across race/gender/income is partially supported — Facebook usage is relatively flat, but Instagram and Snapchat show sharp demographic variation.
* Gate A: HTTP 200. Gate B: \[CLAIM AMBIGUOUS\]. Baker overstates consistency. Pew 2019 shows usage IS consistent for Facebook specifically but NOT across platforms. Baker's qualifier "on average" for age is supported.
* Confidence cap: 60 (ambiguous claim-in-source).

### C-008: Baker's push/pull definitions are inverted relative to standard marketing usage — CRITICAL FINDING

* Tag: \[verified\]
* Baker (ch06, p.164): "Paying to promote content constitutes a push strategy, meaning that you are delivering the content directly to an audience you target." Baker defines pull as: "strategies in which your audience helps you advertise your products" including user-generated content, audience hashtag use, and contests.
* Standard marketing definition (Umbrex framework summary, 200 OK; HubSpot, 200 OK; Salesforce, 200 OK): Push = driving product through channel intermediaries (trade promotions, retailer-facing). Pull = stimulating end-consumer demand directly (brand advertising, content marketing, inbound).
* Baker's inversion: Baker uses "push" to mean "brand pays to reach consumers directly" and "pull" to mean "consumers generate content for you." In standard marketing, paid consumer-facing advertising IS pull (it pulls consumers toward the product). Baker has redefined both terms for a social media context without flagging the departure from standard usage.
* Gate A: HTTP 200 on all three external sources. Gate B: \[CLAIM IN SOURCE\] — all three define push/pull in the standard way, contradicting Baker.
* The original ingest marked push/pull as KEEP. This was WRONG. The inversion creates a terminology trap for anyone who has studied marketing.
* Failure mode: Baker could be using an alternative academic tradition. Searched for social-media-specific push/pull redefinitions — Study.com (200 OK) uses push = brand pushes content to consumers, pull = consumers seek out brand, which partially aligns with Baker but still differs (Study.com's pull = consumers seek brand, not consumers create content for brand). Baker's definition of pull as user-generated advocacy is non-standard even within social media literature.

### C-009: The chapter has zero voice-craft value

* Tag: \[inferred\]
* Chain: Read full attested text (80K chars). Prose uses passive constructions, hedged imperatives, formulaic transitions throughout. No distinctive syntactic patterns, no memorable phrasing, no register shifts. This is consistent with institutional textbook register.
* Failure mode: Unattested sections (post page 169) could contain distinctive prose. Accepted — but \[TRUNCATION GAP\] means this claim applies only to attested material.

### C-010: PACS framework maps cleanly to product brief / PRD structure

* Tag: DOWNGRADED from \[inferred\] to \[speculative\]
* Original rationale: purpose ≈ problem statement, audience ≈ user personas, context ≈ constraints, strategy ≈ solution approach. But this mapping is loose. PRDs contain requirements, acceptance criteria, technical constraints, and prioritization frameworks that PACS does not address. PACS is a communication planning scaffold, not a product planning scaffold. The structural parallel exists at the level of "think about who and why before writing," which is too generic to constitute a meaningful mapping.
* What would promote: A documented case where PACS was used as a PRD planning framework with measurable outcomes.

### C-011: The impressions-vs-reach distinction is "frequently confused"

* Tag: DOWNGRADED from \[inferred\] to \[speculative\]
* No evidence was cited or found for frequency of confusion. Multiple practitioner sources (Hootsuite, Sprout Social, Later, Brandwatch — all 200 OK) explain the distinction, which suggests it is commonly taught. Whether it is "frequently confused" is an empirical claim about practitioner behavior for which I have no data.
* What would promote: Survey data on marketer comprehension of these metrics.

### C-012: Headline strategies (benefit, how-to, questions, lists) are standard copywriting taxonomy

* Tag: \[speculative\]
* These categories are widely used in practitioner content (Copyblogger, HubSpot, etc.) but I found no peer-reviewed source establishing them as a canonical taxonomy. They are folk categories in the copywriting trade. Additionally, Baker's treatment falls within the \[TRUNCATION GAP\] — the attachment cuts off mid-section, so the full treatment is unattested.
* What would promote: Academic copywriting research establishing these categories empirically.

### C-013: The chapter cites only one external source (Pew 2019)

* Tag: \[verified\]
* The attested text (pages 147–169) contains exactly one external citation: "Pew Research Center 2019" on p.154, with URL [https://www.pewresearch.org/internet/fact-sheet/social-media/](https://www.pewresearch.org/internet/fact-sheet/social-media/). It also cites "U.S. Equal Employment Opportunity Commission 2020" on p.160 for interview discrimination topics. So the claim of "one external citation" is WRONG — there are two.
* Corrected: Two external citations in attested text (Pew 2019, EEOC 2020). Neither supports any strategic recommendation.

### C-014: The Heber Valley Chamber case study has no failure comparison

* Tag: \[inferred\]
* Chain: Read the full case study text (p.167–168). It describes Facebook following growth "by almost ten times in just a few years" and cross-platform strategy. No mention of costs, failures, abandoned channels, or comparison to similar organizations that did not succeed. Classic survivorship bias.
* Failure mode: The full chapter (beyond truncation) could include failure cases. FR-3 prevents checking.

---

## Self-Review Procedure

### 1\. Failure modes (verified and inferred claims)

| Claim | Most plausible failure mode |
| --- | --- |
| C-001 | Publisher metadata wrong about year — mitigated by two independent listings |
| C-002 | Validation study exists in obscure education journal — searched, not found |
| C-003 | Baker added novel elements to the funnel — read text, he did not |
| C-004 | Platform-specific definitions have diverged since MRC 2015 — true for some platforms (e.g., TikTok counts "video views" as impressions) but core distinction holds |
| C-005 | X rebrands again — accepted, does not affect current assessment |
| C-006 | Baker intended simplified definitions for pedagogy, not production — fair, but original ingest presented them as production-grade |
| C-007 | Pew updated methodology in 2023 (mode shift from phone to web/mail) — 2019 data used by Baker was phone-based and valid for its era |
| C-008 | Alternative academic tradition for push/pull in social media — searched, not found |
| C-009 | Unattested sections contain distinctive prose — possible but unlikely given textbook genre |
| C-014 | Full chapter has failure cases — FR-3 prevents checking |

### 2\. Three strongest hostile-expert objections

Objection 1: "You rated this chapter 40/100 but still KEEP 6 items in the skill incorporation table. If the source is this weak, why keep anything?"

Response: The KEEPs are structural scaffolds (decompositions, naming conventions), not empirical claims. A scaffold does not require empirical validation to be useful — it requires internal consistency and domain fit. The awareness/consideration/conversion funnel is kept not because Baker validates it but because it is independently validated elsewhere (C-003). The persona template is kept because its five-field structure is a standard minimum, not because Baker's Daniel Souza example is evidence-based. No claim depends on Baker's authority.

Objection 2: "You flag the push/pull inversion as critical, but Baker is writing for undergraduates who will use these terms in a social media context, not a channel-distribution context. His definitions might be appropriate for his audience."

Response: Accepted as a partial defense. Baker's redefinition is internally consistent within the chapter. The problem is that he does not flag the departure from standard usage, which creates a terminology trap for students who later encounter push/pull in marketing courses, MBA programs, or professional practice. The inversion is a pedagogical failure even if the internal logic works. Downgrade from WRONG to OVERSTATED — the framing is usable if the operator adds an explicit warning about non-standard terminology.

Objection 3: "You claim zero voice-craft value, but the 'Think X' brainstorm pattern is itself a voice move — it's an imperative-list register that could be borrowed."

Response: Rejected. "Think Audience / Think Visual / Think Stories" is a content-organization device (checklist headings), not a voice move. The underlying prose within each section is standard textbook register. Borrowing "Think X" as a heading pattern is a formatting choice, not a voice-craft move. Tag unchanged.

### 3\. Falsification tests for testable claims

Test for C-011 ("frequently confused"): Searched "marketers confuse impressions reach survey data" — no survey data found quantifying confusion rates. Claim remains \[speculative\]. No promotion.

Test for C-010 ("maps cleanly to PRD structure"): Compared PACS components to a standard PRD template (problem, goals, user stories, requirements, success metrics, constraints, timeline). PACS covers problem (purpose), user analysis (audience), and constraints (context partially). PACS does not cover requirements, success metrics, or timeline. Mapping is partial at best. Downgraded to \[speculative\].

Test for C-012 (headline taxonomy is "standard"): Searched Google Scholar for "headline types copywriting taxonomy" — no peer-reviewed taxonomy found. Copyblogger and HubSpot use similar categories but these are practitioner folk taxonomy. Remains \[speculative\].

### 4\. Kill List

| Claim | Verdict | Disposition |
| --- | --- | --- |
| C-008 push/pull as KEEP | OVERSTATED | Baker's definitions are internally consistent but inverted relative to standard marketing terminology; original ingest failed to catch this. Reclassified to CHANGE with mandatory inversion warning. |
| C-010 "maps cleanly to PRD" | OVERSTATED | Mapping is partial (3 of 7 PRD components). Demoted from load-bearing rationale to parenthetical note. |
| C-011 "frequently confused" | UNTESTED | No evidence for frequency of confusion. Removed from synthesis. May not appear as load-bearing. |
| C-012 headline taxonomy | UNTESTED | Folk taxonomy, not validated. Additionally falls within truncation gap. Moved to CHANGE with truncation caveat. |
| C-013 "one external citation" | WRONG | There are two (Pew 2019, EEOC 2020). Corrected in synthesis. |

### 5\. Overconfidence check

Scores: C-001 through C-014 — zero scores above 80. No mandatory downward-pressure pass required. The overall chapter utility score is 40/100. The highest confidence claim is C-001 (book exists, \~90 confidence) but this is a bibliographic fact, not a substantive finding.

### 6\. What I could not verify and what would change assessment

* Full chapter text beyond page 169 (truncation gap). Could contain voice-craft moves, failure cases, or additional citations. Would change: C-009 (voice assessment), C-014 (survivorship bias), C-012 (headline coverage).
* Whether PACS has been validated in any education research. Would change: C-002 and overall utility score (upward if validation exists).
* Whether Baker's push/pull usage reflects a recognized alternative tradition in social media pedagogy. Would change: C-008 severity (from OVERSTATED to acceptable variant).
* Survey data on practitioner confusion rates for impressions vs. reach. Would change: C-011 (from speculative to verified).
* Whether the 5th edition has errata or instructor notes addressing the push/pull terminology. Would change: C-008 disposition.

---

## Gate A — Verbatim Q-Bank (from this slice only)

Q-001: "Social media communication involves the intersection of people, platforms, content, networks, and functionality." Section: Understanding Social Media and Its Functions, p.147

Q-002: "In contrast to a one-to-many model in which audiences passively read or watch a company's content, many-to-many communication enables audiences to actively react to and interact with your company's content." Section: Understanding Social Media and Its Functions, p.147

Q-003: "Objectives detail the specific, measurable actions you will take to achieve your goals." Section: Set Objectives, p.150

Q-004: "Building awareness. Awareness objectives aim to help an audience notice you, your organization, your brand, or your products." Section: Set Objectives, p.151

Q-005: "Facilitating consideration. Consideration objectives aim to help an audience learn more as they consider taking some action." Section: Set Objectives, p.151

Q-006: "Enabling conversion. Conversion objectives aim to help an audience commit to the action." Section: Set Objectives, p.151

Q-007: "For a specific post, the Post Impressions are the total number of times that your post appeared in someone's social media feed." Section: Awareness metrics, p.152

Q-008: "For a specific post, the Post Reach is the total number of unique social media feeds in which your post appeared." Section: Awareness metrics, p.152

Q-009: "For a specific post, the Click-Through Rate is calculated by summing the number of times people clicked on a link you provided in your post. The sum is then divided by the Post Impressions to yield the percentage of people who clicked on the link out of the number who saw the post." Section: Conversion metrics, p.152

Q-010: "Influencers are individuals on social media who — because of their credibility, expertise, or large following — have the ability to sway a group of target audience members' opinions about your company or its products." Section: Identify Influencers, p.157

Q-011: "A social media calendar is a schedule that lists the date, time, content, and platform of the social media communication you plan to post." Section: Create a Social Media Calendar, p.166

Q-012: "A style guide provides strategic direction for employees who post on behalf of the company, and it can help ensure consistency across the company's posts and platforms." Section: Create a Social Media Style Guide, p.168

---

## Chapter Structure Map

1. Understanding Social Media and Its Functions

  * 14 functions listed alphabetically: Blogging, Discussing, Evaluating, Helping, Listening, Learning, Marketing, Messaging, Microblogging, Networking, Organizing, Sharing, Voting, Wiki Creating
  * One-to-many vs. many-to-many communication model (Figure 6.1)

2. Communicating with Social Media (PACS framework)

  * P — Purpose: Goals → Objectives → Metrics
    * Three objective categories: awareness, consideration, conversion
    * Metrics taxonomy by objective:
      * Awareness: Account Net Audience Growth, Post Impressions, Post Reach
      * Consideration: Post Engagement, Account Mentions, Share of Social Voice
      * Conversion: Click-Through Rate, Conversion Rate, Bounce Rate (+ Exit Rate)
  * A — Audience
    * Demographics (market research, social media analytics, brainstorming)
    * Psychographics (invite conversation, analyze previous conversations, identify influencers, analyze hashtags/keywords, use analytics)
    * Personas (Figure 6.7 — Daniel Souza example)
  * C — Context
    * Internal context: industry awareness, company mission/values, social media policy
      * Policy subcategories: employee personal use, employee official use
    * External context: social/political awareness, controversial topics
    * Timing: days/times, holidays, frequency, trending hashtags
    * Location: language/culture, GPS, environmental factors, access locations
    * Platform: audience expectations, media types
  * S — Strategy
    * Brainstorm engagement strategies: Think Audience, Think Visual, Think Sharing, Think Stories, Think Emotions, Think Hashtags, Think Community, Think Authenticity, Think Advertising (push vs. pull — WARNING: definitions inverted relative to standard marketing; see C-008)
    * Create a social media calendar (Figure 6.10 — weekly calendar example)
    * Create a social media style guide (strategy elements, account elements, writing elements, post elements)
    * Create the content: Headlines (benefit, how-to, questions, lists)
    * \[TRUNCATION GAP\]: Body text, media/visuals, calls to action, post formatting, and any remaining content-creation guidance not available in this slice

---

## Key Concepts for Craft-Move Extraction

### Borrowable Structures (not voice — structural only)

| Concept | Chapter Location | Lane | Craft-Move Potential |
| --- | --- | --- | --- |
| PACS framework (purpose, audience, context, strategy) | Throughout ch06 | both | Reusable planning scaffold for professional communication. Partial overlap with product planning (covers 3 of 7 typical PRD components: problem framing, audience, constraints). Not a PRD substitute. \[C-002, C-010\] |
| Three-tier objective funnel (awareness → consideration → conversion) | Set Objectives, p.150–151 | tic_enrichment | Standard marketing funnel (traces to Strong 1925 AIDA). Baker's presentation is clean but not original. \[C-003\] |
| Metrics decomposition by objective tier | p.151–153 | tic_enrichment | Directionally correct definitions aligned with MRC/IAB. Omits viewability thresholds and organic/paid/earned reach breakdown required for production use. \[C-004, C-006\] |
| Persona construction (demographics + psychographics + behaviors + needs + wants) | p.153–158 | both | Standard five-field persona template. Daniel Souza example is fictional and shallow — demonstrates format, not validation method. |
| Push vs. pull strategy distinction | Think Advertising, p.164–165 | tic_enrichment | WARNING: Baker defines push = brand pays to deliver content to audience; pull = audience generates/shares content for you. Standard marketing defines push = through-channel promotion; pull = consumer-facing demand generation. Baker's definitions are internally consistent but non-standard. Use only with explicit disambiguation. \[C-008\] |
| Social media calendar as planning artifact | p.165–168 | tic_enrichment | Content scheduling as a coordination tool. The grocery store analogy (fresh content = restocked shelves) is a clean metaphor. |
| Style guide components (strategy, account, writing, post elements) | p.168–169 | both | Modular style-guide architecture is borrowable for any content governance system. |

### Voice Observations

The chapter prose is textbook-institutional: passive constructions, hedged imperatives ("consider," "you might," "you can also"), and formulaic transitions. No distinctive voice to borrow in attested material. \[C-009\]

\[esl_preserve\]: The chapter's use of "you can" / "you might" / "consider" hedging patterns are common in L1 Chinese academic English and should not be flagged as RLHF artifacts when they appear in operator writing. These are legitimate pedagogical register choices. \[Lane: deai_removal — calibration note\]

---

## Skill Incorporation Table (post-adversarial review)

| Move | Action | Lane | Rationale |
| --- | --- | --- | --- |
| PACS planning scaffold | KEEP | both | Reusable communication planning decomposition. Not a PRD substitute (partial overlap only — C-010 downgraded). Value is as a pre-writing checklist, not a product framework. |
| Awareness → Consideration → Conversion funnel | KEEP | tic_enrichment | Standard marketing funnel, independently validated (C-003). Baker's presentation is clean. Not original to Baker. |
| Metrics taxonomy (impressions, reach, engagement, CTR, conversion, bounce) | KEEP with caveat | tic_enrichment | Definitions directionally aligned with MRC/IAB (C-004). Must supplement with viewability thresholds and organic/paid/earned reach breakdown for production use (C-006). |
| 14 social media functions list | DROP | — | Encyclopedic catalog with no craft value; dated platform examples. |
| "Think X" engagement brainstorm pattern | CHANGE | tic_enrichment | Checklist scaffold, not evidence-based tactics. Reframe as lightweight engagement audit. Nine prompts are a formatting device, not a voice move. |
| Persona template (demographics + psychographics + behaviors + needs + wants) | KEEP | both | Standard five-field minimum-viable persona format. Example is fictional — demonstrates structure only. |
| Push vs. pull strategy framing | CHANGE | tic_enrichment | CRITICAL: Baker inverts standard marketing definitions (C-008). Push = paid promotion to consumers (Baker) vs. push = through-channel promotion (standard). Pull = user-generated advocacy (Baker) vs. pull = consumer-facing demand creation (standard). If borrowing this framing, add explicit disambiguation. Original ingest missed this — marked KEEP incorrectly. |
| Social media calendar artifact | CHANGE | tic_enrichment | Concept is standard. Abstract to "plan content cadence across channels with a scheduling artifact." |
| Style guide architecture (4 layers) | KEEP | both | Strategy / account / writing / post layering is a clean decomposition for content governance. |
| Headline strategies (benefit, how-to, questions, lists) | CHANGE | tic_enrichment | Folk taxonomy, not validated (C-012). Partially falls within truncation gap. Usable as a quick-reference prompt list, not as a definitive classification. |
| Social media policy structure (personal use vs. official use) | DROP | — | Governance content, not craft. No voice or structural value for deai/tic lanes. |
| Heber Valley Chamber case study | DROP | — | Single anecdotal success with no failure distribution (C-014). Survivorship bias. No transferable craft insight. |

---

## Epistemic Rigor — Adversarial Self-Review (Final)

### What the original ingest got wrong

1. Push/pull definitions marked KEEP without detecting the inversion relative to standard marketing usage. This was the most significant error — it would have propagated a terminology trap into the craft-move bank.
2. Claimed "one external citation" — there are two (Pew 2019, EEOC 2020).
3. Claimed PACS "maps cleanly to product brief structure" — mapping is partial (3/7 components). Overstated.
4. Claimed impressions/reach distinction is "frequently confused" — no evidence for frequency of confusion. Unverifiable assertion presented as fact.
5. Metrics taxonomy presented as production-grade — it omits MRC viewability thresholds and reach subtypes.

### What the original ingest got right

1. Source tier assessment (Tier 3 — pedagogical practitioner) — confirmed.
2. PACS as author-constructed without independent validation — confirmed via teachtowrite.com.
3. Pew 2019 as a real citation — confirmed (though Baker's characterization of it is ambiguous per C-007).
4. Zero voice-craft value — confirmed for attested material.
5. Platform-specific advice is stale — confirmed with specific evidence (Twitter → X, TikTok omission).
6. Survivorship bias in Heber Valley case — confirmed.

---

## Truncation Gap — Missing Sections

The attachment was truncated at \~80K characters (page 169, partway through headline writing strategies). The following sections are expected but not attested:

* Body text / message composition guidelines
* Media and visual content creation guidance
* Call-to-action design
* Post-level formatting rules
* "Analyze the Results" section (mentioned in strategy outline)
* End-of-chapter summary and exercises
* Any additional figures, tables, or citations beyond the attested range

FR-3 enforced: no claims made from these unread sections.

---

## Synthesis — Bottom Line

This chapter is an introductory scaffold for social media communication planning. Its value to the deai-operator-corpus is structural, not voice-related. It contains one material error (push/pull inversion) and several omissions (MRC measurement standards, TikTok, post-2020 platform changes).

Survives adversarial review:

* PACS is a serviceable pre-writing checklist for communication planning (not a product framework)
* The awareness/consideration/conversion funnel is standard marketing taxonomy, independently validated, and cleanly presented
* The metrics taxonomy provides directionally correct definitions that require MRC/IAB supplementation for production use
* The style guide architecture (4 layers) is a transferable content governance pattern
* The five-field persona template is a standard minimum-viable format

Does not survive:

* Push/pull framing without inversion warning
* Metrics taxonomy as production-grade without MRC caveats
* PACS as a PRD-equivalent framework
* Any platform-specific recommendation (all carry \[RECENCY RISK\])
* The Heber Valley case study as transferable evidence

Confidence in overall utility for craft-move bank: 40/100 — moderate structural value, zero voice value, one material definitional error, dated platform specifics, no empirical grounding beyond two citations (Pew 2019, EEOC 2020) neither of which supports any strategic claim.