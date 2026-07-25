# CAL-002 Route A R01 Query-Only Help Validation Recovery Result

## 1. Executive decision

Decision:

`CAL002_ROUTE_A_R01_QUERY_RECOVERY_TWO_RESULTS_SUCCESS_READY_FOR_MAX_TWO_DOWNLOAD_AUTHORIZATION_DECISION`

The literal-byte Help validator passed its pre-activation self-tests. The one
fresh `query_result -h` call passed the literal command-contract check. PUSH
and IMPACT were then queried exactly once each in the authorized order. Both
returned an exact Provider status of `success`, queue status `Finish`, one
video result, and `download_ready=true`.

This establishes Provider generation completion only. No media was downloaded
or reviewed, so visual and semantic success remain unknown.

## 2. Starting checkpoint and prior transition

- Branch: `main`
- Starting HEAD: `213faf1bf638f7fb4b3e588fa771a994f47c7d8b`
- Starting `origin/main`: `213faf1bf638f7fb4b3e588fa771a994f47c7d8b`
- Starting HEAD parent: `9133eb534729d9bd6502345c830eb9d892f6298d`
- Starting commit message: `query(cal002): record Route A R01 task status`
- HEAD and locally recorded `origin/main` were aligned.
- The parent-to-HEAD transition contained exactly eight additions and no
  modification, deletion, rename, or unexpected path.
- Tracked files, staged files, and `sources/` were clean.
- The pre-existing 26-path untracked baseline SHA-256 was
  `619b91a4981d8000f769bba3d15739ec2b0496df1109a98d809735aaf8abef94`.

## 3. Approval binding and lifecycle

Exact approval:

```text
APPROVE_CAL002_ROUTE_A_R01_QUERY_ONLY_HELP_VALIDATION_RECOVERY_AND_MAX_TWO_QUERY_V0_1__BIND_BLOCKED_QUERY_CHECKPOINT_213FAF1BF638F7FB4B3E588FA771A994F47C7D8B__BIND_BLOCKED_QUERY_REPORT_BYTES_9607__BIND_BLOCKED_QUERY_REPORT_SHA256_9ABFB042DA75DCD35C3BC922AAA225D191ECEA2115B5555AF90AE65DE1C7667E__BIND_BLOCKED_QUERY_EVIDENCE_MANIFEST_BYTES_7961__BIND_BLOCKED_QUERY_EVIDENCE_MANIFEST_SHA256_C1725DE438F592398EF187E0DADD58F4373F76418778C3E401B9C6B79CB6BEF6__BIND_FRESH_VERSION_EVIDENCE_STDOUT_BYTES_96__BIND_FRESH_VERSION_EVIDENCE_STDOUT_SHA256_25BBB1BDC706CB4E6FD486316B89B98A0D29C07FA34C8C51D0F860DA2F29D8F0__BIND_ROUTERA_PUSH_R01_SUBMIT_ID_E0B8F28D-F84F-4D4B-A442-AB3EE6E04984__BIND_ROUTERA_IMPACT_R01_SUBMIT_ID_CE15036A-203C-48C9-8E85-CD303218E72B__AUTHORIZE_FIXED_WINDOWS_CLI_C_USERS_MSJPURF_BIN_DREAMINA_EXE__AUTHORIZE_PRE_ACTIVATION_LITERAL_HELP_PARSER_SELF_TEST_WITH_NO_DREAMINA_CALL__AUTHORIZE_EXACTLY_ONE_FRESH_QUERY_RESULT_HELP_CALL_AND_EXACTLY_ONE_QUERY_RESULT_CALL_FOR_EACH_BOUND_SUBMIT_ID_IN_PUSH_THEN_IMPACT_ORDER_WITHOUT_DOWNLOAD_DIR__REQUIRE_HELP_EXIT_CODE_STDOUT_STDERR_BYTE_LENGTHS_AND_SHA256_TO_BE_CAPTURED_BEFORE_ANY_PARSE__REQUIRE_LITERAL_BYTE_TOKEN_VALIDATION_FOR_QUERY_RESULT_SUBMIT_ID_AND_DOWNLOAD_DIR_AND_FORBID_REGEX_BASED_HELP_PARSING__REQUIRE_QUERY_ONLY_NO_POLL_LOOP_NO_IMPLICIT_REQUERY_NO_LIST_TASK_NO_URL_OPENING_AND_NO_MEDIA_DOWNLOAD__REQUIRE_EXACT_SUBMIT_ID_BINDING_UNAMBIGUOUS_SANITIZED_GEN_STATUS_QUEUE_STATUS_RESULT_COUNTS_AND_DOWNLOAD_READY_BOOLEAN__REQUIRE_RAW_HELP_AND_QUERY_OUTPUT_NOT_PERSISTED_AND_NO_SIGNED_URL_TOKEN_COOKIE_AUTHORIZATION_HEADER_SESSION_SECRET_OR_ACCOUNT_IDENTIFIER_PERSISTED__ALLOW_SECOND_BOUND_QUERY_AFTER_FIRST_VALID_TASK_STATUS_QUERYING_SUCCESS_OR_FAIL__STOP_ON_PARSER_SELF_TEST_FAILURE_HELP_PROCESS_FAILURE_HELP_CONTRACT_FAILURE_SUBMIT_ID_BINDING_MISMATCH_QUERY_PROCESS_FAILURE_AMBIGUOUS_STATUS_OR_UNSANITIZABLE_SENSITIVE_DATA__AUTHORIZE_ONE_RECOVERY_EVIDENCE_SET_GOVERNANCE_REPORT_COMMIT_AND_PUSH_ONLY__NO_VERSION_CALL_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_USER_CREDIT_NO_LOGIN_NO_SESSION_MUTATION_NO_MEDIA_CHANGE_NO_R02_NO_SOURCE_CHANGE_NO_PRODUCTION_REENTRY_NO_PRODUCTION_APPROVAL_NO_FIXED_TASK_COMPLETION_NO_FINAL_MASTER_NO_LOCK__ONE_TIME_NON_REUSABLE
```

