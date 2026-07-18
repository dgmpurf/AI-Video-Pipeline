# CAL-001 P3B-R2-T2 Existing F01 Query/Download Recovery Result

## 1. Phase summary

- executed: true
- status: `existing_F01_query_download_recovery_completed`
- starting_head: `a9aef9647dacd7335d65335ffbc53fc0144608c0`
- experiment_id: `CAL001-F01-P2-R1`
- existing_submit_id: `4e4588dd-a0e1-4539-8390-692cb9bf80f8`
- existing_logid: `20260718154849169254047008489C358`
- new_submit_count: 0
- query_count: 1
- download_count: 1
- final_gen_status: `success`
- media_validation_pass: true
- review_artifacts_created: true
- human_review_status: `unreviewed`
- visual_scores_assigned: false
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- final_master: false
- locked: false
T2 recovered only the existing F01 task. It performed one bounded status query, stopped further querying on terminal success, downloaded once after exact result-count validation, technically validated the single MP4, and created the authorized lightweight local review artifacts. Technical validity is not a visual-success decision.

## 2. Starting checkpoint

- required branch: `main`
- observed branch: `main`
- required HEAD: `a9aef9647dacd7335d65335ffbc53fc0144608c0`
- observed local HEAD before T2: `a9aef9647dacd7335d65335ffbc53fc0144608c0`
- observed `origin/main` before T2: `a9aef9647dacd7335d65335ffbc53fc0144608c0`
- local/origin aligned: true
- staged files before T2: none
- unrelated tracked modifications before T2: none
- `sources/` clean: true

Known unrelated untracked workspace noise remained outside the operation and staging scope: `.vs/`, `productions/chi_yan_tian_qiong/edits/`, `productions/chi_yan_tian_qiong/review_artifacts/`, `reports/context_recovery/`, and `reports/investor/`.

## 3. Authorization verification

Canonical authorization bytes were decoded directly from the human-supplied Base64 before any Dreamina command.

| Check | Required | Observed | Match |
| --- | --- | --- | --- |
| encoding | UTF-8 | valid UTF-8 | true |
| line endings | LF only | LF only | true |
| terminal newline | false | false | true |
| byte length | 3137 | 3137 | true |
| SHA256 | `06587a68d5418b2bd65cc7b2fdeace6b6992462b5016e8eeb9773606697fa10f` | same | true |

- authorization_sha256_match: true
- authorization_byte_length_match: true
- experiment ID match: true
- submit ID match: true
- log ID match: true
- new_submit_count_max: 0
- query_count_max: 3
- download_count_max: 1
- retry_count_max: 0
- resubmit_count_max: 0

Authorization record:

`experiments/CAL-001/reviews/CAL001_P3B_R2_T2_existing_F01_query_download_recovery_authorization_record.json`

The record was created and reverified before the first Dreamina command. At phase completion its `authorization_scope_active` field was closed to `false`.

## 4. Existing F01 evidence verification

Committed evidence was read independently from:

`experiments/CAL-001/execution_records/P3B_R2/CAL001-F01-P2-R1_technical_record.json`

- existing_submit_id_verified: true
- existing_logid_verified: true
- existing submit claim count across CAL-001 execution records before T2: 1
- submit ID: `4e4588dd-a0e1-4539-8390-692cb9bf80f8`
- log ID: `20260718154849169254047008489C358`
- prior last known state: `querying`
- prior submit cost: 70
- prior query count: 0
- prior download count: 0
- prior retry count: 0
- prior resubmit count: 0
- duplicate submit forbidden: true

No historical record was amended. No evidence suggested a second F01 submit.

## 5. Accepted immutable artifact verification

The five accepted digests were reconstructed from current bytes and the committed canonical aggregate formats: UTF-8, lexicographic ordering, LF line endings, and one final LF.

