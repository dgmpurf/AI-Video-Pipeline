# CAL-002 Batch05 Review Derivation Integrity Targeted Fix Result

## 1. Starting Checkpoint and Audit Binding

```yaml
goal_identity: CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_TARGETED_FIX_V0_1
task_label: CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_TARGETED_FIX_NO_LIVE
starting_head: b45dbf9a86c0d862709cfaf48d8fc6885d48a6cf
starting_origin_main: b45dbf9a86c0d862709cfaf48d8fc6885d48a6cf
head_origin_aligned: true
starting_parent: 59a1f39a449b6bffb69e63d72afcd8a4ec83dff3
starting_commit_message: "audit(cal002): verify Batch05 blind review fix"
staged_files_before_write: 0
tracked_modifications_before_write: 0
sources_tracked_or_staged_modifications_before_write: 0
```

The bound independent audit report passed exact-byte verification:

```yaml
path: reports/CAL002_BATCH05_DESIGN_TARGETED_FIX_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
byte_length: 15400
sha256: 924083e8c9d1e681d95b85f0b96c207710a5f181086e5107ea880fd67a2323ba
decision: NEEDS_FIX
specific_verdict: CAL002_BATCH05_TARGETED_FIX_NEEDS_SECOND_BOUNDED_SCHEMA_FIX
required_repair_class: bounded_no_live_review_derivation_integrity_fix
```

## 2. Remaining Defects Corrected

The second bounded fix addresses only the decision-bearing review and
derivation gaps identified by the re-audit:

1. Exact array lengths did not enforce every blind alias and pair ID exactly
   once.
2. Blind validity and preference combinations were not locally constrained.
3. Candidate/Control pair outcomes could be operator-authored without a
   complete derivation truth table.
4. Repeated blind values in a derived record were not verified against the
   finalized blind-record bytes.
5. Mapping byte lengths and hashes could be arbitrary syntactically valid
   values.
6. Family verdict labels were independent of their counts and lacked evidence
   fields needed for deterministic regression and route-reset decisions.
7. No checked-in derive/verify mechanism rejected substitution, drift, or
   contradictory output.

The experiment itself remains unchanged.

```yaml
experimental_redesign: false
Prompt_change: false
task_change: false
budget_change: false
provider_target_change: false
live_authority: false
```

## 3. Exact Write Set

Modified paths:

```text
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json
reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md
```

Added paths:

```text
experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py
tests/test_cal002_batch05_review_derivation.py
reports/CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_TARGETED_FIX_RESULT.md
```

```yaml
modified_paths: 6
added_paths: 3
deleted_paths: 0
unexpected_paths: 0
total_changed_paths: 9
```

## 4. Blind Schema V0.3

```yaml
path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json
schema_id: CAL002_BATCH05_BLIND_VISUAL_REVIEW_SCHEMA_V0_3
record_version: CAL002_BATCH05_BLIND_VISUAL_REVIEW_RECORD_V0_3
byte_length: 18138
sha256: 9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5
draft_2020_12_schema_check: PASS
```

The schema fixes all eight video reviews and four pair reviews through ordered
`prefixItems`, exact lengths, and `items=false`. Every video position binds the
exact blind alias and exact action family. Every pair position binds the exact
pair ID. Duplicate, missing, reordered, and alias/family-mismatched records are
rejected.

Allowed blind validity/preference combinations are:

| Comparison validity | Allowed preference |
| --- | --- |
| `VALID` | `A_CLEARLY_BETTER`, `B_CLEARLY_BETTER`, `NO_CLEAR_DIFFERENCE` |
| `INVALID_UNCONTROLLED_VARIATION` | `NOT_COMPARABLE` |
| `INVALID_TECHNICAL` | `NOT_COMPARABLE` |
| `INCONCLUSIVE` | `NO_CLEAR_DIFFERENCE`, `NOT_COMPARABLE` |

Every pair still requires a non-empty rationale. The schema contains no
Candidate/Control identity and no Candidate-advantage field.

