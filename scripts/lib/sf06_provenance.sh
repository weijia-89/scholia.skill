#!/usr/bin/env bash
# Shared SF-06 / C-DG004 provenance row helpers (sourced by verify + cross-stage scripts)
# Usage: source .../sf06_provenance.sh
# Sets: sf06_claim_rows sf06_unanchored

sf06_is_separator_row() {
  echo "$1" | grep -qE '^[|][[:space:]]*-{3,}'
}

sf06_count_provenance_rows() {
  local prov="$1"
  sf06_claim_rows=0
  sf06_unanchored=0
  [[ -f "$prov" ]] || return 0
  while IFS= read -r line; do
    [[ "$line" == \|* ]] || continue
    echo "$line" | grep -qE '^\|[[:space:]]*claim-id[[:space:]]*\|' && continue
    sf06_is_separator_row "$line" && continue
    sf06_claim_rows=$((sf06_claim_rows + 1))
    local doi
    doi=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $6); print $6}')
    if [[ -z "$doi" || "$doi" == "…" || "$doi" == "none" || "$doi" == "[none]" ]]; then
      sf06_unanchored=$((sf06_unanchored + 1))
      continue
    fi
    if ! echo "$doi" | grep -Eiq 'doi|http|isbn|10\.|\[[a-zA-Z0-9_-]+\]'; then
      sf06_unanchored=$((sf06_unanchored + 1))
    fi
  done <"$prov"
}
