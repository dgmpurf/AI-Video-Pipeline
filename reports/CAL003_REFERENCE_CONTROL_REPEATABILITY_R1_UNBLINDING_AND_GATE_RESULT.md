# CAL-003 R1 Unblinding and Gate Result

## Execution

- Decision: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_UNBLINDING_AND_GATE_DERIVATION_COMPLETE`
- Execution ID: `CAL003-R1-UNBLINDING-GATE-SCHEMA-BOUND-SINGLE-PROCESS-RECOVERY-V0-6`
- Starting checkpoint: `c0be22e06bb79fa036b6619b27c7a0b0be6414cc`
- Corrected parser: `PRODUCER_BOUND_MAPPING_AND_EQUIVALENCE_SCHEMA_V0_6`
- Parser self-tests: `13/13 PASS`
- Direct dictionary set construction: `false`

Five historical local orchestration failures produced zero repository outputs.
V0.1 used an incompatible sentinel-object set construction. V0.2 ended during
an AST command-wrapper quoting check before either ZIP was opened. V0.3 opened
the freeze ZIP once, then stopped on an incorrect generic exclusion-field
predicate before opening the sealed ZIP. V0.4 passed freeze, sealed, and
commitment validation, then stopped because its mapping validator expected
nested media objects. V0.5 parsed the direct mapping but incorrectly required
three fields absent from the immutable producer schema. This V0.6 recovery is
bound to the exact V0.3 creator schema and activates at the first sealed ZIP
open.

## Package and Commitment Validation

- Freeze ZIP: `PASS`; V0.6 pre-activation open count `1`;
  members `9/9`
- Freeze SHA256SUMS: `8/8 PASS`
- Frozen review and sentinel parsing: `6/6 PASS`
- Frozen score arithmetic: `6/6 PASS`
- Producer-schema AST derivation: `PASS`; mapping fields `13`;
  equivalence fields `23`
- Sealed ZIP: `PASS`; open count `1`; members `6/6`
- Sealed SHA256SUMS: `4/4 PASS`
- Mapping/equivalence coverage: `6/6`
- Mapping/equivalence parser corrections: `0/3`
- Four-way public commitment equality: `PASS`

## Verified Mapping

| Alias | Task | Family | Replicate | Ordinal pair |
|---|---|---|---:|---:|
| B01 | PUSH-02 | PUSH | 2 | 2 |
| B02 | IMPACT-03 | IMPACT | 3 | 3 |
| B03 | IMPACT-01 | IMPACT | 1 | 1 |
| B04 | IMPACT-02 | IMPACT | 2 | 2 |
| B05 | PUSH-03 | PUSH | 3 | 3 |
| B06 | PUSH-01 | PUSH | 1 | 1 |

## Scores and Sample Gates

| Alias | PUSH | IMPACT | Family | Own | Cross | Margin | Sample Gate |
|---|---:|---:|---|---:|---:|---:|---|
| B01 | 12 | 4 | PUSH | 12 | 4 | 8 | PASS |
| B02 | 12 | 6 | IMPACT | 6 | 12 | -6 | FAIL |
| B03 | 12 | 6 | IMPACT | 6 | 12 | -6 | FAIL |
| B04 | 12 | 4 | IMPACT | 4 | 12 | -8 | FAIL |
| B05 | 12 | 4 | PUSH | 12 | 4 | 8 | PASS |
| B06 | 12 | 6 | PUSH | 12 | 6 | 6 | PASS |

## Family Gates

| Family | Passes | Own values / median | Margins / median | Ignored | Gate |
|---|---:|---|---|---:|---|
| PUSH | 3/3 | [12, 12, 12] / 12 | [6, 8, 8] / 8 | 0 | PASS |
| IMPACT | 0/3 | [6, 4, 6] / 6 | [-6, -8, -6] / -6 | 0 | FAIL |

- Global material sentinel count: `0`
- Rights/provenance governed validation: `PASS`

## Ordinal-Pair Gate

| Pair | PUSH task | IMPACT task | PUSH margin | IMPACT margin | Gate |
|---:|---|---|---:|---:|---|
| 1 | PUSH-01 | IMPACT-01 | 6 | -6 | FAIL |
| 2 | PUSH-02 | IMPACT-02 | 8 | -8 | FAIL |
| 3 | PUSH-03 | IMPACT-03 | 8 | -6 | FAIL |

- Passing pairs: `0/3`
- Aggregate Gate: `FAIL`

## Proposed Outcome

- Precedence: `PRIORITY_8_MIXED_RESULT`
- Outcome: `CAL003_R1_MIXED_REPEATABILITY_SIGNAL_REQUIRES_HUMAN_DECISION`
- Status: `PROPOSED_PENDING_FRESH_HUMAN_FINAL_DECISION`
- Automatic decision/expansion: `false/false`
- Fresh human decision required: `true`

The result is a governed experimental calculation. It authorizes no automatic
next experiment, retry, resubmit, redownload, production reentry, final master,
or lock.

## Boundaries

- Evidence coverage: `12/12` outputs, `7/7` committed inputs, `2/2` ZIPs
- Dreamina/Provider/credits/randomness: `0/0/0/0`
- Semantic re-review/new scoring: `false/false`
- Source/Prompt/package/reference/media changes: `0/0/0/0/0`
- Salt, salt hash, raw mapping, raw sealed bytes, equivalence persisted: `false`
- Temporary cleanup: required and verified before staging
- Production approved/fixed task/final master/locked: `false/false/false/false`

## Next Phase

`CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_UNBLINDED_GATE_RESULT_AND_NEXT_EXPERIMENT_HUMAN_DECISION`
