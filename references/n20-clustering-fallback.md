# N>20 PDF clustering fallback (open decision)

META: S3 §8 · deferred v0.2 · design stub v0.3

## ELI15

Fan-out = one helper per paper. At **20+ PDFs** that’s a traffic jam. **Clustering** = group similar papers, fewer helpers, each helper covers a cluster.

## Trigger

| PDF count | Default routing |
|-----------|-----------------|
| 1–2 | Direct / minimal fan-out |
| 3–19 | One ingest sub-agent per paper (depth cap 2) |
| **20+** | **Cluster fallback** (this doc) — operator confirm in manifest |

## Proposed algorithm (untested)

1. Extract title + first-page keywords from each PDF text layer (or manifest metadata).
2. Embed or BM25 cluster into K groups where K = min(ceil(N/5), 8).
3. Spawn one palamedes fan-out per cluster (not per paper).
4. SYNTHESIS merges cluster ingests with cluster-id tags in provenance.

## Manifest flag

```yaml
# corpus_manifest.yaml
fan_out_mode: per-paper   # default
# fan_out_mode: cluster   # when N>20 and operator sets
cluster_target: 5         # papers per cluster (approx)
```

## Falsifiers

- Cluster merge loses paper-level provenance anchors.
- Quality drops vs per-paper fan-out on heterogeneous corpora.

## Status

**OPEN** — implement when operator first ships N>20 corpus. See `/Users/dubs/Projects/scholia.skill/references/s4-open-decisions.md`.
