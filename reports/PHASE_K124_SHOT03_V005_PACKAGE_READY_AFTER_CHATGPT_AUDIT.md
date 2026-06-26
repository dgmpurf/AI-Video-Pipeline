# PHASE K124 - SHOT-03 V005 Package Ready After ChatGPT Audit

## Purpose

Revise the SHOT-03 V005 terrain-affordance prompt after ChatGPT K123 audit and prepare a no-submit `multimodal2video` package.

This is not a Dreamina execution phase. No submit, query_result, download, retry, resubmit, or media generation was performed.

## Sources and Reports Inspected

Available files inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K122_SHOT03_V005_TERRAIN_AFFORDANCE_PROMPT_DRAFT_READY_FOR_CHATGPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V005_uploadsafe_terrain_rebound_attack_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K121_SHOT03_V004_HUMAN_REVIEW_AND_V005_TERRAIN_AFFORDANCE_DIRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K117_SHOT03_V004_PACKAGE_READY_AFTER_CHATGPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V004_uploadsafe.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.5.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`

`sources/` was used as read-only reference material only. No file under `sources/` was created, modified, deleted, moved, renamed, or staged.

## K123 Audit Patches Applied

ChatGPT K123 result:

`SHOT03_V005_PROMPT_AUDIT_PASS_WITH_MINOR_PATCH_REQUIRED`

Applied revisions:

- Terrain anchor narrowed from broad alternatives to `wet round column base / column foot beside exterior corridor pillar`.
- Attack action narrowed from broad alternatives to `right forearm with hammerfist-like downward smash`.
- First contact timing clarified:
  - `0.00s-0.12s`: already close range, arms driving in, no pose/setup.
  - `0.12s-0.28s`: first clear hard contact occurs.
- Camera angle clarified:
  - medium / medium-wide framing.
  - slight exterior-corridor diagonal angle toward courtyard.
  - not fully parallel side-on and not side-scroller.
- Existing constraints preserved:
  - one stable exterior corridor / column / railing / wet stone zone.
  - one terrain-assisted attack only.
  - no roof.
  - no full wall-run.
  - no floating.
  - no structural breakage.
  - no smoke-hole suspense.
  - at least 6 clear contact beats.
  - final 0.8s contains at least two contact beats.
  - final frame cuts mid-exchange.
  - Fenshou identity stable.
  - Shuangji female identity stable.

## Package Settings

- task_type: `multimodal2video`
- provider: `dreamina_cli`
- model_version: `seedance2.0_vip`
- duration: `5`
- ratio: `16:9`
- video_resolution: `720p`
- submit_allowed: `false`
- query_allowed: `false`
- download_allowed: `false`
- final_master: `false`
- locked: `false`
- human_review_required_before_submit: `true`

## Active References

The V005 package uses exactly the same three upload-safe JPG references as V004.

1. Fenshou identity reference:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
   Exists: true

2. Shuangji identity reference:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
   Exists: true

3. Temple scene/world reference:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`
   Exists: true

Reference duties:

- `@FENSHOU_UPLOADSAFE`: Fenshou identity only.
- `@SHUANGJI_UPLOADSAFE`: highest-priority Shuangji female identity protection only.
- `@TEMPLE_SCENE_UPLOADSAFE`: rainy temple exterior corridor world only.

## Validation Results

Local validation passed:

- Prompt JSON parses.
- Shot record JSON parses.
- Manifest CSV reads.
- Manifest CSV contains exactly 1 row.
- `task_type=multimodal2video`.
- `model_version=seedance2.0_vip`.
- `duration=5`.
- `ratio=16:9`.
- `video_resolution=720p`.
- All three active reference image paths exist.
- `submit_allowed=false`.
- `query_allowed=false`.
- `download_allowed=false`.
- `final_master=false`.
- `locked=false`.
- No media files were created.
- `sources/` has no git status changes.

## Files Created or Updated

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V005_uploadsafe_terrain_rebound_attack_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V005_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V005_uploadsafe.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V005_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K124_SHOT03_V005_PACKAGE_READY_AFTER_CHATGPT_AUDIT.md`

## Safety

- Dreamina was not run.
- No submit, query_result, download, retry, or resubmit was run.
- No media was created, edited, or staged.
- `sources/` was not modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- `final_master=false`.
- `locked=false`.
- SHOT-02 / V013 / V018 / V004 lock states were not touched.

## Next Step

Human submit authorization is required before K125. Do not run canary, preflight, submit, query_result, or download without explicit human approval for that exact phase.

## Final Verdict

SHOT03_V005_PACKAGE_READY_AFTER_CHATGPT_AUDIT_NO_SUBMIT
