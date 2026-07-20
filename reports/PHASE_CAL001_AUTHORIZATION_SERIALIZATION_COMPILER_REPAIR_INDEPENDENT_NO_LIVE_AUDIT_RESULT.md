# CAL-001 Authorization Serialization Compiler Repair Independent No-Live Audit

## 1. Audit Receipt

- phase: `CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_REPAIR_INDEPENDENT_NO_LIVE_AUDIT`
- audit_status: `COMPLETE`
- decision: `safe_block`
- execution_type: independent no-live audit
- repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- branch: `main`
- required_starting_head: `3e23502988889379fd75c5a9ffbdc444c44b850b`
- starting_local_head: `3e23502988889379fd75c5a9ffbdc444c44b850b`
- starting_origin_main: `3e23502988889379fd75c5a9ffbdc444c44b850b`
- repair_diff_base: `6631902ea6ca03063502990bc7ab6d64df971d1b`
- repair_diff_head: `3e23502988889379fd75c5a9ffbdc444c44b850b`
- Dreamina_authorized: `false`
- provider_authorized: `false`
- F07_authorized: `false`

The repair report was inspected as one changed file but was not used as primary proof. The findings below come from the implementation diff, direct source inspection, independent standard-library derivation, subprocess CLI probes, state probes, and current-versus-parent test comparison.

## 2. Repository And Workspace Preflight

`git fetch origin` completed without changing tracked files. At audit start, local `HEAD` and `origin/main` both matched the required checkpoint, the branch was `main`, and the index was empty.

The only tracked working-tree modification was the known human-managed Source-mirror deletion. The complete known Source-mirror state was:

```text
 D sources/AI视频制作_Source索引与使用优先级_V1.11.md
?? sources/AI视频制作_Source索引与使用优先级_V1.12.md
?? sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md
```

- known_human_source_mirror_changes_present: `true`
- unexpected_source_changes_present: `false`
- sources_touched: `false`
- sources_staged: `false`
- unrelated tracked changes: `false`

Known untracked workspace noise was left untouched. No cleanup, reset, revert, rename, move, or normalization was performed.

## 3. Exact Repair Diff Audited

The base-to-head diff contained exactly the five declared files:

- `app/ai_video_pipeline/governance/authorization_serialization.py`
- `tools/authorization_compiler.py`
- `tests/test_authorization_serialization.py`
- `tests/test_authorization_compiler_cli.py`
- `reports/PHASE_CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_CONTRADICTION_AND_ACTIVATION_BOUNDARY_REPAIR_NO_LIVE_RESULT.md`

`git diff --check 6631902ea6ca03063502990bc7ab6d64df971d1b 3e23502988889379fd75c5a9ffbdc444c44b850b` passed.

## 4. Blocking Findings

### B1. Boolean And Numeric Type Confusion Is Accepted

`_record_values_equal()` is type-sensitive for duplicate conflict detection, but `_record_fact_mismatches()` compares selected record facts with `expected != actual`. Python treats `1 == True` and `0 == False`, so a single occurrence or two identical occurrences with the wrong JSON type can pass verification.

Independent probes supplied integer `1` or `0` for boolean facts and boolean `true` for the integer decode-count fact. The following 14 recognized facts were accepted with no mismatch, no validation error, CLI exit code `0`, and `authorization_evidence_verified=true`:

- `utf8_decode_valid`
- `bom_present`
- `cr_present`
- `lf_present`
- `trailing_carriage_return`
- `trailing_newline`
- `trailing_space`
- `markdown_fence_present`
- `decoded_bytes_equal_original`
- `base64_round_trip_verified`
- `decoded_sha256_equal_original`
- `byte_profile_valid`
- `serialization_round_trip_verified`
- `base64_decode_count`

Two identical malformed occurrences, such as root and nested `utf8_decode_valid=1`, were also accepted because they were representation-consistent and then passed loose equality against `True`.

Classification: `BLOCKING`.

### B2. Malformed Recognized Containers Are Silently Ignored