| Digest | Recomputed SHA256 | Match |
| --- | --- | --- |
| fixed_manifest_sha256 | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` | true |
| fixture_registry_sha256 | `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142` | true |
| prompt_inventory_sha256 | `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d` | true |
| package_inventory_sha256 | `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c` | true |
| full_experiment_inventory_sha256 | `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138` | true |

Additional checks:

- fixed manifest rows: 84
- canonical prompt inventory lines: 28
- canonical package inventory lines: 84
- canonical full inventory lines: 84
- prompt file hash mismatches: 0
- package file hash mismatches: 0
- registered fixture file hash mismatches: 0
- H1 acceptance record SHA256: `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7`
- human checklist SHA256: `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3`
- F01 package SHA256: `f8763f6cf62aa7893b6f0026544f5865eec5fcc6b2c288c809cdd7b5eab5e310`
- F01 Prompt SHA256: `e18bd22187c34bf38cd6cd8c793b0093968f94b263c12ff683987ea0d26f5368`
- F01 fixture set: none
- accepted_artifacts_unchanged: true

## 6. Wrapper repair verification

Before live recovery, `tests/test_dreamina_evidence_persistence.py` passed all 13 no-live cases. Query and download were then executed only through `execute_with_durable_evidence`.

Durable local evidence:

| Operation | Envelope | Parsed evidence | Exit | Sanitization |
| --- | --- | --- | ---: | --- |
| query 1 | `experiments/CAL-001/execution_records/P3B_R2_T2/evidence/query-001.subprocess_envelope.json` | `query-001.parsed_query_result.json` | 0 | no HTTP URL/auth/cookie/token present |
| download 1 | `experiments/CAL-001/execution_records/P3B_R2_T2/evidence/download-001.subprocess_envelope.json` | `download-001.parsed_download_result.json` | 0 | no HTTP URL/auth/cookie/token present |

Envelope SHA256 values:

- query envelope: `1919d66c63a6f7b5f0927d4e217bb96a7b44cfd603f94844d9d6d5a54b9a7a25`
- query parsed evidence: `de955923e035e480262cafdac6fa33a0ddd3ba87f784c050359ceff76acf966b`
- download envelope: `2f799a7205c7c6b22649455f90b665b2a3ca0b816d8750637747e5184537390f`
- download parsed evidence: `872db3634ae09c56cca3548d569bd24a61056fa841d87433772b08d9a62419e0`

Each subprocess envelope was atomically persisted before response parsing, dataset mutation, media validation, or report generation.

## 7. Runtime preflight

Executable used:

`C:/Users/msjpurf/bin/dreamina.exe`

| Command | Exit | Result |
| --- | ---: | --- |
| `dreamina version` | 0 | pass |
| `dreamina user_credit` | 0 | pass; live credit 6377 |
| `dreamina query_result -h` | 0 | pass |

Version summary:

- version: `2a20fff-dirty`
- commit: `2a20fff`
- build time: `2026-06-26T06:36:39Z`
- logger Access Denied: false
- login failure: false
- user_credit failure: false
- query without `--download_dir` is query-only: confirmed
- download requires `--download_dir`: confirmed

No generation command or generation-command help was run.

## 8. Query-only execution

Exactly one query-only command was executed through the repaired wrapper:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 4e4588dd-a0e1-4539-8390-692cb9bf80f8
```

The command did not contain `--download_dir`.

| Query | Exit | submit_id match | gen_status | queue_status | Images | Videos | Outputs | URL present | Fail reason |
| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 1 | 0 | true | `success` | `Finish` | 0 | 1 | 1 | true | none |

- query_history_summary: query 1 returned terminal success; queries 2 and 3 were not run
- polling loop used: false
- wait interval needed: none, because query 1 was terminal
- signed URL printed or recorded in the report: false

## 9. Terminal-state result

- final_gen_status: `success`
- final_queue_status: `Finish`
- returned submit ID matched committed ID: true
- returned log ID: not returned; committed log ID carried forward
- fail_reason: none
- provider credit_count: 70, the already-recorded submit cost
- terminal success caused immediate query stop: true

This is a provider/technical state only. It is not a visual-quality judgment.

## 10. Result-count gate

- expected images: 0
- observed images: 0
- expected videos: 1
- observed videos: 1
- expected outputs: 1
- observed outputs: 1
- exactly one downloadable video result: true
- result_count_match: true

The download gate opened only after all count checks passed.

