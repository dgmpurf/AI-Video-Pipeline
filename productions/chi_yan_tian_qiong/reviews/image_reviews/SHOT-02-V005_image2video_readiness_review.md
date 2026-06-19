# SHOT-02-V005 Image2Video Readiness Review

Task: SHOT-02-V005
Shot: SHOT-02
Status: human_review_partial_success_direction_validated
Concept: spherical_rain_shockwave_reveal / strong-trigger rain shockwave with camera pull-back reveal

## Prior Attempt Review

- Prior task: SHOT-02-KF-003
- Prior status: human_review_target_miss_over_effect
- Technical validity: true
- Useful lesson: strong trigger words can produce visible spherical water/shockwave effects.
- Target miss reason: multiple water spheres; central contact reads as splash; image mixes contact moment and post-impact expansion; not suitable as clean peak keyframe for frames2video.
- Strategy change: do not use KF-003 as a video keyframe; keep the original locked SHOT-02 first-clash keyframe as the video starting image.

## Source Keyframe

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Do not use SHOT-02-KF-003 as the video-driving keyframe.

## Dreamina CLI Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 4
- duration policy: CLI-supported integer duration; seedance2.0_vip image2video supports 4-15s
- final_edit_target: 1-2s
- video_resolution: 720p
- ratio: omitted; image2video infers ratio from input image
- image input count: exactly 1
- command_contract_valid: true

## Package Intent

- Create a CLI-legal 4-second action highlight source from the official SHOT-02 keyframe.
- Final edit should use only the strongest 1-2 seconds.
- Use strong visual trigger words early: 双拳/拳掌相交, 球形冲击波, 圆形水幕, 雨水被弹开, 慢动作, 冲击力强.
- Constrain the result back to the project world: rainy ancient temple, Fenshou left, Shuangji right, central contact point, wuxia cinematic style.
- Camera holds at impact, then pulls back enough to reveal the complete spherical shockwave without losing character readability.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, wet stone courtyard, main hall door, stone steps, rain, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central fist/palm or arm contact point.
- Main effect originates from the central contact point, not the ground or feet.
- The third second reveals the complete spherical shockwave and circular water curtain.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, final_edit_target=1-2s, and command_contract_valid=true before any live submit.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V005_spherical_rain_shockwave_reveal_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V005.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V005.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V005.json
- Package report: reports/PHASE_K7_SHOT02_V005_SPHERICAL_RAIN_SHOCKWAVE_REVEAL_PACKAGE_REPORT.md

## Decision

SHOT_02_V005_PARTIAL_SUCCESS_DIRECTION_VALIDATED

## Live Submit Record

- status=success_downloaded_review_required
- submit_id=2af71f16-d097-4711-b28a-c34fb7d54e82
- logid=20260619012030169254047008249ECB1
- credit_count=56
- command_contract_valid=true
- first_query_status=querying
- query_status=success
- queue_status=Finish
- downloaded=true
- run_dir=productions/chi_yan_tian_qiong/runs/live/SHOT-02-V005_20260619_133555
- output_path=productions/chi_yan_tian_qiong/runs/live/SHOT-02-V005_20260619_133555/SHOT-02-V005_spherical_rain_shockwave_reveal_motion.mp4
- file_size=9234307
- sha256=5cefa6e995b48c4ad4e59e69774777c98da90e162c53092f688daf78fc2f5d03
- video_duration=4.016666666666667
- resolution=1280x720
- fps=24.149377593360995
- frame_count=97
- final_master=false
- locked=false
- usable_video_candidate=false
- human_review_required_after_download=true

## Human Review Result

- status=human_review_partial_success_direction_validated
- technical_valid=true
- command_contract_valid=true
- downloaded=true
- usable_reference_clip=true
- usable_video_candidate=false
- final_master=false
- locked=false
- human_review_result=partial_success_direction_validated
- success_points=spherical shockwave appears; rain/water reacts; strong-trigger prompt works; camera reveal direction partially works
- remaining_issues=shockwave too small; scale does not reach visual distance; lacks pre-impact rain-particle build-up; camera pull-back not strong enough; shockwave edge does not sweep past camera foreground
- lesson_learned=strong trigger words should remain, but V006 must add pre-impact particle build-up and larger camera pull-back reveal
- next_recommended_task=SHOT-02-V006_giant_rain_shockwave_lens_pass
