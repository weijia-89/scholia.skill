# Pressure scenarios (oracles)

Run via:

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --pressure
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --self --pressure
```

Exit 0 = pass; exit 2 = block (Stop hook).

| ID | Scenario | Expected | Automated |
|----|----------|----------|-----------|
| PS-01 | Clean scholia root | verify `--self` exit 0 | yes |
| PS-03 | Ingest >4500w | SF-12 FAIL | yes |
| PS-04 | provenance path-only, no DOI/tag | SF-06 FAIL | yes |
| PS-02 | PDF count vs ingest count mismatch | SF-11 WARN (not FAIL) | yes |
| PS-05 | Hard DRM PDF | operator manifest + judgment | **waived** |
| PS-06 | Watermark DRM | operator manifest + judgment | **waived** |
| PS-07 | Child skill missing frontmatter `name:` | SF-01 FAIL | yes |
| PS-08 | Child skill with `/Users/` in body | SF-05 FAIL | yes |
| PS-09 | Monolith-read 5+ PDFs without fan-out | monolith guard FAIL | yes |
| PS-10 | piranesi in-Cursor without waive-three-stage log | kill-register FAIL on SKILL | yes |
| PS-11 | layout_mode flat — no ingests/ required | corpus layout flat PASS | yes |
| PS-12 | C-DG004 cross-stage (SYNTHESIS + provenance) | C-DG004 PASS; empty SYNTHESIS FAIL | yes |

Hooks (Claude Code): Stop → `verify_scholia.sh`; PreToolUse → monolith warning at N≥5 PDFs.

Last run: `tests/pressure_scenarios/last_run.txt`
