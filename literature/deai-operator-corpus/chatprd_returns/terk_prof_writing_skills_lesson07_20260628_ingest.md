# Ingest — terk_prof_writing_skills_lesson07

Source: Terk, Natasha. Professional Writing Skills: A Write It Well Guide. Lesson 7: Write Effective E-Mail. pp. 219–233. Slug: terk_prof_writing_skills Chapter: lesson07 Lane: tic_enrichment Operator: Wei Jia, L1 Chinese, \[esl_preserve\] active Date: 2025-07-15 Adversarial review: 2025-07-15 (same session)

## 1) TL;DR (post-review)

* Proofreading is credibility infrastructure: spelling/grammar errors produce linearly additive trustworthiness penalties, confirmed by peer-reviewed experiment (Witchel et al. 2022, N=100, P<0.001). Terk's Suzanne Boyles demonstration is directionally correct. However, cross-cultural context moderates the effect — negative attributions from technical language violations are reduced when readers know the sender is from a different culture (Vignovic & Thompson 2010). \[esl_preserve\] guard is not optional. \[verified, conf 60\]
* Front-loading key information is supported by Nielsen/NN Group F-pattern eyetracking (N=232): readers perform two horizontal sweeps across top content then scan vertically down the left edge. First two paragraphs receive disproportionate fixation. Terk's "first few lines" claim aligns. \[verified, conf 55\]
* Subject line specificity increases engagement: multiple large-scale industry datasets (ScienceDirect 140K subject lines; ReachIQ millions of B2B emails; BuzzStream 6M subject lines) converge on specificity as the strongest predictor of open rates. Terk's worked examples are directionally correct but lack the quantitative grounding these sources provide. \[verified, conf 55\]
* Visual chunking (whitespace, short paragraphs, lists) improves reader preference and satisfaction but the comprehension effect is unconfirmed — Scharff et al. found no significant effect on reading time or content retention; a separate study found no significant impact of whitespace on comprehension. Terk overstates the mechanism. Downgraded from STRONG to MODERATE. \[inferred, conf 45\]
* Exclamation points as spam trigger: WRONG as stated by Terk. Email Almanac rates this "Mostly False." SpamAssassin assigns points only for 3+ consecutive exclamation marks, not single instances. Single exclamation marks are not spam triggers. Terk's absolute claim ("Anything with an exclamation point") is falsified. The social-credibility half of the claim (false urgency erodes trust) survives as \[inferred\]. \[KILLED as stated; partial salvage\]

## 2) Coverage attestation

chapters_attested: lesson07 only Pages covered: 219–233 (plus back matter pp. 234–236, not extracted for craft claims) Cross-references to other lessons (Lesson 1: six steps) noted but NOT ingested — closed to lesson07 slice per FR-3.

## 3) Gate A Q-bank (verbatim from slice)

| Q-ID | quote | location hint |
| --- | --- | --- |
| Q-001 | "Convenience is not a good-enough reason for using e-mail to communicate certain kinds of information. E-mail is too public for some messages. It's more like sending a postcard than sealing a letter into an envelope." | p. 219 |
| Q-002 | "Before clicking Send, ask yourself what might happen if someone published your e-mail draft in a newspaper." | p. 219 |
| Q-003 | "Most readers are likely to read only the first few lines before deciding whether the e-mail merits any more of their time. If it does, they scan the rest of the message to pick out the important points." | p. 220 |
| Q-004 | "To get the most important information across quickly and clearly for a reader skimming your e-mail, decide on your single, main point; frame it as a key sentence; and put it at the beginning." | p. 221 |
| Q-005 | "For an e-mail to be useful, your information should answer all the reader's questions—and only those questions." | p. 221 |
| Q-006 | "Stop yourself if you find yourself rewriting the message, moving things around, or adding a lot of new information. Remember your purpose, audience, and main point, and the questions the e-mail needs to answer." | p. 222 |
| Q-007 | "Short sentences and paragraphs are easier to read than long ones" | p. 224 |
| Q-008 | "Lists are easier to read than sentences and paragraphs" | p. 224 |
| Q-009 | "A salutation or greeting is like saying 'Hi' or 'Hello' when you begin a conversation." | p. 224 |
| Q-010 | "A closing is like the period that ends a sentence—it lets the reader know you're done." | p. 226 |
| Q-011 | "The e-mail you write conveys a particular image to your readers. If your grammar, punctuation, and spelling are sloppy, your image will be, too." | p. 228 |
| Q-012 | "A well-written subject line is like the headline for a news article: it draws the reader's attention and tells the reader what the e-mail is about." | p. 228 |
| Q-013 | "Anything with an exclamation point get your message sent to the spam folder." | p. 230 |
| Q-014 | "If you do it too often, no one will ever take you seriously." | p. 230 (re: false urgency / exclamation points — "boy who cried Wolf") |
| Q-015 | "Long subject lines are often truncated, especially on handheld devices. If you can't avoid a long subject line, make sure the key information appears in its first few words." | p. 230 |
| Q-016 | "Always tell your readers whenever you attach a file to your e-mail. Otherwise, they might delete, forward, or save the message before noticing the important file they needed." | p. 228 |
| Q-017 | "how credible is someone who can't take the time to write a message without glaring errors, or doesn't know how?" | p. 227 |
| Q-018 | "In a document as brief as an e-mail, it's especially important to group your points into logical categories that facilitate skimming." | p. 221 |

