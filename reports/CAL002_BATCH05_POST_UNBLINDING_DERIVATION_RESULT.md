# CAL-002 Batch05 Post-Unblinding Derivation Result

## 1. Starting repository checkpoint

- Branch: `main`
- Starting HEAD / origin/main: `972164f2dde5f4122dab8b25236fa4756ae84552`
- Starting commit: `review(cal002): lock Batch05 blind visual record`
- Starting parent: `d737316deab6da847dcae65fa229e2e58712b3ae`
- Parent-to-HEAD transition: exactly `4` additions, `0` modifications, `0` deletions, `0` renames, and `0` unexpected paths.
- Staged files, tracked modifications, and Source modifications at preflight: `0`.

## 2. Blind lock checkpoint and bindings

- Blind lock checkpoint: `972164f2dde5f4122dab8b25236fa4756ae84552`
- Lock ID: `CAL002-BATCH05-BLIND-LOCK-923B054F`
- Lock governance report: `reports/CAL002_BATCH05_PHASE1_BLIND_REVIEW_RECORD_LOCK_RESULT.md`
- Lock governance report bytes / SHA-256: `4210` / `5d31d1c651aa5b92f2dcd9b1fda0723ff51f1f99310b1e80996c4f2302f4d0b0`
- Lock governance decision: `CAL002_BATCH05_BLIND_REVIEW_RECORD_LOCKED_READY_FOR_POST_UNBLINDING_DERIVATION`
- Blind record: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_records/CAL002-BATCH05-BLIND-85BB78B1/blind_review_record_final.json`
- Blind record bytes / SHA-256: `13492` / `923b054f575743f80f7d3b222fd52ee9d2f95c510dfda61459c06f0abf36a8b8`
- Blind report: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_records/CAL002-BATCH05-BLIND-85BB78B1/blind_visual_review_report.md`
- Blind report bytes / SHA-256: `9494` / `db08aea351393e7308dbd468292eab6acda5d92fad3d40048463035c102f63aa`
- Blind lock manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_records/CAL002-BATCH05-BLIND-85BB78B1/blind_review_lock_manifest.json`
- Blind lock manifest bytes / SHA-256: `2905` / `208a8081585adf8797e43354e0e828f4e3b3c92ab3ab9be285d88e27ee6f721d`
- All four lock inputs equal their current `HEAD` blobs.
- The blind record was finalized, locked, and committed before treatment-mapping access.
- The blind record remained byte-for-byte unchanged during and after derivation.

## 3. Tool, schema, and mapping-source bindings

- Python executable: `C:/Users/msjpurf/AppData/Local/Programs/Python/Python310/python.exe`
- Derivation tool: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py`
- Tool version: `CAL002_BATCH05_REVIEW_DERIVATION_TOOL_V0_2`
- Tool bytes / SHA-256: `35997` / `1bff976a6e14c96184936e81db1baf8df4a2154526c1f8770ac4b45c63388321`
- Executing path and bytes equal the expected repository tool and its `HEAD` blob: `true`
- Blind schema: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json`
- Blind schema ID / record version: `CAL002_BATCH05_BLIND_VISUAL_REVIEW_SCHEMA_V0_3` / `CAL002_BATCH05_BLIND_VISUAL_REVIEW_RECORD_V0_3`
- Blind schema bytes / SHA-256: `18138` / `9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5`
- Post-unblinding schema: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_post_unblinding_analysis_schema.json`
- Post schema ID / record version: `CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_SCHEMA_V0_3` / `CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_3`
- Post schema bytes / SHA-256: `18899` / `366a8dac88504626ec400317c116e20c319c70c693a29927fa1753fcb46f396a`
- Both schemas are strict canonical JSON, valid Draft 2020-12 schemas, and equal their `HEAD` blobs.
- Design manifest binding reported by the tool: `17561` bytes / `c3a5265a5e21b90ca993f62892ba0dececf6b34fc8545e5a01e49835f7945574`
- Task matrix binding reported by the tool: `3571` bytes / `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32`

## 4. Derive and verify invocations

- Derive invocation count: `1`
- Derive shell mode / overwrite flag: `false` / `absent`
- Derive argv element count / SHA-256: `9` / `778a5b569363317bb113b82233c3c6a7b5bca248b990816eba004fec8efb8353`
- Derive exit code: `0`
- Derive stdout bytes / SHA-256: `386` / `e95c516e7a24642baa83012f1ddc7067a17c2244ec5a1698f5f9fcabfd04e785`
- Derive stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Verify invocation count: `1`
- Verify shell mode / write performed: `false` / `false`
- Verify argv element count / SHA-256: `9` / `2d2502b00ffddd6724e0e41e43a98b92a48c42b26b9ddcdfdf9c463e9657648b`
- Verify exit code: `0`
- Verify stdout bytes / SHA-256: `199` / `08103071ff3c682297236c5d3646121bd1b342b3d41941ce497e6d49b68ae4ea`
- Verify stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Byte-for-byte deterministic re-derivation: `PASS`
- Derived record unchanged before and after verify: `true`

