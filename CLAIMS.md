# scholia — external claim ledger (parent skill)

Load-bearing routing thresholds in `SKILL.md` cite claim IDs here. Full research lives in piranesi ingests — not duplicated in body.

| ID | Claim (compressed) | Tag | Source (Gate B anchor) | Ingest path |
|----|-------------------|-----|------------------------|-------------|
| C-R001 | Direct handle when corpus ≤~100k tokens and no provenance isolation | [verified] | W10 §1: "handle directly when corpus ≤~100k tokens AND provenance isolation is not required" | `piranesi.skill/research-projects/0621-scholia-corpus/returns/synthesis_decision_canon.md` |
| C-R002 | Paper fan-out at ≥3 peer-reviewed papers | [verified] | W10 §2 row 2: "P9 invoke ≥3 papers" / W02 reconcile | `piranesi.skill/research-projects/0621-scholia-corpus/returns/synthesis_decision_canon.md` |
| C-R003 | Monolith ban / fan-out mandatory at ≥5 PDFs | [verified] | W10 §2 row 2: "ban ≥5" / W02 DUAL-SCHEMA | `piranesi.skill/research-projects/0621-scholia-corpus/returns/synthesis_decision_canon.md` |
| C-R004 | Parallel fan-out N≤16 else workflows | [verified] | S4e C-G004 concurrency routing | `piranesi.skill/research-projects/0621-scholia-corpus/returns/scholia_decision_canon_extended_20260618.md` |
| C-R005 | Platform depth: Cursor subagent depth 1; Claude Code depth 5 | [verified] | W10 §3 row 7: "Cursor IDE = depth 1. Claude Code = depth 5" | `piranesi.skill/research-projects/0621-scholia-corpus/returns/synthesis_decision_canon.md` |
| C-R006 | Fan-out depth cap ≤2 (scholia → ingest subagent) | [verified] | S4e depth cap decision | `references/merged-decision-canon-20260618.md` §1 |
| C-G004 | Cross-stage structure check when SYNTHESIS + provenance (C-DG004); semantic CONTRADICTED → phylax | [verified] | S3b C-DG004 + stage3b §5.3 | `piranesi.skill/research-projects/0621-scholia-corpus/returns/stage3b_coverage_gap_deep_20260618_ingest.md` |
| C-G010 | PS-10 piranesi export-only; in-Cursor web requires waive-three-stage + log | [verified] | W03 kill register + negative-space | `references/negative-space.md` § Piranesi export-only |
| C-G011 | layout_mode flat skips ingests/ requirement (procedural) | [verified] | C-DG007 W02×W05 | `piranesi.skill/research-projects/0621-scholia-corpus/returns/stage3b_coverage_gap_deep_20260618_ingest.md` |
| C-R007 | Sparse corpus N<3 papers → piranesi gap-fill then P9 | [verified] | S4 base Q-011 / C-DG007 sparsity | `piranesi.skill/research-projects/0621-scholia-corpus/returns/scholia_decision_canon_20260618.md` §4 |
| C-R008 | Context-length degradation 13.9–85% (Du et al. 2025) — K-01 kill | [verified] | S2b K-01 + S4e gap-fill | `references/kill-register.md` K-01 |
| C-R009 | Anthropic 5k/skill + 25k compaction budget (K-03 vendor) | [verified] | S3b C-DG001 | `piranesi.skill/research-projects/0621-scholia-corpus/returns/stage3b_coverage_gap_deep_20260618_ingest.md` |
| C-R010 | SkillRouter 31–44pp routing drop without body text | [verified] | S2b K-07 | `references/kill-register.md` K-07 |
| C-R011 | S-09 progressive disclosure (engineering blog) — corroborative; token counts use S-06 | [verified] | Gate B: "Progressive disclosure is the core design principle" (2025-10-16) | `references/source-register-corrections.md` S-09 |

**Operator override (2026-06-18):** DRM classification is **not** mechanically verified — manifest `drm:` field is operator metadata only. See `references/negative-space.md`.
