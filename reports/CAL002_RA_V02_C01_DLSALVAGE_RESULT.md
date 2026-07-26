# CAL-002 Route A V0.2 C01 PUSH Media-First Salvage R3 Result

## 1. Decision and next phase
Decision: `CAL002_ROUTE_A_V0_2_C01_PUSH_MEDIA_FIRST_SALVAGE_SUCCESS`.
Next phase: `CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_IMPACT_MEDIA_FIRST_DOWNLOAD_RECOVERY_HUMAN_DECISION`.

## 2. Starting checkpoint
HEAD/origin: `2b0afdaf36b90009d7a2a776ad8559836ae3ea50` / `2b0afdaf36b90009d7a2a776ad8559836ae3ea50`; aligned: `true`.

## 3. Fresh approval and lifecycle
Approval bytes/SHA-256: `3796` / `b13183c1c5469b7b34d09c23afa053943d88b319f836582316f66dea2df29d29`.
Authorization activated/consumed/reusable: `true/true/false`.

## 4. Superseded prior approval
Prior approval bytes/SHA-256: `5176` / `5e43cb7379859f0642192b996ca29a2f895b3c33a5526954de93a5dc44622302`; prior activated/consumed/reusable: `false/false/false`.

## 5. Prior cross-drive failure
Prior formal self-test: `70` tests, `69` passes, `1` error from cross-drive commonpath use.

## 6. User-directed offline validation
User-directed offline corrected self-check: `73/73`, Dreamina calls `0`, repository writes `0`.

## 7. Cross-drive-safe correction
Drive or UNC anchors are compared before commonpath. Different anchors return outside without calling commonpath; relative paths are rejected.

## 8. Formal corrected self-test
Tests/passes/failures/errors: `141/141/0/0`; suite invocations `1`.
Cross-drive tests/passes/commonpath calls: `15/15/0`.
Handler bytes/SHA: `74256` / `240206853ee686721bf68298d5ee71a816c58b44136bdf1a36579dfe8985a2d1`. Harness bytes/SHA: `33735` / `641e8d8d5dfacf3f60731e7e1bb60c7e8d1bd8f470f0c6883cdfdad54539f43f`.

## 9. Diagnostic and query bindings
DLDIAG report/manifest SHA: `e25b3103ca15f4667fcdcf29798a70989651a2e7fc5b6aac9a749aa366f8fb17` / `d83aa3cfcff2fe8bcc40b5fc8e1d9b18e1b1525ba800d2155d28d5326c58ce32`.
QRYREC report/manifest SHA: `473aeccab818a2d92d3562b2d8bfcc55d485f015008914a1d866aedbe8ab40ed` / `45db71f77c3d0f7450ec206255986fd431064426dcbaec24866c0bffce82d72e`.

## 10. Prior candidate
`1669872` bytes / `f045a4cf65d962f6e19fbf171a2535633a038ed59c33a32a8e7b096fbbc315c3`; prior ffprobe/decode/metadata: `PASS/PASS/PASS`.

## 11. Media-first contract
The committed PUSH query receipt remains authoritative; the CLI call is evaluated as media transfer. Return codes `0` and `1` are allowed.

## 12. Exact one-call boundary
Dreamina/PUSH/IMPACT/second-PUSH calls: `1/1/0/0`; Help/version/user-credit/additional-query/retry/resubmit/new-submit/batch: `0`.

## 13. Exact R3 argv
Six-element compact JSON bytes/SHA: `180` / `b60b3f4babf02c859c1415083e71ae4ddd1399347e5d98532700af6717e20f62`; shell `false`.

## 14. Durable pre-parse checkpoint
External checkpoint bytes/SHA: `2624` / `1cef50250bb2b521f6dabdc8fc1bb1cab21e1fd97b46c107242d7f77a011d77c`; before parse/reread: `true/PASS`.

## 15. Process result
Launched/return code/timeout/exception: `true/0/false/None`.
Start/end/elapsed: `2026-07-26T15:50:49.513Z` / `2026-07-26T15:51:00.903Z` / `11.389` seconds.
stdout bytes/SHA: `3999` / `3348dcba731887b6cf8d44679e9b2e0aa551cd539400ef88534bc9ffa089388f`. stderr bytes/SHA: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## 16. Parse and sanitization
Mode/response submit ID/explicit contradiction/signed URLs: `complete_json` / `5ff0ba35-5a2c-445a-8343-c95f31caaf4a` / `false` / `0`.
Raw stdout/stderr, signed URL values, and raw Provider output persisted: `false/false/false`.

## 17. Filesystem delta
Result/regular files/MP4/unexpected: `PASS/1/1/0`.
Links/reparse/path escapes: `0/0/0`.

## 18. Fresh candidate and comparison
`5ff0ba35-5a2c-445a-8343-c95f31caaf4a_video_1.mp4`: `3031614` bytes / `015fbb4dcb1624268314466408fc56a61e73a1efe529da774225a4513aae7d40`; prior/fresh byte and SHA equality `false/false`.

## 19. Technical validation
Pre-move ffprobe/decode/metadata: `0/0/PASS`; duration/fps/frames `5.06195/24.119601328903656/121`; streams `1/1`; codec/pixel/rotation `h264/yuv420p/0`.

## 20. Media-first outcome
Acceptance/classification/CLI anomaly/Provider failure inferred: `PASS/USABLE_MEDIA_WITH_ZERO_EXIT/false/false`.

## 21. Canonical media and move
Path `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_DLSALVAGE/media/ROUTEA_PUSH_V02_C01.mp4`; `3031614` bytes / `015fbb4dcb1624268314466408fc56a61e73a1efe529da774225a4513aae7d40`; byte-preserving move `PASS`.

## 22. Post-move validation
ffprobe/decode/metadata: `0/0/PASS`.

## 23. Write set and evidence coverage
Created paths: `8`; coverage `7/7`.

## 24. Temporary cleanup
Download/checkpoint/self-test roots cleaned: `true/true/true`; temporary files `0`.

## 25. Boundaries
IMPACT, retry, second PUSH, Source change, prior-media change, and R02 execution: `0/0/0/0/0/0`.
Complete visual review, visual success, reference leakage review, motion-only verification, and Route A capability proof: `false/false/false/false/false`.

## 26. Failure details
Primary failure classification: `None`; sanitized excerpts: `0`; unresolved gaps: `0`.

## 27. Final governance
original_R02_blocked=true
R02_authorized=false
production_approved=false
fixed_task_completion=false
final_master=false
locked=false
