# CAL-002 Batch05 Phase 1 Query Execution Result

## 1. Exact approval and integrity

Exact approval text:

```text
APPROVE_CAL002_BATCH05_PHASE1_EIGHT_EXCLUSIVE_QUERY_RESULT_CALLS_V0_1__BIND_LIVE_SUBMIT_EXECUTION_CHECKPOINT_3ABF7128057749FC1976234D6AC15ECBD713E37F__BIND_LIVE_SUBMIT_EXECUTION_REPORT_SHA256_7CC03C19E446F16B8B645755426AA52D1C53FDB580384456DA604588F617B9B2__BIND_EXECUTION_ID_CAL002_BATCH05_LIVE_2874895E__BIND_SUBMIT_01_F3663D7F_33DC_4937_B6E1_20C6BE10A0D8__BIND_SUBMIT_02_03A03B27_1E3D_48E7_9122_7FDAEA7DF0D1__BIND_SUBMIT_03_866311E6_BE9B_4850_A798_9E74D4A3BCE9__BIND_SUBMIT_04_B506BD61_3B16_4F5C_9209_4DFC49356284__BIND_SUBMIT_05_01193507_CB12_4116_AEC4_9084063A61D9__BIND_SUBMIT_06_924B3F58_D0BB_43B4_80E7_A45BE940CE06__BIND_SUBMIT_07_7453C063_E5D8_49AA_83F7_D4F8E8136697__BIND_SUBMIT_08_DC64226B_D9DD_4D79_BBA4_6BD16F5FA465__AUTHORIZE_FIXED_WINDOWS_CLI_C_USERS_MSJPURF_BIN_DREAMINA_EXE__AUTHORIZE_ONE_VERSION_AND_ONE_QUERY_RESULT_HELP_CANARY__AUTHORIZE_EXACTLY_ONE_QUERY_RESULT_CALL_FOR_EACH_OF_8_BOUND_SUBMIT_IDS_IN_CENTRAL_PHASE1_ORDER__QUERY_ONLY_WITHOUT_DOWNLOAD_DIR__SANITIZE_SIGNED_URLS_CREDENTIALS_AND_RAW_PROVIDER_STREAMS__RECORD_ONLY_BOUND_PARSED_STATUS_LOG_QUEUE_MEDIA_COUNT_AND_RESULT_HASH_EVIDENCE__STOP_ON_RUNTIME_DRIFT_DIRTY_STATE_BINDING_MISMATCH_QUERY_FAILURE_AMBIGUOUS_RESPONSE_OR_SENSITIVE_DATA_EXPOSURE__NO_SECOND_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_NEW_SUBMIT_NO_BATCH_NO_USER_CREDIT_NO_LOGIN_NO_SESSION_OPERATION_NO_MEDIA_NO_REVIEW_NO_SOURCE_CHANGE_NO_PRODUCTION_APPROVAL_NO_FIXED_TASK_COMPLETION_NO_FINAL_MASTER_NO_LOCK__ONE_TIME_NON_REUSABLE
```

- Approval SHA-256: `4083321c8cc1e712c021dab774a7edc26bb159b405c992df01b2c94ee5bcd7f9`
- Goal identity: `CAL002_BATCH05_PHASE1_EIGHT_EXCLUSIVE_QUERY_RESULT_CALLS_V0_1`
- Authorization ID: `CAL002-BATCH05-QUERY-AUTH-4083321C`
- Query execution ID: `CAL002-BATCH05-QUERY-4083321C`

## 2. Authorization lifecycle

- Approval received: `true`
- Approval activated immediately before the first Dreamina canary: `true`
- Approval consumed: `true`
- Approval reusable: `false`
- Authority exhausted at Goal termination: `true`
- Automatic resume authorized: `false`

## 3. Starting checkpoint and submit-evidence binding

- Branch: `main`
- Starting HEAD: `3abf7128057749fc1976234d6ac15ecbd713e37f`
- Starting origin/main: `3abf7128057749fc1976234d6ac15ecbd713e37f`
- HEAD/origin aligned: `true`
- Submit execution checkpoint: `3abf7128057749fc1976234d6ac15ecbd713e37f`
- Prior execution ID: `CAL002-BATCH05-LIVE-2874895E`
- Submit report: `reports/CAL002_BATCH05_PHASE1_LIVE_SUBMIT_EXECUTION_RESULT.md`
- Submit report bytes: `6424`
- Submit report SHA-256: `7cc03c19e446f16b8b645755426aa52d1c53fdb580384456da604588f617b9b2`
- Prior execution-root files equal HEAD: `true`
- Prior evidence-manifest mismatch count: `0`
- No prior query record found for the eight submit IDs: `true`
- Sources clean: `true`

## 4. Exact task and submit-ID bindings

