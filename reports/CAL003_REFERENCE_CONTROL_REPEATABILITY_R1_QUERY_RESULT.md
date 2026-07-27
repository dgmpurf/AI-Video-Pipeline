# CAL-003 Reference Control Repeatability R1 Query Result

All six CAL-003 R1 Provider tasks reached terminal success and report at least one video result. No media was downloaded. Repeatability remains unevaluated until technical validation, blind review freeze, unblinding and Gate derivation.

## 1. Actual decision and next phase

Decision: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_QUERY_SUCCESS_DOWNLOAD_READY`.

Next phase: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_DOWNLOAD_AUTHORIZATION_HUMAN_DECISION`.

## 2. Starting checkpoint

Branch `main`; HEAD and origin/main `8b833947dc58d459a8c8e238219b768107b6f048`; parent `d54c6cad666ae2733a685159ec17714704f8d1a1`; commit message `live(cal003): submit reference repeatability R1`.

## 3. Exact authorization and lifecycle

Authorization bytes/SHA-256/Base64 characters: `6006` / `f62914e9406c1c185239b9224bda7db2fa41724fb26bb44deef631846a133710` / `8008`. Activated/consumed/reusable: `true / true / false`.

## 4. Authorization round-trip

UTF-8 encode, in-memory Base64 encode, exactly one decode, byte equality, and decoded SHA-256 checks: `PASS`. BOM, trailing CR, LF, and space: `false / false / false / false`.

## 5. Submit-stage evidence bindings

All eleven committed submit-stage inputs matched exact byte lengths, SHA-256 values, Git blobs, worktree bytes, and HEAD bytes: `11/11 PASS`. Prior submit evidence coverage and committed-input coverage remain `10/10` and `18/18`.

## 6. Six task identities and submit IDs

- PUSH-01: submit ID `65aa46f5-0125-4d07-8c6e-3fd5112d29a7`; PUSH replicate 1; ordinal pair 1; submission position 1; reference `ACTION_REF_PUSH_02`.
- IMPACT-01: submit ID `b10cf271-288e-4fdb-925c-b4bd45856979`; IMPACT replicate 1; ordinal pair 1; submission position 2; reference `ACTION_REF_IMPACT_02`.
- IMPACT-02: submit ID `3cfa385f-99c9-4e1f-871e-d52ff154ebae`; IMPACT replicate 2; ordinal pair 2; submission position 3; reference `ACTION_REF_IMPACT_02`.
- PUSH-02: submit ID `2258abca-2de6-4394-903f-7de609a7e711`; PUSH replicate 2; ordinal pair 2; submission position 4; reference `ACTION_REF_PUSH_02`.
- PUSH-03: submit ID `3fbcdb18-24d2-4a43-9cd5-5c7d1de41011`; PUSH replicate 3; ordinal pair 3; submission position 5; reference `ACTION_REF_PUSH_02`.
- IMPACT-03: submit ID `10193c64-b91e-454e-9118-6ab3a0cf1fb9`; IMPACT replicate 3; ordinal pair 3; submission position 6; reference `ACTION_REF_IMPACT_02`.

All task IDs and submit IDs are nonempty and unique; metadata completeness `PASS`; reference cross-contamination `false`.

## 7. Fixed query order

`PUSH-01, IMPACT-01, IMPACT-02, PUSH-02, PUSH-03, IMPACT-03`; sequential execution; simultaneous Dreamina processes `1` maximum.

## 8. Version canary

PASS; version `2a20fff-dirty`; commit `2a20fff`; build time `2026-06-26T06:36:39Z`; stdout `96` bytes / `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`; stderr `0` bytes / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## 9. User-credit canary

PASS; fresh total credit `2701`; stdout `103` bytes / `42b72dda3852727f5d8f8cd0384b9a8492d08aca33cc5b6e67057ca70178c53c`; logger/login failures `false / false`; private account fields persisted `false`.

## 10. query_result Help and query-only command contract

PASS; one Help call only; stdout `388` bytes / `74f728cc4d3ae36fb3dcf773e85ed003637c28d048d1cad77a29b59b9bd4b171`; stderr `0` bytes / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Initial local regex result was `INCONCLUSIVE`; the exact output hash matched committed parsed-Help evidence proving `--download_dir` is optional and no implicit query loop is required. Help was not repeated.

## 11. PUSH-01 query result

Called once; return `0`; parse `PASS`; submit ID match `true`; status `success`; queue `Finish`; results/videos `1/1`; terminal/download-ready `true/true`; local result `PASS`; Provider classification `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`.

