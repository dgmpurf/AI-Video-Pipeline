# CAL-002 Batch05 Post-Unblinding Derivation Independent No-Live Audit Result

## 1. Executive decision

- Decision: `CAL002_BATCH05_POST_UNBLINDING_DERIVATION_READY_FOR_EXPERIMENT_RESULT_AND_ROUTE_RESET_DECISION`
- Specific verdict: `INDEPENDENT_AUDIT_PASS_NO_DEFECT`
- Goal identity: `CAL002_BATCH05_POST_UNBLINDING_DERIVATION_INDEPENDENT_NO_LIVE_AUDIT_V0_1`
- The committed post-unblinding result is byte-reproducible, logically correct, correctly bound, and ready for a separate experimental-result acceptance and route-reset decision.
- This audit does not approve production, complete a fixed task, adopt a Source rule, or authorize a route-reset implementation.

## 2. Checkpoint and derivation transition

- Branch: `main`
- Starting HEAD / origin/main: `5bb61fd4cf4b12a8d3372b6d01a5b74266092457`
- Derivation commit parent: `972164f2dde5f4122dab8b25236fa4756ae84552`
- Parent-to-HEAD commit count: `1`
- Derivation commit message: `review(cal002): derive Batch05 post-unblinding results`
- Added paths: `4`
- Modified / deleted / renamed / unexpected paths: `0 / 0 / 0 / 0`
- Staged files, tracked modifications, and Source changes at preflight: `0`
- The four added paths are exactly the derived record, derivation receipt, evidence manifest, and derivation governance report.

## 3. Blind-lock chronology and bindings

- Blind lock commit: `972164f2dde5f4122dab8b25236fa4756ae84552`
- Derivation commit: `5bb61fd4cf4b12a8d3372b6d01a5b74266092457`
- The blind lock commit is the direct parent of the derivation commit.
- The four blind-lock artifacts exist with their current bytes in the lock commit.
- The post-unblinding record and receipt do not exist in the lock commit.
- Therefore the blind record was finalized, locked, and committed before treatment-mapping access.
- Lock ID: `CAL002-BATCH05-BLIND-LOCK-923B054F`
- Lock governance report bytes / SHA-256: `4210` / `5d31d1c651aa5b92f2dcd9b1fda0723ff51f1f99310b1e80996c4f2302f4d0b0`
- Locked blind record bytes / SHA-256: `13492` / `923b054f575743f80f7d3b222fd52ee9d2f95c510dfda61459c06f0abf36a8b8`
- Locked blind report bytes / SHA-256: `9494` / `db08aea351393e7308dbd468292eab6acda5d92fad3d40048463035c102f63aa`
- Blind lock manifest bytes / SHA-256: `2905` / `208a8081585adf8797e43354e0e828f4e3b3c92ab3ab9be285d88e27ee6f721d`
- All four worktree files equal their current `HEAD` blobs.
- Lock evidence records finalized-before-unblinding, locked, and immutable-after-commit as `true`.
- Lock-phase mapping access, post-unblinding, Candidate derivation, and family derivation are all `false`.

## 4. Tool, schema, and mapping audit

- Tool path: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/tools/batch05_review_derivation.py`
- Tool version: `CAL002_BATCH05_REVIEW_DERIVATION_TOOL_V0_2`
- Tool bytes / SHA-256: `35997` / `1bff976a6e14c96184936e81db1baf8df4a2154526c1f8770ac4b45c63388321`
- Blind schema bytes / SHA-256: `18138` / `9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5`
- Post schema bytes / SHA-256: `18899` / `366a8dac88504626ec400317c116e20c319c70c693a29927fa1753fcb46f396a`
- Design manifest bytes / SHA-256: `17561` / `c3a5265a5e21b90ca993f62892ba0dececf6b34fc8545e5a01e49835f7945574`
- Task matrix bytes / SHA-256: `3571` / `141f0c131a28c0cf7a9cda797e0525956cb34d99a4bb8c43fe4f211648d1fc32`
- Every tool, schema, and mapping file equals its current `HEAD` blob.
- Both schemas are strict canonical JSON and valid JSON Schema Draft 2020-12 schemas.
- Complete-source and AST audit: `PASS`
- Executing-path-to-repository-tool and executing-byte-to-HEAD enforcement: `PASS`
- Schema and mapping worktree-to-HEAD enforcement: `PASS`
- Deterministic pair logic and fixed family-decision precedence: `PASS`
- The tool has one subprocess site, limited to read-only `git show`.
- Network, Dreamina, Provider, Git-write, time, random, and environment-decision dependencies: `none`
- Verify-path write operation: `none`

## 5. Committed derived artifacts

- Derivation governance report bytes / SHA-256: `9237` / `dab379be9b7bcbcd4339e036074c74d4792064332e58bb52026279f717b46109`
- Derived record bytes / SHA-256: `5784` / `1cdc124764aa4e35ea7463cb54b8a039a932d5d00dac18c68fe690550e981c96`
- Derivation receipt bytes / SHA-256: `6249` / `149762df4d4c3d41405a5df5eada93c41595111ed2e6473f19e56a1647def229`
- Evidence manifest bytes / SHA-256: `4581` / `5772768824289b14cadca1b9951e018868c5f34458dcfa7c9a756a44f4056821`
- Derived-record V0.3 schema validation: `PASS`
- Receipt invocation and boundary claims: `PASS`
- Evidence manifest counts: `artifact_count=3`, `included_artifact_count=3`, `unique_bound_paths=3`, `self_excluded=true`
- All three artifact bindings and all nine declared input bindings match current worktree and `HEAD` bytes.

## 6. Independent temporary reproduction

- Temporary output location: external system temporary directory
- Temporary output existed before derive: `false`
- Temporary derive invocation count / exit code: `1 / 0`
- Temporary derive shell / overwrite: `false / absent`
- Temporary derive stdout bytes / SHA-256: `308` / `9f14e6b9143f078a0ff1221dff9d74de8e5e96071b67a4488c3bbd30655a17da`
- Temporary derive stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Temporary derived bytes / SHA-256: `5784` / `1cdc124764aa4e35ea7463cb54b8a039a932d5d00dac18c68fe690550e981c96`
- Temporary output equals the committed derived record byte-for-byte: `true`
- Committed-record verify invocation count / exit code: `1 / 0`
- Verify shell / write performed: `false / false`
- Verify stdout bytes / SHA-256: `199` / `08103071ff3c682297236c5d3646121bd1b342b3d41941ce497e6d49b68ae4ea`
- Verify stderr bytes / SHA-256: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Committed derived record unchanged before and after verify: `true`
- Temporary directory and output cleaned: `true`

## 7. Independent pair derivations

| Pair ID | Candidate | Control | Blind preference | Expected and committed class | Candidate clear advantage |
| --- | --- | --- | --- | --- | --- |
| `PUSH_PAIR_01` | `B` | `A` | `A_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |
| `PUSH_PAIR_02` | `A` | `B` | `B_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |
| `IMPACT_PAIR_01` | `A` | `B` | `B_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |
| `IMPACT_PAIR_02` | `B` | `A` | `A_CLEARLY_BETTER` | `CONTROL_CLEAR_ADVANTAGE` | `false` |

