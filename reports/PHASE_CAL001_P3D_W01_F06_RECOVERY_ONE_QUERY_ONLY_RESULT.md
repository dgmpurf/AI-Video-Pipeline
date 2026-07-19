# PHASE CAL-001-P3D-W01 F06 Recovery One-Query-Only Result

## 1. Phase summary

- phase_id: `CAL-001-P3D-W01_F06_RECOVERY_ONE_QUERY_ONLY`
- program_id: `CAL-001`
- macro_id: `CAL-001A`
- wave_id: `W01`
- experiment_id: `CAL001-F06-P1-R1`
- recorded_at: `2026-07-19T15:09:18.408Z`
- executed: true
- query_execution_started: false
- status: `blocked_before_any_dreamina_command`
- decision: `safe_block`
- starting_head: `7e7356131b86874e99a6904267a43a5d7c23feb6`
- stop_condition_triggered: true
- stop_condition_reason: `canonical_authorization_base64_does_not_match_canonical_text_and_declared_sha256`

## 2. Repository and Source preflight

- repository_path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- branch: `main`
- local_HEAD: `7e7356131b86874e99a6904267a43a5d7c23feb6`
- origin/main: `7e7356131b86874e99a6904267a43a5d7c23feb6`
- required starting checkpoint matched: true
- local HEAD and origin/main aligned: true
- staged files before phase: 0
- unrelated tracked modifications before phase: 0
- sources clean: true
- sources touched: false
- existing unrelated untracked workspace noise left untouched: true

## 3. Canonical authorization evidence

The supplied canonical authorization text was:

