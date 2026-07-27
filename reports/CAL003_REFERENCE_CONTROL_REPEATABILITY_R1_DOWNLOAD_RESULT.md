# CAL-003 Reference Control Repeatability R1 Download Result

All six CAL-003 R1 media files were downloaded, technically validated, canonicalized without byte changes, fully decoded, and validated again.

No blind mapping was created.

No semantic review or repeatability conclusion has been performed.

## 1. Actual Decision and Next Phase

- Decision: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_SIX_TASK_DOWNLOAD_SUCCESS_TECHNICAL_VALIDATION_PASS`.
- Next phase: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_BLIND_MAPPING_COMMITMENT_AUTHORIZATION_HUMAN_DECISION`.

## 2. Starting Checkpoint

- Branch: `main`.
- HEAD/origin/main: `6e3ee71dbc608d6eb3d27e41601ccd68524a44ab`.
- Parent: `8b833947dc58d459a8c8e238219b768107b6f048`.
- Commit message: `query(cal003): record reference repeatability R1 task status`.
- Tracked/staged/Source changes: 0/0/0.
- Unrelated untracked baseline: 26 paths, set SHA-256 `619b91a4981d8000f769bba3d15739ec2b0496df1109a98d809735aaf8abef94`.

## 3. Authorization Profile and Lifecycle

- Goal: `CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_MAX_SIX_DOWNLOAD_ONLY_MEDIA_FIRST_TECHNICAL_VALIDATION_V0_1`.
- Execution: `CAL003-REFERENCE-CONTROL-REPEATABILITY-R1-MAX-SIX-DOWNLOAD-ONLY-MEDIA-FIRST-V0-1`.
- Approval bytes/SHA-256/Base64 chars: 6552 / `1f22117473fe06e33a0ed00fbe32b320868cbac4dc22135cfa1d9529c9639d4a` / 8736.
- Activated at first Dreamina version process attempt: true. Consumed: true. Reusable: false.
- Authorized maximums: 9 Dreamina processes and 6 download calls. Query-only, loop, retry, resubmit, batch, new submit, blind mapping, review and production authority were false.

## 4. Authorization Round-Trip

- Encoding: UTF-8; BOM=false; trailing CR/LF/space=false.
- Base64 decode count: 1.
- Decoded bytes equal original: true.
- Decoded SHA-256 equals original: true.
- Independent authorization verification: PASS.

## 5. Thirteen Committed-Input Bindings

