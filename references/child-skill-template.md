# Child skill template (scholia-generated)

Canonical ordering for compaction survival (S3b C-DG003). Copy to generated `*.skill/SKILL.md`.

## Frontmatter (required)

```yaml
---
name: {slug}
description: |
  {≤1024 chars; comprehensive trigger phrases — SkillRouter 31–44pp drop without body}
version: 0.1.0
generated_by: scholia
corpus_session: {YYYY-MM-DD}
pairs_with: []  # body-text convention; document peers only
---
```

## Body sections (order fixed)

1. **Iron laws** — amnesiac corpus; provenance anchors; no training-prior load-bearing claims
2. **When to use (σ+)** — triggers
3. **When NOT to use (σ−)** — negative boundaries (mandatory)
4. **Workflow** — operator steps
5. **Constraints** — corpus paths, caps, platform
6. **Evidence policy** — tags: [verified] [user-asserted] [inferred] [RECENCY RISK]
7. **Verification** — run child verify + phylax before ship
8. **References** — pointer to `references/provenance.md` (include **relation** column per TROVE — see `references/provenance-template.md`)

Defer optional sections below when generating v0.2-style minimal children; include for v0.3+ polish.

9. **Permissions** — what the skill may read/write (corpus paths only; no network unless operator enables)
10. **Human gates** — when to stop and ask (stakes L3+, ambiguous corpus, DRM unknown)
11. **Handoff** — downstream consumers (palamedes output mode, notebooklm-prep, operator review)
12. **Audience** — who the generated skill is for (exam prep, job domain, internal research)

## Cursor portable subset (C-DG008)

Keep SKILL.md ≤500 lines; heavy templates live in `references/`.
