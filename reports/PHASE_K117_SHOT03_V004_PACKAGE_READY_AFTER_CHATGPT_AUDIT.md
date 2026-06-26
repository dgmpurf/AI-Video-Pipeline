# PHASE K117 - SHOT-03 V004 Package Ready After ChatGPT Audit

## Purpose

This phase revises the `SHOT-03-V004` manual prompt based on ChatGPT K116 content-audit feedback and prepares a no-submit multimodal2video package.

This is not a Dreamina execution phase. No submit, query_result, download, retry, resubmit, or media generation was performed.

## Inputs Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K115_SHOT03_V004_ACTUAL_PROMPT_DRAFT_READY_FOR_CHATGPT_AUDIT.md`
- ChatGPT K116 audit instructions provided in the current user request.
- Local V003 package structure for schema continuity:
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V003_uploadsafe.json`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V003_uploadsafe.csv`
  - `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V003_uploadsafe.json`

`sources/` was not modified or staged.

## ChatGPT K116 Audit Revisions Applied

The manual prompt now explicitly records:

- Every contact beat must produce a visible body result: head/shoulder jolt, torso displacement, guard knocked open, short foot skid, brief recoil, or immediate re-entry.
- Soft push-blocking and gentle contact are forbidden.
- Any two contact beats may not be separated by more than `0.20s-0.25s` of pure adjustment, idle movement, observation, or empty footwork.
- The final `0.8s` must contain at least two clear contact beats.
- The final tail may not become defense-only, observation, pose-out, or footwork-only adjustment.
- The `2.30s-3.20s` column section forbids full circling and large side-switching.
- The column is only a brief half-body occlusion and movement line, not a route-change or breakage object.
- Railing shake/flex is allowed only when a body, forearm, or shoulder truly presses into it.
- Uncaused cracks, holes, breakage, splinters, and background structural self-damage are forbidden.
- Faces should stay in readable medium-shot `3/4` views.
- Frequent front/back face cutting and long face occlusion by arms, columns, or rain lines are forbidden.
- Fenshou and Shuangji face structure, hairstyle, and costume language must stay stable.

## Package Settings

- task_type: `multimodal2video`
- provider: `dreamina_cli`
- model_version: `seedance2.0_vip`
- duration: `5`
- ratio: `16:9`
- video_resolution: `720p`
- command_contract_valid: `true`
- submit_allowed: `false`
- query_allowed: `false`
- download_allowed: `false`
- final_master: `false`
- locked: `false`
- human_review_required_before_submit: `true`

## Active References

The V004 package uses exactly three upload-safe JPG references:

1. Fenshou identity reference:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`

2. Shuangji identity reference:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`

3. Temple scene/world reference:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

All three reference paths were checked locally and exist.

## Files Created Or Updated

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V004_uploadsafe.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K117_SHOT03_V004_PACKAGE_READY_AFTER_CHATGPT_AUDIT.md`

## Validation Results

Local validation passed:

- Prompt JSON parses.
- Shot record JSON parses.
- Manifest CSV reads.
- Manual prompt exists.
- All three active reference image paths exist.
- `task_type=multimodal2video`.
- `model_version=seedance2.0_vip`.
- `duration=5`.
- `ratio=16:9`.
- `video_resolution=720p`.
- `submit_allowed=false`.
- `query_allowed=false`.
- `download_allowed=false`.
- `final_master=false`.
- `locked=false`.
- `sources/` has no git status changes.
- No media files are part of the package.
- `.vs/` remains untracked and is not part of the package.

## Safety

- Dreamina was not run.
- No submit was performed.
- No query_result was performed.
- No download was performed.
- No retry or resubmit was performed.
- No media was created, edited, or staged.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `sources/` was not modified or staged.
- SHOT-02 / V013 / V018 lock states were not touched.
- `final_master=false`.
- `locked=false`.

## Final Verdict

`SHOT03_V004_PACKAGE_READY_AFTER_CHATGPT_AUDIT_NO_SUBMIT`
