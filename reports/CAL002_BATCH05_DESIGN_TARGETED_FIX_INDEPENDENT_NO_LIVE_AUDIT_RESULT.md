# CAL-002 Batch05 Targeted Fix Independent No-Live Audit Result

## 1. Executive Decision

```yaml
goal_identity: CAL002_BATCH05_TARGETED_FIX_INDEPENDENT_NO_LIVE_REAUDIT_V0_1
decision: NEEDS_FIX
specific_verdict: CAL002_BATCH05_TARGETED_FIX_NEEDS_SECOND_BOUNDED_SCHEMA_FIX
original_targeted_fix_corrected: true
ready_for_no_live_package_build: false
repair_class: bounded_no_live_review_derivation_integrity_fix
experimental_redesign: false
Prompt_change: false
task_change: false
budget_change: false
provider_target_change: false
live_authority: false
```

The bound targeted fix correctly separates blind A/B review from
Candidate/Control interpretation. It removes the Candidate-specific field from
the blind schema, requires a non-empty pair rationale, and introduces a
post-unblinding record.

The design is not yet ready for a no-live package build. Independent negative
probes show that the current schemas still accept incomplete identity coverage,
contradictory pair derivations, substituted blind values, arbitrary mapping
hashes, and family verdicts that contradict their recorded counts. These are
bounded review and analysis integrity defects. They do not require an
experimental redesign or any change to tasks, Prompt blueprints, provider
target, budget, Source, or authority.

## 2. Checkpoint and Seven-Path Transition Audit

| Check | Audited value | Result |
| --- | --- | --- |
| Repository branch | `main` | PASS |
| Starting local HEAD | `59a1f39a449b6bffb69e63d72afcd8a4ec83dff3` | PASS |
| Locally recorded `origin/main` | `59a1f39a449b6bffb69e63d72afcd8a4ec83dff3` | PASS |
| HEAD/origin alignment | aligned | PASS |
| Expected parent | `b7f93897557b057824544e77f31c452685dbf129` | PASS |
| Actual parent | `b7f93897557b057824544e77f31c452685dbf129` | PASS |
| Parent-to-HEAD commit count | `1` | PASS |
| Commit message | `fix(cal002): separate Batch05 blind review analysis` | PASS |
| Staged files before audit | `0` | PASS |
| Tracked modifications before audit | `0` | PASS |
| Source tracked/staged modifications | `0` | PASS |

The parent-to-HEAD transition contains exactly five modified paths and two
added paths:

