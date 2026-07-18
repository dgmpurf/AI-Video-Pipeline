# CAL-001 P3B-R2-T3A F01 Visual Review and Remaining-Canary Readiness Result

## 1. Phase summary

- executed: true
- status: `F01_visual_review_recorded_remaining_six_family_ready_for_separate_authorization`
- starting_head: `aaa7c93c7dcb207eae08b61196a24a0e2558b9fe`
- experiment_id: `CAL001-F01-P2-R1`
- technical_success_verified: true
- human_review_status: `reviewed`
- dataset_human_review_status: `completed` (the existing schema-equivalent value for `reviewed`)
- experiment_validity_class: `B_VALID_FAILURE_USABLE_FOR_PROMPT_ARCHITECTURE_COMPARISON`
- candidate_status: `usable_with_caveats`
- prompt_goal_match: 3
- action_readability: 2
- temporal_coherence: 5
- style_coherence: 5
- editability: 4
- primary_failure_label: `action_result_underpowered`
- secondary_failure_labels: `slow_action_progression`, `insufficient_final_state_reveal`, `low_motion_variation`, `weak_dramatic_endpoint`, `long_static_tail`
- best_usable_window: `0.0s-1.5s`
- systemic_issue_found: false
- safe_to_continue_remaining_technical_canary: true, subject to separate explicit English authorization
- remaining_six_family_ids: `CAL001-F02-P2-R1`, `CAL001-F03-P2-R1`, `CAL001-F04-P2-R1`, `CAL001-F05-P2-R1`, `CAL001-F06-P2-R1`, `CAL001-F07-P2-R1`
- remaining_six_family_authorized: false
- execution_authority_active: false
- visual_scores_assigned: true
- final_master: false
- locked: false
- sources_clean: true
- accepted_artifacts_unchanged: true
- recommended_next_phase: `CAL-001-P3B-R2-T4_REMAINING_SIX_FAMILY_CANARY_AUTHORIZATION`
- final_verdict: `CAL001_P3B_R2_F01_VALID_FAILURE_RECORDED_REMAINING_SIX_FAMILY_READY_SEPARATE_AUTHORIZATION`

T3A records the completed human visual review. It performs no live operation and grants no authority to execute the remaining six fixed canary tasks.

## 2. Starting checkpoint

- required branch: `main`
- observed branch: `main`
- required local HEAD and `origin/main`: `aaa7c93c7dcb207eae08b61196a24a0e2558b9fe`
- observed local HEAD: `aaa7c93c7dcb207eae08b61196a24a0e2558b9fe`
- observed `origin/main`: `aaa7c93c7dcb207eae08b61196a24a0e2558b9fe`
- local/origin aligned: true
- staged files before T3A: none
- unrelated tracked modifications before T3A: none
- `sources/` clean: true

Known untracked workspace noise and local T2 evidence remained outside the mutation and staging scope.

## 3. T2 technical evidence verification

Verified report: `reports/PHASE_CAL001_P3B_R2_T2_EXISTING_F01_QUERY_DOWNLOAD_RECOVERY_RESULT.md`

- required T2 verdict matched: `CAL001_P3B_R2_F01_EXISTING_TASK_RECOVERED_READY_VISUAL_REVIEW_AND_REMAINING_CANARY_DECISION`
- submit_id: `4e4588dd-a0e1-4539-8390-692cb9bf80f8`
- logid: `20260718154849169254047008489C358`
- final_gen_status: `success`
- result_image_count: 0
- result_video_count: 1
- download_count: 1
- media_validation_pass: true
- actual_credit_cost: 70
- pre-T3A human review state: `unreviewed`, represented as `not_started` in the dataset schema
- pre-T3A visual scores assigned: false
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- final_master: false
- locked: false

The source MP4 remains at `experiments/CAL-001/runs/CAL001-F01-P2-R1/4e4588dd-a0e1-4539-8390-692cb9bf80f8_video_1.mp4`. Its current SHA256 is `df0199aaee019b1b39e64419248a6247a8fec742751f83ab3764b10ce6a915a8`, matching T2. This technical success is not itself a visual-success claim.

