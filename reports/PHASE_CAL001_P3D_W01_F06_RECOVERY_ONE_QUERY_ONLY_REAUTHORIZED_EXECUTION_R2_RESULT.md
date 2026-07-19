# PHASE CAL-001-P3D-W01 F06 Recovery One-Query-Only Reauthorized Execution R2 Result

## 1. Phase summary

- phase_id: `CAL-001-P3D-W01_F06_RECOVERY_ONE_QUERY_ONLY_REAUTHORIZED_EXECUTION_R2`
- program_id: `CAL-001`
- macro_id: `CAL-001A`
- wave_id: `W01`
- experiment_id: `CAL001-F06-P1-R1`
- recorded_at: `2026-07-19T15:32:41.022662Z`
- executed: true
- status: `provider_success_download_not_authorized`
- decision: `ready`
- starting_head: `c65aa2865619d64354ef703d4c5ea2b70f420b9a`
- query invocation count: 1
- download invocation count: 0
- final_master: false
- locked: false

## 2. Corrected canonical authorization

The exact R2 canonical text was the sole authorization source. The incorrect Base64 preserved in the blocked R1 report was not reused.

- authorization type: `corrected_encoding_reauthorization`
- bound starting checkpoint: `c65aa2865619d64354ef703d4c5ea2b70f420b9a`
- authorized submit_id: `f40d2e79-ba98-4873-b92d-539ccc35d2ee`
- encoding: UTF-8
- BOM: false
- CR/LF: absent
- trailing newline: false
- byte length: 432
- SHA-256: `0f4306d42084ab96044eea5a89d338e0cf1e41c31e39d8df85b25a15626fe883`
- locally generated Base64 length: 576
- locally generated Base64 matched the independent cross-check: true
- locally generated Base64 decode count: 1
- decoded bytes matched original bytes: true
- decoded SHA-256 matched: true
- last byte hexadecimal: `2E`
- authorization_verified: true

Authorization record:

`experiments/CAL-001/authorizations/CAL001_P3D_W01_F06_recovery_one_query_only_reauthorization_R2.json`

## 3. Repository and Source preflight

- repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- branch: `main`
- local HEAD before live execution: `c65aa2865619d64354ef703d4c5ea2b70f420b9a`
- origin/main before live execution: `c65aa2865619d64354ef703d4c5ea2b70f420b9a`
- checkpoint binding matched: true
- HEAD/origin aligned: true
- staged files before phase: 0
- tracked modifications before phase: 0
- sources clean: true
- sources touched: false
- existing unrelated untracked noise left untouched: true

## 4. Prior blocked R1 preservation

- prior report: `reports/PHASE_CAL001_P3D_W01_F06_RECOVERY_ONE_QUERY_ONLY_RESULT.md`
- prior report SHA-256: `a84e08ec4c46eccc896f65b6494e5fbca756b5f43037f4956d5b17660317ee62`
- prior report Git blob SHA: `639cfc7bcca4b1e8bf793b7c609994f0883ab070`
- prior blocked commit: `c65aa2865619d64354ef703d4c5ea2b70f420b9a`
- required R1 fact checks passed: 14/14
- R1 query invocation count: 0
- R1 Dreamina invocation count: 0
- R1 query authority carried forward: false
- prior incorrect Base64 reused: false
- prior report modified by R2: false

The blocked R1 authorization check did not count as a provider query.

## 5. Provider task and old-handle binding

The committed recovery-submit records passed 24 binding and quarantine assertions.

- new submit_id: `f40d2e79-ba98-4873-b92d-539ccc35d2ee`
- submit invocation occurred: true
- submit attempt count: 1
- provider task created: true
- provider task creation proven: true
- created task count: 1
- creation classification: `confirmed_created_nonterminal`
- prior gen_status: `querying`
- prior actual query count for the new submit ID: 0
- prior actual download count for the new submit ID: 0
- provider credit count: 70
- pre-submit balance: 5695
- post-submit balance: 5625
- prior credit delta: 70
- prior credit reconciliation verified: true

Old handle:

- submit_id: `cabfa6ab-cc61-4d29-8630-da01dfdeef65`
- state: `orphaned_after_upload_transport_failure`
- provider task created/proven: false/false
- created task count: 0
- quarantined: true
- query recovery eligible: false
- download eligible: false
- reuse/query/download authorized: false/false/false
- confirmed credit cost: null
- credit classification: `credit_consumption_unresolved`
- old-handle live calls in R2: 0

