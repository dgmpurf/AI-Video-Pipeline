# CAL-001 P3D W01 F06 Single Recovery Submit-Only Result

## 1. Phase summary

- completion_status: COMPLETE
- decision: ready
- phase: CAL-001-P3D-W01_F06_SINGLE_RECOVERY_SUBMIT_ONLY
- experiment_id: CAL001-F06-P1-R1
- starting_head: 70ca0ee35c25a85f2ab076bfbe46b99b15c2e84f
- status: F06_recovery_submit_valid_provider_task_created_query_not_authorized
- recorded_at: 2026-07-19T14:33:39.2246561Z

The already activated single-recovery submit-only authority was consumed exactly once. A new provider task was proven created, the immediate 70-credit charge reconciled, and all live execution authority was then closed. This phase did not query or download the task and does not claim generation or visual success.

## 2. Repository and Source checkpoint

Before any Dreamina command, local `main`, local `HEAD`, and `origin/main` all matched `70ca0ee35c25a85f2ab076bfbe46b99b15c2e84f`. The index and tracked worktree were clean. `sources/` was clean and remained untouched. Known unrelated untracked workspace noise was left in place.

## 3. Activation verification

The committed 404-byte authorization record matched SHA-256 `35af5a5ed0dbabf7bf03ab0967a3eb2cf9c13a191c5eebe9ab2f1a4125b1fa33`. Before live execution, macro and activation state were `ACTIVATED_READY_FOR_F06_RECOVERY_SUBMIT_ONLY`, execution authority and exactly one recovery submit were active, recovery count was 0 of 1, and query/download/retry/second-recovery/F07 authority was false.

## 4. Accepted immutable integrity

All six canonical digests were reconstructed from current bytes and matched: fixed manifest `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d`, fixture registry `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142`, Prompt inventory `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d`, package inventory `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c`, full inventory `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138`, and remaining order `783cb601ce9f33f20defadce9b37aff33698dcf492b9b71273a023e4deb0e291`. Counts were 84 manifest rows, 84 unique experiment IDs, 28 Prompt records, 84 package records, and 77 ordered remaining IDs; Prompt/package/fixture mismatch counts were zero.

## 5. Old-handle quarantine

Old submit ID `cabfa6ab-cc61-4d29-8630-da01dfdeef65` remains `orphaned_after_upload_transport_failure`, with `provider_task_created=false`, `provider_task_creation_proven=false`, `created_task_count=0`, and no reuse/query/download authority. It was not called, queried, downloaded, revived, or reinterpreted in this phase. Its confirmed credit cost remains null and its consumption classification remains unresolved.

## 6. Parser correction

The centralized classifier still refuses to treat a submit ID alone as provider-task proof. The synthetic prequeue-upload failure and committed old-handle correction both classified as an orphaned handle with no created task. The directly affected no-live tests passed 36/36.

## 7. Accepted F06 binding

The submit used `multimodal2video`, `seedance2.0_vip`, 5 seconds, `16:9`, `720p`, and `poll=0`. Prompt file SHA-256 remained `1672ee6ba29d82c844af6e4700607582410a323c24409697916b28e56a8b76f0`; the exact 476-character provider payload remained SHA-256 `dfe401cdc9c47e5d46664fb9ffcfbd61b9cf81bb28361c4acea33c7ede944d94`. Package SHA-256 remained `4f0f8356b2d0c04f03f1eb6d3f403259795e24b413031c883491856d25366710`. The command envelope proves the three accepted image paths were passed once each in Fenshou, Shuangji, scene order.

## 8. Dreamina canary and command contract

Executable: `C:/Users/msjpurf/bin/dreamina.exe`, file SHA-256 `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`. Version returned `2a20fff-dirty`, commit `2a20fff`, build time `2026-06-26T06:36:39Z`. Version and `multimodal2video -h` both exited zero with no stderr, logger Access denied, or authentication failure. Current help supports the exact model, duration, ratio, resolution, three ordered images, and disabled polling contract.

