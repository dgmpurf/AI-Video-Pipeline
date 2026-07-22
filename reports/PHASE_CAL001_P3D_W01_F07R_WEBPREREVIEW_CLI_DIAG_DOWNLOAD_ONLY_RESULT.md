# CAL-001 F07R Download-Only Result

## Phase Summary

- Phase: `CAL-001-P3D-W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_ONLY`
- Starting checkpoint: `f6eb6cadb322ca40f1234183228bec265139963b`
- Result classification: `download_succeeded_awaiting_human_review`
- Final route state: `DOWNLOAD_SUCCEEDED_AWAITING_HUMAN_REVIEW`
- Human visual review required: `true`
- Route closed: `false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

This phase performed the one authorized Dreamina download operation. It did not submit, perform a query-only operation, call `user_credit`, retry, resubmit, batch, invoke F08, or use login or web UI routes.

## Canonical Authorization

The content of the following single line, excluding the Markdown fence and line ending, is the exact canonical human authorization persisted for this phase:

```text
APPROVE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_ONLY_BIND_STARTING_HEAD_F6EB6CADB322CA40F1234183228BEC265139963B_BIND_H1_COMMIT_F6EB6CADB322CA40F1234183228BEC265139963B_AND_REPORT_REPORTS_PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_AUTHORIZATION_DECISION_RESULT_MD_BYTE_LENGTH_8085_SHA256_31629E21D385499F4AC2963D82A0793430ED6F8AFC22F61294823A0D47458A8D_GIT_BLOB_ADB9FD45A315368961A1919F368D179441A3586F_ACCEPT_DECISION_DOWNLOAD_AUTHORIZATION_DECISION_READY_EXECUTION_BIND_SEQUENCE_TEN_TRANSITION_EXPERIMENTS_CAL-001_EXECUTION_RECORDS_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_ROUTE_TRANSITIONS_F07R-DOWNLOAD-AUTHORIZED-010_TRANSITION_JSON_BYTE_LENGTH_2164_SHA256_CC0920546FEC92FC9E4A3C834A1F15D21F4E661AB049335C5C4FCF592D169F32_GIT_BLOB_4CA9E341DFF82F83891640DE409A743ED4EC7BE3_ACCEPT_CURRENT_STATE_DOWNLOAD_AUTHORIZED_NOT_CONSUMED_BIND_SUBMIT_ID_8736259F-3E91-442E-9625-ED39145FFF33_AUTHORIZE_AT_MOST_ONE_EXACT_DREAMINA_QUERY_RESULT_DOWNLOAD_CALL_WITH_BOUND_DOWNLOAD_DIR_G-AICODING-AI_VIDEO-AI_VIDEO_PIPELINE-EXPERIMENTS-CAL-001-RUNS-CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_CLASSIFY_AS_DOWNLOAD_OPERATION_WITH_ZERO_PROVIDER_SUBMIT_QUERY_ONLY_USER_CREDIT_RETRY_RESUBMIT_BATCH_F08_LOGIN_RELOGIN_LOGOUT_CHECKLOGIN_OR_WEB_UI_CALLS_REQUIRE_EXCLUSIVE_DOWNLOAD_CLAIM_AND_APPEND_ONLY_SEQUENCE_ELEVEN_BEFORE_COMMAND_NO_SECOND_DOWNLOAD_NO_RETRY_NO_OVERWRITE_REQUIRE_EXACTLY_ONE_NEW_MP4_AT_BOUND_FINAL_PATH_EXACT_BYTE_LENGTH_SHA256_FFPROBE_AND_FULL_DECODE_VALIDATION_REQUIRE_LOCAL_CONTACT_SHEET_SIX_KEYFRAMES_TECHNICAL_MEDIA_MANIFEST_AND_HUMAN_REVIEW_HANDOFF_REQUIRE_FINAL_APPEND_ONLY_SEQUENCE_TWELVE_TO_DOWNLOAD_SUCCEEDED_AWAITING_HUMAN_REVIEW_OR_ONE_EXACT_CLOSED_DOWNLOAD_FAILURE_STATE_REQUIRE_DOWNLOAD_INVOCATION_COUNT_ONE_SUBMIT_COUNT_ONE_QUERY_COUNT_ONE_CREDIT_CHARGED_TOTAL_SEVENTY_AND_ALL_LIVE_AUTHORITIES_FALSE_AFTER_EXECUTION_NO_FINAL_NO_LOCK_NO_FIXED_TASK_COMPLETION_ALLOW_EXACTLY_ONE_BOUNDED_H2_COMMIT_CONTAINING_ONLY_TRACKED_DOWNLOAD_EVIDENCE_TRANSITIONS_HANDOFF_AND_RESULT_REPORT_WHILE_MP4_CONTACT_SHEET_AND_KEYFRAMES_REMAIN_LOCAL_UNTRACKED_NO_EXISTING_TRACKED_FILE_MODIFICATION_NO_SOURCE_GLOBAL_STATE_BINDING_ROUTE_ANCHOR_PACKAGE_MANIFEST_PROMPT_EXECUTABLE_AUTHORIZATION_HISTORY_OR_HISTORICAL_EVIDENCE_CHANGE_FINAL_MASTER_FALSE_LOCKED_FALSE.
```

Independent Python standard-library verification established:

- Encoding: `UTF-8`
- Byte length: `2303`
- SHA-256: `5a69884e9f07fc92e7faa728bd5c82dffd074b35c7c484df62f4b52d1a0e4581`
- Derived Base64 character count: `3072`
- Base64 decode count: `1`
- Decoded bytes equal original bytes: `true`
- Decoded SHA-256 matched: `true`
- BOM, CR, LF, trailing space, or Markdown fence in canonical bytes: `false`
- Last byte: `2E`
- Repository authorization compiler/verifier: `passed`
- Checkpoint binding verification: `passed`

No output from the current implementation was used as the sole authority for this phase.

## Repository And H1 Boundary

Before the live operation:

- Repository root, branch `main`, local HEAD, origin/main, and required checkpoint matched.
- Local HEAD and origin/main were `f6eb6cadb322ca40f1234183228bec265139963b`.
- Sources were clean.
- Staged files and unexpected tracked modifications were absent.
- Exactly one primary worktree existed.
- Existing unrelated untracked workspace noise was left untouched.

H1 was independently bound as follows:

- H1 commit: `f6eb6cadb322ca40f1234183228bec265139963b`
- H1 parent: `821140f93bdd37302b685c0c6186e090de1f8bf9`
- H1 report byte length: `8085`
- H1 report SHA-256: `31629e21d385499f4ac2963d82a0793430ed6f8afc22f61294823a0d47458a8d`
- H1 report Git blob: `adb9fd45a315368961a1919f368d179441a3586f`
- H1 decision: `DOWNLOAD_AUTHORIZATION_DECISION_READY_EXECUTION`
- Sequence 10 byte length: `2164`
- Sequence 10 SHA-256: `cc0920546fec92fc9e4a3c834a1f15d21f4e661ab049335c5c4fcf592d169f32`
- Sequence 10 Git blob: `4ca9e341dff82f83891640de409a743ed4ec7be3`
- Starting route state: `DOWNLOAD_AUTHORIZED_NOT_CONSUMED`

## Preclaim Gates

- Dreamina executable byte length: `31879680`
- Dreamina executable SHA-256: `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- ffprobe available: `true`
- ffmpeg available: `true`
- Dedicated support suite: `200 passed, 1 skipped, 0 failed` from `201` collected tests
- Route chain through sequence 10: `valid`
- Submit evidence manifest: `16` artifacts verified byte-stable
- Query evidence manifest: `9` artifacts verified byte-stable
- Output directory and bound final MP4 were absent before the claim
- Previous H2 download claim or media: `absent`
- Preclaim gate: `passed`

