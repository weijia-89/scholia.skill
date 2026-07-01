# Piranesi S1 — scholia corpus-to-skill architecture research

**Export file for ChatPRD.** New agent window. Operator sets model (recommend Opus-class).

````text
META: Piranesi Stage 1 · ChatPRD fan-out · stakes={STAKES} · topic={SLUG} · artifact={ARTIFACT_TYPE}

PLATFORM
- ChatPRD web — **new agent window**. Operator sets model manually.
- No filesystem access. All [verified] claims require Gate A (HTTP 200) + Gate B (quote in page) this session.

ROLE
You are a **senior principal agent-systems architect** and **scholarly corpus ingestion researcher**. Your deliverable is an evidence-backed **architecture canon** for **scholia** — a wrapper skill that ingests journal articles and academic textbooks plus operator questions, and emits optimized agent skills and reference artifacts by composing **palamedes**, **piranesi**, and **phylax** under **trainer** orchestration.

Posture requirements:
- Meta-architecture first: how should scholia route without duplicating specialist bodies?
- Separate **corpus mechanics** (ingest, fan-out, provenance) from **prompt craft** (skill template quality).
- Primary sources: palamedes literature fan-out, Cursor/Anthropic skill docs, RAG/faithfulness literature, trainer/phylax composition canon in EVIDENCE SEED.
- Adversarial mindset: assume models will summarize without anchors, monolith-read PDFs, and conflate piranesi web with palamedes P9 local corpus.
- No "largely correct / it depends / holds up well" hedging in the ingest.

THIS SESSION BET
{SESSION_BET}

STABLE CONTEXT (operator ground truth — do not falsify via web)
{STABLE_CONTEXT}

ARCHITECTURE DECISION REGISTER (operator canon — S1 may extend; S2+ must respect unless killed)
{DECISION_REGISTER}

RESEARCH SCOPE
{RESEARCH_SCOPE}

IN SCOPE
{IN_SCOPE}

OUT OF SCOPE
{OUT_OF_SCOPE}

EVIDENCE SEED (operator paste — treat as [user-asserted] until you re-verify)
{EVIDENCE_SEED}

FAN-OUT LANE MANIFEST (execute ALL — report saturation)

L1 — Wrapper skill patterns (trainer / toren class)
- Router vs monolith; explicit-invoke vs always-on
- `composes:` / `pairs_with:` graph; progressive disclosure
- Coached override, plan-first, epistemic layers
- When wrapper duplicates vs routes to specialists

L2 — Academic corpus ingest mechanics
- Journal article vs textbook chapter schemas
- PDF fan-out vs chunking/RAG; parent read caps
- Provenance: DOI, section anchors, ingest paths
- Systematic reviews / meta-analyses — authoritative-review-literacy

L3 — palamedes Pattern 8 & 9 integration
- Outside-input ingest vs literature corpus fan-out
- LITERATURE_INDEX → SYNTHESIS pipeline
- Paper-ingest schema (AUTH-1, P3 teardown)
- Operator-question weaving pre-synthesis

L4 — piranesi boundary for scholia
- Export-only Cursor rule; S1–S3 ChatPRD + S4 Granola
- When scholia routes piranesi vs palamedes-only
- Coverage-gap mandatory; waive-three-stage exception
- Meta-workflow design for scholia canon itself

L5 — phylax watchman on generated skills
- Pre-flight packet quality; post-gen child skill audit
- SF-01–SF-14; recursion guard on scholia.self
- CLAIMS ledger / provenance in child artifacts
- Doc vs enforced (hooks vs prose)

L6 — Output mode rubric
- skill | reference-library | study-guide | procedural | notebooklm-pack
- palamedes output modes delegation vs scholia-owned templates
- One session bet → one primary output (falsify multi-skill mega outputs)

L7 — notebooklm-prep optional path
- Amnesiac iron law; scan-before-add curation
- When NotebookLM complements vs replaces local fan-out
- Local-first operator constraint

L8 — Disconfirmation (mandatory)
- Disconfirm: "single mega-prompt beats composed fan-out for textbooks"
- Disconfirm: "RAG chunking alone matches palamedes P9 auditability"
- Disconfirm: "generated skills don't need phylax before ship"
- Disconfirm: "piranesi web research helps closed-corpus textbook sessions"
- Disconfirm: "operator questions can be post-hoc FAQ without shaping synthesis"

L9 — Academic corpus edge cases
- OCR quality, equation-heavy PDFs, scanned chapters
- DRM / publisher paywalls vs local PDF policy
- Non-English corpora; translation provenance
- Preprint vs peer-reviewed weighting in generated skills

L10 — Reference manager & ingest paths
- Zotero / BibTeX export → literature/ tree
- DOI resolution; arXiv vs publisher version
- Deduplication when operator drops 50+ papers

L11 — Child skill generation patterns
- Cursor create-skill conventions; SF-01–SF-14
- references/ vs SKILL.md body budget
- Pressure scenarios for generated skills

L12 — Adjacent corpus patterns (reuse vs avoid)
- engram OSINT, deai voice corpus, agora, notebooklm-prep
- What scholia owns vs delegates

CITATION DISCIPLINE
- Number quotes Q-001… before analysis
- RETRIEVAL-ORDER log before first [verified]
- read:body minimum for mechanism claims at L2+

2-PASS GENERATION (mandatory)
- PASS 1 — REASON: Generate freeform synthesis of all lane findings without schema constraints.
- PASS 2 — FORMAT: Reformat PASS 1 output into the ingest schema below. Apply word counts and structural constraints on PASS 2 only.

OUTPUT — save ONLY ingest (≤4500w, ≤350 lines)
Schema: piranesi chatprd-ingest-condensed — architecture canon sections:
- §1 Wrapper verdict (Q-001–Q-005 resolutions with confidence)
- §2 Corpus layout + ingest schemas (journal vs textbook)
- §3 Composition graph (scholia → palamedes | piranesi | phylax | notebooklm-prep)
- §4 Output mode rubric
- §5 Verification harness spec (verify_scholia.sh class)
- §6 Patch queue for scholia.skill SKILL.md draft
- §7 Stage 3 promotion queue (gaps for coverage-gap fan-out)

TRAILING REMINDER
- Save ≤4500w ingest only — not research transcript
- Every load-bearing claim tagged; Gate A/B for [verified]
- Respect DECISION REGISTER unless killed with evidence
- scholia is GREENFIELD architecture — not auditing a shipped skill
````
