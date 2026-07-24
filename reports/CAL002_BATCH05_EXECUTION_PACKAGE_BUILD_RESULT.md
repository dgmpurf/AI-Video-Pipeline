# CAL-002 Batch05 Execution Package Build Result

## 1. Starting Checkpoint

```text
phase = CAL002_BATCH05_EXECUTION_PACKAGE_BUILD_NO_LIVE
goal_identity = CAL002_BATCH05_EXECUTION_PACKAGE_BUILD_NO_LIVE_V0_1
starting_HEAD = 2575d1a7a7ed7215d06d715c6603495c809d8005
starting_origin/main = 2575d1a7a7ed7215d06d715c6603495c809d8005
branch = main
preflight = PASS
```

## 2. Independent Audit Binding

```text
path = reports/CAL002_BATCH05_REVIEW_DERIVATION_IMPLEMENTATION_PROVENANCE_FIX_INDEPENDENT_NO_LIVE_AUDIT_RESULT.md
byte_length = 20684
sha256 = b262c6ac1db837b2276632b909add688695aef408783312a274bfc1f7b98e95b
decision = CAL002_BATCH05_IMPLEMENTATION_PROVENANCE_FIX_READY_FOR_EXECUTION_PACKAGE_BUILD_NO_LIVE
specific_verdict = READY
```

## 3. Active Project Source Interpretation

```yaml
active_project_source_index: V1.13
active_prompt_compiler: V0.3
active_rolling_state: V0.1
active_by_current_human_instruction: true
embedded_candidate_status_text_stale: true
local_source_sync_authorized: false
ACTION_RULE_V0.4_official_source_status: false
ACTION_RULE_V0.4_stable_general_rule: false
ACTION_RULE_V0.4_not_general_default: true
```

No Source file was modified or synchronized. Prompt bytes were reconstructed
from the committed Batch05 design manifest.

## 4. Runtime Version And Help Preflight

Only these commands were called:

```text
C:/Users/msjpurf/bin/dreamina.exe version
C:/Users/msjpurf/bin/dreamina.exe text2video -h
```

```text
runtime_version = 2a20fff-dirty
runtime_commit = 2a20fff
runtime_build_time = 2026-06-26T06:36:39Z
version_exit = 0
version_stdout_bytes = 96
version_stdout_sha256 = 25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0
version_stderr_bytes = 0
version_stderr_sha256 = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
text2video_help_exit = 0
help_stdout_bytes = 1708
help_stdout_sha256 = 17e92789fc0633fa2563a3f3260865a955c08813d55deb681f4c7936ba2ecde4
help_stderr_bytes = 0
help_stderr_sha256 = e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## 5. Runtime Command-Contract Decision

The current help supports `text2video`, `seedance2.0_vip`, duration 5,
ratio `16:9`, video resolution `720p`, and `--prompt`.

```text
command_contract_valid = true
runtime_preflight = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/runtime_command_contract_preflight.json
runtime_preflight_bytes = 6658
runtime_preflight_sha256 = fedecf44d5b3da7f0d971cd178a4f960f469eef4be006bb8c0a01e0b9f83284b
```

## 6. Four Canonical Prompt Bindings

| Cell | Prompt path | Bytes | SHA-256 |
|---|---|---:|---|
| PUSH_CONTROL | experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/prompts/PUSH_CONTROL_prompt.txt | 1349 | `ace62979b13a2f7994b36673c51ae6bb3f6a6398a71725d2434333445719a604` |
| PUSH_CANDIDATE | experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/prompts/PUSH_CANDIDATE_prompt.txt | 1764 | `e44db0e244923fd3abe701f4118e23687e47fb064cba7aadd6396cfafe963c86` |
| IMPACT_CONTROL | experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/prompts/IMPACT_CONTROL_prompt.txt | 1382 | `dfff87157e2071794c0e2150ded60c68f8787d06117986238f39be41fd76a14b` |
| IMPACT_CANDIDATE | experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/prompts/IMPACT_CANDIDATE_prompt.txt | 1770 | `e14e063895dad06f1c067cc699f93fb04cd3368fbcc8c96a3000bc3473418198` |

All Prompt files use UTF-8 without BOM, LF-only separators, two LF bytes
between blocks, and exactly one terminal LF. They contain no task ID,
replicate ID, blind alias, or review contract.

## 7. Eight Exact Package Identities

| Task | Blind alias | Action family | Treatment | Replicate | Prompt cell |
|---|---|---|---|---|---|
| CAL002-B05-PUSH-CONTROL-R01 | PUSH_PAIR_01_A | push_reaction | control | R01 | PUSH_CONTROL |
| CAL002-B05-PUSH-CONTROL-R02 | PUSH_PAIR_02_B | push_reaction | control | R02 | PUSH_CONTROL |
| CAL002-B05-PUSH-CANDIDATE-R01 | PUSH_PAIR_01_B | push_reaction | candidate | R01 | PUSH_CANDIDATE |
| CAL002-B05-PUSH-CANDIDATE-R02 | PUSH_PAIR_02_A | push_reaction | candidate | R02 | PUSH_CANDIDATE |
| CAL002-B05-IMPACT-CONTROL-R01 | IMPACT_PAIR_01_B | brief_impact_recoil | control | R01 | IMPACT_CONTROL |
| CAL002-B05-IMPACT-CONTROL-R02 | IMPACT_PAIR_02_A | brief_impact_recoil | control | R02 | IMPACT_CONTROL |
| CAL002-B05-IMPACT-CANDIDATE-R01 | IMPACT_PAIR_01_A | brief_impact_recoil | candidate | R01 | IMPACT_CANDIDATE |
| CAL002-B05-IMPACT-CANDIDATE-R02 | IMPACT_PAIR_02_B | brief_impact_recoil | candidate | R02 | IMPACT_CANDIDATE |

No ninth, reserve, tie-breaker, retry, or hidden package exists.

## 8. Mapping Validation

The task matrix and design-manifest blind mapping agree for all eight task IDs,
aliases, treatments, action families, and replicates. R01 and R02 in every
cell bind the same canonical Prompt path and SHA-256.

## 9. Execution Manifest Validation

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_execution_manifest.csv
byte_length = 4804
sha256 = 0aa486cdac6d96a48c2077919e0a17ab26798527d1c4b68f554a2ec51efe581d
row_count = 8
unique_task_ids = 8
unique_aliases = 8
unique_package_paths = 8
unique_output_names = 8
four_cells_x_two_replicates = true
all_authority_and_final_fields_false = true
```

