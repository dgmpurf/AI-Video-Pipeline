# CAL-001 Authorization Serialization Compiler Strict Validation Independent No-Live Audit

## 1. Audit Decision

- phase_id: `CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_STRICT_VALIDATION_INDEPENDENT_NO_LIVE_AUDIT`
- audit_type: independent no-live audit
- required_starting_head: `6fb5a38a04707a1bff0af0cf9034a8d5be00d072`
- starting_local_HEAD: `6fb5a38a04707a1bff0af0cf9034a8d5be00d072`
- starting_origin_main: `6fb5a38a04707a1bff0af0cf9034a8d5be00d072`
- starting_HEAD_origin_aligned: `true`
- status: `COMPLETE`
- decision: `ready`
- blocking_findings: `0`
- material_contract_defects: `0`

Final audit conclusion: the strict-validation repair closes the previously reported type-confusion, malformed-container, blocking-error gating, and hexadecimal consistency defects. No remaining fail-open, recognized-input bypass, ambiguous activation path, or provider-operation side effect was found.

This audit does not authorize Dreamina, a provider call, F07, Source modification, final status, or lock status. The next action is human reconciliation of the local `sources/` mirror before any F07 preflight.

## 2. Independence And Method

The repair receipt, repair report, and newly added tests were treated as audit targets rather than proof. The audit independently:

1. inspected the implementation and CLI control flow;
2. enumerated the semantic contract from an independently written 25-group specification;
3. generated direct library probes without importing test helpers;
4. generated separate CLI subprocess probes in automatically removed temporary directories;
5. derived historical canonical bytes and digests with Python standard-library `json`, `hashlib`, `base64`, and `re`;
6. reran the required committed tests only after the independent probes;
7. verified protected state and hashes before creating this report.

No probe file remains. The one temporary worktree used for parent-checkpoint comparison was removed before this report was created.

## 3. Repository And Source Preflight

- repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- branch: `main`
- `git fetch origin`: succeeded
- local HEAD: required checkpoint
- `origin/main`: required checkpoint
- staged files before audit: none
- unrelated tracked changes: none outside the authorized informational Source status

Exact human-managed Source-mirror status, recorded and left untouched:

```text
 D sources/AI视频制作_Source索引与使用优先级_V1.11.md
?? sources/AI视频制作_Source索引与使用优先级_V1.12.md
?? sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md
```

- known_human_source_mirror_changes_present: `true`
- unexpected_source_changes_present: `false`
- sources_touched: `false`
- sources_staged: `false`

## 4. Exact Repair Diff Audit

Audited base and head:

```yaml
base: 028fc89d0c2c7596f445356621f048fa4a8afbc7
head: 6fb5a38a04707a1bff0af0cf9034a8d5be00d072
```

The commit contains exactly:

- modified `app/ai_video_pipeline/governance/authorization_serialization.py`;
- modified `tests/test_authorization_serialization.py`;
- modified `tests/test_authorization_compiler_cli.py`;
- added the bounded strict-validation repair report.

`tools/authorization_compiler.py` and `app/ai_video_pipeline/governance/__init__.py` are byte-identical between base and head. No additional implementation path changed.

Independent source review confirmed:

- every recognized fact group participates in an explicit exact-type map;
- import-time set equality prevents an untyped recognized group;
- every occurrence is validated before selected-value comparison;
- every present recognized container is shape-checked;
- all validation errors feed one blocking list;
- evidence verification requires that list to be empty;
- valid hexadecimal strings alone receive case-insensitive comparison;
- exact-byte and activation boundaries remain separate.

The repair report's material claims matched the independent evidence below.

## 5. Exhaustive Semantic Type Contract

Independent enumeration found exactly 25 semantic groups and 34 unique aliases.