| Status | Path |
| --- | --- |
| M | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md` |
| M | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json` |
| M | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json` |
| A | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json` |
| M | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json` |
| M | `reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md` |
| A | `reports/CAL002_BATCH05_DESIGN_TARGETED_FIX_RESULT.md` |

```yaml
modified_paths: 5
added_paths: 2
deleted_paths: 0
renamed_paths: 0
unexpected_paths: 0
```

## 3. Updated Artifact Bindings

All seven updated artifacts match the required current byte bindings.

| Artifact | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| `CAL002_BATCH05_DESIGN_SPEC.md` | 17227 | `a8604c73cd41ab45ee8abffd398b5b882da2acb6db2bad127e0ca76819b72ab7` | PASS |
| `batch05_design_manifest.json` | 15801 | `0f226189d89bcc67341e39f668ebd74f5d85eedd8818095c4343619766559c9a` | PASS |
| `batch05_visual_review_schema.json` | 9174 | `3e3f816527334ebd0e57078fd1aa9cfc61022698de27209ccd8a2d0dbfb2854c` | PASS |
| `batch05_post_unblinding_analysis_schema.json` | 8741 | `bd3c21b07e44ebe8b40a7d4d92e74d443967b88a15a350e83b5e94665a0442da` | PASS |
| `batch05_design_evidence_manifest.json` | 3870 | `fe128c8a45007e679e4e073d3c93cf7cf04b412b662e03c23b07d9f3ae527a93` | PASS |
| `CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md` | 11646 | `5ce71940f0ff77628a8be2607d6b9b4b1d1ecab9992b0318a9c87c1134e33940` | PASS |
| `CAL002_BATCH05_DESIGN_TARGETED_FIX_RESULT.md` | 10939 | `33969b9bc3ddfd88655abce6c05e89e53ec1a7a29b6ac32aaede84ee0ec1acc7` | PASS |

The targeted-fix report contains:

```text
CAL002_BATCH05_TARGETED_FIX_APPLIED_READY_FOR_INDEPENDENT_REAUDIT
```

The design evidence manifest declares and contains exactly nine unique
non-self bindings. Every bound path, byte length, and SHA-256 matches the
current committed file. The manifest explicitly excludes itself and does not
bind itself recursively.

All six audited Batch05 JSON artifacts use strict UTF-8 without BOM, LF-only
line endings, two-space `sort_keys` serialization, and exactly one final LF.
Both JSON Schemas pass `Draft202012Validator.check_schema`.

## 4. Original Targeted-Fix Verification

| Required correction | Result |
| --- | --- |
| `candidate_clear_advantage` absent from blind schema | PASS |
| Candidate-specific field rejected as an additional property | PASS |
| `reviewer_rationale` required for every pair | PASS |
| `reviewer_rationale.minLength` equals `1` | PASS |
| Blind video-review count fixed at `8` | PASS |
| Blind pair-review count fixed at `4` | PASS |
| Blind record finalized before unblinding | PASS |
| Candidate advantage moved to post-unblinding schema | PASS |
| Mapping-bearing files excluded from reviewer package | PASS |

The original treatment-leak defect is corrected. The new finding is narrower:
exact array lengths do not guarantee exact identity coverage, and the
post-unblinding schema records derived-looking values without enforcing the
derivation.

## 5. Blind Alias and Pair Coverage Probes

A valid eight-video/four-pair baseline record passes. Each malformed identity
probe below should be rejected, but all six validate successfully.

| Negative probe | Expected | Actual |
| --- | --- | --- |
| Duplicate one `review_alias` and omit another | REJECT | VALIDATED |
| Repeat one `review_alias` eight times | REJECT | VALIDATED |
| Duplicate one `pair_id` and omit another | REJECT | VALIDATED |
| Repeat one `pair_id` four times | REJECT | VALIDATED |
| Eight videos with only four aliases repeated | REJECT | VALIDATED |
| Four pairs with only two pair IDs repeated | REJECT | VALIDATED |

```yaml
blind_alias_coverage_enforced: false
pair_id_coverage_enforced: false
duplicate_alias_probes: FAIL
duplicate_pair_probes: FAIL
```

The blind schema uses `minItems` and `maxItems` with an enum-constrained
generic item schema. It does not use fixed positional identities or another
constraint that requires every alias and pair exactly once. No checked-in
deterministic Batch05 identity validator or explicitly bound future validation
contract was found. A bounded schema correction or a mandatory deterministic
external identity validator is required.

## 6. Pair-Derivation Truth-Table Probes

A structurally valid post-unblinding baseline passes. Every contradictory
probe below should be rejected, but all ten validate successfully.

| Negative probe | Expected | Actual |
| --- | --- | --- |
| Candidate side A, preference B, Candidate-advantage class | REJECT | VALIDATED |
| Candidate side B, preference A, Candidate-advantage class | REJECT | VALIDATED |
| Control-selected preference with Candidate advantage true | REJECT | VALIDATED |
| Invalid comparison classified as Candidate advantage | REJECT | VALIDATED |
| Invalid comparison classified as Control advantage | REJECT | VALIDATED |
| Inconclusive comparison classified as Candidate advantage | REJECT | VALIDATED |
| Valid Candidate preference classified as Control advantage | REJECT | VALIDATED |
| Valid Control preference classified as Candidate advantage | REJECT | VALIDATED |
| Valid no-difference preference classified as Candidate advantage | REJECT | VALIDATED |
| Invalid comparison with an A/B clear preference | REJECT | VALIDATED |

The current schema enforces only two local facts:

1. Candidate and Control sides differ.
2. `candidate_clear_advantage` is true exactly when
   `derivation_class=CANDIDATE_CLEAR_ADVANTAGE`.

It does not derive the class from Candidate side, Control side, blind validity,
and blind preference. Invalid and inconclusive combinations are also not
constrained to their required preference and derivation classes.

```yaml
pair_derivation_truth_table_enforced: false
invalid_comparison_derivation_enforced: false
inconclusive_derivation_enforced: false
contradictory_pair_probes: 10_of_10_unexpectedly_valid
```

## 7. Blind-Record-to-Derived-Record Binding Audit

An in-memory substitution probe kept the same
`blind_review_record_sha256`, changed a pair's repeated blind preference and
validity-derived interpretation, and still produced a schema-valid
post-unblinding record.

```yaml
same_blind_record_hash_retained: true
blind_values_changed: true
mutated_record_validated: true
blind_values_cryptographically_bound_to_derived_record: false
```

The schema checks only the syntax of the blind-record hash. It cannot read the
sealed blind record or prove that repeated `blind_comparison_validity` and
`blind_preference` values came from that record. No checked-in deterministic
Batch05 derivation tool exists, and the current design does not bind a
mandatory external derivation validator. Therefore operator-supplied
substitution can be structurally valid.

## 8. Family-Decision Truth-Table Probes

Every contradictory family probe below should be rejected, but all nine
validate successfully.

| Negative probe | Expected | Actual |
| --- | --- | --- |
| Positive result with all decision counts zero | REJECT | VALIDATED |
| Positive result with Candidate primary pass count `1` | REJECT | VALIDATED |
| Positive result with Candidate advantage count `1` | REJECT | VALIDATED |
| Positive result with one valid pair | REJECT | VALIDATED |
| Both-success result when Candidate is not `2/2` | REJECT | VALIDATED |
| Both-success result with Candidate advantage `2/2` | REJECT | VALIDATED |
| Regression result with an otherwise replicated positive state | REJECT | VALIDATED |
| Route-reset result with an otherwise replicated positive state | REJECT | VALIDATED |
| Inconclusive result with an otherwise replicated positive state | REJECT | VALIDATED |

The schema independently bounds each count to `0..2` and enumerates the result
label, but does not connect them. In addition, the available family-decision
fields do not represent repeated wrong-family routing, uncontrolled variation,
or all evidence needed to derive regression and route-reset outcomes
deterministically.

```yaml
family_decision_truth_table_enforced: false
contradictory_family_probes: 9_of_9_unexpectedly_valid
available_family_decision_fields_sufficient: false
```

The bounded repair must either add the required counts and flags with complete
constraints or bind a deterministic derivation tool that rejects every
contradictory state.

## 9. Mapping-Source Verification Contract

The post-unblinding schema correctly fixes the two mapping-source paths:

```text
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_task_matrix.csv
```

It requires positive byte lengths and lowercase 64-character hashes. However,
a negative probe replaced both byte lengths and hashes with arbitrary
syntactically valid values while preserving the paths; the record still
validated.

The design says the record contains mapping bindings, but it does not
explicitly bind a deterministic step that independently reads the current
committed files, recomputes both values, and blocks before unblinding on any
mismatch. No checked-in Batch05 tool performs that verification.

```yaml
mapping_paths_fixed: true
arbitrary_mapping_values_rejected: false
mapping_hashes_independently_verifiable_by_current_contract: false
```

## 10. Immutable Task, Prompt, and Budget Checks

All immutable design bindings remain unchanged.

| Artifact | SHA-256 | Result |
| --- | --- | --- |
| `batch05_task_matrix.csv` | `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32` | PASS |
| `batch05_variable_lock_table.csv` | `5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a` | PASS |
| `batch05_treatment_diff_matrix.json` | `2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f` | PASS |
| `batch05_budget_and_authority_plan.json` | `82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e` | PASS |

The task matrix contains eight unique task IDs and eight unique aliases. Each
of the four family/treatment cells contains two tasks. All active-reference
counts are zero and every submit, query, download, retry, resubmit, batch,
final, and lock field is false.

Independent UTF-8 Prompt reconstruction also passes:

| Cell | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| `PUSH_CONTROL` | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | PASS |
| `PUSH_CANDIDATE` | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | PASS |
| `IMPACT_CONTROL` | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | PASS |
| `IMPACT_CANDIDATE` | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | PASS |

Shared blocks remain unchanged:

```text
SHARED_VISUAL_CONSTANT_BLOCK =
0dfde4b0f6c8ee1bed94cda3d8e727d5352498524b03bbb0f4d9e15f6304acd9

