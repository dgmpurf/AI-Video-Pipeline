# CAL-001 Authorization Serialization Compiler No-Live Implementation Result

## Phase Summary

- phase_id: `CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_NO_LIVE_IMPLEMENTATION`
- task_type: no-live repository engineering
- starting_checkpoint: `a838723b8824a1003b6abab220257d0e20fa31ad`
- starting_branch: `main`
- starting_local_HEAD_matches_origin_main: `true`
- implementation_status: `complete`
- implementation_decision: `new bounded governance primitive; no equivalent complete implementation existed`
- provider_execution_authorized: `false`
- execution_authority_activated: `false`

The local `sources/` mirror already showed the human-managed V1.11-to-V1.12 replacement and the new authorization serialization Source as pre-existing worktree changes. The Goal's explicit Source-mirror exception treated those exact paths as informational. This phase did not create, edit, delete, rename, move, stage, commit, or push any Source path.

## Files Inspected

- `pyproject.toml`
- `app/ai_video_pipeline/`
- `app/ai_video_pipeline/execution/dreamina_evidence.py`
- existing `tests/` and `tools/` layout
- `sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md` read-only local mirror
- `sources/AI视频制作_Source索引与使用优先级_V1.12.md` read-only local mirror
- `experiments/CAL-001/authorizations/CAL001_P3D_W01_F06_recovery_one_query_only_reauthorization_R2.json`
- `experiments/CAL-001/authorizations/CAL001_P3D_W01_F06_recovery_one_download_only_authorization.json`
- `experiments/CAL-001/authorizations/CAL001_P3D_W01_F06_recovery_review_artifact_creation_authorization.json`
- `experiments/CAL-001/authorizations/CAL001_P3D_W01_F06_recovery_visual_review_record_and_technical_completion_authorization.json`
- `reports/PHASE_CAL001_P3D_W01_F06_RECOVERY_ONE_QUERY_ONLY_RESULT.md`
- `experiments/CAL-001/execution_state/CAL001_P3C_remaining_77_resumable_execution_state_contract.json`

Historical authorization and execution evidence was read only and was not rewritten.

## Reuse And Implementation Decision

The repository had reusable standard-library conventions for dataclasses, SHA-256, stable JSON evidence, and atomic replacement, but no complete authorization compiler/verifier or governance namespace. The implementation therefore adds one provider-independent library and one thin CLI. It reuses those conventions without importing Dreamina execution code or adding dependencies.

- library: `app/ai_video_pipeline/governance/authorization_serialization.py`
- public exports: `app/ai_video_pipeline/governance/__init__.py`
- CLI: `tools/authorization_compiler.py`
- library tests: `tests/test_authorization_serialization.py`
- CLI tests: `tests/test_authorization_compiler_cli.py`

## Public Contract

Library functions:

- `compile_authorization_bytes(raw_bytes)`
- `compile_authorization_text(exact_text)`
- `verify_authorization_bytes(raw_bytes, expected_record)`
- `verify_authorization_record(raw_bytes, record)`
- `verify_checkpoint_binding(required_checkpoint, local_head, origin_main)`
- `evaluate_activation_eligibility(serialization_result, checkpoint_result)`
- `stable_json_text(payload)` and `stable_json_bytes(payload)`

CLI commands:

- `compile --text-file PATH` or `compile --stdin-exact`
- `verify --text-file PATH --expected-byte-length N --expected-sha256 DIGEST [--expected-base64 VALUE]`
- `verify-record --text-file PATH --record RECORD.json`
- `verify-checkpoint --required-checkpoint SHA --local-head SHA --origin-main SHA`

Every exact-input command supports mutually exclusive raw file or binary stdin input. Optional JSON output uses a same-directory temporary file, flush plus `fsync`, and atomic publication. Existing output is preserved unless `--overwrite` is explicitly supplied.

## Exact Byte Preservation

- File input uses `Path.read_bytes()`.
- Stdin input uses `sys.stdin.buffer.read()`.
- UTF-8 decoding is strict and is used only to validate and expose character facts.
- SHA-256 and Base64 are computed from the original bytes.
- Canonical input is never stripped, trimmed, case-folded, Unicode-normalized, translated, newline-converted, or repaired.
- BOM, CR, LF, trailing CR, trailing LF, trailing space, and Markdown fences are reported separately.
- Invalid UTF-8 and the default-profile contaminants produce deterministic failures while preserving all available byte facts.

The code contains no canonical-input use of `strip`, `rstrip`, `lstrip`, or Unicode normalization.

