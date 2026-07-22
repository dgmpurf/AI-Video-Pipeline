# CAL-001 F07R One-Submit-Only Production Execution Result

## 1. Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_ONE_SUBMIT_ONLY`
- Experiment: `CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1`
- Operation: `F07R-submit-001`
- Recorded at: `2026-07-22T10:00:27.776932Z`
- Decision: `ONE_SUBMIT_EXECUTION_STRICT_TASK_CREATED_PENDING_SEPARATE_QUERY_AUTHORIZATION`
- Final verdict: `COMPLETE`

Exactly one authorized provider submit was invoked. Strict task creation is proven. No query or download was performed.

## 2. Canonical Authorization And Checkpoint

The following exact continuous line was independently extracted as the sole human authorization:

```text
APPROVE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_ONE_SUBMIT_ONLY_BIND_STARTING_HEAD_5A8B98412B4D69019F4DC279EFF49BF5F8A7B9D3_BIND_E_DECISION_COMMIT_5A8B98412B4D69019F4DC279EFF49BF5F8A7B9D3_AND_REPORT_REPORTS_PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_ONE_SUBMIT_AUTHORIZATION_DECISION_RESULT_MD_BYTE_LENGTH_10419_SHA256_8526CAB6787B8A4F8A094CC769EFAC0DFEBDF349D1D0AADC98E6F5E1E56472EE_GIT_BLOB_EF3C08667573588D63A4BD289044FC01BEB79725_ACCEPT_DECISION_ONE_SUBMIT_AUTHORIZATION_DECISION_READY_EXECUTION_BIND_SEQUENCE_FOUR_TRANSITION_EXPERIMENTS_CAL-001_EXECUTION_RECORDS_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_ROUTE_TRANSITIONS_F07R-SUBMIT-AUTHORIZED-004_TRANSITION_JSON_BYTE_LENGTH_2058_SHA256_AE7936624A0589DC49D229E07BE2FA9683EA84BB0C62A68D1D35F83127DAB102_GIT_BLOB_67E7C69ADBAF295C496321C9BDA055F832F2340C_ACCEPT_CURRENT_STATE_SUBMIT_AUTHORIZED_NOT_CONSUMED_WITH_PREFLIGHT_PASSED_PROVIDER_ELIGIBILITY_TRUE_SUBMIT_AUTHORIZED_TRUE_ALLOWANCE_UNCONSUMED_AND_ALL_PROVIDER_ROUTE_COUNTERS_ZERO_AUTHORIZE_AT_MOST_ONE_FRESH_PRE_SUBMIT_USER_CREDIT_CALL_ONE_EXACT_BOUND_MULTIMODAL2VIDEO_PROVIDER_SUBMIT_CALL_AND_ONE_FRESH_POST_SUBMIT_USER_CREDIT_CALL_WITH_ZERO_QUERY_DOWNLOAD_RETRY_RESUBMIT_BATCH_F08_LOGIN_RELOGIN_LOGOUT_CHECKLOGIN_REQUIRE_FRESH_ROUTE_BINDING_DUPLICATE_EXECUTABLE_PROMPT_FIXTURE_ARGV_AND_CREDIT_REVALIDATION_BEFORE_PROVIDER_START_REQUIRE_EXCLUSIVE_O_EXCL_SUBMIT_ALLOWANCE_CLAIM_AND_APPEND_ONLY_SEQUENCE_FIVE_ALLOWANCE_CONSUMPTION_TRANSITION_BEFORE_PROVIDER_START_NO_ALLOWANCE_RESTORE_NO_SECOND_SUBMIT_NO_AUTOMATIC_RETRY_MAXIMUM_PROVIDER_CREDIT_COST_SEVENTY_REQUIRE_EXACT_TWENTY_ARGUMENT_VECTOR_SHELL_FALSE_POLL_ZERO_AND_NO_QUERY_OR_DOWNLOAD_REQUIRE_RAW_STDOUT_AND_STDERR_HASHED_SEPARATELY_BEFORE_DECODE_NO_UNSANITIZED_RAW_PERSISTENCE_REQUIRE_INTERNAL_ALL_OCCURRENCE_IDENTIFIER_REDERIVATION_STRICT_TASK_CREATION_PROOF_AND_PRE_POST_CREDIT_RECONCILIATION_REQUIRE_FINAL_APPEND_ONLY_ROUTE_TRANSITION_TO_SUBMITTED_PENDING_SEPARATE_QUERY_AUTHORIZATION_ON_STRICT_ONE_TASK_AND_SEVENTY_CREDIT_SUCCESS_OR_ONE_EXACT_CLOSED_STATE_ON_PREQUEUE_NONCREATION_TERMINAL_AMBIGUOUS_TASK_PROOF_CREDIT_RUNNER_OR_PERSISTENCE_FAILURE_ALLOW_CREATE_ONLY_BRANCH_REQUIRED_VERSIONED_SUBMIT_COMMAND_BINDING_DUPLICATE_SNAPSHOT_CREDIT_EVIDENCE_EXCLUSIVE_CLAIM_SEQUENCE_FIVE_SUBMIT_EVIDENCE_PARSED_TASK_EVIDENCE_CREDIT_RECONCILIATION_EXECUTION_SUMMARY_EVIDENCE_MANIFEST_AUTHORITY_CLOSURE_SEQUENCE_SIX_AND_ONE_SUBMIT_RESULT_REPORT_COMMIT_AND_PUSH_EXACTLY_ONE_BOUNDED_F_COMMIT_NO_SOURCE_GLOBAL_STATE_BINDING_ROUTE_ANCHOR_PACKAGE_MANIFEST_PROMPT_MEDIA_EXECUTABLE_AUTHORIZATION_HISTORY_OR_HISTORICAL_EVIDENCE_MODIFICATION_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

Independent standard-library verification:

| Fact | Value |
| --- | --- |
| Encoding | `UTF-8` |
| Byte length | `2666` |
| SHA-256 | `c065e764c708709c59edbcc720437f437a60ad673e6bad4b5c46f01409f66ff8` |
| Locally derived Base64 length | `3556` |
| Decode count | `1` |
| Round trip | `true` |
| BOM / CR / LF / trailing space / fence | `false / false / false / false / false` |
| Last byte | `2E` |
| Repository authorization verifier | `passed` |
| Checkpoint binding | `verified` |

Required checkpoint, local HEAD, and `origin/main` were all `5a8b98412b4d69019f4dc279eff49bf5f8a7b9d3` before execution. Branch was `main`; tracked and staged diffs were empty; `sources/` was clean; exactly one primary worktree existed.

## 3. E Decision And Starting Route

- E commit: `5a8b98412b4d69019f4dc279eff49bf5f8a7b9d3`
- E decision: `ONE_SUBMIT_AUTHORIZATION_DECISION_READY_EXECUTION`
- E report: `10419` bytes, SHA-256 `8526cab6787b8a4f8a094cc769efac0dfebdf349d1d0aadc98e6f5e1e56472ee`, Git blob `ef3c08667573588d63a4bd289044fc01beb79725`
- Sequence 4: `2058` bytes, SHA-256 `ae7936624a0589dc49d229e07be2fa9683ea84bb0c62a68d1d35f83127dab102`, Git blob `67e7c69adbaf295c496321c9bda055f832f2340c`
- Starting route state: `SUBMIT_AUTHORIZED_NOT_CONSUMED`
- Starting chain: `valid=true`, findings `[]`

## 4. Static Revalidation And Tests

All immutable bindings passed immediately before the live boundary:

- Dreamina executable: `31879680` bytes, SHA-256 `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- Prompt source: `1976` bytes, SHA-256 `094a01dee03f49b65badf1864873f2b85a74a9b801f6a26621a84fb0c409f681`
- Extracted provider payload: `519` bytes, SHA-256 `ca90c5b50b7d244b6264b8ed3f23d4043bf490d25d672e2d05cfad49b487594a`; full Prompt is not reproduced.
- Three fixtures matched exact order, byte lengths, and SHA-256 values.
- Exact argv count: `20`
- Full NUL-joined argv SHA-256: `e79a1d40c9b1e31e019fceb138fe42c455e7235325f1a7b5bc9ebb58e2e956f5`
- Redacted NUL-joined argv SHA-256: `22b8de54f2de0f8f5d4543ccb649d6bf2bc291126ab5f6de1b4d798b89f11e14`
- `shell=false`, stdin closed, `poll=0`, no download directory.
- Support suite: `200 passed / 0 failed / 1 skipped`; the Windows skip was `POSIX permission bits are not stable on Windows`.

