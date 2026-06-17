# Phase G2.3 Fenshou Subject Locked Asset Baseline Report

## 1) locked target
- logical_id: `A-CH-A-SUBJECT-001`
- candidate_id: `A-CH-A-SUBJECT-001_cand_001`

## 2) output paths
- locked path: `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- source output path: `productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/output/A-CH-A-SUBJECT-001_fenshou_full_body_subject.png`

## 3) integrity verification
- file exists: true
- file size: `1959523`
- sha256: `83E21FE549D737A4AC7FDBC23D9B883526F5AEBC668BDB1E107A149244A13D2F`
- Pillow openable: true
- width: `1440`
- height: `2560`
- format: `PNG`

## 4) registry verification
- `productions/chi_yan_tian_qiong/assets/asset_registry.json` contains entry:
  - `logical_id = A-CH-A-SUBJECT-001`
  - `candidate_id = A-CH-A-SUBJECT-001_cand_001`
  - `status = locked_after_human_review`
  - `review_status = approved`
  - `relative_path` points to `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
  - `source_path` preserves `productions/chi_yan_tian_qiong/runs/live/20260613_162002_A-CH-A-SUBJECT-001/output/A-CH-A-SUBJECT-001_fenshou_full_body_subject.png`

## 5) review verification
- review record exists in `productions/chi_yan_tian_qiong/reviews/review_records.jsonl` for `A-CH-A-SUBJECT-001 / A-CH-A-SUBJECT-001_cand_001` with `decision: approve`
- review template has final decision `approve`:
  `productions/chi_yan_tian_qiong/reviews/image_reviews/A-CH-A-SUBJECT-001_cand_001_review.md`

## 6) production status update
- `productions/chi_yan_tian_qiong/PRODUCTION_STATUS.md` updated:
  - first scene asset locked: `A-SC-TEMPLE-COURTYARD-001`
  - first character subject asset locked: `A-CH-A-SUBJECT-001`
  - current production status: `scene_and_first_character_subject_locked`
  - next recommended asset: `A-CH-B-SUBJECT-001`
  - next phase: `G3 Shuangji character subject readiness package`

## 7) safety proof
- No Dreamina command was executed.
- No submit happened.
- No query happened.
- No download happened.
- No external path was touched.

## 8) pytest result
- `python -m pytest -q` executed.

## 9) final verdict
- `PHASE_G2_3_BASELINE_ACCEPTED`