`_record_containers()` only adds `canonical_serialization`, `canonical_authorization`, or their nested `verification` value when that value is a `Mapping`. If a recognized container key exists with a string, array, scalar, or other non-object value, it is silently omitted instead of producing a validation error.

Each of these independently tested records retained CLI exit code `0` and `authorization_evidence_verified=true` when otherwise-valid top-level length and SHA-256 evidence was present:

- `canonical_serialization: "not-an-object"`
- `canonical_authorization: ["not-an-object"]`
- `canonical_serialization.verification: "not-an-object"`
- `canonical_authorization.verification: "not-an-object"`

This violates the requirement that every recognized occurrence participate in validation and that malformed secondary occurrences cannot hide behind valid primary evidence.

Classification: `BLOCKING`.

### B3. A Validation Error Can Still Produce Verified Evidence

When a record supplies `base64_character_count` or `derived_base64_character_count` but supplies no recognized Base64 value, the verifier appends `expected_base64_missing`. That error is not included in `expected_values_match`, and authorization evidence is not gated on an empty validation-error set.

An independently constructed record containing valid byte length, valid SHA-256, and the correct Base64 character count but no Base64 produced:

```yaml
validation_errors:
  - expected_base64_missing
authorization_evidence_verified: true
authorization_verified: true
cli_exit_code: 0
```

Classification: `BLOCKING`.

### B4. Hexadecimal Case Semantics Are Inconsistent

Top-level SHA-256 case-only differences are accepted, and duplicate `decoded_sha256` representations are compared case-insensitively. However, the selected `decoded_sha256` fact is compared case-sensitively with the derived lowercase digest. An uppercase but otherwise identical decoded SHA-256 is therefore rejected. Lowercase `last_byte_hex=2e` is also rejected against derived `2E`.

This is fail-closed rather than an authority bypass, but it does not satisfy the required hexadecimal case-only compatibility rule.

Classification: `BLOCKING_CONTRACT_DEVIATION`.

## 5. Recognized Representation Enumeration

Independent runtime tracing confirmed five recognized container locations:

1. record root
2. `canonical_serialization`
3. `canonical_authorization`
4. `canonical_serialization.verification`
5. `canonical_authorization.verification`

The implementation declares 25 semantic groups and 34 unique aliases. Runtime tracing found no alias used by verification but absent from contradiction enumeration, and no declared alias unused by verification.

| Semantic group | Recognized aliases |
| --- | --- |
| `byte_length` | `byte_length`, `authorization_byte_length` |
| `sha256` | `sha256`, `authorization_text_sha256` |
| `base64` | `base64`, `authorization_base64`, `locally_derived_base64`, `locally_generated_base64` |
| `base64_character_count` | `base64_character_count`, `derived_base64_character_count` |
| `canonical_text` | `canonical_authorization_text`, `exact_authorization_text` |
| `authority_source` | `authority_source` |
| `encoding` | `encoding` |
| `utf8_decode_valid` | `utf8_decode_valid` |
| `bom_present` | `bom`, `bom_present` |
| `cr_present` | `cr_present` |
| `lf_present` | `lf_present` |
| `trailing_carriage_return` | `trailing_carriage_return` |
| `trailing_newline` | `trailing_newline` |
| `trailing_space` | `trailing_space` |
| `markdown_fence_present` | `markdown_fence_present` |
| `last_character` | `last_character` |
| `last_byte_hex` | `last_byte_hex` |
| `base64_decode_count` | `base64_decode_count`, `locally_generated_base64_decode_count` |
| `decoded_bytes_equal_original` | `decoded_bytes_equal_original` |
| `base64_round_trip_verified` | `base64_round_trip_verified` |
| `decoded_sha256_equal_original` | `decoded_sha256_equal_original` |
| `byte_profile_valid` | `byte_profile_valid` |
| `serialization_round_trip_verified` | `serialization_round_trip_verified` |
| `decoded_sha256` | `decoded_sha256` |
| `authorization_verified` | `authorization_verified` |

