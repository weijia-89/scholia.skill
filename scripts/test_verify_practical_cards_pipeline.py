#!/usr/bin/env python3
"""Unit tests for verify_pipeline.py (stdlib unittest)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

PIPE_SCRIPTS = Path(__file__).resolve().parents[1] / (
    "literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts"
)
sys.path.insert(0, str(PIPE_SCRIPTS))

import verify_pipeline as vpp  # noqa: E402


class VerifyPipelineTests(unittest.TestCase):
    def test_self_test_passes(self) -> None:
        self.assertEqual(vpp.run_self_test(), 0)

    def test_stem_from_chapter(self) -> None:
        ch = {"ingest_file": "ai_engineering_2025_ch01_ingest.md"}
        self.assertEqual(vpp.stem_from_chapter(ch), "ai_engineering_2025_ch01")

    def test_operator_table_batch_scope(self) -> None:
        rows_all = vpp.parse_operator_table_paths()
        rows_batch = vpp.parse_operator_table_paths(
            batch_id="w1_foundation_fan-out_01"
        )
        self.assertGreater(len(rows_all), len(rows_batch))
        self.assertEqual(len(rows_batch), 16)
        for batch, _chapter, _a, _p, _s in rows_batch:
            self.assertEqual(batch, "w1_foundation_fan-out_01")


if __name__ == "__main__":
    raise SystemExit(unittest.main())