## 4) Adversarial review: claim registry and verification

### Load-bearing claims

| ID | claim | tag | source | conf | failure mode |
| --- | --- | --- | --- | --- | --- |
| C-001 | Subject line specificity increases open/engagement | \[verified\] | ScienceDirect (Balakrishnan et al. 2023, 140K subject lines); ReachIQ (millions B2B); BuzzStream (6M journalist pitches) — all converge on specificity as top predictor. Gate A: 200 OK. Gate B: specificity-as-predictor explicitly stated in all three. | 55 | All three sources are industry/practitioner datasets, not peer-reviewed RCTs. Effect sizes vary by domain (B2B cold outreach vs. internal business email). Ceiling: cross-sectional max 60, reduced to 55 for COI (platforms selling email tools). |
| C-002 | Visual chunking improves comprehension independently of prose quality | \[inferred\] | Scharff et al. (SFA State, N=57): "ANOVAs indicated neither text format nor instructions had significant effects on reading times or content retention." ResearchGate whitespace study (N=13): "No significant impact of text width or passive white space on reading speed or comprehension." Both Gate A: 200 OK. Gate B: null results on comprehension confirmed. Chunking improves preference/satisfaction, not measured comprehension. | 40 | Terk's Pierre example demonstrates subjective readability improvement. The mechanism claim ("determines comprehension") exceeds the evidence — only satisfaction and preference are supported. Inference chain: chunking → preference → willingness to read → effective comprehension (indirect). |
| C-003 | Readers read only first few lines, then scan | \[verified\] | Nielsen/NN Group F-pattern study (2006, confirmed 2017): "Users first read in a horizontal movement, usually across the upper part of the content area" and "Users won't read your text thoroughly in a word-by-word manner. Exhaustive reading is rare." Gate A: 200 OK. Gate B: claim in source. N=232 users across thousands of web pages. | 55 | Study is on web pages, not specifically email. Transfer to email is plausible but unverified as a direct experimental condition. Separate email eye-tracking study (DOI:10.1057/dddmp.2012.23) confirms "engagement is strongly influenced by how effectively the opening screen draws attention" — supporting the transfer. Cap at 55 for domain transfer. |
| C-004 | Email errors damage sender credibility (halo effect) | \[verified\] | Witchel et al. 2022 (Frontiers in Psychology, N=100): "two spelling errors resulted in a penalty to trustworthiness of 5.91 ± 1.70... while the penalty for five errors was 13.5 ± 2.47; all three conditions were significantly different from each other (P < 0.001)." Kreiner et al. 2002 (J. Gen. Psychology): "A larger number of spelling errors lowered overall perceived ability." Vignovic & Thompson 2010 (J. Applied Psychology, N=not accessible, abstract only): "technical language violations... lead to negative perceptions of sender's conscientiousness and trustworthiness." Gate A: Witchel 200 OK full text; Vignovic \[ABSTRACT-ONLY\]. Gate B: Witchel CLAIM IN SOURCE (exact figures verified). | 60 | Witchel study context is health forum posts about MS, not business email. Kreiner used essays. Vignovic used email context but full text paywalled. Cross-context generalization is reasonable but domain-specific magnitudes unknown. Single study cap 70, reduced to 60 for context transfer + Dalton Maag COI in Witchel (3 of 8 authors employed by type design company). |
| C-005 | Exclamation points in subject lines trigger spam filters | \[speculative\] KILLED | Email Almanac (ReviewMyEmails.com): "Myth: Mostly False. Spam filters do not count exclamation points against you." Second Email Almanac article: "single exclamations generally fine, but three or more in a row... increasing the likelihood of triggering spam flags." SpamAssassin documentation assigns points only for patterns of excessive punctuation, not single instances. Gate A: 200 OK. Gate B: Terk's absolute claim ("Anything with an exclamation point") is directly contradicted. | 0 | Terk's claim is falsified as stated. The social-credibility component (Q-014, "boy who cried Wolf" habituation) is separable and survives as \[inferred\]. |
| C-006 | Mobile truncation of subject lines | \[verified\] | EmailToolTester (device testing): "maximum of 33 characters for the subject line" for universal visibility. BuzzStream (real-device testing): "Safest universal length... under 40 characters." Twilio: "Mobile devices typically truncate email subject lines after about 33–50 characters." ActiveCampaign: "most restrictive common client being the Gmail app on Android at \~33 characters." Gate A: all 200 OK. Gate B: truncation confirmed across all sources with specific character counts. | 65 | These are practitioner/industry sources, not peer-reviewed, but the claim is empirically testable and multiply confirmed via direct device testing. Cap at 65 for lack of peer review. |
| C-007 | Register/tone affects response behavior | \[verified\] | Vignovic & Thompson 2010 (J. Applied Psych): etiquette violations trigger negative attributions independently of cultural context. \[ABSTRACT-ONLY\]. Pragmatics study (DOI:10.1016/j.pragma.2022.12.006): "Less politeness modification: senders perceived as more bossy" but for L2 writers, "less politeness modification increased perceived authority and receivers were more willing to comply." \[ABSTRACT-ONLY\]. CrowdTone study (arxiv 1701.01793): "over 90% of CrowdTone-edited emails would receive a response, versus 59% for originals." Gate A: all resolved. Gate B: CrowdTone claim in source; Pragmatics study abstract confirms L1/L2 divergence. | 45 | CrowdTone N=22 is underpowered. Pragmatics study is abstract-only. Vignovic is abstract-only. Multiple sources converge directionally but none individually strong. Expert opinion + case study ceiling 45. Critical finding for \[esl_preserve\]: L2 directness increases compliance, contradicting Terk's implicit assumption that directness is "abrupt." |
| C-008 | Front-loading key information improves email effectiveness | \[inferred\] | Derived from C-003 (F-pattern verified) + C-001 (subject line specificity verified). If attention concentrates on first lines (C-003) and specificity increases engagement (C-001), then front-loading key information in body text improves effective communication. Chain: attention distribution → information placement → comprehension probability. | 50 | The inference is sound but "effectiveness" is not directly measured in any cited study. Comprehension ≠ action/response. No study measures whether front-loaded emails produce higher response rates vs. buried-lede emails in controlled conditions. |

