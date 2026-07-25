# CAL-002 Route A R01 Max-Two Query-Only Result

## 1. Executive decision

Decision:

`CAL002_ROUTE_A_R01_QUERY_ONLY_BLOCKED_HELP_VALIDATION_FAILURE_NO_QUERY`

The one-time query-only authority was activated and consumed. The fixed
Dreamina version canary passed. The single authorized `query_result -h`
invocation completed, but the local wrapper then raised a regular-expression
compile error while parsing the captured help text. Required help metadata was
therefore not retained. The help call cannot be replayed under this
non-reusable authorization, so neither task query was issued.

This is a local post-call evidence-validation failure. It is not evidence that
the Dreamina CLI help surface drifted, and it is not a Provider task result.

## 2. Starting checkpoint and transition

- Branch: `main`
- Starting HEAD: `9133eb534729d9bd6502345c830eb9d892f6298d`
- `origin/main`: `9133eb534729d9bd6502345c830eb9d892f6298d`
- Starting HEAD parent: `fcd03d287b19431599f87476a3eb737da30c22f1`
- Starting commit message: `live(cal002): record Route A R01 submit execution`
- Local HEAD and locally recorded `origin/main` were aligned.
- Tracked files, staged files, and `sources/` were clean.
- The 26-path pre-existing untracked baseline was preserved.

## 3. Approval binding and lifecycle

Exact approval:

```text
APPROVE_CAL002_ROUTE_A_R01_MAX_TWO_QUERY_ONLY_V0_1__BIND_LIVE_SUBMIT_CHECKPOINT_9133EB534729D9BD6502345C830EB9D892F6298D__BIND_LIVE_SUBMIT_REPORT_BYTES_11212__BIND_LIVE_SUBMIT_REPORT_SHA256_500950105BD072FCE66778C071195FDAB5E6AB35A50D8E3332BC710B89FD9ABA__BIND_ROUTERA_PUSH_R01_SUBMIT_ID_E0B8F28D-F84F-4D4B-A442-AB3EE6E04984__BIND_ROUTERA_IMPACT_R01_SUBMIT_ID_CE15036A-203C-48C9-8E85-CD303218E72B__AUTHORIZE_FIXED_WINDOWS_CLI_C_USERS_MSJPURF_BIN_DREAMINA_EXE__AUTHORIZE_ONE_VERSION_CANARY_ONE_QUERY_RESULT_HELP_CANARY_AND_EXACTLY_ONE_QUERY_RESULT_CALL_FOR_EACH_BOUND_SUBMIT_ID_IN_PUSH_THEN_IMPACT_ORDER_WITHOUT_DOWNLOAD_DIR__REQUIRE_QUERY_ONLY_NO_POLL_LOOP_NO_IMPLICIT_REQUERY_NO_LIST_TASK_NO_URL_OPENING_AND_NO_MEDIA_DOWNLOAD__REQUIRE_EXACT_SUBMIT_ID_BINDING_UNAMBIGUOUS_SANITIZED_GEN_STATUS_QUEUE_STATUS_RESULT_COUNT_AND_DOWNLOAD_READY_BOOLEAN__REQUIRE_RAW_QUERY_OUTPUT_NOT_PERSISTED_AND_NO_SIGNED_URL_TOKEN_COOKIE_AUTHORIZATION_HEADER_SESSION_SECRET_OR_ACCOUNT_IDENTIFIER_PERSISTED__ALLOW_SECOND_BOUND_QUERY_AFTER_FIRST_VALID_TASK_STATUS_QUERYING_SUCCESS_OR_FAIL__STOP_ON_RUNTIME_DRIFT_HELP_DRIFT_SUBMIT_ID_BINDING_MISMATCH_QUERY_PROCESS_FAILURE_AMBIGUOUS_STATUS_OR_SENSITIVE_DATA__RECORD_SUCCESS_QUERYING_FAIL_OR_OTHER_EXACT_PROVIDER_STATUS_WITHOUT_INTERPRETING_SUBMIT_ACCEPTANCE_AS_VIDEO_SUCCESS__NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_USER_CREDIT_NO_LOGIN_NO_SESSION_MUTATION_NO_MEDIA_CHANGE_NO_R02_NO_SOURCE_CHANGE_NO_PRODUCTION_REENTRY_NO_PRODUCTION_APPROVAL_NO_FIXED_TASK_COMPLETION_NO_FINAL_MASTER_NO_LOCK__ONE_TIME_NON_REUSABLE
```

