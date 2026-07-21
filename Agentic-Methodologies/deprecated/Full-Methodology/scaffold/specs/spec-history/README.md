# Specification History

Store a complete snapshot for every accepted spec version.

Recommended format:

```text
spec-history/
|-- README.md
`-- YYYY-MM-DD-vNNNN-short-title/
    |-- README.md
    `-- <copies of all current spec files, excluding spec-history/>
```

The snapshot directory's `README.md` should record:

- version;
- acceptance date;
- reason for the version;
- previous version;
- source planning discussion or task, if applicable;
- notable added, changed, or removed intent.

Snapshots are historical records. The live current specs remain directly under
`specs/`.

Normally, the live specs are identical in meaning to the latest accepted
snapshot. Do not read that snapshot during routine spec work merely to duplicate
the live context. Read a historical snapshot when it is necessary to establish
the last accepted baseline, recover interrupted work, understand removed or
materially changed intent, or inspect relevant historical rationale.
