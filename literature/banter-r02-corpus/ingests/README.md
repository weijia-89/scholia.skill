# Ingest SSOT pointer — do not fan-out here

Chapter ingests (577) and PDFs live in the **aletheia consumer corpus**, not in this scholia mirror tree.

**SSOT:** `/Users/dubs/Projects/aletheia.skill/research/scholia/banter-r02-corpus/literature/ingests/`

Scholia session work: read SSOT ingests (aletheia path) → write/update cards at aletheia `literature/metadata/practical_cards/{topic_slug}.yaml` → run `sync_banter_r02_practical_cards_mirror.sh` → verify scholia mirror.

See `/Users/dubs/Projects/scholia.skill/literature/banter-r02-corpus/CONSUMER_MIRROR.md`.
