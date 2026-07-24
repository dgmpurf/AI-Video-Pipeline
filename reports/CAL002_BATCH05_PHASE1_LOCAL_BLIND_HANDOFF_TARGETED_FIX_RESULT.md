# CAL-002 Batch05 Phase 1 Local Blind Handoff Targeted Fix Result

## 1. Starting checkpoint

- Branch: `main`
- Starting HEAD / origin/main: `9b7a39128ca5d25a6131297c24fcea6206002a97`
- Expected parent: `234abb2f34a4ae30bcd7694886cdf336c65849ea`
- Prior transition: `42` added paths, confined to the download-record root and prior download report.

## 2. Prior evidence bindings

- Prior report: `reports/CAL002_BATCH05_PHASE1_DOWNLOAD_AND_BLIND_HANDOFF_RESULT.md`
- Prior report bytes / SHA-256: `10923` / `1d074e773ff0fd87be22635a2a79472b8f355e08a8835bebf15c257a79f5b5a2`
- Prior evidence manifest: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/download_evidence_manifest.json`
- Prior manifest bytes / SHA-256: `23246` / `97ae33575c135069910fd95b8c9c8ad3d3f2626dd3ef646a5c7af16ed1f4912e`
- Forty-one prior bindings equal both the current worktree and `HEAD`: `true`

## 3. Root cause and correction

The prior build attempted exclusive blind-root creation before its immediate `review_artifacts/` parent existed, producing `ENOENT` before any blind artifact was created. This targeted fix created the parent first, verified it was empty, then created `CAL002-BATCH05-BLIND-85BB78B1/` exclusively before creating its required subdirectories.

- Immediate parent created: `true`
- Blind root created exclusively: `true`
- Build attempt count: `1`

## 4. No-live boundary

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Download/query/submit/retry/resubmit/batch called: `false`
- Media redownloaded: `false`

## 5. Immutable source MP4 bindings

| Source task | Blind alias | Source path | Bytes | SHA-256 |
|---|---|---|---:|---|
| `CAL002-B05-PUSH-CONTROL-R01` | `PUSH_PAIR_01_A` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-PUSH-CONTROL-R01/provider_download/f3663d7f-33dc-4937-b6e1-20c6be10a0d8_video_1.mp4` | 2976752 | `2fec33ed778c0176f1959a2809a6dd051b1a34bd4016c2c52b4562c80dbe00ae` |
| `CAL002-B05-PUSH-CANDIDATE-R01` | `PUSH_PAIR_01_B` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-PUSH-CANDIDATE-R01/provider_download/866311e6-be9b-4850-a798-9e74d4a3bce9_video_1.mp4` | 2957019 | `df1f3d5435f8423079cdefa6369016d716c9fe0b7924d7b92d130b54d8fd359a` |
| `CAL002-B05-PUSH-CANDIDATE-R02` | `PUSH_PAIR_02_A` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-PUSH-CANDIDATE-R02/provider_download/b506bd61-3b16-4f5c-9209-4dfc49356284_video_1.mp4` | 3721924 | `a4c3e2da2ff3b0d474d4d0191a36c4c553d9b9fcf7bc045fd40f9883bfa98832` |
| `CAL002-B05-PUSH-CONTROL-R02` | `PUSH_PAIR_02_B` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-PUSH-CONTROL-R02/provider_download/03a03b27-1e3d-48e7-9122-7fdaea7df0d1_video_1.mp4` | 3163140 | `27c67faa01048a5e9a75f7bcc65c3c0203cd13b3cf775040fb6c3386fffeef0e` |
| `CAL002-B05-IMPACT-CANDIDATE-R01` | `IMPACT_PAIR_01_A` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-IMPACT-CANDIDATE-R01/provider_download/7453c063-e5d8-49aa-83f7-d4f8e8136697_video_1.mp4` | 2972815 | `494415f73fd45ecb1965ff038ba13879d434c7a34a3cbb87386c19d9d3c13b21` |
| `CAL002-B05-IMPACT-CONTROL-R01` | `IMPACT_PAIR_01_B` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-IMPACT-CONTROL-R01/provider_download/01193507-cb12-4116-aec4-9084063a61d9_video_1.mp4` | 3088754 | `de54a174c080edd5aedbf2a05113b1617534158d74fe1e17789bb8e834164e97` |
| `CAL002-B05-IMPACT-CONTROL-R02` | `IMPACT_PAIR_02_A` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-IMPACT-CONTROL-R02/provider_download/924b3f58-d0bb-43b4-80e7-a45be940ce06_video_1.mp4` | 2239605 | `60ab4bb1bd80ae02130ed897320e1124f992cfd130a8aa7ddfca9119319605ae` |
| `CAL002-B05-IMPACT-CANDIDATE-R02` | `IMPACT_PAIR_02_B` | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/download_records/CAL002-BATCH05-DOWNLOAD-85BB78B1/downloads/CAL002-B05-IMPACT-CANDIDATE-R02/provider_download/dc64226b-d9dd-4d79-bba4-6bd16f5fa465_video_1.mp4` | 3162693 | `58834668282832e21b48be4767371ecb047076366fef17b02ebc48cd77dc3496` |

- Source MP4 count: `8`
- Unique source SHA-256 count: `8`
- Existing technical records passed: `8 / 8`
- Source files equal committed `HEAD` blobs: `8 / 8`

## 6. Metadata-leakage audit

Fresh local `ffprobe` inspection found no reviewer-visible processing-group label, task identity, bound submit ID, signed URL, credential-like value, or full Prompt in any source MP4. Generic container and generation-origin metadata did not expose group identity.

- Reviewer-visible source metadata leakage: `false`

## 7. Alias-copy bindings

| Blind alias | Destination | Bytes | SHA-256 | Duration | Resolution |
|---|---|---:|---|---:|---|
| `PUSH_PAIR_01_A` | `media/PUSH_PAIR_01_A.mp4` | 2976752 | `2fec33ed778c0176f1959a2809a6dd051b1a34bd4016c2c52b4562c80dbe00ae` | 5.061950 | `1280x720` |
| `PUSH_PAIR_01_B` | `media/PUSH_PAIR_01_B.mp4` | 2957019 | `df1f3d5435f8423079cdefa6369016d716c9fe0b7924d7b92d130b54d8fd359a` | 5.061950 | `1280x720` |
| `PUSH_PAIR_02_A` | `media/PUSH_PAIR_02_A.mp4` | 3721924 | `a4c3e2da2ff3b0d474d4d0191a36c4c553d9b9fcf7bc045fd40f9883bfa98832` | 5.061950 | `1280x720` |
| `PUSH_PAIR_02_B` | `media/PUSH_PAIR_02_B.mp4` | 3163140 | `27c67faa01048a5e9a75f7bcc65c3c0203cd13b3cf775040fb6c3386fffeef0e` | 5.061950 | `1280x720` |
| `IMPACT_PAIR_01_A` | `media/IMPACT_PAIR_01_A.mp4` | 2972815 | `494415f73fd45ecb1965ff038ba13879d434c7a34a3cbb87386c19d9d3c13b21` | 5.061950 | `1280x720` |
| `IMPACT_PAIR_01_B` | `media/IMPACT_PAIR_01_B.mp4` | 3088754 | `de54a174c080edd5aedbf2a05113b1617534158d74fe1e17789bb8e834164e97` | 5.061950 | `1280x720` |
| `IMPACT_PAIR_02_A` | `media/IMPACT_PAIR_02_A.mp4` | 2239605 | `60ab4bb1bd80ae02130ed897320e1124f992cfd130a8aa7ddfca9119319605ae` | 5.085011 | `1280x720` |
| `IMPACT_PAIR_02_B` | `media/IMPACT_PAIR_02_B.mp4` | 3162693 | `58834668282832e21b48be4767371ecb047076366fef17b02ebc48cd77dc3496` | 5.085011 | `1280x720` |

- Alias MP4 count: `8`
- Source/copy byte-and-hash identity: `8 / 8`
- Transcoding performed: `false`

## 8. Derived reviewer artifacts

- Keyframes: `48`; Pillow decode and `1280x720` dimensions: `48 / 48`
- Keyframe timestamps per alias: `0.10s`, `1.00s`, `2.00s`, `3.00s`, `4.00s`, `4.90s`
- Contact sheets: `8`; Pillow decode and `1920x720` dimensions: `8 / 8`
- Comparison sheets: `4`; Pillow decode and `1920x360` dimensions: `4 / 4`
- Blank review record: `1`; strict deterministic JSON: `PASS`
- Blind review handoff: `1`

## 9. Blind-root evidence manifest

- Path: `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_EXECUTION/review_artifacts/CAL002-BATCH05-BLIND-85BB78B1/blind_review_evidence_manifest.json`
- Artifact bindings: `70`
- Included/unique paths: `70 / 70`
- Recursive self-exclusion: `true`
- Manifest bytes / SHA-256: `19967` / `5954d6c4bbbc4943f21ca72f0741f9a874150cfefadfaf34cb43f5d6edec1b3b`

## 10. Reviewer-facing leakage and governance

- Reviewer-facing leakage count: `0`
- Visual success claimed: `false`
- Treatment winner selected: `false`
- Production approved: `false`
- Fixed-task completion: `false`
- final_master: `false`
- locked: `false`
- Sources changed: `false`
- Existing download, query, submit, package, Prompt, design, Source, and prior-report files changed: `false`

## 11. Final decision

- Decision: `CAL002_BATCH05_LOCAL_BLIND_HANDOFF_FIX_COMPLETE_READY_FOR_BLIND_VISUAL_REVIEW`
- Created blind-root files: `71`
- Created Git paths including this report: `72`
- Next phase: `CAL002_BATCH05_PHASE1_BLIND_VISUAL_REVIEW`
