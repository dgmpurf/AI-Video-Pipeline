# PHASE K32 SHOT-02 V012 Identity-First Correction Plan

Date: 2026-06-22

## Scope

- Prepare a planning-only correction plan for `SHOT-02-V012`.
- Do not run Dreamina.
- Do not submit, query, download, retry, resubmit, or batch.
- Do not create a V012 live package in this phase.
- Do not mark any asset or shot as final master or locked.

Final approval still requires human review.

## Files Inspected

- `reports/PHASE_K31_SHOT02_V011_HUMAN_REVIEW_AND_V012_DIRECTION.md`
- `reports/PHASE_K30_SHOT02_V011_QUERY_DOWNLOAD_RESULT.md`
- `reports/PHASE_K29_SHOT02_V011_SINGLE_SUBMIT_RESULT.md`
- `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V011.json`
- `productions/chi_yan_tian_qiong/assets/asset_registry.json`
- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`

## Current Diagnosis

`SHOT-02-V010` failed because Shuangji identity became unstable and gender drift appeared in the video result.

`SHOT-02-V011` was technically submitted with the intended multimodal reference set, including:

- locked Fenshou full-body subject reference
- locked Shuangji full-body subject reference
- V009 1.00s scene/action continuity frame
- V010 frame_06 as loose action/composition reference
- locked temple scene anchor

V011 still failed human review. Shuangji continued to read male-coded / male-cultivator-like, and the fight rhythm remained too slow and staged.

This is therefore diagnosed as an identity anchoring and model reference-following failure, not a missing-reference or submit-command mismatch.

The asset registry currently contains the locked Shuangji full-body subject reference:

- logical_id: `A-CH-B-SUBJECT-001`
- path: `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`

No stronger Shuangji face, upper-body, or portrait locked reference was found in the current registry.

## Why Direct V012 Video Is Not Recommended Yet

Another direct `multimodal2video` attempt using the same full-body Shuangji reference is likely to repeat the same identity drift.

V010 and V011 frames should not be reused as identity or visual references because they carry contaminated evidence:

- male-coded Shuangji drift
- soft or blurred identity details
- slow staged sparring rhythm
- static arm-lock / performance-combat feel

V009 1.00s may be useful only as loose scene continuity, but it should not be treated as an identity anchor. If it continues to soften character identity, it should be omitted from V012.

The safer next move is to first create or select a stronger Shuangji identity anchor, then use that anchor in a later V012 video package.

## Proposed New Identity Asset

Suggested logical_id:

`A-CH-B-IDENTITY-002`

Suggested concept name:

`shuangji_female_face_upper_body_identity_anchor`

Purpose:

- identity anchor only
- not an action shot
- not final video material
- not a locked asset until human review approves it

Recommended visual target:

- white or simple neutral background
- clear female face
- silver-blue high ponytail
- blue-silver armor collar and shoulder structure
- white-blue robe panels
- calm sharp expression
- elegant, unmistakably female martial character
- clean upper-body / portrait framing with strong facial readability

Avoid:

- male-coded face
- generic white-haired male cultivator
- beard or facial hair
- masculine jaw
- heavy male brow
- broad male torso
- extra characters
- weapons
- text or watermark

## Draft Chinese Prompt For Identity Asset

Use this only if an image identity-anchor generation or image2image-refinement task is later approved. Do not submit from this report.

If using image2image later, use `A-CH-B-SUBJECT-001` as the sole identity source.

```text
参考图只用于霜玑的身份、发型、服装和气质，不参考动作、背景或构图。生成一张霜玑的清晰上半身身份锚定图，白色或简单中性背景，半写实3D武侠电影质感。

霜玑必须是明确女性角色，脸部清晰柔和但冷静锐利，银蓝色高马尾，蓝银色护甲领口和肩部结构，白蓝色长袍衣片，身形纤细优雅，有冷静、敏捷、克制的武侠气质。画面重点是脸、发型、肩颈、上身服装和女性身份稳定性。

不要男性化脸，不要白发男性修士感，不要胡子，不要粗重男性下颌，不要浓重男性眉骨，不要宽厚男性躯干，不要武器，不要动作打斗，不要多人，不要重复角色，不要多余肢体，不要复杂背景，不要文字水印。
```

## V012 Video Direction After Identity Anchor Exists

After a stronger Shuangji identity anchor exists and passes human review, prepare V012 with a reference-duty map like this:

- Fenshou locked reference: Fenshou identity only.
- New Shuangji identity anchor: highest-priority Shuangji identity protection.
- Clean scene anchor: preferably `A-SC-TEMPLE-COURTYARD-004` for rainy ancient temple world and frontal main-hall axis.
- V009 1.00s frame: optional loose scene/action continuity only, not identity. Omit if it weakens identity.
- V010/V011 frames: avoid. Do not use as identity, visual, or action reference.

The V012 video should correct both identity and combat rhythm. It should not be another slow forearm pressure hold.

## V012 Rhythm Correction

Use AI-video language that emphasizes true-speed collision and rapid close-range exchange.

Desired rhythm:

- faster staccato close combat
- `da-da-da` feeling
- 3 quick contact beats within `0.8s-1.2s`
- contact -> recoil -> contact -> deflect -> short palm
- wrist slap
- forearm parry
- elbow / shoulder / hip adjustment
- short palm counter
- visible shoe skids
- small wet-floor splashes
- rain, robe, hair, and sleeve motion

Avoid:

- slow motion
- long hit-stop
- static arm-lock
- frozen pullback
- staged performance sparring
- slow demonstration-style pose transitions
- new giant shockwave
- second explosion
- weapons
- flying or big jump

Final edit target:

`0.6s-1.2s`

## Suggested Paths

### Path A - Recommended

Create `A-CH-B-IDENTITY-002` first as a Shuangji face/upper-body identity anchor, get human review approval, then prepare V012 video using the new anchor as the highest-priority identity reference.

Reason: This directly addresses the current failure mode before spending another video generation attempt.

### Path B - Conditional Backup

If a stronger existing Shuangji close-up or upper-body image is found outside the current registry, register it as a planning/reference candidate first, then use it for V012 after human confirmation.

Reason: This may save an identity-anchor generation step if a suitable approved asset already exists.

### Path C - High Risk

Attempt V012 directly with the existing full-body Shuangji reference plus stronger negative prompt language.

Reason this is not recommended: V011 already tried the full-body Shuangji identity reference and still drifted. Repeating that setup is likely to fail again.

## Safety Boundaries

- Dreamina was not run in this phase.
- No submit was run.
- No query_result was run.
- No download was run.
- No media was generated.
- No V012 live package was created.
- `final_master=false`
- `locked=false`
- Human review is required before any final or lock decision.

## Recommended Next Step

Prepare a package-only task for `A-CH-B-IDENTITY-002_shuangji_female_face_upper_body_identity_anchor` if the human approves the identity-first path.

Do not prepare or submit V012 video until the stronger Shuangji identity anchor is approved.

Final verdict: `SHOT_02_V012_IDENTITY_FIRST_PLAN_READY`