## 4. Human visual-review input

- reviewer: `human_user_with_ChatGPT_Pro_assisted_visual_analysis`
- review_date: `2026-07-18`
- classification: `B_VALID_FAILURE_USABLE_FOR_PROMPT_ARCHITECTURE_COMPARISON`
- candidate_status: `usable_with_caveats`

Human Chinese review summary:

> 雨夜要塞环境中，一名红色斗篷人物持续推动一扇巨大的城门。主体、场景和电影化风格稳定，推门动作确实发生，但动作推进缓慢，最终状态揭示和戏剧结果不足。

## 5. Score rationale

| Dimension | Score | Rationale |
| --- | ---: | --- |
| prompt_goal_match | 3 | The output preserves one red-caped subject, a dark rainy cinematic world, and a continuous pushing action, but substitutes a massive gate for the requested observatory shutter and underdelivers the fully closed endpoint. |
| action_readability | 2 | The push is visible and understandable, but progression is slow, intensity is low, and the action result remains underpowered. |
| temporal_coherence | 5 | Subject, environment, and motion remain temporally stable without a major jump, dissolve failure, or structural break. |
| style_coherence | 5 | The rainy fortress world, lighting, and cinematic rendering remain coherent throughout. |
| editability | 4 | The early 0.0-1.5 second interval is usable, although the later repetitive/static tail weakens the complete five-second output. |

The nine F01 non-applicable scoring dimensions remain null rather than being assigned artificial zero values.

## 6. Dominant visible result

Exact recorded result:

> A hooded figure in a dark rainy fortress environment slowly pushes open a massive gate.

## 7. Subject and world stability

- subject_clear: true
- subject_stable: true
- unrelated_subject_present: false
- identity_or_structure_drift: false
- world_coherent: true
- style_coherent: true
- lighting_coherent: true
- environment_continuity: true

## 8. Action readability and strength

- action_exists: true
- action_readable: true
- action_intensity: `low`
- action_result_strength: `underpowered`
- static_image_only: false

The action is judgeable, but its progression and endpoint are too weak for a full prompt-goal pass.

## 9. Temporal and style coherence

- major_jump: false
- dissolve_failure: false
- major_structure_drift: false
- temporal_coherence: 5
- style_coherence: 5
- long_static_tail: true

The sample is coherent rather than broken. Its principal weakness is insufficient action development, not temporal or stylistic instability.

## 10. Best and weak time windows

- best usable window: 0.0s to 1.5s
- weak/repetitive window: 2.5s to 5.0s

The early interval contains the clearest usable motion. The latter half has low variation and a long static tail.

## 11. Failure labels

- primary: `action_result_underpowered`
- secondary: `slow_action_progression`
- secondary: `insufficient_final_state_reveal`
- secondary: `low_motion_variation`
- secondary: `weak_dramatic_endpoint`
- secondary: `long_static_tail`
- systemic_issue_found: false

## 12. Validity classification

`B_VALID_FAILURE_USABLE_FOR_PROMPT_ARCHITECTURE_COMPARISON` means the experiment and provider execution are valid, the visible result is coherent and judgeable, and the sample remains useful calibration evidence even though it fails to deliver a strong action endpoint. It is neither an invalid experiment nor evidence of a systemic platform failure.

This classification does not claim production-shot acceptance, final quality, a family winner, or a globally best Prompt architecture.

## 13. Dataset updates

Updated only `CAL001-F01-P2-R1` in:

- `experiments/CAL-001/datasets/CAL001_experiment_results_template.csv`
- `experiments/CAL-001/datasets/CAL001_visual_review_template.jsonl`

Both rows now contain the five applicable scores, exact dominant result, primary and secondary diagnostic labels, `0.0s-1.5s` best window, `usable_with_caveats`, and completed human-review state. All submit/query/download/media fields in the CSV were preserved.

