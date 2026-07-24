# CAL-002 Batch05 Review Derivation Implementation Provenance Fix Independent No-Live Audit

## 1. Executive Decision

```yaml
phase: CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_INDEPENDENT_NO_LIVE_AUDIT
goal_identity: CAL002_BATCH05_IMPLEMENTATION_PROVENANCE_FIX_INDEPENDENT_NO_LIVE_AUDIT_V0_1
decision: CAL002_BATCH05_IMPLEMENTATION_PROVENANCE_FIX_READY_FOR_EXECUTION_PACKAGE_BUILD_NO_LIVE
specific_verdict: READY
experimental_redesign_required: false
implementation_followup_fix_required: false
execution_package_created: false
live_authority_created: false
```

The committed V0.2 derivation tool enforces actual executing-path and
executing-byte provenance before record processing. Both review schemas are
verified byte-for-byte against their committed `HEAD` blobs before parsing,
and the deterministic record binds the tool and both schemas. Independent
black-box probes confirmed that external runners, dirty tool or schema inputs,
substituted provenance fields, stale records, and earlier record versions are
rejected.

No blocking or material implementation-integrity defect was found.

## 2. Checkpoint And Eight-Path Transition

```text
repository = G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE
branch = main
starting_HEAD = 1f543ccc312d44763e742e3e84a896e1badd3451
locally_recorded_origin/main = 1f543ccc312d44763e742e3e84a896e1badd3451
HEAD/origin_aligned = true
fix_commit_parent = e89475dbd2d053a940afd61b66e1c3f4adf0a19d
parent_to_HEAD_commit_count = 1
fix_commit_message = fix(cal002): bind Batch05 tool and schemas to HEAD
staged_paths_at_preflight = 0
tracked_modifications_at_preflight = 0
sources_tracked_or_staged_modifications = 0
```

The parent-to-HEAD transition contains exactly seven modified paths and one
added path. It has zero deletions, renames, or unexpected paths.

