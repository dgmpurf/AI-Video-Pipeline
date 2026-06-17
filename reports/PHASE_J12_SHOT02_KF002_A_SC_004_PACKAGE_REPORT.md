# PHASE J12: SHOT-02-KF-002 A-SC-004 Package Report

Date: 2026-06-17

## Scope

- Prepare the SHOT-02-KF-002 image2image package only.
- Use locked A-SC-TEMPLE-COURTYARD-004 as the official SHOT-02 scene anchor.
- Do not submit, query, download, batch, auto-continue, or generate media.
- Do not modify runtime code, providers config, or source files.

## Source Read Status

Read required sources (all present):

- sources/AI瑙嗛鍒朵綔_瀹炴祴瑙勫垯搴揰V1.2_鍔ㄤ綔鍙樿韩杩愰暅澧炶ˉ绋?md
- sources/AI瑙嗛鍒朵綔_瀹炴祴瑙勫垯搴揰V1.9_绌洪棿璋冨害涓庤繙杩戠珯浣嶆帶鍒禵瀹屾暣鐗坃V1_9_2.md
- sources/AI瑙嗛鍒朵綔_瀹炴祴瑙勫垯搴揰V1.10_瑙嗚绾犲亸涓庡満鏅敋鐐归噸鏋勫琛ョ.md
- sources/Dreamina_CLI宸ヤ綔娴佷笌鎵ц瑙勮寖_V1.1_瀹樻柟Help鏍℃鐗?md
- sources/DreaminaBatcher_manifest_schema_V1.1_瀹樻柟Help鏍℃鐗?md
- sources/dreamina_cli_help.md
- sources/AI视频制作_Source索引与使用优先级_V1.2.md
- sources/AI视频制作_实测规则库_V1.10.1_视角重构短硬Prompt地图风格与CTRL_CAM补丁.md

No requested source files are missing locally at this re-audit time.
## Locked References

- Scene anchor: productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
- Fenshou: productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
- Shuangji: productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png

## Dreamina Settings

- task_type: image2image
- provider: dreamina_cli
- model_version: 4.7
- ratio: 16:9
- resolution_type: 2k
- poll: 0 when submitted later

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002_main_hall_combat_exchange_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-002.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-002.csv
- Shot record: productions/chi_yan_tian_qiong/shots/shot_02_keyframe_record_SHOT-02-KF-002.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-KF-002_readiness_review.md

## Risk Notes

- All requested source files were present locally during re-audit.
- The package relies on three media references that remain ignored by git by default.
- Later execution must use repeated image2image --images arguments, not image2video --image.
- Later execution must be one explicit task only, with no batch, no auto-continue, and no download/query in the same step.
- The main visual risk is reverting to a flat side-scroller duel, poster pose, or static distant standoff.
- The anatomical risk is duplicated characters, fused bodies, extra limbs, or unreadable close-contact overlap.

## Later Command Preview

Do not run this command until explicit live-submit approval is given:

```powershell
$prompt = Get-Content -Raw "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002_main_hall_combat_exchange_prompt.txt"
dreamina image2image `
  --images "productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png" `
  --images "productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" `
  --images "productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio 16:9 `
  --resolution_type 2k `
  --poll 0
```

## Decision

SHOT_02_KF_002_PACKAGE_READY_NO_SUBMIT

