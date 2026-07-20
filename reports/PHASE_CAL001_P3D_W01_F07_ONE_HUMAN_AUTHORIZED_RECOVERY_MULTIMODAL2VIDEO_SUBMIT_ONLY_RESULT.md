# CAL-001 P3D W01 F07 Human-Authorized Recovery Submit Result

## Phase Summary

- decision: `FAILED`
- phase: `CAL-001-P3D-W01_F07_ONE_HUMAN_AUTHORIZED_RECOVERY_MULTIMODAL2VIDEO_SUBMIT_ONLY`
- starting checkpoint: `e4527c4c2cccae250ec65a4945bc2e802eb14fb7`
- bounded operation: exactly one new human-authorized F07 recovery `multimodal2video` submit
- provider invocation consumed: `true`
- strict provider task creation proven: `false`
- recovery result: `second_prequeue_upload_failure_route_reset_required`
- F07 CLI submit route stopped: `true`
- third F07 submit permitted: `false`
- final master / locked: `false / false`

The sole recovery allowance was consumed once and authority was closed before
response interpretation. Ordered input 2, IDENTITY_B, failed during prequeue
upload. No query, download, retry, resubmit, second recovery submit, third F07
submit, batch operation, or F08 operation was performed.

## Exact Human Authorization Verification

Exact canonical authorization text:

```text
APPROVE_CAL001_P3D_W01_F07_ONE_HUMAN_AUTHORIZED_RECOVERY_MULTIMODAL2VIDEO_SUBMIT_ONLY_BIND_STARTING_HEAD_e4527c4c2cccae250ec65a4945bc2e802eb14fb7_QUARANTINE_OLD_ORPHANED_SUBMIT_ID_5a69007b-ac19-4cef-86bc-41d19792149f_AND_FORBID_QUERY_OR_DOWNLOAD_OF_OLD_HANDLE_AUTHORIZE_NO_PROVIDER_PREFLIGHT_DREAMINA_VERSION_COUNT_1_DREAMINA_USER_CREDIT_COUNT_MAX_2_DREAMINA_MULTIMODAL2VIDEO_HELP_COUNT_1_AND_PROVIDER_MULTIMODAL2VIDEO_SUBMIT_COUNT_1_ONLY_AS_NEW_HUMAN_AUTHORIZED_RECOVERY_FOR_TASK_CAL001-F07-P1-R1_EXPERIMENT_CAL001-F07-P1-R1_WAVE_W01_MODEL_SEEDANCE2.0_VIP_DURATION_5_RATIO_16_9_VIDEO_RESOLUTION_720P_USING_ONLY_THE_EXACT_ACCEPTED_PROMPT_PACKAGE_MANIFEST_AND_THREE_ORDERED_IMAGE_INPUT_HASHES_REQUIRE_EXISTING_LOGIN_VALIDATED_BY_PRE_SUBMIT_USER_CREDIT_NO_LOGGER_AUTH_LOGIN_PERMISSION_OR_SESSION_FAILURE_REQUIRE_FRESH_PRE_SUBMIT_TOTAL_CREDIT_AT_LEAST_5530_AND_POST_SUBMIT_EXACT_70_CREDIT_RECONCILIATION_REQUIRE_NEW_SUBMIT_ID_DIFFERENT_FROM_OLD_HANDLE_NONEMPTY_LOGID_GEN_STATUS_QUERYING_OR_EQUIVALENT_EXPLICIT_QUERYABLE_NONFAIL_STATE_PROVIDER_CREDIT_COUNT_70_CREDIT_DELTA_70_NO_UPLOAD_FAILURE_AND_CREATED_TASK_COUNT_1_TO_CLASSIFY_TASK_CREATED_IF_LOGIN_IS_MISSING_STOP_FOR_SEPARATE_HUMAN_ASSISTED_LOGIN_AUTHORIZATION_PERSIST_ONLY_SANITIZED_RECOVERY_PREFLIGHT_SUBMIT_CREDIT_RECONCILIATION_AUTHORITY_CLOSURE_AND_BOUNDED_STATE_EVIDENCE_CLOSE_AUTHORITY_AFTER_ONE_RECOVERY_SUBMIT_INVOCATION_REGARDLESS_OF_RESULT_IF_THIS_RECOVERY_HAS_ANY_PREQUEUE_UPLOAD_FAILURE_STOP_CLI_SUBMIT_ROUTE_FOR_F07_AND_REQUIRE_ROUTE_RESET_NO_THIRD_F07_SUBMIT_NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_F08_NO_SOURCE_DATASET_PROMPT_PACKAGE_MANIFEST_OR_LOCAL_MEDIA_CHANGE_NO_STATE_CHANGE_OUTSIDE_THE_EXACT_F07_RECOVERY_SUBMIT_EVIDENCE_SCOPE_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

- encoding: `UTF-8`
- byte length: `1749`
- SHA-256: `b88d2da23e15ffe353d2d7ab76c12862ac6be3cff7f305ac9aee1e55544c2958`
- locally derived Base64 character count: `2332`
- Base64 decode count: `1`
- decoded bytes and SHA-256 match original: `true`
- BOM / CR / LF / trailing space / Markdown fence: `false / false / false / false / false`
- last character / byte: `period / 2E`
- serialization profile valid: `true`
- authorization evidence verified: `true`
- record representations consistent: `true`
- checkpoint binding verified: `true`
- activation eligible: `true`
- focused verifier tests: `124 passed, 0 failed`

## Repository And Protected-State Preflight

- repository / branch: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE / main`
- local HEAD / origin/main: `e4527c4c2cccae250ec65a4945bc2e802eb14fb7 / e4527c4c2cccae250ec65a4945bc2e802eb14fb7`
- HEAD/origin aligned: `true`
- sources clean: `true`
- protected hashes verified: `true`
- historical F07 evidence verified unchanged: `true`
- old F07 one-submit-only state object preserved: `true`