1. `CAL002-B05-PUSH-CONTROL-R01` -> `f3663d7f-33dc-4937-b6e1-20c6be10a0d8`
2. `CAL002-B05-PUSH-CONTROL-R02` -> `03a03b27-1e3d-48e7-9122-7fdaea7df0d1`
3. `CAL002-B05-PUSH-CANDIDATE-R01` -> `866311e6-be9b-4850-a798-9e74d4a3bce9`
4. `CAL002-B05-PUSH-CANDIDATE-R02` -> `b506bd61-3b16-4f5c-9209-4dfc49356284`
5. `CAL002-B05-IMPACT-CONTROL-R01` -> `01193507-cb12-4116-aec4-9084063a61d9`
6. `CAL002-B05-IMPACT-CONTROL-R02` -> `924b3f58-d0bb-43b4-80e7-a45be940ce06`
7. `CAL002-B05-IMPACT-CANDIDATE-R01` -> `7453c063-e5d8-49aa-83f7-d4f8e8136697`
8. `CAL002-B05-IMPACT-CANDIDATE-R02` -> `dc64226b-d9dd-4d79-bba4-6bd16f5fa465`

All eight task IDs and submit IDs were unique and remained in the authorized central order.

## 5. Runtime canaries

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Version calls: `1`
- Version result: `PASS`
- Version stdout bytes / SHA-256: `96` / `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`
- Version stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Version: `2a20fff-dirty`
- Commit: `2a20fff`
- Build time: `2026-06-26T06:36:39Z`
- query_result help calls: `1`
- query_result help result: `PASS`
- `--submit_id` supported: `true`
- `--download_dir` optional and omitted: `true`
- Query-only behavior without download path: `true`

## 6. Per-task query results

| Seq | Task ID | Submit ID | Bound submit log ID | Query-returned log ID | gen_status | Queue | Images | Videos | Results | Downloadable | Classification |
|---:|---|---|---|---|---|---|---:|---:|---:|---|---|
| 1 | `CAL002-B05-PUSH-CONTROL-R01` | `f3663d7f-33dc-4937-b6e1-20c6be10a0d8` | `20260724222712169254047008608C0AF` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 2 | `CAL002-B05-PUSH-CONTROL-R02` | `03a03b27-1e3d-48e7-9122-7fdaea7df0d1` | `20260724222716169254047008641F06C` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 3 | `CAL002-B05-PUSH-CANDIDATE-R01` | `866311e6-be9b-4850-a798-9e74d4a3bce9` | `2026072422272016925404700850102A4` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 4 | `CAL002-B05-PUSH-CANDIDATE-R02` | `b506bd61-3b16-4f5c-9209-4dfc49356284` | `20260724222724169254047008374C2B0` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 5 | `CAL002-B05-IMPACT-CONTROL-R01` | `01193507-cb12-4116-aec4-9084063a61d9` | `20260724222728169254047008225F961` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 6 | `CAL002-B05-IMPACT-CONTROL-R02` | `924b3f58-d0bb-43b4-80e7-a45be940ce06` | `2026072422273216925404700819478A5` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 7 | `CAL002-B05-IMPACT-CANDIDATE-R01` | `7453c063-e5d8-49aa-83f7-d4f8e8136697` | `20260724222736169254047008649C3C4` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |
| 8 | `CAL002-B05-IMPACT-CANDIDATE-R02` | `dc64226b-d9dd-4d79-bba4-6bd16f5fa465` | `202607242227401692540470085943AE2` | `not returned` | `success` | `Finish` | 0 | 1 | 1 | true | `terminal_success` |

The query response did not return a separate log ID; the bound submit-receipt log ID is shown for traceability. No signed URL is included.

## 7. Query accounting

- Planned query count: `8`
- Query maximum: `8`
- Query commands attempted: `8`
- Query responses parsed: `8`
- Query commands failed: `0`
- Unqueried tasks: `0`
- Query count per submit ID: `1`
- Second-query calls: `0`

## 8. Outcome subsets

- Terminal-success tasks: `8`
- Terminal-failure tasks: `0`
- Nonterminal tasks: `0`
- Downloadable-result tasks: `8`
- Each terminal-success task reports at least one video: `true`

A successfully parsed query alone does not prove generation success. Here, the Provider separately returned `gen_status=success` for all eight tasks. Visual success, production approval, and fixed-task completion remain unreviewed and are not claimed.

## 9. Sanitization

- Signed URLs detected: `8`
- Signed URLs persisted: `false`
- Credentials detected: `false`
- Raw query stdout persisted: `false`
- Raw query stderr persisted: `false`
- Sanitization result: `PASS`
- Only raw-stream byte lengths and SHA-256 digests were retained.

## 10. Explicit non-actions

- Download calls: `0`
- Retry calls: `0`
- Resubmit calls: `0`
- New-submit calls: `0`
- Batch calls: `0`
- user_credit calls: `0`
- Login/checklogin/logout/relogin calls: `0`
- Session operations: `0`
- Media created: `false`
- Review artifacts created: `false`
- Sources changed: `false`

## 11. Stop reason and remainder

- Stop reason: `none`
- Unqueried task IDs: `[]`
- Fresh authorization required for an unqueried or nonterminal subset: `false`

## 12. Terminal authority state

- submit_authorized: `false`
- query_authorized: `false`
- download_authorized: `false`
- retry_authorized: `false`
- resubmit_authorized: `false`
- batch_authorized: `false`
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## 13. Final decision

- Decision: `CAL002_BATCH05_PHASE1_QUERY_SWEEP_COMPLETE_READY_FOR_DOWNLOAD_AUTHORIZATION_DECISION`
- Next phase: `CAL002_BATCH05_PHASE1_DOWNLOAD_AUTHORIZATION_DECISION`
- This result creates no download authority. A fresh human authorization is required before any download.
