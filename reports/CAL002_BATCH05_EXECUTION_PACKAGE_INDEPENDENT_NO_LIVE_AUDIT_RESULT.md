# CAL-002 Batch05 Execution Package Independent No-Live Audit Result

## 1. Executive Decision

```text
phase = CAL002_BATCH05_EXECUTION_PACKAGE_INDEPENDENT_NO_LIVE_AUDIT
goal_identity = CAL002_BATCH05_EXECUTION_PACKAGE_INDEPENDENT_NO_LIVE_AUDIT_V0_1
decision = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX
specific_verdict = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX_EXPLICIT_POLL_ZERO
ready_for_live_submit_authorization_decision = false
```

The committed package set is internally consistent in its Prompt bytes,
task mappings, provider parameters, no-live authority state, manifests, and
evidence bindings. It is not ready for a live-submit authorization decision
because the independent audit found three material contract gaps:

| Finding | Result | Required correction |
|---|---|---|
| Explicit poll-zero contract | NEEDS_FIX | Add explicit `--poll 0` to every package command plan, or provide both runtime proof of an omitted zero default and an explicit package omission/default contract. The current evidence satisfies neither alternative. |
| Committed package-checkpoint binding | NEEDS_FIX | Bind the package-build report or the committed package-build checkpoint `3de46cb5c12bba925b274dfcdc818f6b7f6bacdf` in the package index. |
| Strict replicate-difference allowlist | NEEDS_FIX | Resolve `phase1_order` as an extra R01/R02 package difference, either by removing it from package identity or by an explicitly authorized contract correction. |

No package was repaired or executed during this audit.

## 2. Checkpoint And Seventeen-Path Transition

```text
branch = main
starting_HEAD = 3de46cb5c12bba925b274dfcdc818f6b7f6bacdf
starting_origin/main = 3de46cb5c12bba925b274dfcdc818f6b7f6bacdf
HEAD_origin_aligned = true
package_build_parent = 2575d1a7a7ed7215d06d715c6603495c809d8005
parent_to_HEAD_commit_count = 1
package_build_subject = build(cal002): add Batch05 no-live execution packages
added_paths = 17
modified_paths = 0
deleted_paths = 0
renamed_or_other_paths = 0
unexpected_paths = 0
staged_paths_at_preflight = 0
tracked_modifications_at_preflight = 0
sources_modifications_at_preflight = 0
```

The package-build transition contains exactly four Prompt files, eight package
JSON files, one runtime preflight, one execution manifest, one package index,
one package-evidence manifest, and one package-build report. The
`BATCH05_EXECUTION/` tree contains exactly the expected sixteen files and no
run, execution-record, download, media, frame, review, script, or authorization
path.

## 3. Package-Build And Implementation-Audit Bindings

```text
package_build_report_path = reports/CAL002_BATCH05_EXECUTION_PACKAGE_BUILD_RESULT.md
package_build_report_bytes = 8009
package_build_report_sha256 = 7977185b9350ae621125e8af5cffae4942bb575c090dc5d952de01a1a040f692
package_build_report_decision = CAL002_BATCH05_EXECUTION_PACKAGE_BUILT_READY_FOR_INDEPENDENT_NO_LIVE_AUDIT
package_build_report_binding = PASS

implementation_audit_path = reports/CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
implementation_audit_bytes = 20684
implementation_audit_sha256 = b262c6ac1db837b2276632b909add688695aef408783312a274bfc1f7b98e95b
implementation_audit_decision = CAL002_BATCH05_IMPLEMENTATION_PROVENANCE_FIX_READY_FOR_EXECUTION_PACKAGE_BUILD_NO_LIVE
implementation_audit_binding = PASS

design_package_input_checkpoint = 2575d1a7a7ed7215d06d715c6603495c809d8005
committed_package_build_checkpoint = 3de46cb5c12bba925b274dfcdc818f6b7f6bacdf
```

These checkpoints are distinct. A later live authorization must bind the
committed package-build checkpoint, after the targeted fixes and a new
independent audit.

## 4. Runtime Preflight Comparison

The audit independently called exactly:

```text
C:/Users/msjpurf/bin/dreamina.exe version
C:/Users/msjpurf/bin/dreamina.exe text2video -h
```

Each command was called once. The current outputs matched the committed
runtime preflight byte-for-byte.

