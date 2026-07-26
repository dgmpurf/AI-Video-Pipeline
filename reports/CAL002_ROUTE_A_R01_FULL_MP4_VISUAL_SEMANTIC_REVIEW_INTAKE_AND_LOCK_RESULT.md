# CAL-002 Route A R01 Full-MP4 Visual Semantic Review Intake and Lock Result

## 1. Executive Decision

- Decision: `CAL002_ROUTE_A_R01_FULL_MP4_VISUAL_SEMANTIC_REVIEW_LOCKED_ORIGINAL_R02_BLOCKED_READY_FOR_REFERENCE_V0_2_DECISION`
- Next phase: `CAL002_ROUTE_A_CLEAN_FULL_DURATION_MULTI_BEAT_REFERENCE_V0_2_LOCAL_DESIGN_AND_CREATION_DECISION`

## 2. Starting Checkpoint and Scope

- Starting HEAD / origin/main: `523bdf9a25a1856688fb192bc5879f24d89138b8` / `523bdf9a25a1856688fb192bc5879f24d89138b8`
- Parent: `64b0e1bd53daa167ae53f08547be3c2294af3aff`
- Starting transition: exactly 27 additions confined to the Route A R01 recovery root and its governance report.

## 3. Approval and Input Bindings

- Approval bytes / SHA-256: `2043` / `43dd9a587d7f2bf1bc0a58f44b4e0adfc0058f3be03a77ae17e5434790cac792`
- Authorization activated / consumed / reusable: `true / true / false`
- Input ZIP bytes / SHA-256: `5079` / `604ff1ab764f069c86867c08b8bf6f9f62f6a242e4aab2e81b316860b898e515`
- Review JSON bytes / SHA-256: `7725` / `4a9c391cff821a64d89da99589b705fc277c0e52e101c8a149ab057abe110cd1`
- Review Markdown bytes / SHA-256: `3054` / `28e73d588e0af88de7b519e2d6f6df97743c0a46cc7067d8340e2f036516f0ea`
- Human project-owner acceptance received: `true`

## 4. Committed Evidence Bindings

- Download-recovery report: `6127` bytes / `9d429cb80dfae81399ed08769a275d6116c21711a362591206effdab84101baa`
- Visual-review handoff: `5548` bytes / `c81060f5d6ffc3c437f8306b6c3df647d1c9f09fe0f446b9f17e1b9bde68a0fa`
- Review contract Git blob: `176bc0d2b619bd20e36a33c77c0fe64b37e47d45`
- Review-contract validation / JSON-Markdown consistency: `PASS / PASS`

## 5. ROUTEA_PUSH_R01 Review

- Media bytes / SHA-256: `2112498` / `bee521eea1f44608cbf15e8bae423caea99f49581b5c37e693e187b9a13f27e4`
- Complete MP4 reviewed / technical validity: `true / PASS`
- Action-family result: `FAIL`
- Motion-reference result: `WEAK_FRAGMENT_ONLY`; reference mostly ignored.
- Foot result: absent, count `0`.
- Meaningful action duration: under `0.2s`; long static tail approximately `4.86s`.
- Material sentinel count: `0`; strict primary pass: `false`.

## 6. ROUTEA_IMPACT_R01 Review

- Media bytes / SHA-256: `2232992` / `6f3ff60b3d24ac90a3700b7bda9065e16f6b0ecfb109d4a4f9165d8229ccbea0`
- Complete MP4 reviewed / technical validity: `true / PASS`
- Core motion signal: positive; action-family result: `PASS`.
- Post-contact causality and one `REAR_FOOT_RECOIL_STEP`: present.
- Material sentinel: `CONTACT_MARKER_COPY`; count `1`.
- Motion-reference overdominance: `true`.
- Meaningful action duration approximately `0.7s`; long static tail approximately `3.99s`.
- Strict primary pass: `false`.

## 7. Overall Semantic Gate

- Semantic gate: `CANARY_REFERENCE_OVERDOMINANT_ROUTE_A_BLOCK`
- Positive evidence: video reference influenced the intended IMPACT core motion sequence.
- Negative evidence: material contact-marker copying contradicts motion-only role separation.
- Route A capability proven / motion-only behavior verified: `false / false`
- Original R02 blocked / R02 authorized: `true / false`
- Automatic expansion: `false`

## 8. Duration and Future Reference Finding

- Duration utilization: `SEVERE_UNDERUTILIZATION`
- Future reference class: `CLEAN_PROJECT_OWNED_FULL_DURATION_MULTI_BEAT_REFERENCE_V0_2`
- Remove contact markers, grids, and distinctive calibration-stage cues.
- Motion should span nearly the complete five seconds with no long static tail.
- Required density: two to three causal action beats, or four to six connected micro-action beats.
- This Goal does not authorize or create V0.2 media.

## 9. Locked Records

- Final review record: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/review_records/CAL002-ROUTE-A-R01-SEMANTIC-REVIEW-LOCK-4A9C391C/route_a_r01_full_mp4_visual_semantic_review_record_final.json`
- Final review report: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/review_records/CAL002-ROUTE-A-R01-SEMANTIC-REVIEW-LOCK-4A9C391C/route_a_r01_full_mp4_visual_semantic_review_report.md`
- Lock manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_R01_DOWNLOAD_PARSER_AND_EVIDENCE_RECOVERY_MAX_TWO_DOWNLOAD_V0_1/review_records/CAL002-ROUTE-A-R01-SEMANTIC-REVIEW-LOCK-4A9C391C/route_a_r01_full_mp4_visual_semantic_review_lock_manifest.json`
- Lock manifest bytes / SHA-256: `8097` / `403d7d2bf2c84d2ada86c40add7d367c9e4b20842df38c60a487b8138304fa02`

## 10. Explicit Non-Actions and Protected State

- Dreamina / Provider called: `false / false`
- Submit / query / download / retry / resubmit / batch: `false / false / false / false / false / false`
- Canonical media, keyframes, contact sheets, Prompts, packages, prior evidence, and Sources changed: `false`
- Production re-entry / approval / fixed completion / final master / locked: `false / false / false / false / false`
- No signed URL, credential, raw Provider output, account identifier, temporary absolute path, or private environment value was persisted.
