#!/usr/bin/env bash
# verify_scholia.sh — deterministic gates (W10 §9 + S4e §6 merged)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$ROOT"
SELF=0
PRESSURE=0
CROSS_STAGE=0
FAILS=0
WARNS=0

usage() {
  cat <<'EOF'
Usage: verify_scholia.sh [--self] [--pressure] [--cross-stage] [path/to/skill-or-child.skill-or-corpus]

  --self         verify scholia.skill root
  --pressure     run PS-01/03/04/07/08/09/10/11/12 mechanical oracles
  --cross-stage  run C-DG004 cross-stage structure check only
  path           verify generated child skill directory, or literature corpus root
                 (auto-detect: metadata/corpus_manifest.yaml + ingests/ at path)

Exit: 0 pass · 2 fail (Stop hook block)
EOF
}

for arg in "$@"; do
  case "$arg" in
    --self)
      SELF=1
      TARGET="$ROOT"
      ;;
    --pressure)
      PRESSURE=1
      ;;
    --cross-stage)
      CROSS_STAGE=1
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    -*)
      echo "Unknown option: $arg" >&2
      usage
      exit 2
      ;;
    *)
      TARGET="$arg"
      ;;
  esac
done

fail() { echo "FAIL: $1"; FAILS=$((FAILS + 1)); }
warn() { echo "WARN: $1"; WARNS=$((WARNS + 1)); }
pass() { echo "PASS: $1"; }

is_corpus_root() {
  [[ -f "$TARGET/metadata/corpus_manifest.yaml" && -d "$TARGET/ingests" ]]
}

# True when metadata/corpus_manifest.yaml declares mirror: true (consumer SSOT elsewhere)
is_mirror_corpus() {
  local manifest="$TARGET/metadata/corpus_manifest.yaml"
  [[ -f "$manifest" ]] || return 1
  grep -Ev '^[[:space:]]*#' "$manifest" | grep -Eiq 'mirror:[[:space:]]*(true|yes|1)([[:space:]]|$|#)'
}

run_corpus_verify() {
  pass "corpus root detected at $TARGET"

  if [[ -f "$TARGET/metadata/corpus_manifest.yaml" ]]; then
    pass "corpus manifest present"
  else
    fail "corpus manifest missing: metadata/corpus_manifest.yaml"
  fi

  if [[ -f "$TARGET/index/LITERATURE_INDEX.md" ]]; then
    pass "SF-13 LITERATURE_INDEX present (index/)"
  elif [[ -f "$TARGET/ingests/LITERATURE_INDEX.md" ]]; then
    pass "SF-13 LITERATURE_INDEX present (ingests/)"
  else
    fail "SF-13 LITERATURE_INDEX missing"
  fi

  if [[ -f "$TARGET/SYNTHESIS.md" ]]; then
    pass "SYNTHESIS.md present at corpus root"
  else
    warn "SYNTHESIS.md missing at corpus root"
  fi

  if is_mirror_corpus; then
    pass "corpus mirror mode (pdfs/text/ingests SSOT elsewhere)"
  elif [[ -d "$TARGET/pdfs" && -d "$TARGET/text" ]]; then
    pass "corpus layout pdfs/ + text/"
  else
    warn "corpus missing pdfs/ or text/"
  fi

  local ingest_fail=0 f w
  while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    w=$(wc -w < "$f" | tr -d ' ')
    if [[ "$w" -gt 4500 ]]; then
      fail "SF-12 ingest exceeds 4500w: $f ($w words)"
      ingest_fail=1
    fi
  done < <(find "$TARGET/ingests" -maxdepth 1 -name '*.md' ! -name 'LITERATURE_INDEX.md' ! -name 'SYNTHESIS.md' 2>/dev/null || true)
  if [[ "$ingest_fail" -eq 0 ]]; then
    pass "SF-12 ingest word caps"
  fi

  local pdf_count=0 ingest_count=0
  if [[ -d "$TARGET/pdfs" ]]; then
    pdf_count=$( (find "$TARGET/pdfs" -maxdepth 1 -name '*.pdf' 2>/dev/null || true) | wc -l | tr -d ' ')
  fi
  if [[ -d "$TARGET/ingests" ]]; then
    ingest_count=$( (find "$TARGET/ingests" -maxdepth 1 -name '*_ingest.md' 2>/dev/null || true) | wc -l | tr -d ' ')
  fi
  if ! is_mirror_corpus && [[ "$pdf_count" -ge 5 ]]; then
    if [[ "$ingest_count" -gt 0 ]]; then
      pass "monolith guard: $pdf_count PDFs with $ingest_count ingests"
    else
      fail "monolith guard: $pdf_count PDFs but no chapter ingests"
    fi
  fi

  if grep -Ev '^[[:space:]]*#' "$TARGET/metadata/corpus_manifest.yaml" \
    | grep -Eiq 'practical_usage_required:[[:space:]]*(true|yes|1)([[:space:]]|$|#)'; then
    if python3 "$ROOT/scripts/verify_practical_cards.py" "$TARGET"; then
      pass "SF-15 practical_usage cards"
    else
      fail "SF-15 practical_usage cards (verify_practical_cards.py)"
    fi
  else
    pass "SF-15 N/A (practical_usage_required not set)"
  fi
}

