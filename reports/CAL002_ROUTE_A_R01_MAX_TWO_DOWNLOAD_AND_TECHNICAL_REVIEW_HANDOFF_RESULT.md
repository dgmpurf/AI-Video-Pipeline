# CAL-002 Route A R01 Download and Technical Review Handoff Result

## 1. Executive Decision

- Decision: `CAL002_ROUTE_A_R01_PUSH_DOWNLOAD_OR_TECHNICAL_VALIDATION_FAILED_IMPACT_NOT_ATTEMPTED`
- Next phase: `CAL002_ROUTE_A_R01_DOWNLOAD_FAILURE_REVIEW`
- Visual review performed: false
- Route A capability proven: false
- R02 authorized: false

## 2. Starting Checkpoint

- Starting HEAD / origin/main: `65b1116e3fe4111bffa018f7c48adf65b2158d2e`
- Expected parent: `213faf1bf638f7fb4b3e588fa771a994f47c7d8b`
- Parent-to-HEAD transition: 8 additions, 0 modifications, 0 deletions, 0 renames
- Pre-existing untracked baseline: `26` paths / `619b91a4981d8000f769bba3d15739ec2b0496df1109a98d809735aaf8abef94`
- Sources and tracked worktree: clean

## 3. Approval Binding and Lifecycle

Exact approval:

```text
APPROVE_CAL002_ROUTE_A_R01_MAX_TWO_DOWNLOAD_AND_TECHNICAL_REVIEW_HANDOFF_V0_1__BIND_QUERY_RECOVERY_CHECKPOINT_65B1116E3FE4111BFFA018F7C48ADF65B2158D2E__BIND_QUERY_RECOVERY_REPORT_BYTES_11923__BIND_QUERY_RECOVERY_REPORT_SHA256_E28CCD5ED690B99EFE89F2FA2C49831C99B2E96C3AAD836A24E0C21B5F06A32C__BIND_QUERY_RECOVERY_EVIDENCE_MANIFEST_BYTES_9324__BIND_QUERY_RECOVERY_EVIDENCE_MANIFEST_SHA256_77C8831306433409F2E04907D31AAE40472FF2B01C44BE7FC44CA9F90A03CA51__BIND_ROUTERA_PUSH_R01_QUERY_RECEIPT_BYTES_1952__BIND_ROUTERA_PUSH_R01_QUERY_RECEIPT_SHA256_5C0BC0B7A19D370237195ED004D6446AA399F04D6DAD6B392241610B2957AAEA__BIND_ROUTERA_IMPACT_R01_QUERY_RECEIPT_BYTES_1958__BIND_ROUTERA_IMPACT_R01_QUERY_RECEIPT_SHA256_C766A832B6AD50A561D27244CD1FA28809F94D6CC415D436D8DB6802E16FFCEF__BIND_ROUTERA_PUSH_R01_SUBMIT_ID_E0B8F28D-F84F-4D4B-A442-AB3EE6E04984__BIND_ROUTERA_IMPACT_R01_SUBMIT_ID_CE15036A-203C-48C9-8E85-CD303218E72B__BIND_BOTH_TASKS_AS_SUCCESS_FINISH_WITH_EXACTLY_ONE_VIDEO_RESULT_AND_DOWNLOAD_READY_TRUE_FROM_IMMEDIATE_PRECEDING_QUERY_EVIDENCE__AUTHORIZE_FIXED_WINDOWS_CLI_C_USERS_MSJPURF_BIN_DREAMINA_EXE__AUTHORIZE_EXACTLY_ONE_QUERY_RESULT_DOWNLOAD_CALL_FOR_EACH_BOUND_SUBMIT_ID_IN_PUSH_THEN_IMPACT_ORDER_USING_SEPARATE_NEW_ABSENT_DOWNLOAD_DIRECTORIES__AUTHORIZE_PROVIDER_SIGNED_RESULT_LOCATOR_USE_ONLY_INSIDE_THE_CLI_DOWNLOAD_PROCESS_WITH_NO_URL_PERSISTENCE_DISPLAY_MANUAL_OPENING_OR_EXTERNAL_REUSE__REQUIRE_EACH_DOWNLOAD_CALL_TO_RETURN_UNAMBIGUOUS_SUCCESS_FOR_THE_EXACT_BOUND_SUBMIT_ID_AND_EXACTLY_ONE_VIDEO_RESULT__REQUIRE_EXACTLY_ONE_NEW_NONEMPTY_VIDEO_FILE_PER_TASK_NO_OVERWRITE_NO_COLLISION_NO_UNEXPECTED_FILE_TYPE_AND_BYTE_PRESERVING_LOCAL_RENAME_TO_ROUTERA_PUSH_R01_MP4_AND_ROUTERA_IMPACT_R01_MP4__AUTHORIZE_LOCAL_SHA256_FFPROBE_FULL_FFMPEG_DECODE_SIX_KEYFRAMES_PER_VIDEO_TWO_CONTACT_SHEETS_TECHNICAL_RECORDS_EVIDENCE_MANIFEST_GOVERNANCE_REPORT_COMMIT_AND_PUSH__REQUIRE_COMPLETE_MP4_CHATGPT_PRO_AND_HUMAN_PROJECT_OWNER_REVIEW_BEFORE_ANY_R02_OR_ROUTE_A_CAPABILITY_DECISION__REQUIRE_CONTACT_MARKER_MANNEQUIN_STYLE_GRID_SCENE_AND_FIXED_CAMERA_COMPOSITION_SENTINELS_AND_ANY_MATERIAL_COPY_TO_BLOCK_R02__STOP_ON_CHECKPOINT_OR_BINDING_MISMATCH_DOWNLOAD_PROCESS_FAILURE_TASK_STATUS_OR_RESULT_COUNT_DRIFT_SIGNED_URL_PERSISTENCE_UNEXPECTED_FILE_DECODE_FAILURE_SENSITIVE_DATA_OR_PROTECTED_STATE_CHANGE__NO_VERSION_CALL_NO_HELP_CALL_NO_ADDITIONAL_QUERY_ONLY_CALL_NO_QUERY_LOOP_NO_SUBMIT_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_USER_CREDIT_NO_LOGIN_NO_SESSION_MUTATION_NO_R02_NO_SOURCE_CHANGE_NO_PRIOR_MEDIA_CHANGE_NO_PRODUCTION_REENTRY_NO_PRODUCTION_APPROVAL_NO_FIXED_TASK_COMPLETION_NO_FINAL_MASTER_NO_LOCK__ONE_TIME_NON_REUSABLE
```

