# Chi Yan Tian Qiong Production Status

current_production_status: shot_02_scene_anchor_004_locked

## Historical milestones
- scene_and_first_character_subject_locked
- core_scene_and_main_subjects_locked
- A-SC-TEMPLE-COURTYARD-001
- A-CH-A-SUBJECT-001
- A-CH-B-SUBJECT-001
- G3 Shuangji character subject readiness package
- H1 shot-01 keyframe readiness package

## Official SHOT-01 keyframe
- task_id: SHOT-01-KF-004-rerun-03
- locked_path: productions/chi_yan_tian_qiong/locked_refs/SHOT-01-KF-004-rerun-03_locked_official_shot_01_keyframe.png
- status: locked_after_human_review
- review_status: approved

## SHOT-01 video candidate
- task_id: SHOT-01-V001
- output_path: productions/chi_yan_tian_qiong/runs/live/20260616_114203_SHOT-01-V001/output/SHOT-01-V001_stable_standoff_slow_pushin.mp4
- manual_import_path: manual_imports/SHOT-01-V001_vip_web_manual_download.mp4
- submit_id: 4beb7d87-ee4d-4703-af8b-abc232425e95
- status: official_usable_video_candidate
- official_video_candidate: true
- review_status: approved
- visual verdict: pass / usable SHOT-01 establishing motion shot
- locked: false
- first usable image2video pass: complete

## SHOT-02 keyframe readiness
- task_id: SHOT-02-KF-001
- prompt_path: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-001.json
- manual_prompt_path: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-001_combat_keyframe_prompt.txt
- manifest_path: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-001.csv
- status: historical_failed_composition_example
- needs_generation: false
- locked: false
- preferred_candidate: false
- prompt_revision: human-approved revised prompt applied exactly as provided
- next_allowed_action: none; preserve as historical failed composition example only

## SHOT-02 A-grade scene reference readiness
- task_id: A-SC-TEMPLE-COURTYARD-002
- target_asset_name: A-SC-TEMPLE-COURTYARD-002_main_hall_front_combat_stage
- prompt_path: productions/chi_yan_tian_qiong/prompts/production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-002.json
- manual_prompt_path: productions/chi_yan_tian_qiong/prompts/manual_A-SC-TEMPLE-COURTYARD-002_main_hall_front_combat_stage_prompt.txt
- manifest_path: productions/chi_yan_tian_qiong/manifests/production_image2image_A-SC-TEMPLE-COURTYARD-002.csv
- superseded_manifest_path: productions/chi_yan_tian_qiong/manifests/production_text2image_A-SC-TEMPLE-COURTYARD-002.csv
- status: draft_ready
- needs_generation: true
- locked: false
- scene_policy: character_free_scene_only
- task_type: image2image
- model_version: 4.7
- ratio: 16:9
- resolution_type: 2k
- reference: A-SC-TEMPLE-COURTYARD-001 locked scene as world-continuity reference only
- next_allowed_action: human review and explicit user approval for exactly one Dreamina image2image submit

## SHOT-02 A-SC-003 failed viewpoint-correction scene reference
- task_id: A-SC-TEMPLE-COURTYARD-003
- target_asset_name: A-SC-TEMPLE-COURTYARD-003_main_hall_frontal_axis_stage
- prompt_path: productions/chi_yan_tian_qiong/prompts/production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-003.json
- manual_prompt_path: productions/chi_yan_tian_qiong/prompts/manual_A-SC-TEMPLE-COURTYARD-003_main_hall_frontal_axis_stage_prompt.txt
- manifest_path: productions/chi_yan_tian_qiong/manifests/production_image2image_A-SC-TEMPLE-COURTYARD-003.csv
- status: historical_failed_composition_example
- needs_generation: false
- locked: false
- manual_review: failed_composition_example
- failure_reason: retained oblique side-facing composition; not acceptable as true frontal-axis correction
- next_allowed_action: keep as historical failed composition example only

## SHOT-02-KF-002 keyframe package
- task_id: SHOT-02-KF-002
- prompt_path: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-002.json
- manual_prompt_path: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002_main_hall_combat_exchange_prompt.txt
- manifest_path: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-002.csv
- status: draft_ready_scene_anchor_locked
- needs_generation: true
- locked: false
- scene_anchor_policy: A-SC-TEMPLE-COURTYARD-004 only
- blocker: cleared
- scene_anchor_locked_path: productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
- staging: Shuangji cuts in from the right toward center and engages Fenshou in the main hall front mid-courtyard combat area
- recommended_preferred_scene_anchor: A-SC-TEMPLE-COURTYARD-004

## Next recommended action
- Submit SHOT-02-KF-002 only after explicit user approval for exactly one Dreamina image2image task (no batch, no auto-continue).

## SHOT-02 viewpoint-correction scene reference readiness
- task_id: A-SC-TEMPLE-COURTYARD-004
- target_asset_name: A-SC-TEMPLE-COURTYARD-004_main_hall_true_frontal_axis_stage
- prompt_path: productions/chi_yan_tian_qiong/prompts/production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-004.json
- manual_prompt_path: productions/chi_yan_tian_qiong/prompts/manual_A-SC-TEMPLE-COURTYARD-004_main_hall_true_frontal_axis_stage_prompt.txt
- manifest_path: productions/chi_yan_tian_qiong/manifests/production_text2image_A-SC-TEMPLE-COURTYARD-004.csv
- status: locked_after_human_review
- manual_review_status: approved
- needs_generation: false
- locked: true
- output_path: productions/chi_yan_tian_qiong/runs/live/20260617_150916_A-SC-TEMPLE-COURTYARD-004/output/A-SC-TEMPLE-COURTYARD-004_main_hall_true_frontal_axis_stage.png
- locked_path: productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
- preferred_for_shot02_main_hall_front: true
- reason: passes human review, preferred over A-SC-002/A-SC-003
- scene_policy: character_free_scene_only
- task_type: text2image
- model_version: 4.7
- ratio: 16:9
- resolution_type: 2k
- primary_reference: A-SC-TEMPLE-COURTYARD-001 locked scene as world-continuity reference only
- context_reference_policy: text2image package; no image2image input used
- next_allowed_action: submit SHOT-02-KF-002 only after explicit user approval for exactly one Dreamina image2image task

