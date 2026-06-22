# PHASE K28 SHOT-02 V011 Multimodal Package Ready

Date: 2026-06-22

## Scope

- Prepare `SHOT-02-V011` as a text-only `multimodal2video` package.
- Do not run Dreamina.
- Do not submit, query, download, retry, resubmit, or batch.
- Do not mark final master or locked.

## V010 Rejection Summary

`SHOT-02-V010` downloaded successfully, but human review rejected it for final use because Shuangji identity is unstable and carries male-coded / gender drift risk.

V010's final relationship/action composition may be used only as a loose action/composition reference. It must not be used as a character identity reference.

## Why V011 Uses Multimodal2Video

Plain `image2video` repeats the V010 weakness: one soft action frame must carry both scene continuity and character identity. V011 needs separate reference duties, especially an explicit highest-priority Shuangji identity anchor.

`multimodal2video` is the recommended task type because it can include locked character references and scene/action continuity references in the same package.

## Recommended Settings

- task_id: `SHOT-02-V011`
- task_type: `multimodal2video`
- provider: `dreamina_cli`
- model_version: `seedance2.0_vip`
- duration: `4`
- video_resolution: `720p`
- ratio: `16:9`
- final_edit_target: `0.8s-1.5s if a usable section exists after generation`
- package_status: `package_ready_no_submit`
- submit_allowed: `false`
- final_master: `false`
- locked: `false`
- human_review_status: `pending`

## Selected References And Duties

| Reference | Path | Duty | Priority | Status |
|---|---|---|---|---|
| ref_01_fenshou_identity | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | Fenshou identity only. Preserve face, black/red armor, body type, hair, silhouette, male warrior identity. Do not copy background, pose, camera, or framing. | high | included |
| ref_02_shuangji_identity | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | Highest-priority Shuangji identity anchor. Preserve female identity, calm face, silver-blue high ponytail, blue-silver armor, white/blue robe panels, clean silhouette, and elegant martial posture. Prevent male-coded/gender drift. | highest | included |
| ref_03_v009_scene_action_continuity | `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg` | Scene/action continuity only. Use rainy temple courtyard, frontal main-hall axis, wet stone floor, post-impact two-character relationship, and grounded combat spacing. Do not use as character identity reference. | high | included |
| ref_04_v010_loose_action_composition | `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V010/frame_06.jpg` | Loose action/composition reference only. Use broad final relationship/contact direction. Do not use for face, hair, costume, silhouette, identity, or gender. | medium | included |
| ref_05_locked_scene_anchor | `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | Optional world/scene anchor only. Preserve rainy ancient temple, main hall frontal axis, and wet stone stage. Do not create new characters from it. | medium | included |

## Prompt Summary

The V011 prompt directs an identity-stabilized follow-up attack after the SHOT-02 shockwave/body recovery beat:

- motion starts from the first frame
- no frozen pullback
- no slow-motion posing
- Fenshou presses from left/left-front with grounded footwork
- Shuangji sidesteps/slides half-step to screen-right/back-right
- Shuangji redirects Fenshou's wrist/forearm with left forearm
- forearms briefly cross and press
- shoulders, elbows, wrists, waist/hips, feet, clothing, hair, rain lines, and wet floor all react continuously
- Shuangji sends a short right palm toward Fenshou's forearm or shoulder armor
- no new giant shockwave, second explosion, water curtain, shield dome, weapon, flying, third person, duplicate characters, fused bodies, extra limbs, gender drift, or role swap

## Package Files

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V011_multimodal_identity_locked_followup_attack_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V011.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V011.csv`
- Shot record: `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V011.json`
- V010 rejection report: `reports/PHASE_K27_SHOT02_V010_HUMAN_REVIEW_REJECTION.md`

## Execution Boundary

No Dreamina command was run in this pass. No submit/query/download happened.

Future next step: human review of this package. A future live submit requires explicit user authorization for exactly one task after canary and command-contract preflight.

Final verdict: `SHOT_02_V011_MULTIMODAL_PACKAGE_READY_NO_SUBMIT`
