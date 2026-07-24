# CAL-002 Batch05 Targeted Package Fix Independent No-Live Audit Result

## 1. Executive Decision

```text
phase = CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_INDEPENDENT_NO_LIVE_AUDIT
goal_identity = CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_INDEPENDENT_NO_LIVE_AUDIT_V0_1
decision = CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_READY_FOR_LIVE_SUBMIT_AUTHORIZATION_DECISION
specific_verdict = READY
```

The independent re-audit confirms that all three prior package-contract
defects are corrected. The corrected package checkpoint is suitable for a
separate human live-submit authorization decision. This audit itself creates
no live authority.

## 2. Checkpoint And Eleven-Path Transition

```text
branch = main
starting_HEAD = 1a231ef27855aae4e144833c4b633643e5e8fea5
starting_origin/main = 1a231ef27855aae4e144833c4b633643e5e8fea5
HEAD_origin_aligned = true
targeted_fix_parent = 348284c98461debdf559686df92dbfd5fce9a983
parent_to_HEAD_commit_count = 1
targeted_fix_subject = fix(cal002): correct Batch05 execution package contracts
modified_paths = 10
added_paths = 1
deleted_paths = 0
renamed_paths = 0
unexpected_paths = 0
total_changed_paths = 11
```

The ten modified paths are exactly the eight task package JSON files, package
index, and package evidence manifest. The only added path is:

```text
reports/CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_RESULT.md
```

No staged, tracked, or Source modification existed at audit preflight.

## 3. Targeted-Fix And Prior-Audit Bindings

```text
targeted_fix_report = reports/CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_RESULT.md
targeted_fix_report_bytes = 12914
targeted_fix_report_sha256 = 1c3caa02ba2cd1abb38cb01a2e8c05c75622e110a2b0590bfdbb0eb559034f53
targeted_fix_report_decision = CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_APPLIED_READY_FOR_INDEPENDENT_NO_LIVE_AUDIT
targeted_fix_report_binding = PASS

prior_package_audit = reports/CAL002_BATCH05_EXECUTION_PACKAGE_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
prior_package_audit_bytes = 17534
prior_package_audit_sha256 = 4cd1d3522b50b22cfe962d7296e80a3d6998567a56727bb35f7473f4fb772d92
prior_package_audit_decision = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX
prior_package_audit_specific_verdict = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX_EXPLICIT_POLL_ZERO
prior_package_audit_binding = PASS
```

The prior defect set was independently confirmed as:

```text
EXPLICIT_POLL_ZERO_MISSING
PACKAGE_BUILD_CHECKPOINT_OR_REPORT_BINDING_MISSING
PHASE1_ORDER_OUTSIDE_REPLICATE_DIFFERENCE_ALLOWLIST
```

## 4. External Corrected-Checkpoint Binding

This audit report externally binds:

```text
corrected_package_fix_checkpoint = 1a231ef27855aae4e144833c4b633643e5e8fea5
```

The complete lineage is:

```text
design_package_input_checkpoint = 2575d1a7a7ed7215d06d715c6603495c809d8005
original_package_build_checkpoint = 3de46cb5c12bba925b274dfcdc818f6b7f6bacdf
first_package_audit_checkpoint = 348284c98461debdf559686df92dbfd5fce9a983
corrected_package_fix_checkpoint = 1a231ef27855aae4e144833c4b633643e5e8fea5
```

The index correctly avoids impossible commit self-reference. A future live
authorization must bind this corrected checkpoint and the committed checkpoint
of this post-fix independent audit.

## 5. Runtime Help Comparison

The audit independently called exactly once each:

```text
C:/Users/msjpurf/bin/dreamina.exe version
C:/Users/msjpurf/bin/dreamina.exe text2video -h
```

Current output matched the immutable runtime preflight byte-for-byte.

| Stream | Exit | Bytes | SHA-256 | Comparison |
|---|---:|---:|---|---|
| `version` stdout | 0 | 96 | `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0` | exact |
| `version` stderr | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | exact |
| `text2video -h` stdout | 0 | 1708 | `17e92789fc0633fa2563a3f3260865a955c08813d55deb681f4c7936ba2ecde4` | exact |
| `text2video -h` stderr | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | exact |

```text
runtime_version = 2a20fff-dirty
runtime_commit = 2a20fff
runtime_build_time = 2026-06-26T06:36:39Z
text2video_bound_flags_supported = true
poll_help_states_zero_disables_polling = true
session_help_explicit_default_zero = true
runtime_drift = false
```

## 6. Poll-Zero Verification

Every corrected package contains:

```yaml
poll_seconds: 0
poll_is_explicit: true
poll_behavior: SUBMIT_ONLY_NO_IMPLICIT_QUERY
```

Every command plan has exactly one `--poll` entry with integer value `0`.
The independently verified flag order is:

```text
--model_version
--ratio
--duration
--video_resolution
--poll
--prompt
```

```text
packages_checked = 8
explicit_poll_zero_packages = 8
poll_occurrences_per_package = 1
implicit_query_or_wait_present = false
poll_zero_verification = PASS
```