## 5. Post-Unblinding Schema V0.2

```yaml
path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json
schema_id: CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_SCHEMA_V0_2
record_version: CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_2
byte_length: 16213
sha256: 7df7e1dca6cc702eb15c60c8178d9ebca5c77f47c3db2429bb5479ab3f4e4802
draft_2020_12_schema_check: PASS
manual_authoring_permitted: false
```

The schema now requires:

- exact derivation-tool path, byte length, SHA-256, and version;
- blind-record path, exact byte length, SHA-256, and finalized-before-unblind
  confirmation;
- two fixed mapping-source bindings;
- four fixed pair derivations with a complete local truth table;
- two fixed family summaries with all counts, flags, result, and rationale.

The schema defines output shape and local constraints. Cross-file integrity and
family precedence are enforced by deterministic re-derivation, not by trusting
schema-valid operator input.

## 6. Deterministic Derivation Tool

```yaml
path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py
tool_version: CAL002_BATCH05_REVIEW_DERIVATION_TOOL_V0_1
byte_length: 31983
sha256: 02902f29301da671ea9707c56b8a84ed6348cccf7f9e5390b4c7b161a2e09ef9
derive_mode: true
verify_mode: true
provider_operations: false
```

The tool uses strict JSON parsing, rejects BOM, duplicate keys, non-finite
numbers, invalid UTF-8, non-canonical formatting, and schema-invalid records.
It requires sorted keys, two-space indentation, and exactly one terminal LF.

`derive` creates a complete deterministic record and writes atomically. It
never overwrites unless local `--overwrite` is explicit. `verify` independently
re-derives the expected record and requires byte-for-byte equality.

## 7. Pair Truth Table

Candidate and Control sides come only from the verified counterbalanced
mapping.

| Validity | Preference | Derived result |
| --- | --- | --- |
| `VALID` | Candidate side clearly better | `CANDIDATE_CLEAR_ADVANTAGE`, Candidate advantage `true` |
| `VALID` | Control side clearly better | `CONTROL_CLEAR_ADVANTAGE`, Candidate advantage `false` |
| `VALID` | `NO_CLEAR_DIFFERENCE` | `NO_CLEAR_ADVANTAGE`, Candidate advantage `false` |
| Invalid | `NOT_COMPARABLE` | `INVALID_COMPARISON`, Candidate advantage `false` |
| `INCONCLUSIVE` | no difference/not comparable | `INCONCLUSIVE_COMPARISON`, Candidate advantage `false` |

The ten contradictory pair probes from the audit are rejected by post-schema
validation and deterministic verification.

## 8. Family Decision Precedence

The tool computes Candidate and Control primary passes; valid,
Candidate-advantage, Control-advantage, no-advantage, invalid, and inconclusive
pair counts; action-family mismatch counts; technical-invalid counts; and four
decision flags.

Precedence is fixed:

1. `ROUTE_RESET_REQUIRED` when both treatments frequently fail or both family
   pairs are invalid because of uncontrolled variation.
2. `CANDIDATE_FAMILY_COMPILER_REGRESSION` when Candidate repeatedly routes to
   the wrong family or is worse than Control.
3. `FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL` when Candidate passes `2/2`,
   both pairs are valid, and Candidate wins `2/2`.
4. `BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE` when both
   treatments pass `2/2`, both pairs are valid, and both show no clear
   advantage.
5. `INCONCLUSIVE_REPLICATION` otherwise.

The nine contradictory family-decision probes from the audit remain
schema-shaped records but fail verify because they do not byte-match
deterministic re-derivation.

## 9. Blind and Mapping Cryptographic Verification

The exact finalized blind file bytes determine:

```text
blind_review_record_byte_length
blind_review_record_sha256
```

The tool independently reads both mapping sources from the worktree and
`HEAD`, requires exact byte identity, and computes each binding itself. It
cross-validates all eight aliases and tasks, treatment, family, replicate, and
the required counterbalanced mapping.

