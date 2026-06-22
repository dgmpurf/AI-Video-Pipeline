# PHASE K33 Shuangji Identity Anchor Package Ready

Date: 2026-06-22

## Scope

Prepare a text-only `image2image` package for:

`A-CH-B-IDENTITY-002_shuangji_female_face_upper_body_identity_anchor`

No Dreamina command was run in this phase.

## Why This Identity Anchor Is Needed

`SHOT-02-V010` and `SHOT-02-V011` both failed Shuangji identity stability. V011 used all intended references, but human review still found Shuangji male-coded / male-cultivator-like.

The current failure is an identity anchoring and model reference-following problem, not a missing-submit-reference problem.

The asset registry currently has only the locked Shuangji full-body subject reference:

- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`

No stronger Shuangji face, upper-body, or portrait locked reference was found in the current registry.

## Why Direct V012 Video Is Blocked For Now

Repeating `multimodal2video` with the same full-body Shuangji reference may repeat the V011 identity drift.

V010 and V011 frames should not be reused as identity references because they contain contaminated identity evidence:

- male-coded Shuangji drift
- soft or blurred face details
- slow staged sparring rhythm
- pose-to-pose arm-lock motion

The safer path is to create and review a stronger Shuangji identity anchor first, then prepare V012 video only after human approval.

## Why Image2Image From A-CH-B-SUBJECT-001 Is Recommended

The existing full-body Shuangji subject reference is already locked after human review, so it remains the safest known identity source.

`image2image` is recommended because the task is not to invent a new character. The task is to convert the existing approved Shuangji subject into a clearer face / upper-body identity anchor with:

- stronger facial readability
- preserved silver-blue high ponytail
- preserved blue-silver armor collar and shoulder structure
- preserved white-blue robe panels
- unmistakably female identity
- simple neutral background suitable for future video identity reference

## Package Settings

- logical_id: `A-CH-B-IDENTITY-002`
- candidate_id: `A-CH-B-IDENTITY-002-R01`
- asset_type: `image`
- role: `character_identity_anchor`
- status: `package_ready_no_submit`
- review_status: `pending`
- provider: `dreamina_cli`
- task_type: `image2image`
- model_version: `4.7`
- ratio: `9:16`
- resolution_type: `2k`
- final_master: `false`
- locked: `false`

Ratio choice:

`9:16` is selected because the source is a vertical full-body character subject and the target is a vertical upper-body / portrait identity anchor.

## Full Input Reference Path

`productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`

Reference duty:

Use as the sole identity source. Preserve Shuangji identity, female face, silver-blue high ponytail, blue-silver armor collar / shoulder structure, white-blue robe panels, and restrained wuxia temperament. Do not copy background, full-body pose, or foot-level framing.

## Package Output Paths

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_A-CH-B-IDENTITY-002_shuangji_female_face_upper_body_identity_anchor_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/A-CH-B-IDENTITY-002_shuangji_identity_anchor_prompt.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_image2image_A-CH-B-IDENTITY-002.csv`
- Asset planning record: `productions/chi_yan_tian_qiong/assets/A-CH-B-IDENTITY-002_planning_record.json`
- Package report: `reports/PHASE_K33_SHUANGJI_IDENTITY_ANCHOR_PACKAGE_READY.md`

## Manual Prompt

```text
参考图是唯一身份来源，只用于霜玑的身份、脸部特征、发型、服装结构和气质。不参考参考图的背景、全身站姿、脚部构图或原始镜头比例。

请将霜玑转换并重构为一张更清晰的上半身/肖像身份锚定图。画面使用纯白色或简单中性背景，半写实3D武侠电影质感，重点是脸、发型、肩颈、护甲领口、肩部结构、上身白蓝长袍衣片和女性身份稳定性。

霜玑必须是明确女性角色，脸部清晰、冷静、柔和但锐利，银蓝色高马尾，蓝银色护甲领口和肩部结构，白蓝色长袍衣片，身形纤细优雅，有冷静、敏捷、克制的武侠气质。整体应适合作为未来视频生成中的角色身份参考图，面部可读性强，身份特征稳定。

不要男性化脸，不要生成男性修士，不要变成泛白发男修，不要胡子，不要粗重男性下颌，不要厚重男性眉骨，不要宽厚男性躯干，不要战斗动作，不要武器，不要复杂古寺背景，不要使用V010或V011的错误身份倾向，不要多人，不要重复角色，不要双身体，不要多余肢体，不要文字水印。
```

## Command Preview Only

Do not run this command until explicit live-submit approval is given:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_A-CH-B-IDENTITY-002_shuangji_female_face_upper_body_identity_anchor_prompt.txt"
dreamina image2image `
  --images "productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio 9:16 `
  --resolution_type 2k `
  --poll 0
```

## Expected Future Use In V012

If this identity anchor passes human review, use it as the highest-priority Shuangji identity reference in a later SHOT-02-V012 video package.

Expected V012 reference strategy after approval:

- Fenshou locked subject reference for Fenshou identity.
- `A-CH-B-IDENTITY-002` for Shuangji face / upper-body identity protection.
- Clean locked temple scene anchor for world and frontal-axis continuity.
- Avoid V010/V011 frames because they reinforce wrong identity and slow rhythm.

## Boundary Confirmation

- Dreamina was not run.
- No submit was run.
- No query_result was run.
- No download was run.
- No media was generated.
- No runtime code was modified.
- `configs/providers.json` was not modified.
- `final_master=false`
- `locked=false`
- Human review is required before this asset can be locked or used as a production identity anchor.

Final verdict: `SHUANGJI_IDENTITY_ANCHOR_PACKAGE_READY_NO_SUBMIT`
