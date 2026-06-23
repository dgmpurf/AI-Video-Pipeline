# PHASE K55 - SHOT-02-V014 Legwork Package Ready

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass prepares the SHOT-02-V014 multimodal2video package only.

- Dreamina was not run.
- No dreamina version or user_credit command was run.
- No submit, query_result, download, retry, resubmit, batch, multimodal2video, image2video, image2image, or text2video command was run.
- No media was created, moved, deleted, staged, or committed.
- Runtime code and configs/providers.json were not modified.
- Project Source files were not modified.
- V013 lock state was not changed.

## Why V014 Is Being Prepared

SHOT-02-V013 CUT01 has been explicitly human-approved and locked as the current SHOT-02 passed segment version.

V013 is strong, identity-safe, faster than V012, and currently accepted. Its remaining limitation is choreography variety: it is mostly upper-body hand/forearm exchange. V014 is being prepared as an optional enhancement experiment to test legwork, lower-body attack-defense, and hand-foot coordination.

## V013 Locked Baseline

Current locked SHOT-02 passed segment:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V013/SHOT-02-V013_CUT01_0p00_to_2p20_best_close_combat_candidate.mp4

V013 CUT01 remains locked as the current passed version.

V014 is not a replacement requirement. V014 cannot overwrite, downgrade, or replace V013 CUT01 unless the human explicitly approves a future replacement.

## Why V013 Visual Frames Are Excluded

V013 CUT01 is the accepted text baseline, but V013 visual frames may reinforce the upper-body-only exchange that V014 is trying to improve. V014 therefore uses exactly three locked image references and excludes all video frames from V009, V010, V011, V012, and V013.

Excluded as visual references:

- SHOT-02-V009 frames
- SHOT-02-V010 frames
- SHOT-02-V011 frames
- SHOT-02-V012 frames
- SHOT-02-V013 frames
- V013 CUT01 frame
- V013 CUT02 frame
- V013 contact sheet
- V013 downloaded video frame

## Reference-Duty Map

1. Fenshou identity reference

Path:
G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png

Duty:
Fenshou identity only. Black/red armored male warrior, face, hair, armor, silhouette, body type, aggressive forward pressure.

2. Shuangji identity anchor

Path:
G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png

Duty:
Highest-priority Shuangji identity protection only. Female face, female identity, silver-blue high ponytail, blue-silver armor collar/shoulders, white-blue robe panels, calm sharp expression. This is not action, rhythm, scene, or camera reference.

3. Scene/world anchor

Path:
G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png

Duty:
Rainy ancient temple courtyard, frontal main-hall axis, wet stone floor, cinematic environment only. This is not a character identity reference.

## Prompt Summary

The V014 prompt uses explicit @ reference-duty mapping, preserves exactly two characters, and assigns highest priority to the A-CH-B-IDENTITY-002 Shuangji identity anchor.

The action begins with fast hand exchange and escalates into simultaneous upper-body and lower-body attack/defense:

- 0.0s-0.60s: wrist slap, forearm parry, short palm, compact shoulder pressure at true speed.
- 0.60s-1.20s: Fenshou cuts his front foot inside while Shuangji steps diagonally outside.
- 1.20s-1.80s: Fenshou threatens low kick or ankle sweep; Shuangji lifts knee or turns shin to seal the line while hands continue parrying.
- 1.80s-2.60s: palm/forearm contact overlaps with shin check or foot sweep threat; wet stone splashes sideways.
- 2.60s-4.00s: continue fighting, regain balance, and re-enter with hand-foot coordination; no pose-out.

## Legwork / Lower-Body Combat Summary

The package targets:

- fast hand exchange first
- hands-and-legs simultaneous attack/defense
- hand parry continuing while lower body attacks
- front-foot cut-in
- diagonal outside-angle footwork
- low kick attempt
- shin check / lower-leg block
- knee lift to seal the line
- short knee bump inside clinch range
- ankle / foot sweep threat without large acrobatics
- wet stone shoe skid
- small water splashes from low steps
- robe hem flicks, sleeve snap, robe snap, and hair whip

## Camera Note

The camera should stay in medium close combat framing. When legwork begins, both characters should remain visible from upper body to knees, while the frontal rainy temple axis remains readable.

Heavy camera cutting is deferred. Subtle combat-following micro-adjustment is allowed, and the camera may slightly dip or widen when legwork appears. It should not spin around the fighters, zoom into a beauty portrait, or become a static poster.

## Package Files

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V014_multimodal_legwork_hand_foot_combo_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V014.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V014.csv`
- Shot record: `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V014.json`
- Package report: `reports/PHASE_K55_SHOT02_V014_LEGWORK_PACKAGE_READY.md`

## Validation Checklist

- prompt JSON parses
- shot record JSON parses
- manifest CSV reads
- all 3 selected reference paths exist locally
- manifest contains exactly the 3 selected image references
- prompt JSON and manifest contain no V009/V010/V011/V012/V013 frame paths
- submit_allowed=false
- query_allowed=false
- download_allowed=false
- final_master=false
- locked=false
- manual prompt includes @ reference-duty map
- negative constraints include male-coded Shuangji, role swap, duplicate characters, extra limbs, weapons, flying, big jump, big flying kick, acrobatic spin kick, new shockwave, second explosion, text, watermark, slow motion, held-contact choreography, and final pose-out

## Safety Confirmation

- No Dreamina command was run.
- No submit/query/download happened.
- No media was staged.
- final_master=false.
- locked=false.
- Human review is required after any future download.

Final verdict:
SHOT_02_V014_LEGWORK_PACKAGE_READY_NO_SUBMIT
