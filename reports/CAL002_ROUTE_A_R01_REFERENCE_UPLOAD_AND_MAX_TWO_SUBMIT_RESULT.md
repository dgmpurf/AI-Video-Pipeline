# CAL-002 Route A R01 Reference Transmission and Maximum Two Submit Result

## 1. Executive Decision

- Decision: `CAL002_ROUTE_A_R01_TWO_SUBMITS_ACCEPTED_READY_FOR_QUERY_AUTHORIZATION_DECISION`
- Goal identity: `CAL002_ROUTE_A_R01_REFERENCE_UPLOAD_AND_MAX_TWO_SUBMIT_V0_1`
- Execution ID: `CAL002-ROUTE-A-R01-LIVE-SUBMIT-V0-1`
- Two bounded R01 submits were accepted in the required PUSH then IMPACT order.
- This is submit acceptance only. Task, video, motion adherence, reference leakage, and semantic results remain unknown.

## 2. Starting Checkpoint

- Branch: `main`
- Starting HEAD: `fcd03d287b19431599f87476a3eb737da30c22f1`
- Starting `origin/main`: `fcd03d287b19431599f87476a3eb737da30c22f1`
- Expected parent: `56be31e86c1a7844452f01ba2954cade4b73612f`
- Starting commit message: `audit(cal002): verify Route A R01 canary packages`
- Static checkpoint, transition, Source, protected-state, and 26-path untracked-baseline checks: `PASS`

## 3. Approval And Lifecycle

- Approval text:

```text
APPROVE_CAL002_ROUTE_A_R01_REFERENCE_UPLOAD_AND_MAX_TWO_SUBMIT_V0_1__BIND_PACKAGE_AUDIT_CHECKPOINT_FCD03D287B19431599F87476A3EB737DA30C22F1__BIND_PACKAGE_AUDIT_REPORT_BYTES_24057__BIND_PACKAGE_AUDIT_REPORT_SHA256_5EEC45385CF583299D88E368454C4BE70C70DF6C9E9BA5782D839BE784E437F6__BIND_PACKAGE_PREPARATION_CHECKPOINT_56BE31E86C1A7844452F01BA2954CADE4B73612F__BIND_SANITIZED_PREPARATION_CREDIT_EVIDENCE_4151_AS_NONCURRENT_NONSUFFICIENCY_PROOF__BIND_RUNTIME_HELP_STDOUT_SHA256_FB3AA97D2D33B1D745A52519EAC529C4A21A2D90AEF9F1F6A452442FCF884277__BIND_ACTION_REF_PUSH_01_SHA256_D2B570CDD682C82CFB4559CE2B0DF1840C7E459BCBE78DF07FF1C735289743E4__BIND_ACTION_REF_IMPACT_01_SHA256_BF571FAD464C0E4ADAC5FF4DB7D85EC135A98BED07C9DD0EEF9FD83D0F3F60A4__BIND_ROUTERA_PUSH_R01_PROMPT_SHA256_C13D3AEE97A4E2462E7673218D1FA6DABBA9DED48C9812429709D399FE8F1E28__BIND_ROUTERA_IMPACT_R01_PROMPT_SHA256_25D32E3B1499EC9DF9315984F1C5CFB69FEB27E2C3CA5CAFFA841942E3D4CC8A__BIND_ROUTERA_PUSH_R01_PACKAGE_SHA256_2C5D617A75FD2BDBE7ED5559BD55E05CFB4FC85AFF060A0DAE9674FB2F21DAEF__BIND_ROUTERA_IMPACT_R01_PACKAGE_SHA256_633AC4DA3ED75382C129ECB6E8EADC81FA38C63BA6BC46BDAEBCAC0A502FE1D3__AUTHORIZE_FIXED_WINDOWS_CLI_C_USERS_MSJPURF_BIN_DREAMINA_EXE__AUTHORIZE_ONE_VERSION_CANARY_ONE_MULTIMODAL2VIDEO_HELP_CANARY_AND_UP_TO_THREE_USER_CREDIT_CALLS_FOR_PRE_SUBMIT_POST_FIRST_AND_POST_SECOND_BALANCE_EVIDENCE__AUTHORIZE_REFERENCE_TRANSMISSION_ONLY_AS_PART_OF_EXACTLY_ONE_ROUTERA_PUSH_R01_MULTIMODAL2VIDEO_SUBMIT_AND_EXACTLY_ONE_ROUTERA_IMPACT_R01_MULTIMODAL2VIDEO_SUBMIT_IN_THAT_ORDER__AUTHORIZE_MAXIMUM_TWO_TOTAL_SUBMITS_USING_THE_TWO_AUDITED_16_ELEMENT_ARGV_ARRAYS_WITH_EXPLICIT_POLL_0__REQUIRE_PRE_SUBMIT_BALANCE_TO_BE_UNAMBIGUOUS_AND_AT_LEAST_1000__REQUIRE_FIRST_SUBMIT_ACCEPTED_FIRST_CREDIT_DELTA_UNAMBIGUOUS_NOT_GREATER_THAN_500_AND_POST_FIRST_BALANCE_AT_LEAST_1000_BEFORE_SECOND_SUBMIT__STOP_ON_RUNTIME_DRIFT_HELP_DRIFT_REFERENCE_OR_PROMPT_BINDING_MISMATCH_SUBMIT_FAILURE_AMBIGUOUS_CREDIT_DELTA_SENSITIVE_DATA_OR_BUDGET_GATE_FAILURE__RECORD_EXACT_SUBMIT_IDS_AND_CREDIT_DELTAS_WITHOUT_PERSISTING_RAW_CREDIT_OUTPUT_OR_SIGNED_URLS__NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_LOGIN_NO_SESSION_MUTATION_NO_LIST_TASK_NO_R02_NO_MEDIA_CHANGE_NO_SOURCE_CHANGE_NO_PRODUCTION_REENTRY_NO_PRODUCTION_APPROVAL_NO_FIXED_TASK_COMPLETION_NO_FINAL_MASTER_NO_LOCK__ONE_TIME_NON_REUSABLE
```