The initial broad prior-artifact scan treated the legitimate H1 sequence-10 download authorization record as an H2 artifact. A corrected read-only scan explicitly separated H1 authorization from H2 execution artifacts and passed before any claim, local output, or Dreamina invocation was created.

## Binding, Claim, And Sequence 11

- Command binding path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download/F07R-download-001_command_binding.json`
- Command binding byte length: `10291`
- Command binding SHA-256: `8cf071a2daa336f55bf60ea67ace89db34a8ff31452a92c6a5e1921f3ad3d446`
- Exclusive claim path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download_claims/F07R-download-001_invocation_claim.json`
- Exclusive claim byte length: `734`
- Exclusive claim SHA-256: `f4f7d04747817e881421c48650f7d3422d06669bc7319185cae4b18bab99c13e`
- Exclusive claim Git blob: `e4b9f32c64eb6c1ab1c5775a23b70130d9517ea5`
- Sequence 11 path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-download-invocation-started-011_transition.json`
- Sequence 11 SHA-256: `6ebb72c9552754cf28ba8ff00ced102502129072261c768a50e39cdc7f0b188a`
- Sequence 11 Git blob: `2492d913e4ba63d95b781a024e214a9b4a5fd943`
- Route chain through sequence 11: `valid`

The claim was created with exclusive-create semantics, durably reread, and permanently consumed the sole download allowance before process start.

## Exact Download Execution

The exact six-element argv was invoked once with `shell=false`, closed stdin, the repository root as cwd, and a 300-second timeout:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 8736259f-3e91-442e-9625-ed39145fff33 --download_dir G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/experiments/CAL-001/runs/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1
```