## 5. Pre-Claim Gates And Exclusive Claim

The fresh pre-submit credit gate passed against required threshold `5530`; the available-credit balance is intentionally absent from this report. The fresh duplicate-prevention gate passed: no claim, prior F07R provider invocation, task, output, submit evidence, or terminal F07R result existed; both historical handles remained quarantined; the fixed 84-task manifest contained zero F07R rows.

- Claim created: `true`
- Claim path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit_claims/F07R-submit-001_allowance_claim.json`
- Claim bytes: `625`
- Claim SHA-256: `22abede2e901d52ae66d583f43abedc52c709deef0b60571dd709c4745036c0a`
- Claim Git blob: `e62ad2f35a11f76b1f9a34a2f786a4beb0284e48`
- Allowance consumed: `true`
- Submit invocation count: `1`
- Second submit permitted: `false`
- Sequence 5 SHA-256: `91c6441ad2f1cac0a90d68d142ec0d120301570e87815fa11e9e69d6518f7a99`
- Sequence 5 Git blob: `cbc8b4bcc7e068493732126580ccc0614d724992`

## 6. Exact Command Counts

| Operation | Count |
| --- | ---: |
| Fresh pre-submit `user_credit` | 1 |
| Provider `multimodal2video` submit | 1 |
| Fresh post-submit `user_credit` | 1 |
| Query | 0 |
| Download | 0 |
| Retry / resubmit / batch | 0 / 0 / 0 |
| Login / relogin / logout / checklogin | 0 / 0 / 0 / 0 |
| F08 | 0 |

No command was automatically retried.

## 7. Submit Result And Strict Task Proof

- Submit process started: `true`
- Exit classification: `completed_exit_zero`
- Exit code: `0`
- Timed out: `false`
- Returned submit ID: `8736259f-3e91-442e-9625-ed39145fff33`
- Returned logid: `202607221746551692540470082892BEA`
- Identifier consistency: `true`
- Generation status: `querying`
- Queue status: `None`
- Fail reason: `None`
- Creation classification: `confirmed_created_nonterminal`
- Provider task created: `true`
- Provider task creation proven: `true`
- Created task count: `1`
- Provider credit-count evidence: `70`
- Pre/post credit delta: `70`
- Credit reconciliation branch: `EXACT_70_CREDIT_RECONCILED`

Raw stdout and stderr were hashed separately before UTF-8 replacement decoding. No unsanitized raw output, full Prompt, balance, token, cookie, session, signed URL, or private log was persisted in the report.

### Identifier Evidence Correction

The first sanitized stream rendered the already-redacted Prompt placeholder as an unquoted JSON value. That made the sanitized JSON invalid and caused the initial strict identifier map to report missing identifiers. The append-only authoritative correction used only the persisted sanitized text, quoted exactly that one existing redaction placeholder, and changed no identifier, status, credit, or semantic value. `validate_all_identifier_occurrences` then returned one unique submit ID and one unique logid with no contradiction; the accepted parser agreed. The original envelope and initial parse remain unchanged and are listed in the evidence manifest.

## 8. Final Route And Authority Closure

- Final route state: `SUBMITTED_PENDING_SEPARATE_QUERY_AUTHORIZATION`
- Route closed: `false` (the current execution authority is closed; the task awaits a separate query decision)
- Sequence 6 SHA-256: `e05150d74f1e4d5550d58458e9bc137ead086e9609f20287e4f0581550f1f24b`
- Sequence 6 Git blob: `1037c7c0acd655ce4cd49b9364ab3cc1650f4b88`
- Complete transition chain valid: `true`
- Transition findings: `[]`
- Allowance remains consumed: `true`
- Submit invocation count remains: `1`
- Task-created count: `1`
- Proven credit charged total: `70`

All later authority flags are false: `execution_authority_active`, `provider_command_allowed`, `submit_authorized`, `query_authorized`, `download_authorized`, `retry_authorized`, `resubmit_authorized`, `batch_authorized`, `provider_eligibility`, `final_master`, and `locked`.

## 9. Created Artifact Inventory Before Final Manifest

The final canonical evidence manifest is created after this report so it can bind this report without a circular report/manifest hash. It lists every created F artifact except its own hash.

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit/F07R-submit-001_command_binding.json` | `8257` | `a88cbdbf27e825b1886f7087d68ff30480a720617dd7d4b284e002edd5a4827a` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-pre-submit-user-credit-001.subprocess_envelope.json` | `2609` | `e0d4778d18e3aad951c4c7e51cce4a35b2cae7c0bbdb1edd1480579e18ac3935` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-pre-submit-user-credit-001.parsed_credit_snapshot.json` | `1748` | `eb4eca52774f3e2c656d35452d58149fe76a4347fbfb2e06a09c088c27f644af` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit/F07R-submit-001_duplicate_prevention_snapshot.json` | `8307` | `714ef4eee318fefdc0856e78cb4c4118be2c5d83bf986ee2f57f9daf946c0bd9` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit_claims/F07R-submit-001_allowance_claim.json` | `625` | `22abede2e901d52ae66d583f43abedc52c709deef0b60571dd709c4745036c0a` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-submit-invocation-started-005_transition.json` | `2206` | `91c6441ad2f1cac0a90d68d142ec0d120301570e87815fa11e9e69d6518f7a99` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-submit-001.subprocess_envelope.json` | `4207` | `266c4e546305737b37207b5389f149eb84f9d5447b9bfe1f7fe67f3debc032f7` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-submit-001.parsed_task_creation.json` | `2491` | `579d1ad1e9ad4333c77d3cea70864627e0457dd2a9d4d017d4b055774804383e` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-post-submit-user-credit-001.subprocess_envelope.json` | `2699` | `05bf568800045ef0ced4bcaf4755527ab9c30372e78e74066c26e30efafce323` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-post-submit-user-credit-001.parsed_credit_snapshot.json` | `1485` | `bc6fec14d1e0b3800921beb02f4fdc755d759d5ba6335076694d8555ccbf1360` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-submit-001.parsed_task_creation_authoritative_correction.json` | `5146` | `7d535e203615d91e091b3f8eb47d8cbc3038bc14a3d11fd132a13ef190c6a545` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-submit-001.credit_reconciliation.json` | `3098` | `7afb44984ba243d6594884dd6f6b265e75bef57e7ddc342398378578ea2e1ec2` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-submit-result-006_transition.json` | `2319` | `e05150d74f1e4d5550d58458e9bc137ead086e9609f20287e4f0581550f1f24b` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit/F07R-submit-001_execution_summary.json` | `5968` | `33147c6f1b87f19dac2b4d42cba7b0d61c2a5a50efdbf562e6526c9740432a27` |
| `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit/F07R-submit-001_authority_closure_record.json` | `3041` | `66666e6777a287be02a5864ef04e24ea4d076a54f1d3a7101d145107cba93527` |

Final evidence manifest path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/submit/F07R-submit-001_evidence_manifest.json`.

## 10. Protected State And Next Phase

No existing tracked file was modified. `sources/`, CAL-001 global state, immutable binding, route-state anchor, package, fixed manifest, Prompt, media, executable, authorization history, and historical evidence were not modified. No media was created or downloaded.

Next required phase: `RETURN_TO_CHATGPT_FOR_QUERY_AUTHORIZATION_DECISION`.

No query or download is authorized by this result.