## 6. Evidence wrapper and Dreamina canary

- atomic evidence wrapper: `app/ai_video_pipeline/execution/dreamina_evidence.py`
- wrapper SHA-256: `0da551983fce49f59fa0f880b93d1a80b07a192d94631acded2e9654ac7b15d4`
- bounded wrapper tests: 25 passed, 0 failed
- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- executable SHA-256: `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- version: `2a20fff-dirty`
- commit: `2a20fff`
- build time: `2026-06-26T06:36:39Z`
- version invocation count: 1
- user_credit invocation count: 1
- query_result help invocation count: 1
- authenticated account confirmed: true
- private account identifiers redacted before evidence persistence: true
- informational credit balance: 5625
- generation-submit balance gate applied: false
- logger Access denied: false
- authentication failure: false
- query command contract valid: true
- hidden polling introduced: false

Two local inline-script parse failures occurred before subprocess entry: one before the canary commands and one before the query. Both failed during Python parsing, created no Dreamina subprocess, created no query reservation, consumed no provider-query count, and did not consume query authority.

## 7. Exact one-query execution

The only provider-query command executed was:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id f40d2e79-ba98-4873-b92d-539ccc35d2ee
```

- query invocation occurred: true
- query invocation count: 1
- query loop: false
- polling: false
- second query: false
- `--download_dir` present: false
- output/download/save option present: false
- queried submit_id matched authorization: true
- sanitized subprocess envelope persisted before semantic interpretation: true

## 8. Provider response

- subprocess exit code: 0
- returned submit_id matched: true
- gen_status: `success`
- queue_status: `Finish`
- fail_reason present: false
- logid present in query response: false
- provider credit count: 70
- result structure present: true
- images_count: 0
- videos_count: 1
- outputs_count: 1
- expected_result_shape_matched: true
- download_url_present: true
- signed_url_count: 1
- query_outcome: `provider_success_download_not_authorized`

Nonsensitive video metadata returned with the successful result:

- fps: 24
- width: 1280
- height: 720
- format: mp4
- duration: 5.042 seconds

## 9. Sanitization and media boundary

- full signed URL persisted: false
- raw HTTP URL persisted in R2 evidence: false
- signed URL values replaced with `<redacted_url>`: true
- authentication tokens/cookies/session secrets persisted: false
- private account identifier persisted: false
- media downloaded: false
- media created: false
- media inspected: false
- media metadata extracted from a local file: false
- frames/contact sheets created: false
- visual scoring performed: false

Provider success and URL presence did not activate download authority.

## 10. Query-authority closure

Authority was closed immediately after the single query returned:

- query_count: 1
- query_count_max: 1
- query_authorized_after: false
- query_authority_active_after: false
- execution_authority_active_after: false
- download_authorized: false
- retry_authorized: false
- resubmit_authorized: false
- second_query_authorized: false
- second_recovery_submit_authorized: false
- F07_authorized: false
- W02_plus_authorized: false
- CAL001B_authorized: false
- final_master: false
- locked: false

## 11. State and repository writes

The mutable execution-state contract was updated only to record the actual R2 query outcome and closed authority.

- recovery query count: 1
- remaining-task query counter: 15
- recovery task state: `recovery_query_success_download_not_authorized`
- next action: `CAL-001-P3D-W01_F06_RECOVERY_DOWNLOAD_AUTHORIZATION_DECISION`
- initial wave plan changed: false
- fixed manifest changed: false
- Prompt/package/fixture/inventory changed: false
- datasets modified: false
- sources modified: false
- prior R1 report modified: false

## 12. Explicit non-actions

- download: false
- query_result with download directory: false
- retry: false
- resubmit: false
- second query: false
- second recovery submit: false
- old-handle query/download: false
- F07: false
- W02 or later task: false
- other CAL-001 generation task: false
- batch: false
- media creation/retrieval: false
- Source modification: false
- final or lock: false

## 13. Recommended next phase

`CAL-001-P3D-W01_F06_RECOVERY_DOWNLOAD_AUTHORIZATION_DECISION`

A separate human decision is required before one download-only action. This R2 Goal does not authorize download, media inspection, review artifacts, another query, retry, resubmit, F07, final, or lock.

## 14. Final verdict

`CAL001_P3D_W01_F06_RECOVERY_QUERY_R2_SUCCESS_AUTHORITY_CLOSED_READY_DOWNLOAD_AUTHORIZATION_DECISION`
