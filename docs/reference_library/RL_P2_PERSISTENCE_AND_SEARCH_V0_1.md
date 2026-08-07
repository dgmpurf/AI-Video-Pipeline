# RL-P2 Persistence and Search V0.1

## Status

RL-P2 is a derived, disposable read model over the validated RL-P0 immutable
catalog and the validated RL-P1 append-only event ledger. It is not a source of
truth and cannot append events, edit base records, infer rights, execute storage
work, approve production, set a final master, or lock an asset.

The initial implementation uses SQLite 3 with FTS5 `unicode61` plus a
versioned application-side CJK token stream. It performs complete validated
rebuilds only. Incremental mutation and automatic cleanup are outside V0.1.

## Identity

The closed logical registry is:

`RL_P2_LOGICAL_HASH_REGISTRY_V0_1R1`

It contains exactly 23 registered tables. Every table, included column, column
order, and row-order key is declared in `identity.py`. A missing, additional,
or renamed logical table or column fails verification.

The logical hash uses:

`STORED_LOGICAL_CONTENT_HASH_EXCLUDED_FROM_ITS_OWN_PREIMAGE`

The canonical preimage is compact UTF-8 JSON with no BOM or trailing newline.
It includes all registered logical rows in registry order. Within each table,
rows are sorted by the declared typed key: integers numerically and text by
UTF-8 binary order. Explicit SQL null is emitted as JSON null. Bounded JSON is
stored canonically.

`read_model_meta.logical_content_hash` is excluded only from its own preimage.
It remains mandatory stored metadata. Verification recomputes the preimage and
requires the recomputed value to equal the stored value, immutable filename,
and active pointer value.

One immutable generation filename is:

```text
rl_p2--<schema>--<full-generation-id>--sha256-<full-logical-hash>.sqlite3
```

Both IDs are full lowercase 64-character SHA-256 values. Generation identity
binds the builder contract and source identity, RL-P0 package and catalog
identity, RL-P1 ledger and projection identity, checkpoint identity, tokenizer
contract, and full-build mode. It excludes time, host, process, path, duration,
SQLite page layout, physical file hash, and other volatile operational facts.

## Schema and Authority Separation

The relational schema preserves:

- RL-P0 record, duty, artifact, storage, and rights fields;
- every accepted RL-P1 event with ledger/body/entry provenance;
- separate observation, score, proposal, human-decision, execution-receipt,
  relationship, rights-evidence, rights-decision, taxonomy, and checkpoint
  histories;
- current rights as a replay-derived exact facet;
- current and inactive search documents as separate FTS surfaces.

`UNKNOWN` is stored literally and remains distinct from SQL null, false, zero,
missing, denied, and lowest-ranked. Rights evidence does not create a rights
decision. Scores and storage proposals do not create human decisions. Human
decisions do not create execution receipts. Search relevance is labeled
`search_relevance` and never becomes an authority field.

## Tokenizer Contract

Tokenizer identity is:

`RL_P2_UNICODE61_CJK_BIGRAM_V0_1`

Original accepted text is preserved separately. The prepared representation:

1. applies Unicode NFKC;
2. applies Python Unicode case-folding and records the runtime Unicode version;
3. emits Latin letters, digits, and underscore as contiguous tokens;
4. emits overlapping CJK bigrams with a one-character fallback;
5. treats other punctuation and whitespace as boundaries;
6. removes duplicate tokens within one document by first occurrence;
7. omits a standalone governed `UNKNOWN` value from normal document tokens.

Plain-text query parsing uses the same preparation. Raw FTS syntax, boolean
operators, column selectors, prefix operators, nested quotes, empty text,
oversized text, and excessive term counts fail before MATCH execution. MATCH
values are always parameters.

The accepted BM25 weights are description 5, observation 3, taxonomy 2, duty
2, bounded notes 1, and prepared tokens 1. Ranking orders discovery only.

## Build Lifecycle

Every build and promotion requires a complete `RuntimeStateProtectionPolicy`.
It contains exactly one explicit absolute repository root, exactly one explicit
absolute Source root, and one or more explicit absolute media roots. Missing,
incomplete, empty, or relative protection context fails before the first
runtime-state write. The state root must itself be explicit and absolute, and
must be external to every protected root and descendant. Normalized,
case-aware resolved containment rejects equal paths, descendants, and apparent
external paths that traverse symlinks, junctions, or Windows reparse points.
There is no repository-relative, Source-relative, user-profile, machine-global,
or unprotected fallback.

A build:

1. acquires an exclusive state-root lock;
2. creates one deterministic sibling `.partial.sqlite3` candidate without
   overwrite;
