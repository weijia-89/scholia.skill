# cs-ai-textbook-canon — scholia chapter fan-out kickoff

META: operator paste packet · scholia · corpus=cs-ai-textbook-canon · stakes=L3  
Save path: `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-textbook-canon-fanout-kickoff.md`

**Canon source (do not contradict without quote):**  
`/Users/dubs/Projects/piranesi.skill/research-projects/0625-textbook-canon/returns/cs_ai_textbook_canon_decision_20260625.md`

**Manifest:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/corpus_manifest.yaml`

**Triage:** `/Users/dubs/Projects/scholia.skill/references/research-triage-palamedes-scholia-piranesi.md`

---

## Kickoff (paste from here)

````text
You are the scholia parent orchestrator for corpus **cs-ai-textbook-canon** — full-depth chapter fan-out of the Piranesi-ranked CS + AI textbook canon.

Scholia ≠ palamedes ≠ piranesi:
- **piranesi** already produced the reading canon — do NOT web-search for book lists or pedagogy rankings
- **palamedes** owns librarian SYNTHESIS if needed — you parse closed text on disk only
- **scholia** dispatches one sub-agent per chapter (or per doc section for snapshots); parent NEVER monolith-reads a full textbook

## Load before acting (read in order)

1. /Users/dubs/Projects/scholia.skill/SKILL.md
2. /Users/dubs/Projects/scholia.skill/references/research-triage-palamedes-scholia-piranesi.md
3. /Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md
4. /Users/dubs/Projects/scholia.skill/prompts/literature-paper-ingest.md (NAM report only)
5. /Users/dubs/Projects/scholia.skill/references/provenance-template.md
6. /Users/dubs/Projects/piranesi.skill/research-projects/0625-textbook-canon/returns/cs_ai_textbook_canon_decision_20260625.md
7. /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/corpus_manifest.yaml

## Session bet

| Field | Value |
|-------|-------|
| Corpus slug | cs-ai-textbook-canon |
| Corpus root | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon |
| Output mode | **reference-library** — LITERATURE_INDEX.md + chapter ingests + SYNTHESIS.md |
| Child skill | Only if operator explicitly requests output=skill after reference-library ships |
| Stakes | L3 |
| Fan-out | **Mandatory** — 1 chapter (or 1 doc major section) = 1 sub-agent; depth ≤2 |
| Piranesi | export-only — no WebSearch/WebFetch unless operator says waive-three-stage |

## Operator questions (shape every ingest)

Answer these in each chapter ingest under `## Operator hooks`:

1. **Foundation layer** — what prerequisite concept does this chapter establish for later canon titles?
2. **MDCalc alignment** — does content touch agents, trace/eval observability, clinical AI safety, or regulated deployment? Tag [relevant] / [peripheral] / [none]. No invented employer-stack claims.
3. **Redundancy** — flag overlap with other canon titles (especially AIE ↔ DDIA 2e RAG, Kästner ↔ LLMOps ↔ DMLS).
4. **Scholia fit** — worked examples Y/N, exercise hooks, chapter boundary quality.

## Corpus layout (create if missing)

```
/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/
  pdfs/           # operator-supplied {slug}.pdf
  text/           # Marker or pdftotext exports
  ingests/        # {slug}_ch{NN}_ingest.md ≤4500w each
  metadata/       # corpus_manifest.yaml
  index/          # LITERATURE_INDEX.md
```

## Iron laws (this session)

- **DDIA is 2e (2026)** — ISBN 9781098119058. Never ingest or index 1e-only framing.
- **DROP Sommerville** — not in manifest; do not add.
- **MLOps redundancy** — prefer **Kästner ML in Production** as the single MLOps-depth book; ingest LLMOps and DMLS only for gap chapters flagged in SYNTHESIS.
- **CLRS** — TOC index + on-demand chapter ingests only; do not fan-out all 35 chapters unless operator overrides.
- **Docs** (LangSmith, Langfuse, LangGraph) — use **outside-input ingest** on exported markdown snapshots, not chapter-ingest on PDFs.
- **Amnesiac corpus** — claims in ingests must cite text anchors; no training-prior facts.
- **≤4500 words** per ingest file.

## Wave execution (do not launch all books at once)

Execute waves from manifest in order. Complete LITERATURE_INDEX row updates after each wave before starting the next.

| Wave | Weeks | Slugs |
|------|-------|-------|
| w1_foundation | 1–3 | grokking_algorithms_2e_2024, philosophy_software_design_2e_2021, ai_engineering_2025, hands_on_llms_2024 |
| w2_systems_llm | 4–6 | understanding_distributed_systems_2022, ddia_2e_2026, prompt_engineering_llms_2024 |
| w3_clinical_docs | 5–9 | simon_aliferis_healthcare_2024, nam_gen_ai_health_2025, langsmith_docs_snapshot, langfuse_docs_snapshot, langgraph_fault_tolerance_snapshot |
| w4_ops_governance | 8–12 | kaestner_ml_production_2025, responsible_ai_practice_2025 |
| w_optional | operator | clrs_4e_2022, se_modern_approach_2024, llmops_aryan_2025, designing_ml_systems_2022 |

