# Security policy for scholia.skill

## Scope

This repository ships Markdown skill instructions and ingest prompts. Reference templates and local verify scripts ship with it too. Nothing here listens on a network port or runs as a hosted service.

You load files from disk inside an IDE. You run `scripts/verify_*.sh` locally. You may drop PDF corpora under `literature/`. We care about misleading content in shipped prompts. We also watch for unsafe patterns in repo scripts and guidance that could cause harm if followed literally.

## Threat model

| Risk | What happens | Mitigation |
|------|----------------|------------|
| Prompt injection in corpus ingests | Generated child skills repeat attacker text from a PDF | Closed-corpus rule: claims trace to ingest rows. phylax semantic audit before ship. Verify gates on structure. |
| Secrets in ChatPRD attach packs | Operator pastes keys into `*_ATTACH.txt` or `chatprd_returns/` | Flat upload dirs only. No README in attach folders. operator-path-output iron law. Don't commit live credentials. |
| Monolith read of large corpora | Context collapse, un-audited synthesis | Fan-out mandatory at ≥5 PDFs. Depth cap ≤2. Monolith guard in `verify_scholia.sh --pressure`. |
| Unverified procedural steps | Model invents exercise steps not in source | `verify_practical_cards.sh`. `procedure_gap: true` when protocol absent. Banned send-script patterns. |
| Supply chain in scripts | Malicious change to `scripts/` | Review PRs. Run `verify_scholia.sh --self --pressure` before merge. Pin to tagged releases. |
| Operator corpus data | PDFs may contain malware or PII | Treat `literature/` as untrusted input. Scan PDFs locally. `localonly/` stays gitignored. |

## Trust boundaries

| Boundary | Crosses |
|----------|---------|
| Disk read | Files under this repo. Operator corpora under `literature/`. Paths cited in prompts. |
| Disk write | Generated ingests and practical cards. Child `*.skill/` trees the operator chooses to create. |
| Network | None in core verify scripts. ChatPRD runs separately. Piranesi export and consumer RAG sync are operator-initiated outside this repo. |
| Agent tools | Whatever the host IDE exposes. Scholia docs discourage in-Cursor web fetch on closed corpora without `waive-three-stage`. |

## Sensitive corpora

Don't point scholia at PHI without legal review. Same for ITAR-controlled material and no-TDM collections. See `references/negative-space.md` for refusal categories.

DRM classification stays operator metadata in `corpus_manifest.yaml`. Verify doesn't mechanically classify copyright status.

## Child skills and downstream consumers

Generated child skills are separate artifacts. Scholia provides templates and gates. The operator owns what ships.

Run phylax `mode=full` in a fresh session before publishing a child skill. Consumer bridges (for example local RAG) read scholia YAML SSOT. They must not re-extract steps from PDFs.

## Supported versions

| Version | Status | Notes |
| ------- | ------ | ----- |
| 0.3.x | supported | Output verify gates, practical-cards pipeline checks, bounded review loops |
| 0.2.x | security-only | Critical verify or prompt fixes at maintainer discretion |
| < 0.2 | unsupported | Upgrade recommended |

Release tags on GitHub track shipped versions. The `version` field in `SKILL.md` frontmatter is the skill SemVer.

## Reporting a vulnerability

Don't open public GitHub issues for security vulnerabilities.

Use [GitHub Security Advisories](https://github.com/weijia-89/scholia.skill/security/advisories/new) on this repository, or contact the repository owner privately.

Send path and commit hash if you have them. Send steps to reproduce from a clean clone. Describe impact in plain language. Examples include exposed credentials, injected text in a shipped template, or verify scripts running untrusted input. We're not sure our severity read will match yours until we reproduce.

We aim to acknowledge within a few business days. We credit reporters on the advisory unless they ask to remain anonymous.

## No secrets in public issues

Don't paste API keys or tokens into issues or pull request comments. Don't paste private paths either. Corpus excerpts with personal data belong in the private advisory flow.

Owner: repository maintainers. Last reviewed: 2026-07-01.
