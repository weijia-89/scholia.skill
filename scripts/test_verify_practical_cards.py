#!/usr/bin/env python3
"""Unit tests for verify_practical_cards.py (stdlib unittest)."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import verify_practical_cards as vpc  # noqa: E402


class VerifyPracticalCardsTests(unittest.TestCase):
    def test_procedure_gap_empty_steps_ok(self) -> None:
        content = """topic_slug: gap
cards:
  - exercise_name: Efficacy row
    steps: []
    source_anchor: "[read:body] sec02 §Chart"
    procedure_gap: true
    quality_level: procedure_gap
"""
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
            f.write(content)
            path = Path(f.name)
        try:
            errs = vpc.validate_card_file(path, require_quality_level=True)
            self.assertEqual(errs, [], errs)
        finally:
            path.unlink()

    def test_partial_two_steps_fails(self) -> None:
        content = """topic_slug: bad
cards:
  - exercise_name: Bad
    steps:
      - one
      - two
    source_anchor: C-1
    procedure_gap: false
    quality_level: partial
"""
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
            f.write(content)
            path = Path(f.name)
        try:
            errs = vpc.validate_card_file(path, require_quality_level=True)
            self.assertTrue(any("fewer than 3 steps" in e for e in errs), errs)
        finally:
            path.unlink()

    def test_manifest_true_capitalized(self) -> None:
        self.assertEqual(vpc.run_self_test(), 0)


if __name__ == "__main__":
    raise SystemExit(unittest.main())
