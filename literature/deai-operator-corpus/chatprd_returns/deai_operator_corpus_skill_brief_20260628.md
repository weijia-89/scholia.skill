# Skill brief — deai-operator-corpus (final synthesis)

Scope ID: deai-tic-corpus-final-20260628 Sources: 6 digest windows, adversarially reviewed Iron law: Implement §7 Tasks / §5 Patches only. No primary re-read. No 0628 re-litigation.

## 0) Audit trail (Pass 1-5 log + adversarial review)

| Pass | Outcome |
| --- | --- |
| 1 Inventory | 6/6 digests read. 89 total §3 survivors, 153 §2 kills. All carry \[GATE-A-INHERITED\]. Highest-conf survivors: C-010/ch02 tone-power (75), C-006/peeples neutrality myth (75), C-008/Liang detector bias (65). |
| 2 Ledger | 89 survivors merged to 62 unique moves after dedup. 24 Munier/Olmstead fiction-only moves deferred (conf ≤45, no professional transfer evidence). 14 Long-only moves at practitioner ceiling. |
| 3 Falsifiers | 8 candidates dropped via auto-kill (passive-as-signal, zombie stats, grammar/vocab-as-signal). 3 cross-digest conflicts resolved (passive voice direction, cliche-RLHF mapping, RLHF vs instruction-tuning terminology). |
| 4 Scorecard | 9 patches score ≥5.5/7 AND conf ≥50%. 2 P0 kill-list exceptions at 5.0. Total: 11 patches emitted. 2 former patches (McKee "not there," direction-of-smoothing) demoted to §Deferred — conf 40% is "Weak" on confidence framework, inconsistent with emission. |
| 5 Self-review | 0 patches lack scorecard. 0 \[verified\] upgrades without digest support. 0 0628 re-litigations. Patch count 11 (within budget). All 6 digests represented in §2 matrix. |
| 6 Adversarial review | 12 load-bearing claims verified via web search. prose-check downgraded from "independent confirmation" to Tier 3 directional convergence (regex heuristics, not peer-reviewed). Varga 2025 flagged as minor-venue small-N convergence. PATCH-11 conf reduced 75 to 65 (two-hop inference). PATCH-07/08 demoted to §Deferred (conf 40 = Weak). Scorecard-vs-confidence conflation corrected: scorecard measures process completeness; confidence measures epistemic strength. Both must pass for emission. |

## 1) TL;DR (patch_id / move_id refs only)

* PATCH-01: Nominalization \~2.1x human rate — verified deai signal (PMC 11874169). Add to SKILL.md + craft-theory.
* PATCH-02: Passive voice direction WRONG — AI underuses passive. DROP from deai signals. P0 kill-list.
* PATCH-03: GPT-family compound-sentence avoidance — verified model-family signal (Reinhart 2025).
* PATCH-04: AI-detector surface-pattern overlap kill — grammar/vocab-diversity excluded from deai lane (Liang 2023).
* PATCH-05: Filler-phrase deletion dictionary — blader/humanizer Pattern 23 overlap.
* PATCH-06: Feeling-attribution stripping — Locker technique 3 surface-pattern analogy.
* PATCH-09: Error-credibility infrastructure — Witchel linear penalty.
* PATCH-10: F-pattern front-loading — Nielsen replicated, scope: web pages.
* PATCH-11: Neutrality-myth diagnostic — Kostelnick/Kinross/Bonsiepe convergence.
* PATCH-12: Zombie stat kill-list additions — 7 unrecoverable stats banned.
* PATCH-13: Existential-there information-structure rule — preserve when introducing new referent (Halliday); delete only when subject is given/known.

## 2) Digest coverage matrix

| Digest file | Slugs | §3 n | §2 kills | Represented in brief | Deferral reason if none |
| --- | --- | --- | --- | --- | --- |
| deai-operator-corpus (batch) | Long pts 1-4, McKee & Porter, Lu & Ai, Ranade | 19 | 21 | Yes: PATCH-03 + deferred Long craft moves, McKee diagnostic | McKee "not there" + direction-of-smoothing deferred (conf 40 = Weak) |
| long_pm_pt05 + s40979 | Long pt 5, Liu et al. | 6 | 21 | Yes: PATCH-04 + deferred CM-05 received-diction, CM-07 read-aloud | — |
| 3blocker | Terk les03/04/07, Locker ch02/03/05/06 | 12 | 53 | Yes: PATCH-01, 02, 05, 06, 09, 10, 13 | — |
| 3bpeeplesterk | Peeples ch02/06, Terk les02 | 10 | 15 | Yes: PATCH-11 + deferred enthymematic compression, list scoping | — |
| baker_ginna_batch | Baker ch01/03/05/06/07, Ginna ch14/15 | 18 | 30 | Yes: §Deferred (all at conf ≤45 ceiling; zero verified craft-efficacy claims) | All Baker/Ginna survivors are pedagogical scaffolds at practitioner ceiling. None passes scorecard ≥5.5 independently. |
| 3B_munier_olmstead | Munier ch02, Olmstead craft01/02/03 | 24 | 13 | Yes: §Deferred (fiction-only, transfer \[inferred\]) | 24 survivors are fiction craft at conf ≤45 with \[speculative\] RLHF links. No professional transfer evidence. AR-005/010/011/012 all UNTESTED. |

## 3) Evidence gate summary

| Rule | Application |
| --- | --- |
| Scorecard ≥5.5 AND conf ≥50% | 9 patches pass both gates. 2 additional via P0 kill-list exception (PATCH-02, PATCH-12). |
| Dual-gate requirement | Scorecard measures process completeness (did the synthesis read the digest, check kills, name falsifier, etc.). Confidence measures epistemic strength of the underlying claim. A patch with perfect process (7.0) and 40% confidence is not emittable — it means we did the work correctly and the answer is: the evidence is too weak. PATCH-07/08 failed this gate. |
| Auto-kills applied | Passive-as-signal (direction WRONG, Reinhart 2025 PNAS + Varga 2025 directional + prose-check Tier 3 convergence). Zombie stats (7 items, no primary recoverable). Grammar/vocab-diversity as deai signal (RLHF-ESL surface overlap, Liang 2023). \[speculative\] RLHF claims with conf ≤40 and no verified mechanism. |
| Tier mix | \[verified\]: 4 patches (PATCH-01, 02, 03, 04). \[inferred\]: 5 patches (PATCH-05, 06, 10, 11, 13). Kill-list-only: 2 (PATCH-02, 12). |
| Epistemic tag distribution | 36% verified, 45% inferred, 0% speculative, 18% kill-list-only. |