The fixed schema enumerates `completed`, not `reviewed`, so the datasets use `human_review_status=completed` as the schema-equivalent representation of the exact human state `reviewed`. The datasets do not have an `experiment_validity_class` property; changing their schema is outside T3A authority. The exact value is therefore retained as `experiment_validity_class=B_VALID_FAILURE_USABLE_FOR_PROMPT_ARCHITECTURE_COMPARISON` in the existing `reviewer_notes` field and as a structured field in the dedicated review record.

CSV parsing and all 84 JSONL-line parses are validated independently. Score ranges, F01 applicable/null dimensions, review-status and candidate-status enums, ID uniqueness, row count, and CSV/JSONL ID alignment pass. The exact human diagnostic failure labels are preserved as supplied; T3A does not modify or claim expansion of the separate accepted controlled-label taxonomy schema.

- dataset rows updated: 1 (`CAL001-F01-P2-R1`)
- other dataset rows changed: 0
- family_winner: false/unset
- global_template_candidate: false/unset
- final_master: false
- locked: false

## 14. Remaining-six-family readiness

- remaining_six_family_canary_ready_for_human_authorization: true
- remaining fixed IDs: `CAL001-F02-P2-R1`, `CAL001-F03-P2-R1`, `CAL001-F04-P2-R1`, `CAL001-F05-P2-R1`, `CAL001-F06-P2-R1`, `CAL001-F07-P2-R1`
- earlier F01 submit count: 1
- earlier F01 actual cost: 70
- remaining canary submit maximum: 6
- remaining canary credit maximum: 420
- total CAL-001A submit maximum: 84
- total CAL-001A credit budget: 5880
- credit floor: 560
- retry maximum: 0
- resubmit maximum: 0

Readiness is a decision-gate result only. None of the six tasks is authorized or executed by T3A.

## 15. Authority state

- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- CAL001B_authorized: false
- remaining canary requires separate explicit English authorization: true
- final_master: false
- locked: false

## 16. Source and media boundary

- `sources/` clean: true
- Source files modified: false
- media modified, copied, staged, or committed: false
- accepted fixed manifest SHA256: `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d`
- accepted fixture registry SHA256: `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142`
- accepted prompt inventory SHA256: `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d`
- accepted package inventory SHA256: `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c`
- accepted full experiment inventory SHA256: `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138`
- H1 acceptance record SHA256: `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7`
- human checklist SHA256: `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3`
- accepted_artifacts_unchanged: true

## 17. Explicit non-actions

- Dreamina run: false
- submit: false
- query: false
- download: false
- F02-F07 execution: false
- retry: false
- resubmit: false
- Prompt rewrite: false
- manifest/package/fixture modification: false
- Source modification: false
- accepted aggregate input modification: false
- H1/prior execution/prior report modification: false
- media modification or staging: false
- family winner selection: false
- global Prompt architecture selection: false
- final_master set true: false
- locked set true: false
- tag: false

## 18. Recommended next phase

`CAL-001-P3B-R2-T4_REMAINING_SIX_FAMILY_CANARY_AUTHORIZATION`

That phase must be a separate explicit English human authorization decision. T3A itself leaves all live authority closed.

## 19. Final verdict

- status: `F01_visual_review_recorded_remaining_six_family_ready_for_separate_authorization`
- final_verdict: `CAL001_P3B_R2_F01_VALID_FAILURE_RECORDED_REMAINING_SIX_FAMILY_READY_SEPARATE_AUTHORIZATION`
- technical_success_verified: true
- human_review_status: `reviewed`
- experiment_validity_class: `B_VALID_FAILURE_USABLE_FOR_PROMPT_ARCHITECTURE_COMPARISON`
- remaining_six_family_canary_ready_for_human_authorization: true
- remaining_six_family_authorized: false
- execution_authority_active: false
- final_master: false
- locked: false