- All four comparison-validity values are `VALID`.
- All four blind preferences select the mapped Control side.
- Independent pair reconstruction equals the committed pair records exactly.
- No pair was manually relabelled.

## 8. Independent family summaries

### push_reaction

- Candidate / Control primary passes: `0 / 0`
- Valid comparisons: `2`
- Candidate / Control clear advantages: `0 / 2`
- No-clear / invalid / inconclusive comparisons: `0 / 0 / 0`
- Candidate / Control action-family mismatches: `0 / 0`
- Candidate / Control technical-invalid counts: `0 / 0`
- Flags: `both_treatments_frequently_fail=true`, `candidate_repeated_wrong_family=false`, `candidate_worse_than_control=true`, `uncontrolled_variation_prevents_comparison=false`
- Fixed precedence: Rule 1 route reset fires before Rule 2 Candidate regression.
- Family result: `ROUTE_RESET_REQUIRED`

### brief_impact_recoil

- Candidate / Control primary passes: `0 / 0`
- Valid comparisons: `2`
- Candidate / Control clear advantages: `0 / 2`
- No-clear / invalid / inconclusive comparisons: `0 / 0 / 0`
- Candidate / Control action-family mismatches: `1 / 0`
- Candidate / Control technical-invalid counts: `0 / 0`
- Flags: `both_treatments_frequently_fail=true`, `candidate_repeated_wrong_family=false`, `candidate_worse_than_control=true`, `uncontrolled_variation_prevents_comparison=false`
- Fixed precedence: Rule 1 route reset fires before Rule 2 Candidate regression.
- Family result: `ROUTE_RESET_REQUIRED`

Independent family reconstruction, flags, rationales, and results equal the committed family records exactly.

## 9. Contradiction and mutation probes

All probes used in-memory copies only. Exact-byte verification rejected every subcase:

1. Candidate advantage changed to true: `PASS`, 4 subcases.
2. Candidate and Control sides swapped: `PASS`, 4 subcases.
3. Control advantage relabelled Candidate advantage: `PASS`, 4 subcases.
4. Family result changed to replicated positive signal: `PASS`, 2 subcases.
5. Family result changed to both-treatments-successful: `PASS`, 2 subcases.
6. Family result changed to Candidate regression while Rule 1 remained true: `PASS`, 2 subcases.
7. Candidate primary-pass count changed to 1 or 2: `PASS`, 4 subcases.
8. Control-advantage count changed from 2: `PASS`, 2 subcases.
9. `both_treatments_frequently_fail` changed to false: `PASS`, 2 subcases.
10. One-byte committed-record mutation: `PASS`, 1 subcase.

- Mutation probe result: `10 / 10 PASS`
- Committed derived record changed: `false`

## 10. Experimental interpretation boundary

- Component-level causal attribution permitted: `false`
- Statistical-significance claim permitted: `false`
- Cross-action-generalization claim permitted: `false`
- Treatment unit remains a compound family-level bundle.
- Confirmed only within this bounded evidence: every Candidate lost its matched pair, both Candidate and Control had zero primary passes, and both family routes require reset.
- No claim is made about an individual Prompt clause, universal action-generation failure, production readiness, Source adoption, or final/locked state.

## 11. Protected-state and no-live audit

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Submit/query/download/retry/resubmit/batch and login/session operations: `false`
- Media created or changed: `false`
- Sources changed: `false`
- Locked blind evidence, downloaded media, execution evidence, packages, Prompts, Batch05 design files, prior reports, and committed derivation artifacts changed: `false`
- ACTION_RULE, Source candidate, route-reset design, Prompt revision, and production package created: `false`
- The audit report is the only new repository path.
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## 12. Next phase

- Next phase: `CAL002_BATCH05_EXPERIMENT_RESULT_ACCEPTANCE_AND_ROUTE_RESET_DECISION`
