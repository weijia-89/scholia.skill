# Terk Professional Writing Skills — Lesson 02 Ingest: Write the First Draft

## Ingest Metadata

| Field | Value |
| --- | --- |
| Slug | terk_prof_writing_skills |
| Chapter | lesson02 — Write the First Draft |
| Source | Professional Writing Skills: A Write It Well Guide, pp. 58–100 |
| Lane | tic_enrichment (primary); deai_removal (secondary) |
| Operator | Wei Jia · L1 Chinese · ESL fairness mandatory |
| Stakes | L3 |
| Schema | scholia SF-12 ≤4500w |
| chapters_attested | lesson02 only |
| Version | v2 — post-adversarial synthesis |

---

## Iron Law Requirements

* Closed-corpus: all claims traced to attached lesson02 text only (FR-3).
* Gate A: every Q-bank quote verified verbatim against source text.
* No page numbers invented; section headers used as anchors.
* Evidence tags per claim: \[verbatim\], \[verified\], \[inferred\], \[speculative\].
* Calibration gate: chapter is prescriptive pedagogy, not empirical. Confidence scores apply to craft-move transferability, not to source truth-claims.

---

## Source Discovery

| Factor | Assessment |
| --- | --- |
| Source type | Practitioner textbook (Tier 3). No peer-reviewed methodology. Confidence ceiling: 45 per framework. |
| Methodology | Heuristic-based; example-driven; no sample sizes or controlled studies. |
| Conflicts of interest | Publisher sells the guide; incentive to frame advice as universally applicable. |
| Survivorship bias | Only "good" revisions shown; no failed attempts or ambiguous cases. |
| Recency | Pre-digital-era conventions (fax references, overhead projectors). Core clarity principles are format-independent. \[inferred\] |
| Specificity | Concrete before/after examples with named clichés. Actionable. |
| Replication | Aligned with Strunk & White (Elements of Style — omit needless words, avoid clichés) \[verified via gutenberg.org/files/37134\]; Williams Style: Lessons in Clarity and Grace (Pearson, 13th ed — clarity, concision, reader-focus) \[verified via pearson.com\]; plain-language advocacy (Kimble — Lifting the Fog of Legalese) \[verified via cap-press.com\]. |
| Base rate | Not addressed — no data on how often writers actually adopt these habits. |

---

## Confidence Scoring (post-adversarial)

All scores respect confidence ceilings: Tier 3 practitioner source caps at 45 for claims resting solely on chapter evidence. Scores above 45 reflect external corroboration.

| ID | Claim cluster | Conf | Tag | Justification |
| --- | --- | --- | --- | --- |
| C-001 | "Planning reduces drafting difficulty" | 45 | \[inferred\] | Practitioner consensus only. No controlled evidence in text or located externally. Capped at Tier 3 ceiling. |
| C-002 | "Cliché openings reduce reader engagement" | 55 | \[inferred\] | Kimble's plain-language advocacy \[verified — cap-press.com\] argues readers prefer plain language; 1987 survey of 425 Michigan judges favored plain language \[verified — michbar.org\]. But no study isolates "cliché openings" specifically; the chapter's before/after examples are persuasive but anecdotal. |
| C-003 | "Lists improve scannability over paragraphs" | 60 | \[inferred\] | COMPLICATED. Schriver 1997 \[verified — archive.org, doi.org/10.31468/cjsdwr.425\] supports lists for information retrieval. Riley & Chaparro 2007 \[verified — exa.ai\] found bulleted sentences improved search speed (N=36). But Campbell 1999 \[verified — theses.gla.ac.uk/4313\] found blanket bulleting slows reading and reduces memory versus plain text. Jansen 2014 \[verified — jbe-platform.com\] found bulleted lists reduce recall of surrounding text and that benefits diminish with heterogeneous items. Net: lists aid scanning for homogeneous, search-oriented tasks; they can harm comprehension in continuous reading. The chapter's unqualified claim is overstated. |
| C-004 | "Parallel structure in lists aids comprehension" | 55 | \[inferred\] | Standard composition pedagogy across Strunk & White, Williams. No disconfirming evidence located, but no experimental study isolated either. |
| C-005 | "Transitions improve readability" | 45 | \[inferred\] | Practitioner consensus only. The chapter's boldfaced example is illustrative but anecdotal. Capped at Tier 3 ceiling. |
| C-006 | "Headings help readers find information" | 70 | \[inferred\] | Schriver 1997 \[verified\] covers headings, hierarchy, white space as aids to scanning. Multiple document-design sources converge. Downgraded from 80 in v1 via overconfidence pass — the chapter's own claim is unsupported by cited research; external alignment is strong but indirect. \[c1=75 source convergence, c2=70 no direct replication of this exact claim, c3=65 no adversarial counter located; FINAL=70\] |
| C-007 | "Cliché patterns overlap with RLHF model output" | 65 | \[verified\] | Wikipedia AIFICTREF \[verified — en.wikipedia.org/wiki/Wikipedia:AIFICTREF\] lists "I hope this helps," "Let me know if," "Of course!" as AI chatbot artifacts. DeepWiki humanizer patterns \[verified — deepwiki.com\] catalog "Certainly!", "I hope this helps," "feel free to ask" as Pattern 20 (Chatbot Artifacts). The chapter's cliché list ("Please be advised," "Do not hesitate to contact") overlaps partially — both target bureaucratic hedging. Precise overlap: the chapter's "Do not hesitate to contact this writer" maps directly to RLHF "Don't hesitate to reach out." The chapter's "I am writing to inform you" maps to RLHF "I'd be happy to help." Overlap is partial, not total — the chapter also targets pre-digital formalism ("Pursuant to," "Attached herewith") that RLHF models do not typically reproduce. |
| C-008 | "Personal contact in openings/closings improves writing" | 40 | \[speculative\] | The chapter recommends warmth patterns ("Thank you for asking," "Please let me know") that directly overlap with RLHF sycophancy signals. Anthropic sycophancy research \[verified — anthropic.com/research/towards-understanding-sycophancy-in-language-models\] demonstrates RLHF models over-produce agreeable, warm responses. The chapter's advice is sound for human-authored email but becomes a liability when implemented by LLMs — the same pattern that reads as "personal" from a human reads as "sycophantic" from a model. Confidence capped at 40 due to this fundamental ambiguity. |

