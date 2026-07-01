# scholia (σχόλια)

Scholia turns a closed stack of academic PDFs into auditable ingests and procedural indexes. It can emit a child Cursor skill when the session bet asks for one. Greek for marginal notes.

I built it after the same failure kept showing up: an agent could quote a chapter and still couldn't walk me through the exercise that chapter actually named. That's the whole problem in one line. Later sessions should trace a claim or a procedure to a specific section without reopening the whole library. I'm not sure every corpus shape is covered yet; the gates are built for the textbook and paper stacks I run day to day.

**Status:** v0.3.0 · parent platform on GitHub: `weijia-89/scholia.skill`  
**License:** MIT (see `LICENSE`)

## Why this exists

Most agent workflows stop at citation. You get a confident sentence about what a paper or textbook recommends. Often no ordered steps. Exercise hooks vanish. When the source cites efficacy but never describes the protocol, there's rarely an honest gap tag either.

Coaching corpora hit this wall. Exam prep does too. Any skill meant to *do* something from the literature, not just name it, runs into the same hole.

Scholia was built for the operator who already has PDFs on disk. The repeatable path runs from those files to chapter-level ingests with claim rows and section anchors. Add procedure cards (`practical_usage`) when the session needs steps and not just claims. Finish with a generated child skill or reference index that phylax can audit before ship.

The design rejects monolith reads. At five or more PDFs the parent skill fans out to paper or chapter sub-agents, merges output, then runs mechanical verify gates so structure failures surface before semantic review.

## Where scholia sits in the stack

Scholia is a peer skill, not a submodule of palamedes or piranesi.

| Skill | Role |
|-------|------|
| **trainer** | Routes sessions, enforces plan-first and verify-before-completion |
| **piranesi** | Export-only research and architecture canon in ChatPRD (not in-Cursor web on primaries) |
| **palamedes** | Broad librarian passes, synthesis tiers, quick reporting |
| **scholia** | Full-depth closed-corpus parse, chapter fan-out, practical cards |
| **phylax** | Semantic audit of generated skills (BIV taxonomy) |

Scholia owns routing and handoff payloads. It doesn't ship palamedes HTML templates or piranesi export scripts inside this tree.

## Two-phase corpus work

**Phase 1 (claims).** Sub-agents run `prompts/literature-chapter-ingest.md` or the paper variant. Output lands in `literature/<corpus>/ingests/`. Verify enforces word caps (SF-12).

**Phase 2 (procedures, optional).** The manifest flag `practical_usage_required: true` turns this on. A session bet in coach or teach mode turns it on too. Operationalize mode does the same. Scholia then extracts procedure cards with source anchors. Real protocols get ordered steps. Outcome-only sources get `procedure_gap: true` instead of invented steps. Schema: `references/practical-usage-schema.md`.

The cs-ai textbook canon includes a reference pipeline under `literature/cs-ai-textbook-canon/practical_cards_pipeline/`. Curriculum YAML drives ChatPRD attach packs and per-chapter ingest prompts. The pipeline also emits operator tables and runs mechanical gate checks (PC-P01..PC-P14). See `references/output-gate-contract.md`.

## Output modes

| Mode | Handoff | Rendered by |
|------|---------|-------------|
| skill (default) | `references/child-skill-template.md` | scholia + phylax |
| reference-library | `LITERATURE_INDEX.md` | scholia |
| study-guide | `prompts/output-mode-study-guide.md` | palamedes study-guide-site |
| procedural | `prompts/output-mode-procedural.md` | palamedes procedural-guide-site |
| notebooklm-pack | `prompts/output-mode-notebooklm-pack.md` | notebooklm-prep |

## Verify before phylax

Doc-only iron laws don't catch path typos or missing attach sections. They don't catch YAML that fails schema either. Scholia pairs each generator with a verify script.

```bash
# Parent skill + pressure oracles
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --self --pressure

# Practical card YAML on a corpus root
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon

# Pipeline artifacts (attach, ChatPRD prompts, operator table)
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards_pipeline.sh --summary

# Bounded review loop (min 2 escalating phases; circuit breakers in scripts/lib/review_loop_guard.sh)
bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_review_loop.sh
```

Exit code `2` blocks ship hooks. Semantic CONTRADICTED / DRIFT stays with phylax, not verify.

Consumer wiring (for example RAG sync) runs only after scholia verify passes and the operator says `kickoff wire`:

```bash
bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_consumer_wire.sh
```

## Quick start

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --self --pressure
bash /Users/dubs/Projects/scholia.skill/scripts/sync_cursor_skill_mirror.sh
```

Invoke explicitly with `/scholia` or let trainer route inline (`disable-model-invocation: true` on the skill until Cursor preloads it properly).

Drop corpora under `literature/`. Keep session-specific notes in `localonly/` (gitignored).

## Repository layout

| Path | Purpose |
|------|---------|
| `SKILL.md` | Router canon, iron laws, routing tree |
| `prompts/` | Paper and chapter ingest schemas, output-mode handoffs, practical-card fan-out |
| `references/` | Templates, contract graph, merged decision canon, gate contract |
| `literature/` | Operator corpus trees (ingests, text slices, practical_cards_pipeline) |
| `scripts/` | `verify_scholia.sh`, `verify_practical_cards*.sh`, review loops |
| `tests/pressure_scenarios/` | Mechanical oracles PS-01..PS-12 |
| `CLAIMS.md` | Verified routing thresholds (Gate B anchors) |

Full sub-skill map: `references/sub-skills-index.md`.

## Child skills

Generated child `*.skill/` directories usually live outside this repo unless the operator colocates them. After fan-out and merge, use `references/child-skill-template.md`, run verify on the artifact, then phylax in a fresh session (`context:fork` for scholia.self; same-session self-audit blocks).

## Canon and history

- Merged architecture: `references/merged-decision-canon-20260618.md`  
- Kill register (do not revive): `references/kill-register.md`  
- Roadmap: `references/ROADMAP-remaining-tasks.md`  
- Changelog: `CHANGELOG.md`  
- Security: `SECURITY.md`

## Contributing

Pull requests are fine. Run the review loop, or at minimum `verify_scholia.sh --self --pressure`, before opening a PR. Report security issues privately per `SECURITY.md`.
