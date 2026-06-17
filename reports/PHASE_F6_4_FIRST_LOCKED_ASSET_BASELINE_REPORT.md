# Phase F6.4 First Locked Production Asset Baseline Report

## 1) locked asset identifiers
- logical_id: `A-SC-TEMPLE-COURTYARD-001`
- candidate_id: `A-SC-TEMPLE-COURTYARD-001_cand_001`
- submit_id: `821c2865-26da-4c70-939f-07b4eb5a96d8`

## 2) paths
- locked path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png`
- source run output path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\output\A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png`
- review record path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\reviews\review_records.jsonl`
- review file path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\reviews\image_reviews\A-SC-TEMPLE-COURTYARD-001_cand_001_review.md`
- production status file: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\PRODUCTION_STATUS.md`

## 3) integrity verification
- exists: True
- file_size: `3563257`
- sha256: `f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0`
- Pillow openable: True
- width: `2560`
- height: `1440`
- format: `PNG`

## 4) registry verification
- asset is present in `productions/chi_yan_tian_qiong/assets/asset_registry.json`
- `status: locked_after_human_review`
- `review_status: approved`
- `relative_path` points under `productions/chi_yan_tian_qiong/locked_refs`
- `source_path` preserves original run output path
- `submit_id` matches `821c2865-26da-4c70-939f-07b4eb5a96d8`

## 5) review verification
- review record append exists for `A-SC-TEMPLE-COURTYARD-001 / A-SC-TEMPLE-COURTYARD-001_cand_001` with `decision: approve`
- review file shows `Final decision` as `approve`

## 6) production status update
- `first_scene_asset_locked` recorded in `PRODUCTION_STATUS.md`
- next recommended asset: `A-CH-A-SUBJECT-001`

## 7) safety proof
- No Dreamina command was executed in this phase.
- No submit / query / download was performed.
- `providers.json` was not modified.
- No external path was touched.

## 8) pytest result
- `python -m pytest -q` executed; result: pass with exit code `0`.

## 9) final verdict
- `PHASE_F6_4_BASELINE_ACCEPTED`