| Group | Aliases | Exact type |
| --- | --- | --- |
| `byte_length` | `byte_length`, `authorization_byte_length` | integer, not boolean |
| `sha256` | `sha256`, `authorization_text_sha256` | string |
| `base64` | `base64`, `authorization_base64`, `locally_derived_base64`, `locally_generated_base64` | string |
| `base64_character_count` | `base64_character_count`, `derived_base64_character_count` | integer, not boolean |
| `canonical_text` | `canonical_authorization_text`, `exact_authorization_text` | string |
| `authority_source` | `authority_source` | string |
| `encoding` | `encoding` | string |
| `utf8_decode_valid` | `utf8_decode_valid` | boolean |
| `bom_present` | `bom`, `bom_present` | boolean |
| `cr_present` | `cr_present` | boolean |
| `lf_present` | `lf_present` | boolean |
| `trailing_carriage_return` | `trailing_carriage_return` | boolean |
| `trailing_newline` | `trailing_newline` | boolean |
| `trailing_space` | `trailing_space` | boolean |
| `markdown_fence_present` | `markdown_fence_present` | boolean |
| `last_character` | `last_character` | string |
| `last_byte_hex` | `last_byte_hex` | string |
| `base64_decode_count` | `base64_decode_count`, `locally_generated_base64_decode_count` | integer, not boolean |
| `decoded_bytes_equal_original` | `decoded_bytes_equal_original` | boolean |
| `base64_round_trip_verified` | `base64_round_trip_verified` | boolean |
| `decoded_sha256_equal_original` | `decoded_sha256_equal_original` | boolean |
| `byte_profile_valid` | `byte_profile_valid` | boolean |
| `serialization_round_trip_verified` | `serialization_round_trip_verified` | boolean |
| `decoded_sha256` | `decoded_sha256` | string |
| `authorization_verified` | `authorization_verified` | boolean |

Contract audit results:

```yaml
recognized_semantic_groups: 25
recognized_aliases: 34
boolean_aliases: 15
integer_aliases: 6
string_aliases: 13
every_group_has_exactly_one_type: true
every_alias_reaches_type_validation: true
every_validation_alias_reaches_conflict_enumeration: true
every_conflict_alias_reaches_semantic_validation: true
new_group_without_type_fails_deterministically: true
valid_exact_type_alias_cases_passed: 34
```

An in-memory source mutation added a recognized group without adding a type. Module execution stopped deterministically with `every recognized authorization fact requires an exact type`; no repository file was changed.

## 6. Boolean And Integer Confusion Audit

Every boolean alias was supplied as integer `0` and integer `1`. Every integer alias was supplied as JSON `false` and JSON `true`.

| Probe family | Cases | Result |
| --- | ---: | --- |
| boolean alias, single malformed occurrence | 30 | all rejected |
| boolean alias, two equal malformed occurrences | 30 | all rejected |
| boolean alias, valid selected occurrence plus malformed secondary | 30 | all rejected |
| integer alias, single malformed occurrence | 12 | all rejected |
| integer alias, two equal malformed occurrences | 12 | all rejected |
| integer alias, valid selected occurrence plus malformed secondary | 12 | all rejected |
| wrong-type CLI records across boolean/integer/string aliases | 55 | all exited nonzero |

Every rejected result retained false evidence, false authorization, false eligibility, false execution/provider authority, and zero provider/authorized-operation counters.

Static review found no remaining loose-equality bypass: integer coercion explicitly excludes boolean, duplicate comparison requires identical Python types, fact comparison uses that type-sensitive comparator, and all occurrences are validated before evidence can verify.

## 7. String Type Audit

All 13 string aliases were independently supplied with each of:

- array;
- object;
- integer;
- boolean;
- null.

All 65 cases emitted deterministic invalid-type evidence and failed closed. A separate CLI null probe for every string alias also exited nonzero. No recognized string currently permits null.

## 8. Recognized Container Shape Audit

Each of the following paths was supplied as string, array, number, boolean, and null:

- `canonical_serialization`;
- `canonical_authorization`;
- `canonical_serialization.verification`;
- `canonical_authorization.verification`.

Results:

```yaml
invalid_shape_cases: 20
deterministic_shape_errors: 20
library_fail_closed: 20
verify_record_cli_nonzero: 20
evidence_verified_in_any_case: false
eligibility_in_any_case: false
provider_or_execution_authority_in_any_case: false
nonzero_counter_in_any_case: false
```

Absent optional containers and valid object containers remained compatible. Valid top-level length/SHA evidence did not hide a malformed recognized container, and malformed nested verification containers were not ignored.

## 9. Blocking Validation-Error Gating

Independent probes covered 13 blocking families:

1. Base64 character count without Base64;
2. missing byte length;
3. invalid byte-length type;
4. missing SHA-256;
5. malformed SHA-256;
6. malformed Base64;
7. invalid canonical-text type;
8. invalid `authority_source`;
9. invalid `encoding`;
10. invalid profile boolean;
11. invalid recognized-container shape;
12. representation conflict;
13. hexadecimal syntax failure.

All 13 failed closed in the library and all 13 exited nonzero through `verify-record`. The direct `verify` CLI also exited nonzero for every error class representable by that command: byte-length mismatch, SHA mismatch, and malformed/mismatched Base64.

