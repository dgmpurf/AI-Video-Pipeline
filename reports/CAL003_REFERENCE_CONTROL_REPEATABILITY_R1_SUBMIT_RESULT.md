# CAL-003 Reference Control Repeatability R1 Submit Result

Six CAL-003 R1 tasks were submitted successfully in the fixed sequential order. They have not been queried or downloaded. No repeatability conclusion can be made from submit acceptance alone.

## 1. Actual decision and next phase

Decision: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_SUBMIT_SUCCESS`

Next phase: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_QUERY_AUTHORIZATION_HUMAN_DECISION`.

## 2. Starting checkpoint

Branch `main`; HEAD and origin/main `d54c6cad666ae2733a685159ec17714704f8d1a1`; parent `b16c6522c3f09a3b3f81ff816b2090d4cefe5efb`.

## 3. Exact authorization and lifecycle

Authorization bytes/SHA-256/Base64 characters: `5680` / `3ae23f47c015d2089459668ecbd5cc25d95d1e84159cae064f65b0f63ed27012` / `7576`. Activated/consumed/reusable: `true / true / false`.

## 4. Authorization round-trip verification

Independent UTF-8 encode, Base64 encode, one decode, byte equality, and decoded SHA-256 checks: `PASS`.

## 5. CAL-003 design bindings

All committed CAL-003 R1 design bindings matched worktree and HEAD: `PASS`.

## 6. Six package bindings

PUSH-01, IMPACT-01, IMPACT-02, PUSH-02, PUSH-03, and IMPACT-03 package bindings: `6/6 PASS`.

## 7. Common Prompt binding

Exact raw Prompt bytes/SHA-256: `2010` / `bbaadf89c81a60336742a17925bc6d3cf54009e1f99818c2300b90920af6b93d`; terminal LF preserved.

## 8. PUSH and IMPACT reference bindings

PUSH `6006b7abc88a53978a9a7993a0b7852179ddbbbcd960d13f07ebc68218872ed6`; IMPACT `a0a2662dc598f4980d3f1f22cff2c2915a0f422d797f0e09eb53e8e78110623c`; worktree equals HEAD; cross-contamination `false`.

## 9. Provider-payload equality

PUSH `3/3`; IMPACT `3/3`.

## 10. Future-argv equality

PUSH `3/3`; IMPACT `3/3`; shell `false`.

## 11. Four-pointer cross-family isolation

Differences were exactly reference ID, path, SHA-256, and upload binding; non-allowlisted differences `0`.

## 12. Fixed submission order

`PUSH-01, IMPACT-01, IMPACT-02, PUSH-02, PUSH-03, IMPACT-03`; parallelism `0`.

## 13. Version canary

PASS; version `2a20fff-dirty`; commit `2a20fff`; build time `2026-06-26T06:36:39Z`; stdout `96` bytes / `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`.

## 14. User-credit canary

PASS; fresh total credit `3541`; logger/login failures `false / false`; no private account fields persisted.

## 15. Runtime Help and command contract

PASS; one help call only; stdout `2739` bytes / `fb3aa97d2d33b1d745a52519eac529c4a21a2d90aef9f1f6a452442fcf884277`. Initial local poll wording regex was inconclusive; the exact output hash matched existing committed parsed-help evidence proving poll-zero no-wait semantics. Help was not repeated.

## 16. Initial credit Gate

Required `960`; available `3541`; result `PASS`.

## 17. PUSH-01 result

Called once; return `0`; parse `PASS`; submit ID `65aa46f5-0125-4d07-8c6e-3fd5112d29a7`; log ID `202607271739501692540470081473810`; gen status `querying`; credit `140`; acceptance `PASS`; cumulative `140`.

## 18. IMPACT-01 result

Called once; return `0`; parse `PASS`; submit ID `b10cf271-288e-4fdb-925c-b4bd45856979`; log ID `202607271740431692540470082411FE2`; gen status `querying`; credit `140`; acceptance `PASS`; cumulative `280`.

## 19. IMPACT-02 result

Called once; return `0`; parse `PASS`; submit ID `3cfa385f-99c9-4e1f-871e-d52ff154ebae`; log ID `20260727174048169254047008595B9F0`; gen status `querying`; credit `140`; acceptance `PASS`; cumulative `420`.

## 20. PUSH-02 result

Called once; return `0`; parse `PASS`; submit ID `2258abca-2de6-4394-903f-7de609a7e711`; log ID `202607271740531692540470089885BB6`; gen status `querying`; credit `140`; acceptance `PASS`; cumulative `560`.

## 21. PUSH-03 result

Called once; return `0`; parse `PASS`; submit ID `3fbcdb18-24d2-4a43-9cd5-5c7d1de41011`; log ID `2026072717405916925404700884055BF`; gen status `querying`; credit `140`; acceptance `PASS`; cumulative `700`.

## 22. IMPACT-03 result

Called once; return `0`; parse `PASS`; submit ID `10193c64-b91e-454e-9118-6ab3a0cf1fb9`; log ID `2026072717410416925404700878131FB`; gen status `querying`; credit `140`; acceptance `PASS`; cumulative `840`.

## 23. Submit-ID uniqueness

Six nonempty submit IDs are unique: `true`.

## 24. Per-task and cumulative credit accounting

Per task `140`; cumulative `840`; maximum `960`; result `PASS`.

## 25. Actual process and operation counts

Dreamina processes `9`: version `1`, user_credit `1`, help `1`, submit `6`; query/download/retry/resubmit/batch/additional submit all `0`.

## 26. Exact eleven-file write set

Exactly eleven new artifacts were created:

- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/authorization.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/preflight.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/submits/push_01.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/submits/impact_01.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/submits/impact_02.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/submits/push_02.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/submits/push_03.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/submits/impact_03.json`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/execution.json`
- `reports/CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SUBMIT_RESULT.md`
- `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_SUBMIT/evidence_manifest.json`

## 27. Evidence coverage

Non-self output coverage `10/10`; committed-input coverage `18/18`; total unique bound paths `28`.

## 28. Sensitive-data result

PASS. Raw stdout/stderr, raw Provider responses, signed URLs, and private account fields were not persisted.

## 29. Source, Prompt, package, reference, media and protected-state result

Sources and all existing Prompt, package, reference, media, design, production, and protected files remained unchanged.

## 30. Blind-mapping boundary

Blind mapping, aliases, salt, commitment, review media, and review records were not created.

## 31. Query/download/review boundary

No query, download, or review occurred. Provider final generation statuses and visual content remain unknown.

## 32. C02/C03/R02 boundary

C02 reopened `false`; C03 authorized `false`; original R02 remains blocked; R02 authorized `false`.

## 33. Production/completion/final/lock boundary

production re-entry, production approval, fixed-task completion, final master, and lock all remain `false`.

## 34. Commit and push result

Pre-commit validation passed. This report is part of the one authorized commit; actual commit and push transport results are returned in the terminal receipt.

## 35. Exact next phase

`CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_QUERY_AUTHORIZATION_HUMAN_DECISION`. No query authority exists yet.
