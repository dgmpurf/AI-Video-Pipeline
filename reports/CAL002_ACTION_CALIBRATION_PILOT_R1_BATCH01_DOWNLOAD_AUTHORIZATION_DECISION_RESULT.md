# CAL-002 Action Calibration Pilot R1 Batch 01 Download Authorization Decision

## Phase Summary

- Phase: `CAL002_ACTION_CALIBRATION_PILOT_R1_BATCH01_DOWNLOAD_AUTHORIZATION_DECISION_NO_LIVE`
- Task type: `no-live download authorization decision only`
- Repository checkpoint: `aa9c42401d5214cb1008057968e963331f90952e`
- Branch: `main`
- Batch: `CAL002-ACTION-CALIBRATION-PILOT-R1-BATCH-01`
- Decision: `DOWNLOAD_AUTHORIZATION_READY`
- Current download authority: `false`

This phase verifies three successful query results and defines a possible future bounded download contract. It does not call Dreamina or a provider and does not activate download authority.

## Bound Query Execution Result

- Report path: `reports/CAL002_ACTION_CALIBRATION_PILOT_R1_BATCH01_QUERY_EXECUTION_RESULT.md`
- Report SHA-256: `7b88853c6af85ca887c93a5ddd16b5c90678693e3b91084c1c5b7560526648d2`
- Report byte length: `5238`
- Report final state: `CAL002_BATCH01_THREE_QUERY_RESULTS_SUCCESS_READY_DOWNLOAD_AUTHORIZATION_DECISION`
- Report modified by this phase: `false`
- Report staged by this phase: `false`

The query execution report is a local evidence artifact bound by its full-file SHA-256. The commit boundary for this phase excludes it from staging.

## Bound Query Summary

- Path: `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/BATCH_01/execution_records/CAL002-BATCH01-LIVE-23C42E5/batch_query_execution_summary.json`
- SHA-256: `b36b16104a4a5faa73ebdb11dca3d3e83c4022ae5110612ac4d7512f99513109`
- Byte length: `3803`
- Query count: `3`
- All authorized query allowances consumed: `true`

## Verification Results

| Verification | Result | Evidence |
| --- | --- | --- |
| Three query successes exist | PASS | Three unique bound submit IDs returned successful query evidence. |
| Returned task identities match | PASS | Every returned submit ID matches its bound submit ID. |
| Generation status | PASS | Every task has `gen_status=success`. |
| Queue status | PASS | Every task has `queue_status=Finish`. |
| Video result count | PASS | Every task has exactly one video result. |
| Image result count | PASS | Every task has zero image results. |
| Query count | PASS | Exactly `3`; one query per submit ID. |
| Download count | PASS | `0`. |
| Retry count | PASS | `0`. |
| Resubmit count | PASS | `0`. |
| Signed URL persistence | PASS | URL presence is recorded, but signed URL values are not persisted. |
| Local media creation | PASS | No media file exists in the query evidence root. |

## Successful Task Bindings

### CAL002-A01_PUSH_REACTION

- submit_id: `fecedf69-8db9-4c68-83b4-858000d6fedc`
- gen_status: `success`
- queue_status: `Finish`
- result_images_count: `0`
- result_videos_count: `1`
- download_url_present: `true`
- download_called: `false`
- Parsed evidence SHA-256: `e9ebef02d7d00dbe48423343e9acd27ce4666678da79b9cfd4353010c2276f9b`

### CAL002-A04_IMPACT_STEP_BACK

- submit_id: `4ae37492-cc33-4afe-8d83-fd524a8010f0`
- gen_status: `success`
- queue_status: `Finish`
- result_images_count: `0`
- result_videos_count: `1`
- download_url_present: `true`
- download_called: `false`
- Parsed evidence SHA-256: `3d9c8168d6c0165b0f4bb38dc9e35db17786de1a356d8eedcab39df4961981cc`

### CAL002-A03_GRAB_PULL

- submit_id: `9929c159-88dd-473b-b547-ad98a13d8e5e`
- gen_status: `success`
- queue_status: `Finish`
- result_images_count: `0`
- result_videos_count: `1`
- download_url_present: `true`
- download_called: `false`
- Parsed evidence SHA-256: `9ce3a3efb8fc4a6f46309478a79f3a6f104f6db57abc94ee746f47126c181491`

## Decision

`DOWNLOAD_AUTHORIZATION_READY`

Meaning:

- The three exact successful submit IDs are eligible for a fresh human download authorization decision.
- This report does not authorize or perform any download.
- No current download allowance or exclusive download claim exists.
- Query authority is exhausted and no further query is authorized.

## Future Download Contract

Only after a fresh repository checkpoint and fresh explicit human authorization, a future phase may allow exactly:

1. One download for `fecedf69-8db9-4c68-83b4-858000d6fedc`.
2. One download for `4ae37492-cc33-4afe-8d83-fd524a8010f0`.
3. One download for `9929c159-88dd-473b-b547-ad98a13d8e5e`.

- Total future download maximum: `3`
- Per-submit-ID download maximum: `1`
- Download retries: `0`
- Overwrite permitted: `false`

Before every future download invocation, the execution phase must verify:

- Local HEAD is aligned with `origin/main` at the freshly authorized checkpoint.
- Human authorization binds the checkpoint and all three exact submit IDs.
- The bound query report, summary, and per-task parsed-result hashes remain unchanged.
- No prior download claim, download evidence, or destination media exists for the submit ID.
- A unique exclusive download claim is durably created before the provider call.
- The destination path is unique and cannot overwrite an existing file.
- The downloaded media identity, file type, size, checksum, and exact count are validated independently per experiment.
- Execution stops after the single download attempt for each submit ID regardless of outcome.

## Forbidden Future Actions

The future download phase must not perform:

- New submit.
- Query.
- Retry.
- Resubmit.
- Batch retry.
- More than one download for any submit ID.
- More than three total downloads.
- Prompt, package, parameter, reference-strategy, or manifest changes.
- Media overwrite.
- Final approval or lock.

## Current Non-Actions

- Dreamina called: `false`
- Provider called: `false`
- Query called: `false`
- Download called: `false`
- Retry called: `false`
- Resubmit called: `false`
- Media created: `false`
- Download claims created: `false`
- Download authority created: `false`
- Package/prompt/manifest modified: `false`
- CAL-001 modified: `false`
- `sources/` modified: `false`
- `final_master`: `false`
- `locked`: `false`

## Final Verdict

`COMPLETE`

`CAL002_BATCH01_DOWNLOAD_AUTHORIZATION_READY_FOR_FRESH_HUMAN_AUTHORIZATION`
