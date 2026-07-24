# CAL-002 Batch05 Review Derivation Integrity Fix Independent No-Live Audit

## 1. Executive decision

```yaml
goal_identity: CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_INDEPENDENT_NO_LIVE_AUDIT_V0_1
decision: CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_NEEDS_FIX
specific_verdict: NEEDS_FIX
ready_for_execution_package_build_no_live: false
checkpoint_blocked: false
experimental_redesign_required: false
```

The committed fix passes its 59 focused tests and all independent blind-schema,
strict-input, mapping, pair, substitution, determinism, and family-decision
probes. It is not ready for execution-package construction because two bounded
implementation-integrity defects remain:

1. **Material, READY-blocking - executing-tool identity is not enforced.**
   `_tool_binding()` hashes the fixed repository path rather than the Python
   file actually executing. In an isolated repository, a copy at a different
   path with exactly one changed byte completed both `derive` and `verify`
   with exit code 0. The record claimed the clean repository tool SHA-256,
   not the executing copy's SHA-256.
2. **Material, READY-blocking - schemas are hidden mutable inputs.**
   `_load_schema()` reads worktree schema bytes without comparing them with
   `HEAD` and the derived record does not bind either schema. In an isolated
   repository, an uncommitted blind-schema change permitted a previously
   forbidden Candidate-specific top-level field; `derive` still exited 0.

Both defects are local and repairable without changing the experiment,
Prompts, task matrix, provider target, budget, or review policy.

## 2. Checkpoint and nine-path transition

```yaml
repository: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE
branch: main
starting_head: 99f86ddf571a9906152cb0eb486a71c1c816b364
locally_recorded_origin_main: 99f86ddf571a9906152cb0eb486a71c1c816b364
head_origin_aligned: true
expected_parent: b45dbf9a86c0d862709cfaf48d8fc6885d48a6cf
actual_parent: b45dbf9a86c0d862709cfaf48d8fc6885d48a6cf
parent_to_head_commit_count: 1
commit_message: "fix(cal002): enforce Batch05 review derivation integrity"
staged_files_before_audit: 0
tracked_modifications_before_audit: 0
sources_tracked_modifications: 0
sources_staged_modifications: 0
fetch_pull_merge_rebase_reset_clean_stash_amend: false
```

Transition result:

```yaml
modified_paths: 6
added_paths: 3
deleted_paths: 0
renamed_paths: 0
unexpected_paths: 0
total_changed_paths: 9
```

Modified:

- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json`
- `reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md`

Added:

- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py`
- `tests/test_cal002_batch05_review_derivation.py`
- `reports/CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_TARGETED_FIX_RESULT.md`

## 3. Critical artifact bindings

All expected worktree bytes equaled their current committed `HEAD` bytes.

| Artifact | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| Targeted-fix report | 13148 | `43e7d02af33f68ed255924651af8e6b83b1a06be6618ae4be6e1ec575ce2557c` | PASS |
| Blind schema | 18138 | `9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5` | PASS |
| Post-unblinding schema | 16213 | `7df7e1dca6cc702eb15c60c8178d9ebca5c77f47c3db2429bb5479ab3f4e4802` | PASS |
| Derivation tool | 31983 | `02902f29301da671ea9707c56b8a84ed6348cccf7f9e5390b4c7b161a2e09ef9` | PASS |
| Focused tests | 21717 | `92149ec42f5cf907c31e38f399be74e580062d05f139556bf4076bacf35aefb0` | PASS |
| Design evidence manifest | 4630 | `3159336dfe4de4a76b0417259522a5ee757ed97df25f54f64ed351c1bb3fab2b` | PASS |

The targeted-fix decision
`CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_APPLIED_READY_FOR_INDEPENDENT_AUDIT`
was present. It was treated as a claim, not as proof.

## 4. Evidence-manifest validation

```yaml
artifact_count: 11
included_artifact_count: 11
unique_bound_paths: 11
self_excluded: true
all_recorded_byte_lengths_match: true
all_recorded_sha256_values_match: true
all_worktree_bytes_equal_HEAD: true
```

The evidence manifest does not bind itself and records the recursive-hash
reason. No duplicate or missing bound path was found.

## 5. Immutable task, Prompt, and budget audit

Immutable design artifacts:

| Artifact | SHA-256 | Result |
| --- | --- | --- |
| Task matrix | `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32` | PASS |
| Variable locks | `5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a` | PASS |
| Treatment diff | `2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f` | PASS |
| Budget plan | `82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e` | PASS |