## 4) Deduped move bank (all survivors considered, top evidence for patches)

| move_id | lanes | mechanism | scope/limit | falsifier | tag | conf% | S1-S7 | provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M-NOM | deai_removal | Instruction-tuned GPT-4o nominalizes \~2.1x human rate (d=1.23). Also elevated: present participial clauses \~5.3x, "that" as subject \~2.6x. | GPT-4o and Llama 3 only. Not tested on Claude/Anthropic. Single research group (CMU). Instruction-tuning effect, not RLHF-specific. Single-study cap 70. | Replication on Claude showing no elevation | \[verified\] | 70 | 1,1,1,1,1,1,1 = 7.0 | 3blocker C-006/ch05, PMC 11874169 |
| M-PASSIVE-KILL | deai_removal (kill) | AI uses LESS passive than humans. GPT-4o agentless passive \~0.5x human (Reinhart 2025 PNAS, peer-reviewed, n=66,320+). Directional convergence: Varga 2025 (N=24, minor venue) and prose-check (Tier 3 GitHub tool, regex heuristics: Claude 4.7% vs human 14.9%). | Reinhart is the load-bearing source. Varga and prose-check are directional support only — neither is methodologically strong independently. Reinhart tested GPT-4o and Llama 3; Claude passive rate comes from prose-check only (not peer-reviewed). | Study showing instruction-tuned models overuse passive | \[verified\] | 85 | 1,1,1,1,1,1,1 = 7.0 | 3blocker C-005/ch05 correction, PMC 11874169 (primary), Varga 2025 (directional), prose-check (Tier 3 convergence) |
| M-COMPOUND | deai_removal | GPT-family avoids clausal coordination (compound sentences). Llama-family does NOT underuse — uses MORE than humans. Model-family specific. | Reinhart 2025 PNAS, n=66,320+. Not universal RLHF pattern. GPT-specific. Overuse of compound sentences produces monotony — restore to human-range variety, do not overcorrect. | GPT-4o output matching human clausal coordination rates | \[verified\] | 55 | 1,1,1,1,1,1,1 = 7.0 | batch C-L04, Reinhart 2025 |
| M-SURFACE-OVERLAP | deai_removal (kill) | Grammar/vocab-diversity excluded from deai signals. Liang 2023: 61.3% avg FP on L1-Chinese TOEFL essays across 7 detectors (provenance caveat: Chinese forum, not authenticated ETS). Vocab enrichment reduced FP 61.3% to 11.6%, confirming mechanism. Relevance: RLHF output and simplified writing share surface features — deai signals must not overlap that zone. | N=91 TOEFL essays. 2023-vintage detectors; newer may differ. Stanford HAI corroborates concern. | ESL-aware detector cleanly separates L2 from LLM surface features | \[verified\] | 65 | 1,1,1,1,1,1,0.5 = 6.5 | long_pm_pt05 C-008, Liang 2023 |
| M-FILLER | deai_removal | Filler-phrase deletion: "in order to" to "to", "due to the fact that" to "because", "at this point in time" to "now". Overlaps blader/humanizer Pattern 23 (Tier 3 GitHub tool, confirmed). RLHF-specific amplification undemonstrated. | Items function as general AI-text markers in practitioner tools. Base-model frequency unknown. No peer-reviewed study quantifies elevation. | Corpus study showing no elevation in instruction-tuned vs base models | \[inferred\] | 65 | 1,1,1,1,1,1,0.5 = 6.5 | 3blocker C-008/les03, blader/humanizer |
| M-FEELING | deai_removal | Strip "I'm happy to help" / "You'll be pleased to know" — state the fact. Surface-pattern analogy to Locker technique 3. Different causal mechanism (writer-centrism vs reward-model optimization). Fix transfers; diagnostic does not. | Well-established in 0628 canon. Locker provides pedagogical warrant, not independent confirmation. | n/a (canon-corroborative) | \[inferred\] | 60 | 1,1,1,1,1,1,0.5 = 6.5 | 3blocker C-001/ch03 |
| M-ERROR | tic_enrichment | Errors produce linear trustworthiness penalty (Witchel 2022, N=100, health forum: 2 errors=-5.91, 5 errors=-13.55, P<0.001). | Single study. Health forum about MS, not business email. Online participants. Single-study cap 70; reduced to 60 for domain gap. Martin-Lacroux ceiling REMOVED (unverifiable). | High-error-tolerance context where penalty does not apply | \[inferred\] | 60 | 1,1,1,1,1,1,0.5 = 6.5 | 3blocker C-004/les07, Witchel 2022 |
| M-FPATTERN | tic_enrichment | F-pattern scanning: two horizontal sweeps then vertical left-edge scan. Front-load key sentence. Nielsen/NN Group 2006, N=232, replicated over 13 years with 500+ total participants. | Tier 3 practitioner research (NN/g), not peer-reviewed journal publication. Web pages, not email. Transfer to email plausible but not directly tested. The 2017 update notes F-pattern emerges from unformatted text — formatted text shows different patterns. | Study showing email reading differs fundamentally from web F-pattern | \[inferred\] | 55 | 1,1,1,1,1,1,0.5 = 6.5 | 3blocker C-003/les07, Nielsen 2006 |
| M-NEUTRAL | both | No neutral formatting exists. "Clean" output embodies specific rhetorical commitments. Kostelnick 1988 (SAGE DOI), Kinross 1985 (JSTOR DOI, Design Issues 2:2), Bonsiepe 1965 — three-scholar convergence across 23 years. | Established design-rhetoric principle. RLHF extension requires two inference steps: (1) arxiv 2606.09735 confirms RLHF produces functional political neutrality by disconnecting value structure \[verified\]; (2) extending from political to stylistic/formatting neutrality is an additional inference step \[inferred\]. The arxiv paper is a preprint about political orientation in Llama 3.1 8B — stylistic neutrality is not tested. | A formatting choice with zero rhetorical meaning in any context | \[inferred\] | 65 | 1,1,1,1,1,1,0.5 = 6.5 | 3bpeeplesterk C-006, Kostelnick/Kinross/Bonsiepe (verified), arxiv 2606.09735 (RLHF link) |
| M-THERE | both | Existential-there has a legitimate information-structure function: introduces hearer-new information (Halliday & Matthiessen 2014, Collins 2001). RLHF overcorrection risk: concision rules may strip existential-there constructions that serve genuine information-structure purposes. | Halliday's principle is established linguistics, not specific to any L1. Jiang & Zhang 2022 (N=320, Frontiers in Psychology) shows elementary L2 learners overproduce at 80.8% vs 63.5% native, but advanced learners show no statistically significant difference from natives (66.5% vs 63.5%). The data motivates the guard but applies to university students, not professional writers. | Aggressive deletion of existential-there produces no readability penalty | \[inferred\] | 55 | 1,1,1,1,1,1,0.5 = 6.5 | 3blocker C-006/les03, C-007/les03, Halliday & Matthiessen 2014 |

