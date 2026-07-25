# CAL-002 Route A Capability Audit and Minimum Calibration Design Result

## 1. Starting Checkpoint

- Goal identity: `CAL002_ROUTE_A_ACTION_REFERENCE_CAPABILITY_AUDIT_AND_MINIMUM_CALIBRATION_DESIGN_V0_1`
- Task label: `CAL002_ROUTE_A_CAPABILITY_AUDIT_AND_CALIBRATION_DESIGN_NO_LIVE`
- Repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- Branch: `main`
- Starting HEAD: `8803ae7ccaec354c703f67ded79bd01fc33eeaba`
- Starting origin/main: `8803ae7ccaec354c703f67ded79bd01fc33eeaba`
- Starting HEAD parent: `ac9e17486f769138e072332edba61c1d504751c6`
- Starting commit message: `decision(cal002): accept Batch05 result and compare reset routes v0.2`
- Parent-to-HEAD commit count: `1`
- Starting staged paths: `0`
- Starting tracked modifications: `0`
- Starting Source modifications: `0`
- Starting untracked baseline count: `26`
- Starting untracked-set SHA-256: `837ed63e692be6399b6725fd7c577a38e76b1303c8a670164b81eed4e4ad99e2`
- Prior transition: `8 added / 0 modified / 0 deleted / 0 renamed / 0 unexpected`

## 2. Exact Approval and Lifecycle

```text
APPROVE_CAL002_ROUTE_RESET_ROUTE_SELECTION_V0_1__BIND_ROUTE_RESET_CHECKPOINT_8803AE7CCAEC354C703F67DED79BD01FC33EEABA__BIND_ROUTE_RESET_DECISION_PACK_SHA256_5032CC253836DE503E3FD39429826C6C791959254149EB82334795C9C1392C8C__BIND_ROUTE_RESET_GOVERNANCE_REPORT_SHA256_DDD7887C1AFE60EC0A5AFC44B2BF61FE7B67F66F39FD040668A197ED49B0B404__SELECT_ACTION_REFERENCE_MOTION_CONTROL_FOR_NEXT_CAPABILITY_AND_CALIBRATION_DESIGN__AUTHORIZE_ONE_NO_LIVE_ROUTE_A_CAPABILITY_AUDIT_AND_MINIMUM_CALIBRATION_DESIGN__REQUIRE_RIGHTS_SAFE_ACTION_REFERENCE_PROVENANCE_AND_MOTION_ONLY_REFERENCE_DUTY__REQUIRE_PROVIDER_CAPABILITY_TO_REMAIN_UNVERIFIED_UNTIL_OFFICIAL_OR_COMMITTED_EVIDENCE_CONFIRMS_IT__KEEP_ROUTE_B_AS_CONTROLLED_RESEARCH_FALLBACK__KEEP_ROUTE_C_AS_PRODUCTION_FALLBACK__NO_DREAMINA_NO_PROVIDER_NO_SUBMIT_NO_QUERY_NO_DOWNLOAD_NO_RETRY_NO_RESUBMIT_NO_BATCH_NO_MEDIA_NO_REFERENCE_UPLOAD_NO_SOURCE_CHANGE_NO_PRODUCTION_REENTRY_NO_PRODUCTION_APPROVAL_NO_FIXED_TASK_COMPLETION_NO_FINAL_MASTER_NO_LOCK__ONE_TIME_NON_REUSABLE
```

- Approval received: `true`
- Approval byte length: `1002`
- Approval SHA-256: `d521adfe476c14d2189e5ef918ed10c1d8eb0268e8b86768829ba823473706cf`
- Authorization activated: `true`
- Authorization consumed: `true`
- Authorization reusable: `false`
- Activation event: first authorized Route A output write.
- Automatic retry authorized: `false`

## 3. Route Selection

- Selected route: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`
- Selection decision: `SELECT_ACTION_REFERENCE_MOTION_CONTROL_FOR_NEXT_CAPABILITY_AND_CALIBRATION_DESIGN`
- Selection scope: `CAPABILITY_AUDIT_AND_CALIBRATION_DESIGN_ONLY`
- Route selected: `true`
- Route activated: `false`
- Route execution authorized: `false`
- Live authority: `false`
- Reference-upload authority: `false`
- Media authority: `false`
- Production authority: `false`

Route A was selected because the accepted failures concern timing, contact rhythm, receiving-body consequence, exact footwork, recoil, release/retraction, and continued movement. Selection is not a claim that the route works.

## 4. Route-Reset Bindings

### Decision Pack

- Path: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_RESET_DECISION_V0_2/CAL002_ROUTE_RESET_DECISION_PACK_V0_2.md`
- Byte length: `20250`
- SHA-256: `5032cc253836de503e3fd39429826c6c791959254149eb82334795c9c1392c8c`
- Git blob: `f4da49fa8df81c8fb2cf8a46466e725d0e95194a`
- Worktree/HEAD equality: `true`

### Governance Report

