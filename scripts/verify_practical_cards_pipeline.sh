#!/usr/bin/env bash
# Root alias — cs-ai practical cards pipeline output harness
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/verify_pipeline.sh" "$@"