| Command stream | Exit | Bytes | SHA-256 | Committed comparison |
|---|---:|---:|---|---|
| `version` stdout | 0 | 96 | `25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0` | exact |
| `version` stderr | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | exact |
| `text2video -h` stdout | 0 | 1708 | `17e92789fc0633fa2563a3f3260865a955c08813d55deb681f4c7936ba2ecde4` | exact |
| `text2video -h` stderr | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | exact |

```text
runtime_preflight_path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/runtime_command_contract_preflight.json
runtime_preflight_bytes = 6658
runtime_preflight_sha256 = fedecf44d5b3da7f0d971cd178a4f960f469eef4be006bb8c0a01e0b9f83284b
runtime_preflight_binding = PASS
runtime_preflight_current_comparison = EXACT
```

## 5. Treatment Of `2a20fff-dirty`

```text
runtime_version = 2a20fff-dirty
runtime_commit = 2a20fff
runtime_build_time = 2026-06-26T06:36:39Z
installer_metadata_used_as_binary_version = false
```

The `-dirty` suffix is not treated as a defect in this package-layer audit.
The committed preflight accurately records the current binary response rather
than claiming installer metadata `v1.4.10` as the binary version.

The preflight does not bind the executable file SHA-256. That absence is
nonblocking at this no-live package layer only if every future live phase:

1. binds the corrected committed package checkpoint;
2. performs a fresh runtime canary against the fixed executable path; and
3. obtains separate human live authorization.

## 6. Current Command And Help Contract

The current help independently proves support for:

```yaml
command: text2video
prompt: true
model_version: seedance2.0_vip
duration: 5
duration_supported_range: 4-15
ratio: "16:9"
video_resolution: 720p
```

All provider flags currently used by the eight packages are accepted by the
runtime help. The fixed provider parameter set is therefore valid.

## 7. Poll-Zero And Session Behavior

Current help states:

```text
--poll int
submit then poll query_result for up to N seconds at 1s intervals
(0 disables polling)
```

It does not explicitly state that omitting `--poll` defaults to zero. All eight
package command plans omit `--poll`, and none records an omission/default
contract. Therefore neither permitted safety alternative is satisfied:

```text
explicit_--poll_0_in_all_packages = false
help_explicitly_proves_omitted_poll_defaults_to_0 = false
package_records_poll_omission_default_contract = false
poll_zero_contract = NEEDS_FIX
```

Current help explicitly records `--session int` with default `0`. All eight
packages omit `--session`, contain no session ID or session state, and do not
inject a nonzero session:

```text
session_default_zero_explicit_in_help = true
session_omitted_by_all_packages = true
active_session_state_present = false
session_contract = PASS
```

## 8. Four Prompt Bindings

All four Prompts were reconstructed independently from the committed design
manifest by joining the required four blocks with exactly two LF bytes and
adding one final LF.

| Cell | Bytes | SHA-256 | Reconstruction | Format |
|---|---:|---|---|---|
| PUSH_CONTROL | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | exact | PASS |
| PUSH_CANDIDATE | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | exact | PASS |
| IMPACT_CONTROL | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | exact | PASS |
| IMPACT_CANDIDATE | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | exact | PASS |

Each file is strict UTF-8 without BOM, LF-only, and has one terminal LF.
No Prompt contains a task ID, replicate ID, blind alias, review contract,
local output path, submit ID, query instruction, or download instruction.

## 9. Eight Package Mappings

| Task | Alias | Family | Treatment | Replicate | Prompt |
|---|---|---|---|---|---|
| CAL002-B05-PUSH-CONTROL-R01 | PUSH_PAIR_01_A | push_reaction | control | R01 | PUSH_CONTROL |
| CAL002-B05-PUSH-CONTROL-R02 | PUSH_PAIR_02_B | push_reaction | control | R02 | PUSH_CONTROL |
| CAL002-B05-PUSH-CANDIDATE-R01 | PUSH_PAIR_01_B | push_reaction | candidate | R01 | PUSH_CANDIDATE |
| CAL002-B05-PUSH-CANDIDATE-R02 | PUSH_PAIR_02_A | push_reaction | candidate | R02 | PUSH_CANDIDATE |
| CAL002-B05-IMPACT-CONTROL-R01 | IMPACT_PAIR_01_B | brief_impact_recoil | control | R01 | IMPACT_CONTROL |
| CAL002-B05-IMPACT-CONTROL-R02 | IMPACT_PAIR_02_A | brief_impact_recoil | control | R02 | IMPACT_CONTROL |
| CAL002-B05-IMPACT-CANDIDATE-R01 | IMPACT_PAIR_01_A | brief_impact_recoil | candidate | R01 | IMPACT_CANDIDATE |
| CAL002-B05-IMPACT-CANDIDATE-R02 | IMPACT_PAIR_02_B | brief_impact_recoil | candidate | R02 | IMPACT_CANDIDATE |