## Deterministic Output

- Pure result objects contain no timestamp, environment value, machine-specific path, or mutable counter.
- JSON uses stable field types, sorted keys, ASCII-safe escaping, two-space indentation, UTF-8 bytes, and one final LF.
- Compile, verify, record verification, checkpoint binding, and activation eligibility never call Git, Dreamina, or a provider.
- Both success and failure retain `execution_authority_active=false`, `provider_command_allowed=false`, `provider_command_invocation_count=0`, and `authorized_operation_count_consumed=0`.

## Historical Compatibility Results

All required committed successful fixtures reproduced their canonical byte length, SHA-256, and Base64 and passed record verification:

| Fixture | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| F06 recovery query R2 | 432 | `0f4306d42084ab96044eea5a89d338e0cf1e41c31e39d8df85b25a15626fe883` | pass |
| F06 recovery download | 607 | `e56a37cc5e7f17aaa691ec4e5862fa9253e1a0273221523f9b2a2c172601ff4a` | pass |
| F06 review-artifact creation | 583 | `472da91ce12a778f6505844fb52e80a86dd2c1e11cafd469c344cfe08d4df1a1` | pass |
| F06 visual-review record | 1036 | `e50c231685d549167eeb71ce229e3f61e17ad392da1fc1468aa41d9ccdcb2632` | pass |

The verifier recognizes the existing repository aliases `locally_derived_base64`, `locally_generated_base64`, and `authorization_base64` while keeping the decoded canonical bytes authoritative.

## Historical R1 Negative Result

The blocked R1 report was parsed as a regression fixture. Its canonical text and declared values match at 416 bytes with SHA-256 `2ffc26a260839d345c65a51ef6ed83eb0805725a6e844f2f51ec6fb3a46fb2c3`, while the supplied Base64 decodes to different same-length bytes with SHA-256 `f5eb16120e865791f0444a8f0e45cf85aedf141d8f1334c7795196bfb5704b11`.

Result: `authorization_verified=false`, `eligible_for_authority_activation=false`, no authority activated, no provider command allowed, and no operation count consumed.

## Verification Results

Commands:

```text
python -m compileall -q app/ai_video_pipeline/governance tools/authorization_compiler.py tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
python -m pytest -o addopts= -q tests/test_authorization_serialization.py tests/test_authorization_compiler_cli.py
python -m pytest -o addopts= -q --tb=no
```

Results:

- compile validation: pass
- phase-scoped mandatory regression suite: `32 passed, 0 failed`
- full repository suite: `500 passed, 10 failed`
- full-suite failures attributable to this change: `0`

The ten existing repository-suite failures are baseline fixture/state issues outside this phase: nine assertions require uncommitted or absent historical `review_records.jsonl` / `review_records.template.jsonl` files, and one old SHOT-02 assertion expects a production status value that differs in the starting commit. `git ls-tree` and `git show` confirm those conditions at the required starting checkpoint. No out-of-scope historical file was changed to mask them.

## Boundary Confirmation

- Dreamina commands run: `0`
- provider commands run: `0`
- Git discovery inside compiler/verifier: `false`
- Source files changed by this phase: `false`
- historical authorization records changed: `false`
- historical execution records changed: `false`
- CAL-001 completed-task count changed: `false`
- CAL-001 remaining-task count changed: `false`
- F07 called: `false`
- F07 authorized: `false`
- Prompt/package/manifest files changed: `false`
- datasets changed: `false`
- media or review artifacts changed: `false`
- `final_master`: `false`
- `locked`: `false`

## Known Limitations

- This foundation evaluates serialization, record matching, checkpoint binding, and activation eligibility only. It cannot activate execution authority or gate a provider command by itself.
- Checkpoint values must be supplied explicitly; there is intentionally no automatic Git lookup.
- The default profile is the strict single-line AI_VIDEO_PIPELINE profile. It reports and rejects embedded CR or LF rather than converting them.
- Existing authorization records are heterogeneous. The verifier supports the field conventions needed by the required successful fixtures plus common Base64 aliases; it does not rewrite or backfill older schemas.
- The unrelated full-repository baseline failures remain unresolved and outside this Goal.

## Final Verdict

`CAL001_AUTHORIZATION_SERIALIZATION_COMPILER_NO_LIVE_IMPLEMENTATION_COMPLETE_READY_INDEPENDENT_AUDIT`

Next required phase:

`CAL-001_AUTHORIZATION_SERIALIZATION_COMPILER_INDEPENDENT_NO_LIVE_AUDIT`
