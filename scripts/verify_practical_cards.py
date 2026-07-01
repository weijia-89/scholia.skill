#!/usr/bin/env python3
"""Mechanical gate for scholia practical_usage implementation cards (v2)."""
from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

BANNED = re.compile(
    r"text her|text him|send this opener|copy-paste this", re.IGNORECASE
)
MANIFEST_FLAG = re.compile(
    r"^practical_usage_required:\s*(?:true|yes|1)\s*(?:#.*)?$",
    re.MULTILINE | re.IGNORECASE,
)
CARD_SPLIT = re.compile(r"(?m)^\s+- exercise_name:")


def find_manifest(corpus: Path) -> Path | None:
    for candidate in (
        corpus / "metadata" / "corpus_manifest.yaml",
        corpus / "literature" / "metadata" / "corpus_manifest.yaml",
    ):
        if candidate.is_file():
            return candidate
    return None


def manifest_requires_cards(corpus: Path) -> bool:
    manifest = find_manifest(corpus)
    if manifest is None:
        return False
    return bool(MANIFEST_FLAG.search(manifest.read_text(encoding="utf-8")))


def find_cards_dir(corpus: Path) -> Path | None:
    for candidate in (
        corpus / "literature" / "metadata" / "practical_cards",
        corpus / "metadata" / "practical_cards",
    ):
        if candidate.is_dir():
            return candidate
    return None


def split_card_blocks(text: str) -> list[str]:
    parts = CARD_SPLIT.split(text)
    blocks: list[str] = []
    for i, part in enumerate(parts):
        if i == 0:
            continue
        blocks.append("exercise_name:" + part)
    return blocks


def field_value(block: str, field: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(field)}:\s*(.+)$", block, re.MULTILINE)
    if not match:
        return None
    val = match.group(1).strip()
    if val.lower() in {"null", "~", ""}:
        return None
    if val.startswith('"') and val.endswith('"'):
        return val[1:-1]
    if val.startswith("'") and val.endswith("'"):
        return val[1:-1]
    return val


def list_items(block: str, field: str) -> list[str]:
    lines = block.splitlines()
    header_idx = None
    base_indent = 0
    for idx, line in enumerate(lines):
        match = re.match(rf"^(\s*){re.escape(field)}:\s*(.*)$", line)
        if not match:
            continue
        rest = match.group(2).strip()
        if rest == "":
            header_idx = idx
            base_indent = len(match.group(1))
            break
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            if not inner:
                return []
            return [
                x.strip().strip("'\"")
                for x in inner.split(",")
                if x.strip()
            ]

    if header_idx is None:
        return []

    items: list[str] = []
    for line in lines[header_idx + 1 :]:
        item_match = re.match(r"^(\s*)-\s+(.+)$", line)
        if item_match and len(item_match.group(1)) > base_indent:
            items.append(item_match.group(2).strip())
            continue
        key_match = re.match(r"^(\s*)([A-Za-z_][\w-]*)\s*:", line)
        if key_match and len(key_match.group(1)) <= base_indent:
            break
    return items


def procedure_gap(block: str) -> bool:
    val = field_value(block, "procedure_gap")
    if val is None:
        return False
    return val.lower() in {"true", "yes", "1"}


def validate_card_file(path: Path, *, require_quality_level: bool = False) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = path.name

    if BANNED.search(text):
        errors.append(f"{rel}: banned send-script pattern detected")

    blocks = split_card_blocks(text)
    if not blocks:
        errors.append(f"{rel}: no cards[] entries with exercise_name")
        return errors

    for idx, block in enumerate(blocks, start=1):
        label = f"{rel} card {idx}"
        if not field_value(block, "exercise_name"):
            errors.append(f"{label}: missing exercise_name")
        anchor = field_value(block, "source_anchor")
        if not anchor:
            errors.append(f"{label}: missing source_anchor")
        gap = procedure_gap(block)
        steps = list_items(block, "steps")
        if not gap and len(steps) < 3:
            errors.append(
                f"{label}: fewer than 3 steps ({len(steps)}) with procedure_gap: false"
            )
        if not gap and len(steps) > 12:
            errors.append(
                f"{label}: more than 12 steps ({len(steps)}) — split card or trim"
            )
        ql = field_value(block, "quality_level")
        if require_quality_level and not ql:
            errors.append(f"{label}: missing quality_level (manifest requires cards)")
        if ql and ql not in {"full", "partial", "procedure_gap"}:
            errors.append(f"{label}: invalid quality_level {ql!r}")
        if ql == "procedure_gap" and not gap:
            errors.append(f"{label}: quality_level procedure_gap requires procedure_gap: true")
        if ql == "full" and gap:
            errors.append(f"{label}: quality_level full incompatible with procedure_gap: true")
    return errors


