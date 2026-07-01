# Pressure scenario fixtures

Inline temp fixtures in `scripts/verify_scholia.sh` remain the **SSOT** for CI-style `--pressure` runs.

Frozen on-disk copies (R-13) live under `fixtures/*.child.skill/` for editing and offline inspection.

| ID | Expected exit | Gate |
|----|---------------|------|
| PS-01 | 0 | scholia root `--self` clean |
| PS-02 | 0 | SF-11 WARN (5 PDFs, 4 ingests) |
| PS-03 | 2 | SF-12 ingest >4500w |
| PS-04 | 2 | SF-06 path-only provenance |
| PS-07 | 2 | SF-01 missing name |
| PS-08 | 2 | SF-05 absolute path in body |
| PS-09 | 2 | monolith guard (5 PDFs, no ingests) |
| PS-10 | 0 | piranesi export-only kill-register on SKILL |
| PS-11 | 0 | layout_mode flat (no ingests/) |
| PS-12 | 0 | C-DG004 cross-stage structure |
| PS-12-empty | 2 | C-DG004 empty SYNTHESIS.md |

## Commands

```bash
bash /Users/dubs/Projects/scholia.skill/tests/pressure_scenarios/run.sh
bash /Users/dubs/Projects/scholia.skill/tests/pressure_scenarios/run_fixtures.sh
bash /Users/dubs/Projects/scholia.skill/tests/pressure_scenarios/materialize_fixtures.sh
bash /Users/dubs/Projects/scholia.skill/scripts/run_trainer_review_loop.sh
```

Last inline run: `tests/pressure_scenarios/last_run.txt`
