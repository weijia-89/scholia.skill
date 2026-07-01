#!/usr/bin/env python3
"""Generate per-chapter ChatPRD external ingest prompts for practical cards."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import CARDS_OUT, CORPUS, FANOUT_PACKET, PIPELINE, SCHEMA  # noqa: E402

CURRICULUM = PIPELINE / "card_curriculum.yaml"
CHATPRD_PROMPTS = PIPELINE / "prompts" / "chatprd"
RETURNS = PIPELINE / "chatprd_returns"


def build_prompt(ch: dict) -> str:
    stem = ch["ingest_file"].replace("_ingest.md", "")
    attach = f"attachments/{stem}_ATTACH.txt"
    save = f"chatprd_returns/{stem}_cards.yaml"
    return f"""# ChatPRD ingest — practical cards · {ch['slug']} · {ch['chapter_id']}

Platform: **Opus 4.8** · Route: {ch['route']} · hooks≈{ch['hooks']}
Project: `{PIPELINE}`

## Attach (one file only)

1. `{PIPELINE}/{attach}`

**Paste:** this prompt only. Do not upload schema or fan-out packet separately — they are referenced below and embedded in attach stable-context.

## Task

Extract **implementation cards** (`practical_usage`) from attached phase-1 ingest + text slice only.

Load-bearing rules:
- `/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md`
- `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md`

Per named exercise / worked example / explicit step list in source:
- `exercise_name` — source-native hook name
- `steps` — ≥3 ordered steps when `procedure_gap: false`; paraphrase from attach; ≤12 max
- `cognitive_frame`, `observables`, `contraindications`
- `source_anchor` — prefer C-* from ingest; else `[read:body] {ch['ingest_file']} §{{section}}`
- `context_tags` — include `cs-ai-foundation`, `practical-card`, plus wave tags
- `procedure_gap: true` + `steps: []` when efficacy cited but no protocol in corpus

**σ−:** no send-ready scripts; no invented steps; no pillar monikers as topic_slug.

## Output

Save YAML (one file per topic_slug; if multiple exercises, one file per topic with `cards:` list):

`{PIPELINE}/{save}`

```yaml
topic_slug: kebab-case-from-exercise-name
claim_ids: []
wire_status: pending
generated: YYYY-MM-DD
source_ingests:
  - ingests/{ch['ingest_file']}
cards:
  - exercise_name: ...
    steps: [...]
    cognitive_frame: ...
    observables: [...]
    contraindications: [...]
    source_anchor: ...
    consumer_wire: null
    context_tags: [cs-ai-foundation, practical-card]
    procedure_gap: false
```

If zero procedural hooks: emit one gap row or empty `cards: []` with comment in save path — do not fabricate steps.

## Next steps (operator)

1. Copy or merge saved YAML into `{CARDS_OUT}/{{topic_slug}}.yaml` (dedupe by exercise_name + source_anchor).
2. Run verify:
   `bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh {CORPUS}`
3. After all waves PASS → `kickoff wire` for local-rag consumer.

**Iron law:** ChatPRD extracts only — Cursor merges + verify; no RAG re-extract.
"""


def main() -> int:
    if not CURRICULUM.is_file():
        print(f"Missing {CURRICULUM}", file=sys.stderr)
        return 2
    CHATPRD_PROMPTS.mkdir(parents=True, exist_ok=True)
    RETURNS.mkdir(parents=True, exist_ok=True)
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    count = 0
    for wave_def in (data.get("waves") or {}).values():
        for batch in wave_def.get("batches") or []:
            for ch in batch.get("chapters") or []:
                if ch.get("route") == "skip":
                    continue
                name = ch["ingest_file"].replace("_ingest.md", "_card_ingest.md")
                path = CHATPRD_PROMPTS / name
                path.write_text(build_prompt(ch), encoding="utf-8")
                count += 1
                print(f"CHATPRD_PROMPT {name}")
    print(f"Wrote {count} ChatPRD prompts -> {CHATPRD_PROMPTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