| Name | Path | Bytes | SHA-256 | Git blob | Result |
|---|---|---:|---|---|---|
| query_authorization | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/authorization.json` | 17355 | `cdc6d56dda5b1f62ee14770eeca3f4f42b46f59dcba912d5168de859649c2b05` | `8ac58ce41a0c5051bcae4a2119ba2769de225f08` | PASS |
| query_preflight | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/preflight.json` | 10343 | `ef487da64e46842324632b2bccd740477eb7a691b48985eb06beca566e11c5b9` | `85697887e3c7d3e56584624d6088537f889cb045` | PASS |
| push_01_query_receipt | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/push_01.json` | 2061 | `893859eac2742eb4f974b469f5e711286bbc22c699cd99562cc87f45b86e6e8d` | `baa9b70054e9a7f2107253a81b560b13bd721e70` | PASS |
| impact_01_query_receipt | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/impact_01.json` | 2069 | `9b269a3cb9cc5e34a64a1b1c2fdb298fe206ccb79c392030ae5a154cd84547ab` | `bf1c5fc32e7f6c644552d15f4d44c67147f5e033` | PASS |
| impact_02_query_receipt | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/impact_02.json` | 2068 | `90b80608768937bc821bb2eb830142db8c10f53ea339d0cbef07e82b2fab64ab` | `cf0eeb06ca8791c8c8ad2321bb96627c5c6206a3` | PASS |
| push_02_query_receipt | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/push_02.json` | 2061 | `6ce456897b474f5beb820ded4e40bc006a32cfddb8e71d9326785475e016f320` | `b9042116b8f7627bfa135ea2830fe61c13cfb253` | PASS |
| push_03_query_receipt | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/push_03.json` | 2060 | `cd620eed46637c3ac37297dd76cea20e388981948b8a7e787bd0ed6acbadab17` | `5680f93a6f50ad22f84f4c19ca594bf503725a55` | PASS |
| impact_03_query_receipt | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/queries/impact_03.json` | 2069 | `9d817384ec36c03ea03d7e80211431a44c6d4dc951a7bc3d0235ffb3d59ebca1` | `6e05bf3e3a5abc75d6f4e2d0b1d4eaf4a51a2664` | PASS |
| query_execution | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/execution.json` | 7017 | `478ac0fff25d4b4a8e649e3c71f17b58c7c9e22248be5ac90ef67cf8fb366dc0` | `ec4343558608121c3eabafbdcbe85dedf5e080fc` | PASS |
| query_evidence_manifest | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_QUERY/evidence_manifest.json` | 9334 | `8aa0cccafb1da4aee7d3337481441df0a1b2062e1c241907480294e0325c457c` | `47a80e13ccd9c36614921d71386e5ff0e00298fb` | PASS |
| query_governance_report | `reports/CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_QUERY_RESULT.md` | 9658 | `4643052ffa17410cd547a83ace642acecd7171e5aad9e98db54acbe698f79e7b` | `cad619ebf51d315d47cf3ab668d14f4be18fd717` | PASS |
| blind_review_protocol | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DESIGN/blind_review_protocol.json` | 2017 | `0fa75644c2067f8a42c3e689c558fd27618a6297d8010d7b6e1f8c628886e614` | `1ca410f2fcb37b9d2be4e835bc188bfd068933ae` | PASS |
| review_contract | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DESIGN/review_contract.json` | 4609 | `e8855d71ddc39efc07f8db7317d770d76c0ffbda829cee55fde662e18b26c8f4` | `286e424b486331f862eea934ed0a53f070f3d35b` | PASS |

Committed-input coverage: 13/13; every worktree file equals its HEAD blob.

## 6. Six Task and Submit-ID Bindings

| Task | Family | Replicate | Ordinal pair | Position | Submit ID | Reference |
|---|---|---:|---:|---:|---|---|
| PUSH-01 | PUSH | 1 | 1 | 1 | `65aa46f5-0125-4d07-8c6e-3fd5112d29a7` | ACTION_REF_PUSH_02 |
| IMPACT-01 | IMPACT | 1 | 1 | 2 | `b10cf271-288e-4fdb-925c-b4bd45856979` | ACTION_REF_IMPACT_02 |
| IMPACT-02 | IMPACT | 2 | 2 | 3 | `3cfa385f-99c9-4e1f-871e-d52ff154ebae` | ACTION_REF_IMPACT_02 |
| PUSH-02 | PUSH | 2 | 2 | 4 | `2258abca-2de6-4394-903f-7de609a7e711` | ACTION_REF_PUSH_02 |
| PUSH-03 | PUSH | 3 | 3 | 5 | `3fbcdb18-24d2-4a43-9cd5-5c7d1de41011` | ACTION_REF_PUSH_02 |
| IMPACT-03 | IMPACT | 3 | 3 | 6 | `10193c64-b91e-454e-9118-6ab3a0cf1fb9` | ACTION_REF_IMPACT_02 |

Submit IDs unique=true; task metadata complete=PASS.

## 7. All-Six Download-Ready Prerequisite

All six committed query receipts were strict-parse PASS, terminal success/Finish, one-video results, and `download_ready=true`. Reference cross-contamination=false.

## 8. Fixed Download Order

1. dreamina version
2. dreamina user_credit
3. dreamina query_result -h
4. PUSH-01 download
5. IMPACT-01 download
6. IMPACT-02 download
7. PUSH-02 download
8. PUSH-03 download
9. IMPACT-03 download

Execution was sequential with no parallel calls.

## 9. Version Canary