Verify mode blocks:

- changed blind values with a retained old hash;
- copied blind validity/preference substitution;
- arbitrary mapping byte lengths or hashes;
- dirty mapping worktree bytes;
- manifest/task-matrix disagreement;
- duplicate or missing aliases and task IDs;
- pair and family contradictions;
- one-byte derived-record mutation.

## 10. Test Inventory and Results

```yaml
test_path: tests/test_cal002_batch05_review_derivation.py
byte_length: 21717
sha256: 92149ec42f5cf907c31e38f399be74e580062d05f139556bf4076bacf35aefb0
collected_tests: 59
passed_tests: 59
failed_tests: 0
focused_test_result: PASS
```

Coverage includes:

- exact blind alias/pair coverage and alias/family binding;
- validity/preference combinations and non-empty rationale;
- all valid pair truth-table branches;
- all ten contradictory pair probes;
- blind hash mutation and retained-old-hash substitution;
- mapping hash substitution, worktree drift, disagreement, and duplicates;
- all five family verdicts and all nine contradictory family probes;
- deterministic output, exact verify, CLI derive/verify, no-overwrite, and
  semantic one-byte mutation;
- duplicate-key, BOM, non-finite, and invalid-UTF-8 rejection.

## 11. Immutable Task, Prompt, and Budget Regression

| Immutable artifact | SHA-256 | Result |
| --- | --- | --- |
| `batch05_task_matrix.csv` | `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32` | PASS |
| `batch05_variable_lock_table.csv` | `5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a` | PASS |
| `batch05_treatment_diff_matrix.json` | `2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f` | PASS |
| `batch05_budget_and_authority_plan.json` | `82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e` | PASS |

The matrix still contains eight unique tasks, four cells, and two replicates
per cell. Automatic expansion and tie-breaker authority remain false.

| Prompt blueprint | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| `PUSH_CONTROL` | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | PASS |
| `PUSH_CANDIDATE` | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | PASS |
| `IMPACT_CONTROL` | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | PASS |
| `IMPACT_CANDIDATE` | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | PASS |

Shared-block regression passes `3/3`. The provisional budget remains eight
tasks and `560` credits, without current balance or authority.

Protected evidence snapshot:

```yaml
Batch01_through_Batch04_file_count: 567
Batch01_through_Batch04_total_bytes: 182619366
Batch01_through_Batch04_aggregate_sha256: dc84c361b1dbdb20afe147756b1ff1b2b424e033ee6d6ed8f2f008b4688afd25
Batch05_immutable_aggregate_sha256: b330bb0575e977f68ef4477578a2c977a704e6044fbc8c8219061ba758f41b5a
protected_evidence_unchanged: true
```

## 12. Evidence Manifest Update

```yaml
path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json
byte_length: 4630
sha256: 3159336dfe4de4a76b0417259522a5ee757ed97df25f54f64ed351c1bb3fab2b
artifact_count: 11
included_artifact_count: 11
unique_bound_paths: 11
self_excluded: true
all_bindings_match: true
```

The manifest binds the specification, budget plan, design manifest, task
matrix, treatment diff, variable locks, both schemas, derivation tool, focused
tests, and design-result report. Recursive self-exclusion is preserved.

## 13. No-Live Statement

No Dreamina, provider, version, credit, help, submit, query, download, retry,
resubmit, batch, login, or session command was run. No provider Prompt,
package, live manifest, authorization text, execution claim, media, frame,
contact sheet, or comparison sheet was created or modified.

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
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

## 14. Source Governance

`sources/` remained read-only with zero tracked or staged changes. No Source
file was created, modified, deleted, renamed, synchronized, staged, committed,
or pushed.

```yaml
sources_changed: false
```

## 15. Exact Next Phase and Verdict

Next phase:

```text
CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_INDEPENDENT_NO_LIVE_AUDIT
```

Final fix verdict:

```text
CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_APPLIED_READY_FOR_INDEPENDENT_AUDIT
```
