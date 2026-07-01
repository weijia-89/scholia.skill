#!/usr/bin/env python3
"""Export inbox PDFs to source_exports/; build ChatPRD upload files in attachments/."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from build_attach_uploads import main as build_uploads  # noqa: E402
from corpus_paths import (  # noqa: E402
    ATTACH_DIR,
    EXPORT_DIR,
    MANIFEST,
    PIR_PROJECT,
    PREFIX,
    PROJECT,
    export_rel,
)


def export_pdfs() -> bool:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    entries = data.get("entries", [])
    changed = False
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        slug = entry["slug"]
        prefix = PREFIX.get(slug)
        if not prefix:
            continue
        export_path = EXPORT_DIR / f"{prefix}.txt"
        inbox = Path(entry["inbox_file"])
        entry["text_path"] = export_rel(prefix)

        if not inbox.is_file():
            print(f"SKIP missing: {inbox.name}")
            continue
        if export_path.is_file() and export_path.stat().st_size > 100:
            print(f"OK exists: {slug}")
            continue
        if inbox.suffix.lower() != ".pdf":
            continue

        subprocess.run(
            ["pdftotext", "-layout", str(inbox), str(export_path)],
            check=True,
        )
        entry["text_status"] = "ready"
        changed = True
        print(f"EXPORTED: {slug}")

    if changed:
        MANIFEST.write_text(
            yaml.dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )
    return True


def sync_piranesi() -> None:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    entries = data.get("entries", [])
    pir_manifest = PIR_PROJECT / "manifest.yaml"
    if pir_manifest.is_file():
        pir_data = yaml.safe_load(pir_manifest.read_text(encoding="utf-8")) or {}
        for e, src in zip(pir_data.get("entries", []), entries):
            e["text_status"] = src.get("text_status")
            e["text_path"] = src.get("text_path")
            if src.get("attach_upload"):
                e["attach_upload"] = src["attach_upload"]
            for old in ("attach_slice", "attach_primary", "attach_pack"):
                e.pop(old, None)
            e["ingest_path"] = f"chatprd_returns/{e['slug']}_ingest.md"
            e["notes"] = src.get("notes", "")
        pir_manifest.write_text(
            yaml.dump(pir_data, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )

    pir_attach = PIR_PROJECT / "attachments"
    pir_attach.mkdir(parents=True, exist_ok=True)
    for path in pir_attach.iterdir():
        if path.is_file():
            path.unlink()
    for path in ATTACH_DIR.iterdir():
        if path.is_file() and path.name.endswith("_ATTACH.txt"):
            shutil.copy2(path, pir_attach / path.name)


def migrate_legacy_layout() -> None:
    """Move full exports out of attachments/; drop slices and old packs."""
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    ATTACH_DIR.mkdir(parents=True, exist_ok=True)
    for path in list(ATTACH_DIR.glob("*.txt")):
        name = path.name
        if name.endswith("_ATTACH.txt"):
            continue
        if name.endswith("_slice.txt"):
            path.unlink()
            continue
        dest = EXPORT_DIR / name
        if not dest.is_file():
            shutil.move(str(path), dest)
            print(f"MIGRATE {name} -> source_exports/")
        else:
            path.unlink()
    pack_dir = PROJECT / "attach_packs"
    if pack_dir.is_dir():
        for path in pack_dir.iterdir():
            if path.is_file():
                path.unlink()
        pack_dir.rmdir()
        print("REMOVED attach_packs/")


def main() -> None:
    migrate_legacy_layout()
    export_pdfs()
    subprocess.run([sys.executable, str(SCRIPT_DIR / "export_epubs.py")], check=False)
    subprocess.run([sys.executable, str(SCRIPT_DIR / "split_chapters.py")], check=True)
    subprocess.run([sys.executable, str(SCRIPT_DIR / "generate_chapter_prompts.py")], check=True)
    build_uploads()
    sync_piranesi()


if __name__ == "__main__":
    main()
