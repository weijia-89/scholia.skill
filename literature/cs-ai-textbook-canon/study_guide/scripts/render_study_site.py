#!/usr/bin/env python3
"""Render CS+AI Foundation study guide as solarpunk HTML daily site.

Output: study_guide/daily/{index,day-NN,guide,exams,glossary}.html

Usage:
    python3 /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/study_guide/scripts/render_study_site.py
"""

from __future__ import annotations

import re
from pathlib import Path
from html import escape as h

from jinja2 import Template
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.anchors.index import slugify as _default_slug
from mdit_py_plugins.attrs import attrs_plugin

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "daily"

SG_MD = ROOT / "CS_AI_Foundation_Study_Guide.md"
PE_MD = ROOT / "PRACTICE_EXAMS.md"
GLOS_MD = ROOT / "glossary.md"
DAILY_NOTES_MD = ROOT / "daily_notes.md"

DEFAULT_START = "2026-06-30"
PROGRAM_END = "2026-07-11"

DAYS = [
    dict(w=1, d=1, title="Search, memory, complexity defined",
        subtitle="<strong>Track A:</strong> Grokking ch1-2. <strong>Track B:</strong> Ousterhout ch1-2.",
        focus="Morning: binary search on a sorted list. Trace halving on paper for 128 names (7 steps max). Afternoon: Ousterhout's practical definition of complexity and the three symptoms (change amplification, cognitive load, unknown unknowns). Deliverable: one binary-search trace plus a symptom log from code you know. Evening: build memory palace Room 1 (Algorithms).",
        citations=[
            ("Grokking ch1", '"Binary search is an algorithm; its input is a sorted list of elements."'),
            ("Ousterhout ch1", '"Complexity is anything related to the structure of a software system that makes it hard to understand and modify."'),
            ("Serra et al. 2025", "Retrieval practice beats massed re-reading for delayed recall."),
        ],
        links=[("Study Guide Part 1", "guide.html#part-1-algorithms-and-growth-rates-grokking-algorithms-2e"),
               ("Study Guide Part 2", "guide.html#part-2-managing-complexity-in-software-ousterhout-2e"),
               ("Syllabus", "guide.html#appendix-a-chapter-map-and-ingest-status")]),

    dict(w=1, d=2, title="Recursion and divide-and-conquer",
        subtitle="Grokking ch3-4; Ousterhout ch3 (strategic vs tactical).",
        focus="Write recursive sum with base case. Partition an array around a pivot (quicksort step). Read Ousterhout on strategic programming: when does tactical patching become expensive? Deliverable: recursion trace + partition example. Evening: anchor sort/recursion loci in Room 1.",
        citations=[
            ("Grokking ch3-4", "Call stack holds unfinished recursive frames."),
            ("Ousterhout ch3", "Investment in design vs ship-now tactical patches."),
            ("Bjork 1994", "Desirable difficulties: generation effect from writing traces."),
        ],
        links=[("Part 1.3 Recursion", "guide.html#13-recursion-and-the-call-stack"),
               ("Part 1.4 Quicksort", "guide.html#14-divide-and-conquer-quicksort-and-merge-sort"),
               ("Appendix B miss 1", "guide.html#miss-pattern-1-big-o-as-speed-multiplier")]),

    dict(w=1, d=3, title="Hashes and graphs; deep modules",
        subtitle="Grokking ch5-6; Ousterhout ch4-5.",
        focus="Hash collision example (two keys, one slot). BFS layer order on a small graph. Define deep module vs shallow module; Unix open/read/write as the canonical deep interface. Deliverable: collision narrative + BFS visit order. Evening: start Room 2 (Design).",
        citations=[
            ("Grokking ch5", '"First, I\'ve been telling you a white lie" about hash O(1).'),
            ("Ousterhout ch4", "Deep modules: much functionality, simple interface."),
            ("Ousterhout ch5", "Information hiding: Parnas; leakage when interfaces expose internals."),
        ],
        links=[("Part 1.5 Hash tables", "guide.html#15-hash-tables-and-collisions"),
               ("Part 2.4 Deep modules", "guide.html#24-deep-modules-vs-shallow-modules"),
               ("Glossary", "glossary.html")]),

    dict(w=1, d=4, title="Trees, Dijkstra, layers",
        subtitle="Grokking ch7-9; Ousterhout ch7-8.",
        focus="Dijkstra step table on a 4-node weighted graph. Contrast with BFS. Identify a pass-through method in code you have seen. Deliverable: Dijkstra table + one layering critique. Evening: leakage stickers on Room 2 loci.",
        citations=[
            ("Grokking ch9", "Non-negative weights; differs from BFS when edge weights vary."),
            ("Ousterhout ch7", "Pass-through methods signal shallow layers."),
            ("Ingest flag", 'Grokking "no cycles" for Dijkstra is contested; non-negative weights suffice.'),
        ],
        links=[("Part 1.8 Dijkstra", "guide.html#18-dijkstra-and-weighted-graphs"),
               ("Appendix B miss 3", "guide.html#miss-pattern-3-bfs-vs-dijkstra"),
               ("Part 2.6 Layers", "guide.html#26-layers-and-pass-through-methods")]),

    dict(w=1, d=5, title="NP, DP, design capstone — Mock A",
        subtitle="Grokking ch10-12; Ousterhout ch22. Afternoon: Mock A (90 min).",
        focus="Morning: greedy failure on 0/1 knapsack; DP table sketch. Skim ch22: pick 3 design principles and 3 red flags to memorize. Afternoon: Mock A timed (algorithms + design). Score yourself; missed items become Appendix B stickers tonight.",
        citations=[
            ("Grokking ch10-11", "Greedy vs dynamic programming tradeoff."),
            ("Ousterhout ch22", "16 principles + 14 red flags capstone."),
            ("TAP", "Mock form matches weekly assessment; open-book with sources."),
        ],
        links=[("Mock A", "exams.html#mock-a-track-a-day-5-90-minutes"),
               ("Appendix B", "guide.html#appendix-b-high-frequency-miss-patterns"),
               ("Appendix D.4 Day 5", "guide.html#d4-daily-integration-schedule")]),

    dict(w=2, d=1, title="AI engineering framing",
        subtitle="AIE ch1-2.",
        focus='Read ch1 scale thesis and three-layer AI stack. ch2: autoregressive LMs, sampling, hallucination. Deliverable: crawl-walk-run plan for one hypothetical FM app. Evening: build Room 3 (AI framing).',
        citations=[
            ("AIE ch1", '"If I could use only one word to describe AI post-2020, it\'d be scale."'),
            ("AIE ch1", "AI engineering builds on readily available foundation models."),
            ("AIE ch2", "Temperature and top-p control diversity; nondeterminism is structural."),
        ],
        links=[("Part 3", "guide.html#part-3-ai-engineering-framing-aie-ch12"),
               ("Glossary: foundation model", "glossary.html"),
               ("Appendix D.2", "guide.html#d2-build-your-own-memory-palace")]),

    dict(w=2, d=2, title="Evaluation and EDD",
        subtitle="AIE ch3-4.",
        focus="List four reasons FM eval is hard. Draft an 8-row eval rubric for one use case across EDD buckets (domain, generation, instruction, cost/latency). Name three AI-as-judge biases. Evening: Room 4 (Eval) loci.",
        citations=[
            ("AIE ch3", "Perplexity, functional correctness, AI-as-judge."),
            ("AIE ch4", "Evaluation-driven development before leaderboard chasing."),
            ("Appendix B miss 6-7", "Perplexity and leaderboard traps."),
        ],
        links=[("Part 4.1 Eval", "guide.html#41-why-fm-evaluation-is-hard-ch3"),
               ("Part 4.2 EDD", "guide.html#42-evaluation-driven-development-ch4"),
               ("Mock B preview", "exams.html#mock-b-track-b-day-10-120-minutes")]),

    dict(w=2, d=3, title="Prompts, RAG, agents",
        subtitle="AIE ch5-6.",
        focus="Sketch a RAG pipeline: ingest, chunk, embed, retrieve, generate. Define prompt injection (direct vs indirect). Calculate compound accuracy for 10 steps at 95% per step. Evening: RAG/agent images on Room 4.",
        citations=[
            ("AIE ch6", "Two dominating patterns: RAG and agents."),
            ("AIE ch5", "Prompt injection via untrusted retrieved content."),
            ("AIE ch6", "Hybrid search: BM25 + embeddings, often RRF fusion."),
        ],
        links=[("Part 4.4 RAG", "guide.html#44-rag-pattern-ch6"),
               ("Part 4.5 Agents", "guide.html#45-agents-and-compound-accuracy"),
               ("Appendix B miss 8-9", "guide.html#miss-pattern-8-long-context-kills-rag")]),

    dict(w=2, d=4, title="Adaptation, data, decide",
        subtitle="AIE ch7-8; Ousterhout ch20-21 (decide what matters).",
        focus="LoRA vs full finetune in one paragraph each. Apply facts-vs-form heuristic to a customer-support scenario. List three dataset quality dimensions from ch8. Evening: Room 5 (Production) loci.",
        citations=[
            ("AIE ch7", "PEFT/LoRA/QLoRA for adaptation without full retrain."),
            ("AIE ch8", "Dataset engineering often beats architecture churn."),
            ("Ousterhout ch20-21", "Decide what matters; omit needless features."),
        ],
        links=[("Part 5.1 Finetuning", "guide.html#51-finetuning-and-peft-ch7"),
               ("Part 5.2 Data", "guide.html#52-dataset-engineering-ch8"),
               ("Appendix B miss 10", "guide.html#miss-pattern-10-finetune-for-fresh-facts")]),

    dict(w=2, d=5, title="Inference, architecture — Mock B",
        subtitle="AIE ch9-10. Afternoon: Mock B (120 min).",
        focus="Morning: TTFT vs TPOT; draw ch10 architecture stack from memory (guardrails, router, cache, context, model, observability). Afternoon: Mock B. Final palace walk all five rooms. No new material after 8 PM.",
        citations=[
            ("AIE ch9", "KV cache; latency metrics for streaming APIs."),
            ("AIE ch10", "Metrics, logs, traces; guardrails; feedback-loop risks."),
            ("Walker 2017", "Sleep consolidates learning before heavy assessment."),
        ],
        links=[("Mock B", "exams.html#mock-b-track-b-day-10-120-minutes"),
               ("Part 5.4 Architecture", "guide.html#54-architecture-stack-ch10"),
               ("Appendix C checklist", "guide.html#appendix-c-completion-checklist-day-10")]),
]