The implementation computes `authorization_evidence_verified` only after all current validation checks and requires `not errors`. No current validation error is informational; all are intentionally blocking. No tested blocking error coexisted with verified evidence or authorization.

The Base64-count-without-Base64 result specifically retained:

```yaml
expected_base64_missing: true
authorization_evidence_verified: false
authorization_verified: false
eligible_for_authority_activation: false
execution_authority_active: false
provider_command_allowed: false
provider_command_invocation_count: 0
authorized_operation_count_consumed: 0
verify_record_cli_exit_nonzero: true
```

## 10. Hexadecimal Audit

Seven valid case probes passed:

- lowercase, uppercase, and mixed-case SHA-256;
- lowercase and uppercase matching `decoded_sha256`;
- `last_byte_hex=2E` and `last_byte_hex=2e`.

Twenty-four invalid probes covered nonhex, truncated, overlong, whitespace-padded, `0x`-prefixed, empty, integer, and boolean values across SHA-256, decoded SHA-256, and last-byte hexadecimal facts. All were rejected before case normalization.

Unrelated string facts remained case-sensitive in five independent probes covering `authority_source`, `encoding`, canonical text, Base64, and `last_character`.

## 11. Previous Security Repairs

All prior closures independently remained fail-closed:

- conflicting Base64 aliases;
- conflicting locally-derived/generated Base64 aliases;
- nested/top-level byte-length conflict;
- nested/top-level SHA conflict;
- canonical-text alias conflict;
- conflicting boolean/profile duplicates;
- malformed secondary occurrence;
- same-length mutation;
- BOM;
- CR;
- LF;
- trailing space;
- Markdown fence;
- invalid UTF-8;
- historical R1 mismatched Base64.

Fourteen fresh nonhistorical probes covered seven representation/occurrence conflicts, one same-length mutation, and six exact-byte profile failures. Every path retained zero counters and no authority activation.

## 12. Activation Boundary

| Inputs | Evidence verified | Checkpoint verified | Eligible | Execution active | Provider allowed |
| --- | --- | --- | --- | --- | --- |
| compile only | false | absent | false | false | false |
| compile result plus valid checkpoint | false | true | false | false | false |
| verified evidence without checkpoint | true | absent | false | false | false |
| checkpoint verification alone | absent | true | false | false | false |
| verified evidence plus invalid checkpoint | true | false | false | false | false |
| verified noncontradictory evidence plus valid checkpoint | true | true | true | false | false |

All combinations retained `provider_command_invocation_count=0` and `authorized_operation_count_consumed=0`. The final combination establishes eligibility only and does not activate execution authority.

Compile-only `safe_block` remains a clear, non-blocking naming deviation.

## 13. Historical Fixture Independence

Canonical bytes and SHA-256 values were derived with Python standard-library code before invoking the repaired verifier.

| Fixture | Bytes | Independently derived SHA-256 | Strict verifier |
| --- | ---: | --- | --- |
| F06 recovery query R2 | 432 | `0f4306d42084ab96044eea5a89d338e0cf1e41c31e39d8df85b25a15626fe883` | pass |
| F06 recovery download | 607 | `e56a37cc5e7f17aaa691ec4e5862fa9253e1a0273221523f9b2a2c172601ff4a` | pass |
| F06 review-artifact authorization | 583 | `472da91ce12a778f6505844fb52e80a86dd2c1e11cafd469c344cfe08d4df1a1` | pass |
| F06 visual-review authorization | 1036 | `e50c231685d549167eeb71ce229e3f61e17ad392da1fc1468aa41d9ccdcb2632` | pass |

Historical R1 independently reproduced two unequal 416-byte strings:

- canonical SHA-256: `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3`;
- supplied Base64-decoded SHA-256: `f5eb16120e865791f0444a8f0e45cf85aedf141d8f1334c7795196bfb5704b11`.

R1 remained rejected with false evidence, false eligibility, no authority, and zero counters. No historical record was modified.

## 14. CLI Audit

Independent CLI coverage passed for:

- compile from a raw file;
- compile from binary standard input with byte-identical output;
- valid and invalid `verify`;
- valid duplicate and conflicting `verify-record` inputs;
- valid and invalid `verify-checkpoint`;
- all wrong-type fact families;
- all 20 malformed recognized-container shapes;
- all required gating families;
- valid and invalid hexadecimal facts;
- piped trailing LF and invalid UTF-8;
- deterministic sorted JSON with one final LF;
- atomic output creation;
- no-overwrite default;
- explicit overwrite;
- parseable error JSON;
- no canonical-text leakage.

