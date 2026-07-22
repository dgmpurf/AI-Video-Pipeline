# CAL002 Batch02 Download Authorization Decision Result

## Phase Summary

- Phase: `CAL002_BATCH02_DOWNLOAD_AUTHORIZATION_DECISION_NO_LIVE`
- Task type: `no-live download authorization decision only`
- Repository checkpoint: `32ddd4bf5ef89010f5b0216a548ed35c3fabc22a`
- Branch: `main`
- Batch: `CAL002-ACTION-CALIBRATION-BATCH02-STRUCTURE-ONLY`
- Decision: `DOWNLOAD_AUTHORIZATION_READY`
- Current download authority: `false`

This phase verifies that four successful Batch02 provider outputs are eligible for a later bounded download authorization. It does not call Dreamina or a provider and does not activate download authority.

## Bound Query Result

- Report path: `reports/CAL002_BATCH02_QUERY_EXECUTION_RESULT.md`
- Report SHA-256: `d906b8a76c10e40e9415d830564a23f4f7554da7ae09c075300836ad156951ad`
- Report byte length: `5580`
- Report verdict: `CAL002_BATCH02_FOUR_QUERIES_SUCCESS_READY_DOWNLOAD_AUTHORIZATION_DECISION`
- Report modified by this phase: `false`
- Report staged by this phase: `false`

The query result report is a local evidence artifact and is bound here by its full-file SHA-256. The commit boundary for this decision excludes that report and all execution evidence.

## Bound Query Summary

- Path: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH02_EXECUTION/execution_records/CAL002-BATCH02-LIVE-181E6FB/batch_query_execution_summary.json`
- SHA-256: `037be2657bb40bdb6616e40f49f218810b03609ce3b8411f3f144b418360444e`
- Byte length: `11497`
- Strict canonical JSON validation: `passed`
- Internal evidence-reference validation: `passed`
- Signed URL values persisted: `false`

## Verification Results

| Verification | Result | Evidence |
| --- | --- | --- |
| Four successful query results | PASS | All four records have `gen_status=success`. |
| Queue completion | PASS | All four records have `queue_status=Finish`. |
| Submit-ID binding | PASS | All four package-to-submit-ID pairs match the execution evidence. |
| Result video count | PASS | Exactly one video per submit ID; four total. |
| Download URL presence | PASS | Present for all four tasks; values were not persisted. |
| Query count | PASS | Exactly `4`; all query allowances are consumed. |
| Download count | PASS | `0`. |
| Retry count | PASS | `0`. |
| Resubmit count | PASS | `0`. |
| Existing download claim/evidence count | PASS | `0`; this decision creates none. |
| Local media created | PASS | `false`. |

## Successful Task Bindings

### CAL002-B02-A01_PUSH_STRUCTURE_CONTROL

- submit_id: `d7761386-f6b8-428b-ba7c-4246b364a732`
- gen_status: `success`
- queue_status: `Finish`
- result_videos_count: `1`
- download_url_present: `true`
- prior download count: `0`

### CAL002-B02-A01_PUSH_STRUCTURE_CANDIDATE

- submit_id: `6c85d71e-381c-41d1-a505-b0038810de74`
- gen_status: `success`
- queue_status: `Finish`
- result_videos_count: `1`
- download_url_present: `true`
- prior download count: `0`

### CAL002-B02-A04_IMPACT_STRUCTURE_CONTROL

- submit_id: `95ad749c-3307-4ad6-a61f-f9c50d77d0d6`
- gen_status: `success`
- queue_status: `Finish`
- result_videos_count: `1`
- download_url_present: `true`
- prior download count: `0`

### CAL002-B02-A04_IMPACT_STRUCTURE_CANDIDATE

- submit_id: `8f125727-7829-4cb2-b974-731e53cfc731`
- gen_status: `success`
- queue_status: `Finish`
- result_videos_count: `1`
- download_url_present: `true`
- prior download count: `0`

## Decision

`DOWNLOAD_AUTHORIZATION_READY`

Meaning:

- The four exact successful submit IDs are eligible for fresh human download authorization.
- This report does not itself authorize or perform a download.
- No current download allowance or download claim exists.
- Provider success does not constitute local media validation or visual approval.

## Future Download Contract

Only after a fresh repository checkpoint and fresh explicit human authorization, a future phase may allow exactly:

1. One download for `d7761386-f6b8-428b-ba7c-4246b364a732`.
2. One download for `6c85d71e-381c-41d1-a505-b0038810de74`.
3. One download for `95ad749c-3307-4ad6-a61f-f9c50d77d0d6`.
4. One download for `8f125727-7829-4cb2-b974-731e53cfc731`.

- Total future download maximum: `4`
- Per-submit-ID download maximum: `1`
- Download retries: `0`
- Overwrite permitted: `false`

Each download allowance is consumed by its single invocation regardless of outcome. A failed, timed-out, malformed, or technically invalid download does not create retry authority.

## Mandatory Future Preconditions

Before every download invocation, the future phase must verify:

- A fresh checkpoint with local `HEAD` aligned to `origin/main`.
- Fresh explicit human authorization bound to that checkpoint and all four exact submit IDs.
- The bound query report and query-summary hashes remain unchanged.
- The sanitized query evidence still records `success`, `Finish`, one video, and URL presence for the submit ID.
- No prior download claim, download evidence, or target media path exists for the submit ID.
- A unique exclusive download claim is created before the provider call.
- A new isolated target directory is selected with no-overwrite enforcement.
- Independent sanitized command and response evidence is created for the task.
- The downloaded file receives exact byte length, SHA-256, container, stream, resolution, duration, frame-rate, and full-decode validation.

Any failed precondition must stop before the affected provider download.

## Required Technical Media Validation

A future download is not complete until the resulting file passes:

- Exactly one downloaded video file for the submit ID.
- Non-zero byte length and stable SHA-256 after final placement.
- MP4-compatible container validation.
- Exactly one decodable video stream.
- Expected `1280x720` dimensions for the bound `720p` generation.
- Positive duration and frame count.
- Duration and frame rate within documented tolerance.
- Full decode with no fatal error.
- No overwrite, duplicate target, or cross-package filename collision.

Technical validation does not establish visual success or final approval.

## Forbidden Future Actions

The future download phase must not perform:

- New or additional submit.
- Query.
- Retry.
- Resubmit.
- Batch retry.
- More than one download for any submit ID.
- More than four total downloads.
- Prompt, package, manifest, provider-parameter, reference-strategy, or identity change.
- Final approval, final-master state, or lock state.

## Current Non-Actions

- Dreamina called: `false`
- Provider called: `false`
- Query called: `false`
- Download called: `false`
- Retry called: `false`
- Resubmit called: `false`
- New submit called: `false`
- Media created: `false`
- Download claims created: `false`
- Provider artifacts created: `false`
- Batch/package/prompt/manifest modified: `false`
- CAL-001 modified: `false`
- Sources modified: `false`
- final_master: `false`
- locked: `false`

## Final Verdict

`COMPLETE`

`CAL002_BATCH02_DOWNLOAD_AUTHORIZATION_READY_FOR_FRESH_HUMAN_AUTHORIZATION`

The four successful tasks are ready for a separately authorized one-download-per-submit-ID phase. No download authority exists now.
