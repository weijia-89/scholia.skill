#!/usr/bin/env python3
"""CS+AI Foundation notes backend. Stdlib HTTP server + /api/note CRUD.

Run:
    python3 /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/study_guide/scripts/notes_server.py

Open http://localhost:8765/index.html
"""
from __future__ import annotations

import json
import re
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = ROOT / "daily"
STUDY_GUIDE = ROOT / "CS_AI_Foundation_Study_Guide.md"
DAILY_NOTES = ROOT / "daily_notes.md"
HOST = "127.0.0.1"
PORT = 8765

DAY_ANCHOR_RE = re.compile(r"^day-\d+-(focus|citations|links)$")
SAFE_ANCHOR_RE = re.compile(r"^[a-z0-9-]+$")
NOTE_ID_RE = re.compile(r"^note-[a-z0-9-]+-\d+$")
MAX_TEXT_LEN = 2000
NOTE_LINE_RE = re.compile(
    r"^\*(?P<text>.*)\*\{\.user-note\s+#(?P<id>note-[a-z0-9-]+-\d+)\}\s*$"
)


def target_file_for_anchor(anchor: str) -> Path:
    if DAY_ANCHOR_RE.match(anchor):
        return DAILY_NOTES
    return STUDY_GUIDE


def escape_attrs_text(text: str) -> str:
    for old, new in (("\\", "\\\\"), ("*", "\\*"), ("{", "\\{"), ("}", "\\}")):
        text = text.replace(old, new)
    return text


def _open_close_patterns(anchor: str) -> tuple[str, str]:
    return f"<!-- user-notes:{anchor} -->", f"<!-- /user-notes:{anchor} -->"


def find_delimiter_block(md_path: Path, anchor: str) -> Optional[tuple[int, int]]:
    if not md_path.exists():
        raise FileNotFoundError(str(md_path))
    _, close_pat = _open_close_patterns(anchor)
    open_pat, _ = _open_close_patterns(anchor)
    lines = md_path.read_text(encoding="utf-8").splitlines()
    open_idx = close_idx = None
    for i, line in enumerate(lines):
        if open_idx is None and line.strip() == open_pat:
            open_idx = i
            continue
        if open_idx is not None and line.strip() == close_pat:
            close_idx = i
            break
    if open_idx is None or close_idx is None:
        return None
    return open_idx + 1, close_idx - 1


def _unescape_attrs_text(text: str) -> str:
    out, i = [], 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text) and text[i + 1] in ("\\", "*", "{", "}"):
            out.append(text[i + 1])
            i += 2
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def list_notes_in_block(md_path: Path, anchor: str) -> list[tuple[str, str]]:
    block = find_delimiter_block(md_path, anchor)
    if block is None:
        raise ValueError(f"delimiter block missing: {anchor}")
    start, end = block
    if end < start:
        return []
    lines = md_path.read_text(encoding="utf-8").splitlines()
    return [
        (m.group("id"), _unescape_attrs_text(m.group("text")))
        for line in lines[start : end + 1]
        if (m := NOTE_LINE_RE.match(line))
    ]


def _read_lines(md_path: Path) -> list[str]:
    return md_path.read_text(encoding="utf-8").splitlines()


def _write_lines(md_path: Path, lines: list[str]) -> None:
    text = "\n".join(lines)
    if not text.endswith("\n"):
        text += "\n"
    md_path.write_text(text, encoding="utf-8")


def add_note(anchor: str, text: str) -> dict:
    if not SAFE_ANCHOR_RE.match(anchor):
        return {"ok": False, "error": "invalid anchor"}
    if not text or not text.strip():
        return {"ok": False, "error": "empty text"}
    if len(text) > MAX_TEXT_LEN:
        return {"ok": False, "error": "text too long"}
    md_path = target_file_for_anchor(anchor)
    try:
        n = len(list_notes_in_block(md_path, anchor)) + 1
    except (FileNotFoundError, ValueError) as e:
        return {"ok": False, "error": str(e) if isinstance(e, ValueError) else "target file missing"}
    note_id = f"note-{anchor}-{n}"
    new_line = f"*{escape_attrs_text(text.strip())}*{{.user-note #{note_id}}}"
    _, close_pat = _open_close_patterns(anchor)
    lines = _read_lines(md_path)
    insert_at = next((i for i, line in enumerate(lines) if line.strip() == close_pat), None)
    if insert_at is None:
        return {"ok": False, "error": "anchor not found"}
    lines.insert(insert_at, new_line)
    _write_lines(md_path, lines)
    return {"ok": True, "note_id": note_id}