SHARED_SAFETY_AND_CAMERA_BLOCK =
c51ad0c1788a1e923a9d7fa300b3e9b37fe282eee39cbc3c120c50e3febddbdc

SHARED_COMPACT_NEGATIVE_BLOCK =
5e675cf7e987e4a9acc31471650ad27666b6e215433c3e7ba4cf95089697945e
```

```yaml
planned_task_count: 8
automatic_task_expansion: false
tie_breaker_authorized: false
provisional_budget_base: 560
provisional_budget_ceiling: 560
provider_authority_created: false
final_master: false
locked: false
```

## 11. No-Live and Source Boundary

This re-audit made no Dreamina, provider, version, credit, help, submit, query,
download, retry, resubmit, batch, login, or session call. It created no Prompt
package, execution package, command, authorization text, media, or review
artifact. It did not modify any Batch05 design artifact.

`sources/` remained read-only and has zero tracked or staged changes.
Unrelated untracked workspace material was left untouched.

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

## 12. Exact Next Phase

```text
CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_TARGETED_FIX_NO_LIVE
```

The next phase is limited to:

- enforcing every blind alias and pair ID exactly once;
- enforcing the complete pair-derivation truth table;
- binding repeated blind values to the sealed blind record;
- constraining family verdicts from sufficient underlying evidence;
- requiring deterministic verification of mapping-source bytes and hashes.

It must not redesign the experiment, change any Prompt, task, provider target,
budget, Source, or authority, create a provider package, or perform a live
operation.

```yaml
final_verdict: CAL002_BATCH05_TARGETED_FIX_NEEDS_SECOND_BOUNDED_SCHEMA_FIX
required_repair_class: bounded_no_live_review_derivation_integrity_fix
```
