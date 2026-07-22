# CAL-002 Action Calibration Pilot R1 Package Review Result

## Executive Verdict

- Review type: `read-only package review`
- Reviewed experiment: `CAL002-ACTION-CALIBRATION-PILOT-R1`
- Starting repository checkpoint: `7a4100ee5dbcfe13852bf20d1274eac5c6b3ebd0`
- Package decision: `PASS_WITH_NONBLOCKING_DESIGN_LIMITATIONS`
- Blocking defects: `0`
- Recommended execution strategy: `Option B`
- Live execution authority created: `false`

The package is structurally sound and suitable for a human execution-authorization decision. The six outputs should be interpreted as diagnostic probes, not as a statistically controlled comparison of action families.

## Findings

### Material: Action Family And Role Are Partly Confounded

The package keeps character identities and scene stable, but action type is not the only changing semantic variable:

- A01, A03, and A04 use the black armored warrior as initiator and the white haired warrior as receiver.
- A02 reverses the active role: the white haired warrior strikes and the black armored warrior blocks.
- A06 makes the white haired warrior the active subject and introduces sword-object continuity.
- A05 tests solo locomotion, keeps the second character stationary, and uses the authorized wide-shot exception.

This does not invalidate a capability pilot, but it prevents direct claims that score differences are caused only by action type. Results should be classified by capability domain: force transfer, continuous contact, interception, object continuity, or locomotion.

### Material: One Generation Per Action Does Not Measure Reliability

Each action receives one future generation and retry is zero. A single pass or failure may contain normal model variance. The pilot can identify useful failure modes and obvious capability gaps, but it cannot establish repeatability, success rate, or statistically rank the six prompts.

### Nonblocking: Unit Credit Assumption Is Implicit

`max_generations=6` and `expected_credit_cost=420` are arithmetically consistent with `70 credits` per generation. The Pilot manifest does not record that unit-cost assumption directly. Before live authorization, current provider pricing should be reconfirmed; this review does not change the manifest.

### Nonblocking: Dense Negative Constraints May Compete With Motion

All V3 prompts correctly front-load causal order, but A03 and A05 carry long causal chains plus many negative constraints inside a five-second duration. If motion becomes weak or incomplete, the result may reflect prompt-priority competition rather than failure to understand causality.

## Structural Validation

| Check | Result | Notes |
| --- | --- | --- |
| JSON validity | PASS | Seven JSON files parsed with duplicate-key and nonfinite-value rejection. |
| Deterministic serialization | PASS | UTF-8, no BOM, lexicographic keys, 2-space indentation, LF, one trailing LF. |
| Experiment identity uniqueness | PASS | Six unique experiment IDs and six unique package IDs. |
| Fixed-variable consistency | PASS | Characters and scene are identical; five medium shots plus the explicit A05 wide-shot exception. |
| Action-variable isolation | PARTIAL | Clean within each prompt, but actor role, interaction class, object use, and A05 camera vary across families. |
| V3 causal structure | PASS | Every prompt expresses initial state, trigger/contact, ordered consequence, bounded end state, and failure constraints. |
| Seedance parameter consistency | PASS | All six use `seedance2.0_vip`, 5 seconds, 16:9, and 720p. |
| Budget consistency | PASS_WITH_NOTE | Six generations and 420 credits imply 70 credits each; unit cost is not explicit in the manifest. |
| Live authority isolation | PASS | All submit/query/download/retry/resubmit and execution flags are false; no command exists. |

## Experiment Reviews

### 1. CAL002-A01_PUSH_REACTION

- Action hypothesis: explicit contact-before-reaction language improves a grounded push response.
- Prompt quality: `9/10`
- Experimental cleanliness: `9/10`
- Expected information value: `very high`; provides the simplest two-character contact-and-response baseline and a useful comparator for A04.
- Risks: push may become a strike; the receiver may react early; exact one-step language may dominate natural weight transfer; identity or arm merging remains possible.
- Recommended execution order: `1`

The causal chain is clear: planted initiator, visible contact, pressure, torso yield, weight transfer, one recovery step. This is the best low-complexity baseline for deciding whether later contact experiments are worth running.

### 2. CAL002-A04_IMPACT_STEP_BACK

- Action hypothesis: exact impact timing plus a bounded one-step response improves grounded impulse-to-footwork causality.
- Prompt quality: `9/10`
- Experimental cleanliness: `8/10`
- Expected information value: `very high`; directly tests whether the model distinguishes a brief impulse from sustained push or explosive knockback.
- Risks: forearm contact may be visually ambiguous; the half-step may become multiple steps, sliding, flight, or no lower-body response; A01 and A04 may collapse into similar motions.
- Recommended execution order: `2`

Running A04 immediately after A01 creates the strongest pairwise comparison in the pilot: sustained pressure versus brief impact under the same characters, scene, and camera.

### 3. CAL002-A03_GRAB_PULL

