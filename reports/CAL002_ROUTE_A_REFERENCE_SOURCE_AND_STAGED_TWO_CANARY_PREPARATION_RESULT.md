# CAL-002 Route A Reference Source And Staged Two-Canary Preparation Result

## 1. Starting Checkpoint

- Branch: `main`
- Starting HEAD: `a605c7993c81ec396767ffcdfbb2f1c95db74a40`
- Starting origin/main: `a605c7993c81ec396767ffcdfbb2f1c95db74a40`
- Expected parent: `8803ae7ccaec354c703f67ded79bd01fc33eeaba`
- Starting commit message: `design(cal002): audit Route A and define minimum calibration`
- HEAD/origin aligned at preflight: `true`
- Staged paths at preflight: `0`
- Tracked modifications at preflight: `0`
- Source modifications at preflight: `0`
- Pre-existing untracked baseline count: `26`

The parent-to-HEAD transition was verified as ten added paths and zero modified, deleted, renamed, or unexpected paths.

## 2. Exact Approval And Lifecycle

The exact human approval is preserved in `CAL002_ROUTE_A_HUMAN_DESIGN_DECISION_RECORD.md`.

- Approval byte length: `1139`
- Approval SHA-256: `2d7bfa9641c990f2680df4220c2300e9c4f38276f75a31e2bce7c29d5a10b22c`
- Authorization activated immediately before first repository write: `true`
- Authorization consumed: `true`
- Authorization reusable: `false`
- Automatic retry authority: `false`

The approval authorizes only this no-live preparation pack.

## 3. Accepted Route A Audit Binding

- Accepted report: `reports/CAL002_ROUTE_A_CAPABILITY_AUDIT_AND_MINIMUM_CALIBRATION_DESIGN_RESULT.md`
- Bytes: `13141`
- SHA-256: `dfbfc04ad1f6b6997fc7034363f0ab4fb1f7697c46aa0918a8afcf60253d8b56`
- Accepted decision: `CAL002_ROUTE_A_CAPABILITY_AUDIT_AND_MINIMUM_CALIBRATION_DESIGN_COMPLETE_READY_FOR_HUMAN_REVIEW`
- Evidence manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_V0_1/route_a_evidence_manifest.json`
- Evidence manifest bytes: `9473`
- Evidence manifest SHA-256: `a90a21b490bdf853aa3f3d96e07bf66bd1a11cdd08696911c8be06661a1ccd09`
- Revalidated bound entries: `24`
- Binding failures: `0`

Accepted capability conclusion:

`COMMAND_SURFACE_SUPPORT_VERIFIED_MOTION_ONLY_BEHAVIOR_UNVERIFIED`

Provider capability remains:

`UNVERIFIED_PENDING_FUTURE_AUTHORIZED_CAPABILITY_VALIDATION`

The command surface can accept a video input. No accepted evidence proves motion-only Provider behavior, duty separation, exact motion fidelity, leakage prevention, repeatability, or production suitability.

## 4. Accepted Human Decisions

- Capability conclusion accepted: `true`
- Rights-safe provenance gate accepted: `true`
- Motion-only duty contract accepted: `true`
- Reference-leakage taxonomy accepted: `true`
- Two-reference/four-output minimum design accepted: `true`
- Replicates per family: `2`
- Staged execution accepted: `true`
- Selected route: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`
- Route A selected: `true`
- Route A activated: `false`
- Route A execution authorized: `false`

## 5. Project-Owned 3D Reference-Source Strategy

- Strategy ID: `CAL002_ROUTE_A_PROJECT_OWNED_NEUTRAL_3D_ACTION_REFERENCE_SOURCE`
- Preferred source: `PROJECT_OWNED_3D_OR_ANIMATED_REFERENCE`
- Planned references: `2`
- Actual software selected: `false`
- External asset selected: `false`
- Existing asset claimed: `false`
- Reference media created: `false`

The cleanest future source is a project-created neutral mannequin, rig, animation, materials, camera, background, lighting, and render. No current asset, path, hash, software, or external source is selected.

## 6. Rights And Asset-Component Requirements

Future evidence must separately cover mesh, rig, animation, texture/material, background/lighting, software/plugin, mocap or human performance, performer consent, generative upload, derivative generation, commercial use, Provider retention, and redistribution rights.

References with unresolved provenance, identifiable people, third-party IP, private data, real harm, or incompatible upload/derivative/retention/commercial terms are blocked. Free viewing or downloading does not establish active-input rights.

## 7. Push Reference Specification

`ACTION_REF_PUSH_01` defines one safe compact torso-level push:

- separated opening;
- visible onset;
- brief contact;
- readable torso displacement;
- exactly one rear-foot recovery placement;
- release and arm retraction;
- balanced stabilization with continued micro-motion.

The planned continuous motion windows are `0.00-0.35s`, `0.35-0.60s`, `0.60-0.75s`, `0.70-1.10s`, `0.85-1.20s`, and `1.20-2.40s`.

## 8. Impact Reference Specification

`ACTION_REF_IMPACT_01` defines one safe compact torso impact:

- separated opening;
- visible compact onset;
- brief torso contact;
- readable recoil;
- exactly one rear-foot step;
- initiating-limb retraction;
- balanced stabilization with continued micro-motion.

The planned continuous motion windows are `0.00-0.35s`, `0.35-0.55s`, `0.55-0.68s`, `0.60-0.95s`, `0.65-1.00s`, and `1.00-2.40s`.

## 9. Asset Record And Human Review Schema

The blank asset record contains exactly two templates in push/impact order. It contains no real path, hash, creator, license, consent identity, technical value, or human approval.

