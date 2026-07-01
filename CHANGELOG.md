# Changelog

Notable changes to scholia.skill (parent platform).

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions track the `version` field in `SKILL.md` frontmatter unless noted.

## [0.3.0] - 2026-07-01

This release adds mechanical verify gates for the practical-cards pipeline. I may have been wrong about edge cases in older corpora. File an issue if a gate misfires on your tree.

### Added

- Output verify gate for cs-ai practical cards pipeline (`scripts/verify_practical_cards_pipeline.sh`, `verify_pipeline.py`, oracles PC-P01..PC-P14).

- `references/output-gate-contract.md` documents the generator plus verify pattern for skill artifacts.

- `scripts/lib/review_loop_guard.sh` bounds loops (min 2 successful phases, wall-clock cap, stuck-signature circuit breaker).

- `run_practical_cards_verify_gate.sh` and `run_practical_cards_consumer_wire.sh` decouple consumer wiring from the scholia-only gate.

- `pick_review_batch.py` rotates curriculum batches across review-loop phases.

- `scripts/test_verify_practical_cards_pipeline.py`.

- `SECURITY.md` (threat model, reporting, supported versions).

- `LICENSE` (MIT).

- Git repository and remote `https://github.com/weijia-89/scholia.skill`.

### Changed

- `run_practical_cards_review_loop.sh` runs a real multi-phase autonomous loop (never exits after first pass).

- `run_review_loop.sh` and `run_trainer_review_loop.sh` share the same guard semantics; verify gates split single-pass checks.

- `refresh_pipeline.sh` tails with `verify_pipeline.sh`.

- `prompts/ORCHESTRATOR_cs_ai_practical_cards.md` defaults to ChatPRD dispatch (subagents alternate).

- `prompts/PIPELINE.md` and `plans/orchestrator_status.yaml` document verify gates and consumer-wire lanes.

- `README.md` rewritten (purpose, stack, two-phase work, verification commands).

- `SKILL.md` references table entries for verify gates and review-loop guard.

### Fixed

- `verify_pipeline.py` scopes operator table to `--batch`, skips full-table compare on `--route`, adds real PC-P05 negative self-test, adds `--summary` mode.

- Review loop no longer treated first PASS as completion while deeper oracles stayed untested.

## [0.2.1] - 2026-06-18

### Added

- `references/source-register-corrections.md` (S-09 URL, K-06 reconcile).

- `references/kill-register.md` (K-01–K-07 canon dispositions).

- `references/consistency_check-template.md` (C-DG004 semantic log stub).

- CLAIMS C-R007–C-R011 (sparsity N<3, Du et al. K-01, vendor 5k/25k, SkillRouter, S-09 corroborative).

### Changed

- Canon tri-merge: W10 + S4e + S4 base → **CANON-SHIPPED** (`references/merged-decision-canon-20260618.md`).

- `SKILL.md`: v0.2.1, kill-register pointer, sparsity routing C-R007, K-01 iron law, version pins.

- `references/provenance-template.md`: TROVE relation column (C-DG005).

- K-06 reconcile + S4-R2 fold: S3 ledger, open decisions, source-register S-03 fix.

- Canonical base S2: Cursor fold → `piranesi.skill/research-projects/0621-scholia-corpus/returns/stage2_adversarial_20260618_ingest.md` (no ChatPRD rerun).

- Superset doc audit: hooks-config, wc-to-token-approximation, canon drift, gymbuddy→context:fork, script portability.

## [0.3.0-oracles] - 2026-06-18 (in-repo hardening; folded into 0.3.0 release line)

### Added

- SF-11 PDF/ingest parity WARN + PS-02 pressure oracle.

- SF-09 shellcheck gate on `--self`.

- Frozen fixtures: `tests/pressure_scenarios/fixtures/`, `materialize_fixtures.sh`, `run_fixtures.sh`.

- `references/closed-corpus-piranesi-routing.md`, `references/n20-clustering-fallback.md`.

- Child template sections 9–12 (Permissions, Human gates, Handoff, Audience).

### Changed

- `verify_scholia.sh`: SF-11/PS-02/SF-09; case-statement cleanup; pressure PASS=11.

- `references/contract-graph.md`, `pressure-scenarios.md`, `ROADMAP-remaining-tasks.md`.

## [0.2.0] - 2026-06-18

### Added

- `scripts/check_cross_stage_consistency.sh` (C-DG004 mechanical structure check; semantic judge deferred to phylax).

- `prompts/output-mode-study-guide.md`, `output-mode-procedural.md`, `output-mode-notebooklm-pack.md`.

- `references/zotero-mcp-workflow.md`.

- PS-10 piranesi export-only kill-register in `--pressure`.

- `layout_mode: flat` corpus layout exception (C-DG007; PS-11).

- `scripts/lib/sf06_provenance.sh`.

- PS-12 C-DG004 cross-stage oracles.

- `scripts/run_trainer_review_loop.sh`.

- `tests/pressure_scenarios/fixtures/README.md`.

### Changed

- `verify_scholia.sh`: `--cross-stage` flag; auto C-DG004 on child verify; output-mode sub-skill gates on `--self`.

- `SKILL.md`: output modes shipped v0.2; C-DG004 verify contract.

- Review loop scripts: skill-fitness WARN grep.

## [0.1.1] - 2026-06-18

### Added

- `prompts/literature-paper-ingest.md`.

- `references/sub-skills-index.md`, `references/corpus-manifest-template.yaml`.

- Pressure oracles PS-03, PS-07, PS-08.

- `scripts/sync_cursor_skill_mirror.sh`.

- Root `README.md`, `references/ROADMAP-v0.2.md`.

### Changed

- verify: sub-skill presence gates on `--self`.

- Operator waived mechanical DRM checks (manifest field doc-only).

- `CLAIMS.md` for routing threshold Gate B anchors.

## [0.1.0] - 2026-06-18

### Added

- Initial CANON-MERGED skill from ChatPRD W10 + S4e.

- `scripts/verify_scholia.sh`, `scripts/bootstrap_lane_fanout.py`.

- Chapter ingest prompt, child/provenance templates, contract graph.
