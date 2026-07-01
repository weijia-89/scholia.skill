# banter-r02-corpus — scholia mirror (consumer SSOT: aletheia)

**Status:** mirror synced 2026-06-26 · session close  
**Scholia path:** `/Users/dubs/Projects/scholia.skill/literature/banter-r02-corpus/`  
**Consumer SSOT (ingests + runtime):** `/Users/dubs/Projects/aletheia.skill/research/scholia/banter-r02-corpus/`

## What lives here

| Artifact | Mirror | SSOT |
|----------|--------|------|
| `metadata/practical_cards/*.yaml` | **copied** (17 pillar cards) | aletheia same path under `literature/` |
| `metadata/corpus_manifest.yaml` | slim mirror manifest | aletheia `literature/metadata/corpus_manifest.yaml` |
| Chapter ingests (577) | **pointer only** — `ingests/README.md` | aletheia `literature/ingests/` |
| Aletheia runtime loader | — | `/Users/dubs/Projects/aletheia.skill/scripts/harness/load_practical_card.py` |

## Resync cards after scholia extract

```bash
bash /Users/dubs/Projects/scholia.skill/scripts/sync_banter_r02_practical_cards_mirror.sh
bash /Users/dubs/Projects/scholia.skill/scripts/verify_practical_cards.sh \
  /Users/dubs/Projects/scholia.skill/literature/banter-r02-corpus
```

## Pillar canon

`/Users/dubs/Projects/piranesi.skill/research-projects/0626-r02-foundational-guidance/r02-foundational-guidance-pillars.md` (all `scholia_wired`)

## Do not

- Re-extract procedures in aletheia without scholia card pass
- Treat mirror ingests folder as populated — it is a pointer only
