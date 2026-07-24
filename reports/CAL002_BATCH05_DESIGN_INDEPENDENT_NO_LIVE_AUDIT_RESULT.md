# CAL-002 Batch05 Design Independent No-Live Audit Result

## 1. Executive Decision

```yaml
goal_identity: CAL002_BATCH05_DESIGN_INDEPENDENT_NO_LIVE_AUDIT_V0_1
decision: CAL002_BATCH05_DESIGN_NEEDS_FIX
specific_verdict: CAL002_BATCH05_DESIGN_NEEDS_FIX_BLIND_REVIEW_SCHEMA
repair_class: bounded_no_live_schema_fix
experimental_redesign_required: false
prompt_change_required: false
task_change_required: false
budget_change_required: false
live_authority_created: false
```

The committed Batch05 design passes repository-transition, artifact-binding,
serialization, fixed-task, Prompt-blueprint, variable-isolation, endpoint,
budget, and authority checks. It is not ready for package build because the
review schema requires a blind reviewer to set
`candidate_clear_advantage` without access to the Candidate/Control mapping.
No valid two-stage or post-unblinding derived-record semantics are defined.

This is a bounded schema defect. It does not invalidate the research question,
the eight-task design, the four Prompt blueprints, or the budget estimate.

## 2. Checkpoint and One-Commit Transition Audit

| Check | Audited value | Result |
| --- | --- | --- |
| Branch | `main` | PASS |
| Starting local HEAD | `7250719ddb9fd253f15e71190884400674aa65f9` | PASS |
| Locally recorded `origin/main` | `7250719ddb9fd253f15e71190884400674aa65f9` | PASS |
| HEAD/origin alignment | aligned | PASS |
| Expected parent | `f23d9511c5b13c877a9773fe10d68d1772ca3be8` | PASS |
| HEAD parent | `f23d9511c5b13c877a9773fe10d68d1772ca3be8` | PASS |
| Parent-to-HEAD commit count | `1` | PASS |
| Commit message | `design(cal002): add Batch05 action-family replication plan` | PASS |
| Staged files before audit | `0` | PASS |
| Tracked modifications before audit | `0` | PASS |
| Source tracked/staged modifications | `0` | PASS |

The transition contains exactly nine additions. It contains zero modified,
deleted, renamed, or unexpected paths.

Human-confirmed Project Source interpretation remains:

```yaml
active_project_source_index: V1.13
active_prompt_compiler: V0.3
active_rolling_state: V0.1
active_by_current_human_instruction: true
embedded_candidate_status_text_stale: true
local_source_sync_authorized: false
```

The local mirror does not override that human-confirmed state.
`ACTION_RULE_V0.4` remains unofficial, provisional, and not a general default.

## 3. Nine-File Binding Table

Each working-tree file is byte-identical to its committed `HEAD` blob.

| Artifact | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md` | 15452 | `cdf63b0dce697dc80c0d9f4f2ecd2674f00cbc24b93827cc9138a20b400661a4` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json` | 13638 | `7e464052018aca35ed4f8a708928f60f71fbcb9010fa2376626f490eff70e9dc` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_task_matrix.csv` | 3571 | `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_variable_lock_table.csv` | 1902 | `5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_treatment_diff_matrix.json` | 7766 | `2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json` | 9225 | `cadb71d24879c0a60d0658a7a399725b87eccbce15ca208adfd63b1fd476e8b6` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_budget_and_authority_plan.json` | 3359 | `82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e` | PASS |
| `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json` | 3513 | `17da5b76d854b0d44e1d0d37f70d093c52083cddff22594f793b1aaf4049bef9` | PASS |
| `reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md` | 10109 | `ebfc90b20d60e277bc21668434739703aab05beff47eb581a90c39a361d26940` | PASS |

The evidence manifest binds the other eight artifacts by path, byte length,
SHA-256, artifact class, and creation phase. It explicitly excludes itself to
avoid recursive self-hashing. No binding mismatch was found.

## 4. JSON, CSV, and Schema Validation

All five JSON files pass:

- strict UTF-8 parsing;
- no BOM, duplicate key, NaN, or Infinity;
- deterministic `sort_keys` serialization with two-space indentation;
- exactly one terminal LF;
- current bytes equal committed bytes.

Both CSV files pass strict UTF-8 parsing, explicit and stable header order,
exactly one terminal LF, and embedded-command screening.

| CSV | Data rows | Expected | Result |
| --- | ---: | ---: | --- |
| `batch05_task_matrix.csv` | 8 | 8 | PASS |
| `batch05_variable_lock_table.csv` | 24 | 24 | PASS |

