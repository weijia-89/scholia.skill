# phylax pre-flight checklist — scholia SKILL.md draft

META: S4 canon appendix · run in **separate session** (Q-013/Q-014 recursion guard)

Use **context:fork** fresh session (Q-014 recursion guard). Run after `verify_scholia.sh` exits 0 on the draft.

## Gate 0 — recursion / routing

- Audit session is not the scholia generation session
- No scholia/phylax subagent at depth >1
- `pairs_with` only — no `composes:` nesting

## Gate A — frontmatter & contract

- `description` states triggers and negative boundaries
- σ+ / σ− non-empty and mutually exclusive
- Portability (C-DG008): Claude-only flags in body, not frontmatter
- Slug disambiguated (`-corpus-to-skill`)

## Gate B — evidence integrity (K-register)

- No K-01 "7.9%" survivor — use 13.9–85% (Du et al. 2025)
- 5k/25k cited to vendor docs (K-03)
- Load-bearing claims anchored (SF-06)
- Preprints tagged; no preprint-only enforced gates (C-G011)
- Progressive disclosure: cite **S-06** for ~100 tokens / 5k body; **S-09** engineering blog corroborates three-level disclosure only (C-R011)
- provenance relation column populated; zero untriaged CONTRADICTED

## Gate C — cross-stage (C-DG004, L3+)

- SYNTHESIS claims trace to ingests
- Judge: zero CONTRADICTED; DRIFT <20% or WARN
- Log to `references/consistency_check.md`

## Gate D — harness & corpus

- `verify_scholia.sh` exit 0 first
- PS-01…PS-12 documented (SF-14); PS-02/SF-11 deferred WARN-only
- manifest fields: language, legal_status, equation_density, drm
- Negative-space refusals (C-DG009)

## Gate E — ship readiness

- `INGEST_WAVE_REPORT.md` = PASS or PASS-WITH-FLAGS
- Plan-first if >5 files (Q-004)
- Operator nav absolute paths; SKILL.md body SF-05 clean
- Trainer ship notes present

**Verdict:** phylax `mode=full` → PASS only if Gates 0–E clear. WARNs need operator sign-off.

**Open:** Q-006 textbook schema untested; gap #11 wc-to-token ratio approximate for SF-03.