## 10. Package-Index Validation

```text
path = experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/batch05_package_index.json
byte_length = 9187
sha256 = e2164ca62606d9d8a9908e98e6b27d6da8f78e67926dead86f29b1ec64a02b61
fixed_task_count = 8
canonical_prompt_count = 4
package_count = 8
estimated_total_credits = 560
package_build_checkpoint_is_not_live_authority = true
future_live_authorization_must_bind_the_committed_package_checkpoint = true
```

## 11. Credit Estimate And Fresh-Credit Limitation

Estimated unit cost is 70 credits and estimated total cost is 560 credits.
No `user_credit` command was called, no current balance was read or claimed,
and `fresh_credit_checked=false` throughout. These values are planning
estimates only.

## 12. Authority Flags

```yaml
provider_authority: false
submit_authorized: false
query_authorized: false
download_authorized: false
retry_authorized: false
resubmit_authorized: false
batch_authorized: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

## 13. Explicit No-Submit Statement

No submit or generation command was executed. The argument plans are inert
structured data and explicitly set executable invocation authority to false.

## 14. Explicit No-Query, Download, Or Retry Statement

No query, download, retry, resubmit, batch, polling, output-directory, or
download-directory operation was executed or authorized.

## 15. Explicit No-Login Or User-Credit Statement

No login, checklogin, session operation, or `user_credit` command was run.
No credential, token, session ID, or current account balance is persisted.

## 16. Explicit No-Media Statement

No media, frame, contact sheet, comparison sheet, blind review record, or
post-unblinding record was created.

## 17. Explicit No-Source-Change Statement

The `sources/` tree remained read-only and unchanged.

## 18. Protected-File Result

Before package creation, 77 protected tracked files across BATCH01-BATCH04,
BATCH05_DESIGN, and existing CAL002 reports were bound by byte length and
SHA-256. Post-build validation re-hashed the same set: all 77 files matched.
The Source tree object remained
`60eedf926ed525a84c1737fbf8d6dd4b39e46077`, and `git diff -- sources/`
remained empty.

```text
protected_preexisting_files_changed = false
protected_snapshot_match = true
sources_changed = false
unexpected_paths = 0
```

## 19. Final Verdict And Next Phase

```text
verdict = CAL002_BATCH05_EXECUTION_PACKAGE_BUILT_READY_FOR_INDEPENDENT_NO_LIVE_AUDIT
next_phase = CAL002_BATCH05_EXECUTION_PACKAGE_INDEPENDENT_NO_LIVE_AUDIT
```

This package build is not live authority. A future live phase must bind the
ending package-build commit after a separate independent package audit.