- Result: PASS; version=2a20fff-dirty; commit=2a20fff; build_time=2026-06-26T06:36:39Z.
- Return/timeout: 0/false.
- stdout bytes/SHA: 96/`25bbb1bdc706cb4e6fd486316b89b98a0d29c07fa34c8c51d0f860da2f29d8f0`.
- stderr bytes/SHA: 0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## 10. User-Credit Canary

- Result: PASS; total_credit=2701.
- Logger failure=false; login/auth failure=false; private account fields persisted=false.
- stdout bytes/SHA: 103/`42b72dda3852727f5d8f8cd0384b9a8492d08aca33cc5b6e67057ca70178c53c`.
- stderr bytes/SHA: 0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## 11. query_result Help and Download Contract

- Help result: PASS; command contract=PASS; repeated=false.
- Supported: submit_id, optional download_dir, one task per invocation; no output_dir/output_name/retry/query-loop required.
- stdout bytes/SHA: 388/`74f728cc4d3ae36fb3dcf773e85ed003637c28d048d1cad77a29b59b9bd4b171`; stderr bytes/SHA: 0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Six argv bindings matched their approved byte lengths and SHA-256 values.

## 12. Temporary-Root Isolation

- Root: `G:/AICODING/AI_VIDEO/_temp/CAL003_R1_DLOAD_V0_1`; absent before activation=true; outside repository=true; drive G:.
- Six task-specific initially empty directories were used exactly once.
- Repository and temporary root were on the same drive; cross-task contamination=false.
- ffprobe and ffmpeg preflight/version results: PASS/PASS.

## 13. PUSH-01 Download and Technical Result

- Download: called=true, call_count=1, return_code=0, timeout=false, exception=null.
- Argv: bytes=180, SHA-256=`4cc01207978e351ea58054142a07ece4e36d71e4ebab44e50bfdf3d0b79a4d99`, shell=false.
- Process evidence: stdout=2937/`2716d5865d497f9b1e582c6d34c56efbfed3f07fb55fe67d39f51057459ab05b`; stderr=0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; raw output persisted=false.
- Parse and identity: PASS via stdout_complete_json; submit_id_matched=true; failure_contradiction=false.
- Materialization: regular_files=1; mp4_files=1; bytes=2299169; SHA-256=`888bb1a27951cbe211b8a0506a5decb20c4f9aa2e9ba255a7832c1735836380c`.
- Temporary technical result: PASS; h264/yuv420p; 1280x720; duration=5.085011s; rotation=0; frames=121; streams video/audio/other=1/1/0; full_decode=PASS; metadata=PASS.
- Media-first result: PASS; download acceptance=PASS.
- Canonical result: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_01.mp4`; bytes=2299169; SHA-256=`888bb1a27951cbe211b8a0506a5decb20c4f9aa2e9ba255a7832c1735836380c`; byte_equal=true; SHA_equal=true; post_move=PASS.

## 14. IMPACT-01 Download and Technical Result

- Download: called=true, call_count=1, return_code=0, timeout=false, exception=null.
- Argv: bytes=182, SHA-256=`0b08d9f597bed62dd7ce405e8a698214d7203dca5a46f6bd6aa6b0200e0871df`, shell=false.
- Process evidence: stdout=2939/`2642d3a7d72e5a89967cb6817a5c036453d57441565dc474046b37343d2c6862`; stderr=0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; raw output persisted=false.
- Parse and identity: PASS via stdout_complete_json; submit_id_matched=true; failure_contradiction=false.
- Materialization: regular_files=1; mp4_files=1; bytes=2365925; SHA-256=`86505a14f9afbb48db44b429e5b60b36094cb896acf34a23f19a4299785d591f`.
- Temporary technical result: PASS; h264/yuv420p; 1280x720; duration=5.085011s; rotation=0; frames=121; streams video/audio/other=1/1/0; full_decode=PASS; metadata=PASS.
- Media-first result: PASS; download acceptance=PASS.
- Canonical result: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_01.mp4`; bytes=2365925; SHA-256=`86505a14f9afbb48db44b429e5b60b36094cb896acf34a23f19a4299785d591f`; byte_equal=true; SHA_equal=true; post_move=PASS.

