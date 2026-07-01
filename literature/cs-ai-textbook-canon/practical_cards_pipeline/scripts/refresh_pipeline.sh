#!/usr/bin/env bash
# Regenerate curriculum, dispatch prompts, attach slices, STATUS.
set -euo pipefail
PIPE="/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline"
python3 "$PIPE/scripts/plan_card_waves.py"
python3 "$PIPE/scripts/build_attach_slices.py"
python3 "$PIPE/scripts/build_card_dispatch_prompts.py"
python3 "$PIPE/scripts/build_chatprd_attach_uploads.py"
python3 "$PIPE/scripts/build_chatprd_ingest_prompts.py"
python3 "$PIPE/scripts/emit_chatprd_operator_table.py"
bash "$PIPE/scripts/verify_pipeline.sh"
echo "Pipeline refresh complete."