### Kill list

| ID | claim | verdict | one sentence |
| --- | --- | --- | --- |
| C-005 / CM-10 | Exclamation points trigger spam filters | WRONG | Terk's absolute claim is directly contradicted by SpamAssassin behavior and Email Almanac's "Mostly False" rating; single exclamation marks are not spam triggers. |
| C-002 / CM-02 | Visual chunking determines comprehension independently of prose quality | OVERSTATED | Two studies found no significant effect of whitespace/formatting on comprehension or reading time; chunking improves subjective preference, not measured comprehension. Survives as "chunking improves reader willingness to engage" with \[inferred\] tag. |
| CM-01 (scope) | Subject lines "must be" specific and descriptive | OVERSTATED | BuzzStream data shows subject lines over 71 characters had highest open rates for journalist pitches, and 9-13 word lines outperformed shorter ones in that domain — optimal length/specificity is context-dependent, not a universal rule. Survives with scope qualifier "for business email to known recipients." |
| CM-05 (scope) | Directness is "abrupt" and requires polite register correction | OVERSTATED | Pragmatics study (DOI:10.1016/j.pragma.2022.12.006) found L2 writers using less politeness modification were perceived as having more authority and receivers were more willing to comply. Terk's register scale encodes US-anglophone norms as universal. Survives only with \[esl_preserve\] guard. |
| CM-07 | Salutation signals three things (contact, confirmation, tone) | UNTESTED | No external evidence found for or against this tripartite function claim. Practitioner assertion only. Cannot appear as load-bearing in synthesis. |
| CM-08 | Closing functions as structural boundary signal | UNTESTED | No external evidence found. Practitioner assertion only. Cannot appear as load-bearing in synthesis. |

