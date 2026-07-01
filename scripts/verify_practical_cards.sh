#!/usr/bin/env bash
# verify_practical_cards.sh — practical_usage implementation card gate (scholia v2)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CORPUS="${1:-}"

usage() {
  cat <<'EOF'
Usage: verify_practical_cards.sh [corpus_root]

  corpus_root  Path to literature corpus (required for meaningful checks)

Exit: 0 pass · 2 fail

Checks (via verify_practical_cards.py):
  - --self-test   run parser regression oracles
  - manifest practical_usage_required: true → card YAMLs must exist (≥3 when flag set)
  - each card: exercise_name, source_anchor, ≥3 steps unless procedure_gap: true, ≤12 steps max
  - quality_level required when manifest flag set
  - banned send-script patterns
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

if [[ "${1:-}" == "--self-test" || "${1:-}" == "--self" ]]; then
  exec python3 "$SCRIPT_DIR/verify_practical_cards.py" --self-test
fi

if [[ -z "$CORPUS" ]]; then
  echo "FAIL: corpus_root required" >&2
  usage
  exit 2
fi

exec python3 "$SCRIPT_DIR/verify_practical_cards.py" "$CORPUS"
