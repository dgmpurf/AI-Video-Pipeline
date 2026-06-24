# PHASE K67 - SHOT-02-V015 Upload-Safe Fast Hand Exchange Micro-FX Package Ready

Date: 2026-06-24
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass prepares the SHOT-02-V015 upload-safe multimodal2video package only.

- Dreamina was not run.
- No dreamina version or user_credit command was run.
- No submit/query/download happened.
- No retry or resubmit happened.
- No media was created, edited, moved, deleted, staged, or committed.
- Runtime code, configs/providers.json, and Project Source files were not modified.
- V013 shot record was not modified.
- V013 CUT01 remains the locked current SHOT-02 passed segment.
- V014-R02 was not marked final or locked.
- V015 is not final and not locked.
- V016 and V017 packages were not created.

## Why V015 Is Being Prepared Now

K66 recommended a multi-clip route for a possible 10s-15s SHOT-02 fast-combat section. The route starts with V015, then later prepares V016 and V017 separately after review.

V015 is the first polish clip. Its purpose is fast hand exchange with subtle fantasy micro-feedback while preserving the grounded, realistic, 1980s-style close-combat feeling from SHOT-02-V014-R02.

## Current Baseline Relationship

SHOT-02-V013 CUT01 remains the locked current SHOT-02 passed segment version.

V014-R02 is a positive human-reviewed enhancement candidate, but it is not final, not locked, and not a V013 replacement.

Future replacement of locked V013 CUT01 requires explicit human approval.

## V015 Package Settings

| Field | Value |
|---|---|
| shot_id | SHOT-02-V015 |
| variant_id | uploadsafe_fast_hand_exchange_micro_fx |
| source_plan | SHOT-02_long_fast_combat_multi_clip_plan |
| source_positive_candidate | SHOT-02-V014-R02_uploadsafe |
| task_type | multimodal2video |
| provider | dreamina_cli |
| model_version | seedance2.0_vip |
| duration | 5 |
| video_resolution | 720p |
| ratio | 16:9 |
| submit_allowed | false |
| query_allowed | false |
| download_allowed | false |
| final_master | false |
| locked | false |
| human_review_required | true |
| baseline_locked_version | SHOT-02-V013-CUT01-LOCKED |

Replacement policy:

cannot replace locked V013 CUT01 unless human explicitly approves future replacement

## V015 Purpose

V015 is the first clip in the long fast-combat plan. It aims to create:

- fast hand exchange
- true-speed close-combat pressure
- realistic compact body mechanics
- subtle xuanhuan / fantasy micro-feedback
- no giant effects
- no slow-motion-only impact
- continued fighting through the final second

## V015 Action Summary

The planned 5-second action structure:

1. 0.00s-0.80s: true-speed close guard; Fenshou presses with compact shoulder pressure and short forearm line; Shuangji catches with wrist slap and forearm parry.
2. 0.80s-1.70s: Fenshou chains compact palm and forearm shove; Shuangji redirects with a silver-blue forearm block and small outside step; tiny red-blue micro sparks flash for less than 0.2s.
3. 1.70s-2.80s: hand exchange tightens 10%-20% over V014-R02 while staying readable; wrist slap, palm check, forearm bind, shoulder pressure.
4. 2.80s-3.80s: Shuangji breaks pressure with short palm deflection and silver-blue block-edge streak; Fenshou answers with dark-red ember trace; wet stone skids and cold rain splashes.
5. 3.80s-5.00s: both fighters continue through the final second, re-entering the centerline rather than freezing or posing out.

## Micro-Fantasy FX Summary

Allowed effects are strictly small and contact-tied:

- tiny red-blue micro sparks at forearm collision
- short silver-blue light streaks on Shuangji blocks
- dark-red ember traces on Fenshou pressure attacks
- cold glowing rain splashes from low steps
- brief contact flicker under 0.2s
- subtle particle residue that disappears immediately

Forbidden effects:

- giant shockwave
- new giant shockwave
- second explosion
- circular water shield
- energy shield dome
- full-body aura burst
- large spell effect
- big magic beam

## Camera And Rhythm Summary

V015 should use medium close combat framing. Both characters must remain visible enough for hands, shoulders, torsos, and partial footwork. The rainy ancient temple frontal axis should remain readable.

Power should come from real-speed body mechanics:

- grounded stance
- rear-foot push
- hip/waist rotation
- shoulder-driven compact strikes
- short contact and immediate rebound
- 0.1s-0.2s hit-stop only at key contact
- wet stone shoe skid
- small water splash
- robe/sleeve snap
- hair whip
- continuous pressure

The clip should not become slow-motion-only impact or soft fast motion.

## Reference-Duty Map

Use exactly these 3 upload-safe JPG references as active image references:

1. Fenshou identity upload-safe JPG

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg

Duty: Fenshou identity only. Black/red armored male warrior, face, hair, armor, silhouette, body type, aggressive forward pressure.

2. Shuangji identity upload-safe JPG

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg

Duty: highest-priority Shuangji female identity protection only. Female face, female identity, silver-blue high ponytail, blue-silver armor collar/shoulders, white-blue robe panels, calm sharp expression. Do not use this as action/rhythm/scene/camera reference.

3. Temple scene/world upload-safe JPG

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg

Duty: rainy ancient temple courtyard, frontal main-hall axis, wet stone floor, cinematic environment only. Do not use this as character identity reference.

## Reference Exclusion Confirmation

The original PNG locked_refs are not active refs in the V015 manifest.

The V014-R02 MP4 and V014-R02 contact sheet are not active visual refs.

The package does not use these as active visual references:

- SHOT-02-V009 frames
- SHOT-02-V010 frames
- SHOT-02-V011 frames
- SHOT-02-V012 frames
- SHOT-02-V013 frames
- V013 cut frames
- V013 contact sheet
- V013 downloaded video frame
- V014-R02 media/contact sheet as active visual reference

V014-R02 is only a text/action-rhythm baseline for this first V015 package.

## Package Files

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V015_uploadsafe_fast_hand_exchange_micro_fx_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V015_uploadsafe.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V015_uploadsafe.csv`
- Shot record: `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V015_uploadsafe.json`
- Package report: `reports/PHASE_K67_SHOT02_V015_UPLOADSAFE_FAST_HAND_EXCHANGE_MICRO_FX_PACKAGE_READY.md`

## Validation Checklist

- V015 prompt JSON parses.
- V015 shot record JSON parses.
- V015 manifest CSV reads.
- The 3 selected upload-safe JPG reference paths exist locally.
- Manifest contains exactly 3 active image references.
- Manifest uses upload-safe JPG refs, not original PNG locked_refs.
- Prompt JSON and manifest contain no V009/V010/V011/V012/V013 frame/media paths.
- V014-R02 MP4/contact sheet are not active refs in prompt JSON or manifest.
- submit_allowed=false.
- final_master=false.
- locked=false.
- Manual prompt includes upload-safe @ reference-duty map.
- Negative constraints include male-coded Shuangji, role swap, duplicate characters, extra limbs, weapons, flying, big jump, big flying kick, acrobatic spin kick, new shockwave, second explosion, text, watermark, slow-motion-only impact, held-contact choreography, and final pose-out.

## Safety Confirmation

- No Dreamina command was run.
- No submit/query/download happened.
- No media was staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- V013 shot record was not modified.
- V014-R02 shot record was not modified.
- V015 final_master=false.
- V015 locked=false.
- Human review is required after any future download.

## Next Recommended Step

Review the V015 package. Only after package review and explicit human approval should canary/preflight and exactly one Dreamina submit be attempted.

Final verdict:
SHOT_02_V015_UPLOADSAFE_FAST_HAND_EXCHANGE_MICRO_FX_PACKAGE_READY_NO_SUBMIT
