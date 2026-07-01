#!/usr/bin/env bash
# Deprecated entrypoint — use verify_scholia.sh --pressure
exec bash "$(cd "$(dirname "$0")/../.." && pwd)/scripts/verify_scholia.sh" --pressure