### Three strongest hostile-expert objections

Objection 1: All external evidence for subject line specificity comes from marketing/outreach contexts (cold email, journalist pitches, B2B sales). Terk's advice addresses internal business email. The transfer is unvalidated — internal email recipients open messages from known senders regardless of subject line quality.

Response: Valid. C-001 confidence reduced from 65 to 55. The subject-line-as-triage-input mechanism is weaker for internal email where sender identity dominates. Subject line advice applies most strongly to external/group/unfamiliar-recipient email.

Objection 2: The "halo effect" label in CM-06 is imprecise. Witchel et al. 2022 specifically tested whether the trustworthiness penalty is integrative (linear) or heuristic (dichotomous) and found it linear. Terk's demonstration (Suzanne Boyles with \~15 errors) is at the extreme end where ceiling effects may apply — Martin-Lacroux & Lacroux 2017 found that "ten errors had no greater impact than five errors." The ingest's mechanism description ("halo-effect credibility discount") is an oversimplification.

Response: Partially valid. The mechanism label is corrected from "halo-effect credibility discount" to "linearly additive trustworthiness penalty (Witchel 2022), with ceiling effects at high error densities (Martin-Lacroux & Lacroux 2017)." CM-06 mechanism updated in craft moves table.

Objection 3: The ingest extracts 12 craft moves from a practitioner workbook and assigns STRONG/MODERATE rankings without any external validation. This risks dignifying common-sense advice as "craft theory." Most of these claims are folk wisdom dressed in mechanism language.

Response: Valid. Post-review, only 3 claims earned external verification (C-003, C-004, C-006). Two more are supported by inference chains (C-002, C-008). The remainder are practitioner heuristics. Rankings recalibrated: no claim rated above MODERATE. The ingest's original STRONG ratings were overconfident.

### Overconfidence check

Post-review scores: 65, 60, 55, 55, 50, 45, 40, 0. Zero scores above 80. No downward-pressure pass required.

### What could not be verified

* Whether front-loaded emails produce higher response rates than buried-lede emails (no controlled study found)
* Whether salutation formality level affects response behavior (no study found isolating this variable)
* Whether closing presence/absence affects reader perception of message completeness
* Whether the Pierre before/after demonstration generalizes beyond subjective readability to measured comprehension
* Kreiner et al. 2002 and Vignovic & Thompson 2010 full texts are paywalled; claims verified against abstracts only

What would change the assessment: A peer-reviewed RCT comparing front-loaded vs. buried-lede business emails on response rate would promote C-008 from \[inferred\] to \[verified\]. A controlled study of paragraph chunking effects on email comprehension (not just preference) would resolve the CM-02 dispute.

## 5) Craft moves (post-review, ranked MODERATE to WEAK)

