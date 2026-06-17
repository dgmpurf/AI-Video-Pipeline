# Phase F2 Dreamina Preflight Report

## 1) Executable check result

- Config path checked: `configs/providers.json`
- Configured executable: `C:/Users/msjpurf/bin/dreamina.exe`
- Executable path matched the provider config exactly.
- Executable existed at preflight time.
- No PATH search was performed.
- No parent directory was scanned.

## 2) Help snapshot paths

- `reports/DREAMINA_CLI_HELP_SNAPSHOT.md`

## 3) Capabilities JSON path

- `configs/dreamina_cli_capabilities.json`

## 4) Command mapping comparison

- `text2image`: expected flags matched help snapshot.
- `image2image`: builder uses repeated `--images`; help snapshot supports `--images`.
- `multimodal2video`: builder uses repeated `--image`; help snapshot supports `--image`, `--duration`, and `--video_resolution`.
- `image2video`: builder uses single `--image` and does not pass `--ratio`.
- `frames2video`: builder uses `--first` and `--last`.
- `query_result`: help snapshot supports `--submit_id` and `--download_dir`.
- `download_dir` remains query/download-phase only and is not included in submit previews.

## 5) Warnings

- No command mapping warnings were produced by the current help snapshot comparison.

## 6) Preflight command previews

- Output directory: `reports/preflight_command_previews/`
- `TEST-PREFLIGHT-I2I`: argv JSON, readable command, and validation JSON generated.
- `TEST-PREFLIGHT-M2V`: argv JSON, readable command, and validation JSON generated.
- `TEST-PREFLIGHT-I2V`: argv JSON, readable command, and validation JSON generated.
- `image2image` preview uses repeated `--images`.
- `multimodal2video` preview uses repeated `--image`.
- `image2video` preview uses a single `--image`.
- No preview includes `--refs`, `--ref_strength`, or submit-phase `output_dir`.
- Preview media was staged under the workspace with ASCII filenames.

## 7) Live-run disabled proof

- `dreamina_cli.allow_live_run` remains false in `configs/providers.json`.
- `PipelineRunner.can_run_live()` remains false with default config.
- Live-run with `dreamina_cli` remains denied before submit.
- Fake provider remains test-only and absent from production provider config.

## 8) No submit, query, or download proof

- Only Dreamina help commands with `-h` were run.
- No generation command was submitted.
- No `query_result` command was run with a submit id.
- No command was run with a download directory.
- No provider live-run was executed.

## 9) External path safety proof

- Reports, capabilities, previews, and staged preview media were written inside the workspace.
- No external staging directory was created.
- No old project path was accessed.

## 10) Pytest result

- Command: `python -m pytest -q`
- Result: passed with exit code 0.

## 11) Final verdict

- `PHASE_F2_ACCEPTED`
