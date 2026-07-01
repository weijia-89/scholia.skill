#!/usr/bin/env bash
# Bounded autonomous review loop — min 2 passes, escalating phases, circuit breakers.
# Consumer wire: run_practical_cards_consumer_wire.sh (kickoff wire only).
set -euo pipefail

ROOT="/Users/dubs/Projects/scholia.skill"
GATE="$ROOT/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_verify_gate.sh"
GUARD="$ROOT/scripts/lib/review_loop_guard.sh"

MIN_PASS=2
MAX_ATTEMPTS=8
MAX_SECS=900
STUCK_LIMIT=2

# shellcheck source=/Users/dubs/Projects/scholia.skill/scripts/lib/review_loop_guard.sh
source "$GUARD"

review_loop_guard_run "$MIN_PASS" "$MAX_ATTEMPTS" "$MAX_SECS" "$STUCK_LIMIT" \
  "practical-cards-verify" -- bash "$GATE"