---

## Epistemic Rigor Notes

* Survivorship bias audit: The chapter shows only successful revisions. Campbell 1999 demonstrates that formatting changes (including lists) can impair reading — a failure mode the chapter never acknowledges.
* Dunning-Kruger guard: The chapter treats all business writing as a single genre. Formal legal, regulatory, and scientific contexts may require conventions the chapter dismisses as "clichés." \[inferred\]
* Adversarial self-review: The chapter's blanket hostility to phrases like "Pursuant to" and "Please be advised" ignores contexts (legal, compliance) where such phrasing carries precise meaning. Craft moves borrowed from this chapter require register-scope tags.
* Gap: No discussion of digital-native formats (Slack, chat, documentation-as-code). The chapter assumes email and printed memos.

---

## Gate A — Verbatim Q-Bank

All quotes verified against attached lesson02 text.

Q-001: "The first few lines of any piece of writing are extremely important. It is in the opening paragraph that you must catch your readers' attention, set the right tone, and make it clear what you are writing about." Section: Write an Inviting Opening

Q-002: "A transition is a word, phrase, or sentence that relates a new topic to the previous one, smoothly connecting the parts of a piece of writing." Section: Transitions

Q-003: "Transitions are rather like the cartilage and tendons that hold your bones together. They form a connective tissue that links your ideas to one another." Section: Transitions

Q-004: "Your goal as a writer is to help readers find information as quickly as possible. To show consideration and speed things up for your reader, look for opportunities to present information in lists." Section: Using Lists

Q-005: "The items in a list must be parallel—presented in the same forms." Section: Guidelines for Using Lists, guideline 4

Q-006: "Headings make your documents easier to understand by presenting your reader with concise themes." Section: Using Headings

Q-007: "A strong closing achieves the following goals: makes a final personal contact with readers (a crucial factor when you're writing to influence); wraps up any loose ends; tells readers clearly what happens next; uses specific language" Section: Closing Paragraphs

Q-008: "When you have completed your writing plan, the first draft almost writes itself. You've already done the hard work—deciding what you want to accomplish, finding the right words to express your main points, and selecting and organizing the facts and ideas you need to influence or inform readers." Section: Introduction

Q-009: "You can use a list in business writing—and, often, you should use a list—whenever you present three or more related pieces of information." Section: Guidelines for Using Lists

Q-010: "As a general rule, keep lists short. There should be no more than five or six items on your list." Section: Guidelines for Using Lists, guideline 5

---

## Coverage Attestation

chapters_attested: lesson02 only

The chapter covers six instructional segments:

1. Review Your Writing Plan — checklist for plan validation before drafting
2. Write an Inviting Opening — criteria (personal contact, attention, key sentence, brevity); cliché avoidance
3. Summaries — executive summary guidance for reports/proposals
4. Transitions — connective words/phrases taxonomy (additions, contrasts, comparisons, emphasis, result, summary)
5. Using Lists — five guidelines (introduce, relevance, consistency, parallelism, organize for reader)
6. Closing Paragraphs — goals (personal contact, loose ends, next steps, specific language); cliché replacement

Not covered in this chapter: revision, grammar, tone calibration, audience analysis beyond plan review. \[These may appear in other lessons; not attested.\]

---

## Skill Incorporation Table

| \# | Craft Move (from chapter) | Lane | Disposition | Rationale |
| --- | --- | --- | --- | --- |
| 1 | Replace cliché openings ("Please be advised," "Per your request," "Enclosed please find") with direct, specific language | deai_removal | KEEP | Partial overlap with RLHF chatbot artifacts verified (C-007). The chapter's cliché list targets both pre-digital formalism and patterns RLHF models reproduce. Scoping note: keep "Pursuant to" in legal register; "Attached herewith" is pre-digital, not RLHF-correlated. |
| 2 | Transition-word taxonomy: additions, contrasts, comparisons, emphasis, result, summary | tic_enrichment | KEEP | Useful as a diversity checklist against RLHF-correlated transition over-reliance ("Additionally," "Furthermore," "Moreover" clustering). The chapter's full list provides alternatives. Required pre-implementation step: cross-reference against 0628 decision canon RLHF transition signal list; if overlap exceeds 50%, add explicit "do not over-apply" warning. |
| 3 | Five guidelines for lists: introduce, all items belong, consistency, parallelism, organize with subpoints | both | CHANGE | Lists aid scanning for homogeneous items in search-oriented tasks (Riley & Chaparro 2007). But blanket bulleting slows reading (Campbell 1999) and can reduce recall of surrounding text (Jansen 2014). The chapter's unqualified "always list 3+ items" rule (Q-009) is overstated. Revised rule: list when items are homogeneous and readers need to scan/search; use prose when items are heterogeneous or when surrounding context matters for comprehension. The five formatting guidelines (introduce, belong, consistent, parallel, organize) remain sound. |
| 4 | Closing-paragraph pattern: personal contact + loose ends + what happens next + specific language | tic_enrichment | CHANGE | The four-part structure is sound, but "makes a final personal contact with readers" collides with RLHF sycophancy patterns (C-008). In technical documentation, forced personal contact reads as model-generated warmth. Apply selectively: emails/proposals = yes; docs/READMEs/RFCs = suppress personal-contact element, retain loose-ends + next-steps + specific-language. |
| 5 | Executive summary guidance: most important message first, keep short, same order as main document | tic_enrichment | CHANGE | The structural heuristic is clean, but "half a page to a full page" length guidance is register-dependent. For PR/RFC summaries: 2-3 sentences. For reports/proposals: half page. For board memos: one page. Tag with register. |
| 6 | "Plan makes the draft write itself" framing | both | DROP | Motivational scaffolding, not a transferable craft move. No evidence that planning makes drafting automatic. This framing could produce complacency about revision — a dangerous message when the next four lessons (per the chapter's own closing) address revision. |
| 7 | Headings as information-architecture tool: break up dense text, force grouping, aid scanning | tic_enrichment | KEEP | Schriver 1997 corroborates \[verified\]. The chapter's with/without headings example (sales meeting email) is a compelling demonstration. No modification needed. |
| 8 | Blanket ban on formal register phrases ("Pursuant to," "Please be advised") | deai_removal | CHANGE | \[esl_preserve\] — L1-Chinese writers may use formal register phrases as legitimate transfer from Chinese business conventions (敬语 / 书面语). Blanket removal risks erasing culturally-grounded formality. Revised rule: distinguish three categories: (a) RLHF-generated formality = remove; (b) pre-digital business formalism with no current communicative value = flag for writer review; (c) writer-intentional formality with L1-transfer basis = preserve, tag \[esl_preserve\]. |

---

## Kill List

| Claim | Verdict | Rationale |
| --- | --- | --- |
| C-001 "Planning reduces drafting difficulty" | OVERSTATED | Practitioner consensus only, capped at 45. The chapter's stronger claim that "the first draft almost writes itself" (Q-008) is motivational, not empirical. Excluded as load-bearing claim; retained as background context only. |
| C-003 "Lists improve scannability over paragraphs" | OVERSTATED | Campbell 1999 directly disconfirms blanket list superiority. Jansen 2014 shows benefits are conditional on item homogeneity. Survives with scope constraint: lists aid search tasks on homogeneous items; they can harm reading fluency and surrounding-text recall. |
| C-005 "Transitions improve readability" | UNTESTED | No experimental evidence located for or against. Capped at 45. May not appear as load-bearing in synthesis. |
| C-008 "Personal contact improves writing" | OVERSTATED | Sound for human-authored email; becomes an RLHF sycophancy vector when implemented by LLMs. Survives only with lane tag: apply in human-authored contexts, suppress when the writing agent is an LLM. |

---

## Adversarial Second-Pass (P3)

Three strongest objections a hostile domain expert would raise:

1. The chapter's cliché list and RLHF artifact lists are drawn from different eras and only partially overlap. Treating them as equivalent conflates pre-digital business formalism with model-generated sycophancy. They share a surface pattern (bureaucratic hedging) but have different root causes and different removal strategies. Resolution: the skill incorporation table now separates three categories in row 8 — RLHF-generated, pre-digital, and L1-transfer formality.

2. The chapter recommends warmth patterns ("Thank you for asking," "Please let me know") that Anthropic's sycophancy research demonstrates RLHF models over-produce. Borrowing these as craft moves for LLM-assisted writing would increase, not decrease, AI-detectable signals. Resolution: row 4 now suppresses personal-contact element in LLM-authored contexts.

3. The "lists improve scannability" claim is not supported by the weight of experimental evidence. Campbell 1999 and Jansen 2014 both find conditions under which lists impair reading and recall. The chapter presents lists as universally superior, which is false. Resolution: row 3 now scopes list usage to homogeneous-item, search-oriented tasks.

Counterarguments that fail:

* "The chapter is too old to be useful" — the core principles (clarity, directness, reader orientation) are format-independent and hold across Strunk & White (1918/revised), Williams (13 editions through 2020+), and Kimble (2006).
* "Cliché lists are culturally biased" — the specific phrases listed are English-language business clichés with no cultural-preservation argument outside the \[esl_preserve\] scope already handled in row 8.

---

## Overconfidence Check

v1 had 2 of 6 scores at 75 and 1 at 80 (50% at 75+). Mandatory downward-pressure pass applied:

* C-003 (was 75): Campbell 1999 provides direct disconfirming evidence. Downgraded to 60.
* C-004 (was 75): No disconfirming evidence, but no experimental study isolated. Downgraded to 55.
* C-006 (was 80): External alignment is strong but indirect — no study tested this exact chapter's headings claim. Downgraded to 70.

Post-adjustment: 0 of 8 scores at 80+. Distribution is appropriate for a Tier 3 practitioner source with partial external corroboration.

---

## What Could Not Be Verified

* Whether the specific cliché phrases listed in the chapter reduce reader engagement (no experimental study isolates these exact phrases)
* Whether transitions as a category improve readability (practitioner consensus only; no experimental evidence located)
* Whether L1-Chinese formal register phrases are actually perceived differently from RLHF-generated formality by readers (would require controlled study with ESL-aware readers)
* The chapter's implicit claim that its advice generalizes beyond email/memo format (no evidence for or against application to modern formats)

Evidence that would change the assessment:

* A controlled study comparing reader engagement with vs. without the specific cliché phrases the chapter lists → would promote C-002 above 55
* Eye-tracking study on list vs. paragraph comprehension with heterogeneous business content → would resolve the C-003 scope question
* Corpus analysis of RLHF model output frequencies for the chapter's specific cliché phrases → would tighten C-007 overlap estimate

---

## RECENCY RISK

\[RECENCY RISK: Anthropic sycophancy research cited (2023-2024) and arxiv papers on RLHF detectability (2025) are within 12 months of training cutoff. Verified via live fetch but flagged per protocol.\]

---

## Open Questions Resolved

| Question (from v1) | Resolution |
| --- | --- |
| Cross-reference transition taxonomy against 0628 RLHF signal list? | Required pre-implementation step. Added to row 2 rationale. |
| Summary length guidance needs validation? | Scoped by register in row 5. Half-page for reports, 2-3 sentences for PRs/RFCs. |
| No digital-native formatting guidance? | Gap confirmed. Not fillable from this source. Acknowledged in Coverage Attestation. |