- Operation classification: `download`
- Query-only operation: `false`
- Download process started: `true`
- Process exit classification: `zero_exit`
- Exit code: `0`
- Timed out: `false`
- Download invocation count: `1`
- Second download permitted: `false`
- Raw stdout bytes: `1489`
- Raw stdout SHA-256: `639007af63128e66427341e350e1289d13e3115f06c8275a1e5298b1e896fb6c`
- Raw stderr bytes: `0`
- Raw stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- UTF-8 replacement events: `0`
- Unsanitized raw streams persisted: `false`
- Signed URL values persisted: `false`

The tracked envelope contains only separately hashed and sanitized stream evidence. This report contains no raw provider response, signed URL, full Prompt, account balance, token, cookie, session, or credential.

## Downloaded Media

- Newly created regular files from the exact invocation: `1`
- Newly created MP4 files: `1`
- Provider temporary basename: `8736259f-3e91-442e-9625-ed39145fff33_video_1.mp4`
- Bound final local path: `experiments/CAL-001/runs/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1_result.mp4`
- Final byte length: `7215952`
- Final SHA-256: `915c7633dd477f2e55dcd5dd463e066f3cad2056a4c0d9afbbf3a8bc45af3aa7`
- Atomic rename without overwrite: `true`
- Final flush and reread verified: `true`
- Media ignored and untracked: `true`

## Technical Media Validation

- ffprobe exit code: `0`
- Video streams: `1`
- Width: `1280`
- Height: `720`
- Average frame rate: `24.119601328903656 fps` from `7260/301`
- Video-stream duration: `5.016667 seconds`
- Format duration: `5.085011 seconds`
- Frame count: `121`
- Container: `mov,mp4,m4a,3gp,3g2,mj2`
- MP4-compatible container: `true`
- Full ffmpeg decode exit code: `0`
- Fatal ffprobe or decode error: `false`
- Technical media validation: `passed`

The first local validator attempt used an unauthorizedly strict absolute frame-rate tolerance of `0.05 fps` and recorded a failed decision at SHA-256 `da9800f9c01a0b79810ea3f66088991f2d9f46fbf55ac88d7efae85513f0cb55`. The authorization requires only "approximately 24 fps." The persisted final validator explicitly operationalizes that phrase as an absolute tolerance of `0.5 fps` and a relative tolerance of `2%`. The observed deviation is about `0.119601 fps`, or `0.4983%`, so the frame-rate check passes. The original failed attempt and correction reason remain recorded in the final canonical validation evidence. No additional Dreamina or provider call occurred for this correction.

