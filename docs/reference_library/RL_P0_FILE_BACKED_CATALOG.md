# RL-P0 File-Backed Reference Catalog

RL-P0 provides a deterministic, read-only catalog over the bound normalization
candidate ZIP. It validates the package identity, internal checksums, thirty
records, controlled vocabularies, record arithmetic, and fixed pilot totals
before exposing any record.

## Scope

The implementation loads the ZIP into memory without extracting it. It does
not read media, calculate media hashes, open originals, create a database,
access a Provider or network, modify Project Source, or persist catalog state.
Input records are represented by immutable JSON-backed objects. Returned
dictionaries are defensive copies.

`UNKNOWN` is a governed value. The validator checks all 198 unsupported legacy
slots and rejects a package if any of them is replaced by zero, false, an empty
value, or an inferred value. Technical status, artifact availability,
lifecycle, proposals, rights, duplicate status, and human gates remain separate
fields.

`narrative_reference` remains an extension. Its sole record retains
`TAXONOMY_DECISION_REQUIRED`; RL-P0 does not decide that taxonomy.

## Python API

```python
from app.ai_video_pipeline.reference_library import (
    ReferenceCatalog,
    ReferenceQuery,
)

catalog = ReferenceCatalog.from_package("path/to/candidate.zip")
record = catalog.get("G01D-CLIP-005")
action_records = catalog.query(
    ReferenceQuery(content_families=("action",))
)
summary = catalog.summary()
```

Queries support deterministic filtering by pilot ID, primary content family,
content scope, reference duty, technical validation status, artifact
availability, artifact lifecycle, and taxonomy status. Results default to
pilot-ID order.

## Command Line

```text
python -m app.ai_video_pipeline.reference_library \
  --package <candidate.zip> validate

python -m app.ai_video_pipeline.reference_library \
  --package <candidate.zip> summary

python -m app.ai_video_pipeline.reference_library \
  --package <candidate.zip> show G01D-CLIP-005

python -m app.ai_video_pipeline.reference_library \
  --package <candidate.zip> export-jsonl --content-family action
```

All commands write deterministic UTF-8 JSON or JSONL to stdout. There is no
catalog output path. Media, database, Provider, Source-write, repository-write,
replay, and destructive CLI options are rejected.

## Deliberate Non-Goals

RL-P0 does not implement SQLite, FTS, a GUI, event storage, projections,
replay, duplicate resolution, media inspection, taxonomy decisions, or any
production/final/lock action. Those remain outside this bounded phase.