# shellcheck source=lib/sf06_provenance.sh
source "$ROOT/scripts/lib/sf06_provenance.sh"

# True when literature/metadata/corpus_manifest.yaml declares layout_mode: flat (C-DG007)
is_layout_mode_flat() {
  local manifest="$TARGET/literature/metadata/corpus_manifest.yaml"
  if [[ ! -f "$manifest" ]]; then
    return 1
  fi
  grep -Ev '^[[:space:]]*#' "$manifest" | grep -Eiq 'layout_mode:[[:space:]]*flat([[:space:]]|$|#)'
}

check_sf06_provenance() {
  local prov="$TARGET/references/provenance.md"
  if [[ ! -f "$prov" ]]; then
    if [[ "$SELF" -eq 1 && "$TARGET" == "$ROOT" ]]; then
      pass "SF-06 N/A on root (provenance template only)"
    else
      pass "SF-06 N/A (no provenance.md)"
    fi
    return
  fi
  sf06_count_provenance_rows "$prov"
  if [[ "$sf06_unanchored" -eq 0 ]]; then
    pass "SF-06 provenance DOI/tag discipline"
  else
    fail "SF-06: $sf06_unanchored provenance entries lack DOI and epistemic tag"
  fi
}

check_sf09_shellcheck() {
  if [[ "$SELF" -ne 1 || "$TARGET" != "$ROOT" ]]; then
    return
  fi
  if ! command -v shellcheck >/dev/null 2>&1; then
    warn "SF-09: shellcheck not installed (skipped)"
    return
  fi
  local sc_warn=0 f
  for f in "$ROOT"/scripts/*.sh "$ROOT"/scripts/lib/*.sh; do
    [[ -f "$f" ]] || continue
    if ! shellcheck -S warning -e SC1091,SC2154 "$f" >/dev/null 2>&1; then
      warn "SF-09: shellcheck findings in $f"
      sc_warn=1
    fi
  done
  if [[ "$sc_warn" -eq 0 ]]; then
    pass "SF-09 shellcheck clean"
  fi
}

check_sf15_practical_cards_self() {
  if [[ "$SELF" -ne 1 || "$TARGET" != "$ROOT" ]]; then
    return
  fi
  if python3 "$ROOT/scripts/verify_practical_cards.py" --self-test; then
    pass "SF-15 verify_practical_cards self-test"
  else
    fail "SF-15 verify_practical_cards self-test"
  fi
}

check_sf11_ingest_pdf_parity() {
  local lit="$1"
  [[ -d "$lit/pdfs" && -d "$lit/ingests" ]] || return 0
  local pdf_count ingest_count
  pdf_count=$(find "$lit/pdfs" -name '*.pdf' 2>/dev/null | wc -l | tr -d ' ')
  ingest_count=$(find "$lit/ingests" -name '*.md' \
    ! -name 'SYNTHESIS.md' ! -name 'LITERATURE_INDEX.md' 2>/dev/null | wc -l | tr -d ' ')
  [[ "$pdf_count" -gt 0 ]] || return 0
  if [[ "$ingest_count" -eq 0 ]]; then
    return 0
  fi
  if [[ "$pdf_count" -ne "$ingest_count" ]]; then
    warn "SF-11: $pdf_count PDFs but $ingest_count paper ingests (PS-02)"
  else
    pass "SF-11 PDF/ingest count parity ($pdf_count)"
  fi
  return 0
}

run_pressure_scenarios() {
  local verify="$ROOT/scripts/verify_scholia.sh"
  local tmp pass=0 pfail=0
  tmp=$(mktemp -d)
  trap 'rm -rf "$tmp"' RETURN

  run_case() {
    local id="$1" expect_exit="$2"
    shift 2
    echo "=== ${id} ==="
    set +e
    "$@"
    local rc=$?
    set -e
    if [[ "$rc" -eq "$expect_exit" ]]; then
      echo "PASS ${id} (exit ${rc})"
      pass=$((pass + 1))
    else
      echo "FAIL ${id} (expected exit ${expect_exit}, got ${rc})"
      pfail=$((pfail + 1))
    fi
  }

  run_case PS-01 0 bash "$verify" --self

  local fix04="$tmp/ps04.child.skill"
  mkdir -p "$fix04/references"
  cat >"$fix04/SKILL.md" <<'EOF'
---
name: ps04.child
description: pressure fixture
---
# fixture
EOF
  cat >"$fix04/references/provenance.md" <<'EOF'
| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| C-001 | test claim | inferred | Paper | literature/ingests/foo.md | literature/ingests/foo.md | §1 |
EOF
  run_case PS-04 2 bash "$verify" "$fix04"

  local fix02="$tmp/ps02.child.skill"
  mkdir -p "$fix02/literature"/{pdfs,text,ingests,metadata,index}
  mkdir -p "$fix02/references"
  cp "$ROOT/references/provenance-template.md" "$fix02/references/"
  local j
  for j in 1 2 3 4 5; do
    touch "$fix02/literature/pdfs/paper_${j}.pdf"
  done
  for j in 1 2 3 4; do
    echo "# ingest $j" >"$fix02/literature/ingests/paper_${j}.md"
  done
  cat >"$fix02/SKILL.md" <<'EOF'
---
name: ps02.child
description: SF-11 partial ingest fixture
---
# fixture
EOF
  run_case PS-02 0 bash "$verify" "$fix02"

  local fix03="$tmp/ps03.child.skill"
  mkdir -p "$fix03/literature"/{pdfs,text,ingests,metadata,index}
  mkdir -p "$fix03/references"
  cp "$ROOT/references/provenance-template.md" "$fix03/references/"
  cat >"$fix03/SKILL.md" <<'EOF'
---
name: ps03.child
description: SF-12 fixture
---
# fixture
EOF
  python3 -c "print('word ' * 5001)" >"$fix03/literature/ingests/overlimit.md"
  run_case PS-03 2 bash "$verify" "$fix03"

  local fix07="$tmp/ps07.child.skill"
  mkdir -p "$fix07/references"
  cp "$ROOT/references/provenance-template.md" "$fix07/references/"
  cat >"$fix07/SKILL.md" <<'EOF'
---
description: missing name field
---
# fixture
EOF
  run_case PS-07 2 bash "$verify" "$fix07"

  local fix08="$tmp/ps08.child.skill"
  mkdir -p "$fix08/references"
  cp "$ROOT/references/provenance-template.md" "$fix08/references/"
  cat >"$fix08/SKILL.md" <<'EOF'
---
name: ps08.child
description: SF-05 fixture
---
See /Users/operator/secret/path
EOF
  run_case PS-08 2 bash "$verify" "$fix08"

  local fix09="$tmp/ps09.child.skill"
  mkdir -p "$fix09/literature"/{pdfs,text,ingests,metadata,index}
  local i
  for i in 1 2 3 4 5; do
    touch "$fix09/literature/pdfs/paper_${i}.pdf"
  done
  cat >"$fix09/SKILL.md" <<'EOF'
---
name: ps09.child
description: monolith guard fixture
---
# fixture
EOF
  mkdir -p "$fix09/references"
  cp "$ROOT/references/provenance-template.md" "$fix09/references/"
  run_case PS-09 2 bash "$verify" "$fix09"

  local fix11="$tmp/ps11.flat.child.skill"
  mkdir -p "$fix11/literature"/{pdfs,text,metadata}
  mkdir -p "$fix11/references"
  cp "$ROOT/references/provenance-template.md" "$fix11/references/"
  echo 'layout_mode: flat' >"$fix11/literature/metadata/corpus_manifest.yaml"
  touch "$fix11/literature/pdfs/howto.pdf"
  mkdir -p "$fix11/literature/text/howto"
  echo "steps" >"$fix11/literature/text/howto/howto.md"
  cat >"$fix11/SKILL.md" <<'EOF'
---
name: ps11.flat.child
description: layout_mode flat fixture
---
# fixture
EOF
  run_case PS-11 0 bash "$verify" "$fix11"

  local fix12="$tmp/ps12.cdg004.child.skill"
  mkdir -p "$fix12/literature"/{pdfs,text,ingests,metadata,index}
  mkdir -p "$fix12/references"
  cat >"$fix12/references/provenance.md" <<'EOF'
| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| C-001 | test | quoted | Paper | 10.1234/ps12 | literature/ingests/foo.md | §1 |
EOF
  echo "# synthesis content" >"$fix12/literature/ingests/SYNTHESIS.md"
  cat >"$fix12/SKILL.md" <<'EOF'
---
name: ps12.cdg004.child
description: C-DG004 cross-stage fixture
---
# fixture
EOF
  run_case PS-12 0 bash "$verify" "$fix12"

  local fix12bad="$tmp/ps12bad.cdg004.child.skill"
  cp -R "$fix12" "$fix12bad"
  : >"$fix12bad/literature/ingests/SYNTHESIS.md"
  cat >"$fix12bad/SKILL.md" <<'EOF'
---
name: ps12bad.cdg004.child
description: C-DG004 empty synthesis fixture
---
# fixture
EOF
  run_case PS-12-empty 2 bash "$verify" "$fix12bad"

  echo "=== PS-10 ==="
  local skill_md="$ROOT/SKILL.md"
  local ps10_fail=0
  if grep -Ei 'WebSearch|WebFetch' "$skill_md" >/dev/null 2>&1; then
    echo "FAIL PS-10: SKILL.md references in-Cursor web tools (piranesi must be export-only)"
    ps10_fail=1
  elif ! grep -q 'export-only' "$skill_md" || ! grep -q 'waive-three-stage' "$skill_md"; then
    echo "FAIL PS-10: SKILL.md missing piranesi export-only or waive-three-stage guard"
    ps10_fail=1
  else
    echo "PASS PS-10: piranesi export-only + waive-three-stage documented in SKILL.md"
  fi
  if [[ "$ps10_fail" -eq 0 ]]; then
    pass=$((pass + 1))
  else
    pfail=$((pfail + 1))
  fi

  echo "---"
  echo "pressure: PASS=${pass} FAIL=${pfail}"
  {
    echo "date=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "PS-01 PS-02 PS-03 PS-04 PS-07 PS-08 PS-09 PS-10 PS-11 PS-12 PS-12-empty via verify_scholia.sh --pressure"
    echo "PASS=${pass} FAIL=${pfail}"
  } >"$ROOT/tests/pressure_scenarios/last_run.txt"

  [[ "$pfail" -eq 0 ]]
}

run_cross_stage_check() {
  local cs="$ROOT/scripts/check_cross_stage_consistency.sh"
  if [[ ! -x "$cs" ]]; then
    fail "C-DG004 check script missing or not executable"
    return
  fi
  set +e
  bash "$cs" "$TARGET"
  local rc=$?
  set -e
  if [[ "$rc" -eq 2 ]]; then
    fail "C-DG004 cross-stage consistency check failed (exit $rc)"
  elif [[ "$rc" -ne 0 ]]; then
    fail "C-DG004 cross-stage check unexpected exit $rc"
  else
    pass "C-DG004 cross-stage structure check complete"
  fi
}

run_target_verify() {
  if is_corpus_root; then
    run_corpus_verify
    return
  fi

  local skill_md="$TARGET/SKILL.md"
  if [[ ! -f "$skill_md" ]]; then
    fail "SKILL.md missing at $TARGET"
    return
  fi

  if head -1 "$skill_md" | grep -q '^---$'; then
    pass "SF-01 frontmatter block present"
  else
    fail "SF-01 missing YAML frontmatter"
  fi

  if grep -q '^name:' "$skill_md" && grep -q '^description:' "$skill_md"; then
    pass "SF-01 name+description in frontmatter"
  else
    fail "SF-01 name or description missing"
  fi

  local body_lines
  body_lines=$(awk 'BEGIN{s=0} /^---$/{c++; next} c>=2{s++} END{print s}' "$skill_md")
  if [[ "$body_lines" -le 500 ]]; then
    pass "SF-03 SKILL.md body ≤500 lines ($body_lines)"
  else
    fail "SF-03 SKILL.md body exceeds 500 lines ($body_lines)"
  fi

  local body_tmp
  body_tmp=$(mktemp)
  awk '/^---$/{c++; next} c>=2{print}' "$skill_md" >"$body_tmp"
  if grep -E '/Users/|/home/|/[A-Za-z]:\\' "$body_tmp" >/dev/null 2>&1; then
    if [[ "$SELF" -eq 1 && "$TARGET" == "$ROOT" ]]; then
      warn "SF-05 absolute paths in scholia root body (child skills must not)"
    else
      fail "SF-05 hardcoded absolute paths in SKILL.md body"
    fi
  else
    pass "SF-05 no absolute paths in SKILL.md body"
  fi
  rm -f "$body_tmp"

  if [[ "$TARGET" == "$ROOT" ]]; then
    if awk '/^---$/{c++; next} c>=2' "$skill_md" | grep -E '\bP9\b' >/dev/null 2>&1; then
      fail "kill-register: literal P9 reference in scholia SKILL.md (use paper fan-out)"
    else
      pass "kill-register: no P9 literal in scholia SKILL.md"
    fi
  fi

  if grep -Ei 'use gymbuddy|route.*gymbuddy|pairs_with.*gymbuddy' "$skill_md" >/dev/null 2>&1; then
    fail "kill-register: gymbuddy recommended in SKILL.md"
  else
    pass "kill-register: no gymbuddy recommendation"
  fi

  if [[ -d "$TARGET/references" ]]; then
    pass "SF-04 references/ exists"
  else
    if [[ "$SELF" -eq 1 ]]; then
      warn "SF-04 references/ missing on root (templates expected at repo root)"
    else
      fail "SF-04 references/ missing"
    fi
  fi

  if [[ -f "$TARGET/references/provenance-template.md" || -f "$TARGET/references/provenance.md" ]]; then
    pass "SF-04 provenance artifact present"
  else
    if [[ "$SELF" -eq 1 ]]; then
      warn "SF-04 provenance template missing"
    else
      fail "SF-04 provenance.md or template missing"
    fi
  fi

  if [[ "$TARGET" != "$ROOT" ]]; then
    if grep -q '^name:' "$skill_md"; then
      local folder_name yaml_name
      folder_name=$(basename "$TARGET" | sed 's/\.skill$//' | tr '[:upper:]' '[:lower:]' | tr '_' '-')
      yaml_name=$(grep -E '^name:' "$skill_md" | head -1 | sed 's/^name:[[:space:]]*//' | tr -d '"' | tr -d "'")
      if [[ "$yaml_name" == "$folder_name" ]]; then
        pass "name/folder match ($yaml_name)"
      else
        fail "name/folder mismatch: frontmatter name=$yaml_name folder=$folder_name"
      fi
    fi
  fi

  if [[ "$SELF" -eq 1 && "$TARGET" == "$ROOT" ]]; then
    for req in \
      prompts/literature-paper-ingest.md \
      prompts/literature-chapter-ingest.md \
      prompts/practical-usage-card-fanout.md \
      prompts/output-mode-study-guide.md \
      prompts/output-mode-procedural.md \
      prompts/output-mode-notebooklm-pack.md \
      references/sub-skills-index.md \
      references/corpus-manifest-template.yaml \
      references/practical-usage-schema.md \
      references/practical-usage-consumer-bridge.md \
      references/external-paths.md \
      scripts/verify_practical_cards.sh \
      scripts/sync_banter_r02_practical_cards_mirror.sh \
      scripts/check_cross_stage_consistency.sh \
      scripts/lib/sf06_provenance.sh; do
      if [[ -f "$TARGET/$req" ]]; then
        pass "sub-skill present: $req"
      else
        fail "sub-skill missing: $req"
      fi
    done
    check_sf09_shellcheck
    check_sf15_practical_cards_self
  fi

  check_sf06_provenance

  local lit="$TARGET/literature"
  local flat=0
  if is_layout_mode_flat; then
    flat=1
  fi
  if [[ "$flat" -eq 1 ]]; then
    if [[ -d "$lit/pdfs" && -d "$lit/text" && -d "$lit/metadata" ]]; then
      pass "corpus layout flat (layout_mode: flat; ingests/ optional)"
      if [[ -d "$lit/ingests" ]]; then
        local ingest_fail=0 f w
        while IFS= read -r f; do
          [[ -z "$f" ]] && continue
          w=$(wc -w < "$f" | tr -d ' ')
          if [[ "$w" -gt 4500 ]]; then
            fail "SF-12 ingest exceeds 4500w: $f ($w words)"
            ingest_fail=1
          fi
        done < <(find "$lit/ingests" -name '*.md' 2>/dev/null || true)
        if [[ "$ingest_fail" -eq 0 ]]; then
          pass "SF-12 ingest word caps (optional ingests/)"
        fi
      fi
    elif [[ "$SELF" -eq 1 && "$TARGET" == "$ROOT" ]]; then
      warn "corpus layout not initialized (run: mkdir -p literature/{pdfs,text,metadata})"
    else
      fail "corpus layout missing literature/{pdfs,text,metadata}/ (flat mode)"
    fi
  elif [[ -d "$lit/pdfs" && -d "$lit/text" && -d "$lit/ingests" && -d "$lit/metadata" ]]; then
    pass "corpus layout literature/{pdfs,text,ingests,metadata}/"
    local ingest_fail=0 f w pdf_count
    while IFS= read -r f; do
      [[ -z "$f" ]] && continue
      w=$(wc -w < "$f" | tr -d ' ')
      if [[ "$w" -gt 4500 ]]; then
        fail "SF-12 ingest exceeds 4500w: $f ($w words)"
        ingest_fail=1
      fi
    done < <(find "$lit/ingests" -name '*.md' 2>/dev/null || true)
    if [[ "$ingest_fail" -eq 0 ]]; then
      pass "SF-12 ingest word caps"
    fi
    if [[ -f "$lit/ingests/LITERATURE_INDEX.md" || -f "$lit/index/LITERATURE_INDEX.md" ]]; then
      pass "SF-13 LITERATURE_INDEX present"
    else
      warn "SF-13 LITERATURE_INDEX missing"
    fi
    pdf_count=$(find "$lit/pdfs" -name '*.pdf' 2>/dev/null | wc -l | tr -d ' ')
    check_sf11_ingest_pdf_parity "$lit"
    if [[ "$pdf_count" -ge 5 ]]; then
      if find "$lit/ingests" -name '*.md' 2>/dev/null | head -1 | grep -q .; then
        pass "monolith guard: $pdf_count PDFs with ingests present"
      else
        fail "monolith guard: $pdf_count PDFs but no ingests/ fan-out artifacts"
      fi
    fi
  elif [[ "$SELF" -eq 1 && "$TARGET" == "$ROOT" ]]; then
    warn "corpus layout not initialized (run: mkdir -p literature/{pdfs,text,ingests,metadata,index})"
  else
    fail "corpus layout missing literature/{pdfs,text,ingests,metadata}/"
  fi

  if [[ -x "$ROOT/scripts/verify_scholia.sh" ]]; then
    pass "verify script executable"
  fi

  if [[ "$TARGET" != "$ROOT" ]] && \
     [[ -f "$TARGET/literature/ingests/SYNTHESIS.md" && -f "$TARGET/references/provenance.md" ]]; then
    run_cross_stage_check
  fi
}

if [[ "$CROSS_STAGE" -eq 1 ]]; then
  run_cross_stage_check
  echo "---"
  echo "FAIL=$FAILS WARN=$WARNS"
  if [[ "$FAILS" -gt 0 ]]; then
    exit 2
  fi
  exit 0
fi

if [[ "$PRESSURE" -eq 1 && "$#" -eq 1 ]]; then
  if run_pressure_scenarios; then
    exit 0
  fi
  exit 2
fi

run_target_verify

echo "---"
echo "FAIL=$FAILS WARN=$WARNS"
if [[ "$FAILS" -gt 0 ]]; then
  exit 2
fi

if [[ "$PRESSURE" -eq 1 ]]; then
  if run_pressure_scenarios; then
    exit 0
  fi
  exit 2
fi

exit 0
