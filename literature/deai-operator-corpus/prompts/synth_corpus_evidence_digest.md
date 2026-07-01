# ChatPRD — Corpus evidence digest (cross-source merge)

Platform: **Opus 4.6** · Scope: `deai-corpus-extraction-wave-20260627`  
Project: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/`  
Contract v0.2: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

## Attach (≤8 — hard limit)

**Attach order (mandatory):**
1. `00_CORPUS_SYNTH_CONTRACT.md` — **MUST READ AND FOLLOW** before any merge.
2. `01`–`07_*_ingest.md` — adversarially reviewed ingest returns (Gate A verified at ingest).
3. `GA*_ATTACH.txt` — primary Gate A slices when included (use to re-verify `[verify]` rows or conflicts).

Do **not** attach this prompt. Paste this prompt text only.

**QC-skipped merge mode:** Ingest §4 Q-bank is the Gate A carry-forward authority. Do **not** block or error when Gate A attach is absent for a slug — ingest attestation + §4 quotes suffice. Re-read attached `*_ATTACH.txt` only when present or when ingest row has `[verify]`.

**Ingests OK when Phase 2 QC skipped.** `_refined_*.md` also accepted if present. Deai lane first.

## Task

**Evidence curator** across sources. Merge **table rows only** (§3–§5 from each ingest or refined digest) — **never** merge TL;DR prose or narrative summaries (hierarchical merge degrades semantics; CAHM 2025).

Merge only STRONG/MODERATE survivors with primary anchors. Dedupe identical moves (keep richest quote set + full provenance chain). Conflicts → NEEDS_REVIEW with **both quotes** — never blend.

## Workflow (order enforced)

1. **Inventory** — slug, chapter_id, ingest/refined path, lane per attach.
2. **Extract rows** — Pull §3 semantic core + §4 Q-bank + §5 craft moves from each ingest (or refined digest if Phase 2 ran).
3. **Gate A carry-forward** — Copy §4 Q-bank verbatim from ingests (already Gate A–verified at ingest). Re-read attached `*_ATTACH.txt` only when present in this window or when ingest row has `[verify]`. **Do not error** on missing Gate A attach when ingest attestation confirms compliance.
4. **Supplemental web verification (optional)** — For cross-source conflicts or load-bearing STRONG claims lacking external confirmation: ≤5 independent web retrievals (palamedes P2). Web confirms external facts only — never replaces Gate A craft anchors. Log `RETRIEVAL-ORDER`. Tag: `primary Q-ref · web URL · grade · read-depth`. Unresolved after search → NEEDS_REVIEW with falsifier.
5. **Dedupe** — Same mechanism: one row, multiple `source_slug · ID · Q-ID` [· web URL · grade] in provenance column.
6. **Lane sort** — `deai_removal` first for this wave.
7. **NEEDS_REVIEW** — truncation, conflict, missing falsifier, empty mechanism on load-bearing claim, web verification inconclusive.
8. **TL;DR last** — claim_id pointers only.
9. **Footer** — iron laws repeat.
10. ≤4500w per window.

## Anti-patterns

- Summarize ingests in prose → FORBID
- Merge without provenance chain → FORBID
- Single row blending two conflicting quotes → FORBID
- >8 sources in one window → FORBID (split part N)

## Save

`/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/corpus_evidence_digest_YYYYMMDD.md`  
Partial: `corpus_evidence_digest_part{N}_YYYYMMDD.md`

```markdown
# Corpus evidence digest

## 1) TL;DR (≤8 bullets — claim_id pointers only)

## 2) Sources
| slug | chapter_id | refined path | lane | grade |

## 3) Surviving claims (STRONG/MODERATE)
| claim_id | lane | claim | mechanism | scope/limit | falsifier | esl_preserve | provenance |

## 4) Primary anchors (verbatim — no paraphrase)
| claim_id | quote | primary path |

## 5) Operator elicitation — NEEDS_REVIEW
| claim_id | claim | full context | primary path | quotes |

## 6) Dropped (audit)
| claim_id | reason | source |

## 7) Implement order
| P | claim_ids | skill target | depends_on |

## 8) Checklist
| check | PASS instruction |
| Every §3 row has mechanism + falsifier or NEEDS_REVIEW | |
| Every §3 row has provenance chain | |
| §5 unresolved → no implement | |
| No 0628 re-litigation | |
| No prose-only claims outside tables | |

## FOOTER — iron laws
```

**Supplemental web verification (palamedes bar):** Gate A carry-forward remains mandatory. Web search is **supplemental** — resolve cross-source conflicts on external facts, confirm load-bearing STRONG claims, or supply falsifiers when primary alone is insufficient. ≤5 searches per window; log `RETRIEVAL-ORDER`. Tag: `primary Q-ref · web URL · grade · read-depth`. Never blend conflicting quotes; web cannot add craft moves without Gate A anchor.

Operator resolves §5 → `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/synth_corpus_skill_brief.md`
