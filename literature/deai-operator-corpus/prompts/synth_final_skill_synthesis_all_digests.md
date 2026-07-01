# ChatPRD — Final skill synthesis (all digest windows → minimal patches)

Platform: **Opus 4.6** · Scope: `deai-operator-corpus-final-synthesis-20260628`  
Project: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`  
Contract v0.2: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

Epistemic bar: **review-rigor + epistemic-planning** — every load-bearing patch row must carry tag, falsifier, confidence scorecard, and digest provenance. No row without falsifier is emittable.

---

## Attach (7 — hard limit)

**Attach order (mandatory):**
1. `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` — **MUST READ AND FOLLOW**
2. `/Users/dubs/Downloads/Refined digest _ deai-operator-corpus _batch_.md`
3. `/Users/dubs/Downloads/Refined digest _ long_2018_portable_mentor_part05 _ s40979_2024_ai_writing.md`
4. `/Users/dubs/Downloads/Refined digest _ baker_ginna_batch.md`
5. `/Users/dubs/Downloads/Refined digest _ 3bpeeplesterk.md`
6. `/Users/dubs/Downloads/3blocker.md`
7. `/Users/dubs/Downloads/Refined digest _ 3B_munier_olmstead.md`

**Paste:** this prompt (do not attach).

**Gate A status for this window:** Digests are adversarially reviewed artifacts. **Do not** re-read primaries or block on missing `*_ATTACH.txt`. Carry forward digest §3–§5 rows and §4 Q-IDs. Flag `[GATE-A-INHERITED]` rows in §Deferred unless patch is P0 kill-list / verified-external only.

---

## Mission

Synthesize **all six digests** into one **minimal, high-evidence, epistemically audited** implement plan for **deai** + **tic** skills only.

**Optimize for:** fewest patches with highest operator impact and **lowest epistemic regret** — not encyclopedic coverage.

**Success criteria (all required in output):**
1. Every digest inventoried with survivor/kill counts reconciled
2. Every emitted patch has scorecard ≥ 5.5/7 → **≥90% conf** OR explicit P0 kill-list exception (documented)
3. Every emitted patch has named falsifier checkable post-implement
4. Explicit **dropped** and **deferred** lists with reasons (no silent omission)
5. Cross-digest conflicts resolved or marked `[unresolved]` — never blended
6. Composer-ready §Tasks with self-contained verify commands

**Target files (absolute paths only):**
| File | Role |
| ---- | ---- |
| `/Users/dubs/.cursor/skills/deai/SKILL.md` | deai signals, kill-list, detection bias |
| `/Users/dubs/.cursor/skills/deai/craft-theory-reference.md` | craft moves, bibliography |
| `/Users/dubs/.cursor/skills/tic/SKILL.md` | tic moves, ESL preserve |
| `/Users/dubs/Projects/piranesi.skill/research-projects/0628-deai-signal-removal/deai-signal-removal_decision_canon.md` | **inherit only — do not re-litigate** |

**Alignment check (read from digest cross-refs, do not re-open plan as authority):** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/plans/deai_tic_skill_incorporation_plan.md`

---

## Epistemic operating mode (mandatory)

Execute **five internal passes** before writing final output. Log each pass in §0 Audit trail (brief bullets — not prose essays).

### Pass 1 — Surface map (inventory)

For **each** attached digest, extract and record:
| field | required |
| digest filename | yes |
| source slugs / ingests covered | yes |
| §3 survivor count | yes |
| §2 kill count | yes |
| lane tags present | yes |
| Gate A note (inherited / verified / absent) | yes |
| highest-confidence survivor ID + conf | yes |

**Completeness gate:** 6 digests × row = 6 rows. If any attach unread → STOP and list missing.

### Pass 2 — Claims ledger (merge without lossy compression)

Build unified ledger from all §3 rows + §5 craft moves:
- Assign stable `move_id` (reuse digest IDs when present; new IDs only for deduped merges)
- **Provenance chain:** `digest_file · source_slug · claim_id · Q-ID(s)`
- **Epistemic tag per row:** `[verified]` | `[inferred]` | `[speculative]` | `[unknown]` — copy from digest; **never upgrade**
- **Mechanism + scope/limit + falsifier** — copy or compress to one line each; empty mechanism → max MODERATE, not STRONG

**Dedupe rule:** Same mechanism across digests → one row, multiple provenance entries. **Do not** merge rows with conflicting mechanisms or directional claims.

### Pass 3 — Adversarial falsifiers (dialectic)

