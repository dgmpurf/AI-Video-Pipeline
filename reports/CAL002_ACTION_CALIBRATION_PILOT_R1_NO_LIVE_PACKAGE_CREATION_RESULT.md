# CAL-002 Action Calibration Pilot R1 No-Live Package Creation Result

## Phase Summary

- Experiment: `CAL002-ACTION-CALIBRATION-PILOT-R1`
- Task: no-live experiment execution package preparation
- Starting repository checkpoint: `b597cdeab3aa4c2e16206516c00a95c95b672370`
- Source design: `experiments/CAL-002/ACTION_CALIBRATION_V1/`
- Scope: `6` future generations
- Included prompt version: `V3_causal_motion_with_constraints`
- V1 execution packages included: `false`
- V2 execution packages included: `false`
- Live execution authority created: `false`

This phase prepared deterministic local JSON packages for human review. The provider parameters are frozen planning data only; they do not create a command, live authority, provider-ready package, or execution permission.

## Files Created

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/pilot_manifest.json`
2. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/CAL002-A04_IMPACT_STEP_BACK_PILOT_R1_package.json`
3. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/CAL002-A01_PUSH_REACTION_PILOT_R1_package.json`
4. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/CAL002-A03_GRAB_PULL_PILOT_R1_package.json`
5. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/CAL002-A02_BLOCK_IMPACT_PILOT_R1_package.json`
6. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/CAL002-A06_DRAW_SWORD_PILOT_R1_package.json`
7. `experiments/CAL-002/ACTION_CALIBRATION_V1/PILOT_R1/CAL002-A05_RUN_STOP_PILOT_R1_package.json`
8. `reports/CAL002_ACTION_CALIBRATION_PILOT_R1_NO_LIVE_PACKAGE_CREATION_RESULT.md`

## Pilot Matrix

| Order | Experiment | Action type | Prompt version | Camera |
| ---: | --- | --- | --- | --- |
| 1 | `CAL002-A04_IMPACT_STEP_BACK` | impact step back | `V3_causal_motion_with_constraints` | medium shot |
| 2 | `CAL002-A01_PUSH_REACTION` | push reaction | `V3_causal_motion_with_constraints` | medium shot |
| 3 | `CAL002-A03_GRAB_PULL` | grab pull | `V3_causal_motion_with_constraints` | medium shot |
| 4 | `CAL002-A02_BLOCK_IMPACT` | block impact | `V3_causal_motion_with_constraints` | medium shot |
| 5 | `CAL002-A06_DRAW_SWORD` | draw sword | `V3_causal_motion_with_constraints` | medium shot |
| 6 | `CAL002-A05_RUN_STOP` | run stop | `V3_causal_motion_with_constraints` | wide shot |

The A05 camera change is the explicitly permitted Pilot R1 exception. Its derived V3 prompt and final framing success criterion use `wide shot`; the source design file remains unchanged.

## Fixed References

- `character_A`: black armored warrior
- `character_B`: white haired warrior
- `scene`: rainy ancient temple courtyard
- Default camera: medium shot
- A05 camera exception: wide shot

Every package includes its experiment ID, action type, source hypothesis, success criteria, failure categories, V3 prompt text, fixed references, provider parameters, and source SHA-256 binding.

## Provider Parameters

- Model: `seedance2.0_vip`
- Duration: `5`
- Ratio: `16:9`
- Resolution: `720p`

These fields are configuration evidence only. No CLI argv, provider request, credential, upload reference, or Dreamina manifest was generated.

## Budget Boundary

- `max_generations`: `6`
- `expected_credit_cost`: `420`
- `retry`: `0`
- `resubmit`: `0`
- `query`: `0`
- `download`: `0`

The budget describes the maximum scope of a possible later human-authorized execution phase. It grants no submit or generation permission in this phase.

## Deterministic Serialization

All seven Pilot JSON files were independently parsed and reserialized with the recorded profile:

- Encoding: UTF-8
- BOM: absent
- Key order: lexicographic
- Indentation: 2 spaces
- Newline: LF
- Trailing newline: exactly one
- Duplicate JSON keys: rejected during validation
- Deterministic byte comparison: passed

Source fidelity validation passed for all six packages. Five package prompts are byte-equivalent to their source V3 prompt text. A05 matches the source V3 prompt after exactly the authorized `medium shot` to `wide shot` substitution.

## No-Live Authority

For the manifest and every package:

- `provider_ready_live_authority=false`
- `execution_permission_created=false`
- `submit_authorized=false`
- `query_authorized=false`
- `download_authorized=false`
- `retry_authorized=false`
- `resubmit_authorized=false`
- `dreamina_command_generated=false`

Operational confirmations:

- Dreamina called: `false`
- Provider called: `false`
- Submit called: `false`
- Query called: `false`
- Download called: `false`
- Media created: `false`

## Repository Boundary

- CAL-001 modified: `false`
- Existing production manifests modified: `false`
- Existing CAL-002 source design files modified: `false`
- Sources modified: `false`
- Existing tracked files modified: `false`
- Runtime, config, auth, executable, media, and historical evidence modified: `false`

Only the seven new Pilot R1 JSON files and this report are in scope for the bounded commit.

## Next Phase

`human review before execution authorization`

Human review must approve package content, order, A05 camera exception, budget, and any future submit/query/download contract. This phase cannot activate itself.

## Final Verdict

`CAL002_ACTION_CALIBRATION_PILOT_R1_NO_LIVE_PACKAGE_READY_FOR_HUMAN_REVIEW`
