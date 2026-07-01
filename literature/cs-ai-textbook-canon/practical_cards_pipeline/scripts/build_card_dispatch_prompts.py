#!/usr/bin/env python3
"""Generate per-chapter Cursor subagent dispatch prompts from card_curriculum.yaml."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import CARDS_OUT, CORPUS, FANOUT_PACKET, PIPELINE, SCHEMA  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"
DISPATCH = PIPELINE / "prompts" / "dispatch"


def build_prompt(ch: dict) -> str:
    ingest_rel = f"ingests/{ch['ingest_file']}"
    attach = (
        PIPELINE / "attachments" / ch["ingest_file"].replace("_ingest.md", "_SLICE.txt")
    )
    return f"""# SUB-AGENT: practical_usage card extract · {ch['slug']} · {ch['chapter_id']}

**Route:** {ch['route']} · hooks≈{ch['hooks']}

Read only:
- {SCHEMA}
- {FANOUT_PACKET}
- {CORPUS}/{ingest_rel}
- Text slice: {attach if attach.is_file() else ch.get('text_path', 'see ingest coverage_attestation')}

Write / merge:
- {CARDS_OUT}/{{topic_slug}}.yaml

Rules (from fan-out packet):
1. ≥3 steps when procedure_gap: false; ≤12 max; no invented steps.
2. source_anchor: prefer C-*; else "[read:body] {ch['ingest_file']} §{{section}}".
3. Efficacy-only → procedure_gap: true; steps: []; quality_level: procedure_gap.
4. context_tags: cs-ai-foundation, practical-card (+ session tags from wave).
5. topic_slug: kebab-case from exercise_name — not pillar monikers.
6. Merge/dedupe by exercise_name + source_anchor.

Forbidden: send-ready scripts; monolith-read; steps not in ingest/slice.
"""


def main() -> int:
    if not CURRICULUM.is_file():
        print(f"Missing {CURRICULUM} — run plan_card_waves.py first", file=sys.stderr)
        return 2
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    DISPATCH.mkdir(parents=True, exist_ok=True)
    count = 0
    for wave_def in (data.get("waves") or {}).values():
        for batch in wave_def.get("batches") or []:
            for ch in batch.get("chapters") or []:
                if ch.get("route") == "skip":
                    continue
                name = ch["ingest_file"].replace("_ingest.md", "_card_extract.md")
                path = DISPATCH / name
                path.write_text(build_prompt(ch), encoding="utf-8")
                count += 1
                print(f"DISPATCH {name}")
    print(f"Wrote {count} dispatch prompts -> {DISPATCH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