```text
APPROVE_CAL001_F06_RECOVERY_ONE_QUERY_ONLY_BIND_STARTING_HEAD_7E7356131B86874E99A6904267A43A5D7C23FEB6_BIND_NEW_SUBMIT_ID_F40D2E79_BA98_4873_B92D_539CCC35D2EE_AUTHORIZE_EXACTLY_ONE_QUERY_RESULT_WITHOUT_DOWNLOAD_DIR_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_SECOND_QUERY_NO_F07_PRESERVE_OLD_HANDLE_QUARANTINE_ALLOW_BOUNDED_TEXT_EVIDENCE_COMMIT_AND_PUSH_CLOSE_QUERY_AUTHORITY_AFTER_ONE_QUERY_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

The supplied Base64 value was:

```text
QVBQUk9WRV9DQUwwMDFfRjA2X1JFQ09WRVJZX09ORV9RVUVSWV9PTkxZX0JJTkRfU1RBUlRJTkdfSEVBRF83RTczNTYxMzFCODY4NzRFOTlBNjkwNDI2N0E0M0E1RDdDMjNGRUI2X0JJTkRfTkVXX1NVQk1JVF9JRF9GNDBEMkU3OV9CQTk4XzQ4NzNfQjkyRF81MzlDQ0MzNUQyRUVFQVVUSE9SSVpFX0VYQUNUTFlfT05FX1FVRVJZX1JFU1VMVF9XSVRIT1VUX0RPV05MT0FEX0RJUl9OT19ET1dOTE9BRF9OT19SRVRSWV9OT19SRVNVQk1JVF9OT19TRUNPTkRfUVVFUllfTk9fRjA3X1BSRVNFUlZFX09MRF9IQU5ETEVfUVVBUkFOVElORV9BTExPV19CT1VOREVEX1RFWFRfRVZJREVOQ0VfQ09NTUlUX0FORF9QVVNIX0NMT1NFX1FVRVJZX0FVVEhPUklUWV9BRlRFUl9PTkVfUVVFUllfRklOQUxfTUFTVEVSX0ZBTFNFX0xPQ0tFRF9GQUxTRS4=
```

Verification results:

| Check | Expected | Observed | Pass |
| --- | --- | --- | --- |
| authoritative Base64 decode count | 1 | 1 | true |
| canonical UTF-8 byte length | 416 | 416 | true |
| canonical text SHA-256 | `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3` | `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3` | true |
| decoded Base64 byte length | 416 | 416 | true |
| decoded Base64 SHA-256 | `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3` | `f5eb16120e865791f0444a8f0e45cf85aedf141d8f1334c7795196bfb5704b11` | false |
| decoded text equals canonical text exactly | true | false | false |
| canonical text re-encodes to supplied Base64 | true | false | false |
| supplied Base64 decoded-byte round trip | true | true | true |
| BOM present | false | false | true |
| trailing newline present | false | false | true |

- canonical Base64 length: 556 characters
- supplied Base64 length: 556 characters
- first Base64 difference index, zero-based: 211
- authorization_verified: false
- authorization_scope_active: false
- query_authorized: false
- query_authority_active: false

The canonical text, its declared byte length, and its declared SHA-256 are internally consistent. The supplied Base64 encodes a different 416-byte payload. The phase instructions require a mandatory stop before any Dreamina command when any authorization verification fails.

## 4. New provider-task binding verification

The required facts were verified from committed records at the starting checkpoint:

- authorized new submit_id: `f40d2e79-ba98-4873-b92d-539ccc35d2ee`
- experiment_id matched: true
- submit_invocation_occurred: true
- submit_attempt_count: 1
- provider_task_created: true
- provider_task_creation_proven: true
- created_task_count: 1
- creation_classification: `confirmed_created_nonterminal`
- prior_gen_status: `querying`
- logid_present: true
- provider_credit_count: 70
- pre_submit_balance: 5695
- post_submit_balance: 5625
- credit_delta: 70
- prior_credit_reconciliation_verified: true
- recovery_submit_count: 1/1
- recovery_submit_authorized before this phase: false
- execution_authority_active before this phase: false
- prior query/download/retry/second-recovery-submit/F07 counts: 0/0/0/0/0
- submit-ID binding checks passed: true

## 5. Old-handle quarantine verification

- old submit_id: `cabfa6ab-cc61-4d29-8630-da01dfdeef65`
- provider_task_created: false
- provider_task_creation_proven: false
- created_task_count: 0
- submit_handle_state: `orphaned_after_upload_transport_failure`
- orphaned_handle_quarantined: true
- query_recovery_eligible: false
- download_eligible: false
- continuing_query_authority: false
- retry_authorized: false
- resubmit_authorized: false
- confirmed_credit_cost: null
- credit_consumption_classification: `credit_consumption_unresolved`
- old_handle_quarantine_preserved: true

The old handle was not called, queried, downloaded, reused, or reinterpreted.

## 6. Dreamina and operation counts

- Dreamina executable invoked: false
- dreamina version called: false
- dreamina user_credit called: false
- dreamina query_result help called: false
- query_result called: false
- query invocation count: 0
- download called: false
- retry called: false
- resubmit called: false
- second query called: false
- second recovery submit called: false
- F07 called: false
- media created: false
- media downloaded: false
- media staged: false
- datasets modified: false
- final_master: false
- locked: false

No query command was constructed or executed after the mandatory authorization stop. No `--download_dir` invocation occurred.

## 7. Authority result

Because authorization verification failed before activation:

- query_count: 0
- query_count_max activated: 0
- query_authorized_after: false
- query_authority_active_after: false
- download_authorized: false
- retry_authorized: false
- resubmit_authorized: false
- second_query_authorized: false
- second_recovery_submit_authorized: false
- F07_authorized: false
- execution_authority_active: false

The committed execution-state contract was not modified because no valid query authority was activated and no live operation occurred.

## 8. Recommended next phase

`CAL-001-P3D-W01_F06_RECOVERY_ONE_QUERY_ONLY_AUTHORIZATION_ENCODING_CORRECTION_AND_REAUTHORIZATION`

Provide a corrected continuous UTF-8 Base64 value that decodes byte-for-byte to the same 416-byte canonical authorization text and therefore hashes to `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3`. Bind the corrected authorization to the repository checkpoint produced by this blocked evidence report. No query authority carries forward from this phase.

## 9. Final verdict

`CAL001_P3D_W01_F06_RECOVERY_QUERY_BLOCKED_BEFORE_DREAMINA_AUTHORIZATION_BASE64_MISMATCH_NO_QUERY`