Source, datasets, fixed manifest, Prompt, package, and all three input images
matched their required hashes before execution.

## Old Handle And Diagnostic Binding

- old submit ID: `5a69007b-ac19-4cef-86bc-41d19792149f`
- old handle quarantined: `true`
- old task created / query eligible / download eligible: `false / false / false`
- diagnostic classification: `MIXED_OR_UNKNOWN_UPLOAD_TRANSPORT_FAILURE`
- diagnostic route: `ROUTE_A_ONE_HUMAN_AUTHORIZED_RECOVERY_SUBMIT`
- one recovery submit supportable verified: `true`
- third F07 submit recommended: `false`

## Exact F07 Binding

- task / experiment / wave: `CAL001-F07-P1-R1 / CAL001-F07-P1-R1 / W01`
- operation / model: `multimodal2video / seedance2.0_vip`
- duration / ratio / resolution / poll: `5 / 16:9 / 720p / 0`
- input order: `IDENTITY_A, IDENTITY_B, SCENE`
- Prompt file SHA-256: `094a01dee03f49b65badf1864873f2b85a74a9b801f6a26621a84fb0c409f681`
- provider Prompt SHA-256: `ca90c5b50b7d244b6264b8ed3f23d4043bf490d25d672e2d05cfad49b487594a`
- package SHA-256: `daf6ff398ffbc960c06e7d577f9de9e2dfdd9719863074c089a03158dc8adc64`
- manifest / row SHA-256: `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d / 84461634b31d8bfa7007376cbbe0c017be4a282abc3048872445e4a1fa9efab6`
- redacted argv SHA-256: `e79a1d40c9b1e31e019fceb138fe42c455e7235325f1a7b5bc9ebb58e2e956f5`
- argument vector / shell interpolation: `true / false`

## Live Preflight

