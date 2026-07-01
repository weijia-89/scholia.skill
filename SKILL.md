---
name: scholia
description: |
  Corpus-to-skill wrapper for journal articles and textbook chapters plus operator questions.
  Routes palamedes literature fan-out, piranesi export-only research, phylax audit, and notebooklm-prep.
  Use when: scholia, corpus to skill, paper to skill, textbook to skill, academic ingest,
  literature skill builder, turn papers into a Cursor skill, build reference library from PDFs.
  Explicit-invoke only — trainer routes in; manual /scholia until disable-model-invocation bug fixed [RECENCY RISK].
type: project-skill
version: 0.3.0
status: v0.3.0 — output harnesses, practical-cards pipeline verify, bounded review loops; W10+S4e+S4 base merged
authors: Operator + ChatPRD W10/S4e merge
license: MIT
disable-model-invocation: true
required_tools: [file_read]
recommended_tools: [grep]
optional_tools: [zotero-mcp]
composes: []
pairs_with:
  - trainer
  - palamedes
  - piranesi
  - phylax
  - notebooklm-prep
---

# scholia (σχόλια)

**Canon:** `references/merged-decision-canon-20260618.md` · research archive: `references/external-paths.md` § piranesi research archive

**Research triage (read first):** `references/research-triage-palamedes-scholia-piranesi.md` — scholia is an **independent generalist parser**, peer to palamedes and piranesi, not a submodule of aletheia or any consumer skill.

| Skill | Role |
|-------|------|
| **piranesi** | Finds documents and ideas; strategy and gap maps (export-only) |
| **palamedes** | Reference librarian — broad search, epistemic rigor, quick synthesis and reporting |
| **scholia** | Careful parser — full-depth read, procedural idea index, textbook-length rigor |

Wrapper-router for closed academic corpora → generated child skills or reference-library indexes. **Not** a monolith prompt. **Not** a `composes:` parent. Research slug **`scholia-corpus-to-skill`** disambiguates OSS name collisions (C-G001).

## Iron laws

1. **Amnesiac corpus** — load-bearing claims trace to ingested sources or tagged epistemic rows; no training-prior facts in generated skills.
2. **Provenance chain** — section anchors, DOI/ISBN, relative ingest paths in child artifacts.
3. **Route don't duplicate** — **palamedes** owns librarian passes (broad corpus, SYNTHESIS, tier grades, quick analyses); **piranesi** owns export-only discovery and strategy fan-out; **scholia** owns full-depth closed-corpus parse and procedural indexing; **phylax** owns semantic audit. Scholia does not re-run palamedes web loops or piranesi export in Cursor without operator waive.
4. **Operator questions first-class** — shape LITERATURE_INDEX roles before synthesis, not post-hoc FAQ.
5. **Monolith-read ban** — parent never reads N≥5 PDFs; fan-out mandatory at ≥5 PDFs or ≥3 peer-reviewed papers. Context-length evidence: 13.9–85% degradation range (Du et al. 2025, C-R008 [verified]) — never cite K-01 killed "7.9%" quote.
6. **Depth cap** — scholia fan-out ≤2 (scholia → ingest subagent); no nested scholia/phylax at depth >1.

## When NOT to use (σ−)

Do **not** invoke scholia when:

- N≥5 PDFs without paper/chapter fan-out plan (monolith-read ban)
- Same-session phylax audit of scholia.self (use fresh chat / `context:fork`)
- piranesi web research in Cursor without operator `waive-three-stage` + logged reason
- Copy-restricted or unreadable PDFs — operator judgment; set `drm:` in manifest (no mechanical verify)
- PHI/ITAR/no-TDM corpora — see negative-space refusals

## Architecture verdict: CONDITIONAL-WRAPPER

Handle **directly** when corpus ≤~100k tokens (C-R001 [verified]) AND provenance isolation not required (~1–2 papers).

**Delegate** when:

- ≥3 peer-reviewed papers (C-R002 [verified]) → paper fan-out (1 agent/paper)
- ≥5 PDFs (C-R003 [verified]) → fan-out mandatory
- Textbook chapters → chapter sub-agents (`prompts/literature-chapter-ingest.md`)
- Sparse corpus / missing primaries → operator runs **piranesi** in ChatPRD (export-only); return via palamedes P8 ingest
- Generated child skill → **phylax mode=full** before ship (fresh session / `context:fork` for scholia.self — no same-session self-audit)

**Falsifier:** monolith single-context beats composed fan-out on quality + auditability for corpora >100k tokens.

## Composition graph

