# Phase G4.3 Lock Shuangji Subject Asset Report

## 1) Locked target
- logical_id: `A-CH-B-SUBJECT-001`
- candidate_id: `A-CH-B-SUBJECT-001_cand_001`
- submit_id: `b381e6d4-c559-4689-a09c-03289ac63319`
- final status: `locked_after_human_review`
- final review status: `approved`

## 2) Source and locked paths
- source image path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_055254_A-CH-B-SUBJECT-001\output\A-CH-B-SUBJECT-001_shuangji_full_body_subject.png`
- locked image path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`

## 3) Source integrity
- exists: true
- file_size: 1752299
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`
- width: 1440
- height: 2560
- format: `PNG`
- pillow_openable: true

## 4) Locked copy integrity
- exists: true
- file_size: 1752299
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`
- width: 1440
- height: 2560
- format: `PNG`
- sha256_match_source: True
- pillow_openable: true

## 5) Asset registry update
- file: `productions/chi_yan_tian_qiong/assets/asset_registry.json`
- status set to `locked_after_human_review`
- review_status set to `approved`
- relative_path updated to `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- source_path preserved as output path
- metadata and integrity fields recorded

## 6) Review artifacts
- review template: `productions/chi_yan_tian_qiong/reviews/image_reviews/A-CH-B-SUBJECT-001_cand_001_review.md`
- review record: `productions/chi_yan_tian_qiong/reviews/review_records.jsonl`
- review_id: `review-g4-3-a-ch-b-subject-001`
- decision: `approve`
- target_status_after_decision: `locked_after_human_review`

## 7) Safety and execution scope
- no Dreamina command was executed.
- no new submit happened.
- no query happened.
- no download happened.
- original output file was copied (not moved).
- output was not written outside the workspace.

## 8) pytest result
- `python -m pytest -q`

## 9) Final verdict
- `PHASE_G4_3_LOCKED_ASSET_ACCEPTED`
