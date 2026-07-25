# CAL-002 Route A Minimum Calibration Design V0.1

## 1. Calibration Identity

- Calibration ID: `CAL002-ROUTE-A-MIN-V0-1`
- Route: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`
- Route selected: `true`
- Route activated: `false`
- Provider capability verified: `false`
- Execution ready: `false`
- Live authority: `false`
- Reference-upload authority: `false`
- Media authority: `false`
- Production authority: `false`

This document designs but does not execute `CAL002_ROUTE_A_MINIMUM_CALIBRATION_V0_1`.

## 2. Objective

Determine whether a rights-safe action reference materially improves visible motion execution enough to justify a larger Route A experiment.

Only these action families are in scope:

1. `push_reaction`
2. `brief_impact_recoil`

No third action family is allowed. No same-route Batch05 text-only retry is allowed. Historical Batch05 results are a bounded qualitative baseline, not a new randomized control and not statistical evidence.

## 3. Isolated Research Question

The future test asks whether an action reference with a motion-only duty can produce:

- clearer onset and contact timing;
- visible post-contact consequence;
- the required single foot result;
- prompt release or retraction;
- continued movement without a long static tail;
- no material identity, costume, scene, camera, composition, or IP leakage.

It does not test a new Prompt compiler, new scene, new camera, alternate Provider, or production shot.

## 4. Planned Reference Roles

Exactly two future reference roles are planned:

### `ACTION_REF_PUSH_01`

- Duty: push onset, readable contact, receiving-body displacement, exactly one recovery placement, release, and continued movement.
- Useful action-window target: `1.0-2.0 seconds`.
- Status: `NOT_CREATED_NOT_SELECTED_NOT_APPROVED`.

### `ACTION_REF_IMPACT_01`

- Duty: compact onset, brief contact, immediate recoil, exactly one rear-foot step, retraction, and continued movement.
- Useful action-window target: `1.0-2.0 seconds`.
- Status: `NOT_CREATED_NOT_SELECTED_NOT_APPROVED`.

The action-window target is not an API limit. Exact accepted input duration must be revalidated under a future authorized capability phase.

## 5. Reference Preparation Requirements

Each future reference must:

- be project-owned, self-recorded with documented consent, licensed for generative-model input, or contractor-created with explicit generative-use rights;
- use neutral or project-owned people or figures;
- use simple clothing and a simple non-identifying background;
- avoid distinctive IP, props, logos, cinematic design, subtitles, watermarks, and platform UI;
- show the full useful motion without a cut;
- avoid camera motion where practical;
- keep both bodies and both feet visible;
- contain no audio unless separately justified and cleared;
- contain no real injury, gore, or unsafe physical contact;
- pass the provenance requirements and human active-input review.

Preferred future source order:

1. project-owned neutral 3D mannequin animation;
2. self-recorded consenting performers in neutral clothing and background;
3. explicitly licensed action reference.

No asset in any category is claimed to exist now.

## 6. Reference-Duty Separation

Each future task may use one action-reference video for the matching family. Identity, costume, scene, camera, composition, lighting, and style must remain separate duties.

If the verified mode cannot separate action reference, identity reference, and scene reference, the calibration is blocked. The design must not silently accept a role conflict.

## 7. Planned Outputs

Exactly four future outputs are designed:

| Alias | Action family | Replicate | Action reference role |
| --- | --- | ---: | --- |
| `ROUTEA_PUSH_R01` | `push_reaction` | 1 | `ACTION_REF_PUSH_01` |
| `ROUTEA_PUSH_R02` | `push_reaction` | 2 | `ACTION_REF_PUSH_01` |
| `ROUTEA_IMPACT_R01` | `brief_impact_recoil` | 1 | `ACTION_REF_IMPACT_01` |
| `ROUTEA_IMPACT_R02` | `brief_impact_recoil` | 2 | `ACTION_REF_IMPACT_01` |

Planned output count: `4`.

- Replicates per family: `2`
- Proposed model target: `seedance2.0_vip`, only if future capability evidence confirms the selected mode
- Proposed duration: `5 seconds`
- Proposed resolution: `1280x720` or the verified 720p equivalent

These are design values only. This document creates no command, Provider package, Provider manifest, upload plan, task record, credit authority, or execution claim.

## 8. Fixed Calibration Context

To preserve interpretability, a future reviewed package should hold constant:

- two adult professional stunt performers in a safe non-injury rehearsal;
- neutral identity and costume controls;
- neutral indoor rehearsal space;
- medium-wide, full-body, fixed camera;
- both performers and feet visible;
- no camera motion, cuts, dramatic effects, text, logo, props, crowd, or environmental destruction;
- one continuous five-second output;
- one action family and one matching action reference per task.

Any final implementation of these controls requires separate package review.

## 9. Push-Reaction Motion Contract

Required visible sequence:

- visibly separated initial state;
- attacker initiates first;
- contact onset is visible;
- receiver reacts only after contact;
- readable chest and shoulder displacement;
- exactly one rear-foot recovery placement;
- no multi-step retreat;
- attacker releases pressure promptly;
- no prolonged contact;
- both people remain fully in frame;
- receiver stabilizes without leaving frame;
- movement continues naturally after the core action;
- no extended-arm freeze;
- no long static ending.

Primary blocking failures:

- `NO_POST_CONTACT_REACTION`
- `NO_FOOT_RESULT`
- `MULTI_STEP_RETREAT`
- `PROLONGED_CONTACT`
- `NO_RELEASE`
- `EXTENDED_ARM_FREEZE`
- `FRAMING_ESCAPE`
- `LONG_STATIC_TAIL`
- `ACTION_REFERENCE_LEAKAGE`

## 10. Brief-Impact/Recoil Motion Contract

Required visible sequence:

- visibly separated initial state;
- compact attacker onset;
- short readable contact;
- immediate upper-body recoil;
- exactly one rear-foot step;
- prompt attacker retraction;
- no sustained push;
- no prolonged straight-arm contact;
- both people remain fully in frame;
- movement continues naturally after recovery;
- no long static guard tail;
- action remains brief impact/recoil.

Primary blocking failures:

- `SUSTAINED_PUSH_MISMATCH`
- `NO_RECOIL`
- `NO_FOOT_RESULT`
- `MULTI_STEP_RETREAT`
- `LATE_RETRACTION`
- `EXTENDED_ARM_FREEZE`
- `PROLONGED_CONTACT`
- `LONG_STATIC_TAIL`
- `ACTION_REFERENCE_LEAKAGE`

## 11. Proposed Timeline Targets

These are visual-review targets, not guaranteed Provider controls:

| Window | Target |
| --- | --- |
| `0.00-0.45s` | Separated preparation and readable onset |
| `0.45-1.10s` | Contact event |
| `0.65-1.60s` | Receiver reaction and required foot result |
| `1.10-2.00s` | Release, retraction, and stabilization |
| `2.00-5.00s` | Natural continued movement, guard adjustment, breathing, or readiness |

The final interval must not become an unchanged static pose.

## 12. Technical Validation Design

Every future output must pass:

- exactly one downloaded MP4;
- nonzero byte length;
- unique output SHA-256;
- valid container;
- exactly one video stream;
- expected resolution;
- duration within the future authorized tolerance;
- full ffmpeg decode;
- no unexpected overwrite;
- no filename collision;
- no signed-URL persistence;
- no credential persistence.

Technical validity does not imply motion success.

## 13. Human Visual-Review Design

Full MP4 review is mandatory for all four outputs. Contact sheets and comparison sheets are optional assistance only.

Required dimensions:

- technical validity;
- complete MP4 reviewed;
- first-frame separation;
- action onset;
- contact onset;
- contact duration;
- post-contact causality;
- torso displacement or recoil;
- foot-result presence, count, and type;
- release/retract;
- prolonged contact;
- action-family match;
- ending-motion compliance;
- static-tail start and duration;
- full-body visibility;
- camera compliance;
- identity consistency;
- reference identity, costume, scene, and camera leakage;
- overall visual usability;
- strict primary endpoint.

Final visual approval remains human-only.

## 14. Minimum Success Screen

Route A may advance beyond this minimum calibration only if:

1. At least one of two push outputs achieves a strict primary pass.
2. At least one of two impact outputs achieves a strict primary pass.
3. Neither family has action-reference identity leakage in either replicate.
4. Neither family has action-reference scene leakage in either replicate.
5. Neither family reproduces prolonged contact in both replicates.
6. Neither family reproduces a long frozen ending in both replicates.
7. Motion execution is visibly more complete than the bounded Batch05 text-only baseline.
8. Human review judges the route worthy of expansion.
9. Technical evidence is complete.
10. No rights or provenance defect exists.

This is a minimum signal screen, not a statistical-significance test.

## 15. Stopping Conditions

There are exactly 14 route-specific stopping conditions:

1. `CAPABILITY_UNSUPPORTED`
2. `MOTION_ONLY_DUTY_NOT_AVAILABLE`
3. `REFERENCE_ROLE_SEPARATION_UNAVAILABLE`
4. `RIGHTS_SAFE_REFERENCE_UNAVAILABLE`
5. `REFERENCE_UPLOAD_RIGHTS_UNRESOLVED`
6. `IDENTITY_LEAKAGE_REPEATED`
7. `SCENE_LEAKAGE_REPEATED`
8. `REFERENCE_IP_LEAKAGE`
9. `MOTION_REFERENCE_IGNORED_IN_BOTH_REPLICATES`
10. `MOTION_REFERENCE_OVERDOMINATES_BOTH_REPLICATES`
11. `SAME_CRITICAL_ACTION_FAILURE_IN_BOTH_REPLICATES_OF_A_FAMILY`
12. `NO_STRICT_PRIMARY_PASS_IN_EITHER_FAMILY`
13. `PREPARATION_BURDEN_EXCEEDS_HUMAN_APPROVED_LIMIT`
14. `GENERATION_OR_REVIEW_COST_EXCEEDS_HUMAN_APPROVED_CEILING`

No automatic expansion, retry, alternate Provider, Route B switch, or Route C switch is authorized.

## 16. Decision Precedence

1. Rights, consent, provenance, or privacy failure -> `SAFETY_OR_RIGHTS_BLOCK`.
2. Required Provider capability unavailable -> `CAPABILITY_BLOCK_ROUTE_A`.
3. Reference-role separation unavailable -> `REFERENCE_DUTY_CONFLICT_ROUTE_A`.
4. Repeated identity, scene, costume, camera, or IP leakage -> `ROUTE_A_LEAKAGE_FAILURE`.
5. Both action families produce zero strict passes -> `ROUTE_A_RESET_REQUIRED`.
6. One family passes and one family fails -> `FAMILY_SPECIFIC_ROUTE_A_RESULT`.
7. Both families achieve at least one strict pass -> `ROUTE_A_MINIMUM_POSITIVE_SIGNAL`.
8. A positive signal still requires human expansion approval -> `NO_AUTOMATIC_EXPANSION`.

## 17. Preserved Fallbacks

- Route B status: `CONTROLLED_RESEARCH_FALLBACK_NOT_SELECTED`
- Route C status: `PRODUCTION_FALLBACK_NOT_SELECTED`

No fallback implementation is designed here. A fresh human decision is required if Route A blocks.

## 18. Production and Source Boundary

- Source update required later: `true`
- Source update authorized now: `false`
- Sources changed: `false`
- CAL-002 formally closed: `false`
- Production re-entry: `BLOCKED_PENDING_CAPABILITY_VALIDATION_CALIBRATION_EXECUTION_AND_HUMAN_REVIEW`
- Production approved: `false`
- Fixed-task completion: `false`
- Final master: `false`
- Locked: `false`

## 19. Next Phase

`CAL002_ROUTE_A_CAPABILITY_AND_CALIBRATION_DESIGN_HUMAN_DECISION`

The human must review the capability boundary, provenance gate, reference-duty contract, minimum scope, success screen, stopping conditions, and future budget before any further authority exists.
