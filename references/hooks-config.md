# Hooks config — scholia child skills (gap #8)

META: Canon gap #8 · doc-only v0.2.1 · operator enables in Claude Code / Cursor

Mechanical verify does **not** parse hook JSON. This file is the SSOT for recommended hooks after child skill generation.

## Recommended hooks

| Hook | Trigger | Command / action |
|------|---------|------------------|
| Stop | After agent turn on child skill | `bash scripts/verify_scholia.sh` (relative to child `*.skill/`) |
| PreToolUse | Before Read on `literature/pdfs/` when PDF count ≥5 | Warn: monolith-read ban — fan-out required (PS-09) |

## PreToolUse frontmatter guard (optional)

Block Write/Edit to child `SKILL.md` when YAML frontmatter missing `name:` or `description:` (PS-07).

## Platform notes

- Parent scholia.skill: hooks optional; platform gate is `run_trainer_review_loop.sh`.
- Procedural `layout_mode: flat` corpora: Stop hook still runs verify; ingests/ may be empty (PS-11).
- See `/Users/dubs/Projects/scholia.skill/references/pressure-scenarios.md` for oracle mapping.

## Status

**v0.2.1:** documentation only. Operator copies relevant rows into Claude Code `settings.json` or project hooks when shipping a corpus child.
