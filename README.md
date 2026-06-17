# AI_VIDEO_PIPELINE

This repository is a clean, test-first Python skeleton for an AI video production pipeline.
It implements:

- Path policy enforcement
- Domain data models and enums
- Manifest parsing and validation
- Dreamina CLI command building (dry-run safe)
- Media integrity checks
- Internal workspace staging
- Dry-run and mock-run execution plans
- Pytest coverage for Phase A behavior

No external staging, live execution, submit/query/download, or deletion is performed in
Phase A.

## Quick start

- Install dependencies (only stdlib is required for the implemented scope).
- Run tests:

```bash
python -m pytest -q
```

## Directory layout

See the repository tree in the task request for full structure.
