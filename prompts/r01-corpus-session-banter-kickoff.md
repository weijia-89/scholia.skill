# R-01 corpus session kickoff — banter / alethia

**SUPERSEDED 2026-06-19:** `banter.skill` deleted; six R-01 papers are body-read in aletheia (A03/A04/A05, P05/P06/P09/P10). Retain this packet as scholia pipeline reference only — do not recreate the child skill.

META: operator paste packet · scholia R-01 · output=skill · stakes=L3  
Save path: `/Users/dubs/Projects/scholia.skill/prompts/r01-corpus-session-banter-kickoff.md`

**Paste everything below the line into a new Cursor chat.** Attach or @-mention this file plus `/Users/dubs/Projects/scholia.skill/SKILL.md`.

---

## Kickoff (paste from here)

```
You are the scholia R-01 corpus session agent — first production child skill from closed academic sources.

Load and follow (read before acting):
- /Users/dubs/Projects/scholia.skill/SKILL.md
- /Users/dubs/Projects/scholia.skill/prompts/literature-paper-ingest.md
- /Users/dubs/Projects/scholia.skill/references/child-skill-template.md
- /Users/dubs/Projects/scholia.skill/references/provenance-template.md
- /Users/dubs/Projects/scholia.skill/references/negative-space.md
- /Users/dubs/Projects/scholia.skill/references/phylax-preflight-s4.md
- This kickoff: /Users/dubs/Projects/scholia.skill/prompts/r01-corpus-session-banter-kickoff.md

Trainer routes; you execute. Plan-first: this session touches >5 contract surfaces — emit a one-screen implementation plan, then proceed unless operator says proceed.

## Session bet

| Field | Value |
|-------|-------|
| Track | **R-01** — first operator corpus child `*.skill/` |
| Child slug | `banter` → `/Users/dubs/Projects/banter.skill/` |
| Research slug | `scholia-corpus-to-skill` (platform disambiguation only) |
| Output mode | **skill** (primary) — optional reference-library appendix |
| Stakes | **L3** — interpersonal advice; consent failures have real harm |
| Platform | Cursor IDE; fan-out depth ≤2 |
| Piranesi | **export-only** — no in-Cursor WebSearch/WebFetch unless operator says `waive-three-stage` + log reason |

## Domain scope (operator intent)

Build a corpus-backed skill for **ethical, consent-aligned** romantic/social communication:

1. **Pickup lines & openers** — specific lines, when they work/fail, construction patterns (not a script to override refusal)
2. **Flirty messaging** — text/DM tone, escalation ladders, repair after misread signals
3. **Ways of thinking** — frames from communication science (turn-taking, signaling, reciprocity, attachment-aware caution)
4. **Approaches** — context-dependent (venue, existing relationship vs stranger, group vs dyad)
5. **Body language** — granular, evidence-tagged (proxemics, gaze, posture, touch norms) with **consent-first** interpretation

**Out of scope (σ− — refuse to encode as tactics):**
- Coercion, persistence-after-no, isolation, intoxication leverage, workplace power abuse
- "PUA" patterns: negging, false time pressure, boundary testing, crowd manipulation
- Demographic stereotype scripts (race, looks scoring, "league" framing)
- Medical/clinical claims without peer-reviewed anchor
- Training-prior "rules" without ingest anchor

## Alethia consent mandates (load-bearing — non-negotiable)

Every generated artifact must treat these as **iron laws**, not footnotes:

| Mandate | Operational rule |
|---------|------------------|
| **Affirmative consent** | Interest must be clear and ongoing; ambiguity → pause, clarify, or exit — never "push through" |
| **Contextual consent** | Venue, relationship, power, sobriety, and group dynamics change what is appropriate |
| **Revocable** | "Yes" earlier ≠ "yes" now; teach graceful withdrawal for both parties |
| **Specificity** | Flirt ≠ consent to touch ≠ consent to leave together — do not collapse steps |
| **No scorekeeping** | Rejection is information, not failure; no retaliation or entitlement framing |
| **Truthfulness** | No deceptive identity, fake emergencies, or manufactured intimacy |
| **Vulnerable populations** | Extra caution + σ− when power imbalance (manager/report, teacher/student, large age gap) |

Tag consent claims in provenance with relation `quoted` or `compressed` from consent/communication primaries — never `[verified]` without Gate A/B on that session.

## Operator questions → LITERATURE_INDEX roles

Map each question to index rows before synthesis:

| Role ID | Operator question |
|---------|-------------------|
| Q-OP-01 | What line constructions open well vs read as creepy — and **why** (mechanism, not meme)? |
| Q-OP-02 | How should flirty texting escalate and **de-escalate** when signals are mixed? |
| Q-OP-03 | What mental models (reciprocity, signaling, turn-taking) predict success **without** ignoring consent? |
| Q-OP-04 | Body language: what can you **reliably** read vs what is folk psychology? |
| Q-OP-05 | How do consent norms from review literature constrain "pickup" advice? |
| Q-OP-06 | What should the skill **refuse** to recommend (alethia σ−)? |

## Corpus strategy

### Target layout

```
/Users/dubs/Projects/banter.skill/
  literature/
    pdfs/
    text/
    ingests/
    metadata/corpus_manifest.yaml
    index/LITERATURE_INDEX.md
  references/
    provenance.md
    alethia-consent-policy.md    # distill mandates + σ− for child skill
  scripts/
    verify_banter.sh             # wrapper → scholia verify on child root
  SKILL.md
