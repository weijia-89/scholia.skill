#!/usr/bin/env bash
# verify_pipeline.sh — deterministic harness for practical_cards_pipeline artifacts
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

usage() {
  cat <<'EOF'
Usage: verify_pipeline.sh [--self-test] [--batch BATCH_ID] [--route fan-out|inline] [--require-returns] [--summary]

Oracles PC-P01..PC-P14 — curriculum, attach/prompt triangle, operator table,
ChatPRD return YAML (when present or --require-returns).

Exit: 0 pass · 2 fail
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

exec python3 "$SCRIPT_DIR/verify_pipeline.py" "$@"
