# ChatPRD — Corpus skill brief (deduped implement plan)

Platform: **Opus 4.6** · Project: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`  
Contract v0.2: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

## Attach (≤8)

`_refined_*.md` + approved `corpus_evidence_digest_*.md` (operator PASS on §5 NEEDS_REVIEW). Split if >8.

Recommended: paste contract.

**Paste:** this prompt.

## Task

Merge **surviving high-evidence craft moves** into one **Composer-safe** brief. This stage **concept-distills** for a coding executor (Boateng 2025): preserve patch intent + Q-ID pointers + ESL guards; **drop Q-bank prose** but **never drop mechanism or conflict audit**.

Dedupe; resolve conflicts with Gate A quote or mark `[unresolved]`. Long Part III > Part V for deai lane.

## Workflow

1. Import approved rows from evidence digest §3 + §4 (or refined digests if no digest yet).
2. **Row-not-prose** — patches and moves in tables only.
3. Order patches P0/P1/P2 by dependency and lane priority.
4. **Conflict table** — every `[unresolved]` from digest stays unresolved; do not merge away.
5. TL;DR last — move_id / patch row pointers only.
6. Footer — iron laws.
7. ≤4500w.

## Save

Partial: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/deai_operator_corpus_skill_brief_part{N}_YYYYMMDD.md`  
Final: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/deai_operator_corpus_skill_brief_YYYYMMDD.md`

```markdown
# Skill brief — deai-operator-corpus

## 1) TL;DR (≤8 bullets — move_id / patch row refs)

## 2) Themes by lane

## 3) Deduped move bank
| move_id | lanes | sources (provenance) | mechanism (one line) | esl_preserve | note |

## 4) Conflict resolutions
| topic | source A + Q-ID | source B + Q-ID | decision | rationale |

## 5) Patches (ordered P0/P1/P2)
| P | skill | file (absolute) | CHANGE/ADD/DROP | diff intent | Q-IDs | depends_on |

## 6) Implement sequence (serial where conflicts)

## 7) Deferred / UNTESTED / unresolved

## FOOTER — iron laws
```

Then → `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_cursor_implement_brief.md`