- Approval byte length: `1544`
- Approval SHA-256: `f337bf431516cdb3ee1fdf11aa884c4839480a3e75e1ec97275d23278f083c01`
- Authorization activated: `true`
- Authorization consumed: `true`
- Authorization reusable: `false`
- Current query authority active: `false`

## 4. Bound prior evidence

Live-submit governance report:

- Path: `reports/CAL002_ROUTE_A_R01_REFERENCE_UPLOAD_AND_MAX_TWO_SUBMIT_RESULT.md`
- Bytes: `11212`
- SHA-256: `500950105bd072fce66778c071195fdab5e6ab35a50d8e3332bc710b89fd9aba`

Existing live evidence:

- Evidence manifest: `7390` bytes, SHA-256
  `c618bc62d45b8d394aed7199157f9fde284c2c9c39d05262ea78b1fd8bd68e1c`
- PUSH prior submit receipt: `2532` bytes, SHA-256
  `1f7c201984eb1e5becb84424f8dce5e9b47905a275dcc8c1b7c9c9a878bea874`
- IMPACT prior submit receipt: `2551` bytes, SHA-256
  `6c633b92dc09188759f1eed1f70705f240cbe717641c5c5d6618d72d3e2a7a9a`
- Live execution record: `3509` bytes, SHA-256
  `ef3ab56300288b90e7f4baadb4cba6ac1e5644a7467074b56e2ccb7f46437e43`
- Submit manifest: `3973` bytes, SHA-256
  `1449b7973797c73b71b3aeb77dbe02165dfc2fb94177674b231a0e87d128639e`

All committed bindings and the package, Prompt, reference, audit, and
reference-review lineage were unchanged at static preflight.

## 5. Submit-ID bindings

1. `ROUTEA_PUSH_R01`
   - Package: `CAL002-ROUTE-A-PUSH-R01`
   - Reference: `ACTION_REF_PUSH_01`
   - Submit ID: `e0b8f28d-f84f-4d4b-a442-ab3ee6e04984`
2. `ROUTEA_IMPACT_R01`
   - Package: `CAL002-ROUTE-A-IMPACT-R01`
   - Reference: `ACTION_REF_IMPACT_01`
   - Submit ID: `ce15036a-203c-48c9-8e85-cd303218e72b`

## 6. Fixed CLI and runtime canary

Dreamina executable:

`C:/Users/msjpurf/bin/dreamina.exe`

The executable resolved to the same fixed path.

Fresh version invocation:

```text
C:/Users/msjpurf/bin/dreamina.exe version
```

- Calls: `1`
- Exit code: `0`
- Stdout: `96` bytes
- Stdout SHA-256: `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`
- Stderr: `0` bytes
- Stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Parsed version: `2a20fff-dirty`
- Parsed commit: `2a20fff`
- Parsed build time: `2026-06-26T06:36:39Z`
- Runtime drift: `false`
- Raw output persisted: `false`

## 7. Fresh query-result help canary

Fresh help invocation:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result -h
```

- Calls: `1`
- The subprocess returned before the local parser failure.
- Exit code, stdout/stderr byte lengths, hashes, and parsed option facts were
  not retained because the wrapper failed during post-call regex compilation.
- Raw output persisted: `false`
- Help drift: `not established`
- Required help validation passed: `false`
- Replay attempted: `false`

The exact one-help-call authorization is exhausted. Re-running the help command
would exceed the authorized call count.

## 8. Query-only command shape

The prevalidated PUSH command shape was:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id e0b8f28d-f84f-4d4b-a442-ab3ee6e04984
```

