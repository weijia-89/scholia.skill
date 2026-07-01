#!/usr/bin/env bash
# Bounded review-loop guard — min passes, max attempts, wall clock, stuck signature.
# Source from gate scripts; do not run directly.
#
# review_loop_guard_run MIN_PASS_ITERS MAX_ATTEMPTS MAX_SECS STUCK_LIMIT "label" -- command...
# Exports REVIEW_LOOP_ITER (phase, 1-indexed) before each command invocation.
# Success deepens phase; failure retries same phase. Exit 0 only after MIN_PASS_ITERS successes.

review_loop_guard_run() {
  local min_pass="${1:?min_pass_iters}"
  local max_attempts="${2:?max_attempts}"
  local max_secs="${3:?max_secs}"
  local stuck_limit="${4:?stuck_limit}"
  local label="${5:?label}"
  shift 5

  if [[ "${1:-}" != "--" ]]; then
    echo "FAIL: review_loop_guard_run requires -- before command list" >&2
    return 2
  fi
  shift

  local start_ts phase attempt pass_count prev_sig stuck log
  start_ts=$(date +%s)
  phase=1
  attempt=1
  pass_count=0
  prev_sig=""
  stuck=0

  while [[ "$attempt" -le "$max_attempts" ]]; do
    local now elapsed
    now=$(date +%s)
    elapsed=$((now - start_ts))
    if [[ "$elapsed" -gt "$max_secs" ]]; then
      echo "FAIL: ${label} wall-clock budget ${max_secs}s exceeded at attempt ${attempt}"
      return 2
    fi

    export REVIEW_LOOP_ITER="$phase"
    export REVIEW_LOOP_MIN_PASS="$min_pass"
    export REVIEW_LOOP_PASS_COUNT="$pass_count"
    echo "=== ${label} phase ${phase} attempt ${attempt}/${max_attempts} (passes ${pass_count}/${min_pass}, elapsed ${elapsed}s) ==="

    log=$(mktemp "${TMPDIR:-/tmp}/review_loop.XXXXXX")
    if "$@" >"$log" 2>&1; then
      cat "$log"
      rm -f "$log"
      pass_count=$((pass_count + 1))
      if [[ "$pass_count" -ge "$min_pass" ]]; then
        echo "PASS: ${label} ${pass_count} phase(s) cleared (min_pass=${min_pass})"
        return 0
      fi
      echo "PASS: ${label} phase ${phase} — deepening (${pass_count}/${min_pass}, not satisfied yet)"
      phase=$((phase + 1))
      attempt=$((attempt + 1))
      stuck=0
      prev_sig=""
      sleep 1
      continue
    fi

    cat "$log"
    local sig
    sig=$(shasum -a 256 "$log" | awk '{print $1}')
    if [[ -n "$prev_sig" && "$sig" == "$prev_sig" ]]; then
      stuck=$((stuck + 1))
      echo "WARN: ${label} identical failure signature (${stuck}/${stuck_limit}) on phase ${phase}"
      if [[ "$stuck" -ge "$stuck_limit" ]]; then
        rm -f "$log"
        echo "FAIL: ${label} stuck-loop guard — same failure ${stuck_limit}x on phase ${phase}"
        return 2
      fi
    else
      stuck=0
    fi
    prev_sig="$sig"
    rm -f "$log"
    attempt=$((attempt + 1))
    sleep 1
  done

  echo "FAIL: ${label} exhausted ${max_attempts} attempts with ${pass_count}/${min_pass} passes"
  return 2
}
