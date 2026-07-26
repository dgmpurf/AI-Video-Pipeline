# CAL-002 Route A V0.2 C01 IMPACT Media-First Salvage Result

## 1. Decision and next phase
Decision: `CAL002_ROUTE_A_V0_2_C01_IMPACT_MEDIA_FIRST_SALVAGE_SUCCESS`.
Next phase: `CAL002_ROUTE_A_V0_2_MATCHED_PAIR_CANARY_C01_COMPLETE_MP4_HUMAN_REVIEW`.

## 2. Starting checkpoint
HEAD/origin: `43136845f0574e8c9c6936bf94bb51364cd26567` / `43136845f0574e8c9c6936bf94bb51364cd26567`; aligned: `true`.

## 3. Approval and lifecycle
Approval bytes/SHA-256: `4118` / `8b572765e2077cb04deff3357f11e457d05f8dc113afefd6b5535de25ca29d2e`.
Authorization activated/consumed/reusable: `true/true/false`.

## 4. PUSH continuity
PUSH report SHA: `3750ccc2acc8c14a316cbca9c573985f8debd57bfc4f3b0e46ad4ac3be3b475a`.
PUSH manifest blob/bytes/SHA: `0257e67896953b92dd5159d265b110ff860b189b` / `6518` / `94edf6fce2cda74edf2dc2c51707a63219b7f91d1828e3a56d30d5edbd17033a`.
PUSH technical/media/execution SHAs: `b1eb91783ec3a33c57d09db6efc09f640ac779d961aee8e3b49ad702a9383b1f` / `015fbb4dcb1624268314466408fc56a61e73a1efe529da774225a4513aae7d40` / `626da903a4d8867a1a824c66bfbe37be48db60e0af71382b5832df5bd28283a3`.

## 5. IMPACT authoritative query
Receipt SHA: `f8407729a21ab68048b5bf3508b1eb047433bcca29e614708d69d8a05de47d45`; task `success/Finish`, result/video `1/1`, download ready `true`.

## 6. Offline self-test
Iterations authorized/performed: `3/2`.
Iteration 1 suite passed `171/171`, then the integrated pre-activation continuity check exposed a local attestation-field comparison defect; Dreamina/Provider/repository writes remained `0/0/0`.
Iteration 2 complete regression suite: `PASS` with `174/174` passing.
Final tests/passes/failures/errors: `174/174/0/0`.
Cross-drive tests/passes/commonpath calls: `15/15/0`.
Handler bytes/SHA: `74213` / `4944eba2886dbe56580a74cc24e0296e51fbac88994eaa79c55254474b1519e6`; harness bytes/SHA: `41920` / `9c39578a0e72d04842f653f055b04bf524a404723ab0f38a247f93ce4be110ad`.

## 7. Exact one-call boundary
Dreamina/IMPACT/PUSH/second-IMPACT calls: `1/1/0/0`; Help/version/user-credit/query-only/retry/resubmit/new-submit/batch: `0`.

## 8. Exact IMPACT argv
Six-element compact JSON bytes/SHA: `182` / `9446946d56392f25e90db2fac77a80bbf8e9f0e668a570ecdcf116010b306de2`; shell `false`.

## 9. Durable pre-parse checkpoint
External checkpoint bytes/SHA: `2664` / `b5fa3e170b949d97e8ddf1ae5744b0296bd297e08f7f4f7ad86dcad38b508114`; written before parse/reread `true/PASS`.

## 10. Process result
Launched/return/timeout/exception: `true/0/false/None`.
Start/end/elapsed: `2026-07-26T16:24:47.945Z` / `2026-07-26T16:24:56.875Z` / `8.93` seconds.
stdout bytes/SHA: `4043` / `a2787303b28f137c30c490ab4bd06259b2e0ce8b53a39b9eb6c3d2991709369b`; stderr bytes/SHA: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## 11. Parse and sanitization
Mode/response ID/match/contradiction: `complete_json` / `4c8b6184-7c0a-4b41-95f5-e215e35f195b` / `true` / `false`.
Result/video/signed URLs: `None/None/0`.
Raw stdout/stderr, signed URL values, and raw Provider output persisted: `false/false/false`.

## 12. Filesystem delta
Result/pre-post entries/files/MP4/unexpected: `PASS/0-1/1/1/0`.
Links/reparse/path escapes: `0/0/0`.

## 13. Candidate binding
`4c8b6184-7c0a-4b41-95f5-e215e35f195b_video_1.mp4`: `2304263` bytes / `7368cf7f0748b54e928869de7eeb78c47ad71190cb3ff1d27937bdaa349dfb0e`.

## 14. Technical validation
Pre-move ffprobe/decode/metadata: `0/0/PASS`; duration/fps/frames `5.085011/24.119601328903656/121`; streams `1/1`; codec/pixel/rotation `h264/yuv420p/0`.

## 15. Media-first outcome
Acceptance/classification/CLI anomaly/Provider failure inferred: `PASS/USABLE_MEDIA_WITH_ZERO_EXIT/false/false`.

## 16. Canonical IMPACT media
Path `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_IMPSALVAGE/media/ROUTEA_IMPACT_V02_C01.mp4`; `2304263` bytes / `7368cf7f0748b54e928869de7eeb78c47ad71190cb3ff1d27937bdaa349dfb0e`; byte-preserving move `PASS`.

## 17. Post-move validation
ffprobe/decode/metadata: `0/0/PASS`.

## 18. Matched-pair availability
PUSH: `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_DLSALVAGE/media/ROUTEA_PUSH_V02_C01.mp4` / `3031614` / `015fbb4dcb1624268314466408fc56a61e73a1efe529da774225a4513aae7d40`.
IMPACT: `experiments/CAL-002/ACTION_CALIBRATION_V1/RA_V02_C01_IMPSALVAGE/media/ROUTEA_IMPACT_V02_C01.mp4` / `2304263` / `7368cf7f0748b54e928869de7eeb78c47ad71190cb3ff1d27937bdaa349dfb0e`.

## 19. Write set and evidence
Created paths: `8`; coverage `7/7`.

## 20. Temporary cleanup
Download/checkpoint/self-test roots cleaned: `true/true/true`; temporary files `0`.

## 21. Boundaries
PUSH, retry, second IMPACT, Source change, PUSH-media change, other prior-media change, and R02 execution: `0/0/0/0/0/0/0`.
Complete visual review, visual success, reference leakage review, motion-only verification, and Route A capability proof: `false/false/false/false/false`.

## 22. Failure details
Primary failure classification: `None`; sanitized excerpts: `0`; unresolved gaps: `0`.

## 23. Governance
original_R02_blocked=true
R02_authorized=false
production_approved=false
fixed_task_completion=false
final_master=false
locked=false

Both canonical matched-pair MP4s are now locally available and technically validated, but complete visual review remains mandatory before any Route A capability, R02, production, completion, final-master, or lock decision.
