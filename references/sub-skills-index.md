# Scholia sub-skills index

Sub-skills = prompts, templates, and scripts under scholia (not generated child `*.skill/`).

Canon SSOT beyond this table: see `SKILL.md` §References (kill-register, merged canon, S3 ledger, etc.).

| Path | Role | Load when |
|------|------|-----------|
| `prompts/literature-paper-ingest.md` | Peer-reviewed paper fan-out schema | ≥3 papers |
| `prompts/literature-chapter-ingest.md` | Textbook chapter fan-out + TEXTBOOK-Q1 | textbook chapters |
| `references/child-skill-template.md` | Generated child SKILL shape | after synthesis |
| `references/provenance-template.md` | CLAIMS ledger template | child skill gen |
| `references/corpus-manifest-template.yaml` | Session manifest stub | corpus drop |
| `references/contract-graph.md` | Gate → enforcement map | verify vs phylax |
| `references/pressure-scenarios.md` | PS oracles | harness changes |
| `references/negative-space.md` | Refusal categories | routing |
| `references/hooks-config.md` | Recommended Stop/PreToolUse hooks | child skill ship |
| `references/wc-to-token-approximation.md` | SF-03 line vs token budget (gap #11) | compaction planning |
| `references/research-triage-palamedes-scholia-piranesi.md` | palamedes · scholia · piranesi triage | routing any research task |
| `references/n20-clustering-fallback.md` | N>20 fan-out design stub | large corpora |
| `scripts/verify_scholia.sh` | Mechanical gates + `--pressure` | every ship |
| `scripts/bootstrap_lane_fanout.py` | ChatPRD upload sync | piranesi/track B |
| `scripts/sync_cursor_skill_mirror.sh` | Cursor discoverability (SKILL.md only) | after SKILL edit |
| `scripts/run_review_loop.sh` | verify + pressure + skill-fitness | review loops |
| `scripts/run_trainer_review_loop.sh` | + phylax audit_repo | trainer autonomous gate |
| `prompts/output-mode-study-guide.md` | scholia → palamedes study-guide handoff | output mode study-guide |
| `prompts/output-mode-procedural.md` | scholia → palamedes procedural handoff | output mode procedural |
| `prompts/output-mode-notebooklm-pack.md` | scholia → notebooklm-prep handoff | output mode notebooklm |
| `scripts/check_cross_stage_consistency.sh` | C-DG004 structure check | post-synthesis |
| `scripts/lib/sf06_provenance.sh` | Shared SF-06 row counter | verify + C-DG004 |
| `references/zotero-mcp-workflow.md` | Optional Zotero MCP pre-fill | manifest bootstrap |
| `prompts/orchestration-v0.2-superset.md` | New-chat wave manifest (kickoff only; not verify gate) | v0.2 kickoff |
| `prompts/r01-corpus-session-banter-kickoff.md` | R-01 operator paste — banter/alethia corpus child | first corpus session |
| `prompts/r02-textbook-workbook-corpus-kickoff.md` | R-02 deep parse — textbook/workbook/monograph (generic; consumer bridge optional) |
| `prompts/cs-ai-textbook-canon-fanout-kickoff.md` | CS+AI textbook canon — chapter fan-out from Piranesi 0625-textbook-canon |
| `references/practical-usage-schema.md` | Phase-2 `practical_usage` block + card file shape |
| `prompts/practical-usage-card-fanout.md` | Phase-2 subagent paste packet (one chapter per agent) |
| `prompts/cs-ai-practical-cards-fanout-kickoff.md` | cs-ai phase-2 parent kickoff — **wait for `kickoff phase 2`** |
| `prompts/practical-usage-ingest-strategy.md` | Two-phase ingest strategy (shipped v2) |
| `references/practical-usage-consumer-bridge.md` | Consumer wire contract |
| `scripts/verify_practical_cards.sh` | SF-15 implementation card gate (`--self-test`) |
| `scripts/sync_banter_r02_practical_cards_mirror.sh` | Aletheia SSOT → scholia R-02 card mirror resync |

Generated child skills (operator corpus elsewhere) copy from `child-skill-template.md` and live outside this repo unless operator colocates them.
