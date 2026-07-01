# ChatPRD — Cursor implement handoff

Platform: **Opus 4.6** · Audience: **Composer 2.5 / Auto** (execute only — no re-reasoning)  
Contract v0.2: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md`

## Attach (≤8)

1. Final `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/deai_operator_corpus_skill_brief_*.md` OR single `{slug}_refined_*.md`
2. Optional: 0628 canon path only if detection rows present

**Paste:** this prompt.

## Task

**Concept distillation** (strong ChatPRD → weak Composer): translate approved synthesis into **numbered tasks** — pre-resolved directives, not evidence essays.

Composer constraints (see `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` §1):
- Coding-optimized; do not re-weigh evidence
- Context degrades with length — keep brief ≤2500w if possible
- Sections must be **self-contained** (each task repeats ESL guard + verify)

Heavy waves: `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/ORCHESTRATOR_deai_tic_corpus.md` + workers.

Preprocess option: Section 3 of `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/evergreen_chatprd_composer_ingest.md` if output >2000 tokens.

## Preserve vs drop

| Keep in handoff | Drop |
| ------------- | ---- |
| Task order, absolute paths, CHANGE/ADD/DROP, diff intent | Q-bank verbatim text |
| Q-ID / move_id pointers | Mechanism essays |
| ESL guard per task | Kill register history |
| Verify commands | NEEDS_REVIEW context (must be resolved pre-handoff) |

## Save

`/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/cursor_implement_brief_YYYYMMDD.md`

```markdown
# Cursor implement brief

**IRON LAW:** Execute §Tasks only. No primary re-read. No 0628 re-litigation. No new ingests.

## Scope ID
`deai-operator-corpus-skill-wiring-YYYYMMDD`

## Tasks (ordered — self-contained blocks)
### Task 01 — {title}
- Paths: (absolute)
- Action: CHANGE | ADD | DROP
- Diff intent: (one line — copy from skill brief)
- Evidence: Q-ID or brief §5 row
- ESL guard: preserve | N/A
- Verify: grep or pytest command
- depends_on: none

## Out of scope
## Evidence matrix (operator PASS/FAIL)
| task | verify | PASS/FAIL |

## FOOTER — iron laws (repeat for Composer context rot)
```

One task = one file cluster. Ban vague verbs. `[unresolved]` → Deferred, not Tasks.