assert len(DAYS) == 10

_NOTES_OPEN_RE = re.compile(r"^\s*<!--\s*user-notes:([a-z0-9-]+)\s*-->\s*$")
_NOTES_CLOSE_RE = re.compile(r"^\s*<!--\s*/user-notes:([a-z0-9-]+)\s*-->\s*$")
_NOTE_LINE_RE = re.compile(
    r"^\*(?P<text>.*)\*\{\.user-note\s+#(?P<id>note-[a-z0-9-]+-\d+)\}\s*$"
)

PAGE_TMPL = Template("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ title }}</title>
<link rel="stylesheet" href="style.css">
<script src="notes.js" defer></script>
</head>
<body>
<main>
{{ body|safe }}
</main>
</body>
</html>
""")


def _unescape_attrs(text: str) -> str:
    out, i = [], 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text) and text[i + 1] in ("\\", "*", "{", "}"):
            out.append(text[i + 1])
            i += 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def parse_daily_notes() -> dict:
    if not DAILY_NOTES_MD.exists():
        return {}
    lines = DAILY_NOTES_MD.read_text(encoding="utf-8").splitlines()
    notes, current = {}, None
    for line in lines:
        m_open = _NOTES_OPEN_RE.match(line)
        if m_open:
            current = m_open.group(1)
            notes.setdefault(current, [])
            continue
        if _NOTES_CLOSE_RE.match(line):
            current = None
            continue
        if current is None:
            continue
        m_note = _NOTE_LINE_RE.match(line)
        if m_note:
            notes[current].append(
                (m_note.group("id"), _unescape_attrs(m_note.group("text")))
            )
    return notes


def render_user_notes_html(anchor: str, notes_by_anchor: dict) -> str:
    bucket = notes_by_anchor.get(anchor, [])
    if not bucket:
        return ""
    return "".join(
        f'<aside class="user-note" data-note-id="{h(nid)}" data-anchor="{h(anchor)}" data-source="baked">{h(txt)}</aside>'
        for nid, txt in bucket
    )


def _collapse_dashes(s: str) -> str:
    return re.sub(r"-+", "-", _default_slug(s)).strip("-")


def fix_em_dashes(html: str) -> str:
    return html.replace("\u2014", "-").replace("\u2013", "-")


def render_markdown(md_text: str) -> str:
    md = MarkdownIt("gfm-like", {"html": True, "linkify": False, "typographer": False})
    md = md.enable("table").enable("strikethrough")
    try:
        md = md.use(attrs_plugin)
    except Exception:
        pass
    md = md.use(anchors_plugin, min_level=1, max_level=4, slug_func=_collapse_dashes)
    return fix_em_dashes(md.render(md_text))


def render_day_page(idx: int, notes_by_anchor: dict) -> str:
    d = DAYS[idx]
    n = idx + 1
    af, ac, al = f"day-{n}-focus", f"day-{n}-citations", f"day-{n}-links"
    cites_html = "".join(
        f'<aside class="margin-note"><strong>{h(lbl)}</strong>: {gloss}</aside>'
        for lbl, gloss in d["citations"]
    )
    links_html = "<ul>" + "".join(
        f'<li><a href="{h(href)}">{h(lbl)}</a></li>' for lbl, href in d["links"]
    ) + "</ul>"
    prev_href = f"day-{n-1:02d}.html" if n > 1 else "index.html"
    next_href = f"day-{n+1:02d}.html" if n < 10 else "index.html"
    body = f"""
<header class="hero">
  <div class="hero__category">CS + AI Foundation - week {d['w']} - day {d['d']}</div>
  <h1 class="hero__title">{h(d['title'])}</h1>
  <p class="hero__subtitle">{d['subtitle']}</p>
  <div class="hero__meta">
    <span><strong>Day {n}</strong> of 10</span>
    <span><strong>Week {d['w']}</strong> of 2</span>
    <span>Program end {PROGRAM_END}</span>
  </div>
</header>
<div class="focus" data-notable-anchor="{af}">
  <span class="focus__label">Today's focus</span>
  <p>{h(d['focus'])}</p>
</div>
{render_user_notes_html(af, notes_by_anchor)}
<span class="notable-anchor" data-notable-anchor="{ac}" aria-hidden="true"></span>
{cites_html}
{render_user_notes_html(ac, notes_by_anchor)}
<h2 id="{al}" data-notable-anchor="{al}">Links</h2>
{links_html}
{render_user_notes_html(al, notes_by_anchor)}
<nav class="daynav">
  <a href="{prev_href}">{"&larr; Index" if n == 1 else f"&larr; Day {n-1}"}</a>
  <span class="daynav__meta">Start {DEFAULT_START}</span>
  <a href="{next_href}">{"Index &rarr;" if n == 10 else f"Day {n+1} &rarr;"}</a>
</nav>
"""
    return fix_em_dashes(PAGE_TMPL.render(title=f"Day {n}: {d['title']}", body=body))


def render_index() -> str:
    grid = "".join(
        f'<a href="day-{i+1:02d}.html" data-idx="{i}">'
        f'D{i+1}<small>W{d["w"]} D{d["d"]}</small></a>'
        for i, d in enumerate(DAYS)
    )
    script_path = ROOT / "scripts" / "notes_server.py"
    body = f"""
<div id="server-banner" class="callout callout--info server-banner" hidden>
  <span class="callout__label">Notes backend</span>
  <p id="server-banner-msg">Checking backend...</p>
  <div class="server-banner__cmd">
    <code id="server-banner-cmd">python3 {h(str(script_path))}</code>
    <button type="button" class="server-banner__copy" data-copy-target="server-banner-cmd">copy</button>
  </div>
  <p class="server-banner__detail">Then open <code>http://localhost:8765/</code> for notes that persist to markdown.</p>
</div>
<header class="hero">
  <div class="hero__category">CS + AI Foundation</div>
  <h1 class="hero__title">2 weeks, 10 weekdays</h1>
  <p class="hero__subtitle">Grokking Algorithms 2e, Ousterhout 2e, AI Engineering 2025. Open each weekday morning; router sends you to today's lesson.</p>
  <div class="hero__meta">
    <span><strong>Start</strong> {DEFAULT_START}</span>
    <span><strong>End</strong> {PROGRAM_END}</span>
    <span><strong>Cadence</strong> weekdays</span>
  </div>
</header>
<div id="router-status"></div>
<h2>All 10 days</h2>
<div class="toc">{grid}</div>
<h2>Corpus</h2>
<ul>
  <li><a href="guide.html">Full Study Guide</a> - 5 parts + appendices A-D (pedagogy)</li>
  <li><a href="exams.html">Practice Checks</a> - Mock A (Day 5) and Mock B (Day 10)</li>
  <li><a href="glossary.html">Glossary</a> - 50+ terms</li>
</ul>
<h2 id="notes-tools">Notes tools</h2>
<p id="notes-tools-summary" class="hero__subtitle">Loading...</p>
<div class="notes-tools">
  <button type="button" id="notes-export" disabled>Export browser notes</button>
  <label class="notes-tools__import">Import markdown
    <input type="file" id="notes-import" accept=".md,text/markdown,text/plain">
  </label>
  <button type="button" id="notes-clear-ls" disabled>Clear browser notes</button>
</div>
<script>
const START = "{DEFAULT_START}";
function todayIdx() {{
  const [y,m,d] = START.split("-").map(Number);
  const start = new Date(y,m-1,d); start.setHours(0,0,0,0);
  const today = new Date(); today.setHours(0,0,0,0);
  if (today < start) return -1;
  let n = 0; const cur = new Date(start);
  while (cur < today) {{
    cur.setDate(cur.getDate()+1);
    if (cur.getDay() !== 0 && cur.getDay() !== 6) n++;
  }}
  if (today.getDay() === 0 || today.getDay() === 6) return -2;
  return n;
}}
const idx = todayIdx();
const status = document.getElementById("router-status");
if (idx === -1) {{
  status.innerHTML = '<div class="callout callout--info"><span class="callout__label">Not started</span><p>Start {DEFAULT_START}. <a href="day-01.html">Preview Day 1</a>.</p></div>';
}} else if (idx === -2) {{
  status.innerHTML = '<div class="callout callout--ok"><span class="callout__label">Rest day</span><p>Weekend. Light glossary review or extra mock.</p></div>';
}} else if (idx >= 10) {{
  status.innerHTML = '<div class="callout callout--ok"><span class="callout__label">Program complete</span><p><a href="day-10.html">Day 10</a> | Appendix C checklist in guide.</p></div>';
}} else {{
  document.querySelector('.toc a[data-idx="'+idx+'"]')?.classList.add('today');
  status.innerHTML = '<div class="callout callout--info"><span class="callout__label">Today is day '+(idx+1)+'</span><p>Redirecting... <a href="day-'+String(idx+1).padStart(2,"0")+'.html">Go now</a></p></div>';
  setTimeout(() => {{ if (status.style.display !== "none") location.href = 'day-'+String(idx+1).padStart(2,"0")+'.html'; }}, 3000);
}}
</script>
"""
    return fix_em_dashes(PAGE_TMPL.render(title="CS + AI Foundation", body=body))


def render_corpus_page(md_path: Path, title: str, subtitle: str, basename: str, notes_by_anchor: dict) -> str:
    body_html = render_markdown(md_path.read_text(encoding="utf-8"))
    body_html = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", body_html, count=1, flags=re.DOTALL)

    def _anchor_h2(m: re.Match) -> str:
        full = m.group(0)
        id_match = re.search(r'id="([^"]+)"', full)
        if not id_match:
            return full
        anchor = f"corpus-{basename}-{id_match.group(1)}"
        tagged = full.replace(">", f' data-notable-anchor="{anchor}">', 1)
        return tagged + render_user_notes_html(anchor, notes_by_anchor)

    body_html = re.sub(r"<h2[^>]*>.*?</h2>", _anchor_h2, body_html, flags=re.DOTALL)
    hero = f"""
<header class="hero">
  <div class="hero__category">CS + AI Foundation corpus</div>
  <h1 class="hero__title">{h(title)}</h1>
  <p class="hero__subtitle">{h(subtitle)}</p>
</header>
<nav class="daynav" style="margin-top:0;border-top:none;padding-top:0;">
  <a href="index.html">&larr; Daily index</a>
  <span class="daynav__meta">{md_path.name}</span>
  <a href="#" onclick="window.scrollTo({{top:0,behavior:'smooth'}});return false;">Top</a>
</nav>
"""
    return fix_em_dashes(PAGE_TMPL.render(title=title, body=hero + body_html))


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    notes = parse_daily_notes()
    for i in range(10):
        (OUT / f"day-{i+1:02d}.html").write_text(render_day_page(i, notes), encoding="utf-8")
    (OUT / "index.html").write_text(render_index(), encoding="utf-8")
    (OUT / "guide.html").write_text(
        render_corpus_page(SG_MD, "CS + AI Foundation Study Guide",
            "Grokking, Ousterhout, AIE. Parts 1-5 plus pedagogy appendix D.", "guide", notes),
        encoding="utf-8")
    (OUT / "exams.html").write_text(
        render_corpus_page(PE_MD, "Practice Checks",
            "Mock A (Day 5) and Mock B (Day 10). Open-book with sources.", "exams", notes),
        encoding="utf-8")
    (OUT / "glossary.html").write_text(
        render_corpus_page(GLOS_MD, "Glossary",
            "Algorithms, design, and AI engineering terms.", "glossary", notes),
        encoding="utf-8")
    n_notes = sum(len(v) for v in notes.values())
    print(f"rendered 10 daily + index + 3 corpus pages -> {OUT}")
    print(f"  baked notes: {n_notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
