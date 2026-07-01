#!/usr/bin/env bash
# export_text.sh — pdftotext for PDFs; EPUB → operator must use Calibre or paste export
set -euo pipefail
PROJECT="/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus"
ATTACH_DIR="$PROJECT/attachments"
MAX_SLICE=119000

mkdir -p "$ATTACH_DIR"

python3 /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/export_text.py

bash "$PROJECT/scripts/refresh_status.sh"
