# SHOT-02-KF-002-R02_safe Readiness Review

Task: SHOT-02-KF-002-R02_safe
Parent task: SHOT-02-KF-002-R01

Status: locked_official_keyframe
Needs generation: false
Locked: true

## Rerun Reason

R01 reportedly failed because the platform said the text description did not comply with platform rules. R02_safe uses sanitized upload copies of the three locked refs and a softer Chinese prompt while preserving the same visual target.

## Sanitized Upload References

- Metadata: productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/sanitized_refs_metadata_SHOT-02-KF-002-R02_safe.json
- Scene: productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-SC-TEMPLE-COURTYARD-004_safe_upload_1920.png
- Fenshou: productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-CH-A-SUBJECT-001_safe_upload_1920.png
- Shuangji: productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-CH-B-SUBJECT-001_safe_upload_1920.png

## Prompt Strategy

- Chinese only.
- Shorter and softer than R01.
- Avoids platform-sensitive conflict wording and weapon wording.
- Uses safer terms such as 武术动作, 对练, 动作定格, 前臂相接, 掌法卸力, 近距离动作互动, 电影关键帧.

## Required Visual Checks After Generation

- exactly two characters only: one Fenshou and one Shuangji
- sanitized A-SC-004 copy is the only scene/camera anchor
- main hall frontal axis, door, steps, and wet stone area remain visible
- near-distance martial-arts action practice reads clearly
- one clear forearm contact or near-contact point
- bodies separated and readable, feet grounded
- not distant standoff, not side-scroller, not poster pose
- no third person, duplicate character, fused body, extra limb, text, or watermark

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002-R02_safe_main_hall_action_practice_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-002-R02_safe.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-002-R02_safe.csv
- Shot record: productions/chi_yan_tian_qiong/shots/shot_02_keyframe_record_SHOT-02-KF-002-R02_safe.json

## Decision

SHOT_02_KF_002_R02_SAFE_PACKAGE_READY_NO_SUBMIT

## Single Submit Result - 2026-06-17

- submit_id: 5caf63aa-2f3e-414b-93c3-40394e8565f6
- logid: 20260617203306169254047008655E2C2
- submit status: querying
- query status: querying
- queue status: Generating
- credit_count: 1
- run_dir: none
- download: not performed
- retry: not performed
- lock status: not locked
- next action: manual follow-up query only after explicit user approval

## Single Submit Result - 2026-06-17

- submit_id: 5caf63aa-2f3e-414b-93c3-40394e8565f6
- query status: success
- download happened: yes
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-002-R02_safe_20260617_204221
- output path: productions\chi_yan_tian_qiong\runs\live\SHOT-02-KF-002-R02_safe_20260617_204221\SHOT-02-KF-002-R02_safe_main_hall_action_practice.png
- validation: dimensions=2560x1440; size_bytes=4160657; sha256=6a573b598ab813e8ac7997a387303326a9f4836c52cc1ae91ca33ed207db60c7; opens=true
- lock status: not locked
- action taken: download and record; no auto-continue

## Preferred Candidate Registration - 2026-06-17

- preferred_candidate: true
- locked: false
- official_keyframe: false
- candidate_status: preferred
- review result: preferred_candidate_passed
- current preferred keyframe candidate for SHOT-02: yes
- candidate image: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-002-R02_safe_20260617_204221/SHOT-02-KF-002-R02_safe_main_hall_action_practice.png
- human review notes:
  - A-SC-004 frontal main-hall scene anchor preserved: pass
  - main hall door, stone steps, and railings remain legible: pass
  - rainy ancient temple atmosphere preserved: pass
  - wet stone floor and reflections preserved: pass
  - exactly two characters: pass
  - Fenshou on left, Shuangji on right: pass
  - first close-range arm contact / near-contact point visible: pass
  - bodies separated and readable: pass
  - no duplicate characters: pass
  - no fused bodies: pass
  - no extra people: pass
  - not a static distant standoff: pass
  - minor issue: Fenshou appears to have a chain/whip-like element in one hand; acceptable for candidate, record as minor visual risk
  - minor issue: composition still has slight horizontal-duel tendency; acceptable for candidate
- do not lock image yet

## Preferred Candidate Registration Reconfirm - 2026-06-17T20:42:21+08:00

- task: SHOT-02-KF-002-R02_safe
- decision: preferred_candidate_passed
- candidate_status: preferred
- locked: false
- official_keyframe: false
- current preferred keyframe candidate for SHOT-02: yes
- output path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-002-R02_safe_20260617_204221/SHOT-02-KF-002-R02_safe_main_hall_action_practice.png
- human review notes persisted and accepted:
  - chain/whip-like element in Fenshou hand recorded as minor visual risk
  - slight horizontal-duel tendency recorded as minor visual risk
  - do not lock automatically
  - no auto-continue

## Official Keyframe Lock Registration - 2026-06-17

- approved_to_lock: true
- lock_source: SHOT-02-KF-002-R02_safe
- official_keyframe_for_shot: SHOT-02
- locked: true
- official_keyframe: true
- candidate_status: locked_official
- locked_keyframe_path: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- acceptance: approved for official SHOT-02 keyframe
- accepted minor risks: chain/whip-like hand element; slight horizontal-duel tendency
- do not auto-lock in code pipeline; manual lock decision recorded only