For Mapping-shaped containers, an unequal value in every one of the 25 groups was independently tested. Every such conflict reported its semantic group and failed closed with evidence, authorization, eligibility, execution authority, provider permission, and both counters all false or zero.

Equal valid duplicate aliases remained compatible. Unknown fields such as input `eligible_for_authority_activation=true` were not promoted to authority and did not alter the verifier's direct eligibility output.

Exhaustive result:

```yaml
all_recognized_containers_enumerated: true
all_recognized_aliases_enumerated: true
all_mapping_container_group_conflicts_fail_closed: true
every_recognized_occurrence_participates: false
malformed_secondary_occurrence_rejected: false
two_identical_malformed_occurrences_rejected: false
equal_duplicate_occurrence_accepted: true
bool_int_type_confusion_rejected: false
unknown_field_promoted_to_authority: false
```

## 6. Original Blocking Defect Reproduction

The six specified original conflict probes are closed:

| Probe | Conflict group | Evidence verified | Eligible | CLI exit |
| --- | --- | --- | --- | ---: |
| correct `base64` plus conflicting `authorization_base64` | `base64` | false | false | 1 |
| correct `locally_derived_base64` plus conflicting `locally_generated_base64` | `base64` | false | false | 1 |
| correct nested byte length plus conflicting top-level byte length | `byte_length` | false | false | 1 |
| correct nested SHA-256 plus conflicting top-level SHA-256 | `sha256` | false | false | 1 |
| correct canonical text plus conflicting exact text | `canonical_text` | false | false | 1 |
| conflicting nested round-trip fact | `decoded_bytes_equal_original` | false | false | 1 |

Every case also retained:

```yaml
authorization_verified: false
execution_authority_active: false
provider_command_allowed: false
provider_command_invocation_count: 0
authorized_operation_count_consumed: 0
```

Therefore:

- original_base64_alias_blocker_closed: `true`
- original_nested_fact_blocker_closed: `true`
- original_canonical_text_alias_blocker_closed: `true`
- original_compile_only_activation_blocker_closed: `true`

## 7. Path-Qualified Diagnostic Audit

A three-container Base64 conflict emitted only:

```json
{
  "record_representation_conflicts": ["base64"],
  "validation_errors": ["record_representation_conflict:base64"]
}
```

No output field identifies the conflicting container paths or aliases. The semantic group is deterministic and the unequal Mapping-shaped representations fail closed, so this diagnostic limitation does not itself create an authority bypass. The original record can still be enumerated independently to locate all occurrences.

- path_qualified_occurrence_evidence_available: `false`
- path_diagnostic_classification: `NON_BLOCKING_CONTRACT_NOTE`

## 8. State Separation And Decision Semantics

| State | Profile valid | Evidence verified | Checkpoint verified | Eligible | Decision |
| --- | --- | --- | --- | --- | --- |
| compile only | true | false | absent | false | `safe_block` when evaluated |
| compile plus valid checkpoint | true | false | true | false | `safe_block` |
| verified evidence without checkpoint | true | true | absent | false | `safe_block` |
| checkpoint verification alone | not applicable | absent | true | false | no combined decision |
| verified evidence plus invalid checkpoint | true | true | false | false | `safe_block` |
| verified evidence plus valid checkpoint | true | true | true | true | `ready` |

The combined valid case only reports eligibility. It keeps execution authority inactive, provider commands disallowed, provider invocation count zero, and authorized operation count consumed zero.

Compile output has no `decision` field. It reports `serialization_profile_valid=true`, `authorization_evidence_verified=false`, `authorization_verified=false`, and `eligible_for_authority_activation=false`. Calling `evaluate_activation_eligibility()` on compile-only output returns `decision=safe_block`; it never returns `ready`.

The preferred compile-only name `serialization_ready_for_evidence_verification` is not emitted, but the existing state names and `safe_block` result are unambiguous.

- decision_semantics_classification: `NON_BLOCKING_NAMING_DEVIATION`

## 9. Independent Historical Fixture Verification

Canonical bytes were extracted from each JSON record, encoded with Python standard-library UTF-8, hashed independently, Base64-encoded independently, and only then passed to the repaired verifier.

