# Chapter ingest — Understanding Distributed Systems (2e) · Chapter 20

| Field | Value |
|-------|-------|
| slug | understanding_distributed_systems_2022 |
| source_type | textbook |
| pdf_path | [not in corpus; operator: literature/cs-ai-textbook-canon/pdfs/understanding_distributed_systems_2022.pdf] |
| text_path | /Users/dubs/Projects/scholia.skill//Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/text/understanding_distributed_systems_2022.txt |
| ingest_path | /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/ingests/understanding_distributed_systems_2022_ch20_ingest.md |
| text_lines_read | 6193–6375 |
| wrong_file_flag | false |

---

## Bibliographic metadata

| Field | Value |
|-------|-------|
| parent_book_title | Understanding Distributed Systems |
| authors | Roberto Vitillo |
| edition | Version 2.0.0 (March 2022) |
| ISBN_print | [not found in text export] |
| ISBN_electronic | [not found in text export] |
| publisher | Self-published (Roberto Vitillo) |
| chapter_number | 20 |
| chapter_title | Caching |
| part | Part III — Scalability |
| page_range | [not present in text export; operator: confirm from PDF TOC] |

---

## Scope

Application/data caching: hit ratio, side vs inline cache, LRU/TTL, invalidation difficulty, local vs external (Redis/Memcached), thundering herd, consistent-hash rebalance, cache-down cascade.

---

## Key findings

All claims below are **[verified from text]** unless tagged `[contested]` or `[inferred]`.

1. **Fundamentals** (6198–6227): Cache buffers origin; higher stack = more savings; origin must survive cache loss.
2. **Policies** (6231–6271): Side vs inline; LRU eviction; TTL staleness trade-off; serve expired if origin down; invalidation impractical → TTL.
3. **Local cache** (6274–6310): Duplication; thundering herd on cold start; request coalescing per key.
4. **External cache** (6314–6375): Redis/Memcached shared; partition+replicate; consistent hashing rebalance; cache down may cascade — local fallback + shedding.

---

## Section digest (anchored)

### §20.1 Policies (6231–6271)

Side/inline, LRU, TTL.

### §20.2 Local (6274–6310)

Figure 20.1 thundering herd.

### §20.3 External (6314–6375)

Figure 20.2 Redis cluster.


---

## Pedagogy

### Learning objectives

After this chapter, a reader should be able to:

1. Distinguish side vs inline cache.
2. Mitigate thundering herd.
3. Plan cache rebalance.
4. Design cache-down degradation.

### worked_examples_present

**Y** — Redis/Memcached managed services; hot-key scenario.

### exercise_hooks

No end-of-chapter exercises in source. Operator-derivable hooks:

1. **TTL stale-serve:** SLA when origin down.
2. **Singleflight:** Coalesce hot key fetches.
3. **Cache-down:** Fallback + shedding plan.

---

## Coverage attestation

| Section | Status | Text anchor |
|---------|--------|-------------|
| §20.1 | Read | 6231–6271 |
| §20.2 | Read | 6274–6310 |
| §20.3 | Read | 6314–6375 |

**Attestation:** Single-file read of `understanding_distributed_systems_2022.txt` lines 6193–6375 only.

---

## Operator hooks

### 1. w2_systems_llm (Part III — Scalability)

DB read optimization after ch19; stacks ch14 HTTP + ch15 CDN.

### 2. MDCalc alignment

**[peripheral]** — No clinical content; HA/scale patterns port indirectly to regulated services.

### 3. Redundancy

| Canon title | Overlap |
|-------------|---------|
| **DDIA 2e** | Medium — caching chapter |

### 4. Scholia fit

- **Worked examples:** Y (policy + failure modes).

---

## TEXTBOOK-Q1 quality gate

| Criterion | Result | Notes |
|-----------|--------|-------|
| Edition currency | **PASS** | v2.0.0 March 2022 |
| Author authority | **PASS** | Practitioner (Mozilla data platform, Microsoft SaaS) |
| Citation density | **PASS** | Primary papers and vendor docs in footnotes |
| Contested claims flagged | **PASS** | See table |
| Worked examples | **PASS** | Failure mode emphasis |

### Contested or oversimplified claims

| Claim | Text anchor | Flag |
|-------|-------------|------|
| Cache is optimization not proof of scale | 6218–6227 | Origin must stand alone |

**TEXTBOOK-Q1 verdict:** **PASS**

---

## Cross-references (forward pointers)

| Reference | Topic |
|-----------|-------|
| Part IV ch28 | Load shedding |

---

## Provenance notes

- Claims trace to lines 6193–6375 of `understanding_distributed_systems_2022.txt`.
- `[inferred]` used for cross-canon redundancy judgments.
- Part III scalability arc: Cruder narrative thread (Ch.14–23).

---

## Glossary (chapter-local)

| Term | Definition per chapter |
|------|------------------------|
| Thundering herd | Simultaneous cache miss spike |
| Request coalescing | One in-flight fetch per key |
