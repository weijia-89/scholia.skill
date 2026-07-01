# Worker 13 — evergreen MDC rule (optional)

**Status key:** `pipeline_lane.worker_13_evergreen_mdc_rule`  
**Scope ID:** `deai-corpus-pipeline-hardening-20260627`  
**optional:** true — skip if operator does not use `docs/ai-context/` handoffs in scholia repo

## Read (≤4)

Paste this prompt only — agent reads paths from disk.

| # | Path |
| - | ---- |
| 1 | `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` |

**Paste:** this prompt.

## Task

From evergreen Section 4 (Companion MDC Rule), create:

**Path:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/.cursor/rules/research-context.mdc`

Include:

- YAML frontmatter with `globs: ["docs/ai-context/**/*.md"]`, `alwaysApply: false`
- Rule body items 1–6 from evergreen (DIRECTIVE, ANTI-PATTERN halt, YAML anchors, stale_after warn, conflict precedence, no paraphrase)

Create scaffold directory if needed:

```
/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/docs/ai-context/.gitkeep
```

(Add `.gitkeep` only if `docs/ai-context/` does not exist — optional placeholder for future ChatPRD preprocess outputs.)

---

## Verify

```bash
test -f /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/.cursor/rules/research-context.mdc
grep "ANTI-PATTERN" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/.cursor/rules/research-context.mdc
grep "docs/ai-context" /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/.cursor/rules/research-context.mdc
```

**On PASS or skip:** set `worker_13_evergreen_mdc_rule.status: done` or `skipped`

---

## Out of scope

- Populating `docs/ai-context/*.md` content (ChatPRD operator action)
- Skill patches
