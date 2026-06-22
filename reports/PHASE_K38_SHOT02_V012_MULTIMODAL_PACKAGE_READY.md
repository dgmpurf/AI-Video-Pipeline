# PHASE K38 SHOT-02 V012 Multimodal Package Ready

Date: 2026-06-22

## Scope

Prepare `SHOT-02-V012` as a package-only `multimodal2video` task.

No Dreamina command was run. No submit, query_result, download, retry, resubmit, batch, logout, or relogin happened in this phase.

This package is not a final video decision:

- `submit_allowed=false`
- `final_master=false`
- `locked=false`
- human review is required after any future download

## Why V012 Is Prepared Now

`SHOT-02-V010` and `SHOT-02-V011` were rejected for final use because Shuangji identity drifted male-coded and the follow-up combat rhythm remained too slow / staged.

The V011 submit evidence showed the expected references were included, so the failure was not a package-reference mismatch. It was a model identity-preservation and rhythm-following failure.

V012 therefore changes both strategy points:

1. Use the new Shuangji face / upper-body identity anchor as the highest-priority identity reference.
2. Replace slow forearm-pressure language with true-speed staccato close-combat language.

## Files Inspected

- `reports/PHASE_K31_SHOT02_V011_HUMAN_REVIEW_AND_V012_DIRECTION.md`
- `reports/PHASE_K32_SHOT02_V012_IDENTITY_FIRST_CORRECTION_PLAN.md`
- `reports/PHASE_K36_SHUANGJI_IDENTITY_ANCHOR_VISUAL_REVIEW.md`
- `reports/PHASE_K37_SHUANGJI_IDENTITY_ANCHOR_HUMAN_APPROVED_LOCKED.md`
- `productions/chi_yan_tian_qiong/assets/A-CH-B-IDENTITY-002_planning_record.json`
- `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V011.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V011.csv`
- `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V011.json`

The Shuangji identity-anchor metadata is recorded as `human_approved_locked_identity_anchor`, with `locked=true` for the identity asset only. No SHOT-02 video is marked final or locked by this package.

## Reference-Duty Map

Only these 3 image references are selected for V012.

| Order | Path | Duty | Identity Use | Action/Scene Use |
|---:|---|---|---|---|
| 1 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | Fenshou identity only: black/red armored male warrior, face, hair, armor, silhouette, body type, aggressive pressure. | yes | no |
| 2 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | Highest-priority Shuangji identity protection only: female face/identity, silver-blue high ponytail, blue-silver collar/shoulders, white-blue robe panels, calm sharp expression. | yes | no |
| 3 | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | Rainy ancient temple scene/world only: main-hall frontal axis, wet stone floor, cold gray-blue rain light. | no | scene only |

Reference hashes:

- Fenshou full-body subject: `83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F`
- Shuangji identity anchor: `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11`
- Temple courtyard anchor: `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452`

## Why V010 / V011 / V009 Frames Are Excluded

The V010 and V011 frames are contaminated for V012:

- Shuangji can read male-coded.
- Video frames are soft and not reliable for identity protection.
- They reinforce slow staged sparring / static arm-lock motion.

The V009 1.00s frame is also excluded for this R01 package. Even though it is useful for continuity in earlier contexts, it is not needed here and may weaken the identity-first strategy.

Explicitly excluded:

- `SHOT-02-V010` frames
- `SHOT-02-V011` frames
- `V009 1.00s frame for R01`
- `V010 frame_06`
- V011 contact sheet / downloaded video frame
- any V009/V010/V011 frame path in the prompt JSON or manifest

## Prompt Summary

The manual prompt:

- uses Chinese
- places explicit `@` reference-duty mapping at the top
- defines exactly two characters only: Fenshou and Shuangji
- defines Fenshou as black/red armored male warrior
- defines Shuangji as silver-blue high-ponytail female warrior
- states Shuangji identity must follow `@A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`
- explicitly prevents Shuangji from becoming male-coded or a white-haired male cultivator
- prevents role swap, duplicate characters, third person, extra limbs, fused bodies, weapons, flying, big jump, new giant shockwave, second explosion, text, watermark, and logo

## Action Rhythm Summary

V012 is intended as a fast close-range follow-up exchange after the shockwave beat, not another shockwave clip.

Timing target:

- `0.0s-0.4s`: Fenshou hard step-in, foot skid on wet stone, first short forearm/wrist contact.
- `0.4s-0.8s`: Shuangji quick wrist slap / forearm deflection, contact rebounds, sleeve and high ponytail whip sideways.
- `0.8s-1.2s`: Fenshou re-enters; Shuangji answers with short palm / tight forearm parry; three contacts read as `da-da-da`.
- `1.2s-4.0s`: continuation / recovery / next setup only; do not slow the whole motion into a pose.

Rhythm requirements:

- true speed
- fast staccato close combat
- collision-based contact
- visible shoe skids and small splashes
- rain streaks, robe, sleeve, and hair motion
- no slow motion
- no long hit-stop
- no static arm-lock
- no staged performance sparring

Final edit target:

`0.6s-1.2s`

## Package Files

- `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V012_multimodal_identity_locked_fast_staccato_combat_prompt.txt`
- `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V012.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V012.csv`
- `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V012.json`
- `reports/PHASE_K38_SHOT02_V012_MULTIMODAL_PACKAGE_READY.md`

## Command Preview Only

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V012_multimodal_identity_locked_fast_staccato_combat_prompt.txt"
C:\Users\msjpurf\bin\dreamina.exe multimodal2video `
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" `
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png" `
  --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 4 `
  --video_resolution 720p `
  --ratio "16:9" `
  --poll 0
```

This command was not run.

## Validation Checklist

- Prompt JSON parses.
- Shot record JSON parses.
- Manifest CSV reads.
- All 3 selected reference paths exist locally.
- Prompt JSON and manifest contain no V009/V010/V011 frame paths.
- `submit_allowed=false`
- `query_allowed=false`
- `download_allowed=false`
- `final_master=false`
- `locked=false`
- manual prompt includes `@` reference-duty map
- negative constraints include male-coded Shuangji, role swap, duplicate characters, extra limbs, weapons, new shockwave, second explosion, text, and watermark

## Boundary Confirmation

- Dreamina was not run.
- No submit was run.
- No query_result was run.
- No download was run.
- No media was generated.
- No media file was staged.
- No runtime code was modified.
- `configs/providers.json` was not modified.
- No Project Source file was modified.
- `final_master=false`
- `locked=false`
- human review is required after future download

Final verdict: `SHOT_02_V012_MULTIMODAL_PACKAGE_READY_NO_SUBMIT`
