#!/usr/bin/env bash
# materialize_pressure_fixtures.sh — write frozen PS fixtures to disk (wave 5 / R-13)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FIX="$ROOT/tests/pressure_scenarios/fixtures"
PROV="$ROOT/references/provenance-template.md"

write_ps02() {
  local d="$FIX/ps02.child.skill"
  rm -rf "$d"
  mkdir -p "$d/literature"/{pdfs,text,ingests,metadata,index} "$d/references"
  cp "$PROV" "$d/references/"
  local j
  for j in 1 2 3 4 5; do touch "$d/literature/pdfs/paper_${j}.pdf"; done
  for j in 1 2 3 4; do echo "# ingest $j" >"$d/literature/ingests/paper_${j}.md"; done
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps02.child
description: SF-11 partial ingest fixture (5 PDFs, 4 ingests)
---
# fixture
EOF
}

write_ps03() {
  local d="$FIX/ps03.child.skill"
  rm -rf "$d"
  mkdir -p "$d/literature"/{pdfs,text,ingests,metadata,index} "$d/references"
  cp "$PROV" "$d/references/"
  python3 -c "print('word ' * 5001)" >"$d/literature/ingests/overlimit.md"
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps03.child
description: SF-12 overlimit fixture
---
# fixture
EOF
}

write_ps04() {
  local d="$FIX/ps04.child.skill"
  rm -rf "$d"
  mkdir -p "$d/references"
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps04.child
description: SF-06 path-only provenance fixture
---
# fixture
EOF
  cat >"$d/references/provenance.md" <<'EOF'
| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| C-001 | test claim | inferred | Paper | literature/ingests/foo.md | literature/ingests/foo.md | §1 |
EOF
}

write_ps07() {
  local d="$FIX/ps07.child.skill"
  rm -rf "$d"
  mkdir -p "$d/references"
  cp "$PROV" "$d/references/"
  cat >"$d/SKILL.md" <<'EOF'
---
description: missing name field
---
# fixture
EOF
}

write_ps08() {
  local d="$FIX/ps08.child.skill"
  rm -rf "$d"
  mkdir -p "$d/references"
  cp "$PROV" "$d/references/"
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps08.child
description: SF-05 absolute path fixture
---
See /Users/operator/secret/path
EOF
}

write_ps09() {
  local d="$FIX/ps09.child.skill"
  rm -rf "$d"
  mkdir -p "$d/literature"/{pdfs,text,ingests,metadata,index} "$d/references"
  cp "$PROV" "$d/references/"
  local j
  for j in 1 2 3 4 5; do touch "$d/literature/pdfs/paper_${j}.pdf"; done
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps09.child
description: monolith guard fixture
---
# fixture
EOF
}

write_ps11() {
  local d="$FIX/ps11.flat.child.skill"
  rm -rf "$d"
  mkdir -p "$d/literature"/{pdfs,text,metadata} "$d/references"
  cp "$PROV" "$d/references/"
  echo 'layout_mode: flat' >"$d/literature/metadata/corpus_manifest.yaml"
  touch "$d/literature/pdfs/howto.pdf"
  mkdir -p "$d/literature/text/howto"
  echo "steps" >"$d/literature/text/howto/howto.md"
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps11.flat.child
description: layout_mode flat fixture
---
# fixture
EOF
}

write_ps12() {
  local d="$FIX/ps12.cdg004.child.skill"
  rm -rf "$d"
  mkdir -p "$d/literature"/{pdfs,text,ingests,metadata,index} "$d/references"
  cat >"$d/references/provenance.md" <<'EOF'
| claim-id | claim | relation | source-title | DOI/URL/ISBN | ingest-path | section-anchor |
|----------|-------|----------|--------------|--------------|-------------|----------------|
| C-001 | test | quoted | Paper | 10.1234/ps12 | literature/ingests/foo.md | §1 |
EOF
  echo "# synthesis content" >"$d/literature/ingests/SYNTHESIS.md"
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps12.cdg004.child
description: C-DG004 cross-stage fixture
---
# fixture
EOF
}

write_ps12bad() {
  write_ps12
  local d="$FIX/ps12bad.cdg004.child.skill"
  cp -R "$FIX/ps12.cdg004.child.skill" "$d"
  : >"$d/literature/ingests/SYNTHESIS.md"
  cat >"$d/SKILL.md" <<'EOF'
---
name: ps12bad.cdg004.child
description: C-DG004 empty synthesis fixture
---
# fixture
EOF
}

write_ps02
write_ps03
write_ps04
write_ps07
write_ps08
write_ps09
write_ps11
write_ps12
write_ps12bad
echo "materialized fixtures under $FIX"
