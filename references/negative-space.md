# Negative space — scholia refusals

Mandatory **refuse** (do not ingest / do not generate skills):

- PHI / HIPAA-regulated clinical records without BAA
- ITAR / EAR controlled technical data
- Explicit no-AI / no-TDM publisher licenses
- Proprietary source code corpora without license

**Operator-warning** (proceed with flags — not mechanically verified):

- `legal_status: unknown` in corpus_manifest
- Untagged preprints on load-bearing clinical claims
- Non-English corpus without translation provenance
- Copy-restricted or unreadable PDFs — set `drm: hard|unreadable` in manifest; operator decides whether to skip or extract via `literature/text/`

Mechanical verify does **not** inspect DRM. Operator documents decision in manifest + session log.

## Piranesi export-only (PS-10)

**Refuse** in-Cursor piranesi web research (`WebSearch`, `WebFetch`) unless operator explicitly says `waive-three-stage` and logs reason to `localonly/piranesi-waive-log.txt`:

```
date: YYYY-MM-DD
operator: <name>
reason: <one line>
waive-three-stage: acknowledged
```

Without waive log: route to **piranesi export** (`export_piranesi_packets.sh`) — ChatPRD web only.

No automatic fan-out→scholia→piranesi escalation (W03 kill register).
