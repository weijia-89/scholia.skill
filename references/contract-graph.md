# scholia contract graph

Gate enforcement map (W10+S4e merge). **Necessary** = `verify_scholia.sh`; **sufficient** = phylax semantic.

| Gate ID | Description | Enforced-by | Status |
|---------|-------------|-------------|--------|
| SF-01 | frontmatter name+description | verify_scholia.sh | active |
| SF-02 | triggers + σ− boundaries | phylax doc | active |
| SF-03 | SKILL.md body ≤500 lines | verify_scholia.sh | active |
| SF-04 | references/ + provenance artifact | verify_scholia.sh | active |
| SF-05 | no absolute paths in child body | verify_scholia.sh | active |
| SF-06 | provenance DOI/tag not path-only | verify_scholia.sh (child provenance.md) | active |
| SF-07 | load-bearing thresholds cite CLAIMS.md | CLAIMS.md + phylax doc | active |
| SF-08 | textbook exercise hooks | phylax doc (chapter-ingest prompt) | active |
| SF-09 | shellcheck on scripts/ | verify_scholia.sh `--self` | active WARN |
| SF-11 | manifest PDF/ingest count (PS-02) | verify_scholia.sh + hooks-config | active WARN |
| SF-10 | external claim ledger | CLAIMS.md | active |
| SF-12 | ingests ≤4500w | verify_scholia.sh | active |
| SF-13 | LITERATURE_INDEX present | verify_scholia.sh | active |
| SF-14 | L3 pressure scenarios | verify_scholia.sh `--pressure` (PS-01/02/03/04/07/08/09/10/11/12) | active |
| sub-skills | paper + chapter prompts, manifest template, index | verify_scholia.sh `--self` | active |
| monolith | N≥5 PDFs require ingests/ | verify_scholia.sh | active |
| DRM | manifest metadata only | operator (waived mechanical 2026-06-18) | doc |
| kill-P9 | no literal P9 in scholia SKILL | verify_scholia.sh | active |
| kill-gymbuddy | no gymbuddy recommendation | verify_scholia.sh | active |
| pairs_with | doc-only convention | phylax doc | active |
| phylax.self | context:fork fresh session | trainer + phylax doc | active |
| C-DG004 | cross-stage structure (provenance rows + anchors when SYNTHESIS.md present) | check_cross_stage_consistency.sh (auto on child verify; `--cross-stage`) | active |
| C-DG004 semantic | SUPPORTED/CONTRADICTED/DRIFT per claim | phylax mode=full (no LLM in verify script) | active |
| layout_mode flat | procedural corpus layout (C-DG007) | verify_scholia.sh (manifest layout_mode: flat) | active |
| SF-15 | practical_usage cards when manifest flag set | verify_practical_cards.sh; auto in verify_scholia.sh corpus mode | active |

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --self
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh --pressure
bash /Users/dubs/Projects/scholia.skill/scripts/check_cross_stage_consistency.sh /path/to/child.skill
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh --self-test
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh /path/to/corpus/root
```