3. proves FTS5, `unicode61`, parameterized MATCH, and BM25 availability;
4. creates the closed schema and constraints;
5. inserts all mapped logical rows and both FTS indexes;
6. computes and stores the cycle-safe logical hash;
7. closes and reopens the candidate read-only;
8. checks SQLite integrity, foreign keys, registry identity, logical hash, and
   FTS row/content parity;
9. renames without overwrite to the immutable full-hash filename;
10. reopens and verifies the final generation again.

A failed or interrupted build is never promoted. Failure evidence may remain
as a lock or partial candidate; cleanup is a separately authorized operation.
Old immutable generations are never deleted automatically.

## Pointer Promotion and Windows Readers

The active pointer is canonical UTF-8 JSON with exactly one terminal LF and
schema `RL_P2_CURRENT_POINTER_V0_1R1`. It binds the complete generation
filename, hashes, RL-P0 identity, RL-P1 prefix/projection identity, and
checkpoint.

Promotion verifies the candidate first, writes one exclusive same-directory
temporary pointer, flushes it, and atomically creates or replaces the final
pointer. It then reads the final pointer back and reopens the named immutable
generation. Existing Windows readers keep their old immutable file handle;
new readers resolve only the verified pointer. A failed replacement leaves the
prior pointer intact. Timestamp-based generation discovery is forbidden.

## Verification States

Only `VALID_CURRENT_GENERATION` is available to normal queries.

- `STALE_GENERATION`: internally valid and compatible, but behind a requested
  longer ledger tail.
- `INCOMPATIBLE_GENERATION`: unsupported schema, registry, builder, tokenizer,
  or divergent upstream identity.
- `CORRUPT_OR_TAMPERED_GENERATION`: integrity, registry, stored/recomputed
  hash, filename, pointer, foreign-key, or FTS parity failure.

The normal reader pins one verified immutable generation for its lifetime.
There is no fallback to an older or newer file by modification time.

## Query and Pagination

Exact/faceted queries use typed allowlisted filters for RL-P0 identity/content,
duties, artifact status, taxonomy, storage, and effective rights. SQL values
are parameterized. Named sorts end in binary `pilot_clip_id`; keyset cursors
bind the generation and canonical request hash.

FTS current and history modes are separate. Results order by ascending BM25
`search_relevance`, then binary pilot ID, document kind, and document ID. FTS
uses a bounded offset cursor pinned to one generation and request hash. It does
not claim keyset pagination.

Every result envelope contains the query contract and request hash, immutable
generation and logical identity, RL-P0 and RL-P1 provenance, freshness verdict,
normalized filters, declared sort, rows, and cursor. Cursor mismatch, generation
change, unknown fields exposed through typed constructors, or unsupported sort
fails closed.

## Deterministic Exports

JSON uses UTF-8, sorted keys, compact separators, no BOM, and exactly one
terminal LF. JSONL contains one canonical provenance-bearing object per result
row with no blank lines. Export manifests bind contract version, request hash,
generation identity, sort contract, row count, byte count, and SHA-256.

Equivalent logical rebuilds produce the same logical hash and deterministic
query/export bytes. Physical SQLite bytes are not required to match.

## CLI Boundary

The isolated module entry point is:

```text
python -m app.ai_video_pipeline.reference_library.persistent_index <command>
```

Commands are `build`, `verify`, `promote`, `facet`, `search`, and `export`.
Paths are explicit. Unknown arguments fail. The write-capable `build` and
`promote` commands require `--repository-root` exactly once, `--source-root`
exactly once, and `--media-root` one or more times. These role-specific roots
form the same mandatory policy used by the library API; no generic empty list
can bypass it. Build writes only a new immutable generation under the supplied
external state root. Promotion writes only the pointer after verification.
Query/export are read-only and write results only to stdout. No cleanup command
is included in this bounded implementation.

## Recovery and Operator Receipt

Operators should retain, outside authoritative sources:

- exact RL-P0 and RL-P1 input identities;
- builder source identity and tokenizer/runtime identity;
- generation filename, generation ID, and logical hash;
- verification state and diagnostics;
- promotion pointer before/after identity;
- query request hash, generation identity, and deterministic export manifest;
- any retained lock, partial candidate, or failed pointer temporary path.

Recovery means rebuilding from validated RL-P0 and RL-P1 into a new immutable
generation, then promoting it after complete verification. It never means
repairing the only database in place, treating RL-P2 as authoritative,
silently weakening FTS behavior, or deleting old generations without separate
authority.
