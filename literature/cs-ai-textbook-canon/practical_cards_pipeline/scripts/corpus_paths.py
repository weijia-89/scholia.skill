#!/usr/bin/env python3
"""Shared paths for cs-ai practical_cards_pipeline."""
from __future__ import annotations

from pathlib import Path

CORPUS = Path("/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon")
PIPELINE = CORPUS / "practical_cards_pipeline"
INGESTS = CORPUS / "ingests"
TEXT = CORPUS / "text"
CARDS_OUT = CORPUS / "metadata" / "practical_cards"
MANIFEST = CORPUS / "metadata" / "corpus_manifest.yaml"
PIR_PROJECT = Path(
    "/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/phase2-cs-ai"
)
SCHEMA = Path("/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md")
FANOUT_PACKET = Path(
    "/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md"
)
CANON = Path(
    "/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/returns/scholia_practical_ingest_decision_canon_20260626.md"
)
MAX_BATCH = 16