- executable: `C:/Users/msjpurf/bin/dreamina.exe`
- executable bytes / SHA-256: `31879680 / 0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- `dreamina version`: `1 call, 2a20fff-dirty`
- pre-submit `user_credit`: `1 call, 5685 total`
- required credit floor / passed: `5530 / true`
- login viability: `true`
- `multimodal2video -h`: `1 call, contract passed`

No login/checklogin command or private Dreamina log, credential, session, token,
or environment directory was accessed.

## Recovery Submit Result

- provider submit invocation / allowance consumed: `1 / 1`
- subprocess exit code: `0`
- new submit ID: `d5fa2ba3-f4b4-4a8f-9591-5b22b1fac463`
- differs from old / quarantined: `true / true`
- logid / gen status: `null / fail`
- queryable nonfailure status: `false`
- provider credit count: `null`
- upload failure detected: `true`
- created task count: `0`
- provider task created / proven: `false / false`
- failed input index / role: `2 / IDENTITY_B`
- failure stage: `second_ordered_image_upload_prequeue`

Sanitized failure reason:

`upload resource "productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png": upload image: upload phase, no file upload, please check log for more details`

Exit code 0 and a new handle do not prove task creation. The upload failure,
null logid, null provider credit count, zero created tasks, and zero credit
delta establish that no provider generation task or queryable queue entry
exists.

## Credit, Closure, And Route Reset

- post-submit `user_credit`: `1 call, 5685 total`
- total `user_credit` calls: `2`
- observed / required delta: `0 / 70`
- exact reconciliation: `false`
- authority activated / closed: `true / true`
- execution authority active / provider command allowed: `false / false`
- F07 authorized: `false`
- query authorized / eligible: `false / false`
- download authorized / eligible: `false / false`
- retry / resubmit authorized: `false / false`
- third F07 submit permitted: `false`
- F07 CLI route stopped / route reset required: `true / true`

The first F07 attempt failed on input 3 SCENE; this recovery failed on input 2
IDENTITY_B. Both handles remain quarantined. This phase authorizes no further
F07 provider operation.

## State And Boundaries

- F07 submit / recovery submit counts: `2 / 1`
- total / global recovery submit counts: `15 / 2`
- historical invocations including orphan and recovery: `16`
- query / download / retry / resubmit counts: `0 / 0 / 0 / 0`
- completed / remaining fixed tasks: `13 / 71`
- pre/post state SHA-256: `642027f9ff3f3adfa3ce04fdcba2405536c19e9949916dbe08649e11be72b16e / 54ff10de1d68cd82f4522c1984eb6f19fa30f8a6beececa618968d6ba30bee92`
- Dreamina command counts, version/user_credit/help/provider: `1 / 2 / 1 / 1`
- query/download/retry/resubmit/batch/F08/login/checklogin: `0 / 0 / 0 / 0 / 0 / 0 / 0 / 0`
- sources/datasets/Prompt-package-manifest/media changed: `false / false / false / false`
- historical evidence changed: `false`
- run directory/review artifacts created: `false / false`
- final master / locked: `false / false`

## Evidence Paths

- authorization: `experiments/CAL-001/authorizations/CAL001_P3D_W01_F07_one_human_authorized_recovery_multimodal2video_submit_only_authorization.json`
- recovery root: `experiments/CAL-001/execution_records/P3D_W01_F07_RECOVERY_SUBMIT/CAL001-F07-P1-R1/`
- technical record: `experiments/CAL-001/execution_records/P3D_W01_F07_RECOVERY_SUBMIT/CAL001-F07-P1-R1_recovery_submit_technical_execution_record.json`
- evidence manifest: `experiments/CAL-001/execution_records/P3D_W01_F07_RECOVERY_SUBMIT/CAL001-F07-P1-R1/recovery_evidence_manifest.json`
- state: `experiments/CAL-001/execution_state/CAL001_P3C_remaining_77_resumable_execution_state_contract.json`
- report: `reports/PHASE_CAL001_P3D_W01_F07_ONE_HUMAN_AUTHORIZED_RECOVERY_MULTIMODAL2VIDEO_SUBMIT_ONLY_RESULT.md`

Commit and push metadata are reported after Git completes, avoiding
self-referential content.

## Recommended Next Phase

`CAL-001-P3D-W01_F07_CLI_SUBMIT_ROUTE_RESET_HUMAN_DECISION`

## Final Verdict

`CAL001_P3D_W01_F07_RECOVERY_SECOND_PREQUEUE_UPLOAD_FAILURE_CLI_SUBMIT_ROUTE_STOPPED_ROUTE_RESET_REQUIRED_NO_THIRD_SUBMIT`
