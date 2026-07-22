# CAL-002 Action Rule V0.2

## Status

- Rule status: `PROVISIONAL_BATCH02_UPDATE`
- Prior rule: `ACTION_RULE_V0.1.md`
- Evidence scope: Batch01 action-causality observations and Batch02 structure-only comparison
- Covered Batch02 experiments: `CAL002-B02-A01_PUSH_STRUCTURE_CONTROL`, `CAL002-B02-A01_PUSH_STRUCTURE_CANDIDATE`, `CAL002-B02-A04_IMPACT_STRUCTURE_CONTROL`, `CAL002-B02-A04_IMPACT_STRUCTURE_CANDIDATE`
- Official Source status: `false`
- Live execution authority: `false`
- Production approved: `false`
- `final_master`: `false`
- `locked`: `false`

This version carries forward the Batch01 capability boundary and adds the human-reviewed Batch02 finding about prompt organization. It is a provisional experiment rule, not an official Source rule or execution authorization.

## Evidence Basis

| Evidence | Role | SHA-256 |
| --- | --- | --- |
| `ACTION_RULE_V0.1.md` | Batch01 capability-boundary baseline | `a10d28af271155b0fb32c3c8feb204ca487a82c9a60822884ffc576e19126337` |
| `reports/CAL002_BATCH02_DOWNLOAD_EXECUTION_RESULT.md` | Batch02 technical download evidence | `2d91f3244f61557ec8fe0cd12bd1d3d1641332e9f394f106a51fa887c2325966` |
| `reports/CAL002_BATCH02_HUMAN_VISUAL_REVIEW_RESULT.md` | Human control/candidate comparison | recorded in the same no-live update phase |

## Capability Boundary Carried Forward

### Comparatively Strong

- Action intent can remain recognizable.
- Contact relationships can remain readable.
- The spatial relationship between initiator, receiver, and motion direction can remain understandable.

### Comparatively Weak

- Force transfer is not reliably propagated through the receiver's body.
- Weight shift and support-foot behavior are not reliably grounded.
- Impact reactions can remain weak or generic.
- Recovery and final stabilization can remain physically incomplete.

## Batch02 Human Review Findings

| Action | Control observation | Structured candidate observation | Narrow conclusion |
| --- | --- | --- | --- |
| A01 push | push intent present; limited body response | clearer organization and stronger push readability; no major physics improvement | structure improved readability, not mechanics |
| A04 impact | attack pose present; weak impact reaction | clearer event progression and improved readability; impact physics still limited | structure improved progression, not impact realism |

## Extracted Rules

- Structured prompt improves action organization.
- Structured prompt does not guarantee physical realism.
- Mechanics layer should be tested separately.

## Rule 1: Structured Prompt Improves Action Organization

Using ordered sections such as `Initial State`, `Physical Event`, `Body Response`, and `Final State` can make the requested action sequence easier to read. The observed benefit is organizational: intent, event order, and final-state communication become clearer.

This rule does not claim that every structured prompt will outperform every unstructured prompt. It records a consistent direction across the two Batch02 pairs.

## Rule 2: Structured Prompt Does Not Guarantee Physical Realism

Clear section organization does not by itself guarantee convincing force transfer, weight shift, impact reaction, or grounded recovery. A result may communicate the action more clearly while retaining the same physical weaknesses.

Do not infer mechanics quality from action readability alone. Evaluate the receiver's body response and ending state separately.

## Rule 3: Test The Mechanics Layer Separately

Mechanics wording should be treated as a separate experimental variable from prompt organization. A future mechanics test should preserve the proven organizational structure while changing only the mechanics layer under a separately reviewed design.

Do not combine new mechanics semantics, new constraints, new references, and new prompt organization in one comparison when the goal is causal attribution.

## Prompt Use Guidance

For action readability, the preferred organizational sequence is:

1. `Initial State`
2. `Physical Event`
3. `Body Response`
4. `Final State`

Use the labels to organize existing action requirements. Do not treat the labels themselves as a substitute for contact timing, body response, force transfer, balance, or recovery requirements.

## Review Guidance

Score organization and mechanics as separate dimensions:

- **Organization:** Is the event sequence readable from setup through ending?
- **Mechanics:** Does contact visibly cause a proportionate, grounded body response?
- **Final state:** Does the movement settle into the requested stable outcome?

An organizational improvement may be accepted as an experiment finding even when mechanics remain weak, but it must not be recorded as physical-realism success.

## Limitations

- The Batch02 update is based on two action families and one output per treatment.
- The observations are qualitative and are not a repeated-seed statistical result.
- Generation variance remains a plausible contributor to pairwise differences.
- The rule should remain provisional until repeated tests support broader use.

## Governance Boundary

This rule creates no provider package, command, submit permission, query permission, download permission, retry permission, media artifact, production approval, final-master state, or lock state. It does not modify official Source. Any future mechanics-layer experiment requires its own no-live design, independent review, budget decision, and fresh human authorization before live execution.
