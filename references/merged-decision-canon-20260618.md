# scholia — merged decision canon (W10 + S4e)

META: merge · date=2026-06-18 · stakes=L3 · rule=Q-023

**Sources:**

- W10: `/Users/dubs/Projects/piranesi.skill/research-projects/0621-scholia-corpus/returns/synthesis_decision_canon.md`
- S4e: `/Users/dubs/Projects/piranesi.skill/research-projects/0621-scholia-corpus/returns/scholia_decision_canon_extended_20260618.md`
- S4 base: `/Users/dubs/Projects/piranesi.skill/research-projects/0621-scholia-corpus/returns/scholia_decision_canon_20260618.md`

**Merge rules:** W10 owns lane-specific routing thresholds. S4e owns cross-cutting corpus mechanics. S4 base confirms S3b vendor resolutions (K-03/K-04). S2b kill register wins external claims. External-claim ties → S2b.

**Status:** **CANON-SHIPPED v0.2.1** (2026-06-18)

---

## §1 Architecture verdict (merged)

**CONDITIONAL-WRAPPER** (W10 wins over S4e unqualified WRAPPER).

- Handle **directly** when corpus ≤~100k tokens AND provenance isolation not required (≤2 papers typical).
- Route to fan-out when ≥3 peer-reviewed papers OR ≥5 PDFs (monolith-read ban) OR provenance isolation required.
- **Not** a `composes:` parent; specialists are explicit-invoke peers documented in body text (`pairs_with` is convention only — W01/W04/W06).
- **Depth:** scholia-spawned fan-out caps at **depth 2** (S4e). Platform ceilings: Cursor IDE subagent depth **1**; Claude Code **5** (W10 §3 row 7). Document both; scholia fan-out never nests scholia or phylax at depth >1.
- **Falsifier:** monolith single-context outperforms composed fan-out on quality + auditability for corpora >100k tokens.

S4e absorbed without overriding conditional gate: DRM three-way, corpus_manifest fields, cross-stage consistency check (C-DG004), concurrency routing (N≤16 / workflows / batches), Du et al. 13.9–85% (K-01), Anthropic 5k/25k compaction (K-03).

---

## §2 Cross-canon conflicts resolved

| # | Tension | Winner | Merged rule |
|---|---------|--------|-------------|
| 1 | WRAPPER vs CONDITIONAL | **W10** | Conditional gate stands |
| 2 | palamedes passive vs P9 active | **W10** | palamedes = schema SSOT; scholia dispatches paper/chapter sub-agents directly |
| 3 | gymbuddy vs context:fork | **W10** (K-02 killed gymbuddy) | phylax self-audit via `context:fork` fresh session only |
| 4 | SF-01–SF-14 phylax phantom vs verify SF table | **W10 + S4e merge** | verify_scholia.sh = mechanical SF gates; phylax = semantic BIV audit |
| 5 | Depth 1 vs depth 2 | **Both** | Fan-out depth ≤2; platform table separate |
| 6 | study-guide/procedural v0.1 | **W10 + v0.2 ship** | v0.2.0 shipped all five output modes (skill, reference-library, study-guide, procedural, notebooklm-pack) |

---

## §3 Ship checklist

1. SKILL.md patched from W10+S4e+S4 base merge — **DONE v0.2.1 CANON-SHIPPED**
2. `bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --self --pressure` → exit 0 — **DONE**
3. phylax `audit_repo` on scholia.skill — **DONE 2026-06-18** (mode=full semantic on child drafts: separate session)
4. INGEST_WAVE_REPORT **PASS** — **K-06 reconciled** + canonical S2 on disk (2026-06-18)
5. Operator corpus child `*.skill/` — **next track** (outside platform repo)
