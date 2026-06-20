# PHASE K11: SHOT-02-V007 Combo Edit Review

Date: 2026-06-20

## Scope

- Record SHOT-02-V007 human review and combo edit ranking.
- Do not run Dreamina, submit, query, download, generate media, lock, or mark final master.
- Treat all combo edits and review assets as local media only; do not commit media files.

## Source Clip

- Task: SHOT-02-V007
- Source video: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V007_20260619_222501/SHOT-02-V007_preimpact_pressure_charge_motion.mp4
- sha256: e19fad647822f4e134833e6b46e20fdb9f6a266326fad5bf265d5a749c2b92bf
- duration: 4.016666666666667s
- resolution: 1280x720
- fps: 24.149377593360995
- frame_count: 97
- file_size: 10105086

## Human Review Conclusion

- status: human_review_combo_edit_ranked
- V007 is useful as a pre-impact pressure charge source.
- V007_full_clip_usable: false
- V007_preimpact_extract_usable: true
- Later portions of the full clip become too close-up / ring-like.
- Best use is a short extract before CUT03.
- V007_R01_needed: false
- further_dreamina_generation_needed_for_preimpact: false
- final_master: false
- locked: false

## V007 Preview Ranking

- preferred_preimpact_charge: SHOT-02-V007_PREVIEW_C_0p50_to_1p30
- preferred_preimpact_charge_path: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_C_0p50_to_1p30.mp4
- safe_preimpact_backup: SHOT-02-V007_PREVIEW_B_0p25_to_1p05
- safe_preimpact_backup_path: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_B_0p25_to_1p05.mp4
- too_static_backup: SHOT-02-V007_PREVIEW_A_0p00_to_0p80
- too_static_backup_path: productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_A_0p00_to_0p80.mp4

## Combo Edit Ranking

- preferred_combo_edit: C1
- preferred_combo_edit_path: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-v007-combo/SHOT-02_COMBO_TEST_C1_V007C_plus_CUT03.mp4
- preferred_combo_sha256: c4d168b5dff9454a2d0af6fa0a197693a3f0bf9b06b6c20e0ae9afbca41c9342
- preferred_combo_duration: 2.125s
- preferred_combo_reason: clear pre-impact charge followed by direct CUT03 shockwave reveal

- safe_combo_backup: B1
- safe_combo_backup_path: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-v007-combo/SHOT-02_COMBO_TEST_B1_V007B_plus_CUT03.mp4
- safe_combo_backup_sha256: 85970fb17893278dd7494f024499b10a043c8a0ad735da40ba43226e94f8a3e9
- safe_combo_backup_duration: 2.125s
- safe_combo_backup_reason: safer pre-impact lead-in, but less preferred than C1

- rejected_combo: C2
- rejected_combo_path: productions/chi_yan_tian_qiong/edits/tests/SHOT-02-v007-combo/SHOT-02_COMBO_TEST_C2_V007C_plus_TESTB.mp4
- rejected_combo_sha256: ab98b79b09835eba1281155e13ab58c196b2e6b13f65f6fa908069064da1db41
- rejected_combo_duration: 2.625s
- rejected_combo_reason: too_slow_repeated_hold

## Recommended Impact Sequence

V007_PREVIEW_C_0p50_to_1p30 followed by V006 CUT03 2p00_to_3p35.

This sequence is the current preferred SHOT-02 impact edit candidate because it gives a clear pre-impact charge and cuts directly into the CUT03 shockwave reveal.

## Next Action

- next_recommended_action: prepare SHOT-02-V008 aftershock/rain recovery planning or package
- Do not create V007-R01 now.
- Do not run additional Dreamina generation for the pre-impact beat now.

## Decision

SHOT_02_V007_COMBO_EDIT_RANKED_COMMITTED_PUSHED