## 9. Fresh pre-submit balance gate

The one authorized fresh pre-submit `user_credit` call returned numeric balance 5695. The required gate was 5670, so the gate passed. Positive credit state did not enlarge scope.

## 10. Single recovery submit

Exactly one recovery submit invocation occurred. It returned exit code 0, new submit ID `f40d2e79-ba98-4873-b92d-539ccc35d2ee`, logid `20260719222855169254047008682C523`, `gen_status=querying`, null queue status, and numeric `credit_count=70`. The new submit ID differs from the quarantined old ID. No upload/prequeue failure was returned.

## 11. Provider-task creation classification

The corrected classifier returned `confirmed_created_nonterminal`, `provider_task_created=true`, `provider_task_creation_proven=true`, and `created_task_count=1`. This result is supported by a new submit ID, valid nonterminal state, logid, numeric 70-credit provider evidence, and absence of upload failure. It is not inferred from exit code, submit ID, or `querying` alone.

## 12. Immediate post-submit credit reconciliation

The one authorized immediate post-submit `user_credit` call returned balance 5625. The observed delta was `5695 - 5625 = 70`, exactly matching provider `credit_count=70`. Credit reconciliation passed. No additional credit polling occurred.

## 13. Authority closure

After the one submit and post-submit reconciliation, recovery submit count became 1 of 1, `recovery_submit_authorized=false`, and `execution_authority_active=false`. Query, download, retry, second recovery submit, F07, W02+, and CAL001B remain unauthorized. A separate human authorization is required before one query-only action on the new submit ID.

## 14. Explicit non-actions

- query_called: false
- download_called: false
- retry_called: false
- second_recovery_submit_called: false
- F07_called: false
- media_created: false
- media_staged: false
- datasets_modified: false
- sources_touched: false
- final_master: false
- locked: false

## 15. Durable evidence

The existing atomic Dreamina evidence wrapper persisted sanitized envelopes before interpretation. Evidence includes one version call, one help call, one pre-submit credit call, one submit, and one post-submit credit call, with parsed records and SHA-256 manifest. No signed URL, query result, download evidence, binary media, or dataset update exists.

## 16. Files created and modified

Created: one local preflight record, ten command/parsed evidence JSON files, one evidence manifest, one execution record, one authority-closure record, and this report. Modified: only the mutable CAL-001 execution-state contract. Commit and push results are recorded in the final Codex receipt because this report is itself part of that commit.

## 17. Required receipt

- accepted_hashes_verified: true
- activation_verified: true
- parser_correction_verified: true
- old_handle_quarantine_preserved: true
- dreamina_version: 2a20fff-dirty
- canary_status: pass
- command_contract_valid: true
- pre_submit_balance: 5695
- pre_submit_balance_gate_passed: true
- submit_invocation_occurred: true
- submit_attempt_count: 1
- new_submit_id: f40d2e79-ba98-4873-b92d-539ccc35d2ee
- new_submit_id_differs_from_old: true
- subprocess_exit_code: 0
- gen_status: querying
- queue_status: null
- logid_present: true
- provider_credit_count: 70
- provider_task_created: true
- provider_task_creation_proven: true
- created_task_count: 1
- post_submit_balance: 5625
- credit_delta: 70
- credit_reconciliation_passed: true
- recovery_submit_count: 1
- recovery_submit_authorized_after: false
- execution_authority_active_after: false

## 18. Next required phase

`CAL-001-P3D-W01_F06_RECOVERY_QUERY_AUTHORIZATION_DECISION`: separate human authorization for one query-only action. No query is authorized by this result.

## 19. Final verdict

`CAL001_P3D_W01_F06_RECOVERY_SUBMIT_VALID_TASK_CREATED_AUTHORITY_CLOSED_READY_QUERY_AUTHORIZATION_DECISION`