The visual-review schema passes `Draft202012Validator.check_schema`. Its
syntactic validity does not resolve the semantic blind-review contradiction
described in Section 11.

## 5. Fixed-Task Matrix Audit

```yaml
action_family_count: 2
treatments_per_family: 2
replicates_per_cell: 2
fixed_phase1_task_count: 8
actual_task_count: 8
unique_task_ids: 8
unique_review_aliases: 8
automatic_task_expansion: false
tie_breaker_created: false
tie_breaker_authorized: false
```

| Cell | Tasks | Result |
| --- | ---: | --- |
| `push_reaction / control` | 2 | PASS |
| `push_reaction / candidate` | 2 | PASS |
| `brief_impact_recoil / control` | 2 | PASS |
| `brief_impact_recoil / candidate` | 2 | PASS |

All eight exact task identities are present, no ninth task exists, and every
submit/query/download/retry/resubmit/batch/final/lock flag is false.

The future provider design target is consistent:

```yaml
task_type: text2video
model_version: seedance2.0_vip
duration: 5
ratio: "16:9"
video_resolution: 720p
reference_strategy: text_only_no_active_generation_reference
active_generation_reference_count: 0
prompt_language: English
fresh_runtime_support_claimed: false
```

## 6. Prompt-Blueprint Reconstruction

The independent assembly used UTF-8 without BOM, exactly two LF bytes between
blocks, and exactly one terminal LF:

```text
SHARED_VISUAL_CONSTANT_BLOCK

SHARED_SAFETY_AND_CAMERA_BLOCK

SELECTED_ACTION_FAMILY_TREATMENT_BLOCK

SHARED_COMPACT_NEGATIVE_BLOCK
```

| Cell | Reconstructed bytes | Reconstructed SHA-256 | Result |
| --- | ---: | --- | --- |
| `PUSH_CONTROL` | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | PASS |
| `PUSH_CANDIDATE` | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | PASS |
| `IMPACT_CONTROL` | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | PASS |
| `IMPACT_CANDIDATE` | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | PASS |

Shared block hashes also match:

```text
SHARED_VISUAL_CONSTANT_BLOCK =
0dfde4b0f6c8ee1bed94cda3d8e727d5352498524b03bbb0f4d9e15f6304acd9

SHARED_SAFETY_AND_CAMERA_BLOCK =
c51ad0c1788a1e923a9d7fa300b3e9b37fe282eee39cbc3c120c50e3febddbdc

SHARED_COMPACT_NEGATIVE_BLOCK =
5e675cf7e987e4a9acc31471650ad27666b6e215433c3e7ba4cf95089697945e
```

Within each cell, R01 and R02 bind the same reconstructed Prompt hash.
Task IDs, replicate IDs, blind aliases, and `REVIEW_CONTRACT_BLOCK` do not
enter provider Prompt bytes.

## 7. Variable-Isolation Audit

The variable-lock table and clause-level diff preserve performer count,
performer descriptions, costumes, scene, lighting, camera, framing, style,
duration, provider target, reference strategy, active-reference count, safety
framing, and the shared negative block.

The only systematic Control/Candidate difference is:

```text
action_family_causal_compiler_treatment
```

```yaml
treatment_unit: complete_action_family_compiler_bundle
component_level_causal_attribution_permitted: false
```

No component-level causal claim can be derived from this compound treatment.

## 8. Control-Baseline Judgment

Both controls are legitimate matched high-level baselines.

- Push Control clearly requests one controlled two-hand push, backward
  receiver movement, and balance recovery.
- Impact Control clearly requests one controlled forearm impact, receiver
  reaction with a backward step, and a safe finish.

Neither Control is a no-action Prompt or an intentionally defective Prompt.
Candidate-only timing and causal-chain clauses are absent as intended.

```yaml
control_is_intentionally_defective: false
control_matched_baseline_validity: PASS
```

## 9. Replication and Attribution Boundaries

R01 and R02 measure consistency under uncontrolled provider-output variation.
The design does not invent a provider seed and does not permit statistical
significance, single-component attribution, or cross-action generalization.

First-frame contact invalidates onset evaluation for both families. The
family-level decision matrix includes positive, shared-success, inconclusive,
regression, and route-reset outcomes without automatically creating an extra
task. Any tie-breaker requires a separate no-live design and human decision.

## 10. Blind-Alias Balance

The alias placement is correctly counterbalanced:

| Pair | A | B | Result |
| --- | --- | --- | --- |
| `PUSH_PAIR_01` | Control R01 | Candidate R01 | PASS |
| `PUSH_PAIR_02` | Candidate R02 | Control R02 | PASS |
| `IMPACT_PAIR_01` | Candidate R01 | Control R01 | PASS |
| `IMPACT_PAIR_02` | Control R02 | Candidate R02 | PASS |

