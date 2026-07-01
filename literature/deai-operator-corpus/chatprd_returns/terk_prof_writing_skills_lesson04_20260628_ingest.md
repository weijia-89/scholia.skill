# terk_prof_writing_skills_lesson04 — Scholia SF-12 Ingest

P3 adversarial review: 2026-06-28. All analytical claims tagged per grounding rules. Kill list applied.

## Iron Law Requirements

* Closed-corpus run: all claims sourced from attached primary text only (pages 114–136).
* chapters_attested = lesson04 only. No claims from Lesson 3 or Lesson 5 (bleed text on pp. 137–138 excluded from Q-bank and analysis).
* FR-3 enforced: zero open-web research performed.
* Two-lane tags applied to every craft move: deai_removal, tic_enrichment, both, or esl_preserve.
* Schema: SF-12 ≤ 4500 words.

## Source Discovery

Single source — closed corpus:

| Field | Value |
| --- | --- |
| Source | Terk, "Professional Writing Skills: A Write It Well Guide," Lesson 4: Use Clear Language |
| Pages attested | 114–136 (content boundary); pp. 137–138 bleed into Lesson 5 excluded |
| Tier | Tier 3 — Practitioner knowledge (professional writing workbook; prescriptive pedagogy, not peer-reviewed, no empirical methodology) |
| Export file | source_exports/chapters/08_terk_prof_writing_skills_lesson04.txt |
| Access | Attached text export, 2026-06-27 |

## Confidence Scoring

| Factor | Assessment |
| --- | --- |
| Source type | Practitioner workbook — zero empirical evidence cited for any effectiveness claim |
| Methodology | Purely prescriptive: before/after revision pairs with no controlled testing of comprehension, task completion, or writing quality outcomes |
| Conflicts of interest | Author sells the workbook — incentive to frame advice as universally applicable |
| Survivorship bias | All examples show improvement after revision; no cases where "clear" rewrites lost nuance, precision, or register-appropriate formality |
| Recency | Undated in export; references ATMs from the 1970s as historical context; advice is structural and non-perishable |
| Specificity | High — provides verbatim passive-to-active and vague-to-specific revision pairs |
| Replication | Terk participates in a broader plain-language practitioner tradition \[speculative — alignment with specific other sources such as Strunk and White or Williams not verified in this corpus\] |
| Base rate | No data on how often writers successfully adopt these changes or whether adoption improves measurable outcomes |

Confidence ceiling applied: source is expert opinion / practitioner pedagogy with no empirical methodology. Per review protocol, max = 45.

Overall confidence: 42 \[c1=45 (practitioner consensus exists but lacks empirical backing), c2=35 (zero empirical evidence in source or cited by source), c3=45 (advice stable across decades, no serious counter-literature, but also zero replication studies cited)\]. FINAL = 45 (median). Capped at 45 per ceiling.

Craft-move extraction confidence: 45 (at ceiling). Extraction from source text is reliable; whether the extracted moves actually improve writing is a separate, untested question.

## Trustworthiness Assessment

| Red-flag check | Result |
| --- | --- |
| Extraordinary claims | None — advice is conventional |
| Platform selling opportunity | Yes, workbook is a product, but advice is non-controversial |
| Anecdotal success as typical | Revision examples are illustrative, not claimed as empirical proof |
| Missing methodology | No studies cited; pure prescriptive pedagogy — this is the primary limitation |

Verdict: Reliable for extracting craft-move heuristics. Not evidence for empirical claims about writing effectiveness. Every skill-table row is a heuristic, not a validated intervention.

---

## Chapter Summary

Lesson 4 teaches four techniques for sentence-level clarity in professional writing:

1. Use active language — place the actor before the action; eliminate passive constructions that hide agency.
2. Use specific language — replace vague words (recently, some, equipment) with concrete terms (yesterday, five, laptop).
3. Use plain English — swap pompous/formal vocabulary for everyday equivalents (prior to → before; utilize → use; commence → begin).
4. Avoid jargon — eliminate business jargon, nonstandard word usage, and undefined acronyms when writing for audiences who may not share your specialized vocabulary.

Governing principle: language should convey the message swiftly and accurately. Complexity that does not serve precision is waste. \[verified — Q-001\]

---

## Gate A — Verbatim Q-Bank

All 12 quotes verified verbatim against attached primary text, 2026-06-28.

Q-001

* Quote: "Language should convey your message swiftly and accurately."
* Anchor: p. 115, Introduction
* Lane: both
* Note: Core thesis. Clarity framed as speed-and-accuracy function, not aesthetic preference. \[verified — verbatim in source\]

Q-002

