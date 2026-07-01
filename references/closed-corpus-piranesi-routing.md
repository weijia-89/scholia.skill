# Closed-corpus + piranesi routing (gap #9)

META: v0.3 policy stub · operator session bets override

## ELI15

Some PDF piles are **private** (NDA, employer-internal, unreleased). Piranesi means “do research in ChatPRD/Granola, not web in Cursor.” For closed corpora you still need a rule for **when export is OK**.

## Routing matrix

| Corpus class | In-Cursor ingest | Piranesi export | Web in Cursor |
|--------------|------------------|-----------------|---------------|
| Open access papers | ✅ | ✅ optional | ❌ unless `waive-three-stage` |
| Institutional license (personal copy) | ✅ | ✅ with operator attest | ❌ unless waived |
| NDA / employer confidential | ✅ local only | ⚠️ operator attest only | ❌ |
| Unknown legal_status | ✅ ingest | ❌ block export | ❌ |

## Operator attest (required for closed + export)

Log in session or `corpus_manifest.yaml` comment:

```yaml
# closed_corpus_attest: operator-name YYYY-MM-DD — export approved for S4 reconcile only
```

## Waive logging

If operator says `waive-three-stage` for in-Cursor web: log in daily notes — piranesi iron law exception for that session only.

## Related

- `/Users/dubs/Projects/scholia.skill/references/negative-space.md`
- `/Users/dubs/Projects/scholia.skill/SKILL.md` piranesi export-only section
- PS-10 pressure oracle (export-only guard)

**Status:** DOC shipped v0.3 stub — not a mechanical verify gate.