def verify_corpus(corpus: Path) -> int:
    required = manifest_requires_cards(corpus)
    cards_dir = find_cards_dir(corpus)
    yaml_files: list[Path] = []
    if cards_dir is not None:
        yaml_files = sorted(cards_dir.glob("*.yaml"))

    fails = 0

    if required and not yaml_files:
        print("FAIL: practical_usage_required in manifest but no card YAML files")
        fails += 1
    elif required:
        print(f"PASS: manifest requires cards; found {len(yaml_files)} YAML file(s)")
    else:
        print("PASS: practical_usage_required not set — card check optional")

    if not yaml_files:
        if cards_dir is None and required:
            print(f"FAIL: practical_cards directory missing under {corpus}")
            fails += 1
        print(f"---\nFails: {fails}")
        return 2 if fails else 0

    print(f"PASS: cards directory {cards_dir}")

    all_errors: list[str] = []
    for path in yaml_files:
        all_errors.extend(validate_card_file(path, require_quality_level=required))

    if all_errors:
        for err in all_errors:
            print(f"FAIL: {err}")
        fails += len(all_errors)
    else:
        print(f"PASS: validated {len(yaml_files)} card file(s)")

    if required and len(yaml_files) < 3:
        print(
            "FAIL: manifest requires cards but only "
            f"{len(yaml_files)} file(s) (need ≥3 when flag set)"
        )
        fails += 1
    elif len(yaml_files) >= 3:
        print(f"PASS: at least 3 card files ({len(yaml_files)})")

    print(f"---\nFails: {fails}")
    return 2 if fails else 0


def run_self_test() -> int:
    """Mechanical regression oracles for parser edge cases."""
    fails = 0

    def check(name: str, ok: bool, detail: str = "") -> None:
        nonlocal fails
        if ok:
            print(f"PASS: self-test {name}")
        else:
            fails += 1
            print(f"FAIL: self-test {name}" + (f" — {detail}" if detail else ""))

    block = """\
  - exercise_name: Demo
    steps:
      - one
      - two
      - three
    cognitive_frame: hold stance
    observables:
      - visible one
      - visible two
    source_anchor: C-1
    procedure_gap: false
    quality_level: full
"""
    steps = list_items(block, "steps")
    check("steps exclude observables", steps == ["one", "two", "three"], repr(steps))

    block4 = """\
    - exercise_name: Deep
      steps:
        - a
        - b
        - c
      source_anchor: anchor
      procedure_gap: false
      quality_level: full
"""
    check("4-space card split", len(split_card_blocks(block4)) == 1)
    check("4-space step count", len(list_items(block4, "steps")) == 3)

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        meta = root / "metadata"
        meta.mkdir()
        cards = meta / "practical_cards"
        cards.mkdir()
        (meta / "corpus_manifest.yaml").write_text("practical_usage_required: True\n")
        for i in range(3):
            (cards / f"ok{i}.yaml").write_text(
                f"""topic_slug: ok{i}
cards:
  - exercise_name: Ok
    steps:
      - one
      - two
      - three
    source_anchor: C-{i}
    procedure_gap: false
    quality_level: full
"""
            )
        check("manifest True capitalized", verify_corpus(root) == 0)

        (cards / "bad.yaml").write_text(
            """topic_slug: bad
cards:
  - exercise_name: Bad
    steps:
      - one
      - two
    source_anchor: C-b
    procedure_gap: false
"""
        )
        check("detect short steps", verify_corpus(root) == 2)

    print(f"---\nSelf-test fails: {fails}")
    return 2 if fails else 0


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[1] in {"--self-test", "--self"}:
        return run_self_test()

    if len(argv) != 2:
        print(
            "Usage: verify_practical_cards.py [--self-test] <corpus_root>",
            file=sys.stderr,
        )
        return 2

    corpus = Path(argv[1]).resolve()
    if not corpus.is_dir():
        print(f"FAIL: corpus root not found: {corpus}")
        return 2

    return verify_corpus(corpus)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