* Quote: "Unnecessarily complex language can result in miscommunication, frustration, and wasted time."
* Anchor: p. 115, Introduction
* Lane: deai_removal
* Note: Three failure modes of complexity. Terk addresses human business writing. The surface parallel to RLHF residue patterns (overqualified hedging producing similar reader effects) is plausible but undemonstrated — Terk does not address LLM-generated text. \[speculative — RLHF mapping is analytical overlay, not sourced\]

Q-003

* Quote: "The most effective and impressive writing makes complex ideas seem simple and clear."
* Anchor: p. 115, Introduction
* Lane: both
* Note: Redefines "impressive" as making complexity legible, not performing sophistication. The structural incompatibility between this definition and RLHF hedge-stacking patterns exists only if one accepts the analogy between Terk's human-writer advice and LLM output behavior. \[speculative — RLHF mapping\]

Q-004

* Quote: "Passive language can weaken your writing, confuse your readers, and make your sentences longer."
* Anchor: p. 117, Use Active Language
* Lane: deai_removal
* Note: Three costs of passive voice per Terk. The claim that LLM outputs default heavily to passive constructions is practitioner observation from operator domain knowledge, not from this source. \[speculative — LLM passive-voice frequency claim not verified in this corpus\]

Q-005

* Quote: "To use active language, say who acts, not just what the action is."
* Anchor: p. 117, Use Active Language
* Lane: both
* Note: Operational rule. Actor before action. Testable sentence-level heuristic for revision passes. \[verified — verbatim in source\]

Q-006

* Quote: "When you give instructions, it is particularly important to say clearly what you want your readers to do."
* Anchor: p. 117, Use Active Language
* Lane: tic_enrichment
* Note: Instruction-writing as high-stakes subgenre for active voice. Terk creates a priority context (instructions) where passive voice causes the most damage (ambiguity about who should act). \[verified — verbatim in source\]

Q-007

* Quote: "Specific language makes your writing easier to read, while vague language paints an unclear picture."
* Anchor: p. 122, Use Specific Language
* Lane: both
* Note: Binary framing — specific = easy, vague = unclear. No middle ground acknowledged by Terk. \[verified — verbatim in source\]

Q-008

* Quote: "It can show consideration when you supply your readers with precise information."
* Anchor: p. 122, Use Specific Language
* Lane: tic_enrichment
* Note: Precision framed as reader consideration, not just a clarity technique. Specificity signals care. \[verified — verbatim in source\]

Q-009

* Quote: "Pompous language can confuse, intimidate, amuse, or annoy your readers. Plain English communicates your message more reliably."
* Anchor: p. 126, Use Plain English
* Lane: deai_removal
* Note: Four failure modes of pomposity. "Amuse" is underappreciated — pompous language can make the writer look ridiculous. Whether RLHF outputs trigger these same failure modes is plausible but not demonstrated by Terk. \[speculative — RLHF mapping\]

Q-010

* Quote: "Stuffy words and phrases can force readers to mentally translate your writing into everyday language, which can waste valuable time and create misunderstandings."
* Anchor: p. 126, Use Plain English
* Lane: deai_removal
* Note: The "mental translation" cost heuristic. Every time a reader must decode a pompous phrase, they lose momentum and risk misreading. This is the most operationally useful heuristic in the chapter — it provides a reader-simulation test rather than a word list. \[verified — verbatim in source\]

Q-011

* Quote: "Use plain English instead of jargon when you write to someone who may not recognize general business jargon, or terms that are specific to your job."
* Anchor: p. 132, Avoid Jargon
* Lane: both
* Note: Audience-conditional rule. Jargon is contextual — same term is precise within-team, opaque cross-team. \[verified — verbatim in source\]

Q-012

* Quote: "Define any term that may be new to your reader."
* Anchor: p. 132, Avoid Jargon
* Lane: tic_enrichment
* Note: Operational rule for jargon management. Define on first use when audience may not share vocabulary; do not eliminate universally. \[verified — verbatim in source\]

---

## Coverage Attestation

* chapters_attested: lesson04 only
* Pages covered: 114–136
* Pages excluded: 137–138 (Lesson 5 bleed — incomplete sentences, parallel structure)
* Sections covered: Introduction, Use Active Language (+ practice/answers), Use Specific Language (+ practice/answers), Use Plain English (+ practice/answers), Avoid Jargon (+ practice), Review, What's Next
* Gaps within lesson04 boundary: None

---

## Skill Incorporation Table

All rows are craft heuristics extracted from Tier 3 practitioner pedagogy. None are empirically validated interventions. Confidence ceiling: 45.