**Gate before fan-out:** For each slug, confirm `text/{slug}.txt` (or `.md` for doc snapshots) exists. If missing, STOP and list missing paths — do not hallucinate chapter content.

## Sub-agent dispatch (one per chapter)

For each chapter, launch a Task subagent (explore or generalPurpose) with this payload:

---
SUB-AGENT: chapter ingest · {slug} · chapter {NN}

Read:
- /Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md
- Text: /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/{slug}.txt (chapter slice only — parent must pass line range or chapter heading)

Write:
- /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/{slug}_ch{NN}_ingest.md

Mandatory schema (literature-chapter-ingest.md):
1. title, authors, edition, ISBN if known
2. chapter_number, page_range, parent_book_title
3. scope, key_findings (anchor quotes only — [verified from text])
4. coverage_attestation (path, lines read, wrong-file flag)
5. pedagogy: learning_objectives, worked_examples_present Y/N, exercise_hooks
6. ## Operator hooks (four questions above)
7. TEXTBOOK-Q1 gate pass/fail per chapter

Cap: ≤4500 words. Forbidden: summary without anchors; monolith of other chapters.
---

For **nam_gen_ai_health_2025** use paper/report ingest schema (1 agent per major section).

For **doc snapshots** use section-based ingest: `{slug}_sec{NN}_ingest.md` with source URL in frontmatter.

## Parent deliverables (after all requested waves)

1. `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/index/LITERATURE_INDEX.md`
   - Rows: slug · book title · track A|B · wave · chapter count ingested · corpus role (core|optional|docs) · absolute ingest paths
   - Convergent themes table across tracks
2. `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/SYNTHESIS.md`
   - Session bet restatement · redundancy map · foundation stack diagram · gaps for operator
   - Cross-links to MDCalc agent-monitoring canon (pattern-portable only): /Users/dubs/Projects/piranesi.skill/research-projects/0623-mdcalc-agent-monitoring/returns/mdcalc_agent_monitoring_decision_canon_20260625.md
3. Update `corpus_manifest.yaml` — set `ingest_status: complete|partial` per entry
4. Run: `bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon`
5. **phylax mode=full** in a **fresh session** (context:fork) before operator ships reference-library as child skill

## Phase 2 — practical_usage cards (optional, separate session)

**Kickoff prompt (operator-gated):** `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md`

Agent **waits** until you reply **`kickoff phase 2`**. Subagent payload: `prompts/practical-usage-card-fanout.md`.

Consumer: `/Users/dubs/Projects/local-rag-linux-setup` (RAG + operator study) — not aletheia.

**Pilot on disk:** 4 hand-authored cards under `metadata/practical_cards/` — manifest flag stays `false` until fan-out completes.

## σ− (refuse)

- WebSearch for book recommendations (piranesi already ran)
- Monolith-read of any full textbook in parent agent
- Ingesting Sommerville or DDIA 1e as canon
- Claiming MDCalc production stack
- Skipping TEXTBOOK-Q1 / coverage attestation
- Same-session phylax audit of scholia.self

## Operator preflight (confirm before wave 1)

- [ ] PDFs or OA exports on disk under `pdfs/`
- [ ] Text layer exported under `text/`
- [ ] DDIA file is **2e** (2026) not 1e
- [ ] Operator chose: Kästner-only vs Kästner+LLMOps gap chapters
- [ ] Doc snapshots exported for LangSmith / Langfuse / LangGraph

Emit a one-screen plan: wave 1 slug list, estimated chapter fan-out count, missing text files, then begin w1_foundation fan-out.
````

---

## Paths

| Role | Path |
|------|------|
| This kickoff | `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-textbook-canon-fanout-kickoff.md` |
| Manifest | `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/metadata/corpus_manifest.yaml` |
| Canon | `/Users/dubs/Projects/piranesi.skill/research-projects/0625-textbook-canon/returns/cs_ai_textbook_canon_decision_20260625.md` |
| Chapter schema | `/Users/dubs/Projects/scholia.skill/prompts/literature-chapter-ingest.md` |
| Practical cards (phase 2) | `/Users/dubs/Projects/scholia.skill/prompts/practical-usage-card-fanout.md` |
| Practical cards kickoff (cs-ai, gated) | `/Users/dubs/Projects/scholia.skill/prompts/cs-ai-practical-cards-fanout-kickoff.md` |
| Verify | `bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon` |

## Invoke

New Cursor chat → `/scholia` or paste kickoff fence → confirm preflight → execute wave 1.