Task IDs and treatment mapping are absent from the review schema, while the
mapping is stored in the design manifest and task matrix. A future
reviewer-facing package must exclude both mapping-bearing files.

## 11. Blind-Review Schema Finding

**Severity: material and decision-bearing.**

The blinded `pair_reviews` item requires:

```text
pair_id
comparison_validity
preference
candidate_clear_advantage
```

The blind reviewer is intended to know only A/B aliases. Therefore the
reviewer can determine `preference`, but cannot determine whether that
preference means Candidate advantage without accessing treatment mapping.

An in-memory Draft 2020-12 validation probe confirmed:

- a proper blind A/B record without `candidate_clear_advantage` fails because
  that property is required;
- adding a Candidate-specific boolean makes the record pass even when no
  reviewer rationale is supplied;
- an invalid/not-comparable record also passes without rationale.

No post-unblinding derived record or two-stage schema exists in the committed
design. The current schema therefore contradicts its own blind-review policy.

The bounded required correction is:

1. Remove `candidate_clear_advantage` from the blinded reviewer record.
2. Keep the blind record limited to `pair_id`, `comparison_validity`, A/B
   `preference`, and reviewer rationale.
3. Require a non-empty rationale for invalid, inconclusive, not-comparable,
   and clearly-better judgments, either conditionally or for every pair.
4. Define a separate post-unblinding derived record for
   `candidate_clear_advantage`, Candidate/Control interpretation, and the
   family-level decision.
5. Require the future reviewer package to exclude
   `batch05_design_manifest.json` and `batch05_task_matrix.csv`.

```yaml
blind_reviewer_can_complete_current_schema_without_treatment_knowledge: false
blind_review_schema_verdict: NEEDS_FIX
repair_scope: bounded_no_live_schema_fix
experimental_redesign: false
prompt_change: false
task_change: false
budget_change: false
live_authority: false
```

## 12. Review Endpoint Completeness

The schema requires exactly eight video reviews and four pair reviews.
`complete_mp4_review_confirmed` is fixed to true. Contact sheets and
synchronized comparisons cannot replace full-MP4 review.

The required enums cover initial state, action onset, contact onset and
duration, post-contact response, torso displacement, upper-body recoil, foot
count/type/timing, release/retract, prolonged contact, static-tail timing,
ending contract, action-family match, identity, full-body visibility, camera,
technical validity, usability, and primary endpoint.

Action-specific strength and response fields include usable
`NOT_APPLICABLE`, `UNKNOWN`, or null states where needed. No impossible
per-video field combination was found. The material defect is confined to the
pair-level blind/post-unblind separation and rationale requirement.

## 13. Budget and Authority Audit

All four bound Batch04 submit-credit records remain byte/hash valid and record:

```text
70
70
70
70
```

```yaml
observed_minimum: 70
observed_maximum: 70
observed_mean: 70
observed_total: 280
planned_phase1_tasks: 8
provisional_base_estimate: 560
provisional_conservative_ceiling: 560
fresh_current_credit_checked: false
historical_balance_reused_as_current: false
current_credit_balance_claimed: false
```

The `560` estimate is historical and provisional. It is not a fresh budget
authorization and is not a current balance.

Proposed future limits remain non-active:

```yaml
phase1_fixed_submit_max: 8
retry_max: 0
resubmit_max: 0
batch_retry_max: 0
automatic_task_expansion: false
tie_breaker_authorized: false
query_requires_separate_future_authorization: true
download_requires_separate_future_authorization: true
current_provider_authority: false
```

## 14. No-Live and Source Boundary

This audit made no Dreamina, provider, version, credit, help, submit, query,
download, retry, resubmit, batch, login, or session call. It created no Prompt
package, execution package, live manifest, authorization text, media, frame,
contact sheet, comparison sheet, final state, or lock state.

`sources/` remained read-only and clean. No Batch05 design artifact was
modified.

```yaml
Dreamina_called: false
provider_called: false
provider_command_count: 0
Prompt_package_created: false
execution_package_created: false
authorization_text_created: false
submit_authorized: false
query_authorized: false
download_authorized: false
retry_authorized: false
resubmit_authorized: false
batch_authorized: false
media_created: false
review_artifacts_created: false
sources_changed: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

## 15. Exact Next Phase

```text
CAL002_BATCH05_DESIGN_TARGETED_FIX_NO_LIVE
```

That phase should perform only the bounded review-schema separation described
in Section 11. It must not alter experimental tasks, Prompt blueprints,
provider targets, budget, Source, or live authority.
