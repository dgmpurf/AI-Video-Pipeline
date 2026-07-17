# PHASE CAL-001-P1 - Project-Wide Prompt Calibration No-Run Manifest and Schema Creation Result

## 1. Phase summary

CAL-001-P1 stopped at the Git and Source preflight before creating any experiment artifacts. Both human-applied active Source files exist in the local mirror, but `sources/` is not clean.

- phase_id: CAL-001-P1
- status: blocked_p1_precondition_or_fixture_gap
- blocking_condition: dirty_local_source_mirror
- active_source_files_confirmed: true
- local_source_mirror_status: dirty_transition_uncommitted
- fixed_manifest_exists: false
- fixed_manifest_task_count: 0
- execution_authority_active: false
- partial_experiment_artifacts_created: false
- report_only_blocked_outcome: true

The blocked path was selected before fixture inspection or any manifest, prompt, package, schema, dataset, review, budget, or matrix creation.

## 2. Active Source and routing confirmation

The user explicitly confirmed these Project Source files as active, and both exist in the local mirror:

| Active Source file | Exists | SHA256 |
| --- | --- | --- |
| `sources/AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md` | true | `b93d40902e2156dc6269d8df6b3d051c150ad77e0fd3b8c0e968693d49def062` |
| `sources/AI视频制作_Source索引与使用优先级_V1.11.md` | true | `47201316a3a433b3c8f31c7f52c53b219bc3be95bb775b3da84154d329da2769` |

- human_applied_source_state_accepted: true
- mode_routing_confirmed: Codex / Local / high-effort repository work
- formal_authorization_language: English
- source_metadata_debt: true

Both files still contain candidate or pending-human-application header language. Under the user's instruction, that stale header language is nonblocking metadata debt and was not edited. It is distinct from the blocking Git cleanliness condition.

## 3. CAL-001A conditional authorization carry-forward

- authorization_language: English
- authorization_type: conditional_pre_authorization
- execution_authority_active: false
- fixed_manifest_target_count: 84
- submit_count_max: 84
- retry_count_max: 0
- resubmit_count_max: 0
- batch_expansion: false
- credit_budget_max: 5880
- credit_floor: 560
- final_master: false
- locked: false

CAL-001-P1 does not activate CAL-001A and does not change the recorded authorization.

## 4. Fixed 7 x 4 x 3 experiment design

The requested design remains the approved P1 target:

- family_count_target: 7
- prompt_architecture_count_per_family_target: 4
- replicate_count_per_architecture_target: 3
- unique_prompt_count_target: 28
- package_count_target: 84
- manifest_row_count_target: 84

No matrix was materialized because the Source-clean precondition failed.

- family_count_created: 0
- prompt_architecture_count_created: 0
- replicate_rows_created: 0
- matrix_cells_created: 0

## 5. Fixture selection and validation

Fixture inspection did not begin. No project media was opened, scanned, altered, copied, hashed, or selected.

- fixture_registry_created: false
- fixture_count: 0
- fixture_media_scanned: false
- fixture_media_modified: false
- fixture_gap_assessment_performed: false

The seven-family fixture eligibility review must be performed only after the Source mirror is clean.

## 6. Prompt architecture design

The four requested architectures remain unmaterialized:

- P1_LEGACY_DESCRIPTIVE: not_created
- P2_RESULT_FIRST_CONCISE: not_created
- P3_RESULT_FIRST_WITH_DUTIES: not_created
- P4_RESULT_FIRST_TIMED_COMPACT: not_created

No prompt text was drafted or written.

## 7. Prompt inventory

- prompt_files_created: 0
- unique_prompt_count: 0
- prompt_inventory_sha256: not_calculated
- prompt_bytes_written: 0

## 8. Package inventory

- package_files_created: 0
- package_count: 0
- package_inventory_sha256: not_calculated
- no_submit_package_flags_written: false

No package JSON exists for CAL-001-P1.

## 9. Manifest creation and validation

- fixed_manifest_path: `experiments/CAL-001/manifests/CAL001A_fixed_84_task_manifest.csv`
- fixed_manifest_exists: false
- fixed_manifest_task_count: 0
- fixed_manifest_sha256: not_calculated
- manifest_parse_status: not_applicable
- duplicate_experiment_id_check: not_applicable
- matrix_completeness_check: not_applicable

No partial manifest was created.

## 10. Dataset schema

The following planned dataset outputs were not created:

- `experiments/CAL-001/schemas/CAL001_experiment_record.schema.json`
- `experiments/CAL-001/datasets/CAL001_experiment_results_template.csv`
- `experiments/CAL-001/datasets/CAL001_visual_review_template.jsonl`

