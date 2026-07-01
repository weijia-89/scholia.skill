#!/usr/bin/env bash
# sync_banter_r02_practical_cards_mirror.sh — copy practical_cards aletheia SSOT → scholia mirror
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC="/Users/dubs/Projects/aletheia.skill/research/scholia/banter-r02-corpus/literature/metadata/practical_cards"
DST="$ROOT/literature/banter-r02-corpus/metadata/practical_cards"

if [[ ! -d "$SRC" ]]; then
  echo "FAIL: SSOT card root missing: $SRC" >&2
  exit 2
fi

mkdir -p "$DST"
count=0
for f in "$SRC"/*.yaml; do
  [[ -f "$f" ]] || continue
  cp "$f" "$DST/"
  count=$((count + 1))
done

if [[ "$count" -lt 1 ]]; then
  echo "FAIL: no YAML files copied from $SRC" >&2
  exit 2
fi

echo "PASS: synced $count practical card(s) to $DST"
bash "$SCRIPT_DIR/verify_practical_cards.sh" "$ROOT/literature/banter-r02-corpus"