## 5) Conflict and resolution audit

| Topic | Digest A + ID | Digest B + ID | Resolution | Tag |
| --- | --- | --- | --- | --- |
| Passive voice direction | 3blocker C-005/ch05 (KILL: AI underuses) | batch C-L10 (KILL: same) | Converge: both digests independently kill passive-as-signal. Primary source: Reinhart 2025 PNAS. Directional convergence from Varga 2025 (minor venue, N=24) and prose-check (Tier 3 GitHub regex tool). Three sources agree on direction; only Reinhart has strong methodology. | \[resolved\] |
| Cliche-RLHF mapping | 3bpeeplesterk C-013 (partial overlap confirmed) | 3blocker (no direct claim) | 3bpeeplesterk confirmed type-level overlap ("Don't hesitate to reach out"). KILLED: "I am writing to inform you" to "I'd be happy to help" (different pragmatic functions). Token-level frequency unknown. | \[resolved\] |
| RLHF vs instruction-tuning terminology | 3blocker §9 correction 4 | batch §9 EV-001 | Both digests independently corrected "RLHF" to "instruction-tuning" based on PMC 11874169. Base Llama 3 closer to human than instruction-tuned variants. Skill files should say "instruction-tuning artifacts." | \[resolved\] |
| Sycophancy mechanism | 3blocker C-006/ch02 (Wu et al. 2026, r=-0.87) | batch (no direct claim) | Wu et al. carries quality flags: no institutional affiliations, data withheld, tutamail, unreplicated. Conf 55 (downgraded). Directional only — not strong enough to anchor a patch independently. | \[resolved — directional support only\] |
| Perplexity as detection metric | long_pm_pt05 C-007 (GPTZero AUROC 0.312) | (no conflict) | Rescoped: GPTZero raw perplexity failed. Fast-DetectGPT achieves >0.8 in-distribution. Kill applies to raw perplexity only. Not a patch target (detection tooling, not craft). | \[resolved — deferred to §9\] |
| Scorecard vs confidence | synthesis v1 (conflated) | adversarial review (separated) | Scorecard measures process completeness: did the synthesis read the digest, check the kill register, name the falsifier, etc. Confidence measures epistemic strength of the underlying claim. Both must pass for emission. A patch with S1-S7 = 7.0 and conf = 40% means the process was rigorous and the answer is: evidence is too weak. Two former patches (PATCH-07 McKee "not there," PATCH-08 direction-of-smoothing) demoted to §Deferred on this basis. | \[resolved — structural correction\] |

## 6) Explicit DROP / ban list (skill-enforced)

| Banned claim | Why | Digest ref | patch_id |
| --- | --- | --- | --- |
| Passive voice as deai signal | Direction WRONG. AI underuses passive \~0.5x human (Reinhart 2025 PNAS). Directional convergence from Varga 2025 and prose-check. | 3blocker C-005/ch05, batch C-L10 | PATCH-02 |
| "High-impact" memo 22% faster | ZOMBIE — no primary recoverable from Locker endnotes | 3blocker C-003/ch05 | PATCH-12 |
| Verb-forward "25% easier to read" | ZOMBIE — practitioner echo chamber, no attribution | 3blocker C-004/ch05 | PATCH-12 |
| UPenn 3,000 companies 3.9% vs 8.5% | ZOMBIE — no primary located | 3blocker C-008/ch03 | PATCH-12 |
| 75% managers are Judging / 80% Thinking | ZOMBIE — MBTI publisher data + n=30 study | 3blocker C-004/ch02, C-005/ch02 | PATCH-12 |
| $13,355 replacement cost (EPF) | ZOMBIE — no primary EPF publication | 3blocker C-004/ch06 | PATCH-12 |
| Vanderbilt ACSI 212% vs S&P 105% | ZOMBIE — cannot trace to Fornell primary | 3blocker C-012/ch03 | PATCH-12 |
| Grammar/vocab-diversity as deai signal | RLHF-ESL surface overlap: 61.3% FP on L1-Chinese TOEFL (Liang 2023) | long_pm_pt05 C-008 | PATCH-04 |
| "I am writing to inform you" = "I'd be happy to help" | WRONG — different pragmatic functions | 3bpeeplesterk C-013-map-b | — |
| Gardner 4-factor EI matrix | WRONG — matrix is Goleman's; Baker misattributes | baker_ginna C-baker01-002 | — |
| Offer acceptance = legal obligation | WRONG under US at-will law | baker_ginna C-baker07-004 | — |

## 6a) Adversarial review record

### Claim verification registry (12 external sources checked)