| id | lane | claim | mechanism | scope/limit | falsifier | esl_preserve | tag | conf | Q-ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CM-01 | tic_enrichment | Subject lines should be specific, descriptive, and front-loaded with key information for external/group/unfamiliar-recipient email | Reader triage uses subject line as primary input; truncation on mobile clips at \~33-40 characters. Multiple industry datasets confirm specificity as top predictor of open rates. | External and group email. For internal email to known senders, subject line specificity is less determinative — sender identity dominates triage. | A/B test in internal business email showing vague subject lines match or outperform specific ones | n/a | \[verified\] | 55 | Q-012, Q-015 |
| CM-02 | tic_enrichment | Visual chunking (short paragraphs, whitespace, lists) improves reader willingness to engage, but the effect on measured comprehension is unconfirmed | Pierre before/after demonstrates subjective readability transformation. Two studies found no significant comprehension effect from whitespace/formatting changes. Mechanism: chunking → preference → willingness to read (indirect path to comprehension). | All screen-read text. Preference effect is consistent; comprehension effect is undemonstrated. | Study showing chunked email significantly outperforms dense email on measured comprehension | n/a | \[inferred\] | 40 | Q-003, Q-007, Q-008 |
| CM-03 | tic_enrichment | Lead with your single main point as a key sentence — the inverted pyramid for email | Readers perform F-pattern scanning (Nielsen 2006/2017, N=232): first two paragraphs receive disproportionate fixation. Email eye-tracking confirms opening screen drives engagement. Buried key points receive less attention. | All email. Weaker for narrative/storytelling contexts. Transfer from web-page eyetracking to email is plausible but not directly tested. | Study showing buried-lede emails produce equal or higher response rates | n/a | \[inferred\] | 50 | Q-004, Q-003 |
| CM-04 | both | Medium selection is a prerequisite gate, not a style choice | Email is structurally public ("postcard not envelope"); confidential/sensitive/complex content requires a channel with access control. The "newspaper test" is a heuristic. | Professional/organizational email. Less relevant for encrypted messaging platforms (Signal, end-to-end encrypted email). | n/a | n/a | \[speculative\] | 35 | Q-001, Q-002 |
| CM-05 | tic_enrichment | Tone calibration via register substitution requires cultural context awareness | Terk's register scale (abrupt → polite → formal → friendly) encodes US-anglophone norms. Pragmatics research shows L2 writers using less politeness modification were perceived as having more authority, and receivers were more willing to comply. Register norms are culture- and power-dependent, not universal. | All professional email. Register "correctness" is audience-relative. | n/a | \[esl_preserve\] CRITICAL: L2 directness is not "abrupt" — it can increase perceived authority and compliance. Do not correct direct register to polite register without cross-cultural context. Terk's scale is a reference, not a rule. | \[verified\] | 45 | Q-006 |
| CM-06 | tic_enrichment | Proofreading is credibility infrastructure: errors produce linearly additive trustworthiness penalties | Witchel et al. 2022 (N=100): 2 errors = -5.91 units, 5 errors = -13.55 units on 100-point scale (P<0.001). Penalty is linear, not dichotomous, up to 5 errors; ceiling effects observed at higher densities (Martin-Lacroux & Lacroux 2017). Vignovic & Thompson 2010: negative perceptions reduced when reader knows sender is from different culture. | All professional email. Effect size larger for first-contact/external communication. Effect moderated by reader personality (Kreiner 2002) and cross-cultural awareness. | Context where error tolerance is normatively high (e.g., startup culture, SMS-adjacent platforms) | \[esl_preserve\] Systematic L1 transfer (article usage, preposition choice) is categorically different from carelessness-signaling typos. Vignovic & Thompson 2010 confirms that cross-cultural context information mitigates negative attributions from technical language violations. | \[verified\] | 60 | Q-011, Q-017 |
| CM-09 | tic_enrichment | Attachment handling requires explicit announcement + context + action instruction in body | Email body is the only guaranteed-read surface. Without announcement, readers may process message without noticing attachment. | All email with attachments | n/a | n/a | \[speculative\] | 30 | Q-016 |
| CM-10 | KILLED | ~~Exclamation points in subject lines trigger spam filters~~ | WRONG. SpamAssassin assigns points only for 3+ consecutive exclamation marks. Email Almanac: "Mostly False. Spam filters do not count exclamation points against you." Terk's absolute claim ("Anything with an exclamation point") is falsified. | n/a | n/a | n/a | WRONG | 0 | Q-013 |
| CM-10b | tic_enrichment | False urgency in subject lines erodes sender credibility via habituation | Salvaged social component of CM-10. "Boy who cried Wolf" mechanism: repeated false urgency degrades future urgency signals. Exclamation points contribute to perceived unprofessionalism but are not technical spam triggers. | Subject lines; extends to any urgency marker used without genuine time pressure | n/a | n/a | \[inferred\] | 35 | Q-014 |
| CM-11 | tic_enrichment | Scope-match content to audience: one message per audience segment, not one blast | When recipients differ in background knowledge or needed actions, a single message either over-includes or under-includes. "Answer all the reader's questions — and only those questions." | Group email / distribution lists; less relevant for 1:1 | n/a | n/a | \[speculative\] | 30 | Q-005, Q-018 |
| CM-12 | both | Update subject line when reply thread changes topic | Stale subject lines mislead readers about content and break searchability. Subject line is the retrieval key for future reference. | Multi-reply threads | n/a | n/a | \[speculative\] | 30 | Q-012 |

