# Phase F6.3 Lock Scene Asset

## 1) task and approval inputs
- `logical_id: A-SC-TEMPLE-COURTYARD-001`
- `candidate_id: A-SC-TEMPLE-COURTYARD-001_cand_001`
- `submit_id: 821c2865-26da-4c70-939f-07b4eb5a96d8`
- `final decision: approve`
- `reviewer: user`
- `review note: User-approved for production scene lock after manual visual review.`

## 2) source image
- source image path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\output\A-SC-TEMPLE-COURTYARD-001_ancient_temple_rain_courtyard.png`
- source copy target path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png`

## 3) integrity checks on output
- exists: True
- file_size: `3563257`
- sha256: `f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0`
- pillow_openable: True
- width: `2560`
- height: `1440`
- format: `PNG`

## 4) registry updates
- file: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\assets\asset_registry.json`
- status: `locked_after_human_review`
- review_status: `approved`
- relative_path updated to locked reference path.
- source_path preserved as original run output path.
- tags now include `locked_ref` and `production_asset` in addition to prior tags.

## 5) review artifacts
- review template updated: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\reviews\image_reviews\A-SC-TEMPLE-COURTYARD-001_cand_001_review.md`
- final decision set to `approve`.
- review note added.
- review record appended: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\reviews\review_records.jsonl`
- recorded fields include `source_path` and `locked_path`.

## 6) safety confirmations
- no Dreamina command was executed in this phase.
- no new submit / query / download was performed.
- no Dreamina config or provider runtime toggle was modified.
- no external path was touched; all changed files are under `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE`.
- image was copied (not moved) to `locked_refs`.
- no existing production locked reference was reused.

## 7) pytest result
- Result: passed with exit code `0` from `python -m pytest -q`.

## 8) final verdict
- `PHASE_F6_3_LOCKED_ASSET_ACCEPTED`