For each candidate patch (before emit):
1. Write **thesis:** "Patch X because …"
2. Write **antithesis:** strongest counter from any digest §2 kill register or downgraded row
3. Write **synthesis:** emit / defer / drop with cited digest IDs

**Hard kills (auto-drop even if in §3):**
| claim class | reason | digest evidence |
| passive voice as deai signal | directional WRONG | deai batch, 3blocker §2 |
| zombie stats / MBTI workforce % / unrecoverable Locker endnotes | no primary | multiple §2 |
| `[speculative]` RLHF bridge, conf ≤40, no verified mechanism | not emittable | review-rigor <4.5 |
| abstract-only magnitude for patch justification | not emittable | review-rigor S1 |

### Pass 4 — Patch scorecard (per emitted row)

Adapt review-rigor scorecard for digest synthesis:

| # | Axis | 0 | 0.5 | 1 |
| --- | --- | --- | --- | --- |
| S1 | Digest body read | not opened | skim TL;DR only | §3 row + provenance read |
| S2 | Falsifier | absent | vague | named empirical check post-patch |
| S3 | Blast radius | unknown | one skill file | all touched files + ESL impact named |
| S4 | Reciprocal search | none | single digest | checked ≥2 digests for conflict |
| S5 | Numerics | from memory | partial cite | every stat traces to digest ID |
| S6 | Kill-register cross-check | not checked | partial | confirmed claim not in any §2 kill |
| S7 | Implement evidence | hypothesis | digest-only | digest `[verified]` external OR P0 kill-list |

**Mapping:** 7→98% · 6.5→95% · 6→92% · 5.5→90% · 5→87% · **<5.5 → not emittable** (→ §Deferred with reason).

**P0 kill-list exception:** DROP/ban patches may emit at 5.0 if they **remove** a known-wrong claim (passive-as-signal, zombie stat) — mark `exception: P0-kill-list`.

### Pass 5 — Self-review (before save)

Re-read your own §5 Patches table and answer:
1. Any patch lacking scorecard breakdown? → fix or drop
2. Any `[verified]` tag you added without digest support? → downgrade or drop
3. Any ESL regression (`native-norm`, `sound more natural`)? → drop
4. Any 0628 canon re-litigation? → drop
5. Patch count >15? → cut P2 first, document cuts in §Dropped
6. **Coverage:** any digest with zero representation in move bank AND zero explicit deferral reason? → fix

If >15% of patches downgraded in self-review → prefix output: `**Self-review flag:** prior draft over-claimed on …`

---

## Evidence inclusion rules (strict)

Include patch **only if ALL:**
1. Survivor in digest §3 (never §2 kill register)
2. Scorecard **≥5.5/7** OR P0 kill-list exception
3. Operator-actionable — changes agent behavior, not background essay
4. ESL-safe — `[esl_preserve]` honored; no deficit framing

**Prefer (P0 candidates — verify still pass scorecard):**
- Verified model-family patterns: GPT compound-sentence avoidance (Reinhart 2025), nominalization ~2x (PMC 11874169 / Locker C-006)
- McKee rhetorical-context / direction-of-smoothing (Tier-1 source; label RLHF link `[inferred]`)
- Skill **kill-list** bans (passive-as-signal, zombie stats, promoted speculative→verified)
- Tic moves with verified reader behavior: error-credibility (Witchel), F-pattern (Nielsen — **scope: web pages not email**)
- Jones/Lu & Ai non-deficit framing where present

**Always defer (§Deferred, not §Patches):**
- `[GATE-A-INHERITED]` + no `[verified]` external anchor
- `[unresolved]` cross-source conflicts
- Munier/Olmstead/Baker employment hooks unless conf ≥45 AND unique mechanism not elsewhere
- Any patch you cannot name falsifier for

**Patch budget:** ≤12 target · 15 hard max · prefer 8–10 if evidence supports

---

## Analytical requirements (output must explain, not just list)

Your synthesis must **analyze** not aggregate:

1. **Lane architecture** — how deai_removal vs tic_enrichment vs both splits across final patches; where same move serves both lanes
2. **Evidence tier mix** — count patches by `[verified]` / `[inferred]` / `[speculative]`; flag if >50% inferred
3. **Conflict audit** — passive voice, cliché-RLHF, neutrality, sycophancy: state resolution source digest + IDs
4. **ESL impact statement** — one paragraph: which patches preserve L1-Chinese voice vs which risk native-norm pressure
5. **0628 boundary** — one paragraph: what you inherited vs what you did not reopen
6. **Regret minimization** — which high-conf survivors you **intentionally dropped** and why (scope, duplicate, ESL risk)

