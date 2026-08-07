# Reference Library Event Ledger V0.2 Overlay

The V0.2 event ledger is an additive overlay rooted in one validated immutable
V0.1 checkpoint and projection. It does not rewrite V0.1 data.

## Closed vocabulary

The overlay accepts exactly twelve event types. Their aggregate and authority
classes are defined by `event_ledger.v2.registry`; unknown event types,
authority substitutions, payload keys, and incompatible cross-references fail
closed.

Every event preserves the V0.1 base binding. Events that depend on current
V0.2 state also bind an accepted V0.2 checkpoint and projection hash. Ledger
entries are append-only canonical JSONL with deterministic IDs and hashes.

## E1 cluster boundary

Cluster membership and cluster confirmation never create, upgrade, or infer a
pair relation. An all-pair cluster basis requires complete exact coverage of
every unordered member pair by current human ACCEPT decisions. An explicit
cluster-level decision remains cluster-scoped and has no pair-support rows.

## F1 representative boundary

A representative decision binds the exact current, active, unsuperseded and
unretracted proposal event and body. Snapshot, role, members, candidates,
proposed member, policy, checkpoint, and projection must all agree. Execution
also requires a current active unrevoked human ACCEPT decision and valid
per-member rights, lifecycle, availability, and pinned snapshot references.
Historical proposal or decision existence is never sufficient.

Proposal retraction and supersession preserve history. `REVOKE` is a human
decision state, not a proposal state.

## Safety

The overlay creates no media, Provider, production, migration, or Source
operation. It is consumed by derived read models only after full validation.
