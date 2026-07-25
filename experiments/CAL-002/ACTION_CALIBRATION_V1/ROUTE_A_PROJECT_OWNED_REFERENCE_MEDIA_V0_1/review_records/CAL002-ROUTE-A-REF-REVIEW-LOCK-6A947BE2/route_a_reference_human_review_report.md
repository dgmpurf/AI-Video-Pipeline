# CAL-002 Route A Project-Owned Reference Full-MP4 Human Review

## Review state

- Review mode: complete-MP4 human visual review
- References reviewed: `2 / 2`
- Contact sheets: assistance only
- Rights class: `PROJECT_OWNED_3D_OR_ANIMATED_REFERENCE`
- Reference upload authorized by this review: `false`
- Dreamina / Provider called: `false / false`
- R01 canary generation authorized: `false`
- R02 authorized: `false`
- Production approved / fixed-task completion / final master / locked: `false / false / false / false`

## ACTION_REF_PUSH_01

### Complete timeline finding

- The figures start visibly separated.
- The attacker initiates first and extends both arms.
- Short two-hand torso contact is readable.
- The receiver begins moving only after contact.
- Torso displacement is readable.
- Exactly one rear-foot recovery placement occurs; no second step follows.
- Pressure releases and both arms retract promptly.
- No prolonged contact or extended-arm freeze occurs.
- Both full bodies and both sets of feet remain visible.
- The final interval contains subtle continued motion rather than a frozen duplicate frame.

### Governance and leakage finding

- Technical validity: `PASS`
- Rights/provenance: `PASS`
- Consent: `NOT_APPLICABLE`
- Identifiable person / third-party IP / private data / real harm: `ABSENT`
- Continuous shot / static camera / neutral figures / neutral background: `PASS`
- Identity, costume, scene, and camera distinctiveness risk: `LOW`
- Aggregate upload-leakage risk: `MEDIUM`

The medium leakage rating is caused by the visible yellow contact marker together with the flat mannequin styling, grid background, and fixed side-view composition. These do not block a capability canary, but a future output copying the marker, mannequin appearance, scene, or framing must be classified as reference overdominance and must block R02.

### Human decision

`PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST`

This decision accepts the reference as a candidate input for a separately authorized R01 capability canary. It does not authorize upload or generation.

## ACTION_REF_IMPACT_01

### Complete timeline finding

- The figures start visibly separated.
- The attacker uses a compact onset.
- Torso contact is brief and readable.
- The receiver recoils only after contact.
- Exactly one rear-foot recoil step occurs; no multi-step retreat follows.
- The attacker retracts promptly.
- The movement does not become a sustained push.
- No prolonged contact or extended-arm freeze occurs.
- Both full bodies and both sets of feet remain visible.
- The final interval contains subtle continued motion rather than a frozen duplicate frame.

### Governance and leakage finding

- Technical validity: `PASS`
- Rights/provenance: `PASS`
- Consent: `NOT_APPLICABLE`
- Identifiable person / third-party IP / private data / real harm: `ABSENT`
- Continuous shot / static camera / neutral figures / neutral background: `PASS`
- Identity, costume, scene, and camera distinctiveness risk: `LOW`
- Aggregate upload-leakage risk: `MEDIUM`

The medium leakage rating is caused by the visible yellow contact marker together with the flat mannequin styling, grid background, and fixed side-view composition. These do not block a capability canary, but a future output copying the marker, mannequin appearance, scene, or framing must be classified as reference overdominance and must block R02.

### Human decision

`PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST`

This decision accepts the reference as a candidate input for a separately authorized R01 capability canary. It does not authorize upload or generation.

## Final human-review result

```yaml
ACTION_REF_PUSH_01: PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST
ACTION_REF_IMPACT_01: PASS_FOR_FUTURE_UPLOAD_AUTHORIZATION_REQUEST

references_full_mp4_reviewed: 2
references_human_accepted_for_future_upload_request: 2
reference_upload_authorized: false
R01_canary_generation_authorized: false
R02_authorized: false
Route_A_capability_proven: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

Before any upload, the exact committed MP4 bytes and completed review record must be locked in Git, Provider capability and current command surface must be freshly revalidated, and a new human authorization must separately bind the two reference hashes and the maximum two R01 canary submits.