| ID | Craft Move | Source Anchor | Lane | Action | Rationale |
| --- | --- | --- | --- | --- | --- |
| S-01 | Actor-before-action heuristic: in revision passes, locate the actor in each sentence; if actor follows action or is missing, restructure. | Q-005, p. 117 | deai_removal | KEEP | Already in decision canon as passive-voice removal. Terk provides a clean operational definition: "say who acts, not just what the action is." Whether canon already has this exact formulation is unverifiable from this corpus. \[unknown — canon content not accessible\] |
| S-02 | Vague-to-specific substitution list as revision checklist: recently → yesterday; some → five; equipment → laptop; contacted → called. | p. 122, vague/specific table | tic_enrichment | ADD | Terk's substitution pairs provide a scannable reference. Useful for catching default vagueness in drafted text ("various," "several," "appropriate"). Whether these specific pairs are already in existing craft-move banks is unverifiable from this corpus. \[unknown — existing bank content not accessible\] |
| S-03 | Pompous-to-plain vocabulary swap table (16 items): prior to → before; utilize → use; commence → begin; etc. | pp. 127–128 | deai_removal | KEEP | Terk's 16-item table participates in a standard plain-language tradition. Whether it overlaps with existing RLHF residue word lists cannot be verified in this corpus. \[unknown — existing list content not accessible\] |
| S-04 | Jargon as audience-relative, not absolute: same term is precise within-team, opaque cross-team. Rule: define on first use for new audiences; do not eliminate universally. | Q-011, Q-012, p. 132 | tic_enrichment | ADD | Terk's audience-conditional framing (Q-011: "someone who may not recognize"; Q-012: "define any term that may be new") prevents blanket jargon stripping. \[inferred — chain: Q-011 + Q-012 → audience-conditional → prevents blanket elimination\] \[esl_preserve\] — the operator should monitor whether jargon over-elimination is a personal pattern; this ingest cannot make directional claims about L1 Chinese writing habits as a population. \[speculative — no evidence for population-level L1 Chinese jargon behavior in this corpus\] |
| S-05 | "Mental translation" cost as pomposity detector: if the reader must decode a phrase into everyday language before understanding it, the phrase fails. | Q-010, p. 126 | deai_removal | ADD | Reader-simulation test for revision passes. More general than a word list: asks "would a reader need to mentally translate this?" If yes, simplify. This is the chapter's most actionable heuristic. |
| S-06 | Specificity as consideration: supplying precise information signals care for the reader, not just clarity. | Q-008, p. 122 | tic_enrichment | CHANGE | Terk adds an interpersonal dimension to specificity — precision is an act of consideration. Whether existing tic rules already include this framing is unverifiable from this corpus. \[unknown — existing rule content not accessible\] |
| S-07 | Passive voice in instructions specifically: instructions are the highest-stakes context for active voice because passive instructions create ambiguity about who should act. | Q-006, p. 117 | both | ADD | Terk creates a priority context: instructions > general prose for active-voice enforcement. Whether existing rules already differentiate by genre cannot be verified. \[unknown — canon content not accessible\] |

---

## Adversarial Self-Review

### Hostile Expert Objections

Objection 1 — No empirical foundation. Terk provides zero empirical evidence that active voice, specific language, plain English, or jargon avoidance improve reader comprehension, task completion, or writing quality in controlled settings. The entire ingest inherits Terk's authority by practitioner assertion. Every skill-incorporation row rests on Tier 3 opinion.

Response: Valid. Confidence capped at 45. All skill-table rows explicitly framed as heuristics, not validated interventions. The ingest does not claim Terk's advice is empirically demonstrated.

Objection 2 — RLHF mapping is the core value-add and is entirely speculative. Terk wrote about human business writers. Mapping Terk's categories onto LLM output patterns assumes mechanistic equivalence between human corporate hedging and RLHF reward shaping. Surface similarity does not demonstrate shared mechanism.

Response: Valid. All RLHF mappings (C-002, C-003, C-004, Q-009 annotation) retagged \[speculative\]. The analogy is plausible and may be useful for generating hypotheses, but it is not evidence. The synthesis does not treat the mapping as established.

Objection 3 — \[esl_preserve\] annotations contain unsupported cultural generalizations. "L1 Chinese writers tend to over-eliminate jargon" and "Chinese business writing norms are more formal" are essentializing claims about a population of over a billion people. No evidence supports these claims in this corpus.

Response: Valid. Reframed from population claims to operator-specific monitoring prompts. The ingest flags jargon over-elimination as a risk to watch for in the operator's own writing, without claiming it is a general L1 Chinese pattern.

### Kill List

