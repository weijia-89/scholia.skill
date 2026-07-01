#!/usr/bin/env bash
# Consumer bridge — run only after scholia verify PASS and operator kickoff wire.
set -euo pipefail

ROOT="/Users/dubs/Projects/scholia.skill"
CORPUS="/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon"
RAG="/Users/dubs/Projects/local-rag-linux-setup"

if [[ ! -d "$RAG" ]]; then
  echo "FAIL: consumer repo missing: $RAG" >&2
  exit 2
fi

bash "$ROOT/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/run_practical_cards_verify_gate.sh"
export CS_AI_CORPUS_SRC="$CORPUS"
bash "$RAG/scripts/sync_cs_ai_corpus.sh"
bash "$RAG/scripts/check_cs_ai_rag.sh" --no-sync
