# SHOT-02-KF-002 Readiness Review

Task: SHOT-02-KF-002

Status: package_ready_no_submit

Needs generation: true

Locked: false

## Scene Anchor Requirement

- Required scene anchor: A-SC-TEMPLE-COURTYARD-004
- Locked ref: productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
- Anchor status: locked_after_human_review
- Review status: approved
- SHA256: 831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452
- Submit policy: package only for now; do not submit until the user gives explicit approval for exactly one Dreamina image2image task.

## Staging Intent

SHOT-02-KF-002 stages the first close-combat clash in front of the main hall.

Fenshou approaches from the left / left-front side toward the central combat area. Shuangji cuts in from the right side toward the central combat area. They meet in the midground wet stone combat-stage area in front of the main hall door and stone steps.

The result should read as a frozen instant before or at the first close-range clash, not a static distant standoff, poster pose, side-scrolling game composition, or flat two-person lineup.

## Required Visual Checks After Generation

- exactly two characters only
- one Fenshou only
- one Shuangji only
- A-SC-TEMPLE-COURTYARD-004 is the only scene anchor
- no A-SC-TEMPLE-COURTYARD-001/002/003 scene fallback
- no SHOT-01 far-distance static standoff
- main hall front central combat-stage area is visible
- Fenshou enters from left / left-front toward center
- Shuangji cuts in from right toward center
- first close-range clash relationship is clear
- frontal main-hall axis remains the background anchor
- midground diagonal combat tension is visible
- side-scroller game feel avoided
- no duplicate characters, no third person, no fused bodies, no extra limbs
- body mechanics credible
- rainy temple continuity preserved

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002_main_hall_combat_exchange_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-002.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-002.csv
- Shot record: productions/chi_yan_tian_qiong/shots/shot_02_keyframe_record_SHOT-02-KF-002.json

## Decision

package_ready_no_submit

## Single Submit Result - 2026-06-17

- submit_id: d5e31d12-29af-4d2d-a93b-62055843b172
- logid: 2026061720061516925404700897502E2
- submit status: querying
- query status: fail
- credit_count: 1
- fail_reason: generation failed: final generation failed
- download: not performed
- retry: not performed
- lock status: not locked
