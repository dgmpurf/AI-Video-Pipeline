# CAL-002 Route A Motion-Only Reference Duty Contract V0.1

## 1. Classification

This is a non-executable semantic duty contract for future Route A design review.

- Route: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`
- Route selected: `true`
- Route activated: `false`
- Route execution authorized: `false`
- Reference-upload authority: `false`
- Media authority: `false`
- Provider capability verified: `false`

It does not create a Provider Prompt, command, package, manifest task, upload plan, or live authority.

## 2. Allowed Motion Duties

A future approved action reference may be used only for:

- onset timing;
- pose progression;
- direction of force;
- contact rhythm;
- weight transfer;
- receiver reaction;
- exact footwork pattern;
- recoil;
- attacker release or retraction;
- continuing movement through the useful window.

## 3. Prohibited Copied Duties

The reference must not supply or override:

- face or identity;
- body identity;
- costume design;
- hairstyle;
- scene;
- architecture;
- props;
- lighting design;
- color grade;
- camera identity;
- framing;
- lens behavior;
- story;
- dialogue;
- music;
- original-IP character or world design.

## 4. Conceptual Future Instruction

The future generation instruction must communicate this concept:

> Use the video only for action timing, force path, pose sequence, footwork, recoil, and release/retract behavior. Do not copy the people, faces, bodies, clothing, background, camera, composition, lighting, props, or story from the action reference.

This wording is a semantic design requirement only. It is not a ready-to-run Provider Prompt and does not prove that a Provider can enforce the separation.

## 5. Required Role Separation

Future design must keep these duties distinct:

| Duty | Allowed source | Route A action video may supply it |
| --- | --- | --- |
| Action motion | Rights-safe action reference | Yes, within the allowed motion list |
| Character identity | Separately reviewed identity control | No |
| Costume | Separately reviewed identity/costume control | No |
| Scene and architecture | Separately reviewed scene control | No |
| Camera and composition | Explicit calibration design | No |
| Lighting and style | Explicit calibration design | No |
| Story and dialogue | Project design | No |

If a future verified mode cannot keep action, identity, and scene duties separate, the calibration is blocked as `REFERENCE_DUTY_CONFLICT_ROUTE_A`.

## 6. Reference-Leakage Failure Taxonomy

| Failure class | Observable condition | Severity | Blocking status | Review method | One occurrence blocks expansion | Two replicated occurrences close route |
| --- | --- | --- | --- | --- | --- | --- |
| `IDENTITY_LEAKAGE` | Output adopts a materially recognizable person or identity from the action reference | Critical | Blocks production use | Full-MP4 face, silhouette, body-identity, and cross-frame review | Yes | Yes |
| `FACE_LEAKAGE` | Facial geometry or likeness materially follows the action reference | Critical | Blocks production use | Full-MP4 face review at clear frames | Yes | Yes |
| `BODY_APPEARANCE_LEAKAGE` | Body build, proportions, or distinctive physical appearance materially follows the reference | High | Blocks affected output | Full-body temporal comparison | Yes when material | Yes |
| `COSTUME_LEAKAGE` | Clothing design, colors, protective gear, or accessories materially copy the reference | High | Blocks affected output | Costume and frame-sequence review | Yes when material | Yes |
| `SCENE_LEAKAGE` | Background, architecture, location, or environmental layout materially follows the reference | Critical | Blocks production use | Full-MP4 background and spatial review | Yes | Yes |
| `PROP_LEAKAGE` | Distinctive props or weapons from the reference appear in the output | High | Blocks affected output | Prop inventory review across the MP4 | Yes when third-party or material | Yes |
| `CAMERA_LEAKAGE` | Camera motion, angle, lens behavior, or shot identity follows the reference instead of the fixed calibration camera | High | Invalidates calibration comparison | Full-MP4 camera-motion review | Yes | Yes |
| `COMPOSITION_LEAKAGE` | Framing or source-shot composition is materially copied | High | Invalidates calibration comparison | Start/middle/end framing comparison | Yes when material | Yes |
| `LIGHTING_OR_COLOR_LEAKAGE` | Distinctive lighting design or grade from the reference overrides calibration lighting | Medium to high | Invalidates affected comparison | Full-MP4 lighting and grade review | Yes when material | Yes |
| `STORY_OR_IP_LEAKAGE` | Plot beats, branded elements, recognizable characters, or world design transfer from the reference | Critical | Blocks production use and active-input status | Human IP and story review | Yes | Yes |
| `MOTION_REFERENCE_IGNORED` | Output does not show the reference's intended onset, contact, footwork, recoil, or release structure | High | Fails motion treatment | Full-MP4 motion-contract scoring | No, one replicate may fail | Yes within a family |
| `MOTION_REFERENCE_OVERDOMINANT` | Motion reference overwhelms identity, scene, camera, or action-family constraints | High | Invalidates affected output | Cross-duty review | Yes when leakage is material | Yes |
| `REFERENCE_ROLE_CONFLICT` | Action, identity, scene, or camera references compete so their intended duties cannot be distinguished | Critical | Blocks Route A package readiness | Reference-duty audit and output review | Yes | Yes |

Any identity, scene, third-party-IP, or rights leakage materially derived from the action reference blocks production use. Repeated material leakage blocks expansion and triggers Route A review under the stopping rules.

## 7. Review Requirements

Every future output requires:

- complete MP4 review;
- technical validation recorded separately from motion success;
- action-family and motion-contract review;
- explicit identity, costume, scene, prop, camera, composition, lighting, and IP leakage checks;
- human final judgment;
- no inference from contact sheets alone.

## 8. Safety and Rights Boundary

The duty contract applies only after the provenance gate passes. It cannot make an unknown-rights or unsafe reference acceptable. A reference remains inactive until a human verifies rights, consent, Provider terms, privacy, retention, and the intended duty.

No real reference is approved or represented by this document.

## 9. Failure Handling

- A rights or consent defect produces `SAFETY_OR_RIGHTS_BLOCK`.
- Missing motion-only capability produces `CAPABILITY_BLOCK_ROUTE_A`.
- Unavailable role separation produces `REFERENCE_DUTY_CONFLICT_ROUTE_A`.
- Repeated material leakage produces `ROUTE_A_LEAKAGE_FAILURE`.
- No automatic retry, expansion, fallback switch, or production use follows from any failure.