- Approval bytes / SHA-256: `2618` / `6e658b2e6cac2fad6a7e6c96a399d6f214cb56bd8d9e4cac014377447235d243`
- Authorization activated: true
- Authorization consumed: true
- Authorization reusable: false
- Current download authority active: false

## 4. Query-Recovery and Lineage Bindings

- Query-recovery report: `11923` bytes / `e28ccd5ed690b99efe89f2fa2c49831c99b2e96c3aad836a24e0c21b5f06a32c`
- Query-recovery evidence manifest: `9324` bytes / `77c8831306433409f2e04907d31aae40472ff2b01c44be7fc44ca9f90a03ca51`
- PUSH query receipt: `1952` bytes / `5c0bc0b7a19d370237195ed004d6446aa399f04d6dad6b392241610b2957aaea`
- IMPACT query receipt: `1958` bytes / `c766a832b6ad50a561d27244cd1fa28809f94d6cc415d436d8db6802e16ffcef`
- Both bound tasks were `success` / `Finish` with image/video/result counts `0 / 1 / 1` and download-ready `true`.
- Both package, Prompt, project-owned reference, reference-review lock, and locked human-review bindings matched HEAD.

## 5. Runtime and Command Boundary

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Dreamina version calls: 0
- Dreamina Help calls: 0
- Additional query-only calls: 0
- Download calls: `1` (PUSH only); IMPACT was stopped before invocation
- Each download used exactly 6 argv elements and one `--submit_id` plus one `--download_dir`.
- Full argv and exact temporary directories were not persisted.
- Signed result locator count detected and withheld: `1`
- Signed URLs persisted / manually opened: false / false
- Raw stdout or stderr persisted: false

