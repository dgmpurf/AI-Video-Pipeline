# Phase F3.2 Run ID Naming Report

## 1) Where double timestamp came from
- `create_run_dir` always prepended a fresh timestamp to the label it received.
- The Phase F3.1 regeneration path passed a caller-created timestamped `run_id`.
- The resulting basename combined both values into a double timestamp.

## 2) Files fixed
- `app/ai_video_pipeline/execution/run_context.py`
- `tests/test_phase_f3_2.py`
- `reports/PHASE_F3_DREAMINA_SINGLE_TASK_READINESS_REPORT.md`
- `reports/PHASE_F3_1_SUBMIT_ARGV_PURITY_REPORT.md`
- `reports/dreamina_preflight_text2image_001_readiness_summary.json`

## 3) Old run_dir example
- `productions/chi_yan_tian_qiong/runs/dry_run/20260613_133659_20260613_213659_dreamina_preflight_text2image_001`

## 4) New run_dir example
- `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\dry_run\20260613_135650_dreamina_preflight_text2image_001`
- Run ID: `20260613_135650_dreamina_preflight_text2image_001`
- Basename contains exactly one `YYYYMMDD_HHMMSS` timestamp.
- Run ID and run directory basename match.

## 5) Naming policy
- Run directory pattern is `productions/<production_id>/runs/<run_mode>/<timestamp>_<safe_task_or_batch_name>/`.
- Existing timestamp prefixes are stripped from supplied labels before the run context adds one timestamp.
- `output_name` does not affect run directory naming unless a caller explicitly uses it as a label.
- Run directory remains inside the workspace through `PathPolicy`.

## 6) Test result
- Result: passed with exit code 0.

## 7) Safety confirmations
- No Dreamina command was executed.
- No submit command was executed.
- No query_result command was executed.
- No download command was executed.
- Live-run remains disabled.
- `configs/providers.json` was not modified to allow live-run.
- No external path was touched.
- No parent directory was scanned.

## 8) Final verdict
- `PHASE_F3_2_ACCEPTED`

