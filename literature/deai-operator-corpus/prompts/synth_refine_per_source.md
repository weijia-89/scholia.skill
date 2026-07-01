# ChatPRD — Per-source refine (ingest → evidence-filtered digest)

Platform: **Opus 4.6** · Project: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`  
Contract v0.2: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

## Attach (≤8)

1. Live ingest: `chatprd_returns/{slug}_*_ingest.md`
2. Primary Gate A: matching `attachments/{prefix}_ATTACH.txt` or chapter slice (**required**)
3. Recommended: paste `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

**Paste:** this prompt.

## Task

**Evidence filter** between one ingest and Cursor implement. Apply **Semantic preservation protocol** (contract §Quote-first → Row-not-prose → Provenance chain).

**Keep only** STRONG or high-value MODERATE claims that pass Gate A. Kill the rest. Preserve verbatim anchors, mechanisms, scope, falsifiers — **not** a shorter summary.

## Workflow (execute in order — do not skip)

1. **Inventory** — List load-bearing claims from ingest (would change skill patches if wrong).
2. **FR-3 middle re-read** — If primary attach >40k chars, spot-check quotes from start, middle, and end regions.
3. **Gate A verification pass** — Match each ingest Q-ref to primary verbatim **before** scoring. Mismatch → HALLUCINATION-SUSPECTED.
4. **Supplemental web verification (optional)** — For load-bearing STRONG claims where external confirmation would change keep/kill or grade: run ≤5 independent web retrievals (palamedes P2). Log `RETRIEVAL-ORDER`. Web confirms/denies **external facts** cited by the primary — never substitutes for Gate A craft extraction. Tag survivors: `primary Q-ref · web URL · grade · read-depth`. Falsifier per load-bearing claim. Web-only claims without Gate A anchor → kill register.
5. **Score + rank** — evidence grade × skill-patch value; drop WEAK and all kill-register verdicts.
6. **Semantic extract (tables only)** — survivors: claim, mechanism, scope/limit, falsifier, lane, esl_preserve, provenance (`ingest row · Q-ID` [· web URL · grade if verified]).
7. **Skill patches** — §6 rows cite Q-IDs; one file cluster per row; concrete diff intent.
8. **TL;DR last** — ≤6 bullets referencing survivor IDs only; no new claims.
9. **Footer** — repeat contract iron laws.
10. **Cap** — ≤4500w; defer low-value MODERATE to §8.

## Anti-patterns (halt if tempted)

- Paraphrase Q-bank → FORBID
- Prose paragraph restating tables → FORBID
- Kill register without Gate A check → FORBID
- Drop scope/limit to save words → FORBID

## Save

`/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/{slug}_refined_YYYYMMDD.md`

```markdown
# Refined digest — {slug}

## 1) TL;DR (≤6 bullets — IDs only, e.g. C-003, move_02)

## 2) Kill register (non-survivors)
| ID | claim (short) | verdict | Gate A note |

## 3) Semantic core (STRONG/MODERATE survivors)
| ID | claim | mechanism | scope/limit | falsifier | lane | esl_preserve | provenance |

## 4) Verbatim Q-bank (survivors only — no paraphrase)
| Q-ID | quote | primary path |

## 5) Craft moves (ranked by value)
| move_id | lane | structural_borrow | esl_preserve | falsifier | Q-ID | provenance |

## 6) Skill incorporation (Composer-safe)
| skill | file (absolute) | KEEP/CHANGE/ADD/DROP | diff intent | Q-ID |

## 7) Implementor checklist
| check | PASS instruction |
| Gate A quotes unchanged | |
| No 0628 re-litigation | |
| ESL rows preserved | |
| Each §6 row = one edit session | |
| No prose-only survivors outside tables | |

## 8) Deferred (low-value MODERATE / UNTESTED)

## FOOTER — iron laws
FR-3 · ESL · 0628 canon path · ChatPRD authors / Cursor implements
```

**Supplemental web verification (palamedes bar):** Gate A remains mandatory for craft moves **from** the attached primary. Web search is **supplemental** — confirm or falsify load-bearing / STRONG external facts (citations, stats, named methods) when verification would change keep/kill or grade. ≤5 searches per window; log queries in `RETRIEVAL-ORDER`. Tag web-confirmed rows: `primary Q-ref · web URL · grade · read-depth · falsifier`. Web cannot import new craft moves without a Gate A anchor.

**Next:** batch → `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md`