Row-not-prose for patches; **analytical prose allowed only in §8 Narrative analysis** (≤600 words).

---

## Save

`/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/deai_operator_corpus_skill_brief_20260628.md`

If >4500w: split `deai_operator_corpus_skill_brief_part1_20260628.md` + `_part2_` with same Scope ID.

---

## Output template (mandatory — every section)

```markdown
# Skill brief — deai-operator-corpus (final synthesis)

**Scope ID:** `deai-tic-corpus-final-20260628`
**Sources:** 6 digest windows · adversarially reviewed
**Iron law:** Implement §7 Tasks / §5 Patches only. No primary re-read. No 0628 re-litigation.

## 0) Audit trail (Pass 1–5 log)
| pass | outcome (1–2 bullets) |
| 1 inventory | … |
| 2 ledger | N survivors merged → M unique moves |
| 3 falsifiers | K candidates dropped |
| 4 scorecard | J patches ≥90% conf |
| 5 self-review | … |

## 1) TL;DR (≤8 bullets — patch_id / move_id refs only)

## 2) Digest coverage matrix
| digest file | slugs | §3 n | §2 kills | represented in brief | deferral reason if none |

## 3) Evidence gate summary
| rule | application |
| scorecard ≥5.5 | … |
| auto-kills applied | passive-as-signal, … |
| tier mix | verified: X · inferred: Y · speculative: Z |

## 4) Deduped move bank (all survivors considered; top evidence for patches)
| move_id | lanes | mechanism | scope/limit | falsifier | tag | conf% | S1–S7 | provenance |

## 5) Conflict & resolution audit
| topic | digest A + ID | digest B + ID | resolution | tag |

## 6) Explicit DROP / ban list (skill-enforced)
| banned claim | why | digest ref | patch_id if ADD-to-kill-list |

## 7) Patches (ordered P0→P1→P2 — MAX 12–15)
| P | patch_id | skill | file (absolute) | CHANGE/ADD/DROP | diff intent | evidence IDs | conf% | S1–S7 | falsifier | verify (grep) |

## 8) Narrative analysis (≤600w)
Lane architecture · ESL impact · 0628 boundary · regret minimization · evidence-tier risk

## 9) Deferred / not emittable (<90% or inherited Gate A)
| ID | reason | what would lift it |

## 10) Dropped candidates (explicit — sunk-cost guard)
| candidate | reason dropped | digest ref |

## 11) Cursor implement tasks (Composer-ready — self-contained)
### Task 01 — {title}
- Paths: (absolute)
- Action: CHANGE | ADD | DROP
- Diff intent: (copy from §7)
- Evidence: move_id · Q-ID · tag
- ESL guard: preserve | N/A
- Verify: `grep '…' /Users/dubs/.cursor/skills/deai/SKILL.md`
- Falsifier check: (how operator confirms patch worked)
- depends_on: none

## 12) Operator PASS/FAIL matrix
| check | PASS instruction |
| Every §7 patch has conf% + S1–S7 + falsifier | |
| No kill-register claim in §7 | |
| No `[verified]` upgrade vs digests | |
| 6/6 digests in §2 matrix | |
| Patch count ≤15 | |
| ESL guards present on tic/deai patches | |
| §10 dropped list non-empty OR justified | |

## FOOTER — iron laws
- FR-3: no primary re-read in Cursor implement
- ESL: operator L1 Chinese — no native-norm polish
- 0628 canon inherit only
- Kill-list bans are hard constraints
- Epistemic tags never upgraded without new evidence
```

---

## Anti-patterns (FORBID)

- Emit patch without scorecard + falsifier
- Re-open §2 kill-register claims as patches
- Promote `[inferred]` → `[verified]` without digest support
- Blend conflicting quotes into one patch row
- Prose-only claims outside tables (except §8)
- Patch essays instead of one-line diff intent
- Silent omission — every digest must appear in §2 or §9
- More than 15 patches
- Touch files outside target table without §9 justification
- Intrinsic self-critique without Pass 5 checklist (theater review)

---

## Operator handoff

After save:
1. Operator runs §12 checklist — all PASS before Cursor
2. Resolve any `[unresolved]` in §9 before implement
3. Hand §11 Tasks to Composer 2.5 or `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md`

**If agent blocks on Gate A primaries:** paste override — *"QC-skipped digest merge. Proceed from attached digests only; §4 Q-IDs are carry-forward authority. Missing primary attach is not a blocker."*
