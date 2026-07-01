#!/usr/bin/env bash
# Phased trainer verify gate (REVIEW_LOOP_ITER selects depth).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE="${REVIEW_LOOP_ITER:-1}"

case "$PHASE" in
  1)
    echo "--- phase 1: verify + pressure ---"
    bash "$ROOT/scripts/verify_scholia.sh" --self --pressure
    ;;
  2)
    echo "--- phase 2: skill-fitness + phylax ---"
    sf_out=$(python3 /Users/dubs/Projects/skill-fitness.skill/scripts/audit_skill.py "$ROOT")
    echo "$sf_out" | grep -qE '\*\*FAIL:\*\* 0' || { echo "$sf_out"; exit 2; }
    echo "$sf_out" | grep -qE '\*\*WARN:\*\* 0' || { echo "$sf_out"; exit 2; }
    phylax_out=$(python3 /Users/dubs/Projects/phylax.skill/scripts/audit_repo.py "$ROOT" --json)
    echo "$phylax_out" | grep -q '"verdict": "pass"' || exit 2
    echo "$phylax_out" | grep -q '"fail": 0' || exit 2
    ;;
  *)
    echo "--- phase ${PHASE}: full stack re-run ---"
    bash "$ROOT/scripts/verify_scholia.sh" --self --pressure
    sf_out=$(python3 /Users/dubs/Projects/skill-fitness.skill/scripts/audit_skill.py "$ROOT")
    echo "$sf_out" | grep -qE '\*\*FAIL:\*\* 0' || { echo "$sf_out"; exit 2; }
    phylax_out=$(python3 /Users/dubs/Projects/phylax.skill/scripts/audit_repo.py "$ROOT" --json)
    echo "$phylax_out" | grep -q '"verdict": "pass"' || exit 2
    ;;
esac

echo "PASS: trainer verify gate phase ${PHASE}"
