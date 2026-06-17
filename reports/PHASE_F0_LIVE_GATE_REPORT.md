# Phase F0 Live Gate Report

## 1) Implemented modules

- `app/ai_video_pipeline/execution/live_gate.py`
- `app/ai_video_pipeline/providers/fake_live_provider.py`
- `app/ai_video_pipeline/execution/resume_state.py`
- `app/ai_video_pipeline/execution/runner.py`

## 2) Live-run gate rules

- Live-run is denied unless provider config explicitly sets `allow_live_run` to true.
- Explicit user confirmation is required.
- Exactly one task is required.
- A dry-run id is required as dry-run proof.
- An approved fs write plan is required.
- Planned output paths must stay inside the workspace.
- Referenced media must be staged inside the workspace before live-run is allowed.

## 3) Single-task enforcement

- `LiveRunRequest.allow_single_task_only` must be true.
- Gate validation denies empty or multi-task live-run requests.
- Batch and parallel live-run are outside Phase F0 scope.

## 4) fs_write_plan requirement

- Gate validation requires `fs_write_plan_path`.
- The plan must exist, be valid JSON, and include `approved: true`.
- Every planned file is validated with `PathPolicy`.

## 5) Staged media requirement

- Tasks with references require staged media paths.
- Every staged path is validated with `PathPolicy`.
- Missing staged files deny the request before submit.

## 6) Submit id immediate persistence

- Fake live submit returns deterministic `submit_id` and `provider_task_id`.
- The runner immediately writes `submitted_tasks.csv`, `provider_requests.jsonl`, `provider_responses.jsonl`, `job_store.json`, and `execution_log.txt`.
- This write happens before query.
- The interrupted-after-submit test loads `job_store.json` and resumes as `submitted_query_only`.

## 7) Resume behavior

- `submitted` resumes as `submitted_query_only`.
- `querying` resumes as `querying_query_only`.
- `success` resumes as `success_download_only`.
- `downloaded` resumes as `downloaded_rename_only`.
- `completed` skips.
- `failed` requires a user decision.
- Existing dry-run and mock-run resume behavior remains compatible.

## 8) Fake provider test behavior

- `FakeLiveProvider` builds a fake command preview.
- `submit` returns fake ids.
- `query` returns configured fake status.
- `download` writes a fake file inside the live run directory.
- It never invokes Dreamina or writes external paths.

## 9) Real Dreamina execution proof

- Production `configs/providers.json` remains unchanged with `dreamina_cli.allow_live_run` set to false.
- `PipelineRunner.execute(RunMode.live)` remains blocked by runtime live-run controls.
- Direct `live_run` calls with default Dreamina config are denied by `LiveRunGate` before submit.
- Tests monkeypatch `subprocess.run` and verify no subprocess call occurs.

## 10) Default Dreamina disabled proof

- `PipelineRunner.can_run_live()` remains false with default config.
- `dreamina_cli` is not enabled for real live-run in Phase F0.

## 11) Pytest result

- Command: `python -m pytest -q`
- Result: passed with exit code 0.

## 12) Final verdict

- `PHASE_F0_ACCEPTED`