## 15. IMPACT-02 Download and Technical Result

- Download: called=true, call_count=1, return_code=0, timeout=false, exception=null.
- Argv: bytes=182, SHA-256=`379ad6a0a0082b0244302753baea94a301f51f907462f14707916dac70829385`, shell=false.
- Process evidence: stdout=2939/`b126b76eb0e2708575d98f505a9da5ea4f307d276fb4b611c13f1e3bce0b8877`; stderr=0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; raw output persisted=false.
- Parse and identity: PASS via stdout_complete_json; submit_id_matched=true; failure_contradiction=false.
- Materialization: regular_files=1; mp4_files=1; bytes=3147949; SHA-256=`5bff5f8fe963d2db826b2195194a648ebe8823fb53078ee82d43f2adf9ff5ca9`.
- Temporary technical result: PASS; h264/yuv420p; 1280x720; duration=5.085011s; rotation=0; frames=121; streams video/audio/other=1/1/0; full_decode=PASS; metadata=PASS.
- Media-first result: PASS; download acceptance=PASS.
- Canonical result: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_02.mp4`; bytes=3147949; SHA-256=`5bff5f8fe963d2db826b2195194a648ebe8823fb53078ee82d43f2adf9ff5ca9`; byte_equal=true; SHA_equal=true; post_move=PASS.

## 16. PUSH-02 Download and Technical Result

- Download: called=true, call_count=1, return_code=0, timeout=false, exception=null.
- Argv: bytes=180, SHA-256=`3cb5b4aaadcb87d0d54a2dedceecfabfbbbb2eb089267933719b0d25ad409cd2`, shell=false.
- Process evidence: stdout=2937/`a8922ee054967005e16e68c7a46786367aa2cd6d3162e8a3e26ab04a3d387e14`; stderr=0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; raw output persisted=false.
- Parse and identity: PASS via stdout_complete_json; submit_id_matched=true; failure_contradiction=false.
- Materialization: regular_files=1; mp4_files=1; bytes=2852365; SHA-256=`9db1d8dff40c5b69641be0e49f1ff107231bce88f618b218089a38214e85af21`.
- Temporary technical result: PASS; h264/yuv420p; 1280x720; duration=5.085011s; rotation=0; frames=121; streams video/audio/other=1/1/0; full_decode=PASS; metadata=PASS.
- Media-first result: PASS; download acceptance=PASS.
- Canonical result: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_02.mp4`; bytes=2852365; SHA-256=`9db1d8dff40c5b69641be0e49f1ff107231bce88f618b218089a38214e85af21`; byte_equal=true; SHA_equal=true; post_move=PASS.

## 17. PUSH-03 Download and Technical Result

