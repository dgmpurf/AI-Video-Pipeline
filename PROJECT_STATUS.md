# AI_VIDEO_PIPELINE Project Status

## Phase A (Current)

### Completed
- ✅ Project skeleton created under `app/ai_video_pipeline`
- ✅ `configs/` added:
  - `path_policy.json`
  - `providers.json`
  - `runtime_defaults.json`
- ✅ Path policy implementation:
  - workspace-only path checks for writes/reads/copy/rename
  - no delete operations
- ✅ Core enums and dataclasses
- ✅ Manifest CSV parser/validator
- ✅ Dreamina CLI command builder (argv only, no execution)
- ✅ Media integrity checker and staging utilities
- ✅ Dry-run execution producing:
  - `provider_requests.jsonl`
  - `command_preview.csv`
- ✅ Mock-run execution producing:
  - `submitted.csv`
  - `completed.csv`
  - `downloaded.csv`
- ✅ Unit tests for required behavior

### Deferred (by design, not in scope for Phase A)
- ❌ Live execution / submit / query / download orchestration
- ❌ Real provider adapters beyond command building
- ❌ Long-form script/story expansion, scene planning, visual bible workflows
- ❌ External staging or migration tooling
