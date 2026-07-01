#!/usr/bin/env python3
"""Slugs with saved chatprd_returns ingests — do not overwrite prompts via regen."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

from corpus_paths import PROJECT  # noqa: E402

RETURNS = PROJECT / "chatprd_returns"
PROMPTS = PROJECT / "prompts"
CURRICULUM = PROJECT / "chapter_curriculum.yaml"
MANIFEST = PROJECT / "manifest.yaml"

_SKIP_NAME = ("refined", "batch", "four_source", "composer_ready")


def discover_completed_slugs() -> set[str]:
    slugs: set[str] = set()
    for path in RETURNS.glob("*_*_ingest.md"):
        if any(s in path.name for s in _SKIP_NAME):
            continue
        m = re.match(r"^(.+)_(\d{8})_ingest\.md$", path.name)
        if m:
            slugs.add(m.group(1))
    # Monolith returns without dated pattern
    for extra in ("05_baker_refined_ingest",):
        if (RETURNS / f"{extra}.md").is_file():
            slugs.add("baker_2020_prof_writing_speaking")
    return slugs


def _chapter_index() -> dict[str, Path]:
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    out: dict[str, Path] = {}
    for book in data.get("books", []):
        prefix = book["prefix"]
        slug = book["slug"]
        for ch in book.get("chapters", []):
            cid = ch["chapter_id"]
            save_slug = f"{slug}_{cid}"
            out[save_slug] = PROMPTS / f"{prefix}_{cid}_ingest.md"
    return out


def _manifest_index() -> dict[str, Path]:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    out: dict[str, Path] = {}
    for entry in data.get("entries", []):
        prefix = Path(entry["text_path"]).stem
        out[entry["slug"]] = PROMPTS / f"{prefix}_ingest.md"
    return out


def prompt_path_for_slug(slug: str) -> Path | None:
    chapters = _chapter_index()
    if slug in chapters:
        return chapters[slug]
    manifest = _manifest_index()
    if slug in manifest:
        return manifest[slug]
    return None


def frozen_prompt_paths() -> set[Path]:
    paths: set[Path] = set()
    for slug in discover_completed_slugs():
        p = prompt_path_for_slug(slug)
        if p:
            paths.add(p.resolve())
    return paths


def is_frozen(path: Path) -> bool:
    return path.resolve() in frozen_prompt_paths()
