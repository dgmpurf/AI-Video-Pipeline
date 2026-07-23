# CAL-002 Action Rule V0.3

## Status

- Rule status: `PROVISIONAL_BATCH03_UPDATE`
- Prior rule: `ACTION_RULE_V0.2.md`
- Prior rule SHA-256: `a91d654b9cf961300f5ad9a6f7d06485bc51032da4c78ef9931664d356ef7cb6`
- Evidence scope: Batch01 capability observations, Batch02 structure-only comparison, and Batch03 generic Action Causality Layer comparison
- Official Source status: `false`
- Live execution authority: `false`
- Production approved: `false`
- `final_master`: `false`
- `locked`: `false`

This version preserves the V0.2 capability boundary and structured-prompt findings. It adds the provisional Batch03 finding that a generic appended causality suffix is not a substitute for action-specific causal compilation.

## Evidence Basis

| Evidence | Role | SHA-256 |
| --- | --- | --- |
| `ACTION_RULE_V0.1.md` | Batch01 capability-boundary baseline | `a10d28af271155b0fb32c3c8feb204ca487a82c9a60822884ffc576e19126337` |
| `ACTION_RULE_V0.2.md` | Batch02 structured-prompt rule baseline | `a91d654b9cf961300f5ad9a6f7d06485bc51032da4c78ef9931664d356ef7cb6` |
| `reports/CAL002_BATCH03_DOWNLOAD_EXECUTION_RESULT.md` | Batch03 technical media identity and validation | `a465a4a445f1c01a2ddb1b26b5bf04ba46b52f7703810e8a4c5e65b6044034b9` |
| `reports/CAL002_BATCH03_HUMAN_VISUAL_REVIEW_RESULT.md` | Human Control/Candidate comparison | recorded in this no-live update phase |

## V0.2 Capability Boundary Preserved

### Comparatively Strong

- Action intent can remain recognizable.
- Contact relationships can remain readable.
- The spatial relationship between initiator, receiver, and motion direction can remain understandable.

### Comparatively Weak

- Force transfer is not reliably propagated through the receiver's body.
- Weight shift and support-foot behavior are not reliably grounded.
- Impact reactions can remain weak or generic.
- Recovery and final stabilization can remain physically incomplete.

## V0.2 Rules Preserved

### Rule 1: Structured Prompt Can Improve Action Organization

Using ordered sections such as `Initial State`, `Physical Event`, `Body Response`, and `Final State` can make the requested sequence easier to read. The observed benefit is organizational: intent, event order, and final-state communication may become clearer.

Structured organization remains provisionally useful for readability. It does not claim that every structured prompt outperforms every unstructured prompt.

### Rule 2: Structured Prompt Does Not Guarantee Physical Realism

Clear section organization does not by itself guarantee convincing force transfer, weight shift, impact reaction, or grounded recovery. A result may communicate the action more clearly while retaining the same physical weaknesses.

Neither structure labels nor generic causality suffixes guarantee physical realism. Mechanics and action readability must be reviewed separately.

### Rule 3: Test The Mechanics Layer Separately

Mechanics wording remains a separate experimental variable from prompt organization and causality syntax. Do not combine new mechanics semantics, constraints, references, and organization in one comparison when the goal is causal attribution.

## Batch03 Human Review Findings

| Action | Control | Generic causality candidate | Pair decision |
| --- | --- | --- | --- |
| A01 push | clear initiation and contact; weak force transfer; delayed readable foot adjustment | prolonged static contact; no clearer torso yield or displacement | `NO_CLEAR_CAUSALITY_GAIN_CONTROL_SLIGHTLY_BETTER` |
| A04 impact | clear initiation, contact, receiver response, and partial recovery | starts in contact; lacks initiation, contact moment, consequence, and recovery chain | `CAUSALITY_CANDIDATE_REGRESSION_CONTROL_CLEARLY_BETTER` |

Batch03 decision:

`GENERIC_APPENDED_ACTION_CAUSALITY_LAYER_NOT_SUPPORTED`

Confidence:

`MEDIUM`

## Rule 4: Generic Causality Meta-Instructions Are Not Action Compilation

Generic appended causality meta-instructions are not a substitute for action-specific causal clauses.

Do not append abstract instructions such as `make causality visible` and assume that the model will compile the physical sequence. Batch03 showed no clear A01 gain and a substantial A04 regression under the tested generic suffix.

This is a narrow rule about the tested generic meta-instruction. It does not establish that action-specific causality wording is ineffective.

## Rule 5: Compile Causality Into The Primary Action Beat

Causality should be compiled into the P0 action beat using explicit fields:

1. `attacker`
2. `defender`
3. `force line`
4. `contact point`
5. `body reaction`
6. `foot result`
7. `timing window`
8. `ending state`

These fields should form one action-specific causal chain rather than a detached abstract suffix. The wording should state who acts, where contact occurs, what visible result follows, when that result occurs, and how the bodies settle.

## Rule 6: Put The Visible Result First

Place the primary visible result and action causality before long scene, style, and negative-constraint text.

Recommended priority:

1. `P0 visible result and action causality`
2. `P1 minimum identity, scene, camera, and continuity context`
3. `P2 concise negative constraints`

The P0 beat should bind the requested result to the responsible contact and ending state. Long contextual text must not outrank the action result.

## Action-Specific Causal Syntax Template

Use this as a field order, not as a fixed universal prompt:

```text
Visible result:
<defender's required visible displacement or state change>.

Action causality:
<attacker> acts along <force line> and contacts <contact point> during
<timing window>. Only after contact, <defender body reaction> occurs,
producing <foot result>. The action ends in <ending state>.
```

The concrete values must be action-specific. Avoid replacing them with generic phrases such as `show causality`, `make impact clear`, or `show a visible consequence`.

## Review Guidance

Score the following dimensions independently:

- initiation
- contact timing
- post-contact consequence
- receiver body response
- recovery and stabilization
- identity, camera, and fixed-variable stability

An output can have readable organization while failing consequence or recovery. A pairwise difference should not be attributed solely to prompt treatment when costume, scene, framing, or other fixed variables drift.

## Provisional Boundary

Keep this rule provisional because:

- each Batch03 treatment has only one sample;
- generated costume, scene, and framing variables drifted;
- generation variance remains a plausible contributor;
- the experiment tested a generic appended suffix rather than a fully compiled action-specific P0 beat.

The current evidence supports rejecting the tested generic suffix as a reliable shortcut. It does not support a broad claim against action-specific causal syntax.

## Governance Boundary

- Official Source status: `false`
- Official Source modified: `false`
- Provider operation authorized: `false`
- Media operation authorized: `false`
- Production approved: `false`
- Fixed task completion: `false`
- `final_master`: `false`
- `locked`: `false`

This rule creates no provider package, Dreamina command, submit permission, query permission, download permission, retry permission, media artifact, production approval, final-master state, or lock state.

## Recommended Next Design Only

`CAL002_BATCH04_RESULT_FIRST_ACTION_CAUSALITY_DESIGN_NO_LIVE`

No Batch04 design file or execution authority is created by V0.3.