Every package matches the design manifest and task matrix for task identity,
alias, family, treatment, replicate, order, Prompt, provider fields, reference
strategy, and estimated credit. All eleven JSON artifacts under the package
set use strict deterministic serialization with sorted keys, two-space
indentation, and one final LF.

All eight packages explicitly retain:

```yaml
task_type: text2video
model_version: seedance2.0_vip
duration: 5
ratio: "16:9"
video_resolution: 720p
reference_strategy: text_only_no_active_generation_reference
active_generation_reference_count: 0
estimated_credit: 70
fresh_credit_checked: false
no_submit: true
```

All required authority and final-state fields are present and explicitly
false.

## 10. Deterministic Future Argv Rendering

The audit rendered eight inert argv arrays in memory without invoking any of
them. Hashes below are SHA-256 over compact UTF-8 JSON serialization of each
ordered argv array.

| Task | Elements | Argv SHA-256 |
|---|---:|---|
| CAL002-B05-PUSH-CONTROL-R01 | 12 | `b6a0c6b3de6ae985ccfa149f3a85888380bf20b141dd980d80c7497ac58d0895` |
| CAL002-B05-PUSH-CONTROL-R02 | 12 | `b6a0c6b3de6ae985ccfa149f3a85888380bf20b141dd980d80c7497ac58d0895` |
| CAL002-B05-PUSH-CANDIDATE-R01 | 12 | `800be0a0fa7b2c22c9e09d3b5817a67f8436d795e4e6c39855bfeecdf57844ff` |
| CAL002-B05-PUSH-CANDIDATE-R02 | 12 | `800be0a0fa7b2c22c9e09d3b5817a67f8436d795e4e6c39855bfeecdf57844ff` |
| CAL002-B05-IMPACT-CONTROL-R01 | 12 | `391ecfcd82d59a77bab022382667aa42a927370e1c04104073b11b3efc75e59a` |
| CAL002-B05-IMPACT-CONTROL-R02 | 12 | `391ecfcd82d59a77bab022382667aa42a927370e1c04104073b11b3efc75e59a` |
| CAL002-B05-IMPACT-CANDIDATE-R01 | 12 | `3c5808e44e9b949d7871864a0b180a34b224b128df5bf0899690f2dff496f6cb` |
| CAL002-B05-IMPACT-CANDIDATE-R02 | 12 | `3c5808e44e9b949d7871864a0b180a34b224b128df5bf0899690f2dff496f6cb` |

The declared stable flag order is:

```text
--model_version
--ratio
--duration
--video_resolution
--prompt
```

The Prompt is loaded as exact UTF-8 text and occupies one argv element.
No Prompt path, task ID, blind alias, output path, output name, output
directory, download directory, submit ID, session ID, authorization token, or
retry field enters argv. The plan is structured data, not a shell command, and
`shell_script=false`.

```text
rendered_argv_count = 8
rendered_argv_shape_except_poll = PASS
rendered_argv_overall_safety = NEEDS_FIX_EXPLICIT_POLL_ZERO
argv_invoked = false
```

## 11. Output-Bookkeeping Separation

Every package keeps `planned_local_output_root` and `planned_output_name` as
bookkeeping fields only.

```text
output_directory_is_submit_argument = false
output_name_is_submit_argument = false
unique_planned_output_names = 8
all_output_names_derived_from_task_ids = true
--output_dir_present = false
--output_name_present = false
--download_dir_present = false
output_bookkeeping_isolated = PASS
```

## 12. Replicate Identity Checks

Within all four cells, R01 and R02 have identical Prompt path, Prompt SHA,
Prompt bytes, provider parameters, reference strategy, command plan, credit
estimate, and authority state. Their rendered argv hashes are identical.

The top-level differing keys in every pair are:

```text
blind_alias
package_id
phase1_order
planned_output_name
replicate
task_id
```

The audit contract permits only:

```text
blind_alias
package_id
planned_output_name
replicate
task_id
```