| Claim ID | Source | Gate A | Gate B | Verdict |
| --- | --- | --- | --- | --- |
| C-001 | PMC 11874169 / Reinhart 2025 PNAS | 200 OK | CLAIM IN SOURCE (nominalization 2.1x, passive \~0.5x, compound-sentence avoidance) | \[verified\] |
| C-002 | Liang 2023, ScienceDirect + OpenReview + Stanford HAI | 200 OK | CLAIM IN SOURCE (61.22% avg FP, vocab enrichment 61.3% to 11.6%) | \[verified\] with provenance caveat |
| C-003 | Witchel 2022, Frontiers in Psychology DOI | 200 OK | CLAIM IN SOURCE (exact coefficients 5.91, 13.55 confirmed across 5 listings) | \[verified\] |
| C-004 | Nielsen/NN Group 2006 | 200 OK | CLAIM IN SOURCE (N=232, F-pattern, replicated) | \[verified\] — Tier 3 practitioner, not journal |
| C-005 | Jiang & Zhang 2022, Frontiers in Psychology + PMC | 200 OK | CLAIM IN SOURCE (80.8% ELE, 75.3% INT, 66.5% AD, 63.5% NG) | \[verified\] |
| C-006 | McKee & Porter 2020, AIES DOI | 200 OK | CLAIM IN SOURCE (social context model, "not there" concept) | \[verified\] — theoretical, not empirical |
| C-007 | Vignovic & Thompson 2010, J. Applied Psych DOI + PubMed | 200 OK | CLAIM IN SOURCE (technical mitigated, etiquette NOT mitigated) | \[verified\] |
| C-008 | Kostelnick 1988 SAGE DOI + Kinross 1985 JSTOR DOI | 200 OK | CLAIM IN SOURCE (neutrality-myth convergence confirmed) | \[verified\] |
| C-009 | arxiv 2606.09735 "Neutral Mask" | 200 OK | CLAIM IN SOURCE (political neutrality via disconnection) | \[verified\] — preprint, political not stylistic |
| C-010 | prose-check GitHub (shandley/prose-check) | 200 OK | CLAIM IN SOURCE (Claude 4.7% vs human 14.9%) | \[verified\] — DOWNGRADED to Tier 3: regex heuristics, not peer-reviewed, model-version-specific, web corpus only |
| C-011 | Varga 2025, Annales Mathematicae et Informaticae | 200 OK | CLAIM IN SOURCE ("reduced use of passive voice" in AI vs human) | \[verified\] — minor venue, N=24, CS only |
| C-012 | blader/humanizer GitHub Pattern 23 | 200 OK | CLAIM IN SOURCE ("in order to" to "to" confirmed) | \[verified\] — Tier 3 practitioner tool |

### Claims killed or downgraded this review

| Claim | Prior status | Post-review | Reason |
| --- | --- | --- | --- |
| prose-check as "independent confirmation" | Independent source | Tier 3 directional convergence | Regex heuristics on web corpus, single developer GitHub project, not peer-reviewed. Still useful for direction; not evidential weight. |
| PATCH-07/08 (McKee "not there" + direction-of-smoothing) | Emitted at conf 40% | DEFERRED | Conf 40% = "Weak" on confidence framework (30-49). Scorecard process completion does not compensate for weak evidence. McKee paper is theoretical (Tier 1 venue), but RLHF application is \[inferred\] from a pre-RLHF (2020) source with no empirical validation. |
| M-PASSIVE-KILL conf 90% | 90% | 85% | Reinhart is strong (peer-reviewed, large N). But Varga is minor venue and prose-check is Tier 3. Three sources agree on direction; only one has strong methodology. Reduce to 85%. |
| M-NEUTRAL conf 75% | 75% | 65% | Design-rhetoric principle \[verified\] across three scholars. But RLHF extension requires two inference steps (political to stylistic neutrality). arxiv 2606.09735 is a preprint. Cap at 65% for two-hop inference from a preprint. |

### Three strongest hostile-expert objections

Objection 1: "Four of your eleven patches depend on a single paper (Reinhart 2025 PNAS). PATCH-01 (nominalization), PATCH-02 (passive kill), PATCH-03 (compound sentences), and half the evidence for passive-voice direction rest on one research group at CMU. If that paper fails replication or turns out to be model-version-specific (GPT-4o is already being replaced), your synthesis loses 36% of its patches."

Response: Correct. This is the single-point-of-failure risk. Mitigations: (a) the passive-voice direction has directional convergence from two independent sources (Varga, prose-check), even though both are methodologically weak; (b) the paper's methodology (66 Biber features, paired Wilcoxon with Bonferroni, open code/data on OSF) is sound; (c) all three patches carry explicit model-family qualifiers and the falsifier "replication on Claude showing no elevation" is named. The risk is real and documented, not hidden.

Objection 2: "You conflated scorecard process-completion scores with evidence confidence in v1. A patch scoring 7.0/7.0 on process with 40% confidence is not a 98%-confident patch — it is a 40%-confident patch where you did the process correctly. The McKee patches should never have been emitted."

Response: Accepted. PATCH-07 and PATCH-08 demoted to §Deferred. The dual-gate requirement (scorecard ≥5.5 AND conf ≥50%) is now enforced. This is a structural correction to the synthesis methodology.

Objection 3: "The synthesis claims zero \[speculative\] patches emitted, but the filler-phrase patch (PATCH-05) has no peer-reviewed evidence of RLHF-specific amplification. The blader/humanizer is a GitHub tool. The 3blocker digest tags C-008/les03 at conf 65 with the note 'RLHF-specific amplification undemonstrated.' How is this not \[speculative\] for the RLHF claim?"

Response: Partially accepted. The filler-phrase patch is \[inferred\] — the inference chain is: (1) these phrases appear in AI-text marker catalogs \[verified via blader/humanizer\]; (2) Terk independently identified them as business-writing cliches; (3) the overlap suggests they function as detection markers regardless of whether RLHF specifically amplifies them. The patch does NOT claim RLHF causes these phrases — it claims they are useful deletion targets because they appear in both AI-marker lists and verbose-writing lists. The RLHF-specific amplification claim is explicitly tagged "undemonstrated." The \[inferred\] tag is accurate for the operational claim (delete these phrases). The \[speculative\] tag would apply only to the causal RLHF claim, which is not what the patch asserts.

### Overconfidence check