```
trainer (L0, always-on)
  └── scholia (L1, explicit-invoke, /scholia)     [fan-out depth ≤2]
        ├── paper sub-agent × N (L2) — palamedes paper-ingest schema
        ├── chapter sub-agent × N (L2) — scholia chapter-ingest schema
        ├── phylax mode=full (L2, context:fork for scholia.self)
        └── notebooklm-prep (L2, opt-in)

piranesi (external ChatPRD only) → P8 ingest → local corpus
```

`pairs_with` is **body-text documentation only** — zero platform enforcement (W01/W04/W06).

**palamedes** is passive: schema SSOT; scholia dispatches sub-agents directly (flat fan-out).

## Routing decision tree

1. Operator invokes scholia with session bet + corpus path + output mode.
2. Estimate token volume + source count; scan `corpus_manifest.yaml` (text_quality, legal_status).
3. **Direct handle** if ≤~100k tokens (C-R001), ≤2 papers, no provenance isolation.
4. **Paper fan-out** if ≥3 peer-reviewed papers (parallel; N≤16 subagents per C-R004 [verified], else workflows).
5. **Chapter fan-out** for textbook material (TEXTBOOK-Q1 gate).
6. **Piranesi** if sparse (N<3, C-R007) or missing primaries — export-only; `waive-three-stage` operator override with logged reason only.
7. Cross-stage consistency check after synthesis (C-DG004): CONTRADICTED → block+route.
8. **Practical-usage pass (phase 2):** after `deep_read_v2` claim extraction, if manifest `practical_usage_required: true` or session bet includes coach / teach / operationalize / procedural output, fan out one subagent per book chapter per `prompts/practical-usage-card-fanout.md` (depth ≤2). Output: `literature/metadata/practical_cards/{topic_slug}.yaml` (or `metadata/practical_cards/` per corpus layout) per `references/practical-usage-schema.md`. Efficacy-only rows → `procedure_gap: true`, not silent.
9. Generate child artifact per output mode (see `prompts/output-mode-*.md` handoffs); run verify → phylax → trainer ship gate.
10. **Practical cards verify:** `bash scripts/verify_practical_cards.sh [corpus_root]` — fails when manifest requires cards but none exist; card has `<3` steps with `procedure_gap: false`; missing `source_anchor`; banned send-script patterns.

### Piranesi vs palamedes-only (Q-011)

| Route | When |
|-------|------|
| palamedes fan-out | PDFs on disk, closed corpus |
| piranesi export then fan-out | **N<3 papers** for target domain (C-R007 [verified]) |
| piranesi export only | missing primaries, architecture meta-design, coverage-gap on canon |

No automatic fan-out→scholia→piranesi escalation (W03 kill).

## Depth budget

| Level | Owner |
|-------|-------|
| L0 | trainer |
| L1 | scholia |
| L2 | paper/chapter ingest sub-agents, phylax, notebooklm-prep |
| L3–L4 | reserved |

**Platform:** Cursor IDE subagent depth **1**; Claude Code **5** (C-R005 [verified]). Document target platform per session.

## Corpus layout

```
literature/
  pdfs/           # operator-supplied; text layer required
  text/           # Marker / pdftotext exports
  ingests/        # {slug}_ingest.md ≤4500w each
  metadata/       # corpus_manifest.yaml
  index/          # LITERATURE_INDEX.md (optional alt: ingests/)
references/       # templates + generated provenance
prompts/          # chapter-ingest SSOT
scripts/          # verify_scholia.sh
```

**corpus_manifest.yaml:** doi, title, authors, year, source_type, pdf_path, ingest_status, text_quality, equation_density, language, legal_status, drm (none|watermark|hard|unreadable — operator metadata only), epistemic_tag (peer-reviewed|preprint), layout_mode (full|flat).

**Paper-ingest** (8 fields): title, authors, year, venue, DOI, scope, key_findings, coverage_attestation — see `prompts/literature-paper-ingest.md`.

**Chapter-ingest:** see `prompts/literature-chapter-ingest.md` + TEXTBOOK-Q1.

## Output modes (2-axis)

**Axis-A — ingest pattern:** none | single | paper fan-out | chapter fan-out | P8 outside-input

**Axis-B — rendering mode:**

| Mode | v0.1 | Owner | Artifact |
|------|------|-------|----------|
| skill (default) | ✅ | scholia | SKILL.md + references/ + scripts/ ≤500 lines |
| reference-library | ✅ | scholia | LITERATURE_INDEX + references/ |
| study-guide | ✅ v0.2 | palamedes | `prompts/output-mode-study-guide.md` → study-guide-site |
| procedural | ✅ v0.2 | palamedes | `prompts/output-mode-procedural.md` → procedural-guide-site; `layout_mode: flat` |
| notebooklm-pack | ✅ v0.2 | notebooklm-prep | `prompts/output-mode-notebooklm-pack.md` → `.sources` manifest |