Its four-element compact JSON argv SHA-256 was
`073a6959f7ca55843860a2f37ca7b2502bbeac45b85f4e2ab2d2efe5418ba6bd`.

The prevalidated IMPACT command shape was:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id ce15036a-203c-48c9-8e85-cd303218e72b
```

Its four-element compact JSON argv SHA-256 was
`8cc05813568594babc621a39799e1118ad3bd0aaebafa828300aca8bd3dbaa2a`.

Both shapes omitted `--download_dir`. Neither command was executed.

## 9. PUSH query result

- Query called: `false`
- Query count for bound submit ID: `0`
- Exact Provider status: `null`
- Normalized status: `not_queried`
- Queue status: `null`
- Image/video/result counts: `0 / 0 / 0`
- Signed result URL count: `0`
- Download ready: `false`
- Response submit ID returned: `false`
- Query ambiguity: `false`
- Sensitive data detected: `false`

Not-called reason: the fresh help invocation could not be validated after the
local post-call parser failure, and replay was forbidden.

## 10. IMPACT query result

- Query called: `false`
- Query count for bound submit ID: `0`
- Exact Provider status: `null`
- Normalized status: `not_queried`
- Queue status: `null`
- Image/video/result counts: `0 / 0 / 0`
- Signed result URL count: `0`
- Download ready: `false`
- Response submit ID returned: `false`
- Query ambiguity: `false`
- Sensitive data detected: `false`

Not-called reason: the PUSH query was not permitted to start, so the
second-query gate was never reached.

## 11. Call and privacy accounting

- Total Dreamina calls: `2`
- Version calls: `1`
- `query_result -h` calls: `1`
- Task-query calls: `0`
- Unique queried submit IDs: `0`
- Second query per submit ID: `false`
- Query loop performed: `false`
- Implicit requery performed: `false`
- `list_task` calls: `0`
- Download calls: `0`
- URLs opened: `0`
- Retry calls: `0`
- Resubmit calls: `0`
- Batch calls: `0`
- `user_credit` calls: `0`
- Login/checklogin/session calls: `0`
- New submit calls: `0`
- Signed URLs persisted: `false`
- Credentials persisted: `false`
- Raw query output persisted: `false`
- Account identifiers persisted: `false`

## 12. Task-state and visual boundary

- Terminal-success count: `0`
- Terminal-failure count: `0`
- Nonterminal-querying count: `0`
- Other-status count: `0`
- Download-ready count: `0`
- Unqueried aliases: `ROUTEA_PUSH_R01`, `ROUTEA_IMPACT_R01`
- Task statuses known: `false`
- Video bytes obtained: `false`
- Visual success known: `false`
- Motion-only behavior verified: `false`
- Reference leakage reviewed: `false`
- Route A capability proven: `false`

Prior submit acceptance remains only evidence that two tasks were accepted by
the submit route. It is not evidence of Provider generation success.

## 13. Reference-overdominance sentinels

The four future visual-review sentinels remain:

1. `CONTACT_MARKER_COPY`
2. `MANNEQUIN_STYLE_COPY`
3. `GRID_SCENE_COPY`
4. `FIXED_CAMERA_COMPOSITION_COPY`

No leakage review occurred. Any material sentinel copy in a future downloaded
R01 video must block R02 and automatic expansion pending a fresh human
decision.

## 14. Protected boundaries

- Media created: `false`
- Media changed: `false`
- Sources changed: `false`
- Prompt/package/reference/manifest changed: `false`
- R02 authorized: `false`
- Automatic expansion: `false`
- Production re-entry authorized: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- Final master: `false`
- Locked: `false`

## 15. Next phase

Next phase:

`CAL002_ROUTE_A_R01_QUERY_ONLY_HELP_VALIDATION_FAILURE_REAUTHORIZATION_DECISION`

That phase must decide whether a fresh, separately bound authorization may
re-run the help canary and query the still-unqueried PUSH and IMPACT submit
IDs. This report grants no such authority.