Modified:

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md`
2. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json`
3. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json`
4. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json`
5. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py`
6. `reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md`
7. `tests/test_cal002_batch05_review_derivation.py`

Added:

1. `reports/CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_RESULT.md`

The blind visual-review schema does not appear in the transition.

## 3. Implementation-Fix Report Binding

```text
path = reports/CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_RESULT.md
byte_length = 9938
sha256 = 40f4efaf9aa41e35df2f0dbd4f5f646efe99f36065c83d618fd339b44982bc99
recorded_decision = CAL002_BATCH05_IMPLEMENTATION_PROVENANCE_FIX_APPLIED_READY_FOR_INDEPENDENT_AUDIT
binding_result = PASS
```

The report was treated as a claim source only. Its claims were checked against
the committed source, schemas, tests, independent hashes, and isolated
black-box executions.

## 4. Critical Artifacts And Evidence Manifest

| Artifact | Bytes | SHA-256 | Worktree = HEAD |
|---|---:|---|---|
| `batch05_visual_review_schema.json` | 18138 | `9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5` | true |
| `batch05_post_unblinding_analysis_schema.json` | 18899 | `366a8dac88504626ec400317c116e20c319c70c693a29927fa1753fcb46f396a` | true |
| `tools/batch05_review_derivation.py` | 35997 | `1bff976a6e14c96184936e81db1baf8df4a2154526c1f8770ac4b45c63388321` | true |
| `tests/test_cal002_batch05_review_derivation.py` | 30952 | `6f82d104952044886cb47b73fbdd0004eff3000e6c2e0d5ccba6e36acefea408` | true |

Schema identities:

```text
blind_schema_id = CAL002_BATCH05_BLIND_VISUAL_REVIEW_SCHEMA_V0_3
blind_record_version = CAL002_BATCH05_BLIND_VISUAL_REVIEW_RECORD_V0_3
post_schema_id = CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_SCHEMA_V0_3
post_record_version = CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_3
```

The blind schema is byte-identical between the fix parent and current `HEAD`.
All six JSON files under the Batch05 design directory parse strictly,
serialize canonically with sorted keys, two-space indentation and one terminal
LF, and both schemas pass Draft 2020-12 schema checking.

The V0.4 evidence manifest binds exactly eleven unique non-self artifacts.
Every recorded byte length and SHA-256 matches both current worktree bytes and
the corresponding committed `HEAD` blob.

```yaml
artifact_count: 11
included_artifact_count: 11
unique_bound_paths: 11
self_excluded: true
binding_mismatches: 0
```

## 5. Immutable Task, Prompt, Provider, And Budget Audit

| Immutable artifact | SHA-256 | Result |
|---|---|---|
| `batch05_task_matrix.csv` | `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32` | PASS |
| `batch05_variable_lock_table.csv` | `5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a` | PASS |
| `batch05_treatment_diff_matrix.json` | `2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f` | PASS |
| `batch05_budget_and_authority_plan.json` | `82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e` | PASS |

```yaml
task_count: 8
unique_task_ids: 8
unique_review_aliases: 8
experimental_cells: 4
tasks_per_cell: 2
automatic_task_expansion: false
tie_breaker_created: false
tie_breaker_authorized: false
```

Independent Prompt reconstruction used the declared four-block order, two LF
bytes between blocks, UTF-8 without BOM, and exactly one final LF.

| Blueprint | Bytes | SHA-256 | Result |
|---|---:|---|---|
| PUSH_CONTROL | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | PASS |
| PUSH_CANDIDATE | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | PASS |
| IMPACT_CONTROL | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | PASS |
| IMPACT_CANDIDATE | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | PASS |

Shared-block hashes also match:

```text
SHARED_VISUAL_CONSTANT_BLOCK = 0dfde4b0f6c8ee1bed94cda3d8e727d5352498524b03bbb0f4d9e15f6304acd9
SHARED_SAFETY_AND_CAMERA_BLOCK = c51ad0c1788a1e923a9d7fa300b3e9b37fe282eee39cbc3c120c50e3febddbdc
SHARED_COMPACT_NEGATIVE_BLOCK = 5e675cf7e987e4a9acc31471650ad27666b6e215433c3e7ba4cf95089697945e
```

The provider design target remains `seedance2.0_vip`, 5 seconds, 16:9, 720p,
with `text_only_no_active_generation_reference`. All submit, query, download,
retry, resubmit, batch, final, and lock fields remain false. Provider command
count remains zero.

## 6. Static Source-Code Audit

The complete V0.2 source was inspected. The effective order is:

```text
resolve --repo-root
resolve expected repository tool path
resolve actual Path(__file__)
compare resolved paths
read actual executing bytes
read expected worktree tool bytes
read HEAD tool blob
require three-way byte equality
bind tool version and actual executing bytes
verify blind schema worktree = HEAD, then parse and validate
verify post schema worktree = HEAD, then parse and validate
load blind record
verify design manifest and task matrix against HEAD
derive pairs and family decisions
validate post record
```

There is no fallback that reads the expected repository tool while allowing a
different file to execute. The actual executing path must first resolve to the
expected path, and the resulting binding is calculated from actual executing
bytes after three-way equality succeeds.

AST and literal scans found:

```yaml
network_or_HTTP_imports: 0
Dreamina_or_provider_references: 0
shell_true_calls: 0
eval_calls: 0
exec_calls: 0
pickle_calls: 0
dynamic_import_calls: 0
environment_controlled_decision_inputs: 0
current_time_or_randomness_inputs: 0
locale_or_timezone_inputs: 0
unbounded_directory_traversals: 0
Git_write_commands: 0
```

The only subprocess invocation in the derivation tool is:

```text
git show HEAD:<fixed-or-validated-repository-relative-path>
```

It uses an argument list, `shell=False` by default, bounded stdout/stderr
capture, and no Git write operation.

Explicit output writes occur only in CLI `derive`, after all provenance,
schema, blind-input, mapping, pair, family, and post-schema checks pass.
`verify` performs no output write.

## 7. Executing-Path And Executing-Byte Provenance Probes

All probes used independently created minimal Git repositories under the
system temporary directory. The canonical project was read-only.

Positive clean fixture:

```text
derive_exit = 0
verify_exit = 0
recorded_tool_path = expected repository-relative path
recorded_tool_version = CAL002_BATCH05_REVIEW_DERIVATION_TOOL_V0_2
recorded_tool_bytes = actual executing bytes
recorded_tool_sha256 = actual executing SHA-256
worktree_equals_HEAD = true
executing_file_equals_HEAD = true
```

Adversarial runner results:

| Probe | Derive | Verify | New output |
|---|---:|---:|---|
| Byte-identical external copy | 1 | 1 | false |
| One-byte-modified external copy | 1 | 1 | false |
| Different resolved path using an external hard link | 1 | 1 | false |
| Dirty expected repository tool | 1 | 1 | false |

Existing derived bytes remained unchanged after every failed verify. No
partial output remained after a failed derive.

The hard-link case exercises a different resolved path without requiring
privileged Windows symlink creation. A path alias that resolves to the exact
expected file is not an external copied runner; a copied or hard-linked file
whose resolved path differs is rejected.

## 8. Committed Alternative Tool Boundary

An isolated repository with a nonsemantic tool-byte modification committed at
the expected path was tested:

```text
alternative_repository_internal_derive = 0
alternative_repository_internal_verify = 0
alternative_tool_hash_differs = true
canonical_fixture_verify_of_alternative_record = 1
repository_checkpoint_field_in_record = false
```

This is the expected trust boundary. A different repository `HEAD` may prove
its own internal state, but its record binds a different tool hash and cannot
verify against the canonical tool, schemas, and mappings.

Nonblocking observation: the derived record does not contain a Git commit ID.
For this deterministic derivation layer, exact tool, schema, mapping, and blind
record byte bindings are sufficient to reject a different content state.
Future execution-package construction should still bind the repository
checkpoint as a separate authorization and package-level requirement. No
change to the derivation implementation is required by this observation.

## 9. Blind And Post Schema Provenance Probes

Clean schemas passed derive and verify. The output contains exactly two
`schema_source_bindings` in fixed order:

1. `batch05_visual_review_schema.json`
2. `batch05_post_unblinding_analysis_schema.json`

Each binding contains:

```text
relative_path
byte_length
sha256
schema_id
record_version
worktree_equals_HEAD = true
```

Dirty-schema results:

| Probe | Derive | Verify | New output | Existing record changed |
|---|---:|---:|---|---|
| Dirty blind schema | 1 | 1 | false | false |
| Dirty post schema | 1 | 1 | false | false |

Schema worktree/HEAD equality is checked before strict JSON parsing and before
Draft 2020-12 validation.

## 10. Schema-Binding Mutation Probes

Verify rejected all twelve independently mutated binding fields:

```text
blind relative_path
blind byte_length
blind sha256
blind schema_id
blind record_version
blind worktree_equals_HEAD
post relative_path
post byte_length
post sha256
post schema_id
post record_version
post worktree_equals_HEAD
```

A record with
`CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_2` was rejected.

The V0.3 post schema successfully validates a record that binds the post
schema's own committed bytes. This is nonrecursive: the binding is ordinary
content metadata derived from already verified schema bytes, not a hash
embedded in the schema file itself.

## 11. Independent Derive And Verify Round Trip

The exact command form used in the independently created clean fixture was:

```text
C:/Users/msjpurf/AppData/Local/Programs/Python/Python310/python.exe C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean/experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py derive --repo-root C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean --blind-record C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean/review/blind.json --output C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean/review/derived.json

