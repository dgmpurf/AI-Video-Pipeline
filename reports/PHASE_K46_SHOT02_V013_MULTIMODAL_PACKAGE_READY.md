# PHASE K46 SHOT-02 V013 Multimodal Package Ready

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Purpose

SHOT-02-V013 is prepared as a package-only multimodal2video correction after SHOT-02-V012.

V012 improved Shuangji identity, but it remains rejected for final use because the action is still too slow, impact/contact density is too soft, and the tail does not continue fighting strongly enough. K45 reviewed the V012 local cut/speed diagnostics and found CUT01 1.5x closest to the desired rhythm, but still diagnostic only.

Therefore V013 is prepared as a new generation direction with stronger choreography, not as an edit-forcing attempt on V012.

## Package Summary

- task_id: SHOT-02-V013
- task_type: multimodal2video
- provider: dreamina_cli
- model_version: seedance2.0_vip
- duration: 4
- video_resolution: 720p
- ratio: 16:9
- submit_allowed: false
- query_allowed: false
- download_allowed: false
- final_master: false
- locked: false
- human_review_status: pending
- human_review_required: true

## Why V012 Is Diagnostic Only

V012 is useful as text failure guidance only:

- identity improved
- Shuangji female identity was much more stable
- CUT01 1.5x was the best local diagnostic
- 1.5x speed-up improved rhythm most

But V012 still fails final review:

- contact density remains too low
- impact remains soft
- the action reads as one held exchange
- speed-up cannot create new contact beats
- tail continuation remains insufficient

Primary path remains SHOT-02-V013 new generation with stronger action choreography.

## Why A-CH-B-IDENTITY-002 Remains The Shuangji Anchor

A-CH-B-IDENTITY-002 is the approved locked Shuangji identity anchor. It is the highest-priority Shuangji identity reference for:

- female face
- female identity
- silver-blue high ponytail
- blue-silver armor collar/shoulders
- white-blue robe panels
- calm sharp expression

It is not used as action, rhythm, scene, or camera reference.

## Excluded Visual References

The V013-R01 package excludes:

- any SHOT-02-V009 frame
- any SHOT-02-V010 frame
- any SHOT-02-V011 frame
- any SHOT-02-V012 frame
- V012 cut/speed test frames
- V012 contact sheet
- V012 downloaded video frame

Reason:

V012 and prior video frames may reinforce held-contact choreography, soft impact, or earlier identity drift. They are retained only as text lessons, not visual references.

## Reference-Duty Map

Reference 1:

- path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
- duty: Fenshou identity only
- identity role: black/red armored male warrior, face, hair, armor, silhouette, body type, aggressive forward pressure

Reference 2:

- path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
- duty: highest-priority Shuangji identity protection only
- identity role: female face, female identity, silver-blue high ponytail, blue-silver armor collar/shoulders, white-blue robe panels, calm sharp expression
- not action/rhythm/scene/camera reference

Reference 3:

- path: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
- duty: scene/world only
- scene role: rainy ancient temple courtyard, frontal main-hall axis, wet stone floor, cinematic environment
- not character identity reference

## Prompt Summary

The manual prompt uses Chinese and includes an explicit @ reference-duty map near the top with the actual reference filenames.

The prompt states:

- exactly two characters only: Fenshou and Shuangji
- Fenshou is the black/red armored male warrior
- Shuangji is the silver-blue high-ponytail female warrior
- Shuangji face and female identity must follow @A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
- do not turn Shuangji into a white-haired male cultivator
- do not swap roles
- do not duplicate either character
- do not create a third person

## Action Rhythm Summary

V013 targets:

- true speed
- at least 2x faster feel than V012 original
- fast staccato close combat
- five quick contact beats within the first 1.0s
- da-da-da-da-da rhythm
- contact -> immediate rebound -> re-entry -> deflect -> counter -> re-entry
- short impact, immediate recoil
- no slow motion
- no long hit-stop
- no static arm-lock
- no slow forearm pushing
- no held forearm relationship
- no demonstration-style pose transitions
- no staged performance sparring feel

Timing plan:

- 0.0s-0.20s: Fenshou explosive step-in and first forearm/wrist collision
- 0.20s-0.40s: Shuangji sharp wrist slap/deflection and immediate rebound
- 0.40s-0.60s: Fenshou compact shoulder/forearm bump; Shuangji tight forearm parry
- 0.60s-0.80s: Shuangji short palm or elbow-line interruption; Fenshou recoils
- 0.80s-1.00s: Fenshou cuts back in; Shuangji diagonal step and deflects again
- 1.00s-3.00s: second chain of fast close-range attacks/defenses
- 3.00s-4.00s: continue fighting through the tail, no pose-out

## Force And Impact Mechanics Summary

The prompt asks for:

- sharp stop-start footwork
- strong shoulder-hip weight transfer
- sudden acceleration and abrupt redirection
- visible body recoil on contact
- contact pushing rain droplets and sleeves outward
- shoe skid on wet stone
- small splashes kicked sideways
- robe snap, sleeve snap, hair whip
- contact lasting only a fraction of a second
- immediate physical response after every contact
- power from body mechanics and collision, not slow motion

## Camera Note

V013 allows subtle combat-following:

- medium close combat framing
- keep both characters visible
- frontal rainy temple axis remains readable
- slight handheld urgency allowed
- subtle follow and micro-adjustments allowed

Heavy camera cutting is deferred. Do not overcomplicate V013 with heavy camera switching yet.

## Package Files

- manual prompt: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V013_multimodal_identity_locked_2x_impact_combo_prompt.txt
- prompt JSON: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V013.json
- manifest CSV: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V013.csv
- shot record: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V013.json
- package report: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K46_SHOT02_V013_MULTIMODAL_PACKAGE_READY.md

## Package Validation Checklist

- Prompt JSON parses.
- Shot record JSON parses.
- Manifest CSV reads.
- All 3 selected reference paths exist locally.
- Manifest contains exactly the 3 selected image references.
- No prior video-frame paths are present in prompt JSON or manifest.
- submit_allowed=false.
- final_master=false.
- locked=false.
- Manual prompt includes @ reference-duty map.
- Negative constraints include male-coded Shuangji, role swap, duplicate characters, extra limbs, weapons, new shockwave, second explosion, text, watermark, slow motion, held-contact choreography, and final pose-out.

## Safety Confirmation

- No Dreamina command was run.
- No dreamina version/user_credit command was run.
- No submit/query/download happened.
- No generation was performed.
- No media files were moved, deleted, staged, or committed.
- final_master=false.
- locked=false.
- Human review is required after any future download.

Final verdict:
SHOT_02_V013_MULTIMODAL_PACKAGE_READY_NO_SUBMIT
