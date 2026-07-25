# CAL-002 Route A Staged Two-Canary Preparation Pack V0.1

## Current State

- Selected route: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`
- Preferred reference class: `PROJECT_OWNED_3D_OR_ANIMATED_REFERENCE`
- Capability conclusion: `COMMAND_SURFACE_SUPPORT_VERIFIED_MOTION_ONLY_BEHAVIOR_UNVERIFIED`
- Route A activated: `false`
- Route A execution authorized: `false`
- Reference media created: `false`
- Reference upload authorized: `false`
- Provider calls authorized: `false`

This pack describes future gates. It does not supply a ready-to-run Prompt, command, task package, upload path, media hash, Provider identifier, or live authority.

## Stage 0: Reference-Source Decision

Accepted source class: `PROJECT_OWNED_3D_OR_ANIMATED_REFERENCE`.

The source strategy is `CAL002_ROUTE_A_PROJECT_OWNED_NEUTRAL_3D_ACTION_REFERENCE_SOURCE`. No media exists or is created by this pack.

## Stage 1: Separate Reference-Media Creation Authorization

A future, separate authorization may permit creation or rendering of exactly:

1. `ACTION_REF_PUSH_01`
2. `ACTION_REF_IMPACT_01`

That authority must not permit Provider upload, Provider generation, R01 execution, R02 preparation, or production re-entry.

## Stage 2: Technical And Human Reference Review

Each exact reference file must be:

- technically validated;
- hashed;
- entered in a completed asset record;
- reviewed as a complete MP4;
- rights and provenance reviewed;
- motion reviewed;
- leakage-risk reviewed;
- accepted by the human against its exact bytes and SHA-256.

Required gate:

- technical validation: `PASS`;
- full MP4 reviewed: `true`;
- rights and provenance: `PASS`;
- generative upload allowed: `true`;
- derivative generation allowed: `true`;
- commercial-use status explicitly recorded;
- Provider-retention status explicitly recorded;
- identifiable person: absent;
- third-party IP: absent;
- private or sensitive data: absent;
- real harm: absent;
- motion-family match: `PASS`;
- full bodies and feet visible;
- camera motion: absent;
- cut in useful window: absent;
- prolonged contact: absent;
- extended-arm freeze: absent;
- human decision: `PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST`.

A contact sheet cannot replace complete reference review. No automation may set the human approval. No upload occurs at this stage.

## Stage 3: Provider-Mode And Package Preflight

Only after both references are accepted may a separate no-live Goal:

- revalidate official capability evidence;
- bind the exact accepted reference bytes;
- bind separately approved identity and scene inputs;
- compile treatment-neutral canary instructions;
- prepare exactly two bounded canary packages.

This stage still has no live authority unless separately granted. If a verified mode cannot separate action, identity, scene, and camera duties, the result is `BLOCKED_REFERENCE_ROLE_CONFLICT`.

## Stage 4: First Canary Submit Gate

A future exact approval may authorize at most:

1. one `ROUTEA_PUSH_R01` submit;
2. one `ROUTEA_IMPACT_R01` submit.

No R02 submit is permitted. Submit, query, and download remain separate authorization gates. There is no automatic retry, resubmit, batch retry, or expansion.

## Stage 5: Complete Canary Review

Both complete MP4 outputs must undergo:

- technical validation;
- full visual review;
- motion-reference adherence review;
- reference-leakage review;
- action-family review;
- strict endpoint review.

Review dimensions include technical validity, first-frame separation, onset, contact onset and duration, post-contact causality, torso displacement or recoil, foot-result presence/count/type, release or retraction, prolonged contact, extended-arm freeze, action-family match, ending motion, static-tail timing, full-body visibility, camera compliance, and identity consistency.

Reference-specific review includes motion adherence, ignored reference, overdominant reference, role conflict, and identity, face, body-appearance, costume, scene, prop, camera, composition, lighting/color, and story/IP leakage.

Full MP4 review remains human-only.

## Stage 6: Human R02 Decision

Only a fresh human decision may:

- authorize `ROUTEA_PUSH_R02`;
- authorize `ROUTEA_IMPACT_R02`;
- request reference fixes;
- block Route A;
- return to a Route B or Route C decision.

No automatic expansion is permitted.

## First-Canary Semantic Gate

Possible decisions:

- `CANARY_SEMANTIC_GATE_PASS_READY_FOR_R02_HUMAN_DECISION`
- `CANARY_MIXED_RESULT_REQUIRES_HUMAN_DECISION`
- `CANARY_REFERENCE_IGNORED_ROUTE_A_BLOCK`
- `CANARY_REFERENCE_OVERDOMINANT_ROUTE_A_BLOCK`
- `CANARY_REFERENCE_ROLE_CONFLICT_ROUTE_A_BLOCK`
- `CANARY_RIGHTS_OR_PROVENANCE_BLOCK`
- `CANARY_TECHNICAL_FAILURE_NEEDS_SEPARATE_DECISION`
- `CANARY_ACTION_FAILURE_NEEDS_HUMAN_DECISION`

The semantic pass requires both outputs to be technically valid and fully reviewed, with no material identity, costume, scene, camera/composition, or third-party-IP leakage. The action reference must not be ignored in both outputs or overdominant in either. Both outputs must remain in the intended action family and show at least partial visible motion-sequence adherence. A human must decide that R02 replication is justified.

A strict primary pass is desirable but not mandatory for the R01 semantic gate. After any separately authorized R02 phase, a minimum-positive four-output result still requires at least one strict push pass, at least one strict impact pass, all rights and leakage conditions, and human expansion approval.

## Future Technical Gate

Each future output must have:

- exactly one downloaded MP4;
- nonzero bytes and a unique SHA-256;
- a valid container and exactly one video stream;
- verified expected resolution and authorized duration tolerance;
- a full decode;
- no overwrite, filename collision, or cross-output collision;
- no raw signed URL or credential persistence.

Technical validity does not imply semantic success.

## Cost Boundary

- Current price checked: `false`
- Current credit checked: `false`
- First gate estimate: `2 x then-current verified per-canary unit cost`
- Full calibration estimate: `4 x then-current verified per-output unit cost`

Local 3D creation, review, rendering, storage, and editing effort must be recorded separately. Historical Batch05 credits are not a current Route A price.

## Preserved Alternatives And Production Block

- Route B: `CAL002_ROUTE_B_MANUAL_POSE_START_END_FRAME_CONTROL`
- Route B status: `CONTROLLED_RESEARCH_FALLBACK_NOT_SELECTED`
- Route C: `CAL002_ROUTE_C_EDITORIAL_ACTION_DECOMPOSITION`
- Route C status: `PRODUCTION_FALLBACK_NOT_SELECTED`

Failure or block of Route A requires a fresh human route decision.

Production re-entry remains `BLOCKED_PENDING_REFERENCE_CREATION_HUMAN_REVIEW_CAPABILITY_VALIDATION_AND_CANARY_EXECUTION`.
