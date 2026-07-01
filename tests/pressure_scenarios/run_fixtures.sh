#!/usr/bin/env bash
# run_fixtures.sh — verify frozen on-disk fixtures (R-13); inline harness remains SSOT
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VERIFY="$ROOT/scripts/verify_scholia.sh"
FIX="$ROOT/tests/pressure_scenarios/fixtures"
pass=0
fail=0

run_one() {
  local id="$1" path="$2" expect="$3"
  set +e
  bash "$VERIFY" "$path" >/dev/null 2>&1
  local rc=$?
  set -e
  if [[ "$rc" -eq "$expect" ]]; then
    echo "PASS $id (exit $rc)"
    pass=$((pass + 1))
  else
    echo "FAIL $id (expected $expect, got $rc)"
    fail=$((fail + 1))
  fi
}

[[ -d "$FIX/ps02.child.skill" ]] || bash "$ROOT/tests/pressure_scenarios/materialize_fixtures.sh"

run_one PS-02 "$FIX/ps02.child.skill" 0
run_one PS-03 "$FIX/ps03.child.skill" 2
run_one PS-04 "$FIX/ps04.child.skill" 2
run_one PS-07 "$FIX/ps07.child.skill" 2
run_one PS-08 "$FIX/ps08.child.skill" 2
run_one PS-09 "$FIX/ps09.child.skill" 2
run_one PS-11 "$FIX/ps11.flat.child.skill" 0
run_one PS-12 "$FIX/ps12.cdg004.child.skill" 0
run_one PS-12-empty "$FIX/ps12bad.cdg004.child.skill" 2

echo "---"
echo "fixtures: PASS=$pass FAIL=$fail"
[[ "$fail" -eq 0 ]]