| ID | Verdict | Detail |
| --- | --- | --- |
| C-002 | OVERSTATED | RLHF-to-Terk mapping presented as direct parallel. Survives as \[speculative\] with qualifier: surface similarity exists, mechanistic equivalence undemonstrated. |
| C-003 | OVERSTATED | "Directly contradicts" overstates an analogical mapping. Rewritten: structural incompatibility exists only if one accepts the analogy. |
| C-004 | OVERSTATED | LLM passive-voice default claim attributed to Terk by proximity. Reattributed to operator domain knowledge; tagged \[speculative\]. |
| C-005 | WRONG | Claimed \[inferred\] alignment with Strunk and White / Williams / federal guidelines. No inference chain. No verification. Excluded from synthesis. Replaced with: "participates in a broader plain-language tradition \[speculative\]." |
| C-006 | OVERSTATED | "L1 Chinese writers tend to over-eliminate jargon" is an unsupported population generalization. Reframed to operator-specific monitoring prompt. |
| C-007 | OVERSTATED | Same as C-006. Causal mechanism ("uncertainty about audience expectations") also unsupported. |
| C-008 | UNTESTED | References decision canon not in corpus. Cannot appear as load-bearing. |
| C-009 | UNTESTED | "Chinese business writing norms are more formal" — cultural claim with no source. Cannot appear as load-bearing. |
| C-011 | OVERSTATED | Confidence FINAL was 75. Source is expert opinion; ceiling is 45. Reduced to 42/45. |
| C-012 | UNTESTED | References RLHF word lists not in corpus. Cannot appear as load-bearing. |

### What Could Not Be Verified

* Whether Terk's advice aligns with Strunk and White, Williams, or federal plain-language guidelines — requires reading those sources
* Whether existing RLHF residue word lists overlap with Terk's pompous-word table — requires reading decision canon
* Whether existing canon treats passive voice uniformly across genres — requires reading decision canon
* Whether L1 Chinese writers systematically over-eliminate jargon — requires empirical study
* Whether RLHF outputs default to passive voice at higher rates than base models — requires quantitative LLM output analysis

### What Would Change the Assessment

* Controlled studies showing plain-language revisions improve reader comprehension (e.g., federal plain-language mandate outcome data) would promote source confidence from 42 to 70+
* Quantitative analysis of passive-voice frequency in RLHF-trained vs. base LLM outputs would promote C-004 from \[speculative\] to \[verified\]
* Cross-referencing against the decision canon would resolve C-008 and C-012
* Operator-specific writing samples showing jargon over-elimination would promote C-006 from \[speculative\] to \[inferred\] for this operator specifically

---

## Review Section Answers (from primary text, p. 136)

Captured for completeness — the chapter's own fill-in-the-blank review:

1. In active language, the actor comes before the action.
2. Specific language makes your writing easier to read.
3. Plain English communicates your message more reliably.
4. Business writing is full of business jargon.

---

## Recency Gate

No claims in this ingest rely on time-sensitive evidence. Terk's advice is structural writing pedagogy; no recency risk flags apply.

## Steelmanned Synthesis

What survives adversarial review, stated at its strongest:

Terk Lesson 4 provides four operationally distinct heuristics for sentence-level revision. The two with the highest implementation value for the deai/tic pipeline are:

1. S-05 — Mental translation cost detector (Q-010). A general-purpose reader-simulation test: "would a reader need to mentally decode this phrase?" This is more flexible than a word-list approach and catches novel instances of pomposity that a static list would miss. Applicable to both human and LLM-generated text revision, though its effectiveness in either context is asserted by practitioner opinion, not empirical evidence.

2. S-04 — Audience-relative jargon management (Q-011, Q-012). Prevents two failure modes: leaving opaque jargon for unfamiliar readers, and over-stripping precise technical vocabulary. The "define on first use" rule is simple, testable, and context-sensitive.

The remaining moves (S-01 actor-before-action, S-02 vague-to-specific list, S-03 pompous-to-plain table, S-06 specificity-as-consideration, S-07 instructions-priority) are conventional practitioner wisdom. They are useful as revision checklists but add no novel analytical insight to the craft-move bank.

The RLHF-to-Terk mapping — the hypothesis that RLHF residue patterns and human pompous-business-writing patterns share failure modes — is the most interesting analytical claim in this ingest and also the least supported. It is a hypothesis worth testing, not a finding.

## Output Metadata

| Field | Value |
| --- | --- |
| Slug | terk_prof_writing_skills |
| Chapter | lesson04 |
| chapters_attested | lesson04 only |
| Word count target | ≤ 4500 (SF-12) |
| Lane distribution | deai_removal: 4 moves, tic_enrichment: 4 moves, both: 3 moves |
| Q-bank size | 12 verbatim quotes (all verified) |
| Skill table rows | 7 (KEEP: 2, ADD: 4, CHANGE: 1, DROP: 0) |
| Confidence (source) | 42 (capped at 45 per expert-opinion ceiling) |
| Confidence (extraction) | 45 (at ceiling) |
| Claims killed/downgraded | 10 (1 WRONG, 6 OVERSTATED, 3 UNTESTED) |
| P3 review date | 2026-06-28 |
| Save path | chatprd_returns/terk_prof_writing_skills_lesson04_YYYYMMDD_ingest.md |
| Refine path | terk_prof_writing_skills_lesson04_refined_YYYYMMDD.md (optional) |