Static source and AST inspection found no implicit Git lookup, Dreamina/provider invocation, network library, subprocess invocation, environment-variable read, or credential/session/token read. CLI `os` use is limited to atomic local-file operations.

## 15. Focused And Full-Suite Validation

Required current-checkpoint commands:

```text
python -m compileall -q app/ai_video_pipeline/governance tools/authorization_compiler.py tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
python -m pytest -o addopts= -q tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
python -m pytest -o addopts= -q --tb=no
```

Results:

```yaml
compileall: pass
focused_tests_passed: 124
focused_tests_failed: 0
full_tests_passed: 592
full_tests_failed: 10
pre_existing_full_test_failures: 10
new_full_test_failures: 0
```

The ten current failures are the exact task-established baseline nodes:

1. `tests/test_phase_c.py::test_16_templates_are_ascii_safe`
2. `tests/test_phase_c.py::test_17_templates_do_not_contain_false_true_mixed_token`
3. `tests/test_phase_f6_3.py::test_16_f6_3_review_record_appends_lock_with_paths`
4. `tests/test_phase_f6_4.py::test_03_f6_4_review_record_exists`
5. `tests/test_phase_g2_3.py::test_03_review_records_and_template_show_approve`
6. `tests/test_phase_g4_3.py::test_05_review_record_and_template_show_approval`
7. `tests/test_phase_g4_4.py::test_03_all_locked_assets_have_review_records`
8. `tests/test_phase_h3.py::test_02_review_record_was_added_without_locking_failed_keyframe`
9. `tests/test_phase_j11.py::test_03_review_record_documents_user_lock_decision`
10. `tests/test_phase_j11.py::test_04_prompt_and_status_files_unblock_shot_02_kf_002`

The parent checkpoint was also checked in a temporary clean worktree. Compile validation passed and the parent focused suite reproduced `39 passed, 0 failed`. Its full suite produced `452 passed, 65 failed` because a clean worktree omits numerous local untracked/ignored historical workspace artifacts required by older phase tests. That result is not comparable to the task-established live-workspace baseline and was not used to relabel failures. The temporary worktree was removed. Current-checkpoint failure identities match the authoritative established baseline exactly, and all 85 newly added focused tests pass.

## 16. Protected State And Boundaries

Protected artifact hashes remained:

| Artifact | SHA-256 |
| --- | --- |
| CAL-001 resumable execution state | `e42e92700d63e9f78a9ac9fb564f3d7410d94f4160dd6e047ab02eeaa02c205b` |
| experiment-results CSV | `f1d183267b24997bb848ff83abd9231b53d84ae82e715d9e4d9b5c2b3de3ff3b` |
| visual-review JSONL | `6f86873a445021f88503625008550c99e7a2ef323acde500d38ccd6a5e5c693a` |
| fixed 84-task manifest | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` |

Protected state remained:

```yaml
macro_state: STOPPED_AUTHORITY_CLOSED
execution_authority_active: false
remaining_noncanary_tasks_authorized: false
completed_fixed_task_count: 13
remaining_completed_task_count: 6
total_submit_count: 13
next_experiment_id: CAL001-F07-P1-R1
F07_authorized: false
final_master: false
locked: false
```

Boundary confirmations:

- Dreamina_called: `false`
- provider_called: `false`
- F07_called: `false`
- sources_touched: `false`
- implementation_files_modified: `false`
- tests_modified: `false`
- CAL001_state_changed: `false`
- CAL001_completed_task_count_changed: `false`
- CAL001_remaining_task_count_changed: `false`
- datasets_modified: `false`
- Prompt_package_manifest_modified: `false`
- media_modified: `false`

## 17. Non-Blocking Notes

1. Conflict diagnostics identify deterministic semantic groups but do not provide fully path-qualified occurrence details. All conflicts still fail closed; this remains a non-blocking diagnostic note.
2. Compile-only uses the decision label `safe_block`. Its evidence, eligibility, authority, provider, and counter semantics are unambiguous; this remains a non-blocking naming note.
3. The parent clean-worktree full-suite count is not comparable because historical workspace-local artifacts are intentionally absent there. Current-checkpoint tests match the established working-environment baseline.

## 18. Final Verdict

`CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_STRICT_VALIDATION_INDEPENDENT_NO_LIVE_AUDIT_PASS_READY_HUMAN_SOURCE_MIRROR_RECONCILIATION`

Next required action:

`human reconciliation of the local sources/ mirror before any F07 preflight`

Do not proceed to F07 preflight or any live operation from this audit receipt.
