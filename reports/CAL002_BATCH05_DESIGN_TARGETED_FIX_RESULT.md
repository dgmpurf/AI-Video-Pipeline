# CAL-002 Batch05 Design Targeted Blind-Review Schema Fix Result

## 1. Starting Checkpoint

```yaml
goal_identity: CAL002_BATCH05_DESIGN_TARGETED_BLIND_REVIEW_SCHEMA_FIX_V0_1
task_label: CAL002_BATCH05_DESIGN_TARGETED_FIX_NO_LIVE
branch: main
starting_head: b7f93897557b057824544e77f31c452685dbf129
starting_origin_main: b7f93897557b057824544e77f31c452685dbf129
head_origin_aligned: true
previous_design_checkpoint: 7250719ddb9fd253f15e71190884400674aa65f9
tracked_modifications_before_write: 0
staged_files_before_write: 0
source_status_entries_before_write: 0
```

No fetch, pull, merge, rebase, reset, clean, stash, amend, or history rewrite
was performed.

## 2. Audit-Result Binding

| Field | Bound value | Result |
| --- | --- | --- |
| Path | `reports/CAL002_BATCH05_DESIGN_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md` | PASS |
| Byte length | `14547` | PASS |
| SHA-256 | `2c0085a5767831cbe4d86c1f2fc72d321c82151271b6b50b26407712a405f258` | PASS |
| Decision | `CAL002_BATCH05_DESIGN_NEEDS_FIX` | PASS |
| Specific verdict | `CAL002_BATCH05_DESIGN_NEEDS_FIX_BLIND_REVIEW_SCHEMA` | PASS |
| Repair class | `bounded_no_live_schema_fix` | PASS |

The audit requires no experimental redesign, Prompt change, task change,
budget change, Source change, or live authority.

## 3. Exact Bounded Defect

The original blinded pair-review record required
`candidate_clear_advantage`. A reviewer who sees only A/B aliases cannot
determine Candidate advantage without treatment mapping, so the field
contradicted the declared blind-review process.

The same pair schema allowed valid, invalid, inconclusive, and clearly-better
judgments without a rationale. The correction is confined to blind and
post-unblinding record semantics.

## 4. Exact Modified and Added Files

Modified existing paths:

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md`
2. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_manifest.json`
3. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json`
4. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_design_evidence_manifest.json`
5. `reports/CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_RESULT.md`

New paths:

1. `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json`
2. `reports/CAL002_BATCH05_DESIGN_TARGETED_FIX_RESULT.md`

No other path is authorized or required.

## 5. Blind-Schema Before and After

Before:

```text
pair_id
comparison_validity
preference
candidate_clear_advantage
```

After:

```text
pair_id
comparison_validity
preference
reviewer_rationale
```

Current blind schema:

```yaml
schema_id: CAL002_BATCH05_BLIND_VISUAL_REVIEW_SCHEMA_V0_2
record_id: CAL002_BATCH05_BLIND_VISUAL_REVIEW_RECORD_V0_2
path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json
byte_length: 9174
sha256: 3e3f816527334ebd0e57078fd1aa9cfc61022698de27209ccd8a2d0dbfb2854c
candidate_clear_advantage_present: false
reviewer_rationale_required: true
reviewer_rationale_min_length: 1
pair_reviews_exact_count: 4
video_reviews_exact_count: 8
additional_pair_properties_allowed: false
```

The blind reviewer records only treatment-neutral A/B observations. The
complete-MP4 requirement and every per-video endpoint field and enum remain
unchanged.

## 6. Post-Unblinding Schema Structure

```yaml
schema_id: CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_SCHEMA_V0_1
record_id: CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_1
path: experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json
byte_length: 8741
sha256: bd3c21b07e44ebe8b40a7d4d92e74d443967b88a15a350e83b5e94665a0442da
draft: JSON Schema 2020-12
additional_properties: false
pair_derivation_count: 4
family_decision_count: 2
```

The derived record requires the blind record to have been finalized before
unblinding, binds its lowercase SHA-256, and binds the exact manifest and task
matrix used as mapping sources.

Each pair derivation records Candidate and Control sides, sealed blind
validity and preference, derived Candidate advantage, derivation class, and a
non-empty rationale. Candidate and Control sides must differ.
`candidate_clear_advantage=true` is valid only with
`CANDIDATE_CLEAR_ADVANTAGE`; every other derivation class requires false.

Family decisions are ordered and fixed to `push_reaction` and
`brief_impact_recoil`, with counts restricted to `0..2` and a required
non-empty rationale.

## 7. Reviewer-Package Exclusion Contract

The future blinded reviewer package may contain only:

- alias-labeled complete MP4 files;
- alias-labeled technical metadata;
- alias-labeled review aids;
- `batch05_visual_review_schema.json`;
- a blank blind review record.

It must exclude:

- `batch05_design_manifest.json`;
- `batch05_task_matrix.csv`;
- `batch05_treatment_diff_matrix.json`;
- `CAL002_BATCH05_DESIGN_SPEC.md`;
- `batch05_budget_and_authority_plan.json`;
- `batch05_post_unblinding_analysis_schema.json`;
- `batch05_design_evidence_manifest.json`;
- all design, audit, and fix reports;
- all package files containing treatment labels;
- every filename containing `CONTROL` or `CANDIDATE`.

Review-facing media must use blind aliases. This is a future package-builder
constraint and creates no package or authority now.

## 8. Schema-Validation Probes

Both schemas pass `Draft202012Validator.check_schema`.

Blind-schema positive probes:

| Probe | Expected | Result |
| --- | --- | --- |
| Complete record with 8 videos, 4 pairs, no Candidate field, and non-empty pair rationales | PASS | PASS |