- Path: `reports/CAL002_BATCH05_EXPERIMENT_RESULT_ACCEPTANCE_AND_ROUTE_RESET_DECISION_V0_2_RESULT.md`
- Byte length: `13556`
- SHA-256: `ddd7887c1afe60ec0a5afc44b2bf61fe7b67f66f39fd040668a197ed49b0b404`
- Git blob: `b56a4ec8ce82cc64e4ee0c9271ffb9815e25d6fe`
- Worktree/HEAD equality: `true`

## 5. Evidence Hierarchy and Bindings

Exactly 15 committed evidence files were used:

- Level 1: `6`
- Level 2: `7`
- Level 3: `2`

All 15 used files matched their `HEAD` blobs. Their path, byte length, SHA-256, Git blob, evidence level, and role are recorded in `CAL002_ROUTE_A_CAPABILITY_AUDIT_V0_1.md` and `route_a_evidence_manifest.json`.

The highest committed Source index is V1.12. The committed Batch05 design separately records the human-confirmed active Project Source index as V1.13. No V1.13 Source path is committed, so its bytes were not invented or used as capability proof.

No command-surface conflict was found among the used Level 1 evidence. A governance availability gap exists for the uncommitted V1.13 index. Project motion-duty rules guide design but do not prove Provider behavior.

## 6. Command-Surface Findings

Committed Level 1 evidence verifies:

- `multimodal2video` accepts repeated local image, video, and audio inputs;
- at least one image or video is required;
- image/video/audio limits are `9 / 3 / 3`;
- audio inputs are listed as 2-15 seconds;
- `seedance2.0_vip` is listed;
- output duration is 4-15 seconds;
- VIP output resolution choices are 720p, 1080p, and 4k;
- ratios are 1:1, 3:4, 16:9, 4:3, 9:16, and 21:9.

Committed Level 1 evidence does not define:

- semantic duties for each reference;
- motion-only transfer;
- identity, costume, scene, or camera separation;
- reference weighting or priority;
- exact action replication;
- deterministic repeatability;
- production suitability.

The existence of a video-input flag is not evidence of motion-only action transfer.

## 7. Capability Matrix Summary

The matrix contains `21` capabilities.

- `CLI_MULTIMODAL_VIDEO_INPUT_SURFACE`: `VERIFIED_COMMAND_SURFACE`
- `SEEDANCE2_VIP_MULTIMODAL_COMMAND_SURFACE`: `VERIFIED_COMMAND_SURFACE`
- `VIDEO_REFERENCE_COUNT_LIMIT`: `VERIFIED_COMMAND_SURFACE`
- `OUTPUT_DURATION_SURFACE`: `VERIFIED_COMMAND_SURFACE`
- `OUTPUT_RESOLUTION_SURFACE`: `VERIFIED_COMMAND_SURFACE`
- Motion semantics, action fidelity, leakage separation, weighting, repeatability, rights-safe asset availability, and route readiness: `UNVERIFIED`

- Provider capability verified: `false`
- Motion-only semantics verified: `false`
- Route A execution ready: `false`

## 8. Exact Capability Conclusion

`COMMAND_SURFACE_SUPPORT_VERIFIED_MOTION_ONLY_BEHAVIOR_UNVERIFIED`

Provider capability status:

`UNVERIFIED_PENDING_FUTURE_AUTHORIZED_CAPABILITY_VALIDATION`

No committed evidence proves Route A behavior or production suitability.

## 9. Rights and Provenance Gate

Allowed active-input rights classes:

1. `PROJECT_OWNED_3D_OR_ANIMATED_REFERENCE`
2. `SELF_RECORDED_WITH_DOCUMENTED_CONSENT`
3. `LICENSED_FOR_GENERATIVE_MODEL_INPUT`
4. `CONTRACTOR_CREATED_WITH_EXPLICIT_GENERATIVE_USE_RIGHTS`

Unknown-rights, public-reference-only, third-party entertainment, unlicensed social-media, nonconsensual real-person, private or sensitive, gore, unauthorized choreography, and unresolved upload/redistribution material are disallowed.

The provenance requirements define all mandatory identity, rights, consent, upload, derivative-use, commercial-use, retention, redistribution, privacy, duty, path, hash, technical, and human-review fields. The blank template contains no real path, hash, or asset identity.

- Real reference records created: `0`
- Rights-safe reference availability: `UNVERIFIED`
- Active-input approval remains human-only.

## 10. Motion-Only Duty Contract

Allowed duties are onset timing, pose progression, force direction, contact rhythm, weight transfer, receiver reaction, exact footwork, recoil, release/retraction, and continuing movement.

Prohibited copied duties include identity, face, body identity, costume, hairstyle, scene, architecture, props, lighting, grade, camera, framing, lens behavior, story, dialogue, music, and original-IP design.

Thirteen leakage classes are defined, including identity, face, body appearance, costume, scene, prop, camera, composition, lighting/color, story/IP, ignored motion, overdominant motion, and role conflict.