## 5. Derived record

- Path: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/post_unblinding_records/CAL002-BATCH05-POST-923B054F/post_unblinding_analysis.json`
- Bytes / SHA-256: `5784` / `1cdc124764aa4e35ea7463cb54b8a039a932d5d00dac18c68fe690550e981c96`
- Schema version: `CAL002_BATCH05_POST_UNBLINDING_ANALYSIS_RECORD_V0_3`
- Strict canonical JSON validation: `PASS`
- Post-unblinding schema validation: `PASS`
- Pair derivation count: `4`
- Family summary count: `2`

## 6. Pair derivations

| Pair ID | Candidate side | Control side | Blind preference | Derivation class | Candidate clear advantage |
| --- | --- | --- | --- | --- | --- |
| `PUSH_PAIR_01` | `B` | `A` | `A_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |
| `PUSH_PAIR_02` | `A` | `B` | `B_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |
| `IMPACT_PAIR_01` | `A` | `B` | `B_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |
| `IMPACT_PAIR_02` | `B` | `A` | `A_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |

All four comparisons were `VALID`. In every pair, the blind preference selected the Control side.

## 7. Family summaries

### push_reaction

- Candidate / Control primary-pass counts: `0 / 0`
- Valid comparisons: `2`
- Candidate / Control clear-advantage counts: `0 / 2`
- No-clear-advantage / invalid / inconclusive counts: `0 / 0 / 0`
- Candidate / Control action-family mismatch counts: `0 / 0`
- Candidate / Control technical-invalid counts: `0 / 0`
- Derived flags: `both_treatments_frequently_fail=true`, `candidate_repeated_wrong_family=false`, `candidate_worse_than_control=true`, `uncontrolled_variation_prevents_comparison=false`
- Family-level result: `ROUTE_RESET_REQUIRED`
- Rationale: `Rule 1 ROUTE_RESET_REQUIRED: both_treatments_frequently_fail=true; uncontrolled_variation_prevents_comparison=false.`

### brief_impact_recoil

- Candidate / Control primary-pass counts: `0 / 0`
- Valid comparisons: `2`
- Candidate / Control clear-advantage counts: `0 / 2`
- No-clear-advantage / invalid / inconclusive counts: `0 / 0 / 0`
- Candidate / Control action-family mismatch counts: `1 / 0`
- Candidate / Control technical-invalid counts: `0 / 0`
- Derived flags: `both_treatments_frequently_fail=true`, `candidate_repeated_wrong_family=false`, `candidate_worse_than_control=true`, `uncontrolled_variation_prevents_comparison=false`
- Family-level result: `ROUTE_RESET_REQUIRED`
- Rationale: `Rule 1 ROUTE_RESET_REQUIRED: both_treatments_frequently_fail=true; uncontrolled_variation_prevents_comparison=false.`

## 8. Derivation provenance

- Mapping access was performed only by the committed deterministic tool during the single `derive` and single `verify` calls.
- No mapping table or pair/family result was manually authored before tool execution.
- The post-unblinding analysis values were generated by the committed deterministic tool and the derived record was not manually edited or replaced.
- This report and the execution receipt only bind and summarize values from that unchanged tool-generated record.
- Derivation receipt: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/post_unblinding_records/CAL002-BATCH05-POST-923B054F/derivation_execution_receipt.json`
- Derivation receipt bytes / SHA-256: `6249` / `149762df4d4c3d41405a5df5eada93c41595111ed2e6473f19e56a1647def229`

## 9. Experimental interpretation boundary

- Statistical-significance claim permitted: `false`
- Component-level causal attribution permitted: `false`
- Cross-action-generalization claim permitted: `false`
- The family treatment remains a compound treatment.
- No ACTION_RULE or Source-update candidate was created in this phase.

## 10. No-live and protected-state confirmation

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Submit/query/download/retry/resubmit/batch and login/session operations: `false`
- Media created or changed: `false`
- Sources changed: `false`
- Existing blind records, artifacts, media, execution evidence, packages, Prompts, Batch05 design files, Sources, and prior reports changed: `false`
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## 11. Decision

- Decision: `CAL002_BATCH05_POST_UNBLINDING_DERIVATION_COMPLETE_READY_FOR_INDEPENDENT_NO_LIVE_AUDIT`
- Evidence manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/post_unblinding_records/CAL002-BATCH05-POST-923B054F/post_unblinding_evidence_manifest.json`
- Next phase: `CAL002_BATCH05_POST_UNBLINDING_DERIVATION_INDEPENDENT_NO_LIVE_AUDIT`
