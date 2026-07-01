#!/usr/bin/env python3
"""Plan phase-2 practical card waves from existing chapter ingests."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import (  # noqa: E402
    CORPUS,
    INGESTS,
    MANIFEST,
    MAX_BATCH,
    PIPELINE,
    PIR_PROJECT,
    TEXT,
)

SKIP_NAME = re.compile(
    r"(index|bibliography|front.?matter|preface|toc|looking ahead|epilogue|appendix)",
    re.I,
)


def count_hooks(text: str) -> tuple[int, str]:
    m = re.search(r"### exercise_hooks\s*\n(.*?)(?=\n## |\n### [^e]|\Z)", text, re.S)
    if not m:
        return 0, "none"
    block = m.group(1)
    numbered = len(re.findall(r"^\d+\.\s", block, re.M))
    table_rows = max(0, len(re.findall(r"^\|[^|\n]+\|[^|\n]+\|", block, re.M)) - 1)
    bullets = [
        b
        for b in re.findall(r"^-\s+(.+)$", block, re.M)
        if "No formal" not in b and "No end-of-chapter" not in b
    ]
    inferred = sum(
        1
        for b in bullets
        if "[inferred]" in b.lower() or "Operator drill" in b or "Instructor hooks" in b
    )
    source_bullets = len(bullets) - inferred
    if (
        "classroom assignment" in block.lower() or "Extensive **classroom" in block
    ) and numbered == 0 and table_rows == 0:
        return 4, "classroom-prose-est≥4"
    count = numbered + table_rows + source_bullets
    return count, f"n={numbered} t={table_rows} b={source_bullets}"


def slug_from_ingest(name: str) -> str:
    stem = name.replace("_ingest.md", "")
    for sep in ("_ch", "_sec"):
        if sep in stem:
            return stem.rsplit(sep, 1)[0]
    return stem


def load_wave_map() -> dict[str, str]:
    if not MANIFEST.is_file():
        return {}
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    out: dict[str, str] = {}
    for wave_key, wave_def in (data.get("waves") or {}).items():
        if isinstance(wave_def, dict):
            for s in wave_def.get("slugs") or []:
                out[s] = wave_key
    for entry in data.get("entries") or []:
        slug = entry.get("slug")
        wave = entry.get("wave")
        if slug and wave:
            out[slug] = wave
    return out


def parse_line_range(text: str) -> tuple[int, int] | None:
    for pat in (
        r"lines_read\s*\|\s*(\d+)\s*[–-]\s*(\d+)",
        r"text_lines_read\s*\|\s*(\d+)\s*[–-]\s*(\d+)",
        r"\*\*lines_read\*\*\s*\|\s*(\d+)\s*[–-]\s*(\d+)",
    ):
        m = re.search(pat, text)
        if m:
            return int(m.group(1)), int(m.group(2))
    return None


def chapter_entries() -> list[dict]:
    wave_map = load_wave_map()
    entries: list[dict] = []
    for path in sorted(INGESTS.glob("*_ingest.md")):
        name = path.name
        if SKIP_NAME.search(name):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        hooks, method = count_hooks(text)
        slug = slug_from_ingest(name)
        ch_m = re.search(r"_(ch|sec)(\d+)_", name)
        ch_id = ch_m.group(2) if ch_m else "?"
        route = "skip" if hooks == 0 else ("inline" if hooks <= 3 else "fan-out")
        line_range = parse_line_range(text)
        entries.append(
            {
                "ingest_file": name,
                "ingest_path": str(path),
                "slug": slug,
                "chapter_id": ch_id,
                "wave": wave_map.get(slug, "unknown"),
                "hooks": hooks,
                "hook_method": method,
                "route": route,
                "text_slice": list(line_range) if line_range else None,
                "text_path": str(TEXT / f"{slug}.txt") if (TEXT / f"{slug}.txt").is_file() else None,
            }
        )
    return entries


def batch_chapters(chapters: list[dict], prefix: str) -> list[dict]:
    batches: list[dict] = []
    fan = [c for c in chapters if c["route"] == "fan-out"]
    inline = [c for c in chapters if c["route"] == "inline"]
    idx = 1
    for group_name, group in (("fan-out", fan), ("inline", inline)):
        for i in range(0, len(group), MAX_BATCH):
            chunk = group[i : i + MAX_BATCH]
            if not chunk:
                continue
            batches.append(
                {
                    "batch_id": f"{prefix}_{group_name}_{idx:02d}",
                    "route": group_name,
                    "chapters": chunk,
                }
            )
            idx += 1
    return batches


def build_curriculum(entries: list[dict]) -> dict:
    by_wave: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_wave[e["wave"]].append(e)
    waves_out: dict = {}
    wave_order = sorted(by_wave.keys())
    for wave in wave_order:
        chs = by_wave[wave]
        waves_out[wave] = {
            "summary": {
                "total": len(chs),
                "fan_out": sum(1 for c in chs if c["route"] == "fan-out"),
                "inline": sum(1 for c in chs if c["route"] == "inline"),
                "skip": sum(1 for c in chs if c["route"] == "skip"),
            },
            "batches": batch_chapters(chs, wave),
        }
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "corpus": str(CORPUS),
        "schema": str(Path("/Users/dubs/Projects/scholia.skill/references/practical-usage-schema.md")),
        "waves": waves_out,
    }


def write_status(curriculum: dict) -> None:
    total = fan = inline = skip = 0
    batch_count = 0
    for wave_def in curriculum["waves"].values():
        s = wave_def["summary"]
        total += s["total"]
        fan += s["fan_out"]
        inline += s["inline"]
        skip += s["skip"]
        batch_count += len(wave_def["batches"])

    status = f"""# STATUS — cs-ai practical cards phase 2

