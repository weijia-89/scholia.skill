#!/usr/bin/env python3
"""Extract EPUB spine chapters to source_exports/chapters/ (Option A).

Maps curriculum chapters via epub_nav_match (regex on nav label) or epub_spine_index.
Falls back to byte-offset split_chapters when EPUB missing or no match.
"""
from __future__ import annotations

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from corpus_paths import EXPORT_DIR, MANIFEST, PROJECT  # noqa: E402

CURRICULUM = PROJECT / "chapter_curriculum.yaml"
CHAPTER_DIR = EXPORT_DIR / "chapters"

NS = {
    "ncx": "http://www.daisy.org/z3986/2005/ncx/",
    "opf": "http://www.idpf.org/2007/opf",
    "xhtml": "http://www.w3.org/1999/xhtml",
    "epub": "http://www.idpf.org/2007/ops",
    "container": "urn:oasis:names:tc:opendocument:xmlns:container",
}

try:
    from bs4 import BeautifulSoup

    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


def html_to_text(html: bytes) -> str:
    if HAS_BS4:
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style"]):
            tag.decompose()
        return soup.get_text("\n", strip=True)
    text = re.sub(rb"<[^>]+>", b" ", html)
    return unescape(text.decode("utf-8", errors="replace"))


def read_opf(zf: zipfile.ZipFile) -> tuple[str, ET.Element, dict[str, ET.Element]]:
    container = ET.fromstring(zf.read("META-INF/container.xml"))
    rootfile = container.find(".//container:rootfile", NS)
    if rootfile is None:
        rootfile = container.find(".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile")
    opf_path = rootfile.get("full-path")
    opf = ET.fromstring(zf.read(opf_path))
    opf_dir = str(Path(opf_path).parent)
    if opf_dir == ".":
        opf_dir = ""
    manifest = {item.get("id"): item for item in opf.findall(".//opf:manifest/*", NS)}
    return opf_dir, opf, manifest


def spine_hrefs(zf: zipfile.ZipFile, opf_dir: str, opf: ET.Element, manifest: dict) -> list[str]:
    hrefs: list[str] = []
    for itemref in opf.findall(".//opf:spine/opf:itemref", NS):
        item = manifest.get(itemref.get("idref"))
        if item is None:
            continue
        href = item.get("href")
        full = f"{opf_dir}/{href}" if opf_dir else href
        hrefs.append(full)
    return hrefs


def nav_points(zf: zipfile.ZipFile, opf_dir: str, manifest: dict) -> list[tuple[str, str]]:
    """Return (label, spine_href) from NCX or EPUB3 nav."""
    points: list[tuple[str, str]] = []
    ncx_item = next(
        (m for m in manifest.values() if m.get("media-type") == "application/x-dtbncx+xml"),
        None,
    )
    if ncx_item:
        ncx_path = f"{opf_dir}/{ncx_item.get('href')}" if opf_dir else ncx_item.get("href")
        ncx = ET.fromstring(zf.read(ncx_path))
        for np in ncx.findall(".//ncx:navPoint", NS):
            label_el = np.find("ncx:navLabel/ncx:text", NS)
            content = np.find("ncx:content", NS)
            if label_el is not None and content is not None:
                label = (label_el.text or "").strip()
                src = content.get("src", "").split("#")[0]
                full = f"{opf_dir}/{src}" if opf_dir and not src.startswith("/") else src
                points.append((label, full))
    return points


