# Changelog

All notable changes to scholia.skill (parent platform).

## [0.2.1] - 2026-06-18

### Added

- `references/source-register-corrections.md` — S-09 URL (K-06 reconcile)
- `references/kill-register.md` — K-01–K-07 canon dispositions
- `references/consistency_check-template.md` — C-DG004 semantic log stub
- CLAIMS C-R007–C-R011 (sparsity N<3, Du et al. K-01, vendor 5k/25k, SkillRouter, S-09 corroborative)

### Changed

- Canon tri-merge: W10 + S4e + S4 base → **CANON-SHIPPED** (`references/merged-decision-canon-20260618.md`)
- `SKILL.md`: v0.2.1, kill-register pointer, sparsity routing C-R007, K-01 iron law, version pins
- `references/provenance-template.md`: TROVE relation column (C-DG005)
- K-06 reconcile + S4-R2 fold: S3 ledger, open decisions, source-register S-03 fix
- Canonical base S2: Cursor fold → `piranesi.skill/research-projects/0621-scholia-corpus/returns/stage2_adversarial_20260618_ingest.md` (no ChatPRD rerun)
- Superset doc audit: hooks-config, wc-to-token-approximation, canon drift, gymbuddy→context:fork, script portability
- Superset doc audit: hooks-config, wc-to-token-approximation, canon drift, gymbuddy→context:fork, script portability

## [0.3.0-harness] - 2026-06-18 (in-repo hardening; SKILL.md still v0.2.1)

### Added

- SF-11 PDF/ingest parity WARN + PS-02 pressure oracle
- SF-09 shellcheck gate on `--self`
- Frozen fixtures: `tests/pressure_scenarios/fixtures/`, `materialize_fixtures.sh`, `run_fixtures.sh`
- `piranesi.skill/research-projects/0621-scholia-corpus/returns/granola_attach_bundle_20260618.md` + `research-projects/0621-scholia-corpus/scripts/build_condense_bundle.sh`
- `references/closed-corpus-piranesi-routing.md`, `references/n20-clustering-fallback.md`
- Child template sections 9–12 (Permissions, Human gates, Handoff, Audience)

### Changed

- `verify_scholia.sh`: SF-11/PS-02/SF-09; case-statement cleanup; pressure PASS=11
- `references/contract-graph.md`, `pressure-scenarios.md`, `ROADMAP-remaining-tasks.md`

## [0.2.0] - 2026-06-18

### Added

- `scripts/check_cross_stage_consistency.sh` — C-DG004 mechanical structure check (semantic judge deferred to phylax)
- `prompts/output-mode-study-guide.md`, `output-mode-procedural.md`, `output-mode-notebooklm-pack.md` — v0.2 handoff contracts
- `references/zotero-mcp-workflow.md` — optional Zotero MCP manifest pre-fill
- PS-10 piranesi export-only kill-register in `--pressure` (10 oracles)
- `layout_mode: flat` corpus layout exception in verify (C-DG007; PS-11)
- `scripts/lib/sf06_provenance.sh` shared SF-06 helper (macOS regex fix)
- PS-12 C-DG004 cross-stage oracles
- `scripts/run_trainer_review_loop.sh` autonomous trainer gate
- `scripts/lib/sf06_provenance.sh` on `--self` sub-skill gate list
- `tests/pressure_scenarios/fixtures/README.md` — oracle documentation

### Changed

- `verify_scholia.sh`: `--cross-stage` flag; auto C-DG004 on child verify when SYNTHESIS + provenance present; output-mode sub-skill gates on `--self`
- `SKILL.md`: output modes shipped v0.2; C-DG004 verify contract; zotero workflow step
- `references/contract-graph.md`: C-DG004 rows (mechanical vs phylax semantic)
- Review loop scripts: skill-fitness WARN grep (combined summary line)
- `references/pressure-scenarios.md`: PS-10 automated yes

## [0.1.1] - 2026-06-18

### Added

- `prompts/literature-paper-ingest.md` — peer-reviewed fan-out sub-skill
- `references/sub-skills-index.md`, `references/corpus-manifest-template.yaml`
- Pressure oracles PS-03, PS-07, PS-08 in `verify_scholia.sh --pressure`
- `scripts/sync_cursor_skill_mirror.sh` for Cursor discoverability
- Root `README.md`, `references/ROADMAP-v0.2.md`

### Changed

- verify: sub-skill presence gates on `--self`; `.skill` suffix name/folder match
- Operator waived mechanical DRM checks (manifest field doc-only)
- `CLAIMS.md` for routing threshold Gate B anchors

## [0.1.0] - 2026-06-18

### Added

- Initial CANON-MERGED skill from ChatPRD W10 + S4e
- `scripts/verify_scholia.sh`, `scripts/bootstrap_lane_fanout.py`
- Chapter ingest prompt, child/provenance templates, contract graph
