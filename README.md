# scholia (σχόλια)

Corpus-to-skill wrapper for academic PDFs. Routes paper/chapter fan-out, piranesi export-only research, phylax semantic audit, and child skill generation.

**Status:** v0.2.0 SHIPPED (parent platform). Operator generates child `*.skill/` in separate corpus sessions.

## Output modes (v0.2)

| Mode | Handoff prompt | Renders via |
|------|----------------|-------------|
| skill (default) | child-skill-template | scholia |
| reference-library | LITERATURE_INDEX | scholia |
| study-guide | `prompts/output-mode-study-guide.md` | palamedes study-guide-site |
| procedural | `prompts/output-mode-procedural.md` | palamedes procedural-guide-site |
| notebooklm-pack | `prompts/output-mode-notebooklm-pack.md` | notebooklm-prep |

Scholia owns routing + handoff payloads only — no palamedes HTML templates in this repo.

## Quick start

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --self --pressure
bash /Users/dubs/Projects/scholia.skill/scripts/sync_cursor_skill_mirror.sh
```

Invoke explicitly: `/scholia` or trainer inline routing (`disable-model-invocation: true`).

## Layout

| Path | Purpose |
|------|---------|
| `SKILL.md` | Router canon |
| `prompts/` | Paper + chapter ingest sub-skills |
| `references/` | Templates, contract graph, merged canon |
| `literature/` | Operator corpus drop zone |
| `scripts/` | verify, bootstrap, review loop |

See `references/sub-skills-index.md` for full sub-skill map.

## Child skills

Generated outside this track unless operator colocates. Use `references/child-skill-template.md` after fan-out + synthesis.

## Docs

- Merged canon: `references/merged-decision-canon-20260618.md`
- Roadmap: `references/ROADMAP-v0.2.md`
- Changelog: `CHANGELOG.md`
