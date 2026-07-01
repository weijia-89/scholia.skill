#!/usr/bin/env bash
# sync_cursor_skill_mirror.sh — copy scholia SKILL to Cursor skills dir
# Note: mirrors SKILL.md only; references/ and prompts/ stay at repo path.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CURSOR_SKILLS_DIR:-$HOME/.cursor/skills}/scholia"
mkdir -p "$DEST"
cp "$ROOT/SKILL.md" "$DEST/SKILL.md"
echo "synced: $DEST/SKILL.md"