- Approval byte length: `2342`
- Approval SHA-256: `38bbad8ae99e526de38c56337ab2c7126e1e99a35333a66491eee4600b34ec4d`
- Authorization activated / consumed / reusable: `true / true / false`
- Current live authority active after execution: `false`

## 4. Independent Audit Binding

- Path: `reports/CAL002_ROUTE_A_R01_TWO_PACKAGE_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md`
- Bytes: `24057`
- SHA-256: `5eec45385cf583299d88e368454c4be70c70df6c9e9ba5782d839be784e437f6`
- Decision: `CAL002_ROUTE_A_R01_TWO_PACKAGE_AUDIT_PASS_READY_FOR_TWO_SUBMIT_AUTHORIZATION_DECISION`
- Specific verdict: `INDEPENDENT_AUDIT_PASS_NO_DEFECT`
- Checks / failures: `185 / 0`
- Mutation probes: `23 / 23`

## 5. Package Preparation And Evidence Bindings

- Package-build checkpoint: `56be31e86c1a7844452f01ba2954cade4b73612f`
- Preparation report bytes/SHA-256: `17333` / `1887b725abf9880d4abd9ef8b845ccf99710e16f28c7367ee1566a255cc54134`
- Package evidence-manifest bytes/SHA-256: `9291` / `dc5a984f8a61c0944ed75823ff60e9552a79ffe075a6c0797d5c1004c22185e3`
- Artifact/input bindings: `14 / 11`
- Binding mismatches: `0`

## 6. Exact Reference Bindings

| Alias | Reference | Bytes | SHA-256 | Human decision | Leakage risk |
| --- | --- | ---: | --- | --- | --- |
| `ROUTEA_PUSH_R01` | `ACTION_REF_PUSH_01` | 69720 | `d2b570cdd682c82cfb4559ce2b0df1840c7e459bcbe78df07ff1c735289743e4` | `PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST` | `MEDIUM` |
| `ROUTEA_IMPACT_R01` | `ACTION_REF_IMPACT_01` | 69385 | `bf571fad464c0e4adac5ff4db7d85ec135a98bed07c9dd0eef9fd83d0f3f60a4` | `PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST` | `MEDIUM` |

Both references remained byte-identical to HEAD. Each had one video stream, zero audio streams, and PASS technical/full-decode records. The references left the machine only through their associated authorized submit commands.

## 7. Exact Prompt And Package Bindings

| Alias | Prompt bytes/SHA-256 | Package bytes/SHA-256 |
| --- | --- | --- |
| `ROUTEA_PUSH_R01` | `2186` / `c13d3aee97a4e2462e7673218d1fa6dabba9ded48c9812429709d399fe8f1e28` | `10504` / `2c5d617a75fd2bdbe7ed5559bd55e05cfb4fc85aff060a0dae9674fb2f21daef` |
| `ROUTEA_IMPACT_R01` | `2189` / `25d32e3b1499ec9df9315984f1c5cfb69feb27e2c3ca5caffa841942e3d4cc8a` | `10531` / `633ac4da3ed75382c129ecb6e8eadc81fa38c63ba6bc46bdaebcac0a502fe1d3` |

Motion-only reference duty, separate identity/scene/camera/composition/lighting/style duties, prohibited-copy duties, inert package authority, and the shared visual-duty block remained unchanged.

## 8. Static Argv Reconstruction

| Alias | Elements | Compact JSON-array SHA-256 | Poll |
| --- | ---: | --- | ---: |
| `ROUTEA_PUSH_R01` | 16 | `f3c289767055471161932fc01de173e49d4214aaa0842634a291411d6d7a388b` | 0 |
| `ROUTEA_IMPACT_R01` | 16 | `9b00079d2680fe5e43035729c91913bb9c355cd590f7b588b4470047a76f87a0` | 0 |

