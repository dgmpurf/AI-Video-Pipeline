# CAL-002 Route A V0.3 C02 Submit Result

## 1. Decision And Next Phase
- decision: `CAL002_ROUTE_A_V0_3_C02_MATCHED_PAIR_SUBMIT_SUCCESS`
- next_phase: `CAL002_ROUTE_A_V0_3_MATCHED_PAIR_CANARY_C02_QUERY_AUTHORIZATION_HUMAN_DECISION`

## 2. Starting Checkpoint
- HEAD: `f7f065fc3c69820377b59c51a2ca28515cf514a7`
- origin/main: `f7f065fc3c69820377b59c51a2ca28515cf514a7`
- parent: `7c224daba162f14a3026e2f6dbef72bb26fbfe34`
- message: `design(cal002): prepare final Route A V0.3 C02 causal isolation`

## 3. Authorization And Lifecycle
- goal_identity: `CAL002_ROUTE_A_V0_3_MATCHED_PAIR_CANARY_C02_MAX_TWO_SUBMIT_ONLY_LIVE_CAUSAL_ISOLATION_V0_1`
- execution_id: `CAL002-ROUTE-A-V0-3-C02-MAX-TWO-SUBMIT-ONLY-LIVE-V0-1`
- activated: `true`
- consumed: `true`
- reusable: `false`

## 4. Authorization Round-Trip Verification
- bytes: `4939`
- sha256: `7c2e199b4fc3965cf565defb23dfb8239ecc2d4ac7c2e076a8f918a734ceffc7`
- Base64 decode count: `1`
- decoded bytes equal original: `true`

## 5. C02 Design Bindings
- All ten committed C02 PREP paths match HEAD, byte length, SHA-256, and expected Git state.

## 6. Prompt Byte Identity
- PUSH and IMPACT Prompt bytes are identical: `true`
- common Prompt SHA-256: `bbaadf89c81a60336742a17925bc6d3cf54009e1f99818c2300b90920af6b93d`

## 7. Package Four-Pointer Isolation
- differing pointers: `/reference_binding/reference_id`, `/reference_binding/reference_path`, `/reference_binding/reference_sha256`, `/reference_binding/reference_upload_binding`
- non-allowlisted differences: `0`

## 8. Reference Bindings
- PUSH: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CLEAN_FULL_DURATION_MULTI_BEAT_REFERENCE_V0_2/media/ACTION_REF_PUSH_02.mp4` / `6006b7abc88a53978a9a7993a0b7852179ddbbbcd960d13f07ebc68218872ed6`
- IMPACT: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CLEAN_FULL_DURATION_MULTI_BEAT_REFERENCE_V0_2/media/ACTION_REF_IMPACT_02.mp4` / `a0a2662dc598f4980d3f1f22cff2c2915a0f422d797f0e09eb53e8e78110623c`
- reference cross-contamination: `false`

## 9. Output Root And Write Set
- output root and report were absent before authorization activation.
- exact new artifact count: `7`

## 10. Canary Process Order
- expected: `['dreamina version', 'dreamina user_credit', 'dreamina multimodal2video -h', 'PUSH multimodal2video submit', 'IMPACT multimodal2video submit']`
- actual: `['dreamina version', 'dreamina user_credit', 'dreamina multimodal2video -h', 'PUSH multimodal2video submit', 'IMPACT multimodal2video submit']`

## 11. Version Result
- result: `PASS`
- version: `2a20fff-dirty`
- commit: `2a20fff`
- build_time: `2026-06-26T06:36:39Z`

## 12. User-Credit Result
- result: `PASS`
- baseline total_credit: `3821`
- private account fields persisted: `false`

## 13. Runtime Help And Command Contract
- help result: `PASS`
- command contract: `PASS`

## 14. PUSH Argv Binding
- bytes: `2374`
- sha256: `d8836d007a57abde39fff545597e5ce8b3441e8fddb489e066455be4dd693010`
- shell: `false`

## 15. PUSH Process And Acceptance
- called: `true`
- return_code: `0`
- submit_id: `e0d50a2a-d8c8-4d32-9838-a76a8cad4fed`
- gen_status: `querying`
- credit_count: `140`
- accepted: `true`

## 16. Credit Guard Before IMPACT
- projected_pair_decrement: `280`
- result: `PASS`

## 17. IMPACT Argv Binding
- bytes: `2376`
- sha256: `0ff0ca4f3ad80be62f8b6ce026ac151c56e39732679d377b188e7fc9303b906a`
- shell: `false`

## 18. IMPACT Process And Acceptance
- called: `true`
- reason_not_called: `None`
- return_code: `0`
- submit_id: `8f4e9bf1-bdce-4653-a92a-6041dcf779c3`
- gen_status: `querying`
- credit_count: `140`
- accepted: `true`

## 19. Credit Accounting
- baseline total_credit: `3821`
- actual pair decrement: `280`
- maximum allowed pair decrement: `320`

## 20. Submit-ID Uniqueness
- unique: `true`

## 21. Dreamina And Provider Counts
- Dreamina CLI process attempts: `5`
- PUSH submits: `1`
- IMPACT submits: `1`

## 22. Forbidden Operation Counts
- query: `0`
- download: `0`
- retry: `0`
- resubmit: `0`
- batch: `0`

## 23. Sensitive Data
- sensitive-data scan: `PASS`
- raw Provider output persisted: `false`
- signed URL persisted: `false`

## 24. Protected State
- Source, Prompt, package, reference, media, and all prior artifacts remain unchanged.

## 25. Exact Seven-File Write Set
- `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_LIVE/authorization.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_LIVE/preflight.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_LIVE/submits/push.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_LIVE/submits/impact.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_LIVE/execution.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_LIVE/evidence_manifest.json`
- `reports/CAL002_RA_V03_C02_SUBMIT_RESULT.md`

## 26. Evidence Coverage
- evidence manifest binds six non-self outputs: `6/6`

## 27. Commit And Push Result
- At immutable report freeze, Git finalization has not yet occurred.
- Actual commit and push outcome is recorded in the terminal receipt after artifact validation.

## 28. Final Bounded Canary
- C02 remains the final bounded Route A canary: `true`

## 29. C03 Boundary
- automatic C03 authorized: `false`

## 30. Original R02 Boundary
- original R02 blocked: `true`
- R02 authorized: `false`

## 31. Governance Flags
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## 32. Exact Next Human-Decision Gate
- `CAL002_ROUTE_A_V0_3_MATCHED_PAIR_CANARY_C02_QUERY_AUTHORIZATION_HUMAN_DECISION`

Both C02 causal-isolation tasks were accepted for asynchronous processing.
Neither task has been queried or downloaded. Their final generation status
and visual content remain unknown.
