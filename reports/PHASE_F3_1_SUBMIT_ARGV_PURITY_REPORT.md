# Phase F3.1 Submit Argv Purity Report

## 1) Where `--output_name` was found
- `app/ai_video_pipeline/providers/dreamina_cli.py`: previous command builder appended `--output_name` to every submit argv.
- Previous F3 readiness report, readiness summary, provider request, and command preview contained the stale submit flag before regenerated artifacts were created.
- Current F3 artifacts are regenerated from the corrected builder and do not include `--output_name` in submit argv.

## 2) Module fixed
- Fixed `app/ai_video_pipeline/providers/dreamina_cli.py`.
- Submit argv is constructed per Dreamina command type, with only provider-supported submit flags.
- `app/ai_video_pipeline/providers/dreamina_preflight.py` preview validation treats pipeline-only fields as forbidden preview tokens.

## 3) Corrected text2image argv
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "text2image",
  "--model_version",
  "5.0",
  "--ratio",
  "16:9",
  "--prompt",
  "A simple cinematic ancient temple courtyard in light rain, wet stone ground, wooden hall, prayer flags, cool misty atmosphere, no characters, no text, no watermark.",
  "--resolution_type",
  "2k"
]
```

## 4) output_name preservation
- `TaskSpec.output_name` remains required by manifest parsing.
- `ProviderRequest.output_name` remains present as metadata.
- `run_plan.json` and `job_store.json` still preserve `output_name` for internal tracking.
- Download and post-download rename paths continue to use `output_name` internally.

## 5) Submit argv purity confirmation
- `output_name` is not in the corrected submit argv.
- `output_dir`, `local_output_path`, `download_dir`, `rename_path`, `review_status`, `notes`, `status`, `provider_task_id`, and `submit_id` are not submit argv fields.
- Corrected text2image argv includes only `text2image`, `--model_version`, `--ratio`, `--prompt`, and `--resolution_type` after the executable.

## 6) Safety confirmations
- No Dreamina command was executed.
- No submit command was executed.
- No query_result command was executed.
- No download command was executed.
- Dreamina live-run remains disabled in provider config.
- No external path was touched.
- No parent directory was scanned.

## 7) Pytest result
- Result: passed with exit code 0.

## 8) Final verdict
- `PHASE_F3_1_ACCEPTED`