- dataset_schema_created: false
- result_template_created: false
- visual_review_template_created: false

## 11. Scoring schema

Planned path:

`experiments/CAL-001/schemas/CAL001_scoring.schema.json`

- scoring_schema_created: false
- family_applicability_rules_created: false
- visual_scores_assigned: false

## 12. Failure-label schema

Planned path:

`experiments/CAL-001/schemas/CAL001_failure_labels.schema.json`

- failure_label_schema_created: false
- failure_labels_assigned: false
- unexpected_success_labels_assigned: false

## 13. Review artifact plan

No review artifact plan file or execution artifact was created.

- metadata_created: false
- review_frames_created: false
- contact_sheets_created: false
- cuts_created: false
- media_created: false

The proposed future frame plan remains planning input only and was not executed.

## 14. Budget plan

The authorization supplied these planning values, but no budget-plan file was created:

- user_reported_credits: 6447
- fixed_task_count_target: 84
- planned_unit_cost_assumption: 70
- planned_total_cost: 5880
- credit_floor: 560
- budget_plus_floor: 6440
- residual_against_reported_balance: 7
- live_cost_verified: false

The 70-credit value remains an unverified planning assumption and cannot activate execution.

## 15. Human review checklist

Planned path:

`experiments/CAL-001/reviews/CAL001_human_manifest_review_checklist.md`

- checklist_created: false
- human_manifest_reviewed: false
- human_manifest_accepted: false
- accepted_manifest_sha256: blank
- accepted_package_inventory_sha256: blank

## 16. Inventory hashes

- fixture_registry_sha256: not_calculated
- fixed_manifest_sha256: not_calculated
- prompt_inventory_sha256: not_calculated
- package_inventory_sha256: not_calculated
- full_experiment_inventory_sha256: not_calculated

No inventory exists to hash.

## 17. Matrix completeness validation

- expected_matrix: 7 families x 4 prompt architectures x 3 replicates
- expected_task_count: 84
- actual_task_count: 0
- unique_experiment_id_count: 0
- matrix_validation_status: not_run_blocked_before_creation
- partial_matrix_created: false

## 18. No-run and no-submit gates

- Dreamina_run: false
- Dreamina_version_run: false
- Dreamina_user_credit_run: false
- Dreamina_help_run: false
- submit_count: 0
- query_count: 0
- download_count: 0
- retry_count: 0
- resubmit_count: 0
- batch_count: 0
- execution_authority_active: false
- final_master: false
- locked: false

## 19. Source governance

Codex did not modify, stage, commit, push, delete, restore, rename, or move any file under `sources/`.

The pre-existing Source transition observed at preflight was:

```text
 D sources/AI视频制作_Source索引与使用优先级_V1.10.md
?? sources/AI视频制作_Source索引与使用优先级_V1.11.md
?? sources/AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md
```

- sources_clean: false
- sources_staged: false
- source_changes_created_by_CAL001_P1: false
- source_changes_included_in_commit: false

The human-controlled Source transition must be settled outside this phase before P1 can be rerun.

## 20. Explicit non-actions

CAL-001-P1 did not:

- run Dreamina or any Dreamina preflight/help command
- submit, query, download, retry, resubmit, or batch
- inspect or modify media fixtures
- extract frames or create contact sheets
- create prompts, packages, manifests, schemas, datasets, matrices, budget files, or review checklists
- create visual scores or perform visual approval
- modify or stage Source files
- alter CAL-001A authorization
- activate execution authority
- create CAL-001B tasks
- set `final_master=true`
- set `locked=true`
- create a tag

## 21. Risks and unresolved items

Blocking issue:

- `sources/` fails the required clean-state precondition.

Source transition requiring human settlement:

- tracked V1.10 deletion remains unstaged
- V1.11 remains untracked
- GPT5.6 routing overlay remains untracked

Nonblocking metadata debt:

- the two human-applied active files still contain candidate or pending-human-application header language

P1 must be rerun from preflight after the human completes the Source transition and `git status --short -- sources/` is empty. Fixture availability has not yet been assessed and may reveal a later independent block.

## 22. Recommended next phase

`CAL-001-P1_TRIAGE_OR_FIXTURE_PREPARATION`

Immediate action within that phase: human settlement of the active Source mirror followed by a clean-source P1 rerun. This report does not authorize Codex to stage or commit the Source transition.

## 23. Final verdict

`CAL001_P1_BLOCKED_P1_PRECONDITION_DIRTY_SOURCE_MIRROR_NO_PARTIAL_ARTIFACTS_CREATED`
