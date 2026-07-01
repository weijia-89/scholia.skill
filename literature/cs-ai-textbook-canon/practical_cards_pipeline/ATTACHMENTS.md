# Attachments — phase 2 practical cards

**Project:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/`

## ChatPRD external (primary — deai-operator-corpus pattern)

| Folder | File pattern | Operator action |
|--------|--------------|-----------------|
| `attachments/` | `{slug}_ch{NN}_ATTACH.txt` | **Upload 1 file** to ChatPRD |
| `prompts/chatprd/` | `{slug}_ch{NN}_card_ingest.md` | **Paste only** (do not upload) |
| `chatprd_returns/` | `{slug}_ch{NN}_cards.yaml` | Save ChatPRD output here → merge to `../metadata/practical_cards/` |

**Operator table:** `/Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/references/chatprd-operator-table.md`

Regenerate all attach packs + prompts:

```bash
bash /Users/dubs/Projects/scholia.skill/literature/cs-ai-textbook-canon/practical_cards_pipeline/scripts/refresh_pipeline.sh
```

## Cursor subagent (alternate)

| Folder | Purpose |
|--------|---------|
| `attachments/*_SLICE.txt` | Optional disk read for Task subagents |
| `prompts/dispatch/*_card_extract.md` | Paste into Cursor subagent |

## Iron laws (ChatPRD external)

- **≤8 uploads per ChatPRD window** — one self-contained `*_ATTACH.txt` per chapter (piranesi + deai)
- **Paste prompt only** — prompts live under `prompts/chatprd/`, not in upload folder
- **No README** in attach/upload folders (`operator-path-output` iron law)
- **Scholia σ−** — no invented procedures; no send-ready scripts in cards

## Piranesi sibling

Architecture + S4 canon: `/Users/dubs/Projects/piranesi.skill/research-projects/0628-scholia-practical-ingest/phase2-cs-ai/INDEX.md`
