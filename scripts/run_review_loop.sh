#!/usr/bin/env bash
# Bounded scholia review loop — verify + pressure + skill-fitness with circuit breakers.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GUARD="$ROOT/scripts/lib/review_loop_guard.sh"
GATE="$ROOT/scripts/run_scholia_verify_gate.sh"

MIN_PASS=2
MAX_ATTEMPTS=8
MAX_SECS=900
STUCK_LIMIT=2

# shellcheck source=/Users/dubs/Projects/scholia.skill/scripts/lib/review_loop_guard.sh
source "$GUARD"

review_loop_guard_run "$MIN_PASS" "$MAX_ATTEMPTS" "$MAX_SECS" "$STUCK_LIMIT" \
  "scholia-review" -- bash "$GATE"