def _find_note_line(note_id: str) -> Optional[tuple[Path, int]]:
    for md_path in (STUDY_GUIDE, DAILY_NOTES):
        if not md_path.exists():
            continue
        for i, line in enumerate(_read_lines(md_path)):
            if (m := NOTE_LINE_RE.match(line)) and m.group("id") == note_id:
                return md_path, i
    return None


def update_note(note_id: str, text: str) -> dict:
    if not NOTE_ID_RE.match(note_id) or not text or not text.strip():
        return {"ok": False, "error": "invalid input"}
    if len(text) > MAX_TEXT_LEN:
        return {"ok": False, "error": "text too long"}
    found = _find_note_line(note_id)
    if not found:
        return {"ok": False, "error": "note_id not found"}
    md_path, idx = found
    lines = _read_lines(md_path)
    lines[idx] = f"*{escape_attrs_text(text.strip())}*{{.user-note #{note_id}}}"
    _write_lines(md_path, lines)
    return {"ok": True, "note_id": note_id}


def delete_note(note_id: str) -> dict:
    if not NOTE_ID_RE.match(note_id):
        return {"ok": False, "error": "invalid note_id"}
    found = _find_note_line(note_id)
    if not found:
        return {"ok": False, "error": "note_id not found"}
    md_path, idx = found
    lines = _read_lines(md_path)
    del lines[idx]
    _write_lines(md_path, lines)
    return {"ok": True, "note_id": note_id}


class NotesHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def _read_json_body(self) -> Optional[dict]:
        length = self.headers.get("Content-Length")
        if not length:
            return None
        try:
            return json.loads(self.rfile.read(int(length)).decode("utf-8"))
        except (ValueError, json.JSONDecodeError):
            return None

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/note":
            self._send_json(404, {"ok": False, "error": "not found"})
            return
        body = self._read_json_body()
        if not isinstance(body, dict):
            self._send_json(400, {"ok": False, "error": "invalid JSON body"})
            return
        anchor, text = body.get("anchor"), body.get("text")
        if not isinstance(anchor, str) or not isinstance(text, str):
            self._send_json(400, {"ok": False, "error": "anchor and text required"})
            return
        result = add_note(anchor, text)
        self._send_json(200 if result.get("ok") else 400, result)

    def do_PUT(self) -> None:
        parsed = urlparse(self.path)
        if not parsed.path.startswith("/api/note/"):
            self._send_json(404, {"ok": False, "error": "not found"})
            return
        body = self._read_json_body()
        text = body.get("text") if isinstance(body, dict) else None
        if not isinstance(text, str):
            self._send_json(400, {"ok": False, "error": "text required"})
            return
        result = update_note(parsed.path[len("/api/note/"):], text)
        self._send_json(200 if result.get("ok") else 404, result)

    def do_DELETE(self) -> None:
        parsed = urlparse(self.path)
        if not parsed.path.startswith("/api/note/"):
            self._send_json(404, {"ok": False, "error": "not found"})
            return
        result = delete_note(parsed.path[len("/api/note/"):])
        self._send_json(200 if result.get("ok") else 404, result)

    def log_message(self, fmt: str, *args) -> None:
        sys.stdout.write("notes_server: " + (fmt % args) + "\n")


def main() -> int:
    server = ThreadingHTTPServer((HOST, PORT), NotesHandler)
    print(f"notes_server: http://{HOST}:{PORT}")
    print(f"  static: {STATIC_DIR}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
