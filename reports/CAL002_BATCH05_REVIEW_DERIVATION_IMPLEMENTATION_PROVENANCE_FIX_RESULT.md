# CAL-002 Batch05 Review Derivation Implementation Provenance Fix Result

## 1. Starting checkpoint and audit binding

```yaml
goal_identity: CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_V0_1
starting_branch: main
starting_HEAD: e89475dbd2d053a940afd61b66e1c3f4adf0a19d
starting_origin_main: e89475dbd2d053a940afd61b66e1c3f4adf0a19d
HEAD_origin_aligned: true
starting_parent: 99f86ddf571a9906152cb0eb486a71c1c816b364
starting_commit_message: "audit(cal002): verify Batch05 review derivation integrity"
staged_files: 0
tracked_modifications: 0
sources_modifications: 0
```

Bound independent audit:

```yaml
path: reports/CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
byte_length: 19127
sha256: 1a23e2089270f09b66ad47508b44c40e2b8adc66c736641d3eb34af853f34793
decision: CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_NEEDS_FIX
```

## 2. Exact two defects

The bounded implementation correction addresses exactly:

1. `EXECUTING_TOOL_IDENTITY_NOT_ENFORCED`
2. `SCHEMAS_ARE_HIDDEN_MUTABLE_INPUTS`

No experimental redesign, Prompt change, task change, budget change, provider
target change, review-policy change, or live authority is included.

## 3. Exact write set

Modified:

- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json`
- `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py`
- `tests/test_cal002_batch05_review_derivation.py`
- `reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md`

Added:

- `reports/CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_RESULT.md`

The blind-review schema remains byte-identical and does not appear in the diff.

## 4. Executing-tool path and byte invariants

Tool:

```yaml
relative_path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py
tool_version: CAL002_BATCH05_REVIEW_DERIVATION_TOOL_V0_2
byte_length: 35997
sha256: 1bff976a6e14c96184936e81db1baf8df4a2154526c1f8770ac4b45c63388321
resolved_path_policy: ACTUAL_EXECUTING_PATH_MUST_EQUAL_EXPECTED_REPOSITORY_TOOL_RESOLVED_PATH
```

Before either mode processes a record, the implementation:

1. Resolves `--repo-root`.
2. Resolves the required repository tool path.
3. Resolves the actual `Path(__file__)` with `strict=True`.
4. Requires both resolved paths to be equal.
5. Reads actual executing bytes, expected-path worktree bytes, and the
   committed `HEAD:<tool path>` blob.
6. Requires all three byte sequences to be equal.
7. Derives the tool binding only from the verified executing bytes.

The output records `worktree_equals_HEAD=true` and
`executing_file_equals_HEAD=true`. No fixed-path fallback is used when the
actual runner differs.

## 5. Schema worktree and HEAD invariants

Both schema inputs now pass through the same committed-input gate before
parsing:

| Schema | Bytes | SHA-256 |
| --- | ---: | --- |
| Blind visual review V0.3 | 18138 | `9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5` |
| Post-unblinding V0.3 | 18899 | `366a8dac88504626ec400317c116e20c319c70c693a29927fa1753fcb46f396a` |

For each schema, the tool reads worktree and `HEAD` bytes, requires exact
equality, performs strict canonical JSON parsing, checks the expected schema
ID and record version, and validates the schema as Draft 2020-12. Dirty bytes,
missing committed blobs, BOM, invalid UTF-8, duplicate keys, non-finite values,
and noncanonical formatting fail closed.

## 6. Derived-record schema bindings

Post-unblinding schema identity:

```yaml
schema_id: CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_SCHEMA_V0_3
record_schema_version: CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_3
```

The required top-level `schema_source_bindings` array contains exactly two
entries in fixed order:

1. `batch05_visual_review_schema.json`
2. `batch05_post_unblinding_analysis_schema.json`

Each binding records:

```text
relative_path
byte_length
sha256
schema_id
record_version
worktree_equals_HEAD
```

The paths, schema IDs, record versions, order, count, and
`worktree_equals_HEAD=true` are enforced by the V0.3 output schema.

## 7. Verify-mode provenance behavior

`verify` independently rechecks:

- actual executing path and bytes;
- expected tool worktree and committed blob;
- blind schema worktree and committed blob;
- post schema worktree and committed blob;
- exact blind-record bytes;
- design manifest worktree and committed blob;
- task matrix worktree and committed blob.

It validates the supplied V0.3 record, re-derives all bindings, pairs, and
family decisions, then requires exact canonical byte equality. Tool-binding
changes, schema-binding changes, dirty tool/schema bytes, external runners,
earlier record versions, blind substitution, mapping substitution, and any
one-byte derived-record mutation are rejected.

## 8. New isolated tests

The prior 59 tests were preserved. Twenty-one new collected cases cover:

- clean required-path execution and actual-byte binding;
- byte-identical external runner rejection;
- one-byte-modified external runner rejection;
- external verify rejection despite a clean repository hash in the record;
- dirty expected tool rejection before output;
- substituted tool path/version rejection;
- dirty blind and post schemas during derive;
- dirty blind and post schemas during verify;
- substituted schema hashes, lengths, IDs, and record versions;
- earlier post-record version rejection;
- deterministic repeated schema bindings.

All use isolated temporary Git repositories. The real checked-in tool is not
modified by a test.

## 9. Total focused-test result

Command:

```text
pytest -q tests/test_cal002_batch05_review_derivation.py
```

Result:

```yaml
collected: 80
passed: 80
failed: 0
skipped: 0
xfailed: 0
warnings: 0
```

## 10. External-runner negative probes

Independent subprocess probes outside the focused suite:

| Probe | Exit | Output created | Result |
| --- | ---: | --- | --- |
| Byte-identical external runner | 1 | false | PASS_REJECTED |
| One-byte-modified external runner | 1 | false | PASS_REJECTED |
| Dirty expected repository tool | 1 | false | PASS_REJECTED |

The one-byte mutation changed exactly one byte in a nonsemantic CLI
description string. Path provenance blocked it before record processing.

## 11. Dirty-schema negative probes

Independent subprocess probes:

| Probe | Exit | Output created/changed | Result |
| --- | ---: | --- | --- |
| Dirty blind schema during derive | 1 | false | PASS_REJECTED |
| Dirty post schema during derive | 1 | false | PASS_REJECTED |
| Dirty blind schema during verify | 1 | supplied bytes unchanged | PASS_REJECTED |
| Dirty post schema during verify | 1 | supplied bytes unchanged | PASS_REJECTED |

A clean isolated fixture completed derive and verify with exit code 0.
Repeated derivation produced byte-identical output with SHA-256
`b29a165bc7b0a8a6d4ff011dc46646dbf0c0b2848c89075e950d09730a9c75e2`.
All temporary fixture directories were removed.

## 12. Immutable task, Prompt, and budget regression

Protected design hashes:

```yaml
task_matrix: 141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32
variable_locks: 5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a
treatment_diff: 2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f
budget_plan: 82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e
```

Prompt reconstruction:

| Blueprint | Bytes | SHA-256 |
| --- | ---: | --- |
| PUSH_CONTROL | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` |
| PUSH_CANDIDATE | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` |
| IMPACT_CONTROL | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` |
| IMPACT_CANDIDATE | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` |

Shared blocks remain:

```yaml
SHARED_VISUAL_CONSTANT_BLOCK: 0dfde4b0f6c8ee1bed94cda3d8e727d5352498524b03bbb0f4d9e15f6304acd9
SHARED_SAFETY_AND_CAMERA_BLOCK: c51ad0c1788a1e923a9d7fa300b3e9b37fe282eee39cbc3c120c50e3febddbdc
SHARED_COMPACT_NEGATIVE_BLOCK: 5e675cf7e987e4a9acc31471650ad27666b6e215433c3e7ba4cf95089697945e
```

Task count, identities, aliases, four cells, two replicates per cell, treatment
mapping, provider target, budget, and all authority flags remain unchanged.

## 13. Evidence-manifest update

```yaml
schema_version: CAL002_BATCH05_DESIGN_EVIDENCE_MANIFEST_V0_4
artifact_count: 11
included_artifact_count: 11
unique_bound_paths: 11
self_excluded: true
all_bound_lengths_match: true
all_bound_sha256_values_match: true
```

The exact eleven non-self design artifacts remain the same. Only affected
lengths, hashes, and creation-phase labels were updated.

## 14. Explicit no-live statement

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
live_manifest_created: false
authorization_text_created: false
media_created: false
review_artifacts_created: false
```

## 15. Explicit no-Source-change statement

```yaml
sources_read_only: true
sources_changed: false
source_sync_performed: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

## 16. Exact next phase and verdict

Next phase:

```text
CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_INDEPENDENT_NO_LIVE_AUDIT
```

Final fix verdict:

```text
CAL002_BATCH05_IMPLEMENTATION_PROVENANCE_FIX_APPLIED_READY_FOR_INDEPENDENT_AUDIT
```