C:/Users/msjpurf/AppData/Local/Programs/Python/Python310/python.exe C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean/experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py verify --repo-root C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean --blind-record C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean/review/blind.json --derived-record C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn/clean/review/derived.json
```

The command-bound temporary root
`C:/Users/msjpurf/AppData/Local/Temp/cal002-b05-independent-audit-p7mb0qjn`
was deleted after the probes.

```text
initial_derive_exit = 0
verify_exit = 0
second_identical_derive_exit = 0
derived_byte_length = 5787
derived_sha256 = 35edb9fad77484d5c8550ef59fbbd43c6a6d7665572841590af19726248a764b
repeated_output_byte_identical = true
repeated_output_sha256_identical = true
derive_without_overwrite_exit = 1
existing_output_unchanged_after_no_overwrite = true
derive_with_explicit_overwrite_exit = 0
explicit_overwrite_bytes_identical = true
verify_filesystem_write = false
post_schema_validation = PASS
```

## 12. Strict Input And Blind-Schema Regression

Twenty-three independent malformed or policy-invalid blind inputs were
rejected before output creation:

```text
UTF-8 BOM
duplicate JSON key
NaN
Infinity
invalid UTF-8
missing terminal LF
multiple terminal LFs
unsorted keys
four-space indentation
trailing whitespace
unknown top-level property
wrong blind schema version
duplicate alias
missing alias
reordered aliases
alias/action-family mismatch
duplicate pair ID
missing pair ID
reordered pair IDs
invalid validity/preference combination
missing rationale
empty rationale
Candidate-specific blind field
```

```yaml
strict_input_probe_count: 23
rejected: 23
outputs_created: 0
```

## 13. Mapping Provenance Regression

The design manifest and task matrix are read from fixed repository-relative
paths, compared byte-for-byte with their `HEAD` blobs, parsed only after the
comparison, and bound by path, byte length, and SHA-256.

Independent probes rejected:

```text
dirty design-manifest worktree bytes
dirty task-matrix worktree bytes
arbitrary manifest binding SHA-256
arbitrary manifest binding byte length
arbitrary task-matrix binding SHA-256
arbitrary task-matrix binding byte length
treatment disagreement
action-family disagreement
replicate disagreement
duplicate alias
duplicate task ID
missing task
extra task
incorrect Candidate/Control mapping placement
```

All committed semantic-defect fixtures failed derive without creating output.

## 14. Pair And Blind-Substitution Regression

Seven valid pair branches independently derived and verified:

| Input branch | Derived class |
|---|---|
| Valid Candidate preference | `CANDIDATE_CLEAR_ADVANTAGE` |
| Valid Control preference | `CONTROL_CLEAR_ADVANTAGE` |
| Valid no difference | `NO_CLEAR_ADVANTAGE` |
| Invalid uncontrolled variation | `INVALID_COMPARISON` |
| Invalid technical | `INVALID_COMPARISON` |
| Inconclusive with no difference | `INCONCLUSIVE_COMPARISON` |
| Inconclusive not comparable | `INCONCLUSIVE_COMPARISON` |

Verify rejected all independently forged conditions:

```text
Candidate-side contradiction
Control preference labelled Candidate advantage
invalid comparison labelled advantage
inconclusive comparison labelled advantage
no-difference comparison labelled advantage
changed blind preference with stale derived bytes
changed blind validity with stale derived bytes
changed blind bytes with otherwise unchanged semantics
changed pair derivation with stale family decision
changed family decision with stale pair derivation
one-byte derived-record mutation
```

The blind record's exact bytes, byte length, path, and SHA-256 participate in
deterministic re-derivation, so a semantically harmless blind-byte change still
invalidates the old record as required.

## 15. Five Family Results And Mutation Probes

Independent fixtures produced and verified all five family results:

| Fixture | Candidate pass | Control pass | Valid pairs | Candidate advantages | Result |
|---|---:|---:|---:|---:|---|
| Replicated positive | 2 | 2 | 2 | 2 | `FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL` |
| Both successful | 2 | 2 | 2 | 0 | `BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE` |
| Inconclusive | 1 | 1 | 2 | 0 | `INCONCLUSIVE_REPLICATION` |
| Candidate regression | 0 | 2 | 2 | 0 | `CANDIDATE_FAMILY_COMPILER_REGRESSION` |
| Route reset | 0 | 0 | 2 | 0 | `ROUTE_RESET_REQUIRED` |

The route-reset fixture set
`both_treatments_frequently_fail=true`. The regression fixture set
`candidate_worse_than_control=true`. The declared decision precedence fired
correctly in every fixture.

Verify rejected independent mutations to:

```text
family result
computed count
computed flag
decision rationale
family order
```

## 16. Focused Test Results And Test-Quality Review

Commands:

```text
pytest --collect-only -q tests/test_cal002_batch05_review_derivation.py
pytest -q tests/test_cal002_batch05_review_derivation.py
```

The audit disabled bytecode and pytest cache writes through environment
settings; it did not alter the test selection or test logic.

```yaml
collected: 80
passed: 80
failed: 0
skipped: 0
xfailed: 0
warnings: 0
```

Static test-quality findings:

```yaml
top_level_test_functions: 31
provenance_test_functions: 10
new_provenance_cases_after_parameterization: 21
isolated_temporary_repository_usage: true
real_external_runner_subprocess_coverage: true
dirty_blind_schema_derive_and_verify_coverage: true
dirty_post_schema_derive_and_verify_coverage: true
output_noncreation_assertions: true
exact_tool_and_schema_binding_assertions: true
actual_project_tool_or_schema_mutated_by_tests: false
skip_or_xfail_markers: 0
```

The tests assert intended failure reasons for external-path and dirty-input
cases instead of succeeding through incidental missing files or malformed
fixtures.

Nonblocking coverage note: the committed 21 cases do not separately enumerate
dirty-tool verify, modified-external-runner verify, schema path substitution,
or `worktree_equals_HEAD=false`. This independent audit executed each of those
cases successfully. The omission is not material because the relevant
implementation paths are shared, the independent black-box probes passed, and
the checked-in suite retains broad deterministic and schema validation
coverage.

## 17. No-Hidden-Write And No-Live Audit

Before report creation, project `git status --porcelain` exactly matched the
pre-audit baseline. No tracked or staged path changed during inspection,
focused tests, or black-box probes. Pre-existing unrelated untracked workspace
noise remained untouched.

Both independent temporary roots were removed:

```text
cal002-b05-independent-audit-p7mb0qjn = cleaned
cal002-b05-independent-logic-d6ouj4qr = cleaned
```

Temporary fixture setup used local Git writes only inside disposable system
temporary directories. The audited derivation tool itself invoked only
read-only `git show`. No project Git write occurred before the required audit
report phase.

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

## 18. Exact Next Phase

```text
CAL002_BATCH05_EXECUTION_PACKAGE_BUILD_NO_LIVE
```

This decision authorizes no provider operation and creates no execution
package or live authority. A separate fresh checkpoint and explicit task are
required for the next no-live package-build phase.