- Action hypothesis: continuous grip and visible tension improve hand-to-arm-to-torso-to-foot causal continuity.
- Prompt quality: `9/10`
- Experimental cleanliness: `8/10`
- Expected information value: `very high`; tests persistent contact and multi-joint force propagation, a harder capability than momentary impact.
- Risks: wrist ownership may drift; grip may detach; the receiver may move before tension; the long causal chain may not complete within five seconds.
- Recommended execution order: `3`

This is the highest-complexity member of the proposed first batch. Its result determines whether continuous-contact actions deserve further investment after simpler contact and impact probes.

### 4. CAL002-A02_BLOCK_IMPACT

- Action hypothesis: explicit interception and force transfer improve stopping and recoil at a block.
- Prompt quality: `9/10`
- Experimental cleanliness: `7/10`
- Expected information value: `high`; probes two moving limbs, collision timing, deceleration, and small recoil.
- Risks: initiator identity reverses relative to the first three; limbs may pass through or merge; the guard may miss; role reversal complicates cross-action comparison.
- Recommended execution order: `4`

This should begin the second batch because it extends contact causality into bidirectional motion after the first batch establishes whether basic two-character contact is readable.

### 5. CAL002-A06_DRAW_SWORD

- Action hypothesis: hand-to-hilt contact and progressive blade emergence improve object state continuity from sheathed to drawn.
- Prompt quality: `9/10`
- Experimental cleanliness: `8/10`
- Expected information value: `high`; isolates object ownership, progressive reveal, and start-to-end state continuity rather than force transfer.
- Risks: sword materialization, duplicate blade or sheath, hand-object disconnect, incomplete draw, and actor-role reversal relative to the first batch.
- Recommended execution order: `5`

The prompt is causally explicit and well bounded. It belongs after the interaction tests because it answers a different question: object continuity rather than body-to-body force propagation.

### 6. CAL002-A05_RUN_STOP

- Action hypothesis: planted-foot braking language improves deceleration and stable stopping on a wet surface.
- Prompt quality: `8/10`
- Experimental cleanliness: `7/10`
- Expected information value: `high`; probes self-motion, inertia, traction loss, traction recovery, and final stillness.
- Risks: exact three-step counting may fail; the stop may freeze, slide indefinitely, spin, or fall; the wide-shot exception and solo-action structure prevent direct comparison with medium-shot contact actions.
- Recommended execution order: `6`

The wide shot is justified for readable footwork, but it is intentionally a separate locomotion probe. It should run last and be reviewed against its own criteria rather than compared numerically with the five medium-shot packages.

## Recommended Execution Order

The current manifest order is valid. For information efficiency, the review recommends this operational order:

1. `CAL002-A01_PUSH_REACTION`
2. `CAL002-A04_IMPACT_STEP_BACK`
3. `CAL002-A03_GRAB_PULL`
4. `CAL002-A02_BLOCK_IMPACT`
5. `CAL002-A06_DRAW_SWORD`
6. `CAL002-A05_RUN_STOP`

The only change from the manifest order is placing A01 before A04. This establishes the simpler sustained-contact baseline before testing brief impact. This is review advice only; no package or manifest was modified.

## Batch Decision

### Option A: Six Generations / 420 Credits

Advantages:

- Produces immediate breadth across five causal-motion domains.
- Requires only one authorization cycle.
- Provides a complete first-look failure taxonomy.

Risks:

- Spends the full budget before learning whether basic two-character contact is readable.
- A systematic identity or motion-priority failure could make several later outputs predictably low-value.
- One sample per family still does not establish repeatability.

### Option B: First Three / 210 Credits, Then Decide

First batch:

1. A01 push reaction
2. A04 impact step back
3. A03 grab pull

Decision gate after visual review:

- Are both identities stable?
- Does visible contact precede reaction?
- Is the causal chain readable through torso and feet?
- Does sustained contact differ from brief impact?
- Can continuous grip survive long enough to transfer motion?

If these results provide interpretable evidence, authorize the second batch of A02, A06, and A05 separately. If all three fail through the same identity, contact, or motion-priority mechanism, preserve the remaining 210 credits and revise the route before further execution.

## Recommendation

`RECOMMEND_OPTION_B_FIRST_3_GENERATIONS_210_CREDITS_THEN_HUMAN_REVIEW_GATE`

Do not execute the full six-generation batch under one initial authorization. The staged approach has higher expected information per credit and preserves a clean human decision point without changing the package contents.

## Explicit Non-Actions

- Dreamina called: `false`
- Provider called: `false`
- Submit called: `false`
- Query called: `false`
- Download called: `false`
- Media created: `false`
- Package files modified: `false`
- Manifest modified: `false`
- CAL-001 modified: `false`
- Existing production manifests modified: `false`
- Sources modified: `false`

## Final Verdict

`CAL002_ACTION_CALIBRATION_PILOT_R1_PACKAGE_REVIEW_COMPLETE_RECOMMEND_OPTION_B`

Next required phase: human decision on first-three execution authorization. This review creates no execution permission.
