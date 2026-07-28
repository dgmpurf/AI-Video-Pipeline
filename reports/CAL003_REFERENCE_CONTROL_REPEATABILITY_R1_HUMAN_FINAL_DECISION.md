# CAL-003 Reference-Control Repeatability R1 Human Final Decision

## Decision

- Human final decision: `CAL003_R1_MIXED_REPEATABILITY_SIGNAL_REQUIRES_HUMAN_DECISION`
- Human decision complete: `true`
- CAL-003 R1 round closed: `true`
- Automatic expansion: `false`

## Accepted Gate Evidence

| Family | Sample passes | Own scores | Median own | Margins | Median margin | Gate |
|---|---:|---|---:|---|---:|---|
| PUSH | 3/3 | 12, 12, 12 | 12 | 6, 8, 8 | 8 | PASS |
| IMPACT | 0/3 | 6, 4, 6 | 6 | -6, -8, -6 | -6 | FAIL |

Ordinal matched pairs passed `0/3`; the aggregate ordinal-pair Gate is `FAIL`.

## Scientific Interpretation

The PUSH reference produced repeatable PUSH-like differentiation. The IMPACT
reference did not produce IMPACT-specific differentiation. The six outputs
collectively showed asymmetric collapse toward PUSH-like behavior.

CAL-003 does not independently identify common Prompt dominance, weak
IMPACT-reference signal, Provider action-family bias, scene or actor prior, or
any single Prompt component as the cause.

## Governance Deviation

Classification:
`NON_SCIENTIFIC_TEMPORARY_CLEANUP_TIMING_DEVIATION`

The temporary recovery helper was deleted after push rather than before
staging. It was neither staged nor committed; the committed path set remained
exactly 13/13. No sealed bytes, salt, raw mapping, raw equivalence, or secret
entered the helper. No experiment input, frozen review, score, Gate, mapping,
or outcome changed. The scientific result remains accepted. The historical
report statement claiming cleanup before staging is preserved and is not
silently rewritten.

## Governance State

- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`
