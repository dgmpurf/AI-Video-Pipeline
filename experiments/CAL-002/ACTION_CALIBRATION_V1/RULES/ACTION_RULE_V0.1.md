# CAL-002 Action Rule V0.1

## Status

- Rule status: `PROVISIONAL_BATCH01_EXTRACTION`
- Source batch: `CAL002-ACTION-CALIBRATION-PILOT-R1-BATCH-01`
- Covered experiments: `CAL002-A01_PUSH_REACTION`, `CAL002-A04_IMPACT_STEP_BACK`, `CAL002-A03_GRAB_PULL`
- Live execution authority: `false`
- Final or approved asset claim: `false`

This rule extracts the capability boundary supplied for the Batch01 synthesis phase. Batch01 technical evidence confirms that three outputs were created and validated as media, while the existing review handoff still requires separate human visual acceptance. This document therefore guides later prompt experiments; it does not mark any output final, approved, or locked.

## Experiment Summary

| Experiment | Intended causal chain | V3 emphasis | Rule-extraction use |
| --- | --- | --- | --- |
| `CAL002-A01_PUSH_REACTION` | hand contact -> sustained pressure -> torso yield -> rearward weight shift -> one recovery step | contact before reaction and bounded displacement | distinguish readable push intent from complete force transfer |
| `CAL002-A04_IMPACT_STEP_BACK` | brief forearm contact -> impulse -> torso response -> one half-step -> stabilization | contact timing and bounded impact response | isolate impact reaction, weight shift, and recovery quality |
| `CAL002-A03_GRAB_PULL` | wrist grip -> arm tension -> shoulder/torso follow -> one balancing step | grip continuity and delayed whole-body response | test whether spatial linkage becomes connected body mechanics |

## Observed Capability Boundary

Batch01 indicates a useful but incomplete action-causality boundary. The model is comparatively strong at presenting the intended interaction and its spatial relationship. It is comparatively weak at carrying force through the body into a physically grounded ending.

### Strong

- **Action intent:** the requested push, impact, or pull can remain recognizable as the intended class of interaction.
- **Contact relationship:** the two-character cause-and-effect relationship can be made readable at the contact or grip point.
- **Spatial interaction:** attacker, receiver, direction, and relative placement can remain understandable within the shot.

### Weak

- **Force transfer:** visible contact does not reliably propagate as a coherent impulse or sustained pressure through the receiver.
- **Weight shift:** torso motion and center-of-mass movement do not reliably produce legible load transfer between the feet.
- **Impact reaction:** an impact may read as generic motion rather than a proportionate, contact-caused response.
- **Grounded recovery:** the final step and stabilization can become sliding, floating, extra travel, or an unresolved pose-out.

## Successful Behaviors To Preserve

- Name the initiator, receiver, contact point, and direction explicitly.
- Require visible contact or grip before receiver motion.
- Keep the interaction spatially bounded and easy to read.
- Preserve character identity, limb ownership, scene, framing, and camera controls.
- Distinguish sustained pressure from a brief impulse.

## Failed Behaviors To Target

- Contact that is visible but mechanically disconnected from the receiver's body.
- Receiver translation without torso compression, center-of-mass change, or foot loading.
- Reaction that starts before contact or tension.
- A requested single step that becomes multiple steps, sliding, flight, or a fall.
- Motion that ends without a stable grounded state.

## Prompt Design Recommendations

Use four ordered state-transition blocks. Each block should describe one causal responsibility and should remain positive and concrete before negative constraints are added.

### Initial State

- Establish distance, orientation, balance, planted feet, and which character is the initiator.
- State the fixed camera, environment, and identity constraints once.

### Physical Event

- Name the exact contact point and event type.
- State that contact occurs before receiver motion.
- Distinguish duration: sustained pressure for a push, brief impulse for an impact, continuous attachment for a pull.

### Body Mechanics

- Describe propagation through a specific chain: contact point -> torso or connected limb -> center of mass -> foot loading -> bounded step.
- Make temporal dependencies explicit with terms such as `only after`, `then`, and `before`.
- Specify grounding, step count, travel direction, and the absence of continued sliding.

### Final State

- Define the exact stable ending rather than only prohibiting failure.
- State final foot placement, balance, force cessation, and preserved spacing.
- Put negative constraints after the complete positive transition.

## V4 Design Rule

For the next comparison, change only the prompt organization from `V3_causal_motion_with_constraints` to `V4_state_transition`. Preserve the model, duration, ratio, resolution, text-only reference treatment, characters, scene, camera, action identity, and evaluation criteria. V4 must make the four states visibly separable in wording without introducing timing claims or live execution authority.

## Boundary

This document creates no provider package, command, submit permission, query permission, download permission, retry permission, media artifact, final-master state, or lock state. Any future V4 execution requires a separate reviewed package and explicit human authorization.
