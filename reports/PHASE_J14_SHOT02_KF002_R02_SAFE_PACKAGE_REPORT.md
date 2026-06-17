# PHASE J14: SHOT-02-KF-002-R02_safe Package Report

Date: 2026-06-17

## Scope

- Create SHOT-02-KF-002-R02_safe image2image package only.
- Create sanitized upload copies of the three locked reference images.
- Preserve SHOT-02-KF-002 and SHOT-02-KF-002-R01 as historical attempts.
- Do not submit, query, download, retry, batch, auto-continue, or generate final media.
- Do not overwrite locked_refs, source files, runtime code, or configs/providers.json.

## Rerun Reason

R01 reportedly failed because the platform said the text description did not comply with platform rules. R02_safe uses stripped/resized reference copies plus a softer compliance-safe Chinese prompt.

## Sanitized Reference Metadata

Metadata JSON: productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/sanitized_refs_metadata_SHOT-02-KF-002-R02_safe.json

- A-SC-TEMPLE-COURTYARD-004: original=productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png; sanitized=productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-SC-TEMPLE-COURTYARD-004_safe_upload_1920.png; original_dimensions=2560x1440; sanitized_dimensions=1920x1080; original_size_bytes=4147285; sanitized_size_bytes=3907269; sanitized_sha256=5f7f3eed0934fd083e4775215e6e79fa86c0bdd9d099effc0957a692cf85130a
- A-CH-A-SUBJECT-001: original=productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png; sanitized=productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-CH-A-SUBJECT-001_safe_upload_1920.png; original_dimensions=1440x2560; sanitized_dimensions=1080x1920; original_size_bytes=1959523; sanitized_size_bytes=1811278; sanitized_sha256=653d2b0ec5ea7e4720488a47baff91e0e50695468e6db668e5af1bb91c7753de
- A-CH-B-SUBJECT-001: original=productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png; sanitized=productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-CH-B-SUBJECT-001_safe_upload_1920.png; original_dimensions=1440x2560; sanitized_dimensions=1080x1920; original_size_bytes=1752299; sanitized_size_bytes=1951105; sanitized_sha256=c6b1167e5335ef747900282740bc6da14a0931f13c90d9a7ad31f8c635d731b2

## Dreamina Settings

- task_type: image2image
- provider: dreamina_cli
- model_version: 4.7
- ratio: 16:9
- resolution_type: 2k
- poll: 0 when submitted later

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002-R02_safe_main_hall_action_practice_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-002-R02_safe.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-002-R02_safe.csv
- Shot record: productions/chi_yan_tian_qiong/shots/shot_02_keyframe_record_SHOT-02-KF-002-R02_safe.json
- Readiness review: productions/chi_yan_tian_qiong/reviews/image_reviews/SHOT-02-KF-002-R02_safe_readiness_review.md

## Command Preview Only

Do not run this command until explicit live-submit approval is given:

``powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-002-R02_safe_main_hall_action_practice_prompt.txt"
dreamina image2image `
  --images "productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-SC-TEMPLE-COURTYARD-004_safe_upload_1920.png" `
  --images "productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-CH-A-SUBJECT-001_safe_upload_1920.png" `
  --images "productions/chi_yan_tian_qiong/working_refs/safe_upload/SHOT-02-KF-002-R02/A-CH-B-SUBJECT-001_safe_upload_1920.png" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio 16:9 `
  --resolution_type 2k `
  --poll 0
``

## Decision

SHOT_02_KF_002_R02_SAFE_LOCKED_OFFICIAL_KEYFRAME

## Single Submit Result - 2026-06-17

- submit_id: 5caf63aa-2f3e-414b-93c3-40394e8565f6
- logid: 20260617203306169254047008655E2C2
- submit status: querying
- query status: querying
- queue status: Generating
- credit_count: 1
- run_dir: none
- output path: none
- validation result: not applicable because no output was downloaded
- action taken: one submit, one query_result, no retry, no batch, no auto-continue, no download, no output lock

## Single Submit Result - 2026-06-17

- submit_id: 5caf63aa-2f3e-414b-93c3-40394e8565f6
- query status: success
- credit_count: 1
- download happened: yes
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-002-R02_safe_20260617_204221
- output path: productions\chi_yan_tian_qiong\runs\live\SHOT-02-KF-002-R02_safe_20260617_204221\SHOT-02-KF-002-R02_safe_main_hall_action_practice.png
- validation result: dimensions=2560x1440; size_bytes=4160657; sha256=6a573b598ab813e8ac7997a387303326a9f4836c52cc1ae91ca33ed207db60c7; opens successfully
- action taken: no auto-lock, no auto-continue

## Preferred Candidate Registration - 2026-06-17

- task: SHOT-02-KF-002-R02_safe
- preferred_candidate: true
- candidate_status: preferred
- locked: false
- review result: preferred_candidate_passed
- current preferred keyframe candidate for SHOT-02: yes
- candidate image: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-002-R02_safe_20260617_204221/SHOT-02-KF-002-R02_safe_main_hall_action_practice.png
- human review notes recorded in readiness review: anchor preserved / two characters / readable contact / not distant standoff; minor risks noted (chain-whip element, slight horizontal-duel tendency) but accepted for candidate.
- no lock action taken
- no auto-continue

## Preferred Candidate Registration Reconfirm - 2026-06-17

- task: SHOT-02-KF-002-R02_safe
- preferred_candidate: true
- candidate_status: preferred
- current preferred keyframe candidate for SHOT-02: yes
- locked: false
- official_keyframe: false
- output path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-KF-002-R02_safe_20260617_204221/SHOT-02-KF-002-R02_safe_main_hall_action_practice.png
- do not lock this image yet
- no batch/no retry/no auto-continue
## Official Keyframe Lock Registration - 2026-06-17

- lock decision: approved_to_lock=true
- lock_source: SHOT-02-KF-002-R02_safe
- lock target: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- locked=true; official_keyframe=true; candidate_status=locked_official
- lock risk log: chain/whip-like hand element and slight horizontal-duel tendency accepted
- locked keyframe path: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- approved by human for official keyframe status
- status: official keyframe candidate now active; video generation not started automatically