- Approval byte length: `2222`
- Approval SHA-256: `9a06ee2aff87e2f383026c39a13baf723a97ad89d75305ea7631cdd05b315660`
- Authorization activated: `true`
- Authorization consumed: `true`
- Authorization reusable: `false`
- Current query authority active: `false`

## 4. Prior blocked-query evidence

Prior blocked-query report:

- Path: `reports/CAL002_ROUTE_A_R01_MAX_TWO_QUERY_ONLY_RESULT.md`
- Bytes: `9607`
- SHA-256: `9abfb042da75dcd35c3bc922aaa225d191ecea2115b5555af90ae65de1c7667e`
- Decision:
  `CAL002_ROUTE_A_R01_QUERY_ONLY_BLOCKED_HELP_VALIDATION_FAILURE_NO_QUERY`

Prior blocked-query evidence manifest:

- Path:
  `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_MAX_TWO_QUERY_ONLY_V0_1/route_a_r01_query_evidence_manifest.json`
- Bytes: `7961`
- SHA-256: `c1725de438f592398ef187e0dadd58f4373f76418778c3e401b9c6b79cb6bef6`
- Artifact bindings: `7 / 7`, zero mismatches
- Declared input bindings: zero mismatches
- Self excluded: `true`

The prior block was a local post-call Help-validation failure. It was not
evidence of CLI drift or Provider task failure.

## 5. Prior version evidence and no-new-version result

Version evidence source:

`PRIOR_IMMEDIATELY_PRECEDING_BLOCKED_QUERY_EXECUTION`

- New version calls: `0`
- Prior version call exit code: `0`
- Prior stdout: `96` bytes
- Prior stdout SHA-256:
  `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`
- Prior stderr: `0` bytes
- Prior stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Parsed version: `2a20fff-dirty`
- Parsed commit: `2a20fff`
- Parsed build time: `2026-06-26T06:36:39Z`
- Runtime drift: `false`
- Fresh version evidence reused: `true`

## 6. Submit and argv bindings

PUSH:

- Alias: `ROUTEA_PUSH_R01`
- Package: `CAL002-ROUTE-A-PUSH-R01`
- Reference: `ACTION_REF_PUSH_01`
- Submit ID: `e0b8f28d-f84f-4d4b-a442-ab3ee6e04984`
- Query argv elements: `4`
- Compact argv SHA-256:
  `073a6959f7ca55843860a2f37ca7b2502bbeac45b85f4e2ab2d2efe5418ba6bd`

IMPACT:

- Alias: `ROUTEA_IMPACT_R01`
- Package: `CAL002-ROUTE-A-IMPACT-R01`
- Reference: `ACTION_REF_IMPACT_01`
- Submit ID: `ce15036a-203c-48c9-8e85-cd303218e72b`
- Query argv elements: `4`
- Compact argv SHA-256:
  `8cc05813568594babc621a39799e1118ad3bd0aaebafa828300aca8bd3dbaa2a`

Both query commands used direct argv arrays with `shell=false`, one
`--submit_id`, and no `--download_dir`.

## 7. Literal parser self-test

- Method: `LITERAL_BYTE_TOKEN_CONTAINMENT`
- Input type: bytes
- Required tokens: `query_result`, `--submit_id`, `--download_dir`
- Self-test count: `8`
- Self-test pass count: `8`
- All self-tests passed: `true`
- Regex Help parsing used: `false`
- Dreamina calls during self-test: `0`
- Repository writes during self-test: `0`

The fixtures covered the valid token set, each missing token, an empty byte
string, both required-hyphen near matches, and a non-bytes input.

## 8. Capture-before-parse invariant

For the Help call and both task queries, process exit code, raw byte lengths,
raw byte hashes, timing, and the false raw-output-persisted flag were captured
immediately after subprocess return and before parsing.

- Capture before parse completed: `true`
- Metadata survived parsing: `true`
- Raw Help output persisted: `false`
- Raw query output persisted: `false`

## 9. Fresh Help result

