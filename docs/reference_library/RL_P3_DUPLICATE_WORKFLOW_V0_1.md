# Reference Library Duplicate Workflow Read Model V0.1

RL-P3 is a separate immutable, disposable, and rebuildable SQLite read model.
It materializes governed duplicate evidence, pair history, immutable cluster
snapshots, cluster confirmations, representative workflow history, and
execution receipts from validated RL-P1 V0.1/V0.2 state.

## Identity and schema

The physical schema is the exact closed 15-table registry. V0.1 has no FTS,
trigger, migration, or authority-producing table. Canonical JSON columns,
declared binary row ordering, the full logical export, logical hash, generation
ID, immutable filename, and canonical pointer are independently verifiable.
The `logical_content_hash` column is excluded from its own preimage.

An RL-P2 generation may be included only as independently verified pinned
context. Search similarity is not duplicate evidence and cannot become a
human decision.

## Build and promotion

Persistent writes require a complete policy with explicit absolute repository,
Source, and media roots. State roots equal to or below a protected boundary,
or traversing links/reparse points, are rejected before attributable output.

Builds use one exclusive lock and deterministic partial database. Promotion
occurs only after integrity, foreign-key, closed-registry, logical-hash,
filename, and independent read-only checks pass. The pointer uses canonical
UTF-8 JSON with exactly one terminal LF and atomic replacement. There is no
latest-by-time fallback or automatic generation deletion.

## Query authority

Pair queries read `pair_relation_history` only; cluster membership cannot fill
missing pair state. Representative execution eligibility is recomputed from
current proposal and decision history with exact body, snapshot, role,
member/candidate, policy, checkpoint/projection, rights, lifecycle, and
availability bindings. Execution rows are receipts only.

`UNKNOWN` remains explicit. Rights and provenance remain per member. Exports
retain authority classes and source traces.

## Scope

This implementation selects no production state root, performs no migration,
touches no real media, and changes no existing RL-P0, RL-P1 V0.1, RL-P2, CLI,
or Project Source file. Synthetic stores exist only under pytest temporary
directories.
