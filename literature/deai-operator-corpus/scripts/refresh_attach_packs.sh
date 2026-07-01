#!/usr/bin/env bash
# refresh_attach_packs.sh — rebuild ChatPRD upload files in attachments/
set -euo pipefail
PROJECT="/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus"
python3 "$PROJECT/scripts/build_attach_uploads.py"
echo "OK: $PROJECT/attachments/ (upload files only)"