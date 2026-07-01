#!/usr/bin/env bash
# Phased scholia verify gate (REVIEW_LOOP_ITER selects depth).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE="${REVIEW_LOOP_ITER:-1}"

case "$PHASE" in
  1)
    echo "--- phase 1: scholia self ---"
    bash "$ROOT/scripts/verify_scholia.sh" --self
    ;;
  2)
    echo "--- phase 2: pressure + skill-fitness ---"
    bash "$ROOT/scripts/verify_scholia.sh" --self --pressure
    sf_out=$(python3 /Users/dubs/Projects/skill-fitness.skill/scripts/audit_skill.py "$ROOT")
    echo "$sf_out" | grep -qE '\*\*FAIL:\*\* 0' || { echo "$sf_out"; exit 2; }
    echo "$sf_out" | grep -qE '\*\*WARN:\*\* 0' || { echo "$sf_out"; exit 2; }
    ;;
  *)
    echo "--- phase ${PHASE}: pressure + cross-stage ---"
    bash "$ROOT/scripts/verify_scholia.sh" --self --pressure --cross-stage
    ;;
esac

echo "PASS: scholia verify gate phase ${PHASE}"