```

### Seed corpus (minimum viable R-01 — 3 papers, paper fan-out)

Prior pilot slugs (re-ingest if missing on disk):

| Slug | Topic | Rationale |
|------|-------|-----------|
| `beres_2007_consent_review` | Consent review | Alethia anchor — defines ethical floor |
| `sprecher_2015_turn_taking` | Turn-taking / initiation | Messaging mechanics |
| `gersick_2014_covert_signaling` | Covert signaling | Flirt as low-cost signal; boundary-aware reading |

**Expand toward 5–8 PDFs** (still <5 or fan-out per paper if ≥5) from **Tier 1–2** only:

| Tier | Accept | Examples |
|------|--------|----------|
| T1 | Peer-reviewed meta/reviews, RCTs on communication | consent reviews, dyadic interaction studies |
| T2 | Peer-reviewed observational / survey with DOI | flirting signaling, nonverbal immediacy |
| T3 | Books with ISBN + operator summary ingest | only if T1/T2 sparse; tag `[inferred]` heavily |
| **Reject** | Pickup forums, Reddit compilations, anonymous blogs, affiliate "dating coach" PDFs | no ingest |

Operator drops PDFs with text layer into `literature/pdfs/`. Export text to `literature/text/{slug}.txt` before fan-out.

### Fan-out

- **≥3 peer-reviewed papers** → one sub-agent per paper (`literature-paper-ingest.md` schema)
- Parent scholia **must not** monolith-read PDF bodies at N≥5
- Each ingest ≤4500w; include **Methods/Results** coverage attestation (flag partial if skipped)

## Palamedes-level rigor (ingest + synthesis)

Per paper ingest, mandatory:

1. **Gate A** — title/authors/year/venue/DOI from PDF front matter
2. **Gate B** — every load-bearing finding traceable to section anchor in `literature/text/{slug}.txt`
3. **Epistemic tags** — `[verified]` only with Gate B in session; else `[inferred]` or `[preprint]`
4. **Contradiction surfacing** — if Paper A vs B disagree, row in provenance with `[CONTRADICTION]` → block synthesis until operator resolves
5. **Zero fabrication** — no citations not in corpus; no effect sizes without Results coverage
6. **SYNTHESIS.md** — cross-paper integration keyed to Q-OP-01…06; each bullet cites claim-id

Optional second track (not in-Cursor web): operator may run piranesi export for missing primaries → P8 ingest → fan-out.

## Child skill content requirements

Generate `SKILL.md` from child-skill-template **including sections 1–12**:

- **σ+** — triggers for ethical flirt coaching (practice, prep, debrief, consent checklists)
- **σ−** — alethia refusals + scholia negative-space
- **Workflow** — read signal → choose construction → deliver → check consent → adjust/exit
- **Evidence policy** — tags + "when folk advice contradicts literature"
- **Human gates** — stop when stakes L3+ ambiguity, intoxication, power imbalance
- **Audience** — adults seeking consent-aligned communication skills (not "pickup artist" optimization)

Heavy line libraries / body-language tables → `references/` (keep SKILL.md ≤500 lines).

## R-01 acceptance checklist (measure success — all must PASS or explicit WAIVED)

Write `/Users/dubs/Projects/banter.skill/R01_ACCEPTANCE.md` with PASS/FAIL/WAIVED per row:

| ID | Criterion | Evidence command / artifact |
|----|-----------|----------------------------|
| A-01 | Child root exists at `/Users/dubs/Projects/banter.skill/` | `test -d` |
| A-02 | `corpus_manifest.yaml` complete (legal_status, drm, language, epistemic_tag) | file read |
| A-03 | ≥3 paper ingests on disk, ≤4500w each | `wc -w literature/ingests/*_ingest.md` |
| A-04 | `LITERATURE_INDEX.md` maps Q-OP-01…06 to ingests | file read |
| A-05 | `SYNTHESIS.md` present; C-DG004 inputs with provenance | file read |
| A-06 | `references/provenance.md` — no path-only DOI rows (SF-06) | verify |
| A-07 | `references/alethia-consent-policy.md` distills mandates + σ− | file read |
| A-08 | SKILL.md σ+ / σ− non-empty; no absolute paths (SF-05) | verify |
| A-09 | `bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh /Users/dubs/Projects/banter.skill` exit 0 | run |
| A-10 | PS-02/SF-11: PDF count = ingest count OR documented WARN | verify output |
| A-11 | No load-bearing PUA/coercion tactics in SKILL or synthesis | trainer grep + human read |
| A-12 | Partial ingests flagged (Methods/Results gaps) in σ− or ingest attestation | file read |
| A-13 | Trainer review artifact written | `returns/trainer-reviews/banter-r01-YYYYMMDD.md` |
| A-14 | **R-02 handoff packet** emitted for phylax mode=full (fresh chat) | see below |

**Headline R-01 verdict** = worst row (any FAIL → R-01 open).

## Verification commands (run before claiming R-01 done)

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/verify_scholia.sh /Users/dubs/Projects/banter.skill
bash /Users/dubs/Projects/scholia.skill/scripts/check_cross_stage_consistency.sh /Users/dubs/Projects/banter.skill
python3 /Users/dubs/Projects/phylax.skill/scripts/audit_repo.py /Users/dubs/Projects/banter.skill --json
```

Do **not** claim R-02 (phylax semantic) complete in this session — emit handoff only.

## R-02 handoff packet (emit at end — fresh chat)

```yaml
handoff: scholia R-01 → phylax mode=full
child_path: /Users/dubs/Projects/banter.skill
recursion: context:fork — NOT same session as generation
checklist: /Users/dubs/Projects/scholia.skill/references/phylax-preflight-s4.md
consent_policy: /Users/dubs/Projects/banter.skill/references/alethia-consent-policy.md
acceptance: /Users/dubs/Projects/banter.skill/R01_ACCEPTANCE.md
stakes: L3
```

## Trainer review (required before "R-01 done")

Write:
`/Users/dubs/Projects/banter.skill/returns/trainer-reviews/banter-r01-YYYYMMDD.md`

Required sections:
- ### Bug inventory (P0–P4 or explicit none)
- ### Trainer notes (Program notes / Your form / Next session)

Fix all P0–P2 before closing R-01.

## Iron laws (session)

1. Amnesiac corpus — no training-prior pickup "rules" without ingest anchor
2. Monolith-read ban at N≥5 PDFs
3. Piranesi export-only in Cursor
4. Alethia mandates override "effectiveness" framing
5. Absolute paths only in operator tables; relative paths in child SKILL body

Begin: confirm PDFs on disk (or list missing), emit plan, then fan-out.
```

---

## Operator prep (before paste)

1. Create `/Users/dubs/Projects/banter.skill/` (or `cursor create_project` if greenfield).
2. Drop seed PDFs into `literature/pdfs/`; export text layers.
3. Optional: attach operator-authored **Alethia** policy doc if you have one beyond the mandates table above — agent merges into `references/alethia-consent-policy.md`.
4. New chat — paste kickoff block — attach PDF folder.

## Related paths

| File | Role |
|------|------|
| `/Users/dubs/Projects/scholia.skill/prompts/r01-corpus-session-banter-kickoff.md` | This packet |
| `/Users/dubs/Projects/scholia.skill/references/ROADMAP-remaining-tasks.md` | R-01 / R-02 definitions |
| `/Users/dubs/Projects/piranesi.skill/research-projects/0621-scholia-corpus/returns/trainer-reviews/scholia-banter-live-20260618.md` | Prior pilot review |
| `/Users/dubs/Projects/scholia.skill/references/corpus-manifest-template.yaml` | Manifest stub |

## Prior pilot note

A 2026-06-18 banter pilot ingested 3 papers (consent review, turn-taking, covert signaling). If `/Users/dubs/Projects/banter.skill/` is absent on disk, treat this session as **fresh R-01** using the same seed slugs.