def epub_text_by_href(zf: zipfile.ZipFile, hrefs: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for href in hrefs:
        try:
            out[href] = html_to_text(zf.read(href))
        except KeyError:
            print(f"WARN missing spine item: {href}")
    return out


def slug_epub_path(slug: str) -> Path | None:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or {}
    for entry in data.get("entries", []):
        if entry.get("slug") == slug and entry.get("format") == "epub":
            p = Path(entry["inbox_file"])
            if p.is_file():
                return p
    return None


def extract_range(hrefs: list[str], texts: dict[str, str], start_href: str, end_href: str | None) -> str:
    try:
        i0 = hrefs.index(start_href)
    except ValueError:
        # fuzzy: match basename
        base = Path(start_href).name
        i0 = next(i for i, h in enumerate(hrefs) if Path(h).name == base)
    if end_href:
        try:
            i1 = hrefs.index(end_href)
        except ValueError:
            base = Path(end_href).name
            i1 = next(i for i, h in enumerate(hrefs) if Path(h).name == base)
    else:
        i1 = len(hrefs)
    parts = [texts.get(h, "") for h in hrefs[i0:i1]]
    return "\n\n".join(p for p in parts if p).strip()


def match_nav_start(nav: list[tuple[str, str]], pattern: str) -> str | None:
    rx = re.compile(pattern, re.I)
    for label, href in nav:
        if rx.search(label):
            return href
    return None


def split_epub_book(book: dict) -> list[dict]:
    slug = book["slug"]
    prefix = book["prefix"]
    epub_path = slug_epub_path(slug)
    if not epub_path:
        print(f"SKIP epub missing for {slug}")
        return []

    chapters = book.get("chapters", [])
    built: list[dict] = []

    with zipfile.ZipFile(epub_path) as zf:
        opf_dir, opf, manifest = read_opf(zf)
        hrefs = spine_hrefs(zf, opf_dir, opf, manifest)
        texts = epub_text_by_href(zf, hrefs)
        nav = nav_points(zf, opf_dir, manifest)

        if nav:
            print(f"NAV {slug}: {len(nav)} points")
            for label, href in nav[:15]:
                print(f"  {label[:50]:50s} {Path(href).name}")

        CHAPTER_DIR.mkdir(parents=True, exist_ok=True)
        resolved: list[tuple[str, dict, str | None]] = []

        for ch in chapters:
            start_href = None
            if ch.get("epub_nav_match"):
                start_href = match_nav_start(nav, ch["epub_nav_match"])
            if start_href is None and ch.get("epub_spine_href"):
                start_href = ch["epub_spine_href"]
            if start_href is None:
                print(f"WARN no epub match {prefix}/{ch['chapter_id']}")
                continue
            resolved.append((start_href, ch, start_href))

        # sort by spine order
        def spine_index(h: str) -> int:
            base = Path(h).name
            for i, sh in enumerate(hrefs):
                if Path(sh).name == base or sh == h:
                    return i
            return 10**9

        resolved.sort(key=lambda x: spine_index(x[0]))

        for i, (start_href, ch, _) in enumerate(resolved):
            end_href = resolved[i + 1][0] if i + 1 < len(resolved) else None
            body = extract_range(hrefs, texts, start_href, end_href)
            if len(body) < 200:
                print(f"WARN short epub slice {prefix}/{ch['chapter_id']} ({len(body)} chars)")
                continue

            cid = ch["chapter_id"]
            out_name = f"{prefix}_{cid}.txt"
            out_path = CHAPTER_DIR / out_name
            out_path.write_text(body, encoding="utf-8")
            rel = f"source_exports/chapters/{out_name}"
            meta = {
                "prefix": prefix,
                "slug": slug,
                "chapter_id": cid,
                "title": ch["title"],
                "lanes": ch.get("lanes", []),
                "rationale": ch.get("rationale", ""),
                "split_mode": "epub_spine",
                "epub_start_href": start_href,
                "char_len": len(body),
                "chapter_path": rel,
            }
            built.append(meta)
            print(f"EPUB SLICE {out_name} ({len(body):,} chars)")

    return built


def main() -> None:
    data = yaml.safe_load(CURRICULUM.read_text(encoding="utf-8")) or {}
    all_built: list[dict] = []
    for book in data.get("books", []):
        if book.get("split_mode") != "epub_spine":
            continue
        all_built.extend(split_epub_book(book))

    if all_built:
        index_path = CHAPTER_DIR / "_index_epub.yaml"
        index_path.write_text(
            yaml.dump({"chapters": all_built}, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        print(f"Wrote {len(all_built)} epub slices → {CHAPTER_DIR}")
    else:
        print("No epub_spine books processed")


if __name__ == "__main__":
    main()