Both argv arrays were independently reconstructed before activation and again immediately before execution. Both used `shell=false`; no query, download, retry, resubmit, batch, session, output, or download-directory element was present.

## 9. Fresh Runtime Canaries

- Executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Version calls/result: `1 / PASS`
- Version stdout bytes/SHA-256: `96` / `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`
- Version stderr bytes/SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Parsed version/commit/build: `2a20fff-dirty` / `2a20fff` / `2026-06-26T06:36:39Z`
- Help calls/result: `1 / PASS`
- Help stdout bytes/SHA-256: `2739` / `fb3aa97d2d33b1d745a52519eac529c4a21a2d90aef9f1f6a452442fcf884277`
- Help stderr bytes/SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Runtime drift / help drift: `false / false`
- The version field-label parser was corrected without repeating the live call. Exact fresh output bytes matched the committed bound version evidence.
- Motion-only semantics were not inferred from help.

## 10. Credit Gates

- Preparation credit evidence: `4151`, classified as noncurrent nonsufficiency proof.
- Fresh pre-submit balance: `4151`
- Pre-submit minimum gate `>=1000`: `PASS`
- The first credit field-name parser was corrected without repeating the call. Fresh bytes exactly matched committed sanitized credit evidence.
- Post-PUSH balance: `4053`
- First-submit credit delta: `98`
- First delta nonnegative and `<=500`: `PASS`
- Post-PUSH balance `>=1000`: `PASS`
- Second-submit budget gate: `PASS`
- Post-IMPACT balance: `4021`
- Second-submit credit delta: `32`
- Total submit credit delta: `130`
- Post-second credit evidence complete: `true`
- Cost anomaly detected: `false`
- Current multimodal unit cost verified: `false`

## 11. PUSH Submit

- Attempted / accepted: `true / true`
- Reference transmission attempted: `true`
- Reference transmission occurred only as part of the exact submit: `true`
- Exit code: `0`
- stdout bytes/SHA-256: `2365` / `df5704cd3235b903a489f44f973c819533dc606b0eaf658f15244db917cf9197`
- stderr bytes/SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Sensitive data detected: `false`
- Raw output persisted: `false`
- Submit-ID parse method: explicit structured JSON field `submit_id`
- Sanitized submit ID: `e0b8f28d-f84f-4d4b-a442-ab3ee6e04984`

## 12. IMPACT Submit

- Attempted / accepted: `true / true`
- Reference transmission attempted: `true`
- Reference transmission occurred only as part of the exact submit: `true`
- Exit code: `0`
- stdout bytes/SHA-256: `2368` / `4013455acd90a327efdc11e6680092172ff82c0abfed8c5ce2d6406039ed61d8`
- stderr bytes/SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Sensitive data detected: `false`
- Raw output persisted: `false`
- Submit-ID parse method: explicit structured JSON field `submit_id`
- Sanitized submit ID: `ce15036a-203c-48c9-8e85-cd303218e72b`
- Submit IDs unique: `true`

## 13. Exact Operation Counts

- Dreamina process calls: `7`
- Version/help/user_credit/submit calls: `1 / 1 / 3 / 2`
- Submit attempts/accepted submits: `2 / 2`
- Reference transmissions attempted/associated with accepted submits: `2 / 2`
- Query/download/retry/resubmit/batch calls: `0 / 0 / 0 / 0 / 0`
- Login/checklogin/logout/relogin/list_task/session calls: all `0`
- Standalone reference-upload calls: `0`
- R02 submits: `0`

## 14. No-Query And No-Download Confirmation

No query, polling, list-task, download, URL opening, web interface, or task-completion wait occurred. Explicit `--poll 0` remained effective. Submit acceptance created no query or download authority.

## 15. No-Retry, No-Session, And Protected-State Confirmation

No retry, resubmit, batch, login, checklogin, logout, relogin, session mutation, or automatic second attempt occurred. Existing references, media, technical records, review records, Prompts, packages, manifests, indexes, Source files, and prior reports were not modified.

## 16. Review And Route Boundary

- Task result known: `false`
- Video result known: `false`
- Motion-only behavior verified: `false`
- Route A capability proven: `false`
- Full-MP4 review still required: `true`
- Sentinel count: `4`
- Any material contact-marker, mannequin-style, grid-scene, or fixed-camera-composition copy blocks R02: `true`
- R02 authorized: `false`
- Automatic expansion: `false`

## 17. Final Governance State

- Media created locally / changed: `false / false`
- Sources changed: `false`
- Production re-entry authorized: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- Final master: `false`
- Locked: `false`
- Authorization consumed / reusable / currently active: `true / false / false`

## 18. Next Phase

`CAL002_ROUTE_A_R01_MAX_TWO_SUBMIT_QUERY_AUTHORIZATION_DECISION`

The next phase requires a fresh human decision. This report does not authorize any query or download.
