# STATUS — deai operator corpus (ChatPRD delegation)

**Updated:** 2026-06-27 23:00 UTC · **Sources:** 13 · **Done:** 0 · **Pending:** 13

**Manifest:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/manifest.yaml`
**Upload folder:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/` (one `_ATTACH.txt` per source)
**Full exports:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/source_exports/` (not uploaded)
**ChatPRD returns:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/`
**Granola returns:** `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/granola_returns/`

## Pipeline

| Step | Command |
| ---- | ------- |
| Export + rebuild uploads | `bash /Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/scripts/export_text.sh` |
| ChatPRD ingest | Opus 4.6 · attach one `attachments/NN_slug_ATTACH.txt` + paste prompt |
| Save return | `chatprd_returns/{slug}_YYYYMMDD_ingest.md` |

## Source tracker

| Status | Text | Slug | Lane | Upload file |
| ------ | ---- | ---- | ---- | ----------- |
| ⬜ pending | ✓ | `corpus_3375627` | both | `attachments/01_corpus_3375627_ATTACH.txt` |
| ⬜ pending | ✓ | `olmstead_2011_elements_writing_craft` | both | `attachments/10_olmstead_2011_elements_writing_craft_ATTACH.txt` |
| ⬜ pending | ✓ | `baker_2020_prof_writing_speaking` | tic_enrichment | `attachments/05_baker_2020_prof_writing_speaking_ATTACH.txt` |
| ⬜ pending | ✓ | `locker_2012_prof_writing_w231` | tic_enrichment | `attachments/06_locker_2012_prof_writing_w231_ATTACH.txt` |
| ⬜ pending | ✓ | `peeples_2003_prof_writing_rhetoric` | both | `attachments/07_peeples_2003_prof_writing_rhetoric_ATTACH.txt` |
| ⬜ pending | ✓ | `terk_prof_writing_skills` | tic_enrichment | `attachments/08_terk_prof_writing_skills_ATTACH.txt` |
| ⬜ pending | ✓ | `long_2018_portable_mentor` | both | `attachments/11_long_2018_portable_mentor_ATTACH.txt` |
| ⬜ pending | ✓ | `munier_2016_writers_guide_beginnings` | both | `attachments/12_munier_2016_writers_guide_beginnings_ATTACH.txt` |
| ⬜ pending | ✓ | `ginna_what_editors_do` | both | `attachments/13_ginna_what_editors_do_ATTACH.txt` |
| ⬜ pending | ✓ | `henry_2000_writing_workplace` | both | `attachments/09_henry_2000_writing_workplace_ATTACH.txt` |
| ⬜ pending | ✓ | `jones_2015_jslw` | both | `attachments/02_jones_2015_jslw_ATTACH.txt` |
| ⬜ pending | ✓ | `s00146_2024_ai_writing` | deai_removal | `attachments/03_s00146_2024_ai_writing_ATTACH.txt` |
| ⬜ pending | ✓ | `s40979_2024_ai_writing` | deai_removal | `attachments/04_s40979_2024_ai_writing_ATTACH.txt` |

## Next action

1. ChatPRD (Opus 4.6): attach `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/attachments/01_corpus_3375627_ATTACH.txt`
2. Paste `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/01_corpus_3375627_ingest.md`
3. Save to `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/chatprd_returns/corpus_3375627_YYYYMMDD_ingest.md`