- Download: called=true, call_count=1, return_code=0, timeout=false, exception=null.
- Argv: bytes=180, SHA-256=`ae4a9e8d5381574064863bdfc3845458d5e89fcfb638576d6ca5f4b603c1c68d`, shell=false.
- Process evidence: stdout=2937/`f208fafb237f55eb347ab1a09321a78cee759237a2fa1bc21f963679194c5ee3`; stderr=0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; raw output persisted=false.
- Parse and identity: PASS via stdout_complete_json; submit_id_matched=true; failure_contradiction=false.
- Materialization: regular_files=1; mp4_files=1; bytes=2417274; SHA-256=`196945461a5a7c748e75911e962dde8523f99762bc64e0ffa2bb506d4f52f921`.
- Temporary technical result: PASS; h264/yuv420p; 1280x720; duration=5.085011s; rotation=0; frames=121; streams video/audio/other=1/1/0; full_decode=PASS; metadata=PASS.
- Media-first result: PASS; download acceptance=PASS.
- Canonical result: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_03.mp4`; bytes=2417274; SHA-256=`196945461a5a7c748e75911e962dde8523f99762bc64e0ffa2bb506d4f52f921`; byte_equal=true; SHA_equal=true; post_move=PASS.

## 18. IMPACT-03 Download and Technical Result

- Download: called=true, call_count=1, return_code=0, timeout=false, exception=null.
- Argv: bytes=182, SHA-256=`07b91a9531d669c86d0a6c9d506c5a51bcedb2300a9aac842871b45435e6b1f6`, shell=false.
- Process evidence: stdout=2939/`27260e5669eec098aeb4b1f371f1378de6772b3fdd25139f79bdf88785c97098`; stderr=0/`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; raw output persisted=false.
- Parse and identity: PASS via stdout_complete_json; submit_id_matched=true; failure_contradiction=false.
- Materialization: regular_files=1; mp4_files=1; bytes=2419698; SHA-256=`36bfa241c6262daccce1c87df53e8e589ef63a46fdfeef385a560ee55ea74cd9`.
- Temporary technical result: PASS; h264/yuv420p; 1280x720; duration=5.085011s; rotation=0; frames=121; streams video/audio/other=1/1/0; full_decode=PASS; metadata=PASS.
- Media-first result: PASS; download acceptance=PASS.
- Canonical result: `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_03.mp4`; bytes=2419698; SHA-256=`36bfa241c6262daccce1c87df53e8e589ef63a46fdfeef385a560ee55ea74cd9`; byte_equal=true; SHA_equal=true; post_move=PASS.

## 19. Media-First Handling

For each called task, exact media materialization and local MP4 validation were authoritative. Structured process parsing was secondary. Every task produced exactly one regular nonempty MP4 and passed local validation before the next task began.

## 20. All-Six Temporary-Media Gate

- Gate result: PASS; called downloads=6; temporary MP4s=6; six technical results=PASS.
- Submit bindings correct=true; positive bytes=true; hashes present=true; sensitive-data scan=PASS; canonical paths absent before move=true.
- A generic local boolean aggregator initially treated contract-required false fields as failures. Explicit polarity-aware evaluation corrected this local aggregation issue to PASS. Provider calls added=0 and downloads repeated=0.

## 21. Canonicalization

After the all-six Gate passed, six same-drive byte-preserving moves were performed in fixed order. Canonical media count=6; source temporary files absent=6/6; destination regular files=6/6; symlink/reparse=false for all.

## 22. Six Canonical Paths, Bytes and SHA-256 Values

