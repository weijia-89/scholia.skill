# Research triage — palamedes · scholia · piranesi

META: scholia canon · operator-facing · 2026-06-19  
**Scope:** How the three research skills divide labor. **Scholia is independent** — not a submodule of aletheia, banter, or any consumer project.

---

## ELI15

| Skill | Metaphor | Job |
|-------|----------|-----|
| **piranesi** | Imp on errands | Finds documents, ideas, and strategy gaps you do not yet have on disk — export-only web/ChatPRD fan-out |
| **palamedes** | Reference librarian | Broad retrieval, epistemic rigor, tier-graded synthesis, quick analyses and reporting — does **not** pretend to have read every page |
| **scholia** | Careful parser | Full-depth read of texts already in hand; procedural indexing of ideas, nuance, chapter structure — textbook-length with the same rigor palamedes applies to claims |

**Consumer skills** (aletheia, banter, job-prep sites, etc.) **consume** indexed output from all three. They do not own scholia.

---

## When to invoke which

```
Need sources / strategy / gap map?     → piranesi (export) → operator saves ingests
Need catalog + rigor + fast synthesis? → palamedes (Pattern 9 body-read queue, SYNTHESIS, audits)
Need full text indexed in depth?       → scholia (chapter/paper fan-out, LITERATURE_INDEX, reference-library)
Building product from indexes?         → consumer skill (aletheia, …) — wiring plan, not scholia's job
```

| Question | Route |
|----------|-------|
| "What exists on IG/DM flirt evidence?" | palamedes literature corpus + piranesi if sparse |
| "What should our workbook canon contain?" | piranesi S1–S3 → palamedes BOOKS_REFERENCES merge |
| "I bought Antony — index every load-bearing chapter" | **scholia** chapter fan-out |
| "Quick TL;DR for operator decision" | palamedes SYNTHESIS / CURATED_OPERATOR |
| "Integrate all lanes into coaching framework" | piranesi meta-workflow **or** consumer architecture — **after** palamedes + scholia indexes exist |

---

## Division of labor (load-bearing)

### Palamedes

- Broad search and corpus design (Pattern 9, literature reviews, fact-check loops)
- Epistemic tags, tier grading, contradiction hunt, saturation reports
- **Quick** paper teardowns, operator-facing SYNTHESIS, gap registers (C-015, C-016)
- YAML claim rows, quality audits, curated operator views
- **Does not skim every page** of a 400-page handbook — cites chapters, abstracts, secondary summaries where sufficient

### Scholia

- **Closed corpus on disk** — PDFs/text the operator already has
- **No skimming mandate** — chapter sub-agents read assigned span; capture nuance palamedes fast passes may miss
- Procedural indexing: learning objectives, exercise hooks, argument structure, definitional forks, contested claims **inside** the text
- Textbook-length and workbook-length material at same rigor as paper fan-out
- Output: `literature/ingests/`, LITERATURE_INDEX, reference-library YAML, optional generated `*.skill/` child
- **Does not** replace palamedes web discovery or piraneses strategy export

### Piranesi

- **Export-only** — ChatPRD/Granola; no filesystem in session
- Finds and frames: what to read, what bets to make, coverage gaps, meta-workflow design
- Produces ingests and decision canons operator merges locally
- **Does not** deep-parse PDFs; returns reading lists and strategy, not chapter indexes

---

## Typical pipeline (any domain)

```
1. piranesi     → "what to acquire / what gap to close" (strategy ingests)
2. palamedes    → catalog, tier, SYNTHESIS, operator reports (librarian pass)
3. operator     → obtains PDFs
4. scholia      → deep parse + procedural index (parser pass)
5. consumer     → wires indexes into product (aletheia framework, exam site, etc.)
```

Steps 2 and 4 **both** apply epistemic rigor; depth differs. Palamedes may **point** scholia at titles ("body-read Phillips"); scholia **executes** the read.

---

## Anti-patterns

| Wrong | Right |
|-------|-------|
| Scholia as "aletheia depth plane" | Scholia indexes text; aletheia consumes via bridge docs |
| Palamedes monolith-read of full workbook | Scholia chapter fan-out |
| Piranesi in Cursor for PDF chapter quotes | Scholia or palamedes closed corpus |
| Scholia WebSearch without `waive-three-stage` | piranesi export or palamedes with operator waive |
| One scholia child skill per consumer book **required** | reference-library mode; consumer chooses wiring |

---

## Consumer bridge pattern (example: aletheia)

When a consumer project needs scholia output, document a **consumer bridge** in the **consumer repo** — not inside scholia canon:

- `/Users/dubs/Projects/aletheia.skill/references/aletheia-scholia-consumer-bridge.md`

Scholia sessions use generic kickoffs (`prompts/r02-textbook-workbook-corpus-kickoff.md`); bridge doc says **where merged artifacts land** in aletheia.

---

## Paths

- Scholia: `/Users/dubs/Projects/scholia.skill/SKILL.md`
- Palamedes: `/Users/dubs/Projects/.cursor/skills/palamedes/SKILL.md`
- Piranesi: `/Users/dubs/Projects/piranesi.skill/SKILL.md`