## 11. Download execution

Before download:

- authorized directory resolved under repository root: true
- directory matched `CAL001-F01-P2-R1`: true
- pre-existing file count: 0
- overwrite risk: false

Exactly one download command was executed through the repaired wrapper:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id 4e4588dd-a0e1-4539-8390-692cb9bf80f8 --download_dir G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/experiments/CAL-001/runs/CAL001-F01-P2-R1
```

- subprocess exit code: 0
- returned submit ID match: true
- downloaded file count: 1
- download_count: 1
- download_status: `success`
- second download: false

## 12. Technical media validation

Downloaded media:

- absolute path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/experiments/CAL-001/runs/CAL001-F01-P2-R1/4e4588dd-a0e1-4539-8390-692cb9bf80f8_video_1.mp4`
- repository-relative path: `experiments/CAL-001/runs/CAL001-F01-P2-R1/4e4588dd-a0e1-4539-8390-692cb9bf80f8_video_1.mp4`
- filename: `4e4588dd-a0e1-4539-8390-692cb9bf80f8_video_1.mp4`
- size: 6,974,557 bytes
- SHA256: `df0199aaee019b1b39e64419248a6247a8fec742751f83ab3764b10ce6a915a8`
- container: MP4, `ftyp` major brand `isom`
- codec: H.264
- dimensions: 1280x720
- ratio: 16:9
- provider-reported fps: 24
- locally detected fps: approximately 24.1196
- provider-reported duration: 5.042 seconds
- local frame-derived duration: approximately 5.0167 seconds
- declared frame count: 121
- fully decoded frame count: 121
- decode backend: OpenCV `FFMPEG`
- decode readability: pass
- dimensions consistent across decoded frames: true
- zero-byte check: pass
- truncation check: pass
- media_validation_pass: true

Standalone `ffprobe` was not present on PATH; equivalent required fields were available through OpenCV's FFMPEG backend and a full sequential decode. No visual score or visual-success claim was made.

## 13. Review-artifact creation

Artifacts were created only after technical validation passed.

| Label | Requested | Actual | Frame | SHA256 |
| --- | ---: | ---: | ---: | --- |
| 0.00s | 0.000s | 0.000s | 0 | `04bc3887af156612047722566442667fca94a1763b05f47c59e6b7b5aff4b63c` |
| 1.00s | 1.000s | 0.995s | 24 | `7e4813f32fe2522b9b7e60dc02bcc5aec8a33623058206e0295152dd19286a97` |
| 2.00s | 2.000s | 1.990s | 48 | `6366c111868427bcf643f16ed85e59433e2c8d7823babef89306b681be9b69d5` |
| 3.00s | 3.000s | 2.985s | 72 | `6766558eddc475ce21482d997eb1f313e1e83a10fcebef03af0a6b6d554f8c43` |
| 4.00s | 4.000s | 3.980s | 96 | `cc82c4c427762366803d1282c00e67059773f38753cebd0656d8dc0e3d82bcf4` |
| final readable | clamped | 4.975s | 120 | `5214d62ad961e50a2fc799f2891c0a359f006e4e63f08306b15884f8b8e794de` |

Contact sheet:

- layout: 3x2
- dimensions: 1920x720
- path: `experiments/CAL-001/runs/CAL001-F01-P2-R1/review_artifacts/CAL001-F01-P2-R1_contact_sheet_3x2.png`
- SHA256: `6bc4c4f8ab0759e00513162c4ea44b705a1a3aea5c4bf26b5fe783627a83f59a`

Metadata:

`experiments/CAL-001/runs/CAL001-F01-P2-R1/review_artifacts/CAL001-F01-P2-R1_review_metadata.json`

- total review artifact paths recorded: 8
- cuts created: false
- scores assigned: false
- winner selected: false

## 14. Credit-state observation

- prior P3B-R2 pre-submit credit: 6447
- prior recorded submit cost: 70
- prior post-submit/final credit: 6377
- live_credit_pre_recovery: 6377
- live_credit_post_recovery: 6377
- unexplained_credit_delta: 0
- new_generation_credits_consumed: 0

