# CAL-002 Batch05 Phase 1 Blind Review Record Lock Result

## 1. Starting checkpoint

- Branch: `main`
- Starting HEAD / origin/main: `d737316deab6da847dcae65fa229e2e58712b3ae`
- Parent-to-HEAD transition: `72` additions, `0` modifications, `0` deletions, `0` unexpected paths.

## 2. Attachment bindings

- Archive: `CAL002_BATCH05_BLIND_REVIEW_FINAL_INPUTS.zip`
- Archive bytes / SHA-256: `5541` / `444c0eb365f04a31f54b746312c60f6e8369eb65f3e95daf1dc238681588006b`
- Archive members: exactly `2` regular, non-executable files; no directories, links, traversal, duplicates, or hidden extras.
- JSON member bytes / SHA-256: `13492` / `923b054f575743f80f7d3b222fd52ee9d2f95c510dfda61459c06f0abf36a8b8`
- Markdown member bytes / SHA-256: `9494` / `db08aea351393e7308dbd468292eab6acda5d92fad3d40048463035c102f63aa`

## 3. Bound blind handoff evidence

- Blind handoff: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_artifacts/CAL002-BATCH05-BLIND-85BB78B1/BLIND_REVIEW_HANDOFF.md`
- Handoff bytes / SHA-256: `2829` / `acb14f33a6383ab166f502fd9dedd1bf58b7820ba422a58c46a0a59a9c607d20`
- Blind evidence manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_artifacts/CAL002-BATCH05-BLIND-85BB78B1/blind_review_evidence_manifest.json`
- Manifest bytes / SHA-256: `19967` / `5954d6c4bbbc4943f21ca72f0741f9a874150cfefadfaf34cb43f5d6edec1b3b`
- Verified committed reviewer-artifact bindings: `70 / 70`

## 4. Blind schema and validation

- Schema: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/batch05_visual_review_schema.json`
- Schema bytes / SHA-256: `18138` / `9e98bc7f50c218ef75f19f211c0d0eefd5b93f0d41a4780e280f412804b9ebc5`
- Schema ID: `CAL002_BATCH05_BLIND_VISUAL_REVIEW_SCHEMA_V0_3`
- Record version: `CAL002_BATCH05_BLIND_VISUAL_REVIEW_RECORD_V0_3`
- JSON Schema Draft 2020-12 validation: `PASS`
- Exact JSON/Markdown consistency: `PASS`
- JSON byte profile and strict parsing: `PASS`

## 5. Blind review results recorded

- Video review count: `8`
- Pair review count: `4`
- Primary endpoint PASS / FAIL: `0 / 8`
- `PUSH_PAIR_01`: `A_CLEARLY_BETTER`
- `PUSH_PAIR_02`: `B_CLEARLY_BETTER`
- `IMPACT_PAIR_01`: `B_CLEARLY_BETTER`
- `IMPACT_PAIR_02`: `A_CLEARLY_BETTER`
- All four reviewer rationales are nonempty.

## 6. Blindness and derivation boundary

- Reviewer-facing treatment leakage: `false`
- Treatment mapping accessed in this phase: `false`
- Post-unblinding performed: `false`
- Candidate advantage derived: `false`
- Family result derived: `false`
- Mapping-bearing files and the derivation tool were not read or executed.

## 7. Locked paths

- Final blind record: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_records/CAL002-BATCH05-BLIND-85BB78B1/blind_review_record_final.json`
- Final record bytes / SHA-256: `13492` / `923b054f575743f80f7d3b222fd52ee9d2f95c510dfda61459c06f0abf36a8b8`
- Final blind report: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_records/CAL002-BATCH05-BLIND-85BB78B1/blind_visual_review_report.md`
- Final report bytes / SHA-256: `9494` / `db08aea351393e7308dbd468292eab6acda5d92fad3d40048463035c102f63aa`
- Lock manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_records/CAL002-BATCH05-BLIND-85BB78B1/blind_review_lock_manifest.json`
- Lock manifest bytes / SHA-256: `2905` / `208a8081585adf8797e43354e0e828f4e3b3c92ab3ab9be285d88e27ee6f721d`
- Blind record finalized before unblinding: `true`
- Blind record locked: `true`
- Record must not change after commit: `true`

## 8. Non-actions and protected state

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Submit/query/download/retry/resubmit/batch called: `false`
- Media created or changed: `false`
- Sources changed: `false`
- Prompt, package, design, handoff, prior evidence, and prior report files changed: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- final_master: `false`
- locked: `false`

## 9. Decision

- Decision: `CAL002_BATCH05_BLIND_REVIEW_RECORD_LOCKED_READY_FOR_POST_UNBLINDING_DERIVATION`
- Created paths: `4`
- Unexpected paths: `0`
- Next phase: `CAL002_BATCH05_POST_UNBLINDING_DERIVATION_NO_LIVE`