Blind-schema negative probes:

| Probe | Expected | Result |
| --- | --- | --- |
| Pair contains `candidate_clear_advantage` | FAIL | PASS |
| Pair missing `reviewer_rationale` | FAIL | PASS |
| Pair has empty rationale | FAIL | PASS |
| Pair count is 3 | FAIL | PASS |
| Pair count is 5 | FAIL | PASS |
| Video count is 7 | FAIL | PASS |
| Video count is 9 | FAIL | PASS |

Post-unblinding positive probes:

| Probe | Expected | Result |
| --- | --- | --- |
| Complete record with 4 pair derivations and 2 family decisions | PASS | PASS |
| Candidate advantage true with Candidate-advantage class | PASS | PASS |
| False with Control-advantage class | PASS | PASS |
| False with no-clear-advantage class | PASS | PASS |
| False with invalid-comparison class | PASS | PASS |
| False with inconclusive-comparison class | PASS | PASS |

Post-unblinding negative probes:

| Probe | Expected | Result |
| --- | --- | --- |
| True with a non-Candidate derivation class | FAIL | PASS |
| Candidate and Control side equal | FAIL | PASS |
| Blind-record SHA missing | FAIL | PASS |
| Mapping-source binding missing | FAIL | PASS |
| Pair derivation count is 3 | FAIL | PASS |
| Pair derivation count is 5 | FAIL | PASS |
| Family decision count is 1 | FAIL | PASS |
| Family decision count is 3 | FAIL | PASS |
| Decision rationale missing | FAIL | PASS |
| Decision rationale empty | FAIL | PASS |

Probe summary:

```yaml
blind_positive_probes_passed: 1
blind_negative_probes_passed: 7
post_unblinding_positive_probes_passed: 6
post_unblinding_negative_probes_passed: 10
schema_probe_result: PASS
```

## 9. Immutable Design-File Checks

| Immutable artifact | SHA-256 | Result |
| --- | --- | --- |
| `batch05_task_matrix.csv` | `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32` | PASS |
| `batch05_variable_lock_table.csv` | `5d58b410b93492d87b1cf82940a44a4d0ae3a4b7dd0cce8bf544cca3175d9a9a` | PASS |
| `batch05_treatment_diff_matrix.json` | `2571b6b587562b3268f1380000573b775e902c1bd5edca5a1da72f7f40b02c3f` | PASS |
| `batch05_budget_and_authority_plan.json` | `82cbc92ebbc8faf5188c9e67852c178180c09d3f01b83cf5d1bcfd06a9c1b40e` | PASS |

The task count remains eight, each of the four cells remains balanced at two,
automatic expansion remains false, the tie-breaker remains absent and
unauthorized, and every live/final/lock flag remains false.

## 10. Prompt-Blueprint Regression

All four Prompt blueprints were independently reconstructed from the modified
manifest:

| Blueprint | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| `PUSH_CONTROL` | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` | PASS |
| `PUSH_CANDIDATE` | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` | PASS |
| `IMPACT_CONTROL` | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` | PASS |
| `IMPACT_CANDIDATE` | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` | PASS |

Shared blocks remain:

```text
SHARED_VISUAL_CONSTANT_BLOCK =
0dfde4b0f6c8ee1bed94cda3d8e727d5352498524b03bbb0f4d9e15f6304acd9

SHARED_SAFETY_AND_CAMERA_BLOCK =
c51ad0c1788a1e923a9d7fa300b3e9b37fe282eee39cbc3c120c50e3febddbdc

SHARED_COMPACT_NEGATIVE_BLOCK =
5e675cf7e987e4a9acc31471650ad27666b6e215433c3e7ba4cf95089697945e
```

Prompt-blueprint and shared-block regression result: `PASS_UNCHANGED`.

## 11. Evidence-Manifest Update

`batch05_design_evidence_manifest.json` now has:

```yaml
schema_version: CAL002_BATCH05_DESIGN_EVIDENCE_MANIFEST_V0_2
artifact_count: 9
included_artifact_count: 9
self_excluded: true
byte_length: 3870
sha256: fe128c8a45007e679e4e073d3c93cf7cf04b412b662e03c23b07d9f3ae527a93
```

It binds the design spec, budget plan, design manifest, task matrix, treatment
diff, variable locks, blind visual-review schema, post-unblinding schema, and
updated design-result report. All nine byte-length and SHA-256 bindings pass.

## 12. Explicit No-Live Statement

No Dreamina, provider, version, credit, help, submit, query, download, retry,
resubmit, batch, login, or session operation was performed.

```yaml
Dreamina_called: false
provider_called: false
provider_command_count: 0
Prompt_package_created: false
execution_package_created: false
authorization_text_created: false
media_created: false
review_artifacts_created: false
```

## 13. Explicit No-Source-Change Statement

`sources/` remained read-only. No Source was created, modified, synchronized,
staged, committed, or pushed.

```yaml
sources_changed: false
local_source_sync_authorized: false
```

## 14. Explicit No Task, Prompt, or Budget Redesign

```yaml
experimental_redesign: false
task_change: false
Prompt_change: false
provider_target_change: false
reference_strategy_change: false
endpoint_change: false
budget_change: false
authority_change: false
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

## 15. Exact Next Phase and Verdict

Next phase:

```text
CAL002_BATCH05_DESIGN_TARGETED_FIX_INDEPENDENT_NO_LIVE_AUDIT
```

Final fix verdict:

```text
CAL002_BATCH05_TARGETED_FIX_APPLIED_READY_FOR_INDEPENDENT_REAUDIT
```