## 6. Per-Task Results

### ROUTEA_PUSH_R01

- Submit ID: `e0b8f28d-f84f-4d4b-a442-ab3ee6e04984`
- Called / exit code: `true` / `UNKNOWN_NOT_DURABLY_PRESERVED`
- Argv elements / SHA-256: `6` / `UNKNOWN_LOST_BY_LOCAL_EVIDENCE_HANDLER`
- Provider status / queue: `UNRESOLVED_NUMERIC_RUNTIME_STATUS_NOT_MAPPED` / `UNRESOLVED_NUMERIC_RUNTIME_STATUS_NOT_MAPPED`
- Image/video/result payload counts: `0 / 1 / 1`
- Filesystem regular files / result: `unknown` / `NOT_ENUMERATED_BEFORE_LOCAL_STOP`
- Candidate bytes / SHA-256: `None` / `None`
- Preliminary ffprobe / pre-move decode: `None` / `None`
- Byte-preserving move: `None`
- Canonical path: `None`
- Canonical bytes / SHA-256: `None` / `None`
- Post-move decode / technical result: `None` / `NOT_RUN`
- Keyframes / contact sheet: `0` / `None`

### ROUTEA_IMPACT_R01

- Not called reason: `PUSH_LOCAL_PARSER_CONTRACT_MISMATCH_STOP`
- Submit ID: `ce15036a-203c-48c9-8e85-cd303218e72b`
- Called / exit code: `false` / `None`
- Argv elements / SHA-256: `6` / `None`
- Provider status / queue: `None` / `None`
- Image/video/result counts: `None / None / None`
- Filesystem regular files / result: `0` / `NOT_RUN`
- Candidate bytes / SHA-256: `None` / `None`
- Preliminary ffprobe / pre-move decode: `None` / `None`
- Byte-preserving move: `None`
- Canonical path: `None`
- Canonical bytes / SHA-256: `None` / `None`
- Post-move decode / technical result: `None` / `NOT_RUN`
- Keyframes / contact sheet: `0` / `None`


## 7. Local Failure Diagnosis

- The PUSH Dreamina process was invoked exactly once after authorization activation; the bound PUSH submit ID appears twice in the same-hour local CLI log, while the IMPACT submit ID appears zero times.
- The sanitized runtime-log summary shows one MP4 result item: 1280x720, 24 fps, 5042 ms.
- The runtime payload used numeric task and queue status values (`50` and `3`). The local runner required literal string fields `gen_status=success` and `queue_status=Finish`, so it stopped at its parser contract before filesystem enumeration.
- A local exception-transfer defect then discarded the already captured in-memory process metadata instead of carrying it into the durable receipt. Exit code and stdout/stderr byte hashes are therefore unknown and are not invented.
- The ephemeral download root was removed by the mandatory cleanup path. No canonical media was accepted, preserved, staged, or committed.
- This is a local orchestration/evidence defect, not a visual failure and not proof of Provider download failure.

## 8. Review Artifacts and Cleanup

- Validated canonical videos: `0`
- Keyframes: `0`
- Contact sheets: `0`
- Review handoff created: `false`
- Temporary files and directories cleaned: `true`
- Exact created repository paths: `8`

## 9. Explicit Non-Actions and Governance Boundary

- Exactly one PUSH `query_result --download_dir` invocation occurred. No IMPACT invocation, additional query-only call, submit, retry, resubmit, batch, user-credit, login, session, or list-task operation was performed.
- No R02 operation was created or authorized.
- No prior media, Prompt, package, manifest, review artifact, Source, or protected file was changed.
- Provider generation success, local download success, and local technical PASS are distinct from visual and semantic review.
- Visual pass, action-family pass, motion-reference adherence, motion-only semantics, identity/scene/camera separation, and leakage absence remain unknown.
- Production re-entry authorized: false
- Production approved: false
- Fixed-task completion: false
- Final master: false
- Locked: false
