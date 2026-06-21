# PHASE_K23_SHOT02_V010_PROMPT_REVISION_READY_FOR_SUBMIT

- project: Chi Yan Tian Qiong
- shot: SHOT-02
- task_id: SHOT-02-V010
- status: planning_only_no_submit
- revision_status: prompt_revised_ready_for_canary_and_submit_review
- final_master: false
- locked: false

## Human Review Input

Human reviewed the V010 start frame and prompt.

Approved start frame:

- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg`

Human feedback:

- The start frame is usable.
- The previous V010 direction is correct, but the timing is too soft and regular.
- The action must begin immediately from the first frame.
- Avoid the old issue where camera pulls back while both fighters remain static/frozen.
- Camera pullback should be minimized or avoided.
- Characters must continue moving with visible footwork, forearm contact, shoulder/hip adjustment, clothing/hair motion, and wet-floor feedback.
- Final approval still requires human review after any future generation.

## Revision Summary

The V010 prompt was revised to:

- begin motion immediately on frame one
- use explicit timing windows: 0.0-0.6s, 0.6-1.6s, 1.6-2.6s, 2.6-4.0s
- minimize camera pullback and preserve the frontal-axis mid-wide view
- require continuous fighter motion during the full clip
- emphasize grounded footwork, forearm contact, shoulder/hip/arm mechanics, clothing/hair motion, and wet-floor splashes
- preserve no-submit, no-lock, and no-final-master status

## Current Package Files

- manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V010_followup_forearm_clash_sidestep_counter_prompt.txt`
- prompt json: `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V010.json`
- manifest: `productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V010.csv`
- shot record: `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V010.json`
- original planning report: `reports/PHASE_K22_SHOT02_V010_FOLLOWUP_ATTACK_PLANNING.md`

## Execution Boundary

Do not submit from this report alone. Next live step requires explicit user approval, Dreamina canary if requested by the workflow, and command-contract preflight.

Final package state:

- status: planning_only_no_submit
- final_master: false
- locked: false
- submitted: false
- queried: false
- downloaded: false