```yaml
task_count: 8
unique_task_ids: 8
unique_review_aliases: 8
experimental_cells: 4
tasks_per_cell: 2
automatic_task_expansion: false
tie_breaker_created: false
tie_breaker_authorized: false
all_submit_query_download_retry_resubmit_batch_flags_false: true
final_master: false
locked: false
```

Prompt blueprints were independently reconstructed from the declared block
order, two-LF separators, UTF-8 encoding without BOM, and one final LF:

| Blueprint | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| PUSH_CONTROL | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | PASS |
| PUSH_CANDIDATE | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | PASS |
| IMPACT_CONTROL | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | PASS |
| IMPACT_CANDIDATE | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | PASS |

Shared-block hashes also passed:

- `SHARED_VISUAL_CONSTANT_BLOCK`: `0dfde4b0f6c8ee1bed94cda3d8e727d5352498524b03bbb0f4d9e15f6304acd9`
- `SHARED_SAFETY_AND_CAMERA_BLOCK`: `c51ad0c1788a1e923a9d7fa300b3e9b37fe282eee39cbc3c120c50e3febddbdc`
- `SHARED_COMPACT_NEGATIVE_BLOCK`: `5e675cf7e987e4a9acc31471650ad27666b6e215433c3e7ba4cf95089697945e`

## 6. Static source-code findings

Passes:

- CLI exposes only `derive` and `verify`.
- Strict JSON rejects duplicate keys, UTF-8 BOM, invalid UTF-8, NaN,
  Infinity, and noncanonical bytes.
- Canonical JSON is UTF-8, sorted-key, two-space indentation, no NaN, and one
  final LF.
- Blind and post-unblinding records are validated with Draft 2020-12.
- Output uses same-directory temporary creation, file flush and `fsync`,
  explicit no-overwrite behavior, atomic link/replace, cleanup, and parent
  directory sync where supported.
- `verify` reparses the supplied canonical record and byte-compares it with a
  fresh deterministic derivation.
- Mapping files are compared with `HEAD`, independently hashed, and
  cross-validated against exact hard-coded alias/task/family/treatment/
  replicate expectations.
- Pair and family iteration use fixed tuples; no filesystem enumeration,
  current time, locale, timezone, randomness, or environment-controlled
  decision input was found.

Forbidden dependency/call scan:

```yaml
network_or_http_clients: none
Dreamina_or_provider_calls: none
shell_true: false
eval_exec_pickle: none
dynamic_import: none
environment_reads: none
time_or_random_reads: none
filesystem_walk_glob_rglob: none
Git_write_commands: none
subprocess_calls: 1
```

The only tool subprocess is argument-list-based:

```text
git show HEAD:<fixed relative path>
```

It does not use a shell and is read-only.

Findings:

- **Material:** lines 713-720 bind the fixed repository tool path, not the
  executing `__file__`.
- **Material:** lines 208-216 load schemas directly from worktree bytes without
  a `HEAD` comparison or output binding.
- **Nonblocking:** malformed Unicode surrogate input can fail closed through an
  uncaught encoding exception rather than the normalized `DerivationError`
  receipt path. No output is produced, but error normalization could be
  improved separately.

## 7. Tool self-binding result

Normal-path checks passed:

```yaml
worktree_tool_equals_HEAD: true
normal_recorded_tool_hash_matches_repository_tool: true
one_byte_dirty_expected_repository_path_rejected: true
manually_substituted_tool_hash_rejected: true
manually_substituted_tool_path_rejected: true
manually_substituted_tool_version_rejected: true
```

Independent copied-runner probe:

```yaml
executing_copy_path_different: true
executing_copy_byte_differences: 1
executing_copy_sha256: 3b23ceb4272c2c92e3a8b6c12b9bd7829218da41eeeed7f7800423f0f49b68e4
repository_tool_sha256: 02902f29301da671ea9707c56b8a84ed6348cccf7f9e5390b4c7b161a2e09ef9
derive_exit_code: 0
verify_exit_code: 0
recorded_sha256: 02902f29301da671ea9707c56b8a84ed6348cccf7f9e5390b4c7b161a2e09ef9
recorded_hash_matches_executing_copy: false
result: FAIL
```

This is stronger than merely recording a modified self-hash: an uncommitted
external runner can execute while the output falsely records the clean
repository tool identity.

Hidden-schema probe:

```yaml
blind_schema_worktree_differs_from_HEAD: true
dirty_schema_allowed_candidate_specific_top_level_field: true
derive_exit_code: 0
derived_record_created: true
schema_binding_present_in_derived_record: false
result: FAIL
```

## 8. Blind-schema independent probes

The schema declares JSON Schema Draft 2020-12 and passed independent
`check_schema`.