## Local Review Artifacts

Six lossless PNG keyframes were created at `0.000`, `0.840`, `1.680`, `2.520`, `3.360`, and `4.200` seconds. One chronological JPG contact sheet was created. Every artifact is nonempty, decodable, hashed, ignored, and untracked.

- Keyframes: `6`
- Contact sheets: `1`
- Review artifacts valid: `true`
- Contact sheet path: `experiments/CAL-001/runs/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/review_artifacts/F07R-download-001_contact_sheet.jpg`
- Contact sheet byte length: `148223`
- Contact sheet SHA-256: `53c0effb64ed97dcd575f531b8d38552e94509568dce519b6a545d115b573fb7`
- Subjective visual-quality judgment performed: `false`

The technical manifest binds the MP4, six keyframes, contact sheet, exact identities, media metadata, and decode result. The human-review handoff requires ChatGPT Pro plus human visual review and contains no acceptance decision.

## Sequence 12 And Route Closure

- Sequence 12 path: `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-download-result-012_transition.json`
- Sequence 12 byte length: `2609`
- Sequence 12 SHA-256: `6c12401709770ca50e4e1d143bf784da3cfa6dbaee16f21812970f0b91fed5a5`
- Sequence 12 Git blob: `5a29fc2c0faf5061e9b2845c060b86d22fa2bcf7`
- Complete chain valid: `true`
- Terminal state: `DOWNLOAD_SUCCEEDED_AWAITING_HUMAN_REVIEW`
- Chain findings: `[]`
- Route closed: `false`
- Human review required: `true`

Final route counters:

- Provider submit invocations: `1`
- Provider tasks created: `1`
- Credit charged total: `70`
- Query invocations: `1`
- Download invocations: `1`
- Retry, resubmit, and batch invocations: `0`

All live authorities are closed after the one download:

- `execution_authority_active=false`
- `provider_command_allowed=false`
- `provider_eligibility=false`
- `download_authorized=false`
- `query_authorized=false`
- `submit_authorized=false`
- `retry_authorized=false`
- `resubmit_authorized=false`
- `batch_authorized=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

## H2 File Boundary

Exactly these 12 tracked H2 artifacts are intended for the bounded commit:

1. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download/F07R-download-001_command_binding.json`
2. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download_claims/F07R-download-001_invocation_claim.json`
3. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-download-invocation-started-011_transition.json`
4. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-download-001.subprocess_envelope.json`
5. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/evidence/F07R-download-001.media_validation.json`
6. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download/F07R-download-001_technical_media_manifest.json`
7. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download/F07R-download-001_execution_summary.json`
8. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download/F07R-download-001_authority_closure_record.json`
9. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/review/F07R-download-001_human_review_handoff.md`
10. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/route_transitions/F07R-download-result-012_transition.json`
11. `reports/PHASE_CAL001_P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG_DOWNLOAD_ONLY_RESULT.md`
12. `experiments/CAL-001/execution_records/P3D_W01_F07R_WEBPREREVIEW_CLI_DIAG/CAL001-F07R-WEBPREREVIEW-CLI-DIAG-P1-R1/download/F07R-download-001_evidence_manifest.json`

The MP4, six PNGs, and JPG remain local ignored files. No existing tracked file, Source, CAL-001 global state, route-state anchor, binding, package, production manifest, Prompt, executable, authorization history, or historical evidence was modified.

## Final Verdict

Decision: `download_succeeded_awaiting_human_review`

Final verdict: `CAL001_F07R_DOWNLOAD_SUCCEEDED_AWAITING_HUMAN_REVIEW`

Next required phase: `RETURN_TO_CHATGPT_PRO_FOR_HUMAN_VISUAL_REVIEW`