Command shape:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result -h
```

- Calls: `1`
- Start UTC: `2026-07-25T16:44:01.849Z`
- End UTC: `2026-07-25T16:44:04.393Z`
- Elapsed seconds: `2.543603`
- Exit code: `0`
- Stdout: `388` bytes
- Stdout SHA-256:
  `74f728cc4d3ae36fb3dcf773e85ed003637c28d048d1cad77a29b59b9bd4b171`
- Stderr: `0` bytes
- Stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `query_result` literal token: `true`
- `--submit_id` literal token: `true`
- `--download_dir` literal token: `true`
- Matched literal tokens: `3 / 3`
- Help contract result: `PASS`
- Sensitive data detected: `false`
- Raw output persisted: `false`

## 10. PUSH sanitized task result

- Query called: `true`
- Query count for bound submit ID: `1`
- Start UTC: `2026-07-25T16:45:18.068Z`
- End UTC: `2026-07-25T16:45:22.921Z`
- Elapsed seconds: `4.853115`
- Exit code: `0`
- Stdout: `3496` bytes
- Stdout SHA-256:
  `dee1ecfd41a21f4799a80c71c149213cba150dfe9c420fceb952287b749b4b78`
- Stderr: `0` bytes
- Stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Structured parse mode: `complete_json`
- Response submit ID returned: `true`
- Response submit ID matched: `true`
- Exact Provider status: `success`
- Normalized status: `success`
- Queue status: `Finish`
- Image/video/result counts: `0 / 1 / 1`
- Signed URL count: `1`
- Signed URL persisted: `false`
- URL opened: `false`
- Download ready: `true`
- Parse ambiguity: `false`
- Sensitive data detected: `false`
- Sanitization result: `PASS`
- Raw output persisted: `false`

## 11. IMPACT sanitized task result

- Query called: `true`
- Query count for bound submit ID: `1`
- Start UTC: `2026-07-25T16:45:50.292Z`
- End UTC: `2026-07-25T16:45:54.679Z`
- Elapsed seconds: `4.386565`
- Exit code: `0`
- Stdout: `3498` bytes
- Stdout SHA-256:
  `8d7a013dcda4f7dc2856690aa87398378db3e2a1d856cc2b8f6e0c24eec41aef`
- Stderr: `0` bytes
- Stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Structured parse mode: `complete_json`
- Response submit ID returned: `true`
- Response submit ID matched: `true`
- Exact Provider status: `success`
- Normalized status: `success`
- Queue status: `Finish`
- Image/video/result counts: `0 / 1 / 1`
- Signed URL count: `1`
- Signed URL persisted: `false`
- URL opened: `false`
- Download ready: `true`
- Parse ambiguity: `false`
- Sensitive data detected: `false`
- Sanitization result: `PASS`
- Raw output persisted: `false`

## 12. Command, privacy, and state accounting

- Total Dreamina process calls: `3`
- New version calls: `0`
- Fresh Help calls: `1`
- Task-query calls: `2`
- PUSH query calls: `1`
- IMPACT query calls: `1`
- Unique queried submit IDs: `2`
- Second query per submit ID: `false`
- Query loop performed: `false`
- Implicit requery performed: `false`
- New generation submit calls: `0`
- Download calls: `0`
- URLs opened: `0`
- Retry calls: `0`
- Resubmit calls: `0`
- Batch calls: `0`
- `user_credit` calls: `0`
- Login/checklogin/logout/relogin/session calls: `0`
- `list_task` calls: `0`
- Signed URLs detected: `2`
- Signed URLs persisted: `false`
- Credentials persisted: `false`
- Raw Help output persisted: `false`
- Raw query output persisted: `false`
- Account identifiers persisted: `false`

## 13. Provider and visual-review boundary

- Terminal-success count: `2`
- Terminal-failure count: `0`
- Nonterminal-querying count: `0`
- Other-status count: `0`
- Download-ready count: `2`
- Unqueried aliases: none
- Task statuses known: `true`
- Provider generation success: `true` for both tasks
- Video bytes obtained: `false`
- Visual success known: `false`
- Motion-only behavior verified: `false`
- Reference leakage reviewed: `false`
- Route A capability proven: `false`

No visual, motion, identity, scene, camera-separation, or reference-leakage
claim is made.

## 14. Reference-overdominance sentinels

The four future visual-review sentinels remain:

1. `CONTACT_MARKER_COPY`
2. `MANNEQUIN_STYLE_COPY`
3. `GRID_SCENE_COPY`
4. `FIXED_CAMERA_COMPOSITION_COPY`

Any material sentinel copy in a future downloaded R01 video blocks R02 and
automatic expansion pending a fresh human decision. Provider success does not
override this rule.

## 15. Protected boundaries

- Media created: `false`
- Media changed: `false`
- Sources changed: `false`
- Prior blocked-query evidence changed: `false`
- Prompt/package/reference/live-submit evidence changed: `false`
- R02 authorized: `false`
- Automatic expansion: `false`
- Production re-entry authorized: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- Final master: `false`
- Locked: `false`

## 16. Next phase

Next phase:

`CAL002_ROUTE_A_R01_MAX_TWO_DOWNLOAD_AUTHORIZATION_DECISION`

This report does not authorize download. A fresh human authorization and its
own bounded execution contract are required.