```yaml
independent_positive_records_passed: 1/1
independent_negative_records_rejected: 14/14
exact_alias_coverage: PASS
exact_alias_order: PASS
exact_pair_coverage: PASS
exact_pair_order: PASS
validity_preference_consistency: PASS
rationale_required_and_nonempty: PASS
candidate_specific_field_rejected_by_committed_schema: PASS
```

The 14 rejected cases covered duplicate/omitted/repeated/reordered aliases,
wrong alias family, duplicate/omitted/repeated/reordered pairs, four invalid
validity/preference combinations, missing rationale, empty rationale, and a
Candidate-specific field.

## 9. Strict-input probes

All 12 independent CLI probes exited nonzero and created no derived output:

1. UTF-8 BOM.
2. Duplicate JSON key.
3. NaN.
4. Infinity.
5. Invalid UTF-8.
6. Missing terminal LF.
7. More than one terminal LF.
8. Unsorted keys.
9. Non-two-space indentation.
10. Trailing whitespace.
11. Unknown top-level property.
12. Wrong blind schema version.

```yaml
strict_input_rejections: 12/12
partial_outputs: 0
```

## 10. Independent derive/verify round trip

Exact isolated commands:

```text
C:\Users\msjpurf\AppData\Local\Programs\Python\Python310\python.exe C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo\experiments\CAL-002\ACTION_CALIBRATION_V1\BATCH05_DESIGN\tools\batch05_review_derivation.py derive --repo-root C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo --blind-record C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo\audit\blind.json --output C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo\audit\derived1.json

C:\Users\msjpurf\AppData\Local\Programs\Python\Python310\python.exe C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo\experiments\CAL-002\ACTION_CALIBRATION_V1\BATCH05_DESIGN\tools\batch05_review_derivation.py verify --repo-root C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo --blind-record C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo\audit\blind.json --derived-record C:\Users\msjpurf\AppData\Local\Temp\cal002_b05_audit_z18na7je\repo\audit\derived1.json
```

Results:

```yaml
first_derive_exit_code: 0
verify_exit_code: 0
second_derive_exit_code: 0
derived_schema_valid: true
first_sha256: 40527a6bb26b93858159e0a28557b459818d1f3af2d90952dcb76b0ab6e0ebac
second_sha256: 40527a6bb26b93858159e0a28557b459818d1f3af2d90952dcb76b0ab6e0ebac
repeated_bytes_identical: true
derive_without_overwrite_exit_code: 1
existing_output_preserved: true
derive_with_overwrite_exit_code: 0
overwrite_bytes_identical: true
verify_wrote_files: false
```

## 11. Mapping mutation probes

Current mapping:

```yaml
manifest_aliases: 8
unique_manifest_aliases: 8
manifest_task_ids: 8
unique_manifest_task_ids: 8
task_matrix_rows: 8
unique_matrix_aliases: 8
unique_matrix_task_ids: 8
alias_order_exact: true
manifest_matrix_cross_binding_exact: true
counterbalanced_candidate_control_placement: true
```

All 12 isolated negative probes failed derive or verify:

```yaml
dirty_manifest_worktree_byte: rejected
dirty_task_matrix_worktree_byte: rejected
arbitrary_mapping_sha: rejected
arbitrary_mapping_byte_length: rejected
treatment_disagreement: rejected
family_disagreement: rejected
replicate_disagreement: rejected
duplicate_alias: rejected
duplicate_task_id: rejected
missing_task: rejected
extra_task: rejected
incorrect_candidate_control_pair_placement: rejected
mapping_negative_probes: 12/12
```

## 12. Pair truth-table probes

All nine independently specified valid branches returned the expected class and
Candidate-advantage boolean:

```yaml
candidate_A_A_better: PASS
candidate_B_B_better: PASS
control_B_B_better: PASS
control_A_A_better: PASS
valid_no_difference: PASS
invalid_uncontrolled_not_comparable: PASS
invalid_technical_not_comparable: PASS
inconclusive_no_difference: PASS
inconclusive_not_comparable: PASS
pair_truth_table: 9/9
```

All 10 contradictory records were rejected by schema validation or exact
deterministic re-derivation:

```yaml
pair_contradiction_probes: 10/10
```

The cases included both Candidate-side orientations, Control-preferred but
Candidate-advantage claims, invalid and inconclusive advantage claims,
Candidate-preferred but Control-class claims, no-difference advantage claims,
and invalid comparisons carrying a clear A/B preference.

## 13. Blind substitution probes

All eight substitutions failed verify:

```yaml
preference_changed_old_sha: rejected
validity_changed_old_sha: rejected
bytes_changed_only_length_updated: rejected
bytes_changed_sha_updated_pairs_stale: rejected
pairs_updated_family_stale: rejected
different_valid_record_same_path: rejected
one_byte_derived_output_mutation: rejected
copied_blind_values_replaced_in_derived: rejected
blind_substitution_probes: 8/8
```

## 14. Five family-result fixtures

Five independently constructed blind records each derived and verified
successfully for both action families:

| Fixture | Candidate pass | Control pass | Valid pairs | Candidate advantage | Control advantage | No clear advantage | Result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Positive | 2 | 0 | 2 | 2 | 0 | 0 | `FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL` |
| Both successful | 2 | 2 | 2 | 0 | 0 | 2 | `BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE` |
| Inconclusive | 1 | 1 | 2 | 0 | 0 | 2 | `INCONCLUSIVE_REPLICATION` |
| Regression | 0 | 2 | 2 | 0 | 2 | 0 | `CANDIDATE_FAMILY_COMPILER_REGRESSION` |
| Route reset | 0 | 0 | 2 | 0 | 0 | 2 | `ROUTE_RESET_REQUIRED` |

```yaml
family_fixture_count: 5
family_fixtures_derived: 5/5
family_fixtures_verified: 5/5
decision_precedence_verified: true
```

The observed precedence was Rule 1 route reset, Rule 2 regression, Rule 3
replicated positive, Rule 4 both successful/no advantage, and Rule 5
inconclusive.

## 15. Contradictory family mutations

All 14 required mutations failed verify:

```yaml
positive_candidate_pass_count_0: rejected
positive_candidate_pass_count_1: rejected
positive_valid_pair_count_1: rejected
positive_candidate_advantage_count_1: rejected
both_success_one_treatment_not_2_of_2: rejected
both_success_with_clear_advantage: rejected
positive_relabelled_regression: rejected
positive_relabelled_route_reset: rejected
positive_relabelled_inconclusive: rejected
family_summaries_reordered: rejected
computed_mismatch_count_changed: rejected
candidate_worse_than_control_changed: rejected
both_treatments_frequently_fail_changed: rejected
uncontrolled_variation_prevents_comparison_changed: rejected
family_contradiction_probes: 14/14
```

## 16. Focused-test review and results

Exact command:

```text
pytest -q tests/test_cal002_batch05_review_derivation.py
```

```yaml
collected: 59
passed: 59
failed: 0
skipped: 0
xfailed: 0
warnings: 0
```

Test-quality audit:

- No skip, xfail, or monkeypatch bypass was found.
- Tests use isolated temporary Git repositories and do not depend on project
  output artifacts.
- Hard-coded pair and family expectations exist, so the core assertions are
  not wholly tautological.
- Some JSON fixture serialization uses the implementation's own
  `canonical_json_bytes`; independent raw-byte probes in this audit compensate.
- The test module loads current worktree tool bytes and does not independently
  require that the executing module is the committed path.
- Ten parameterized pair-contradiction rows contain only eight unique
  dictionaries.
- The focused suite does not probe an external one-byte-modified runner or
  dirty schema provenance. Those omissions explain why 59/59 can coexist with
  the two material audit findings.

The suite result is necessary evidence but is not sufficient for READY.

## 17. No-hidden-write and no-live audit

```yaml
Dreamina_called: false
provider_called: false
provider_command_count: 0
submit_called: false
query_called: false
download_called: false
retry_or_resubmit_called: false
Prompt_package_created: false
execution_package_created: false
authorization_text_created: false
media_created: false
review_artifacts_created: false
sources_changed: false
tracked_project_files_changed_by_probes: false
staged_project_files_created_by_probes: false
project_Git_write_commands_during_probes: false
temporary_fixtures_outside_project: true
temporary_fixtures_cleaned: true
```

Temporary fixture setup used temporary Git repositories under the local system
temporary directory. Those directories were outside the project and were
deleted after each probe group. The derivation tool itself executed only the
read-only `git show` subprocess. Existing unrelated untracked workspace noise
was left untouched.

## 18. Exact next phase

```text
CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_IMPLEMENTATION_TARGETED_FIX_NO_LIVE
```

The targeted fix should, at minimum:

1. Require the executing file bytes and resolved executing path to equal the
   committed `HEAD:<tool path>` bytes and path before derive or verify.
2. Require both schema worktree files to equal their committed `HEAD` blobs and
   bind their byte lengths and SHA-256 values into the derived record, with the
   post schema updated accordingly.
3. Add independent regression tests for a one-byte-modified external runner,
   a different executing path, and dirty blind/post schemas.

No execution package, provider authority, or live permission is created by this
audit.

```yaml
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```
