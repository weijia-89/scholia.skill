# Syllabus — CS + AI Foundation (2 weeks)

**Program:** cs-ai-textbook-canon wave-1 foundation track  
**Cadence:** 10 weekdays (Mon–Fri × 2 weeks), ~2–3 hours/day  
**Sources on disk:** Grokking Algorithms 2e · A Philosophy of Software Design 2e · AI Engineering (Huyen 2025)  
**Site root:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/study_guide/daily/index.html`

## Learning outcomes

By end of week 2 you should be able to:

1. **Reason about growth rates** — state whether a problem is O(n), O(n log n), O(n²), etc., and why it matters for scale.
2. **Use core algorithm families** — search, sort, hash, BFS/Dijkstra, greedy vs DP tradeoffs.
3. **Diagnose software complexity** — name symptoms (change amplification, cognitive load, unknown unknowns) and apply deep-module / information-hiding heuristics.
4. **Frame AI products** — explain foundation models, the three-layer AI stack, and crawl-walk-run deployment.
5. **Design evaluation** — build a mental model for exact eval, AI-as-judge, and custom eval pipelines.
6. **Construct context** — compare RAG vs long-context, agents vs chains, finetune vs RAG for facts vs form.
7. **Operate in production** — articulate observability (metrics/logs/traces), guardrails, and feedback-loop risks.

## Weekly arc

| Week | Theme | Track A | Track B |
|------|-------|---------|---------|
| **1** | Thinking in steps + hiding complexity | Grokking ch 1–12 (curated) | Ousterhout ch 1–5, 9, 20–22 (curated) |
| **2** | Building on foundation models | — | AIE ch 1–10 |

## Daily schedule

| Day | Focus | Readings (ingest paths) | Deliverable |
|-----|-------|-------------------------|-------------|
| **D1** | Search, memory, complexity defined | Grokking ch1–2; Ousterhout ch1–2 | Binary search trace; complexity symptom log |
| **D2** | Recursion & divide-and-conquer | Grokking ch3–4; Ousterhout ch3 | Recursive sum + quicksort partition on paper |
| **D3** | Hashes & graphs; deep modules | Grokking ch5–6; Ousterhout ch4–5 | Hash collision example; BFS order trace |
| **D4** | Trees & weighted paths; layers | Grokking ch7–9; Ousterhout ch7–8 | Dijkstra table; pass-through method refactor sketch |
| **D5** | NP, DP, design capstone | Grokking ch10–12; Ousterhout ch22 principles | **Mock A** (algorithms + design) |
| **D6** | AI engineering framing | AIE ch1–2 | Crawl-walk-run plan for one hypothetical app |
| **D7** | Evaluation | AIE ch3–4 | Draft 8-row eval rubric for one use case |
| **D8** | Prompts, RAG, agents | AIE ch5–6 | Prompt + retrieval sketch (no code required) |
| **D9** | Adaptation & data | AIE ch7–8; Ousterhout ch20–21 | RAG vs finetune decision for one scenario |
| **D10** | Inference & architecture | AIE ch9–10 | **Mock B** (AI engineering); palace walkthrough |

## Assessment

| Component | Weight | When |
|-----------|--------|------|
| Daily retrieval drills (Appendix D.4) | 30% | Each evening |
| Mock A (Track A) | 25% | Day 5 |
| Mock B (Track B) | 25% | Day 10 |
| Palace + mnemonic portfolio | 10% | Day 10 |
| Glossary self-test | 10% | Day 10 |

## Materials

| Item | Path |
|------|------|
| Full study guide | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/study_guide/CS_AI_Foundation_Study_Guide.md` |
| Practice checks | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/study_guide/PRACTICE_EXAMS.md` |
| Glossary | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/study_guide/glossary.md` |
| Chapter ingests | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/` |
| EPUB/PDF sources | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/pdfs/` |

## Honest scope notes

- **Hands-On LLMs** is canon-paired tutorial code but **not** in this 2-week sprint; schedule a follow-on week for labs.
- **Figures** in the text export are often `[]` placeholders; open the EPUB/PDF for diagrams (binary search, DP grids, architecture figures).
- Quotes in the study site are **[verified from text]** exports; contested claims are flagged, not smoothed.