One session bet → one primary output (Q-019).

## Operator workflow

1. Drop PDFs → `literature/pdfs/` (`{author}_{year}_{slug}.pdf`).
2. **Optional — zotero-mcp:** pre-fill `literature/metadata/corpus_manifest.yaml` from a Zotero collection — see `references/zotero-mcp-workflow.md`. Operator still supplies PDFs on disk; MCP gate (`@wintermute` → form-check if invoking MCP in session).
3. Run `bash scripts/verify_scholia.sh` on corpus (layout, manifest fields).
4. Operator questions + session bet → index roles.
5. Trainer: stakes L2–L4; plan-first if >5 output files.
6. Fan-out → ingests → LITERATURE_INDEX → SYNTHESIS (skip fan-out for procedural `layout_mode: flat`).
7. **Output mode branch:**
   - `skill` / `reference-library` → generate from `references/child-skill-template.md`
   - `study-guide` / `procedural` / `notebooklm-pack` → hand off via `prompts/output-mode-*.md` (palamedes / notebooklm-prep render)
8. `verify_scholia.sh` on artifact → phylax full → trainer ship gate.

**ChatPRD upload folders:** flat attachable `*.md` only (≤8) — **no README**, no sync scripts inside the folder. Runbook in chat or parent export README. Path output iron law: `references/external-paths.md` § operator rules.

## verify_scholia.sh contract

Mechanical gates below — semantic audit is **phylax** (BIV taxonomy; SF-02/07/08/14 doc gates). See `references/contract-graph.md`.

```bash
bash scripts/verify_scholia.sh [--self|--pressure|--cross-stage|/path/to/generated.skill]
```

| Gate | Check |
|------|-------|
| SF-01 | frontmatter name+description |
| SF-03 | SKILL.md body ≤500 lines (C-R009 [verified]: vendor 5k token budget) |
| SF-04 | references/ + provenance |
| SF-05 | no absolute paths in body |
| SF-06 | claims have DOI/tag not path-only |
| SF-12 | ingests ≤4500w |
| SF-13 | LITERATURE_INDEX present |
| monolith | N≥5 PDFs require ingests/ fan-out |
| C-DG004 | cross-stage structure when SYNTHESIS.md + provenance.md (auto on child verify; `--cross-stage`) |
| layout_mode flat | procedural corpus: pdfs+text+metadata only (C-DG007); ingests/ optional |

**Mechanical vs phylax (C-DG004):** verify counts provenance rows and WARNs on unanchored claims; semantic SUPPORTED/CONTRADICTED/DRIFT is **phylax only** — CONTRADICTED → block+route per routing tree step 7.

**Not mechanical (operator / phylax):** DRM classification. **PS-10** piranesi export-only guard is mechanical via `--pressure`. See `CLAIMS.md` C-R006 override note.

Claude Code: register as **Stop** hook (exit 0 pass, exit 2 block). See `references/pressure-scenarios.md`.

## phylax + trainer ship

- **Child skills:** phylax `mode=full` before operator ships.
- **scholia.self:** phylax in **fresh session** via `context:fork` — recursion guard (Q-014). No same-session self-audit (W10 K-02 killed legacy recursion critic).
- **Trainer:** coached pushback on skipped plan gate, monolith-read, ship-without-phylax; log SHIPPED-WITH-OVERRIDE.

## Explicit-invoke workaround (Q-003)

`disable-model-invocation: true` — trainer routes via inline instructions until platform preload bug fixed [RECENCY RISK]. Operator may invoke `/scholia` manually.

## Kill register (do not revive)

See `references/kill-register.md` (K-01–K-07). Platform enforces K-01/K-03 in CLAIMS.md.

- recursion critic alias → use context:fork
- SF-01–SF-14 as phylax semantic checklist → BIV taxonomy
- composes:/pairs_with: platform enforcement
- palamedes as active routing intermediary
- Pattern-9-as-universal for textbook chapters (use chapter-ingest)
- Automatic piranesi escalation loops

## References (load on demand)