| Task | Canonical path | Bytes | SHA-256 |
|---|---|---:|---|
| PUSH-01 | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_01.mp4` | 2299169 | `888bb1a27951cbe211b8a0506a5decb20c4f9aa2e9ba255a7832c1735836380c` |
| IMPACT-01 | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_01.mp4` | 2365925 | `86505a14f9afbb48db44b429e5b60b36094cb896acf34a23f19a4299785d591f` |
| IMPACT-02 | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_02.mp4` | 3147949 | `5bff5f8fe963d2db826b2195194a648ebe8823fb53078ee82d43f2adf9ff5ca9` |
| PUSH-02 | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_02.mp4` | 2852365 | `9db1d8dff40c5b69641be0e49f1ff107231bce88f618b218089a38214e85af21` |
| PUSH-03 | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_03.mp4` | 2417274 | `196945461a5a7c748e75911e962dde8523f99762bc64e0ffa2bb506d4f52f921` |
| IMPACT-03 | `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_03.mp4` | 2419698 | `36bfa241c6262daccce1c87df53e8e589ef63a46fdfeef385a560ee55ea74cd9` |

## 23. Post-Move Validation

All six canonical media files passed ffprobe, stream constraints, 4-6 second duration, zero rotation, positive frame evidence, full ffmpeg decode, and metadata safety. Pre/post byte equality=6/6; pre/post SHA equality=6/6; post-move technical PASS=6/6.

## 24. Identical-Hash Pair Analysis

- Pair comparisons: 15.
- Identical pair count: 0.
- Identical task pairs: none.
- Human-decision flag: false. Hash uniqueness was observed but was not a technical acceptance requirement.

## 25. Temporary Cleanup

- Cleanup result: PASS; exact target guard=PASS.
- Temporary root exists=false; regular files/directories/symlinks/reparse points remaining=0/0/0/0.
- No path outside the exact temporary root was removed.

## 26. Exact Dreamina and Operation Counts

- Dreamina processes: 9/9 maximum.
- Version/user_credit/query_result-help/download: 1/1/1/6.
- Query-only/query-loop/retry/resubmit/batch/new-submit: 0/0/0/0/0/0.
- No login, checklogin, session mutation, list_task, reference upload or additional Provider operation occurred.

## 27. Exact Success Write Set

Exactly these 23 new paths comprise the success write set:

1. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/authorization.json`
2. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/preflight.json`
3. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/downloads/push_01.json`
4. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/downloads/impact_01.json`
5. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/downloads/impact_02.json`
6. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/downloads/push_02.json`
7. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/downloads/push_03.json`
8. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/downloads/impact_03.json`
9. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/technical/push_01.json`
10. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/technical/impact_01.json`
11. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/technical/impact_02.json`
12. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/technical/push_02.json`
13. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/technical/push_03.json`
14. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/technical/impact_03.json`
15. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_01.mp4`
16. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_01.mp4`
17. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_02.mp4`
18. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_02.mp4`
19. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/PUSH_03.mp4`
20. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/media/IMPACT_03.mp4`
21. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/execution.json`
22. `experiments/CAL-003/REFERENCE_CONTROL_REPEATABILITY_V1/R1_DOWNLOAD/evidence_manifest.json`
23. `reports/CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_DOWNLOAD_RESULT.md`

Existing paths modified/deleted/renamed: 0/0/0.

## 28. Evidence Coverage

The manifest is created last and binds 22 non-self outputs plus 13 committed inputs: output coverage 22/22, committed-input coverage 13/13, total unique bound paths 35, self excluded=true.

## 29. Sensitive-Data Result

Sensitive-data scan=PASS. Raw stdout/stderr, raw Provider response, signed URL values, tokens, cookies, credentials, private account payloads, blind mapping, blind salt and blind commitment were not persisted. Only sanitized process metadata and approved technical facts were recorded.

## 30. Protected-State Result

All CAL-002 artifacts, CAL-003 R1_DESIGN/R1_SUBMIT/R1_QUERY artifacts, existing Prompts, packages, references, prior media, prior reports, production artifacts and Source files remained unchanged. Only the exact R1_DOWNLOAD success output set was created.

## 31. Blind-Mapping Boundary

Blind mapping materialized=false; blind aliases assigned=false; blind salt generated=false; blind commitment created=false. No family-to-alias mapping was created or inferred.

## 32. Review and Repeatability Boundary

Complete-MP4 review performed=false; Provider visual content reviewed=false; semantic review performed=false; repeatability conclusion known=false. Media is locally available only for the separately authorized future blind workflow.

## 33. C02, C03 and R02 Boundaries

C02 reopened=false; C03 authorized=false; original R02 blocked=true; R02 authorized=false. CAL-003 R1 download phase complete=true; experiment complete=false.

## 34. Production, Completion, Final and Lock Boundaries

production_reentry_authorized=false; production_approved=false; fixed_task_completion=false; final_master=false; locked=false.

## 35. Commit and Push Outcome

At deterministic report serialization, stage/commit/push are pending. The authorized terminal Git step may stage exactly the 23 success paths, create one commit with message `download(cal003): retrieve reference repeatability R1`, and push `main` once to `origin/main`. Actual Git outcome is returned in the terminal receipt; no post-commit report modification is permitted.

## 36. Exact Next Phase

`CAL003_REFERENCE_CONTROL_REPEATABILITY_R1_BLIND_MAPPING_COMMITMENT_AUTHORIZATION_HUMAN_DECISION`

No authority for that phase is created here.