**Updated:** {curriculum['generated_at'][:19]} UTC
**Corpus:** `{CORPUS}`
**Pipeline:** `{PIPELINE}`

| Metric | Count |
|--------|-------|
| Chapter ingests | {total} |
| Fan-out (>3 hooks) | {fan} |
| Inline (≤3 hooks) | {inline} |
| Skip (0 hooks) | {skip} |
| Dispatch batches (≤{MAX_BATCH}) | {batch_count} |
| Pilot cards on disk | see `{CORPUS}/metadata/practical_cards/` |

## Commands

| Step | Command |
|------|---------|
| Regenerate curriculum | `python3 {PIPELINE}/scripts/plan_card_waves.py` |
| Build dispatch prompts | `python3 {PIPELINE}/scripts/build_card_dispatch_prompts.py` |
| Build attach slices | `python3 {PIPELINE}/scripts/build_attach_slices.py` |
| Verify preflight | `bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh --self-test` |
| Review loop | `bash {PIPELINE}/scripts/run_practical_cards_review_loop.sh` |
| Orchestrator | paste `{PIPELINE}/prompts/ORCHESTRATOR_cs_ai_practical_cards.md` |

## Operator gates

| Phrase | Action |
| **`kickoff phase 2`** | Run next pending wave batch (subagents) |
| **`kickoff verify`** | Re-run verify only |
| **`kickoff wire`** | RAG consumer wire (after verify PASS) |

## Piranesi mirror

`/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/phase2-cs-ai/STATUS.md`
"""
    (PIPELINE / "STATUS.md").write_text(status, encoding="utf-8")
    try:
        PIR_PROJECT.mkdir(parents=True, exist_ok=True)
        (PIR_PROJECT / "STATUS.md").write_text(
            status.replace("Piranesi mirror", "Scholia SSOT").replace(
                str(PIR_PROJECT / "STATUS.md"), str(PIPELINE / "STATUS.md")
            ),
            encoding="utf-8",
        )
    except OSError as exc:
        print(f"WARN: could not write Piranesi mirror STATUS: {exc}", file=sys.stderr)


def main() -> int:
    PIPELINE.mkdir(parents=True, exist_ok=True)
    (PIPELINE / "scripts").mkdir(exist_ok=True)
    entries = chapter_entries()
    curriculum = build_curriculum(entries)
    out = PIPELINE / "card_curriculum.yaml"
    out.write_text(yaml.dump(curriculum, sort_keys=False, allow_unicode=True), encoding="utf-8")
    write_status(curriculum)
    print(f"Wrote {out}")
    print(
        f"chapters={len(entries)} fan-out={sum(1 for e in entries if e['route']=='fan-out')} "
        f"inline={sum(1 for e in entries if e['route']=='inline')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
