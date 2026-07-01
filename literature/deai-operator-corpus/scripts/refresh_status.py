#!/usr/bin/env python3
"""Write STATUS.md for deai-operator-corpus ChatPRD delegation."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import yaml

PROJECT = Path("/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus")
MANIFEST = PROJECT / "manifest.yaml"
STATUS = PROJECT / "STATUS.md"
RETURNS = PROJECT / "chatprd_returns"

STATUS_ICONS = {
    "none": "⬜ pending",
    "done": "✅ done",
}


def main() -> None:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    entries = data.get("entries", [])
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    done = sum(1 for e in entries if e.get("ingest_status") == "done")
    pending = len(entries) - done

    next_entry = None
    for e in entries:
        if e.get("ingest_status") != "done" and e.get("text_status") == "ready":
            next_entry = e
            break

    lines = [
        "# STATUS — deai operator corpus (ChatPRD delegation)",
        "",
        f"**Updated:** {now} · **Sources:** {len(entries)} · **Done:** {done} · **Pending:** {pending}",
        "",
        f"**Manifest:** `{MANIFEST}`",
        f"**Upload folder:** `{PROJECT}/attachments/` (one `_ATTACH.txt` per source)",
        f"**Full exports:** `{PROJECT}/source_exports/` (not uploaded)",
        f"**ChatPRD returns:** `{RETURNS}/`",
        f"**Granola returns:** `{PROJECT}/granola_returns/`",
        "",
        "## Pipeline",
        "",
        "| Step | Command |",
        "| ---- | ------- |",
        f"| Export + rebuild uploads | `bash {PROJECT}/scripts/export_text.sh` |",
        f"| ChatPRD ingest | Opus 4.6 · attach one `attachments/NN_slug_ATTACH.txt` + paste prompt |",
        f"| Save return | `chatprd_returns/{{slug}}_YYYYMMDD_ingest.md` |",
        "",
        "## Source tracker",
        "",
        "| Status | Text | Slug | Lane | Upload file |",
        "| ------ | ---- | ---- | ---- | ----------- |",
    ]
    for e in entries:
        slug = e["slug"]
        prefix = Path(e["text_path"]).stem
        icon = STATUS_ICONS.get(e.get("ingest_status", "none"), "⬜ pending")
        text_ok = "✓" if e.get("text_status") == "ready" else "—"
        lane = e.get("lane_hint", "both")
        upload = f"`attachments/{prefix}_ATTACH.txt`"
        lines.append(f"| {icon} | {text_ok} | `{slug}` | {lane} | {upload} |")

    lines.extend(["", "## Next action", ""])
    if next_entry:
        prefix = Path(next_entry["text_path"]).stem
        lines.append(
            f"1. ChatPRD (Opus 4.6): attach `{PROJECT}/attachments/{prefix}_ATTACH.txt`"
        )
        lines.append(
            f"2. Paste `{PROJECT}/prompts/{prefix}_ingest.md`"
        )
        lines.append(f"3. Save to `{RETURNS}/{next_entry['slug']}_YYYYMMDD_ingest.md`")
    else:
        lines.append("All sources with text exported are done — run Granola S4 or trigger Cursor skill patches.")

    lines.append("")
    STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {STATUS}")


if __name__ == "__main__":
    main()
