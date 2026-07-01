#!/usr/bin/env python3
"""Shared paths and ordering for deai-operator-corpus export/attach."""
from __future__ import annotations

from pathlib import Path

PROJECT = Path("/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus")
EXPORT_DIR = PROJECT / "source_exports"
ATTACH_DIR = PROJECT / "attachments"
MANIFEST = PROJECT / "manifest.yaml"
STABLE = PROJECT / "stable-context.txt"
PIR_PROJECT = Path(
    "/Users/dubs/Projects/piranesi.skill/research-projects/0630-deai-operator-corpus"
)
MAX_SLICE = 119_000

ORDER = [
    "corpus_3375627",
    "jones_2015_jslw",
    "s00146_2024_ai_writing",
    "s40979_2024_ai_writing",
    "baker_2020_prof_writing_speaking",
    "locker_2012_prof_writing_w231",
    "peeples_2003_prof_writing_rhetoric",
    "terk_prof_writing_skills",
    "henry_2000_writing_workplace",
    "olmstead_2011_elements_writing_craft",
    "long_2018_portable_mentor",
    "munier_2016_writers_guide_beginnings",
    "ginna_what_editors_do",
]
PREFIX = {slug: f"{i:02d}_{slug}" for i, slug in enumerate(ORDER, 1)}


def attach_upload_name(prefix: str) -> str:
    return f"{prefix}_ATTACH.txt"


def export_rel(prefix: str) -> str:
    return f"source_exports/{prefix}.txt"


def attach_upload_rel(prefix: str) -> str:
    return f"attachments/{attach_upload_name(prefix)}"
