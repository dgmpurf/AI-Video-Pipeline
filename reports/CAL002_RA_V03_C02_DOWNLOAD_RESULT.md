# CAL-002 Route A V0.3 C02 Download Result

## 1. Decision
- Actual decision: `CAL002_ROUTE_A_V0_3_C02_MATCHED_PAIR_DOWNLOAD_SUCCESS_TECHNICAL_VALIDATION_PASS`
- Next phase: `CAL002_ROUTE_A_V0_3_MATCHED_PAIR_CANARY_C02_COMPLETE_MP4_HUMAN_REVIEW`
- Starting checkpoint: `e49f67fa514feceaa2baa59775174ab95a54d6d3`

## 2. Authorization
- Goal identity: `CAL002_ROUTE_A_V0_3_MATCHED_PAIR_CANARY_C02_MAX_TWO_DOWNLOAD_ONLY_MEDIA_FIRST_TECHNICAL_VALIDATION_V0_1`
- Execution ID: `CAL002-ROUTE-A-V0-3-C02-MAX-TWO-DOWNLOAD-ONLY-MEDIA-FIRST-V0-1`
- Matched-pair ID: `CAL002-ROUTE-A-V0-3-C02-CAUSAL-ISOLATION-MATCHED-PAIR`
- Authorization bytes / SHA-256 / Base64 characters: `5193` / `017a4232798f75f166c87d4fca156dd6d6f0cb103aa023bf262a5582619a7f7b` / `6924`
- Deterministic UTF-8 Base64 decode count: `1`
- Authorization round-trip: `PASS`
- Authorization activated / consumed / reusable: `true / true / false`

## 3. Query Evidence Binding
- Query authorization, preflight, PUSH receipt, IMPACT receipt, execution, evidence manifest, and governance report: `PASS`.
- Query evidence coverage: `6/6`.
- PUSH submit ID / download-ready: `e0d50a2a-d8c8-4d32-9838-a76a8cad4fed` / `true`.
- IMPACT submit ID / download-ready: `8f4e9bf1-bdce-4653-a92a-6041dcf779c3` / `true`.
- Reference cross-contamination: `false`.

## 4. Temporary Policy And Process Order
- Task-specific temporary root: `G:/AICODING/AI_VIDEO/_temp/CAL002_RA_V03_C02_DLOAD_V0_1`.
- It was absent before activation, outside the repository, on G:, and split into initially empty `push` and `impact` directories.
- Fixed process order: `version -> user_credit -> query_result -h -> PUSH download -> IMPACT download`.
- Actual Dreamina processes: `5` of maximum `5`.

## 5. Canaries And Download Contract
- Version canary: `PASS`.
- Version / commit / build time: `2a20fff-dirty` / `2a20fff` / `2026-06-26T06:36:39Z`.
- User-credit canary: `PASS`; fresh total credit: `3541`.
- Private account fields persisted: `false`.
- query_result help canary: `PASS`.
- Download command contract: `PASS`.
- Raw command output and signed URL values persisted: `false / false`.

## 6. PUSH Download And Technical Validation
- Exact argv bytes / SHA-256: `185` / `d7bbb9bac16a473aef1f04afce2300315157021053857c042c3506eecc30ccc4`.
- Called / call count: `true` / `1`.
- Process return / timeout / exception: `0` / `false` / `null`.
- Materialized regular files / MP4s: `1` / `1`.
- Media-first / temporary technical result: `PASS` / `PASS`.
- Temporary bytes / SHA-256: `2140523` / `814a2a183247b99c28bb86594aa054a7ae3891c4c9ac0612f6081788fdc35e18`.
- ffprobe / full decode / metadata: `PASS` / `PASS` / `PASS`.
- Video/audio/other streams: `1` / `1` / `0`.
- Codec / pixel format / dimensions: `h264` / `yuv420p` / `1280x720`.
- Duration / rotation / frame evidence: `5.085011` / `0` / `121`.

## 7. IMPACT Gate, Download And Technical Validation
- PUSH gate permitting IMPACT: `true`.
- Exact argv bytes / SHA-256: `187` / `909fd2df18b4387a1bf1b4985d1620dff158e191b5238b56268b46c42153eb46`.
- Called / call count / reason not called: `true` / `1` / `null`.
- Process return / timeout / exception: `0` / `false` / `null`.
- Materialized regular files / MP4s: `1` / `1`.
- Media-first / temporary technical result: `PASS` / `PASS`.
- Temporary bytes / SHA-256: `2217491` / `d9116ee8798f4f0c0a5957fb1988880c1b1f8d06dfd36005f1de9c327bc8e1cb`.
- ffprobe / full decode / metadata: `PASS` / `PASS` / `PASS`.
- Video/audio/other streams: `1` / `1` / `0`.
- Codec / pixel format / dimensions: `h264` / `yuv420p` / `1280x720`.
- Duration / rotation / frame evidence: `5.085011` / `0` / `121`.

## 8. Both-Media Gate And Canonicalization
- Both-media gate: `true`.
- Canonicalization performed: `true`.
- PUSH canonical path: `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_DLOAD/media/ROUTEA_PUSH_V03_C02.mp4`.
- PUSH canonical bytes / SHA-256: `2140523` / `814a2a183247b99c28bb86594aa054a7ae3891c4c9ac0612f6081788fdc35e18`.
- PUSH pre/post equality: `true`.
- IMPACT canonical path: `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V03_C02_DLOAD/media/ROUTEA_IMPACT_V03_C02.mp4`.
- IMPACT canonical bytes / SHA-256: `2217491` / `d9116ee8798f4f0c0a5957fb1988880c1b1f8d06dfd36005f1de9c327bc8e1cb`.
- IMPACT pre/post equality: `true`.
- Generated MP4 hashes identical: `false`.

## 9. Cleanup, Evidence And Protected State
- Temporary cleanup / root remains / regular files remaining: `PASS` / `false` / `0`.
- Exact outcome write set: `11` new paths.
- Evidence coverage: `10/10`.
- Sensitive-data scan: `PASS`.
- Source, Prompt, package, reference, prior media, and protected state changed: `false / false / false / false / false / false`.
- Commit and push are performed only after this report and all evidence pass validation; the terminal receipt records the resulting commit and transport state.

## 10. Governance Boundary
- New submit / query-only / retry / resubmit / batch calls: `0 / 0 / 0 / 0 / 0`.
- Download calls: `2`.
- Contact sheets, review frames, semantic comparison, and complete-MP4 visual review: `not performed`.
- Route A capability proven: `false`.
- Automatic C03 authorized / R02 authorized / production re-entry authorized: `false / false / false`.
- production_approved / fixed_task_completion / final_master / locked: `false / false / false / false`.

Both canonical MP4 files passed technical validation and full decoding.
Complete-MP4 visual comparison has not yet been performed. Technical validity
does not establish reference-specific motion adherence or Route A capability.

## 11. Next Phase
`CAL002_ROUTE_A_V0_3_MATCHED_PAIR_CANARY_C02_COMPLETE_MP4_HUMAN_REVIEW`
