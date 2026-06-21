# PHASE K26 SHOT-02 V011 Reference Pack Plan

Date: 2026-06-21

## Scope

- Prepare planning only for `SHOT-02-V011`.
- Do not run Dreamina, submit, query, download, retry, resubmit, batch, generate media, lock, or mark final master.
- Final approval still requires human review.

## Current Assessment Of V010

`SHOT-02-V010` was downloaded successfully and is pending human review in project metadata. Human review found that the final frame relationship appears usable for the next action direction, but character identity stability is not reliable enough, especially for Shuangji.

The main issue is not the broad action idea. The problem is that blurred or soft video frames are not sufficient to protect character identity through the next generation step. V011 should therefore use explicit character identity references, with Shuangji treated as the highest-priority identity anchor.

## Why Explicit Character References Are Needed

- V010 video frames contain useful motion/action relationship information, but the faces, costume details, and silhouette read softer than locked character subject references.
- Shuangji's identity is more vulnerable in the V010 frames because white/silver hair and light clothing can drift into generic pale-robed character designs.
- A single image2video start frame can preserve timing/composition, but it cannot simultaneously provide strong separate identity anchors for both characters.
- V011 should separate duties: character identity refs define who the two fighters are; continuity/action frames define where they are and what relationship continues.

## Candidate Reference Images

### Fenshou Character Identity Reference

Recommended:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`

Evidence:

- Registered asset logical_id: `A-CH-A-SUBJECT-001`
- Role: character
- Status: `locked_after_human_review`
- Review status: `approved`
- Registry note: user-approved production character lock after manual visual review
- Registry sha256: `83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F`

Reference duty:

- Identity, costume, body type, hair, black/red armor silhouette.
- Do not use as pose, scene, camera, or framing reference.

### Shuangji Character Identity Reference

Recommended:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`

Evidence:

- Registered asset logical_id: `A-CH-B-SUBJECT-001`
- Role: character
- Status: `locked_after_human_review`
- Review status: `approved`
- Registry note: approved Shuangji subject image; hair color and high ponytail correct; blue-silver armor and long-robe silhouette stable; face integrity good; suitable locked production subject reference
- Registry sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`

Reference duty:

- Highest-priority identity protection for Shuangji.
- Protect silver-blue high ponytail, calm face, blue-silver armor, white/blue robe panels, and clean silhouette.
- Do not use as pose, scene, camera, or framing reference.

### Scene Continuity Frame

Recommended primary continuity frame:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg`

Evidence:

- This frame was the human-approved V010 start frame.
- It keeps the rainy temple courtyard, frontal main-hall axis, wet stone ground, and two-character post-impact relationship.
- It is better suited than V010 frames for scene continuity because V010 was specifically reviewed as identity-unstable.

Reference duty:

- Scene continuity, wet courtyard, main hall axis, post-shockwave combat position, and broad two-character relationship.
- Not a character identity reference.

Backup continuity frame:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_0p50s.jpg`

Use only if the next V011 motion needs to start from a slightly earlier, more active body-reaction moment.

### Optional Action / Composition Reference

Candidate:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V010/frame_06.jpg`

Evidence:

- V010 final frame relationship appears usable according to human review.
- The frame can help communicate the desired follow-up contact relationship and screen direction.

Reference duty:

- Loose action/composition reference only.
- Do not use as identity reference.
- Do not trust it for Shuangji face, hair, costume, or silhouette details.
- Include only if human confirms that the final-frame relationship is the intended V011 starting relationship.

### Optional World / Scene Anchor

Candidate:

`G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png`

Evidence:

- Registered asset logical_id: `A-SC-TEMPLE-COURTYARD-004`
- Role: scene
- Status: `locked_after_human_review`
- Review status: `approved`
- Preferred SHOT-02 true frontal-axis scene anchor
- Registry sha256: `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452`

Reference duty:

- World/scene anchor only: rainy ancient temple, main hall frontal axis, wet stone stage.
- Use only if V011 packaging needs extra scene stability beyond the V009 continuity frame.

## Task Type Comparison

### image2video

Pros:

- Simple and well-tested in this project.
- Exactly one `--image`, no ratio flag.
- Good when the single start frame is already visually stable.

Cons:

- Cannot include separate Fenshou and Shuangji identity references.
- Would repeat the V010 risk: the model must infer character identity from a soft video frame.
- Not recommended when the main goal is identity protection.

### multimodal2video

Pros:

- Designed for all-around references.
- Supports multiple images, so V011 can pass character identity refs and scene/action refs together.
- Better fit for explicit identity protection, especially Shuangji.

Cons:

- More reference duties must be stated clearly in the prompt.
- Higher risk of reference-role confusion if the package does not say which image controls identity, scene, or action.

Recommendation:

Use `multimodal2video` for V011.

Suggested contract based on existing CLI audit/help snapshots:

- task_type: `multimodal2video`
- model_version: `seedance2.0_vip`
- duration: `4`
- video_resolution: `720p`
- ratio: `16:9`
- inputs: multiple `--image` refs, each with explicit role in the prompt/package
- final_master: `false`
- locked: `false`
- human_review_status: `required`

## Proposed V011 Reference-Duty Mapping

| Reference | Path | Duty | Priority |
|---|---|---|---|
| Fenshou identity | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | Fenshou face, hair, body type, black/red armor identity | High |
| Shuangji identity | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | Shuangji face, silver-blue high ponytail, blue-silver armor, robe silhouette | Highest |
| Scene continuity | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg` | Rainy temple courtyard, main hall frontal axis, wet floor, post-impact relationship | High |
| Optional action/composition | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V010/frame_06.jpg` | Loose V010 final relationship and action direction only | Medium, human-confirmed |
| Optional scene anchor | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | Stable SHOT-02 main hall stage and frontal axis | Medium |

## Planning Recommendation For V011

Prepare V011 as a `multimodal2video` package, not a plain `image2video` package, if the goal is to preserve both character identities while continuing the post-V010 action.

Minimum recommended reference pack:

1. Fenshou locked full-body subject reference.
2. Shuangji locked full-body subject reference.
3. V009 frame 1.00s as scene/action continuity frame.

Optional additions after human confirmation:

4. V010 final frame as loose action/composition reference.
5. A-SC-TEMPLE-COURTYARD-004 locked scene anchor if the scene starts drifting.

Prompting principle:

- State early that character subject refs are identity-only.
- State that the V009/V010 frames are continuity/action references only.
- Explicitly say the video must not copy the studio backgrounds from character refs.
- Explicitly say Shuangji must keep the locked Shuangji design rather than the softened V010 video-frame identity.

## Open Questions For Human Confirmation

1. Should V011 continue directly from V010 final relationship, or restart from the cleaner V009 1.00s continuity frame with a revised action prompt?
2. Should `frame_06.jpg` from V010 be included as a loose action/composition reference, despite its identity instability?
3. Should the locked scene anchor `A-SC-TEMPLE-COURTYARD-004` be included, or is V009 frame 1.00s enough for scene continuity?
4. Is V011 intended to be a follow-up attack continuation, a reset into next combat beat, or a short identity-stabilized repair of V010's usable final relationship?
5. Should V011 package target `multimodal2video` with three images first, or include all five references in one stronger but more complex reference pack?

## Decision

Planning-only recommendation: use `multimodal2video` for SHOT-02-V011 with explicit reference-duty separation.

Final verdict: `SHOT_02_V011_REFERENCE_PACK_PLAN_READY`
