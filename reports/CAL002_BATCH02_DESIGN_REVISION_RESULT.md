# CAL002 Batch02 Design Revision Result

## Phase Result

- Phase: `CAL002_BATCH02_DESIGN_REVISION_NO_LIVE`
- Result: `COMPLETE`
- Starting checkpoint: `be28e85cc6456b9e822737b8b7e4ddf7ffc1eaf4`
- Revision input: `reports/CAL002_BATCH02_DESIGN_REVIEW_RESULT.md`
- Revision input SHA-256: `5764511b33e97f768562bc7a1086d45332ae133a0959d3a53eece1e0a7200a53`
- Experiment objective: test whether prompt organization alone improves action generation

## Files Created

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH02_DESIGN_V2/batch02_design_v2_manifest.json`
2. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH02_DESIGN_V2/CAL002-B02-A01_PUSH_STRUCTURE_V1.json`
3. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH02_DESIGN_V2/CAL002-B02-A04_IMPACT_STRUCTURE_V1.json`
4. `reports/CAL002_BATCH02_DESIGN_REVISION_RESULT.md`

## Renamed Experiments

| Prior design identity | Revised identity |
| --- | --- |
| `CAL002-B02-A01_PUSH_V4` | `CAL002-B02-A01_PUSH_STRUCTURE_V1` |
| `CAL002-B02-A04_IMPACT_V4` | `CAL002-B02-A04_IMPACT_STRUCTURE_V1` |

## Isolation Repair

Each revised experiment contains two no-live prompt treatments:

- Control: one flat causal sequence.
- Candidate: the same sequence grouped under `Initial State`, `Physical Event`, `Body Response`, and `Final State`.

The camera/identity/screen-direction replacement and the balance/foot wording are applied symmetrically to both treatments. They are therefore controlled semantics rather than candidate-only additions. Removing the four exact section labels from each candidate produces its control prompt byte-for-byte.

| Experiment | Control SHA-256 | Candidate SHA-256 | Normalized candidate equals control |
| --- | --- | --- | --- |
| `CAL002-B02-A01_PUSH_STRUCTURE_V1` | `8634cb031d29662f689f5374bb84b8d0c544bfb42a1aa899696e210aafaec854` | `1fa97dd97ee7bda68fb8d6240091f4cd3be03ce202c1d619310e80a4551d93f8` | `true` |
| `CAL002-B02-A04_IMPACT_STRUCTURE_V1` | `4e33aaafbfb5ef84b6aa6f46e080c57743137dfd59759349234795079b1384a7` | `8260c14bcb66c21dac9cdd48b795345e22e2a102b7592b4e5da5f69dfd55d18a` | `true` |

No candidate-only center-of-mass, impulse, force-vector, muscle, torque, acceleration, mechanics, or extra-constraint language is present.

## Contradiction Repairs

- Removed every unchanged-spacing requirement.
- Preserved camera composition, character identity, and readable screen direction instead.
- Removed continuous bilateral floor-contact language.
- Used balance, support-foot stability, and one opposite-foot recovery placement in both treatments.
- Kept action identity, causal order, contact requirement, bounded reaction, and original negative action classes aligned between treatments.

## Fixed Variables

- Characters: black armored warrior and white haired warrior.
- Scene: rainy ancient temple courtyard, wet stone floor, cinematic fantasy style.
- Camera: medium shot, eye level, static.
- Informational future settings: `seedance2.0_vip`, 5 seconds, `16:9`, `720p`.
- Reference strategy: text-only, zero active generation references.

## Comparison Shape

A valid structure-only comparison requires both treatments for each of the two actions. One paired sample per action would therefore contain four future generation units. This is design metadata only; no budget approval, provider package, command, claim, or execution authority is created.

## Validation

- Revised JSON file count: three.
- JSON validity: passed for all three revised files.
- Deterministic serialization: passed for UTF-8, lexicographic keys, two-space indentation, LF, and one final LF.
- Revised identities: exactly two and unique; passed.
- Candidate normalization: equals each flat control byte-for-byte after label removal; passed.
- Prompt hashes: match all embedded prompt text; passed.
- Batch01 evidence hashes: match their bound preflight values; passed.
- CAL-001 changes by this phase: `false`.
- Provider operations: `false`.
- Media operations: `false`.

## Boundary Confirmation

- `Dreamina_called=false`
- `provider_called=false`
- `submit_called=false`
- `query_called=false`
- `download_called=false`
- `media_created=false`
- `live_provider_package_created=false`
- `execution_authority_created=false`
- `CAL001_modified=false`
- `final_master=false`
- `locked=false`

## Final Verdict

`CAL002_BATCH02_DESIGN_REVISION_COMPLETE_READY_INDEPENDENT_NO_LIVE_REVIEW`
