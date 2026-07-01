# Rename table (historical → current layout)

**Current layout (2026-06-27):**

| Role | Path |
| ---- | ---- |
| ChatPRD upload (one per source) | `attachments/{NN}_{slug}_ATTACH.txt` |
| Full export (not uploaded) | `source_exports/{NN}_{slug}.txt` |
| Prompt (paste, not attach) | `prompts/{NN}_{slug}_ingest.md` |

Regenerate uploads after export changes:

```bash
bash /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/export_text.sh
```

**Legacy paths removed:** `attach_packs/`, `attachments/*_slice.txt`, bare `attachments/*.txt` (moved to `source_exports/`).
