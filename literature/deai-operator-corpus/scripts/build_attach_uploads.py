#!/usr/bin/env python3
"""Build ChatPRD upload files: full attach for papers; per-chapter for textbooks."""
from __future__ import annotations

from datetime import date

import yaml

from corpus_paths import (
    ATTACH_DIR,
    EXPORT_DIR,
    MANIFEST,
    MAX_SLICE,
    PREFIX,
    PROJECT,
    STABLE,
    attach_upload_name,
    attach_upload_rel,
    export_rel,
)

CURRICULUM = PROJECT / "chapter_curriculum.yaml"
CHAPTER_DIR = EXPORT_DIR / "chapters"


def primary_body(export_path) -> tuple[str, bool, int]:
    raw = export_path.read_text(encoding="utf-8", errors="replace")
    full_len = len(raw)
    if full_len > MAX_SLICE:
        return raw[:MAX_SLICE], True, full_len
    return raw, False, full_len


def chapter_attach_name(prefix: str, chapter_id: str) -> str:
    return f"{prefix}_{chapter_id}_ATTACH.txt"


def chapter_attach_rel(prefix: str, chapter_id: str) -> str:
    return f"attachments/{chapter_attach_name(prefix, chapter_id)}"


def write_attach(
    attach_name: str,
    entry: dict,
    body_label: str,
    body: str,
    prompt_hint: str,
    truncate_note: str = "",
) -> None:
    stable = STABLE.read_text(encoding="utf-8").strip() if STABLE.is_file() else ""
    content = (
        f"{attach_name} — ChatPRD upload (attach this file only)\n"
        f"Generated: {date.today().isoformat()}\n"
        f"Slug: {entry['slug']}\n"
        f"Project: {PROJECT}\n"
        f"ChatPRD maximum: 8 uploaded files per window — this file is self-contained.\n"
        f"Also paste: {prompt_hint}\n\n"
        f"{'=' * 72}\nSTABLE-CONTEXT\n{'=' * 72}\n\n{stable}\n\n"
        f"{'=' * 72}\nPRIMARY-TEXT ({body_label}){truncate_note}"
        f"{'=' * 72}\n\n{body}"
    )
    ATTACH_DIR.mkdir(parents=True, exist_ok=True)
    (ATTACH_DIR / attach_name).write_text(content, encoding="utf-8")


def build_monolith(entry: dict, prefix: str) -> bool:
    export_path = EXPORT_DIR / f"{prefix}.txt"
    if not export_path.is_file() or export_path.stat().st_size < 100:
        return False

    body, truncated, full_len = primary_body(export_path)
    attach_name = attach_upload_name(prefix)
    truncate_note = ""
    if truncated:
        truncate_note = (
            f"\nNOTE: Embedded primary truncated to {MAX_SLICE:,} chars "
            f"(full export {full_len:,} chars at {export_rel(prefix)}).\n"
        )

    write_attach(
        attach_name,
        entry,
        export_rel(prefix),
        body,
        f"prompts/{prefix}_ingest.md",
        truncate_note,
    )

    entry["text_path"] = export_rel(prefix)
    entry["attach_upload"] = attach_upload_rel(prefix)
    entry["text_status"] = "ready"
    entry.pop("attach_slice", None)
    entry.pop("attach_primary", None)
    entry.pop("attach_pack", None)
    if truncated:
        entry["notes"] = (
            f"ChatPRD attach uses first {MAX_SLICE:,} chars; full at {export_rel(prefix)}."
        )
    elif entry.get("notes", "").startswith("ChatPRD attach"):
        entry["notes"] = ""
    return True


def build_chapter_attaches(entry: dict, book: dict, prefix: str) -> int:
    built = 0
    chapter_uploads: list[str] = []
    for ch in book.get("chapters", []):
        cid = ch["chapter_id"]
        chapter_path = CHAPTER_DIR / f"{prefix}_{cid}.txt"
        if not chapter_path.is_file():
            print(f"SKIP missing chapter slice: {chapter_path.name}")
            continue

        body = chapter_path.read_text(encoding="utf-8", errors="replace")
        attach_name = chapter_attach_name(prefix, cid)
        rel_ch = f"source_exports/chapters/{prefix}_{cid}.txt"
        truncate_note = ""
        if len(body) > MAX_SLICE:
            body = body[:MAX_SLICE]
            truncate_note = (
                f"\nNOTE: Chapter slice truncated to {MAX_SLICE:,} chars "
                f"(full chapter at {rel_ch}).\n"
            )

        write_attach(
            attach_name,
            entry,
            rel_ch,
            body,
            f"prompts/{prefix}_{cid}_ingest.md",
            truncate_note,
        )
        chapter_uploads.append(chapter_attach_rel(prefix, cid))
        built += 1
        print(f"ATTACH {attach_name} ({len(body):,} chars)")

    if built:
        entry["text_path"] = export_rel(prefix)
        entry["attach_upload"] = chapter_uploads[0]
        entry["chapter_attaches"] = chapter_uploads
        entry["text_status"] = "ready"
        entry["notes"] = (
            f"Chapter fan-out: {built} attaches in attachments/; "
            f"full export at {export_rel(prefix)}."
        )
    return built


def clean_attach_dir(papers_no_fanout: list[str], book_prefixes: list[str]) -> None:
    """Remove stale monolith book attaches and non-_ATTACH cruft."""
    ATTACH_DIR.mkdir(parents=True, exist_ok=True)
    keep_monolith = {attach_upload_name(p) for p in papers_no_fanout}
    for path in ATTACH_DIR.iterdir():
        if not path.is_file():
            continue
        if not path.name.endswith("_ATTACH.txt"):
            path.unlink()
            continue
        # Drop old monolith textbook attaches superseded by chapter fan-out
        for bp in book_prefixes:
            if path.name == attach_upload_name(bp):
                path.unlink()
                print(f"REMOVE stale monolith {path.name}")
                break


def main() -> None:
    curriculum = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    papers_no_fanout = curriculum.get("papers_no_fanout", [])
    books_by_slug = {b["slug"]: b for b in curriculum.get("books", [])}
    book_prefixes = [b["prefix"] for b in curriculum.get("books", [])]

    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    entries = data.get("entries", [])
    clean_attach_dir(papers_no_fanout, book_prefixes)

    built = 0
    for entry in entries:
        slug = entry["slug"]
        prefix = PREFIX.get(slug)
        if not prefix:
            print(f"SKIP unknown slug: {slug}")
            continue

        if prefix in papers_no_fanout:
            if build_monolith(entry, prefix):
                built += 1
                print(f"ATTACH {attach_upload_name(prefix)}")
            else:
                print(f"SKIP no export: {slug}")
            continue

        book = books_by_slug.get(slug)
        if book and entry.get("chapter_fanout"):
            n = build_chapter_attaches(entry, book, prefix)
            built += n
            if n == 0:
                print(f"WARN chapter fan-out failed for {slug}; falling back to monolith")
                if build_monolith(entry, prefix):
                    built += 1
            continue

        if build_monolith(entry, prefix):
            built += 1
            print(f"ATTACH {attach_upload_name(prefix)}")

    MANIFEST.write_text(yaml.dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Built {built} upload files in {ATTACH_DIR}")


if __name__ == "__main__":
    main()