| Fixture | Bytes | Independently derived SHA-256 | Stored Base64 matches | Repaired verifier |
| --- | ---: | --- | --- | --- |
| F06 recovery query R2 | 432 | `0f4306d42084ab96044eea5a89d338e0cf1e41c31e39d8df85b25a15626fe883` | true | pass |
| F06 recovery download | 607 | `e56a37cc5e7f17aaa691ec4e5862fa9253e1a0273221523f9b2a2c172601ff4a` | true | pass |
| F06 review-artifact authorization | 583 | `472da91ce12a778f6505844fb52e80a86dd2c1e11cafd469c344cfe08d4df1a1` | true | pass |
| F06 visual-review authorization | 1036 | `e50c231685d549167eeb71ce229e3f61e17ad392da1fc1468aa41d9ccdcb2632` | true | pass |

The historical R1 probe independently reproduced two different 416-byte strings:

- canonical SHA-256: `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3`
- supplied Base64-decoded SHA-256: `f5eb16120e865791f0444a8f0e45cf85aedf141d8f1334c7795196bfb5704b11`

The repaired verifier rejected R1 with Base64 mismatch, decoded-byte mismatch, and decoded-SHA mismatch errors.

## 10. CLI Audit

Independent temporary-directory probes confirmed:

- compile from raw file: pass, exit 0;
- compile from binary stdin: pass, byte-identical stable JSON;
- verify: pass, evidence true but direct eligibility false;
- verify-record with equal valid duplicate aliases: pass;
- verify-checkpoint: binding true but direct eligibility false;
- conflicting alias: rejected with exit 1;
- ordinary malformed secondary alias conflicting with a valid alias: rejected with exit 1;
- piped trailing LF: rejected with exit 1 and no trimming;
- invalid UTF-8: rejected with exit 1;
- stable JSON: deterministic, sorted, and final LF present;
- atomic output: first write succeeded and left no temporary file;
- no-overwrite default: second write returned exit 2 and preserved prior bytes;
- explicit overwrite: succeeded and reproduced identical bytes;
- input/output error: parseable generic JSON on stderr;
- canonical text leakage: false.

The three blocking fail-open records in Sections B1 through B3 also reproduced through `verify-record` with exit 0.

Static source inspection found no Git command, Dreamina command, provider invocation, subprocess call, network access, credential read, session read, token read, or environment-variable read in the library or CLI. Temporary probe directories were automatically removed.

## 11. Test And Parent-Baseline Audit

Required commands:

```text
python -m compileall -q app/ai_video_pipeline/governance tools/authorization_compiler.py tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
python -m pytest -o addopts= -q tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
python -m pytest -o addopts= -q --tb=no
```

Current checkpoint results:

- compileall: pass
- focused tests passed: `39`
- focused tests failed: `0`
- full tests passed: `507`
- full tests failed: `10`

The same full suite was run in a clean temporary detached worktree at parent checkpoint `6631902ea6ca03063502990bc7ab6d64df971d1b`:

- parent full tests passed: `445`
- parent full tests failed: `65`
- every one of the current 10 failures was also present in the parent failure set
- current full-suite failures pre-existing at parent: `10`
- new full-suite failures introduced by repair: `0`

The parent worktree lacked untracked historical artifacts present in the main workspace, explaining its larger failure set. Set inclusion, not aggregate count equality, establishes that the repair introduced none of the current failures. The temporary worktree was removed and `git worktree list` returned only the main worktree.

The focused tests do not cover the three fail-open cases or path-qualified diagnostic output identified by this audit.

## 12. Protected Boundaries

Protected hashes remained:

| Protected artifact | SHA-256 |
| --- | --- |
| CAL-001 resumable execution state | `e42e92700d63e9f78a9ac9fb564f3d7410d94f4160dd6e047ab02eeaa02c205b` |
| experiment-results CSV | `f1d183267b24997bb848ff83abd9231b53d84ae82e715d9e4d9b5c2b3de3ff3b` |
| visual-review JSONL | `6f86873a445021f88503625008550c99e7a2ef323acde500d38ccd6a5e5c693a` |
| fixed 84-task manifest | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` |

State remained:

```yaml
macro_state: STOPPED_AUTHORITY_CLOSED
execution_authority_active: false
remaining_noncanary_tasks_authorized: false
stop_condition: F06_technically_completed_authority_closed_no_F07_authorization
```

Boundary confirmation:

```yaml
Dreamina_called: false
provider_called: false
F07_called: false
F07_authorized: false
sources_touched: false
sources_staged: false
implementation_files_modified: false
tests_modified: false
CAL001_state_changed: false
datasets_modified: false
Prompt_package_manifest_modified: false
media_modified: false
execution_authority_active: false
final_master: false
locked: false
```

## 13. Decision

The original conflicting-alias blockers and compile-only activation blocker are closed. State separation, historical compatibility, CLI output safety, and protected boundaries pass.

Decision is nevertheless `safe_block` because recognized authorization evidence can still be verified through wrong JSON types, malformed recognized containers can be ignored, and a record carrying `expected_base64_missing` can still verify. Hexadecimal case semantics also remain inconsistent. These violate the exhaustive recognized-representation and strict type/format requirements.

No repair was made during this audit. F07 preflight and any live action remain unauthorized.

Required next action: obtain a new bounded no-live repair authorization covering strict selected-fact type validation, recognized-container shape validation, validation-error gating, hexadecimal fact normalization rules, and regression tests for all findings. After that repair, run another independent no-live audit. Do not reconcile or proceed to F07 from this safe-block result.

## 14. Required Receipt Fields

```yaml
status: COMPLETE
Decision: safe_block
phase: CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_REPAIR_INDEPENDENT_NO_LIVE_AUDIT
starting_head: 3e23502988889379fd75c5a9ffbdc444c44b850b
audit_checkpoint_head_before_report_commit: 3e23502988889379fd75c5a9ffbdc444c44b850b
known_human_source_mirror_changes_present: true
unexpected_source_changes_present: false
sources_touched: false
sources_staged: false
implementation_files_modified: false
tests_modified: false
original_base64_alias_blocker_closed: true
original_nested_fact_blocker_closed: true
original_canonical_text_alias_blocker_closed: true
original_compile_only_activation_blocker_closed: true
all_recognized_containers_enumerated: true
all_recognized_aliases_enumerated: true
malformed_secondary_occurrence_rejected: false
equal_duplicate_occurrence_accepted: true
bool_int_type_confusion_rejected: false
path_qualified_occurrence_evidence_available: false
path_diagnostic_classification: NON_BLOCKING_CONTRACT_NOTE
decision_semantics_classification: NON_BLOCKING_NAMING_DEVIATION
compile_authorization_verified: false
compile_eligible_for_authority_activation: false
compile_activation_decision: safe_block
evidence_without_checkpoint_eligible: false
checkpoint_without_evidence_eligible: false
combined_valid_evidence_and_checkpoint_eligible: true
combined_execution_authority_active: false
combined_provider_command_allowed: false
historical_R2_verified: true
historical_download_verified: true
historical_review_artifact_verified: true
historical_visual_review_verified: true
historical_R1_mismatch_rejected: true
focused_tests_passed: 39
focused_tests_failed: 0
full_tests_passed: 507
full_tests_failed: 10
pre_existing_full_test_failures: 10
new_full_test_failures: 0
Dreamina_called: false
provider_called: false
F07_called: false
F07_authorized: false
CAL001_state_changed: false
datasets_modified: false
media_modified: false
audit_report_path: reports/PHASE_CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_REPAIR_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
final_master: false
locked: false
```

The report commit SHA, ending HEAD, `origin/main`, and push result are recorded in the external final receipt after the report-only commit is created. They cannot be embedded as this report's own commit hash without making the commit self-referential.

Final verdict:

`CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_REPAIR_INDEPENDENT_NO_LIVE_AUDIT_SAFE_BLOCK_REPAIR_REQUIRED`