The Draft 2020-12 review schema requires exactly two records in the same order and covers complete-MP4 confirmation, technical validity, rights/provenance, consent, safety/privacy, visual neutrality, action-chain behavior, foot result, ending motion, distinctiveness risk, leakage risk, usability, human decision, and notes.

Full MP4 review is mandatory. A contact sheet cannot replace it.

## 10. Motion-Only Reference-Role Matrix

The action reference may control only action grammar:

- timing and pose progression;
- onset and brief contact rhythm;
- force direction;
- weight transfer;
- one family-appropriate rear-foot result;
- release or retraction;
- continued movement.

It may not control identity, face, body appearance, costume, scene, props, camera, framing, lighting, color grade, story, or IP design. Identity, scene, camera/layout, and action semantics remain conceptual separate duties.

If a future verified mode cannot separate duties, the canary status is `BLOCKED_REFERENCE_ROLE_CONFLICT`.

## 11. First-Gate R01 Aliases

Exactly two future capability canaries are selected:

1. `ROUTEA_PUSH_R01`
2. `ROUTEA_IMPACT_R01`

First-gate output count: `2`.

## 12. R02 Blocked Status

The preserved four-output design also includes `ROUTEA_PUSH_R02` and `ROUTEA_IMPACT_R02`.

- R02 live preparation authorized: `false`
- R02 execution authorized: `false`
- Automatic expansion: `false`

R02 requires completed and reviewed references, separately authorized R01 execution, complete R01 review, and a fresh human decision.

## 13. Canary Semantic Gate

Possible R01 decisions are:

- `CANARY_SEMANTIC_GATE_PASS_READY_FOR_R02_HUMAN_DECISION`
- `CANARY_MIXED_RESULT_REQUIRES_HUMAN_DECISION`
- `CANARY_REFERENCE_IGNORED_ROUTE_A_BLOCK`
- `CANARY_REFERENCE_OVERDOMINANT_ROUTE_A_BLOCK`
- `CANARY_REFERENCE_ROLE_CONFLICT_ROUTE_A_BLOCK`
- `CANARY_RIGHTS_OR_PROVENANCE_BLOCK`
- `CANARY_TECHNICAL_FAILURE_NEEDS_SEPARATE_DECISION`
- `CANARY_ACTION_FAILURE_NEEDS_HUMAN_DECISION`

The R01 semantic gate requires technical validity, complete review, no material prohibited leakage, correct action family, useful motion adherence, and a human R02 decision. A strict primary pass is desirable but not mandatory at this canary gate.

After a separately authorized R02 phase, the full minimum-positive result still requires at least one strict push pass, at least one strict impact pass, all rights and leakage conditions, and human expansion approval.

## 14. Future Authorization Sequence

The preparation artifacts separate:

1. reference-media creation;
2. reference technical validation;
3. human reference acceptance;
4. Provider capability revalidation;
5. no-live canary package preparation;
6. R01 submit;
7. R01 query;
8. R01 download;
9. R01 visual review and record lock;
10. R02 human decision;
11. R02 execution.

Every authority requires human approval, has automatic activation set to `false`, and is inactive now.

## 15. Cost And Credit Uncertainty

- Current price checked: `false`
- Current credit checked: `false`
- First gate planning formula: `2 x then-current verified per-canary unit cost`
- Full calibration planning formula: `4 x then-current verified per-output unit cost`

Local 3D creation, review, rendering, storage, and editing effort must be tracked separately. Historical Batch05 credits are not treated as the Route A price.

## 16. Route B And Route C Preservation

- Route B: `CAL002_ROUTE_B_MANUAL_POSE_START_END_FRAME_CONTROL`
- Route B status: `CONTROLLED_RESEARCH_FALLBACK_NOT_SELECTED`
- Route C: `CAL002_ROUTE_C_EDITORIAL_ACTION_DECOMPOSITION`
- Route C status: `PRODUCTION_FALLBACK_NOT_SELECTED`

No fallback is activated. Route A failure or block requires a fresh human route decision.

## 17. No Dreamina Or Provider Operation

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Submit/query/download/retry/resubmit/batch: `0/0/0/0/0/0`
- Login, session, help, version, or credit calls: `0`

## 18. No Reference Or Media Operation

- Reference-media discovery or inspection: `false`
- Reference media created: `false`
- Reference uploaded: `false`
- Media created: `false`
- Media changed: `false`
- Ready-to-run Provider Prompt created: `false`
- Executable command created: `false`
- Task package created: `false`

## 19. No Source Change

- Source update required later: `true`
- Source update authorized now: `false`
- Sources changed: `false`

## 20. Production Re-Entry Block

Production re-entry status:

`BLOCKED_PENDING_REFERENCE_CREATION_HUMAN_REVIEW_CAPABILITY_VALIDATION_AND_CANARY_EXECUTION`

- Production re-entry authorized: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- Final master: `false`
- Locked: `false`

## 21. Required Next Human Decision

The human must review this preparation pack and decide whether to authorize a separate, bounded reference-media creation phase. That future decision must preserve no-upload and no-Provider boundaries unless a later distinct authorization is granted.

## 22. Decision And Next Phase

Decision:

`CAL002_ROUTE_A_REFERENCE_SOURCE_AND_STAGED_TWO_CANARY_PREPARATION_COMPLETE_READY_FOR_HUMAN_REVIEW`

Next phase:

`CAL002_ROUTE_A_REFERENCE_SOURCE_AND_STAGED_CANARY_PREPARATION_HUMAN_DECISION`
