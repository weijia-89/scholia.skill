#!/usr/bin/env bash
# check_cross_stage_consistency.sh — C-DG004 mechanical structure check
# Semantic SUPPORTED/CONTRADICTED/DRIFT judge deferred to phylax (no LLM in script).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=lib/sf06_provenance.sh
source "$ROOT/scripts/lib/sf06_provenance.sh"
TARGET="${1:-$ROOT}"
FAILS=0
WARNS=0

usage() {
  cat <<'EOF'
Usage: check_cross_stage_consistency.sh [path/to/child.skill]

Lightweight cross-stage structure check when both exist:
  literature/ingests/SYNTHESIS.md
  references/provenance.md

Exit: 0 pass or WARN-only · 2 fail (Stop hook block)
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

fail() { echo "FAIL: $1"; FAILS=$((FAILS + 1)); }
warn() { echo "WARN: $1"; WARNS=$((WARNS + 1)); }
pass() { echo "PASS: $1"; }

if [[ ! -d "$TARGET" ]]; then
  fail "target directory missing: $TARGET"
  echo "---"
  echo "FAIL=$FAILS WARN=$WARNS"
  exit 2
fi

synthesis="${TARGET}/literature/ingests/SYNTHESIS.md"
prov="${TARGET}/references/provenance.md"

if [[ ! -f "$synthesis" || ! -f "$prov" ]]; then
  pass "C-DG004 N/A (SYNTHESIS.md and provenance.md not both present)"
  exit 0
fi

pass "C-DG004 inputs present: SYNTHESIS.md + provenance.md"

sf06_count_provenance_rows "$prov"

if [[ "$sf06_unanchored" -gt 0 ]]; then
  warn "C-DG004: ${sf06_unanchored} claims in provenance.md have no DOI/epistemic anchor (SF-06 pattern)"
else
  pass "C-DG004: all ${sf06_claim_rows} provenance rows anchored (DOI/tag)"
fi

if [[ ! -s "$synthesis" ]]; then
  fail "C-DG004: SYNTHESIS.md is empty"
fi

echo "INFO: ${sf06_claim_rows} claims in provenance.md — run phylax mode=full for semantic consistency (SUPPORTED/CONTRADICTED/DRIFT)"

echo "---"
echo "FAIL=$FAILS WARN=$WARNS"
if [[ "$FAILS" -gt 0 ]]; then
  exit 2
fi
exit 0