| File | Purpose |
|------|---------|
| `references/research-triage-palamedes-scholia-piranesi.md` | palamedes · scholia · piranesi division of labor |
| `references/hooks-config.md` | Stop/PreToolUse hooks (gap #8 doc) |
| `references/closed-corpus-piranesi-routing.md` | Gap #9 closed-corpus policy stub |
| `references/n20-clustering-fallback.md` | N>20 fan-out design stub |
| `references/wc-to-token-approximation.md` | Line vs token budget (gap #11) |
| `references/merged-decision-canon-20260618.md` | W10+S4e+S4 base merge |
| `references/s3-source-ledger.md` | S3 §9 folded (43 sources) |
| `references/s4-open-decisions.md` | S3 §8 open decisions |
| `references/source-register-corrections.md` | S-06/S-09 URLs (K-06 reconciled) |
| `references/kill-register.md` | K-01–K-07 dispositions |
| `references/phylax-preflight-s4.md` | Child-skill phylax checklist |
| `references/child-skill-template.md` | Generated skill shape |
| `references/provenance-template.md` | CLAIMS ledger |
| `references/negative-space.md` | Refusal categories |
| `CLAIMS.md` | Verified routing thresholds (Gate B → piranesi ingests) |
| `references/contract-graph.md` | Gate → enforcement map |
| `references/pressure-scenarios.md` | Test oracles |
| `prompts/literature-paper-ingest.md` | Peer-reviewed fan-out schema |
| `prompts/literature-chapter-ingest.md` | Textbook schema |
| `references/practical-usage-schema.md` | Phase-2 implementation cards (practical_usage) |
| `prompts/practical-usage-card-fanout.md` | Phase-2 subagent paste packet |
| `prompts/cs-ai-practical-cards-fanout-kickoff.md` | cs-ai phase-2 kickoff (operator-gated) |
| `references/practical-usage-consumer-bridge.md` | Consumer wire contract (scholia → downstream) |
| `scripts/verify_practical_cards.sh` | Implementation card mechanical gate (manifest-driven) |
| `scripts/verify_practical_cards_pipeline.sh` | Phase-2 pipeline artifact harness (PC-P01..P14) |
| `references/output-gate-contract.md` | Generator + verify gate pattern for skill outputs |
| `scripts/lib/review_loop_guard.sh` | Bounded loop circuit breaker (max iters · wall clock · stuck signature) |
| `scripts/sync_banter_r02_practical_cards_mirror.sh` | Aletheia SSOT → scholia mirror card sync |
| `references/sub-skills-index.md` | Platform sub-skill map |
| `references/corpus-manifest-template.yaml` | Session manifest stub |
| `references/zotero-mcp-workflow.md` | Optional Zotero MCP pre-fill |
| `prompts/output-mode-study-guide.md` | study-guide handoff |
| `prompts/output-mode-procedural.md` | procedural handoff |
| `prompts/output-mode-notebooklm-pack.md` | notebooklm-pack handoff |
| `prompts/practical-usage-ingest-strategy.md` | Two-phase ingest strategy prompt |
| `prompts/practical-usage-implement-kickoff.md` | Phase 2 implementation orchestrator (operator-gated) |
| `literature/deai-operator-corpus/prompts/PIPELINE.md` | Closed-corpus ChatPRD ingest → refine → evidence digest → implement |
| `literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` | v0.2 semantic preservation — quote-first, row-not-prose, provenance chain |
| `literature/deai-operator-corpus/localonly/research/opus46-synthesis-scratchpad.md` | Palamedes research — Opus 4.6 / context / orchestration refinements |
| `literature/deai-operator-corpus/prompts/synth_corpus_evidence_digest.md` | High-evidence cross-source synthesis + operator elicitation rows |
| `literature/deai-operator-corpus/prompts/KICKOFF_ORCHESTRATOR_corpus_extraction_wave.md` | Superset wave kickoff (trainer gates, verify loop) |
| `literature/deai-operator-corpus/references/synthesis-operator-table.md` | ChatPRD synthesis handoff — Prompt + bulleted Attachments; current phase only; no Save to in chat |
| `literature/deai-operator-corpus/scripts/emit_synthesis_operator_table.py` | Regenerate active-phase operator table from disk |
| `references/ROADMAP-v0.2.md` | v0.2.1 canon shipped |
| `references/external-paths.md` | Cross-repo absolute paths + Q-001–Q-024 decision register (SF-05 offload) |

## Specialist version pins (canon §4)

palamedes ≥3.11.0 · phylax ≥0.2.1 · piranesi ≥0.6.0 — document in child skill handoffs when pairs_with peers are invoked.

## Trainer notes

**Program:** job-search / exam-prep / project research → domain Cursor skills from paper corpora.

**Your form:** text-layer PDFs only; no silent OCR; equation-heavy → Marker → `literature/text/`.

**Next session:** operator corpus child `*.skill/` session — first end-to-end use.
