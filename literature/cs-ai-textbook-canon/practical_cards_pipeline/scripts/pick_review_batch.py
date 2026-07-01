#!/usr/bin/env python3
"""Pick curriculum batch_id for review-loop iteration (rotate unexplored batches)."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import PIPELINE  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"


def fan_out_batch_ids() -> list[str]:
    if not CURRICULUM.is_file():
        return []
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    ids: list[str] = []
    seen: set[str] = set()
    for wave_def in (data.get("waves") or {}).values():
        for batch in wave_def.get("batches") or []:
            bid = batch.get("batch_id", "")
            if not bid or bid in seen:
                continue
            chapters = batch.get("chapters") or []
            if any(ch.get("route") == "fan-out" for ch in chapters):
                ids.append(bid)
                seen.add(bid)
    return ids


def main(argv: list[str]) -> int:
    iter_n = int(argv[1]) if len(argv) > 1 else 1
    ids = fan_out_batch_ids()
    if not ids:
        print("w1_foundation_fan-out_01", end="")
        return 0
    idx = (max(1, iter_n) - 1) % len(ids)
    print(ids[idx], end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
