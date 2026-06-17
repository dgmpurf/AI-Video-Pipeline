# Phase F1 Fake Live Full Loop Report

## 1) Implemented modules

- `app/ai_video_pipeline/providers/fake_live_provider.py`
- `app/ai_video_pipeline/execution/live_gate.py`
- `app/ai_video_pipeline/execution/runner.py`
- `app/ai_video_pipeline/core/models.py`
- `tests/fixtures/live_fake/fake_live_manifest.csv`
- `tests/test_phase_f1.py`

## 2) Fake provider scenarios

- `submit_then_querying`
- `submit_then_success`
- `submit_then_fail`
- `submit_then_success_download`
- `submit_interrupted_before_query`
- `success_downloaded_not_renamed`

## 3) Live gate behavior

- Fake live-run can pass only when the provider is configured with `mode=fake_live` and `allow_live_run=true`.
- User confirmation, single-task mode, dry-run proof, approved fs write plan, staged media, and workspace-bound paths are required.
- Default Dreamina CLI config remains denied.

## 4) Single-task enforcement

- Gate validation denies multi-task live-run requests.
- Runner live-run remains a single-task skeleton for fake provider testing.

## 5) fs_write_plan requirement

- The gate requires an existing fs write plan.
- The plan must be valid JSON with `approved=true`.
- Planned files must resolve inside the workspace.

## 6) Staged media requirement

- Tasks with references require staged media.
- Staged media must exist and stay inside the workspace.
- External staging is denied.

## 7) Immediate submit id persistence proof

- Fake submit writes submitted rows, provider requests, provider responses, job store, and execution log before fake query.
- The interruption test stops after submit, reloads `job_store.json`, and resumes as `submitted_query_only`.

## 8) Fake success path proof

- Fake submit returns deterministic ids.
- Fake query returns success for success scenarios.
- Fake download writes inside the live run `downloads` directory.
- The runner renames the downloaded fake output into the live run `output` directory.
- Completed and downloaded CSV artifacts are written.

## 9) Fake interruption and resume proof

- Submitted resumes as `submitted_query_only`.
- Querying resumes as `querying_query_only`.
- Success resumes as `success_download_only`.
- Downloaded resumes as `downloaded_rename_only`.
- Completed resumes as `completed_skip`.
- Failed resumes as `failed_requires_user_decision`.

## 10) Fake download and rename proof

- Downloaded files are created only under `productions/<production_id>/runs/live/<run_id>/downloads`.
- Renamed outputs are written under `productions/<production_id>/runs/live/<run_id>/output`.
- No locked refs path is used.

## 11) Output integrity proof

- The rename path checks that the final output exists and has nonzero size.
- Tests verify the final fake output content and workspace containment.

## 12) Dreamina disabled proof

- Default `dreamina_cli.allow_live_run` remains false.
- `PipelineRunner.execute(RunMode.live)` remains blocked by runtime live-run controls.
- Fake live tests monkeypatch `subprocess.run` and verify no subprocess call occurs.

## 13) External path safety proof

- `PathPolicy` validates staged media, fs write plans, planned output files, downloads, and renamed outputs.
- External planned output paths are denied.

## 14) Pytest result

- Command: `python -m pytest -q`
- Result: passed with exit code 0.

## 15) Final verdict

- `PHASE_F1_ACCEPTED`
