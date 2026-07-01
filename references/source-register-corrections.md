# Source register corrections (canon SSOT)

META: K-06 reconcile + S4 re-reconcile · date=20260618 · supersedes S1 register rows where noted

Patches ChatPRD S1 source ledger gaps without rewriting piranesi ingests. Raw S1: `/Users/dubs/Projects/piranesi.skill/research-projects/0621-scholia-corpus/returns/stage1_research_20260618_ingest.md` §Source Register.

| ID | Title | Tier | URL | Gate A | Gate B anchor |
|----|-------|------|-----|--------|---------------|
| S-03 | Context Length Alone Hurts (Du et al., EMNLP 2025 Findings) | 1 | https://aclanthology.org/2025.findings-emnlp.1264/ | PASS | **K-01 kill:** use "13.9–85% degradation range across 5 models" — never "7.9% on Llama/Mistral" |
| S-06 | Anthropic Agent Skills overview | 1.5 (vendor) | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | PASS | Level 1 metadata ~100 tokens; Level 2 under 5k tokens (C-DG001) |
| S-09 | Equipping agents for the real world with Agent Skills | 1.5 (vendor) | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | PASS | Progressive disclosure three-level model. **Corroborative only** — token counts use S-06 |

**K-06 disposition:** RESOLVED — S-09 URL located; corroborative for progressive disclosure only.

**S1 register (S-01–S-20):** see raw ingest; apply K-01/K-03/K-04/K-06 corrections above when citing in platform docs.