The contract is semantic and non-executable. It does not prove Provider enforcement.

## 11. Proposed Minimum Calibration

- Calibration ID: `CAL002-ROUTE-A-MIN-V0-1`
- Action families: `2`
- Planned references: `2`
- Planned outputs: `4`
- Replicates per family: `2`
- Proposed duration: `5 seconds`
- Proposed resolution: `1280x720` or verified 720p equivalent
- Model target: `seedance2.0_vip` only after future capability confirmation

Reference roles:

- `ACTION_REF_PUSH_01`
- `ACTION_REF_IMPACT_01`

Output aliases:

- `ROUTEA_PUSH_R01`
- `ROUTEA_PUSH_R02`
- `ROUTEA_IMPACT_R01`
- `ROUTEA_IMPACT_R02`

No reference asset, Prompt package, Provider manifest, executable command, upload plan, task, credit authority, or media was created.

## 12. Review and Stopping Criteria

Full MP4 review is mandatory for every future output. The Draft 2020-12 review schema requires exactly four aliases, technical validity, complete-MP4 confirmation, motion-chain fields, foot-result fields, static-tail timing, camera and identity checks, explicit reference-leakage fields, strict endpoint results, and two family summaries.

Minimum advancement screen:

- at least one strict push pass;
- at least one strict impact pass;
- no identity or scene leakage in either family;
- no repeated prolonged contact;
- no repeated long frozen ending;
- visibly more complete motion than the bounded Batch05 baseline;
- complete technical evidence;
- no rights or provenance defect;
- human expansion approval.

Exactly `14` stopping conditions are defined. Automatic expansion is `false`.

## 13. Route B and Route C Preservation

- Route B: `CAL002_ROUTE_B_MANUAL_POSE_START_END_FRAME_CONTROL`
- Route B status: `CONTROLLED_RESEARCH_FALLBACK_NOT_SELECTED`
- Route C: `CAL002_ROUTE_C_EDITORIAL_ACTION_DECOMPOSITION`
- Route C status: `PRODUCTION_FALLBACK_NOT_SELECTED`

No fallback switch or implementation package is authorized.

## 14. No-Live Confirmation

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Dreamina version/help/login/checklogin/user_credit: `0 / 0 / 0 / 0 / 0`
- Submit/query/download/retry/resubmit/batch: `0 / 0 / 0 / 0 / 0 / 0`
- External network search: `0`

## 15. Reference and Media Confirmation

- Reference files read: `0`
- Reference uploaded: `false`
- Reference media created: `false`
- Image/video/audio created: `false / false / false`
- Frame/contact-sheet/comparison-sheet creation: `0 / 0 / 0`
- Media changed: `false`

## 16. Source and Protected-State Confirmation

- Sources changed or synchronized: `false`
- Existing Route Reset V0.2 files changed: `false`
- Existing Batch05 files changed: `false`
- Existing review records changed: `false`
- Existing Prompt/package/design/schema files changed: `false`
- Existing CLI evidence changed: `false`
- Existing reports changed: `false`
- Protected files changed: `false`

## 17. Production Re-Entry Block

- CAL-002 formally closed: `false`
- Production re-entry: `BLOCKED_PENDING_CAPABILITY_VALIDATION_CALIBRATION_EXECUTION_AND_HUMAN_REVIEW`
- Production re-entry authorized: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- Final master: `false`
- Locked: `false`

No return to production is authorized.

## 18. Human Decision Required

The human must decide whether to accept:

- the conservative capability conclusion;
- the mandatory rights and provenance gate;
- the motion-only duty and leakage taxonomy;
- the two-reference/four-output minimum scope;
- the success screen and 14 stopping conditions;
- a later bounded capability-validation and calibration budget.

This Goal does not create that later authority.

## 19. Created-Path Boundary

Exactly ten paths are authorized:

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/CAL002_ROUTE_A_SELECTION_RECORD.md`
2. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/CAL002_ROUTE_A_CAPABILITY_AUDIT_V0_1.md`
3. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/route_a_capability_matrix.json`
4. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/route_a_reference_provenance_requirements.json`
5. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/CAL002_ROUTE_A_MOTION_ONLY_REFERENCE_DUTY_CONTRACT_V0_1.md`
6. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/CAL002_ROUTE_A_MINIMUM_CALIBRATION_DESIGN_V0_1.md`
7. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/route_a_calibration_review_schema.json`
8. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/route_a_calibration_manifest.json`
9. `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/route_a_evidence_manifest.json`
10. `reports/CAL002_ROUTE_A_CAPABILITY_AUDIT_AND_MINIMUM_CALIBRATION_DESIGN_RESULT.md`

Unexpected paths: `0`.

## 20. Decision and Next Phase

- Decision: `CAL002_ROUTE_A_CAPABILITY_AUDIT_AND_MINIMUM_CALIBRATION_DESIGN_COMPLETE_READY_FOR_HUMAN_REVIEW`
- Next phase: `CAL002_ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_HUMAN_DECISION`