The returned `credit_count=70` is the existing task's recorded generation cost. T2 does not claim a new generation charge.

## 15. Technical-record update

Created:

`experiments/CAL-001/execution_records/P3B_R2_T2/CAL001-F01-P2-R1_query_download_recovery_record.json`

The record contains the prior identifiers/cost, one-query history, exact result counts, one-download evidence, local media path/hash/metadata, eight review-artifact paths, credit observations, stop state, null visual scores, and closed authority flags.

- all 14 visual score fields null: true
- human_review_status: `unreviewed`
- final_master: false
- locked: false
- historical P3B-R2 technical records modified: false

## 16. Dataset update

Updated only the `CAL001-F01-P2-R1` row in:

`experiments/CAL-001/datasets/CAL001_experiment_results_template.csv`

Changed technical fields:

- `query_count`: 0 -> 1
- `final_gen_status`: `querying` -> `success`
- `result_count_match`: blank -> `true`
- `download_status`: `not_attempted` -> `success`
- `local_media_path`: recorded
- `local_media_sha256`: recorded

Preserved:

- existing submit evidence
- actual_credit_cost: 70
- prior `stop_condition_triggered=true`, because this unqualified dataset field preserves the historical P3B-R2 stop event; T2's phase-specific record separately records `stop_condition_triggered=false`
- all visual score columns blank/null
- reviewer_notes blank
- human_review_status: `not_started`, the schema-valid equivalent of unreviewed
- candidate_status: `unreviewed`

Git diff confirms one removed and one added CSV line, both for the same F01 row. The other 83 rows are byte-for-byte unchanged.

`experiments/CAL-001/datasets/CAL001_visual_review_template.jsonl` was not modified because it has no technical recovery fields. Its SHA256 remains `d36b08bc1dd5ef6792676eac99cc3b2be07ff2edc32b7ef7cd81940a33d02869`, all F01 scores remain null, and no outcome was assigned.

## 17. Stop-condition evaluation

- stop_condition_triggered: false
- stop_condition_reason: none
- query limit exceeded: false
- terminal failure: false
- result-count mismatch: false
- download anomaly: false
- media-validation failure: false
- account anomaly: false

The phase completed normally after terminal success, exact result counts, one download, and passing technical validation.

## 18. Remaining-task authority

- authorization_scope_active: false
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- retry_count: 0
- resubmit_count: 0
- task replacement: false
- F02-F07 submit authority: false
- CAL001B_authorized: false
- final_master: false
- locked: false

T2 grants no continuation authority beyond this completed recovery.

## 19. Media/Git boundary

The MP4, extracted PNG frames, contact sheet, and local review metadata remain untracked/ignored and uncommitted. The four durable wrapper evidence JSON files also remain local and unstaged because the authorized staging allowlist names only the consolidated recovery record, authorization record, dataset row, and report.

No media path will be staged. No ignored workspace noise will be staged.

## 20. Explicit non-actions

- new submit: false
- `text2video` call: false
- query another submit ID: false
- query 2 or 3: false
- fourth query: false
- second download: false
- retry: false
- resubmit: false
- replacement task: false
- F02-F07 execution: false
- Prompt rewrite: false
- manifest expansion: false
- batch expansion: false
- Source modification: false
- accepted-artifact modification: false
- historical-record modification: false
- cuts: false
- visual scoring: false
- family winner selection: false
- global template selection: false
- media staging/commit: false
- tag: false

## 21. Recommended next phase

`CAL-001-P3B-R2-T3_F01_VISUAL_REVIEW_AND_REMAINING_CANARY_DECISION`

T3 requires a separate human decision. It should visually review the downloaded video/contact sheet before deciding whether any remaining fixed canary may receive new authority.

## 22. Final verdict

- status: `existing_F01_query_download_recovery_completed`
- final_verdict: `CAL001_P3B_R2_F01_EXISTING_TASK_RECOVERED_READY_VISUAL_REVIEW_AND_REMAINING_CANARY_DECISION`
- new_submit_count: 0
- execution_authority_active: false
- remaining_fixed_tasks_authorized: false
- final_master: false
- locked: false
