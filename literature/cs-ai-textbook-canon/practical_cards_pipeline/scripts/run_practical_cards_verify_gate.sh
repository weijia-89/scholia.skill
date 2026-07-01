#!/usr/bin/env bash
# Phased scholia verify gate for practical cards (REVIEW_LOOP_ITER selects depth).
# REVIEW_LOOP_ITER=1 surface oracles · 2+ deepen unexplored paths.
set -euo pipefail

ROOT="/Users/dubs/Projects/scholia.skill"
CORPUS="/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon"
PIPE="$CORPUS/practical_cards_pipeline"
PHASE="${REVIEW_LOOP_ITER:-1}"

phase_banner() {
  echo "--- phase ${PHASE}: $1 ---"
}

case "$PHASE" in
  1)
    phase_banner "surface oracles (self-test, unit, summary, corpus layout)"
    bash "$ROOT/scripts/verify_practical_cards.sh" --self-test
    python3 "$ROOT/scripts/test_verify_practical_cards.py" -q
    python3 "$ROOT/scripts/test_verify_practical_cards_pipeline.py" -q
    bash "$ROOT/scripts/verify_practical_cards_pipeline.sh" --self-test
    bash "$ROOT/scripts/verify_practical_cards_pipeline.sh" --summary
    bash "$ROOT/scripts/verify_practical_cards.sh" "$CORPUS"
    bash "$ROOT/scripts/verify_scholia.sh" "$CORPUS"
    ;;
  2)
    phase_banner "pressure + skill-fitness + full pipeline batch + inline route"
    bash "$ROOT/scripts/verify_scholia.sh" --self --pressure
    sf_out=$(python3 /Users/dubs/Projects/skill-fitness.skill/scripts/audit_skill.py "$ROOT")
    echo "$sf_out" | grep -qE '\*\*FAIL:\*\* 0' || { echo "$sf_out"; exit 2; }
    batch=$(python3 "$PIPE/scripts/pick_review_batch.py" 1)
    echo "deep batch: ${batch}"
    bash "$ROOT/scripts/verify_practical_cards_pipeline.sh" --batch "$batch"
    bash "$ROOT/scripts/verify_practical_cards_pipeline.sh" --route inline --summary
    bash "$ROOT/scripts/verify_scholia.sh" "$CORPUS"
    bash "$ROOT/scripts/verify_practical_cards.sh" "$CORPUS"
    ;;
  *)
    phase_banner "rotate batch + full corpus pipeline + scholia self"
    batch=$(python3 "$PIPE/scripts/pick_review_batch.py" "$PHASE")
    echo "rotate batch: ${batch}"
    bash "$ROOT/scripts/verify_practical_cards_pipeline.sh" --batch "$batch"
    bash "$ROOT/scripts/verify_practical_cards_pipeline.sh"
    bash "$ROOT/scripts/verify_scholia.sh" --self
    bash "$ROOT/scripts/verify_practical_cards.sh" "$CORPUS"
  ;;
esac

echo "PASS: practical-cards verify gate phase ${PHASE}"
