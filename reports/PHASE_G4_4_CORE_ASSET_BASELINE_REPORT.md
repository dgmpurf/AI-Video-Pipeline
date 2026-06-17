# Phase G4.4 Core Asset Baseline Report

## 1) Locked asset list
- `A-SC-TEMPLE-COURTYARD-001`
- `A-CH-A-SUBJECT-001`
- `A-CH-B-SUBJECT-001`

## 2) Scene asset verification
- logical_id: `A-SC-TEMPLE-COURTYARD-001`
- candidate_id: `A-SC-TEMPLE-COURTYARD-001_cand_001`
- locked path: `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png`
- exists: true
- file_size: `3563257`
- sha256: `f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0`
- openable: true
- width: `2560`
- height: `1440`
- format: `PNG`

## 3) Fenshou subject asset verification
- logical_id: `A-CH-A-SUBJECT-001`
- candidate_id: `A-CH-A-SUBJECT-001_cand_001`
- locked path: `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- exists: true
- file_size: `1959523`
- sha256: `83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F`
- openable: true
- width: `1440`
- height: `2560`
- format: `PNG`

## 4) Shuangji subject asset verification
- logical_id: `A-CH-B-SUBJECT-001`
- candidate_id: `A-CH-B-SUBJECT-001_cand_001`
- locked path: `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- exists: true
- file_size: `1752299`
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`
- openable: true
- width: `1440`
- height: `2560`
- format: `PNG`

## 5) Registry verification
- `productions/chi_yan_tian_qiong/assets/asset_registry.json` contains all three records.
- all target records are `status: locked_after_human_review`.
- all target records are `review_status: approved`.
- all target records keep `relative_path` under `productions/chi_yan_tian_qiong/locked_refs`.

## 6) Review record verification
- `productions/chi_yan_tian_qiong/reviews/review_records.jsonl` contains approval records for all three candidates.
- each record has `decision: approve`.
- each record has `target_status_after_decision: locked_after_human_review`.

## 7) Review markdown verification
- `productions/chi_yan_tian_qiong/reviews/image_reviews/A-SC-TEMPLE-COURTYARD-001_cand_001_review.md` final decision is `approve`.
- `productions/chi_yan_tian_qiong/reviews/image_reviews/A-CH-A-SUBJECT-001_cand_001_review.md` final decision is `approve`.
- `productions/chi_yan_tian_qiong/reviews/image_reviews/A-CH-B-SUBJECT-001_cand_001_review.md` final decision is `approve`.

## 8) Production status update
- `productions/chi_yan_tian_qiong/PRODUCTION_STATUS.md` updated to:
  - `core_scene_and_main_subjects_locked`
  - scene: `A-SC-TEMPLE-COURTYARD-001`
  - character subjects: `A-CH-A-SUBJECT-001`, `A-CH-B-SUBJECT-001`
  - next phase: `H1 shot-01 keyframe readiness package`

## 9) Safety confirmations
- No Dreamina command was executed during this phase.
- No submit/query/download action happened in this phase.
- No file was written outside `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE`.

## 10) pytest result
- `python -m pytest -q` passed.

## 11) Final verdict
- `PHASE_G4_4_CORE_ASSET_BASELINE_ACCEPTED`