`phase1_order` is consistent with the task matrix and does not alter provider
argv, but it is an additional package-level difference outside the strict
allowlist. It must be resolved in the targeted no-live fix rather than silently
accepted by this audit.

```text
replicate_Prompt_identity = PASS
replicate_provider_identity = PASS
replicate_command_plan_identity = PASS
replicate_strict_allowed_difference_set = NEEDS_FIX
```

## 13. Execution-Manifest Audit

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_execution_manifest.csv
byte_length = 4804
sha256 = 0aa486cdac6d96a48c2077919e0a17ab26798527d1c4b68f554a2ec51efe581d
row_count = 8
unique_task_ids = 8
unique_aliases = 8
unique_package_paths = 8
unique_output_names = 8
cell_count = 4
replicates_per_cell = 2
estimated_credit_total = 560
all_authority_and_final_fields_false = true
package_cross_check = PASS
execution_manifest_validation = PASS
```

The CSV is UTF-8 without BOM, LF-only, and has exactly one final LF.

## 14. Package-Index Audit

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_package_index.json
byte_length = 9187
sha256 = e2164ca62606d9d8a9908e98e6b27d6da8f78e67926dead86f29b1ec64a02b61
fixed_task_count = 8
canonical_prompt_count = 4
package_count = 8
estimated_total_credits = 560
fresh_credit_checked = false
automatic_task_expansion = false
tie_breaker_created = false
package_build_checkpoint_is_not_live_authority = true
future_live_authorization_must_bind_the_committed_package_checkpoint = true
core_bindings = PASS
```

The index correctly binds the design checkpoint, implementation audit, design
manifest, task matrix, runtime preflight, four Prompts, eight packages, and
execution manifest. However, it contains neither:

```text
committed_package_build_checkpoint = 3de46cb5c12bba925b274dfcdc818f6b7f6bacdf
```

nor an explicit package-build report binding. Its generic future-binding
boolean is insufficient under this audit contract.

```text
package_index_core_validation = PASS
package_checkpoint_binding_rule = NEEDS_FIX
```

## 15. Evidence-Manifest Audit

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_package_evidence_manifest.json
byte_length = 6482
sha256 = bbfd75f0be4b31c01c70e51f1c010154b865c3f6d0dc66ba849810fef8e4e825
artifact_count = 16
included_artifact_count = 16
unique_bound_paths = 16
self_excluded = true
```

All sixteen non-self paths, byte lengths, SHA-256 values, artifact classes, and
creation phases match both worktree and committed `HEAD` bytes. Recursive
self-exclusion is explicit and correct.

```text
evidence_manifest_validation = PASS
```

## 16. Prohibited-Content Scan

The exact seventeen package-build artifacts contain no active:

```text
submit_id
result_url
signed URL
download URL
cookie
authorization token
session secret or session ID
login state
account balance
current credit balance
retry, resubmit, or batch authority
production, completion, final, or lock state
```

Field names and no-live statements were distinguished from active values.
There are no executable shell commands, PowerShell scripts, batch files, shell
scripts, submit loops, query loops, download loops, or retry loops.

```text
sensitive_state_present = false
live_authority_present = false
prohibited_content_scan = PASS
```

## 17. Credit And Authority Audit

```yaml
estimated_unit_credits: 70
estimated_total_credits: 560
fresh_credit_checked: false
current_credit_balance_claimed: false

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

No `user_credit` command was called. The 560-credit value remains a historical
planning estimate and this audit creates no spending authority.

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
tracked_package_files_changed_by_probes = false
protected_preexisting_files_changed = false
temporary_audit_files_created = false
temporary_audit_files_cleaned = true
```

The package-build commit changes exactly the expected seventeen paths.
All pre-existing paths outside that transition remain represented by the
unchanged parent tree, the audit probes left the tracked worktree and index
clean, and `git status --short -- sources/` remained empty before report
creation.

## 19. Final Verdict And Next Phase

```text
decision = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX
specific_verdict = CAL002_BATCH05_EXECUTION_PACKAGE_NEEDS_FIX_EXPLICIT_POLL_ZERO
next_phase = CAL002_BATCH05_EXECUTION_PACKAGE_TARGETED_FIX_NO_LIVE
```

The targeted fix must remain no-live and must address all three material
findings before another independent no-live package audit. No live-submit
authorization decision is permitted from this checkpoint.
