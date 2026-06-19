# SHOT-02-V006 Image2Video Readiness Review

Task: SHOT-02-V006
Shot: SHOT-02
Status: human_review_impact_edit_tests_ranked
Concept: giant_rain_shockwave_lens_pass / large spherical shockwave pull-back reveal / rain curtain sweeps past camera

## Prior Attempt Review

- Prior task: SHOT-02-V005
- Prior status: human_review_partial_success_direction_validated
- Technical validity: true
- Useful direction: visible spherical shockwave, rain/water reaction, strong-trigger prompt works, camera reveal direction partially works.
- Remaining issues: shockwave too small; scale does not reach visual distance; lacks pre-impact rain-particle build-up; camera pull-back not strong enough; shockwave edge does not sweep past camera foreground.
- Strategy change: keep strong trigger words, add pre-impact particle build-up, larger shockwave scale, stronger pull-back reveal, and lens-foreground rain curtain pass.

## Source Keyframe

- Input image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Use the original locked SHOT-02 first-clash keyframe as the clean start.

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
- Show pre-impact rain-line bending and suspended particle build-up before the shockwave.
- Make the shockwave much larger than V005 and reveal it with a faster pull-back.
- Make the outer shockwave edge sweep past the camera foreground like a rain curtain.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve frontal main-hall axis, wet stone courtyard, main hall door, stone steps, rain, and reflections.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central fist/palm or arm contact point.
- Main effect originates from the central contact point, not the ground or feet.
- Shockwave scale should expand toward frame edges and foreground lens edge.
- Do not use ratio for image2video.
- Confirm duration=4, exactly one input image, final_edit_target=1-2s, and command_contract_valid=true before any live submit.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V006_giant_rain_shockwave_lens_pass_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V006.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V006.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V006.json
- Package report: reports/PHASE_K8_SHOT02_V006_GIANT_RAIN_SHOCKWAVE_LENS_PASS_PACKAGE_REPORT.md

## Decision

SHOT_02_IMPACT_EDIT_TESTS_RANKED

## Live Submit Record

- status=success_downloaded_review_required
- submit_id=44bcdf99-97c9-4d62-b47d-4c623f920b91
- logid=20260619145824169254047008114EAC2
- credit_count=56
- command_contract_preflight=pass
- command_contract_valid=true
- first_query_status=querying
- query_status=success
- queue_status=Finish
- downloaded=true
- run_dir=productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923
- output_path=productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923/SHOT-02-V006_giant_rain_shockwave_lens_pass_motion.mp4
- file_size=8222075
- sha256=959fe1aeea02ce2954a5a3735010609292382a031826996bffa0ae739b20a236
- video_duration=4.016666666666667
- resolution=1280x720
- fps=24.149377593360995
- frame_count=97
- final_master=false
- locked=false
- usable_video_candidate=false
- human_review_required_after_download=true

## Human Review Impact Edit Tests

- status=human_review_impact_edit_tests_ranked
- human_review_result=impact_edit_tests_ranked
- source_video_path=productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923/SHOT-02-V006_giant_rain_shockwave_lens_pass_motion.mp4
- full_clip_usable=false
- usable_video_candidate=false
- extract_candidate=true
- final_master=false
- locked=false
- recommended_extract_cut01=2.00s-4.00s
- recommended_extract_cut02=2.00s-3.50s
- recommended_extract_cut03=2.00s-3.35s
- CUT01 role=long_full_shockwave_backup
- CUT02 role=tight_impact_extract_candidate
- CUT03 role=preferred_full_shockwave_short_extract_candidate
- preferred_extract=CUT03
- preferred_extract_path=productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4
- recommended_edit_structure=0.50s contact/hit-stop beat followed by CUT03 shockwave reveal
- TEST_A role=fast_impact_backup
- TEST_A path=productions/chi_yan_tian_qiong/edits/tests/SHOT-02-impact-cut/SHOT-02_IMPACT_TEST_A_0p35s_hold_plus_CUT03.mp4
- TEST_B role=preferred_impact_edit_candidate
- TEST_B path=productions/chi_yan_tian_qiong/edits/tests/SHOT-02-impact-cut/SHOT-02_IMPACT_TEST_B_0p50s_hold_plus_CUT03.mp4
- preferred_impact_edit=TEST_B
- preferred_impact_edit_path=productions/chi_yan_tian_qiong/edits/tests/SHOT-02-impact-cut/SHOT-02_IMPACT_TEST_B_0p50s_hold_plus_CUT03.mp4
- backup_impact_edit_path=productions/chi_yan_tian_qiong/edits/tests/SHOT-02-impact-cut/SHOT-02_IMPACT_TEST_A_0p35s_hold_plus_CUT03.mp4
- optional_later_refinement=0.42s contact hold may be tested during final edit if 0.50s feels slightly long after sound design
- further_dreamina_generation_needed=false
- next_recommended_action=prepare short contact/hit-stop beat if needed; otherwise preserve CUT03 as current SHOT-02 shockwave highlight candidate
- next_review_required=none
- success_points=large shockwave reveal after 2.0s; wide rain curtain; camera pull-back reveal works
- remaining_issues=front section looks like water spraying from fists; pre-impact particle build-up not convincing; full 4s clip too slow
- recommended_current_use=prefer CUT02 for fast impact edit; CUT01/CUT03 for larger shockwave reveal

## Local Extract Validation

- CUT01 path=productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT01_2p00_to_4p00_giant_shockwave_extract.mp4
- CUT01 exists=true
- CUT01 file_size=1765998
- CUT01 sha256=fa66ad03e359e017e72d4ad1e9a605807d525ecf0904c60291d9ac2e1a204eb3
- CUT01 duration=2.028985507246377
- CUT01 resolution=1280x720
- CUT01 fps=24.15
- CUT01 frame_count=49
- CUT02 path=productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT02_2p00_to_3p50_tight_shockwave_extract.mp4
- CUT02 exists=true
- CUT02 file_size=1301713
- CUT02 sha256=121b16c364c91b71ce3ce07fb47c7b7dca9fe339e66d004376ef62d52c18e059
- CUT02 duration=1.5320910973084887
- CUT02 resolution=1280x720
- CUT02 fps=24.15
- CUT02 frame_count=37
- CUT03 path=productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4
- CUT03 exists=true
- CUT03 file_size=1082032
- CUT03 sha256=bbffd3551e84c54cad210674d6bb1b03f07d649e55d7f698684c94cb24702a6b
- CUT03 duration=1.3250517598343685
- CUT03 resolution=1280x720
- CUT03 fps=24.15
- CUT03 frame_count=32
