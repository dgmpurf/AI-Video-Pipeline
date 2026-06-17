# Phase F1.1 Fake Provider Isolation Report

## 1) Provider config result

- `configs/providers.json` does not define `fake_live_provider`.
- `dreamina_cli.allow_live_run` remains false.
- No real API keys are present in provider config.
- `kling_api`, `hailuo_api`, `runway_api`, and `midjourney_image` remain disabled stubs.
- If `fake_live_provider` is ever added to production config, it must remain disabled with mode `test_only` and live-run disabled.

## 2) Fake provider isolation policy

- `fake_live_provider` is available only for tests and fixture manifests.
- Fake live-run requires provider config mode `fake_live`.
- Fake live-run also requires explicit `test_context=true`.
- The runner instantiates `FakeLiveProvider` only when `test_context=true` is present.
- Production config does not enable the fake provider.

## 3) Production manifest validation result

- `tests/fixtures/live_fake/fake_live_manifest.csv` may use `fake_live_provider`.
- Manifests under `productions/<production_id>/manifests/` reject `fake_live_provider`.
- Any non-fixture manifest using the fake provider is rejected by parser validation.

## 4) Live gate result

- Fake provider gate approval requires user confirmation.
- Fake provider gate approval requires exactly one task.
- Fake provider gate approval requires dry-run proof.
- Fake provider gate approval requires an approved fs write plan.
- Fake provider gate approval requires staged media when the task has references.
- Planned output paths and staged media must stay inside the workspace.
- Dreamina CLI remains denied.

## 5) Runner result

- Production runner cannot silently switch to `FakeLiveProvider`.
- `FakeLiveProvider` is created only from a temporary test config with explicit test context.
- Mock-run remains non-real-provider behavior.
- Live-run with default Dreamina config is denied before submit.
- Live-run with fake provider outside test context is denied.

## 6) Pytest result

- Command: `python -m pytest -q`
- Result: passed with exit code 0.

## 7) Dreamina execution proof

- No Dreamina command was executed.
- No real submit, query, or download operation was run.
- Tests monkeypatch subprocess calls and confirm no subprocess execution.

## 8) External path proof

- No external path was touched by this audit.
- No parent directory was scanned.
- Planned output paths outside the workspace are denied by `PathPolicy`.

## 9) Final verdict

- `PHASE_F1_1_ACCEPTED`
