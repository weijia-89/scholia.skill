# Cross-stage consistency log (C-DG004)

META: template · populate after phylax semantic check on child skill

| date | skill | claims_checked | CONTRADICTED | DRIFT | verdict | operator |
|------|-------|----------------|--------------|-------|---------|----------|
| YYYY-MM-DD | {slug}.skill | 0 | 0 | 0% | PASS | — |

**Rules:** CONTRADICTED >0 → block ship. DRIFT >20% → WARN + operator review. Mechanical structure check: `bash scripts/check_cross_stage_consistency.sh TARGET`.
