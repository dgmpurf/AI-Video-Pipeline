# CAL-002 Route A R01 Download Parser and Evidence Recovery Result

## 1. Executive Decision

- Decision: `CAL002_ROUTE_A_R01_DOWNLOAD_RECOVERY_TWO_VIDEOS_TECHNICALLY_VALID_READY_FOR_FULL_MP4_HUMAN_REVIEW`
- Next phase: `CAL002_ROUTE_A_R01_COMPLETE_MP4_HUMAN_VISUAL_AND_SEMANTIC_REVIEW`
- Provider and technical results remain separate from visual and semantic review.
- No visual pass or Route A capability is claimed.

## 2. Starting Checkpoint

- Starting HEAD / origin/main: `64b0e1bd53daa167ae53f08547be3c2294af3aff` / `64b0e1bd53daa167ae53f08547be3c2294af3aff`
- Expected parent: `65b1116e3fe4111bffa018f7c48adf65b2158d2e`
- Parent-to-HEAD transition: exactly 8 additions, 0 modifications, 0 deletions, 0 renames.

## 3. Approval Binding and Lifecycle

- Goal identity: `CAL002_ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1`
- Recovery execution ID: `CAL002-ROUTE-A-R01-DOWNLOAD-RECOVERY-V0-1`
- Approval bytes / SHA-256: `2895` / `62741ce6da710b78adfa224512c5da7adf54145fd1d11affb819b53c38f3b27e`
- Authorization activated / consumed / reusable: `true / true / false`

## 4. Failed Evidence and Prior Query Bindings

- Failed report bytes / SHA-256: `8541` / `967ad70079636d0e3f4a8221567762a5c5f7bbdf40d8246b0f1f4945625ba3c3`
- Failed evidence manifest Git blob: `3428f528fccfba33aaf25fbf7d69689460bfdbfe`
- Prior query-recovery report bytes / SHA-256: `11923` / `e28ccd5ed690b99efe89f2fa2c49831c99b2e96c3aad836a24e0c21b5f06a32c`
- Prior PUSH and IMPACT query receipts remain authoritative: success / Finish / one video / download-ready.

## 5. Parser, Evidence, and Payload Self-Tests

- Classes / cases / passed: `7 / 37 / 37`
- Result: `PASS`
- Status parser preserves strings, integers, null, and booleans without inventing numeric semantics.
- Process metadata and filesystem facts are checkpointed before status interpretation.
- Payload cleanup remains blocked until canonical move or durable bounded-failure evidence.
- Dreamina calls / repository writes during self-tests: `0 / 0`

## 6. Exact Call Count and Order

- Actual Dreamina/download calls: `2`
- Call order: `['ROUTEA_PUSH_R01', 'ROUTEA_IMPACT_R01']`
- Version / Help / additional query-only calls: `0 / 0 / 0`
- Submit / generation retry / resubmit / batch: `0 / 0 / 0 / 0`
- User-credit / login / session / list-task calls: `0 / 0 / 0 / 0`

## 7. Per-Task Results

### ROUTEA_PUSH_R01

- Called / accepted: `True` / `True`
- Not-called reason: `None`
- Process exit code: `0`
- Stdout bytes / SHA-256: `3149` / `fe2795b06104c922fe155aff42edecb61b308f1805f6e320a9a51128dde2d10c`
- Stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Argv elements / SHA-256: `6` / `19dd0639b2241c9a9f038338d01118ba790f9b86f48dc9fa0cb4e6f2892662b5`
- Capture before parse / durable checkpoint: `True` / `True`
- Raw gen status: `string` / `success` / `SUCCESS`
- Raw queue status: `string` / `Finish` / `FINISH`
- Explicit failure contradictions: `[]`
- Filesystem regular files / result: `1` / `PASS`
- Candidate bytes / SHA-256: `2112498` / `bee521eea1f44608cbf15e8bae423caea99f49581b5c37e693e187b9a13f27e4`
- Preliminary ffprobe / pre-move decode: `PASS` / `PASS`
- Byte-preserving move: `PASS`
- Canonical path: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/media/ROUTEA_PUSH_R01.mp4`
- Canonical bytes / SHA-256: `2112498` / `bee521eea1f44608cbf15e8bae423caea99f49581b5c37e693e187b9a13f27e4`
- Post-move ffprobe / decode: `PASS` / `PASS`
- Keyframes / contact sheet: `6` / `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/contact_sheets/ROUTEA_PUSH_R01_contact_sheet.png`

### ROUTEA_IMPACT_R01

- Called / accepted: `True` / `True`
- Not-called reason: `None`
- Process exit code: `0`
- Stdout bytes / SHA-256: `3145` / `28661a13346154177c3800745192932a3fbf17b9017cf27619bde0eaaf10951c`
- Stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Argv elements / SHA-256: `6` / `5ba0720275444eb5865576c7004a095081dedac53a8f8012f699fc1ed1b8e8b1`
- Capture before parse / durable checkpoint: `True` / `True`
- Raw gen status: `string` / `success` / `SUCCESS`
- Raw queue status: `string` / `Finish` / `FINISH`
- Explicit failure contradictions: `[]`
- Filesystem regular files / result: `1` / `PASS`
- Candidate bytes / SHA-256: `2232992` / `6f3ff60b3d24ac90a3700b7bda9065e16f6b0ecfb109d4a4f9165d8229ccbea0`
- Preliminary ffprobe / pre-move decode: `PASS` / `PASS`
- Byte-preserving move: `PASS`
- Canonical path: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/media/ROUTEA_IMPACT_R01.mp4`
- Canonical bytes / SHA-256: `2232992` / `6f3ff60b3d24ac90a3700b7bda9065e16f6b0ecfb109d4a4f9165d8229ccbea0`
- Post-move ffprobe / decode: `PASS` / `PASS`
- Keyframes / contact sheet: `6` / `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/contact_sheets/ROUTEA_IMPACT_R01_contact_sheet.png`

## 8. Review Artifacts and Cleanup

- Validated canonical videos: `2`
- Keyframes: `12`
- Contact sheets: `2`
- Review handoff: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/review/ROUTE_A_R01_VISUAL_REVIEW_HANDOFF.md`
- Temporary parent cleaned: `true`
- Signed URLs persisted / opened: `false / false`
- Raw Provider output persisted: `false`
- Temporary absolute paths persisted: `false`

## 9. Governance Boundary

- No prior media, Prompt, package, manifest, review artifact, Source, or protected file was modified.
- Complete MP4 human and ChatGPT Pro review remains mandatory before any Route A capability or R02 decision.
- Motion-only behavior verified: false
- Reference leakage reviewed: false
- Route A capability proven: false
- R02 authorized: false
- Automatic expansion: false
- Production re-entry authorized: false
- Production approved: false
- Fixed-task completion: false
- Final master: false
- Locked: false