## 12. IMPACT-01 query result

Called once; return `0`; parse `PASS`; submit ID match `true`; status `success`; queue `Finish`; results/videos `1/1`; terminal/download-ready `true/true`; local result `PASS`; Provider classification `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`.

## 13. IMPACT-02 query result

Called once; return `0`; parse `PASS`; submit ID match `true`; status `success`; queue `Finish`; results/videos `1/1`; terminal/download-ready `true/true`; local result `PASS`; Provider classification `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`.

## 14. PUSH-02 query result

Called once; return `0`; parse `PASS`; submit ID match `true`; status `success`; queue `Finish`; results/videos `1/1`; terminal/download-ready `true/true`; local result `PASS`; Provider classification `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`.

## 15. PUSH-03 query result

Called once; return `0`; parse `PASS`; submit ID match `true`; status `success`; queue `Finish`; results/videos `1/1`; terminal/download-ready `true/true`; local result `PASS`; Provider classification `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`.

## 16. IMPACT-03 query result

Called once; return `0`; parse `PASS`; submit ID match `true`; status `success`; queue `Finish`; results/videos `1/1`; terminal/download-ready `true/true`; local result `PASS`; Provider classification `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`.

## 17. Local query-validation results

All six processes launched, returned code 0, parsed as complete JSON, matched their bound submit IDs, and passed local command, transport, authentication, and task-isolation validation: `6/6 PASS`.

## 18. Provider classifications

Every task is `PROVIDER_TASK_SUCCESS_WITH_VIDEO_RESULT`; Provider terminal failures `0`; terminal incomplete results `0`; nonterminal tasks `0`.

## 19. Result and video counts

Each task reports `result_count=1` and `video_count=1`; totals are `6` results and `6` videos.

## 20. Terminal and download-ready states

All six terminal states are `true`; all six download-ready states are `true`. Download authorization is not active.

## 21. Decision-precedence application

Local failure precedence did not apply; Provider terminal-failure precedence did not apply; nonterminal continuation did not apply. The all-six-success branch selected `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_QUERY_SUCCESS_DOWNLOAD_READY`.

## 22. Exact Dreamina and operation counts

Dreamina processes `9`: version `1`, user_credit `1`, Help `1`, task queries `6`. Maximums were not exceeded.

## 23. No download, retry, resubmit, batch or new submit

Download/retry/resubmit/batch/new-submit calls: `0 / 0 / 0 / 0 / 0`. No query loop, reference upload, login repair, checklogin, session mutation, or list_task occurred.

## 24. No raw Provider output or signed URL persistence

Raw stdout, raw stderr, raw Provider responses, signed URL values, and private account payloads were not persisted. Only byte lengths, hashes, sanitized statuses, counts, and booleans were recorded.

## 25. No blind mapping, alias, salt or commitment

Blind mapping materialized `false`; aliases assigned `false`; mapping salt generated `false`; mapping commitment created `false`.

## 26. No review or repeatability conclusion

Review performed `false`; media locally available `false`; repeatability conclusion known `false`. Query status alone does not establish visual repeatability.

## 27. Exact eleven-file write set

Exactly eleven new artifacts were created:

- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/authorization.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/preflight.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/push_01.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/impact_01.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/impact_02.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/push_02.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/push_03.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/impact_03.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/execution.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/evidence_manifest.json`
- `reports/CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_QUERY_RESULT.md`

## 28. Evidence coverage

Non-self output coverage `10/10`; committed submit-input coverage `11/11`; total unique bound paths `21`; evidence manifest self-excluded.

## 29. Sensitive-data result

PASS. No raw Provider payload, signed URL value, private account field, credential value, blind mapping, salt, or commitment was persisted.

## 30. Source, Prompt, package, reference, media and protected-state result

All Sources and all existing Prompt, package, reference, media, CAL-002, CAL-003 design, CAL-003 submit, production, prior-report, and protected files remained unchanged.

## 31. Commit and push result

Pre-commit validation passed. This report is part of the one authorized commit; actual commit and single-push transport results are returned in the terminal receipt.

## 32. C02, C03 and R02 boundaries

C02 reopened `false`; C03 authorized `false`; original R02 blocked `true`; R02 authorized `false`.

## 33. Production, completion, final and lock boundaries

Production re-entry, production approval, fixed-task completion, final master, and lock all remain `false`.

## 34. Exact next phase

`CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_DOWNLOAD_AUTHORIZATION_HUMAN_DECISION`. Fresh human authorization is required before any download.