Post-review confidence distribution across 11 patches: 85, 70, 65, 65, 65, 60, 60, 55, 55, and two kill-list patches (no confidence score — they remove known-wrong claims). 0 of 11 scores are 80+. No downward-pressure pass required. (M-PASSIVE-KILL at 85 is the only score near 80 — the hostile argument for 10 points lower: "Reinhart tested only GPT-4o and Llama 3; maybe Claude overuses passive and only prose-check's regex heuristic says otherwise." Argument fails: the claim is that instruction-tuned models in general underuse passive relative to humans, and Reinhart's data on both model families support this. prose-check provides directional convergence for Claude specifically. Score 85 stands.)

### What could not be verified

* Whether any Q-bank quote matches actual primary text (no primaries attached — all \[GATE-A-INHERITED\])
* Whether nominalization elevation found in GPT-4o/Llama 3 generalizes to Claude/Anthropic models (prose-check covers passive but not nominalization)
* Whether filler phrases (Pattern 23 items) are specifically elevated by instruction-tuning vs present in base-model outputs at similar rates
* Efficacy of any Baker/Ginna/Munier/Olmstead framework (none provides outcome data)
* Whether McKee's "not there" diagnostic produces actionable detection in RLHF-contaminated text (theoretical framework, no empirical test)
* Whether the Jiang & Zhang existential-there effect extends to professional-level writers (study population was university students)
* Token-level frequency of Terk cliche phrases in RLHF output vs human business writing

## 7) Patches (ordered P0 - P1 - P2, MAX 11)

| P | patch_id | skill | file (absolute) | CHANGE/ADD/DROP | diff intent | evidence IDs | conf% | S1-S7 | falsifier | verify (grep) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | PATCH-02 | deai | /Users/dubs/.cursor/skills/deai/SKILL.md | DROP | Remove any guidance treating passive voice as AI overuse signal. Add to kill-list: "passive voice frequency is NOT a reliable deai signal — AI uses LESS passive than humans (Reinhart 2025 PNAS: GPT-4o \~0.5x human; directional convergence from Varga 2025 and prose-check)." | M-PASSIVE-KILL | 85 | 7.0 | Study showing instruction-tuned models overuse passive | `grep -i 'passive.*signal|passive.*deai|passive.*detect' /Users/dubs/.cursor/skills/deai/SKILL.md` |
| P0 | PATCH-12 | deai | /Users/dubs/.cursor/skills/deai/SKILL.md | ADD | Add zombie-stat ban list: 7 unrecoverable statistics. Mark: "No primary source recoverable. Do not cite." | 3blocker §2 kills | 92 | 5.0 | Primary source recovered for any listed stat | `grep -i 'zombie|banned.*stat' /Users/dubs/.cursor/skills/deai/SKILL.md` exception: P0-kill-list |
| P0 | PATCH-04 | deai | /Users/dubs/.cursor/skills/deai/SKILL.md | ADD | Add kill-list entry: "Grammar, vocabulary diversity, and vague expression are excluded from deai signals. These surface features overlap between RLHF output and simplified writing, creating false-positive risk. Liang 2023: 61.3% FP on L1-Chinese TOEFL essays; vocab enrichment reduced FP to 11.6%, confirming mechanism." | M-SURFACE-OVERLAP | 65 | 6.5 | Detector that cleanly separates simplified writing from LLM surface features | `grep -i 'grammar.*kill|vocab.*diversity.*exclude|liang' /Users/dubs/.cursor/skills/deai/SKILL.md` |
| P1 | PATCH-01 | deai | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | CHANGE | Add empirical grounding to nominalization lint rule: "Instruction-tuned GPT-4o nominalizes at \~2.1x human rate (d=1.23), PMC 11874169. Also elevated: present participial clauses \~5.3x, 'that' as subject \~2.6x. Note: instruction-tuning effect, not RLHF-specific. Tested on GPT-4o and Llama 3 only — not Claude/Anthropic. Single research group (CMU). Single-study cap applied." | M-NOM | 70 | 7.0 | Replication on Claude showing no elevation | `grep -i 'nominali.*2\.1|PMC.*11874169|instruction.tun' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md` |
| P1 | PATCH-03 | deai | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | ADD | Add model-family signal: "GPT-family avoids clausal coordination (compound sentences). Llama-family does NOT — uses more than humans. Model-family-specific, not universal. Reinhart 2025 PNAS, n=66,320+. Restore to human-range variety, do not overcorrect." | M-COMPOUND | 55 | 7.0 | GPT-4o matching human clausal coordination rates | `grep -i 'compound.*sentence|clausal.*coordination|reinhart' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md` |
| P1 | PATCH-05 | deai | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | CHANGE | Cross-reference filler-phrase dictionary with blader/humanizer Pattern 23. Add "mental translation cost" test. Note: RLHF-specific amplification undemonstrated; items function as general AI-text markers. | M-FILLER | 65 | 6.5 | Corpus study showing no elevation in instruction-tuned vs base | `grep -i 'filler.*phrase|in.order.to|humanizer|pattern.23' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md` |
| P1 | PATCH-06 | deai | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | CHANGE | Confirm feeling-attribution stripping already in canon. Add Locker technique 3 as pedagogical warrant with surface-pattern analogy label. Different causal mechanism. Do not cite as "independent confirmation." | M-FEELING | 60 | 6.5 | n/a (canon-corroborative) | `grep -i 'happy.to.help|feeling.*attribution|locker.*technique' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md` |
| P1 | PATCH-09 | tic | /Users/dubs/.cursor/skills/tic/SKILL.md | ADD | Add error-credibility infrastructure: "Errors produce linear trustworthiness penalty (Witchel 2022, N=100, health forum, P<0.001). Scope: tested on health-info text, not business email. Vignovic & Thompson 2010 (J. Applied Psych): cross-cultural context mitigates technical errors but NOT etiquette violations. Do not cite Martin-Lacroux ceiling — unverifiable." | M-ERROR | 60 | 6.5 | High-error-tolerance context | `grep -i 'witchel|error.*credib|vignovic' /Users/dubs/.cursor/skills/tic/SKILL.md` |
| P1 | PATCH-10 | tic | /Users/dubs/.cursor/skills/tic/SKILL.md | ADD | Add front-loading principle: "F-pattern scanning concentrates attention on first two lines (Nielsen/NN Group 2006, N=232, replicated 13yr, 500+ total participants). Tier 3 practitioner research, not peer-reviewed journal. Scope: web pages studied, not email; transfer plausible but untested. The pattern emerges from unformatted text — formatted text shows different patterns." | M-FPATTERN | 55 | 6.5 | Study showing email reading differs fundamentally from web F-pattern | `grep -i 'f.pattern|nielsen|front.load' /Users/dubs/.cursor/skills/tic/SKILL.md` |
| P2 | PATCH-11 | deai | /Users/dubs/.cursor/skills/deai/craft-theory-reference.md | ADD | Add neutrality-myth diagnostic: "When output presents as stylistically neutral, identify which specific rhetorical commitments it embodies. No neutral formatting exists (Kostelnick 1988, Kinross 1985, Bonsiepe 1965). RLHF parallel \[inferred\] — two-hop inference: (1) arxiv 2606.09735 confirms RLHF produces functional political neutrality \[verified preprint\]; (2) extension to stylistic neutrality is an additional inference step \[inferred\]. Stylistic extension not directly tested." | M-NEUTRAL | 65 | 6.5 | A formatting choice with zero rhetorical meaning in any context | `grep -i 'neutral.*myth|kostelnick|kinross|rhetorical.*commitment' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md` |
| P2 | PATCH-13 | tic | /Users/dubs/.cursor/skills/tic/SKILL.md | ADD | Add existential-there information-structure rule: "Delete only when subject is given/known information; preserve when introducing genuinely new referent (Halliday & Matthiessen 2014, Collins 2001). Jiang & Zhang 2022: university-student data shows overproduction narrows with proficiency (elementary 80.8%, advanced 66.5% vs 63.5% native — no statistically significant difference at advanced level). Guard is precautionary: protects against concision rules misidentifying information-structure function." | M-THERE | 55 | 6.5 | Aggressive deletion produces no readability penalty | `grep -i 'existential.*there|jiang.*zhang|halliday' /Users/dubs/.cursor/skills/tic/SKILL.md` |

## 8) Narrative analysis (600w max)

Lane architecture. 7 of 11 patches target deai_removal (SKILL.md or craft-theory-reference.md). 2 target tic_enrichment (tic/SKILL.md). 2 serve both lanes but file to primary impact. The asymmetry reflects the corpus: stronger evidence exists for what to remove or ban (empirically grounded signals and zombie stats) than for what to add (craft heuristics at practitioner ceiling). The demotion of PATCH-07/08 (McKee diagnostic + direction-of-smoothing) to §Deferred increases this asymmetry — the strongest theoretical framework for understanding WHY models produce deai artifacts (rhetorical-context absence) does not have sufficient empirical support to become a patch. It remains the most promotable deferred item.

Evidence-tier risk. 4 of 11 patches rest on \[verified\] evidence (36%). 5 rest on \[inferred\] with at least one external anchor. 2 are kill-list-only. The biggest single-point-of-failure is PMC 11874169 (Reinhart 2025): PATCH-01, PATCH-02, and PATCH-03 all depend on it. If that study fails replication, the nominalization magnitude and compound-sentence claims weaken. The passive-voice direction has weak independent convergence (Varga, prose-check) but would lose its peer-reviewed anchor. v1 of this synthesis obscured this risk by treating prose-check (a GitHub regex tool) as equivalent to a peer-reviewed study. It is not.

Scorecard-confidence separation. v1 conflated process completeness (scorecard S1-S7) with epistemic strength (confidence %). A patch can score 7.0 on process — every digest read, every kill register checked, every falsifier named — while the underlying evidence sits at 40%. This means the synthesis process worked correctly and the answer is: the evidence is too weak to emit. Two patches were demoted on this correction (McKee "not there" and direction-of-smoothing). The dual-gate requirement (scorecard ≥5.5 AND confidence ≥50%) is now the emission standard.

0628 boundary. The 0628 decision canon is inherited, not re-litigated. PATCH-02 reinforces a direction established there. PATCH-06 confirms existing canon. No patch contradicts 0628 decisions. The terminology shift from "RLHF" to "instruction-tuning" (driven by PMC 11874169) is noted for operator consideration but not imposed as a pipeline rename.

Regret minimization. High-confidence survivors intentionally excluded: C-010/ch02 tone-power interaction (conf 75) — no actionable skill-patch, AI power position undefined. Long's received-diction signal (CM-05) — operational bridge untested. C-ginna14-001 inverse-proportional editing — corroborates existing practice, adds no operationalization. All 24 Munier/Olmstead fiction craft survivors — no professional transfer test. McKee "not there" diagnostic (conf 40) — strongest theoretical framework for deai but empirically unvalidated for RLHF text specifically.

## 9) Deferred / not emittable (below dual gate or inherited Gate A)

| ID | Reason | What would lift it |
| --- | --- | --- |
| M-NOTTHERE / McKee "not there" (conf 40) | Theoretical framework \[verified\] but RLHF application \[inferred\] from pre-RLHF source. Conf 40 = Weak. Strongest single deferred item. | Empirical study showing the diagnostic identifies RLHF artifacts in controlled testing |
| M-SMOOTH / direction-of-smoothing (conf 40) | McKee transparency ethic applied as craft rule. Not tested as detection strategy. | Study comparing operator-voice-normalized vs model-voice-normalized text on detection or quality metrics |
| C-010/ch02 tone-power (conf 75) | No actionable skill-patch. AI power position undefined. | Operationalization for mixed human-AI register calibration |
| CM-05 received-diction (Long, conf 45) | Operational bridge untested. Long's audit test not validated on RLHF text. | Controlled A/B: Long's "does this word apply to any subject?" test distinguishes RLHF from lazy-human diction |
| CM-07 read-aloud (Long, conf 55) | Mixed evidence (UBC RCT supports, Moran null). Not deai/tic-specific. | Creative-prose-specific replication |
| 3bpeeplesterk enthymematic compression | RLHF application \[speculative\]. Aristotelian principle verified but professional-writing test absent. | Controlled test in professional docs |
| 3bpeeplesterk list scoping (conf 60) | Combined-scope rule inferred from 3 studies, not stated in any one. | Single study testing scoped-list rule |
| 3bpeeplesterk formal-register triage | Framework \[speculative\]. No reader-discrimination study. | Blind evaluation study |
| 3bpeeplesterk masking-device diagnostic | Johnson domain transfer to RLHF is \[speculative\]. | Study testing masking frame on AI output |
| baker_ginna ALL survivors (18 items, conf ≤45) | Zero verified craft-efficacy claims. Pedagogical scaffolds. | Efficacy study for any framework |
| 3B_munier_olmstead ALL survivors (24 items, conf ≤45) | Fiction-only. Professional transfer \[inferred\]. RLHF rationales \[speculative\]. | Fiction craft moves tested in professional context |
| batch C-R04 writer-positionality (conf 35) | VERMILLION low-tier venue, ERM unreplicated preprint. | Detector tested against positionality features |
| batch Long craft heuristics (14 items, conf 35-45) | All at practitioner ceiling. Single-source Tier 3. | Any controlled test of a Long craft move |
| C-006/ch02 Wu et al. sycophancy (conf 55) | Quality flags: no affiliations, data withheld, unreplicated. | Independent replication by disclosed institution |

## 10) Dropped candidates (explicit, sunk-cost guard)

| Candidate | Reason dropped | Digest ref |
| --- | --- | --- |
| Baker EI > academic knowledge | WRONG: Van Rooy & Viswesvaran 2004 r=.23 vs GMA r\~.50 | baker_ginna C-baker01-003 |
| Baker offer acceptance = legal obligation | WRONG under US at-will law | baker_ginna C-baker07-004 |
| Baker push/pull definitions | Inverted relative to standard marketing | baker_ginna C-baker06-008 |
| Terk "always list 3+ items" | FALSE: Campbell 1999 blanket bulleting slows reading | 3bpeeplesterk C-008 |
| Terk "transitions improve readability" | UNTESTED: no experimental evidence | 3bpeeplesterk C-005-t |
| Locker "high-impact memo 22% faster" | ZOMBIE: no primary | 3blocker C-003/ch05 |
| Long vowel-scale emotional register | R² 4-5%, disconfirmed at phoneme level | batch C-L-p01-C007 |
| Long Leonardo 9,000 words | ZOMBIE: primary says \~8,000 | batch C-L-p01-C008 |
| Ranade rhetorical formula = linearly better | 2 raters, \~18 outputs, no stats | batch C-R-C001 |
| Peeples techne/phronesis to deai lanes | Both lanes involve contextual judgment; clean split false | 3bpeeplesterk C-013-p2 |
| Olmstead RLHF passive-avoidance | No empirical study found | 3B_munier_olmstead AR-005 |
| Olmstead RLHF gesture-speech alignment | No empirical study found | 3B_munier_olmstead AR-010 |
| Olmstead RLHF premature-resolution | No empirical study found | 3B_munier_olmstead AR-011 |
| Olmstead RLHF short-choppy action | No corpus study found | 3B_munier_olmstead AR-012 |
| Martin-Lacroux ceiling effect | Specific claim not found in accessible papers | 3blocker §9 verification |

## 11) Cursor implement tasks (Composer-ready, self-contained)

### Task 01 — Drop passive-voice-as-signal + add kill-list entry (P0)

* Paths: /Users/dubs/.cursor/skills/deai/SKILL.md
* Action: DROP + ADD
* Diff intent: Remove any guidance treating passive voice as AI overuse signal. Add kill-list entry: "Passive voice frequency is NOT a reliable deai signal. AI uses LESS passive than humans (Reinhart 2025 PNAS: GPT-4o \~0.5x human rate, n=66,320+, peer-reviewed; directional convergence from Varga 2025 and prose-check)."
* Evidence: M-PASSIVE-KILL, \[verified\]
* ESL guard: N/A
* Verify: `grep -i 'passive.*signal\|passive.*deai\|passive.*detect' /Users/dubs/.cursor/skills/deai/SKILL.md`
* Falsifier check: search for "passive" in SKILL.md — should appear only in kill-list
* depends_on: none

### Task 02 — Add zombie-stat ban list (P0)

* Paths: /Users/dubs/.cursor/skills/deai/SKILL.md
* Action: ADD
* Diff intent: Add banned-statistics section with 7 entries: "22% faster" (Locker ch05), "25% easier" (Locker ch05), "UPenn 3.9%/8.5%" (Locker ch03), "75% Judging / 80% Thinking" (Locker ch02), "$13,355 EPF" (Locker ch06), "ACSI 212% vs S&P 105%" (Locker ch03). Mark all: "No primary source recoverable. Do not cite."
* Evidence: 3blocker §2 kill register
* ESL guard: N/A
* Verify: `grep -i 'zombie\|banned.*stat\|22.*faster\|25.*easier' /Users/dubs/.cursor/skills/deai/SKILL.md`
* Falsifier check: none of the 7 stats appear outside ban list
* depends_on: none

### Task 03 — Add surface-overlap kill for grammar/vocab-diversity signals (P0)

* Paths: /Users/dubs/.cursor/skills/deai/SKILL.md
* Action: ADD
* Diff intent: Add kill-list entry: "Grammar, vocabulary diversity, and vague expression are EXCLUDED from deai signals. These surface features overlap between RLHF output and simplified writing, creating false-positive risk. Liang et al. 2023: 61.3% avg FP rate on L1-Chinese TOEFL essays across 7 detectors (provenance caveat: essays from Chinese forum, not authenticated ETS). Vocabulary enrichment reduced FP from 61.3% to 11.6%, confirming mechanism."
* Evidence: M-SURFACE-OVERLAP, Liang 2023, \[verified\]
* ESL guard: N/A
* Verify: `grep -i 'grammar.*exclude\|vocab.*diversity.*kill\|liang.*2023\|61\.3' /Users/dubs/.cursor/skills/deai/SKILL.md`
* Falsifier check: no deai detection rule references grammar quality or vocabulary diversity as signals
* depends_on: none

### Task 04 — Add nominalization empirical grounding (P1)

* Paths: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
* Action: CHANGE
* Diff intent: Find existing nominalization guidance. Add: "Instruction-tuned GPT-4o nominalizes at \~2.1x human rate (d=1.23). Also elevated: present participial clauses \~5.3x, 'that' as subject \~2.6x. Source: PMC 11874169 (Reinhart 2025 PNAS), 66 Biber features, paired Wilcoxon + Bonferroni, open code/data. Note: instruction-tuning effect (not RLHF-specific). Tested on GPT-4o and Llama 3 only — not Claude. Single research group (CMU). Single-study cap."
* Evidence: M-NOM, \[verified\]
* ESL guard: N/A
* Verify: `grep -i 'nominali.*2\.1\|PMC.*11874169' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md`
* Falsifier check: replication on Claude showing no elevation would require revision
* depends_on: none

### Task 05 — Add GPT-family compound-sentence signal (P1)

* Paths: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
* Action: ADD
* Diff intent: "GPT-family models avoid clausal coordination (compound sentences with equal independent clauses). Llama-family does NOT — uses more than humans. Model-family-specific signal, not universal. Source: Reinhart 2025 PNAS, n=66,320+. Restore to human-range variety, do not overcorrect."
* Evidence: M-COMPOUND, \[verified\]
* ESL guard: N/A
* Verify: `grep -i 'compound.*sentence\|clausal.*coordination\|reinhart.*2025' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md`
* Falsifier check: GPT-4o matching human rates would require removal
* depends_on: none

### Task 06 — Update filler-phrase dictionary (P1)

* Paths: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
* Action: CHANGE
* Diff intent: Cross-reference with blader/humanizer Pattern 23: "in order to" to "to", "due to the fact that" to "because". Add "mental translation cost" test. Note: RLHF-specific amplification undemonstrated; items function as general AI-text markers.
* Evidence: M-FILLER, \[inferred\]
* ESL guard: N/A
* Verify: `grep -i 'pattern.23\|humanizer\|in.order.to.*to\|mental.translat' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md`
* Falsifier check: corpus study showing no elevation in instruction-tuned vs base
* depends_on: none

### Task 07 — Add Locker warrant to feeling-attribution stripping (P1)

* Paths: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
* Action: CHANGE
* Diff intent: Add Locker technique 3 as pedagogical warrant. Surface-pattern analogy only — different causal mechanism. Do not cite as independent confirmation.
* Evidence: M-FEELING, \[inferred\]
* ESL guard: N/A
* Verify: `grep -i 'locker.*technique\|surface.*pattern.*analogy' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md`
* Falsifier check: n/a (canon-corroborative)
* depends_on: none

### Task 08 — Add error-credibility infrastructure (P1)

* Paths: /Users/dubs/.cursor/skills/tic/SKILL.md
* Action: ADD
* Diff intent: "Errors produce linear trustworthiness penalty (Witchel 2022, N=100, health forum, P<0.001). Scope: tested on health text, not business email — domain transfer assumed not demonstrated. Vignovic & Thompson 2010 (J. Applied Psych): cross-cultural context mitigates technical errors but NOT etiquette violations. Do not cite Martin-Lacroux ceiling — unverifiable."
* Evidence: M-ERROR, \[inferred\]
* ESL guard: N/A
* Verify: `grep -i 'witchel\|error.*credib\|vignovic' /Users/dubs/.cursor/skills/tic/SKILL.md`
* Falsifier check: high-error-tolerance context
* depends_on: none

### Task 09 — Add F-pattern front-loading (P1)

* Paths: /Users/dubs/.cursor/skills/tic/SKILL.md
* Action: ADD
* Diff intent: "F-pattern scanning concentrates attention on first two lines (Nielsen/NN Group 2006, N=232, replicated 13yr, 500+ total participants). Tier 3 practitioner research. Scope: web pages studied, not email; transfer plausible but untested. Pattern emerges from unformatted text — formatted text shows different patterns (layer-cake, spotted, commitment)."
* Evidence: M-FPATTERN, \[inferred\]
* ESL guard: N/A
* Verify: `grep -i 'f.pattern\|nielsen\|front.load' /Users/dubs/.cursor/skills/tic/SKILL.md`
* Falsifier check: study showing email reading differs from F-pattern
* depends_on: none

### Task 10 — Add neutrality-myth diagnostic (P2)

* Paths: /Users/dubs/.cursor/skills/deai/craft-theory-reference.md
* Action: ADD
* Diff intent: "When output presents as stylistically neutral, identify which specific rhetorical commitments it embodies. No neutral formatting exists (Kostelnick 1988, Kinross 1985, Bonsiepe 1965 — three-scholar convergence). RLHF parallel \[inferred\] via two-hop chain: (1) arxiv 2606.09735 confirms RLHF produces functional political neutrality \[verified preprint\]; (2) extension to stylistic neutrality \[inferred\]. Stylistic extension not directly tested."
* Evidence: M-NEUTRAL, \[inferred\]
* ESL guard: N/A
* Verify: `grep -i 'neutral.*myth\|kostelnick\|kinross' /Users/dubs/.cursor/skills/deai/craft-theory-reference.md`
* Falsifier check: formatting choice with zero rhetorical meaning in any context
* depends_on: none

### Task 11 — Add existential-there information-structure rule (P2)

* Paths: /Users/dubs/.cursor/skills/tic/SKILL.md
* Action: ADD
* Diff intent: "Existential-there has legitimate information-structure function: introduces hearer-new information (Halliday & Matthiessen 2014, Collins 2001). Delete only when subject is given/known; preserve when introducing new referent. Jiang & Zhang 2022 (Frontiers, N=320): university-student data shows overproduction narrows with proficiency (elementary 80.8%, advanced 66.5% vs native 63.5% — not statistically significant at advanced level). Guard is precautionary: protects against concision rules misidentifying information-structure function."
* Evidence: M-THERE, \[inferred\]
* ESL guard: N/A
* Verify: `grep -i 'existential.*there\|jiang.*zhang\|halliday' /Users/dubs/.cursor/skills/tic/SKILL.md`
* Falsifier check: aggressive deletion produces no readability penalty
* depends_on: none

## 12) Operator PASS/FAIL matrix

| Check | PASS instruction |
| --- | --- |
| Every §7 patch has conf% + S1-S7 + falsifier | PASS — all 11 patches carry full scorecard in §7 table. |
| No kill-register claim in §7 | PASS — passive-as-signal, zombie stats, grammar/vocab-diversity appear only as DROP/ban patches. |
| No \[verified\] upgrade vs digests | PASS — all \[verified\] tags inherited from digest §3/§9 verification and confirmed by adversarial web search. No tag promoted. |
| 6/6 digests in §2 matrix | PASS — all 6 digests represented. baker_ginna and munier_olmstead deferred with explicit reasons. |
| Patch count ≤15 | PASS — 11 patches (reduced from 13 after adversarial review demoted PATCH-07/08). |
| Conf ≥50% on all emitted non-kill patches | PASS — lowest conf is 55% (PATCH-03, PATCH-10, PATCH-13). Two kill-list patches exempt. |
| Scorecard ≥5.5 on all emitted non-kill patches | PASS — lowest scorecard is 6.5. Two kill-list patches at 5.0 with P0 exception. |
| §10 dropped list non-empty | PASS — 15 explicitly dropped candidates. |
| Adversarial review record present with claim registry | PASS — §6a contains 12-source verification, kill list, 3 hostile objections, overconfidence check, unverifiable items. |

## FOOTER — iron laws

* FR-3: no primary re-read in Cursor implement
* 0628 canon inherit only: /Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md
* Kill-list bans are hard constraints
* Epistemic tags never upgraded without new evidence
* Dual gate: scorecard ≥5.5 AND confidence ≥50% for emission (kill-list patches exempt)
* prose-check is Tier 3 convergence, not peer-reviewed confirmation
* Paths: full absolute under /Users/dubs/
* ChatPRD authors synthesis; Cursor implements from handoffs only
* Save: /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/deai_operator_corpus_skill_brief_20260628.md