## 7. Eight Inert Argv Hashes

Eight argv arrays were reconstructed independently from corrected package data
and exact Prompt bytes. No argv was executed. Hashes are SHA-256 over compact
UTF-8 JSON serialization of the ordered argv array.

| Task | Elements | Argv SHA-256 |
|---|---:|---|
| CAL002-B05-PUSH-CONTROL-R01 | 14 | `762442b3a416eaff1b32ccbdfac67c4a868b82c24c83831fad530bb8eaf13f65` |
| CAL002-B05-PUSH-CONTROL-R02 | 14 | `762442b3a416eaff1b32ccbdfac67c4a868b82c24c83831fad530bb8eaf13f65` |
| CAL002-B05-PUSH-CANDIDATE-R01 | 14 | `090b5d766be3ed7a18662a814f24d91d583fa8b8e1b7215ff65328f47ecb23b0` |
| CAL002-B05-PUSH-CANDIDATE-R02 | 14 | `090b5d766be3ed7a18662a814f24d91d583fa8b8e1b7215ff65328f47ecb23b0` |
| CAL002-B05-IMPACT-CONTROL-R01 | 14 | `3326c8fa8a22f37c13529d2b758b7b0068b3cfc7cb8544efa0cabf47e4aff101` |
| CAL002-B05-IMPACT-CONTROL-R02 | 14 | `3326c8fa8a22f37c13529d2b758b7b0068b3cfc7cb8544efa0cabf47e4aff101` |
| CAL002-B05-IMPACT-CANDIDATE-R01 | 14 | `3522e9c93ba34c5f94d9a607d1a5eea9b8763f68f2e80eb8a116466766ad08c1` |
| CAL002-B05-IMPACT-CANDIDATE-R02 | 14 | `3522e9c93ba34c5f94d9a607d1a5eea9b8763f68f2e80eb8a116466766ad08c1` |

```text
rendered_argv_count = 8
elements_per_argv = 14
unique_argv_hashes = 4
R01_R02_argv_identity_within_cell = true
Prompt_text_is_one_argv_element = true
argv_executed = false
```

No argv contains a task ID, blind alias, Prompt path, session, output
directory, output name, download directory, submit ID, result ID,
authorization token, or retry instruction.

## 8. Session-Default Treatment

Current help still explicitly records session default `0`. All packages and
all reconstructed argv arrays omit `--session`.

```text
session_argument_present = false
active_session_state_present = false
session_operation_called = false
session_contract = PASS
```

## 9. `phase1_order` Absence

Exact package-byte scans and parsed-object scans confirm:

```text
phase1_order_present_in_package_bytes = false
phase1_order_present_in_parsed_packages = false
phase1_order_present_in_command_plans = false
phase1_order_present_in_provider_arguments = false
phase1_order_present_in_output_bookkeeping = false
packages_checked = 8
phase1_order_package_scan = PASS
```

## 10. Central Phase-1 Order

The package index contains exactly one centralized ordered list:

```text
1. CAL002-B05-PUSH-CONTROL-R01
2. CAL002-B05-PUSH-CONTROL-R02
3. CAL002-B05-PUSH-CANDIDATE-R01
4. CAL002-B05-PUSH-CANDIDATE-R02
5. CAL002-B05-IMPACT-CONTROL-R01
6. CAL002-B05-IMPACT-CONTROL-R02
7. CAL002-B05-IMPACT-CANDIDATE-R01
8. CAL002-B05-IMPACT-CANDIDATE-R02
```

```text
central_order_count = 8
central_order_unique_tasks = 8
central_order_matches_task_matrix = true
provider_argv_affected_by_order = false
central_phase1_order = PASS
```

## 11. Replicate-Difference Audit

Complete parsed-object comparison for every R01/R02 pair returns exactly:

```text
blind_alias
package_id
planned_output_name
replicate
task_id
```

There is no sixth differing key.

```text
replicate_difference_allowlist = PASS
replicate_Prompt_identity = PASS
replicate_command_plan_identity = PASS
replicate_poll_contract_identity = PASS
replicate_provider_identity = PASS
replicate_lineage_identity = PASS
replicate_authority_identity = PASS
```

## 12. Original Package-Build Lineage

The package index correctly binds:

```text
original_package_build_checkpoint.commit = 3de46cb5c12bba925b274dfcdc818f6b7f6bacdf

original_package_build_report.relative_path = reports/CAL002_BATCH05_EXECUTION_PACKAGE_BUILD_RESULT.md
original_package_build_report.byte_length = 8009
original_package_build_report.sha256 = 7977185b9350ae621125e8af5cffae4942bb575c090dc5d952de01a1a040f692
original_package_build_report.decision = CAL002_BATCH05_EXECUTION_PACKAGE_BUILT_READY_FOR_INDEPENDENT_NO_LIVE_AUDIT
```

The index does not claim that the original build commit contains the corrected
package bytes.

## 13. Prior Package-Audit Lineage

The package index correctly binds:

```text
package_audit_checkpoint.commit = 348284c98461debdf559686df92dbfd5fce9a983

package_audit_report.relative_path = reports/CAL002_BATCH05_EXECUTION_PACKAGE_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
package_audit_report.byte_length = 17534
package_audit_report.sha256 = 4cd1d3522b50b22cfe962d7296e80a3d6998567a56727bb35f7473f4fb772d92
package_audit_report.decision = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX
```

## 14. Package-Index Validation

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_package_index.json
byte_length = 10803
sha256 = 9ebf8f5ffb926ac2327d93925f31e09e9fae40367e7202c74264892d9b55e894
strict_canonical_JSON = true
corrected_package_bindings = 8_of_8_PASS
original_build_lineage = PASS
prior_audit_lineage = PASS
central_order = PASS
poll_contract = PASS
package_set_invariants = PASS
```

The self-reference contract is exact:

```yaml
corrected_package_commit_self_bound_in_index: false
corrected_package_commit_requires_external_post_commit_binding: true
future_live_authorization_must_bind_corrected_package_fix_checkpoint: true
future_live_authorization_must_bind_post_fix_independent_audit_checkpoint: true
```

## 15. Evidence-Manifest Validation

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_package_evidence_manifest.json
byte_length = 6483
sha256 = 73be6ac9fc40753295ee7e1a1003f8bf81042b27343a9232128d96bf3bfbb3d9
artifact_count = 16
included_artifact_count = 16
unique_bound_paths = 16
self_excluded = true
binding_mismatches = 0
worktree_HEAD_equality = PASS
```

The manifest binds exactly four Prompts, eight corrected package JSON files,
runtime preflight, execution manifest, corrected package index, and original
package-build report. The targeted-fix report remains outside this original
package evidence manifest as required.

## 16. Mapping, Prompt, Provider, And Budget Regression

All eight packages were cross-checked against the design manifest, task
matrix, and execution manifest.

```text
fixed_task_count = 8
package_count = 8
unique_task_ids = 8
unique_aliases = 8
unique_output_names = 8
experimental_cells = 4
replicates_per_cell = 2

task_type = text2video
model_version = seedance2.0_vip
duration = 5
ratio = 16:9
video_resolution = 720p
reference_strategy = text_only_no_active_generation_reference
active_generation_reference_count = 0

estimated_credit_each = 70
estimated_total_credits = 560
fresh_credit_checked = false
current_balance_claimed = false
provider_field_regression = PASS
```

Immutable bindings:

| Artifact | Bytes | SHA-256 | Result |
|---|---:|---|---|
| PUSH_CONTROL Prompt | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | unchanged |
| PUSH_CANDIDATE Prompt | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | unchanged |
| IMPACT_CONTROL Prompt | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | unchanged |
| IMPACT_CANDIDATE Prompt | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | unchanged |
| Runtime preflight | 6658 | `fedecf44d5b3da7f0d971cd178a4f960f469eef4be006bb8c0a01e0b9f83284b` | unchanged |
| Execution manifest | 4804 | `0aa486cdac6d96a48c2077919e0a17ab26798527d1c4b68f554a2ec51efe581d` | unchanged |
| Original build report | 8009 | `7977185b9350ae621125e8af5cffae4942bb575c090dc5d952de01a1a040f692` | unchanged |

## 17. Authority And Prohibited-Content Audit

Every corrected package explicitly retains:

```yaml
no_submit: true
submit_authorized: false
query_authorized: false
download_authorized: false
retry_authorized: false
resubmit_authorized: false
batch_authorized: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

No corrected artifact contains an active submit ID, result URL, signed URL,
download URL, cookie, token, authorization secret, session ID, login state,
current credit balance, automatic submit/query/download loop, or retry loop.

```text
prohibited_content_scan = PASS
sensitive_state_present = false
live_authority_present = false
```

## 18. Protected-File And No-Live Audit

```text
Dreamina_non_live_introspection_called = true
Dreamina_version_called = true
Dreamina_text2video_help_called = true
Dreamina_generation_called = false
provider_called = false
provider_command_count = 0
user_credit_called = false
login_called = false
session_operation_called = false

Prompt_packages_created_by_audit = false
execution_packages_created_by_audit = false
media_created = false
review_artifacts_created = false
sources_changed = false
tracked_files_changed_by_probes = false
protected_preexisting_files_changed = false
temporary_audit_files_created = false
temporary_audit_files_cleaned = true
```

The Batch05 design tree remains
`493b6ed2c55d52c97607f00b72607f6098bcb2a2`. The Source tree remains
`60eedf926ed525a84c1737fbf8d6dd4b39e46077`. Pre-existing untracked
workspace material was left untouched.

## 19. Final Verdict And Next Phase

```text
decision = CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_READY_FOR_LIVE_SUBMIT_AUTHORIZATION_DECISION
specific_verdict = READY
next_phase = CAL002_BATCH05_PHASE1_LIVE_SUBMIT_AUTHORIZATION_DECISION
```

The next phase is an authorization decision only. This audit does not
authorize or perform submit, query, download, retry, resubmit, batch, credit
spending, production approval, completion, finalization, or locking.
