# RL-P1 Event Ledger

RL-P1 is an additive, append-only event ledger over the validated RL-P0
file-backed catalog. It does not replace or modify RL-P0 records, schemas,
vocabularies, packages, or CLI behavior. Projected records are separate
overlay objects.

## Authority boundary

The registry contains exactly fourteen event types and binds each type to one
authority class:

- observations, relationship assertions, rights evidence, and taxonomy
  bindings use `OBSERVATION_ONLY`;
- scores and storage proposals use `MODEL_PROPOSAL`;
- human and rights decisions use `HUMAN_DECISION`;
- execution audits use `EXTERNAL_EXECUTION_RECEIPT`;
- checkpoints use `SYSTEM_PROJECTION`.

Observation does not become proposal automatically. Proposal does not become
decision automatically. Decision does not prove execution. An execution
receipt does not rewrite the decision that authorized it. Projection creates
no authority.

Default rights come from the immutable RL-P0 record:

```text
rights_provenance = purchased_unverified_license
active_generation_input_allowed = false
publication_allowed = UNKNOWN
```

Rights evidence alone cannot change these values. A rights transition requires
a `RIGHTS_DECISION_RECORDED` event with human-decision authority and exact
rights-evidence event bindings. Scores, taxonomy state, proxy tiers, and
storage proposals cannot enable generation, publication, redistribution,
commercial use, or training rights.

## Canonical identity

Canonical JSON is strict UTF-8 without BOM, with recursively sorted object
keys, compact separators, and preserved Unicode. Event identity is calculated
from the canonical event draft bytes without a terminal LF:

```text
event_body_hash = lowercase SHA-256
event_id = RL-EVT- + uppercase first 24 hexadecimal characters
```

Every read verifies the complete body hash as well as the shortened ID. An
exact duplicate is rejected as `DUPLICATE_EVENT_ID`. A matching prefix with a
different full hash or body is rejected as
`EVENT_ID_COLLISION_OR_TAMPER`.

The four identity arrays in an event draft must already be lexicographically
sorted and unique. The implementation never inserts current time, generates a
UUID, normalizes Unicode, coerces a numeric value, or silently reorders an
identity array.

## Ledger files

One ledger directory contains only:

```text
ledger_manifest.json
events.jsonl
events.jsonl.lock  # present only while one append invocation owns the lock
```

The manifest binds the RL-P0 package filename, bytes, SHA-256, record count,
record schema version, exact accepted RL-P0 commit
`1b86aae6ff08d74ce2993ef92721c9ef585854f8`, and deterministic base-catalog
hash. The commit is also part of the base-catalog hash input and checkpoint
base identity. Its ledger ID is derived from the canonical manifest body
excluding `ledger_id`. The manifest is created exclusively and is immutable.

The adapter owns canonical JSON byte snapshots of every base record and the
validation summary. Public record, map, and validation accessors return
detached values, so caller mutation cannot change the bytes consumed by replay
or make projection diverge from the bound base-catalog hash.

Each JSONL entry contains:

```text
ledger_schema_version
ledger_id
ledger_position
previous_entry_hash
event
entry_hash
```

The genesis previous hash is 64 lowercase zeroes. Entry hashes cover the
canonical wrapper excluding `entry_hash`. Every entry line has exactly one LF.
Malformed UTF-8, a partial tail, missing final LF, noncanonical JSON, duplicate
or skipped position, broken previous hash, incorrect entry hash, duplicate
event, and unknown schema or event type are hard failures.

## Append durability

The authoritative append sequence is:

1. Validate manifest and base-catalog identity.
2. Exclusively create the sibling `events.jsonl.lock`.
3. While holding the lock, validate the complete existing ledger and replay.
4. Validate the event, authority, payload, transitions, and preconditions.
5. Reject duplicates or collisions without writing.
6. Construct one next entry.
7. Open `events.jsonl` with a writable binary append descriptor.
8. Complete-write the canonical entry plus one LF.
9. Flush and fsync the writable descriptor.
10. Close the descriptor while retaining the lock.
11. Reopen the ledger read-only and revalidate the complete chain and tail.
12. Release only the lock owned by this invocation.

A stale lock, partial tail, or complete entry left by an interrupted call is
evidence. No stale-lock deletion, truncation, replacement, tail repair, or
automatic retry is performed.

## Projection and checkpoints

Replay starts from thirty immutable RL-P0 records and dispatches entries in
ascending position to one reducer each. The overlay separately retains review
observations, score proposals, storage proposals, human decisions, execution
receipts, relationship assertions, rights evidence and decisions, taxonomy
bindings, and checkpoints. Correction, supersession, and retraction preserve
prior history and mark prior facts inactive from the later position forward.

Projection hashes are SHA-256 over canonical projection JSON without a final
LF. Replay can stop at an exact position, entry hash, or accepted checkpoint
ID without editing the ledger.

`SCORE_RECORD_SUPERSEDED`, `STORAGE_PROPOSAL_SUPERSEDED`, and
`RELATIONSHIP_ASSERTION_RETRACTED` remain in history as inactive transition
rows. They deactivate the compatible prior fact but never become a new active
score, open proposal, or relationship assertion. Checkpoint counts include
only active domain facts and exclude these transition rows.

`CHECKPOINT_CREATED` summarizes the validated prefix immediately before the
checkpoint event. Its payload binds the prefix identity, projection hash,
base-catalog identity, record and event counts, technical failures, current
proxy and segment counts and bytes, UNKNOWN counts, rights distribution, open
proposals, human decisions, execution receipts, media-operation count, and
validation errors. Verification rebuilds that prefix and compares the entire
payload.

## CLI

The isolated entry point is:

```text
python -m app.ai_video_pipeline.reference_library.event_ledger
```

Read-only commands are `validate-ledger`, `replay`, `show-event`,
`list-events`, `show-projection`, `list-projections`, `summary`,
`verify-checkpoint`, `export-events-json`, `export-events-jsonl`, and
`export-projection-json`.

`init-ledger` and `append-event` are write-capable. They require explicit
absolute ledger and base-package paths. Write targets inside a Git repository,
worktree, or the project `reference_library` runtime directory are refused.
The CLI never interprets payloads as commands and provides no media, database,
network, Provider, Source, repository-mutation, destructive, final, or lock
operation.

## Scope

RL-P1 is local infrastructure for durable evidence history and deterministic
read-only replay. It does not authorize media access, proxy or segment
creation, source hashing, database work, Provider calls, network access,
repository integration, production approval, final master, or governance
lock.