Removed from craft moves table: CM-07 (salutation) and CM-08 (closing) — UNTESTED practitioner assertions with no external evidence. Retained in Q-bank (Q-009, Q-010) as source material for future verification.

## 6) Skill incorporation (post-review)

| skill | file (absolute) | KEEP/CHANGE/ADD/DROP | diff intent | tag | conf | Q-ID |
| --- | --- | --- | --- | --- | --- | --- |
| Front-load key sentence in email body | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | CHANGE | Add F-pattern scanning mechanism (Nielsen 2006/2017). Terk's "first few lines" claim is directionally correct but the skill entry should cite the eyetracking evidence, not Terk. | \[inferred\] | 50 | Q-004, Q-003 |
| Visual chunking as reader engagement driver | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | ADD | Chunking improves reader preference and willingness to engage. Do not claim comprehension improvement — two studies found null results on comprehension. Frame as engagement infrastructure, not comprehension infrastructure. | \[inferred\] | 40 | Q-007, Q-008 |
| Register calibration with esl_preserve guard | /Users/dubs/.cursor/skills/deai/research/deai-tic-voice-craft-canon/decision_canon/deai_tic_voice_craft_decision_canon_20260619.md | CHANGE | Add finding: L2 directness increases perceived authority and compliance (Pragmatics DOI:10.1016/j.pragma.2022.12.006). Terk's register scale is a reference point, not a correction target. \[esl_preserve\] guard must be explicit in skill file. | \[verified\] | 45 | Q-006 |
| Subject-line-as-headline pattern | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | ADD | Scope to external/group/unfamiliar-recipient email. Cite truncation data (33-40 char safe zone). Do not repeat Terk's falsified spam-filter claim. | \[verified\] | 55 | Q-012, Q-015 |

## 7) External sources consulted

| source | Gate A | Gate B | tier | used for |
| --- | --- | --- | --- | --- |
| Witchel et al. 2022 — Frontiers in Psychology | 200 OK, full text | CLAIM IN SOURCE (exact coefficients verified) | Tier 1 (peer-reviewed) | C-004 |
| Vignovic & Thompson 2010 — J. Applied Psychology | 200 OK, abstract only | CLAIM IN SOURCE (abstract confirms cross-cultural moderation) | Tier 1 \[ABSTRACT-ONLY\] | C-004, C-007 |
| Kreiner et al. 2002 — J. General Psychology | 200 OK via Exa.ai summary | CLAIM AMBIGUOUS (secondary summary, not primary text) | Tier 1 \[ABSTRACT-ONLY\] | C-004 |
| Nielsen/NN Group F-Pattern 2006 | 200 OK, full text | CLAIM IN SOURCE ("Users won't read your text thoroughly"; N=232) | Tier 2 (industry research lab) | C-003 |
| Scharff et al. — SFA State email format study | 200 OK, full text | CLAIM IN SOURCE (null results on comprehension confirmed verbatim) | Tier 1 (academic experiment) | C-002 |
| ResearchGate — text width and white space | 200 OK, summary | CLAIM IN SOURCE (no significant impact on comprehension) | Tier 1 (peer-reviewed) | C-002 |
| Email Almanac — exclamation points myth | 200 OK, full text | CLAIM IN SOURCE ("Mostly False") | Tier 3 (practitioner) | C-005 |
| EmailToolTester — subject line character limits | 200 OK, summary | CLAIM IN SOURCE (33 char universal limit) | Tier 3 (device testing) | C-006 |
| BuzzStream — 6M subject lines | 200 OK, summary | CLAIM IN SOURCE (9-13 words highest open rate) | Tier 3 (industry dataset) | C-001 |
| ReachIQ — B2B email subject lines | 200 OK, summary | CLAIM IN SOURCE (specificity +9 points open rate) | Tier 3 (industry dataset) | C-001 |
| Pragmatics DOI:10.1016/j.pragma.2022.12.006 | 200 OK, abstract only | CLAIM IN SOURCE (L2 less politeness → more authority + compliance) | Tier 1 \[ABSTRACT-ONLY\] | C-007, CM-05 |

---

Iron law compliance:

* No Cursor skill patches from this raw ingest.
* All Q-bank quotes verified verbatim against attached slice.
* Adversarial review used external sources per search policy.
* One claim killed (CM-10), three scoped down, two flagged UNTESTED.
* Scope: lesson07 only.