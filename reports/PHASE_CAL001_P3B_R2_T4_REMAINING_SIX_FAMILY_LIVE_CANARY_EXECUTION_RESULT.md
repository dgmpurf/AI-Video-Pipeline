# CAL-001 P3B R2 T4 Remaining Six-Family Live Canary Execution Result

## 1. Phase summary

- phase_id: `CAL-001-P3B-R2-T4`
- status: `remaining_six_family_live_canary_completed`
- executed task scope: exactly `CAL001-F02-P2-R1` through `CAL001-F07-P2-R1` in the authorized order
- T4 completed canaries: 6
- total completed seven-family canaries including carried-forward F01: 7
- visual review performed in T4: false
- final_master: false
- locked: false

## 2. Starting checkpoint

- branch: `main`
- starting HEAD: `8df9da5ec084e5066d03344bdc3b1ba711d0623b`
- starting `origin/main`: `8df9da5ec084e5066d03344bdc3b1ba711d0623b`
- `sources/` clean: true
- tracked worktree clean before live execution: true
- staged files before live execution: none
- known untracked workspace noise was preserved and excluded from staging.

## 3. Authorization verification

The canonical authorization was decoded and verified before the first Dreamina command. It was not normalized, trimmed, reflowed, or reconstructed before hashing.

| Check | Result |
|---|---:|
| Base64 character length | 5640 |
| Base64 ASCII SHA256 | `c9e8bd289585bbf7238cde8d8fe27e3ce1a34704876b5e0684590384051f5cb7` |
| Decoded UTF-8 byte length | 4229 |
| Decoded authorization SHA256 | `ed774a087a5e09a6973d95b7309ecb2ad7cb699aac8c7cca73d6775d2c4ffd55` |
| Valid UTF-8 | true |
| LF only | true |
| Terminal newline | false |
| Exact prefix and task order | true |
| Counter, credit, stop, Source, score, final, and lock limits present | true |

Authorization record: `experiments/CAL-001/reviews/CAL001_P3B_R2_T4_remaining_six_family_live_canary_authorization_record.json`

Final authorization-record SHA256: `7b8d681876e85e535c447bbda3fc6a3b2b718a9ee783d82d2697225f5976692a`

The temporary scope is now closed with `authorization_scope_active=false`.

## 4. T3A and F01 carry-forward verification

- T3A human review record SHA256: `cbd7bbbd6446ff53d6615cde4becc86089ed63fa48e01bd9369d89252b8dc0bd`
- T3A result report SHA256: `eae13c218e5b4d267b679a7df1a9ed8b706afcb3c7fa9536fee4581276192321`
- F01 carried-forward completed: true
- F01 carried-forward submit count: 1
- F01 carried-forward cost: 70 credits
- F01 carried-forward validity class: `B_VALID_FAILURE_USABLE_FOR_PROMPT_ARCHITECTURE_COMPARISON`
- F01 was not submitted, queried, downloaded, rescored, or otherwise re-executed in T4.

## 5. Accepted immutable artifact verification

All accepted inputs were recomputed before live execution and rechecked at each pre-submit gate.

| Artifact | SHA256 | Match |
|---|---|---:|
| Fixed 84-task manifest | `b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d` | true |
| Fixture registry | `cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142` | true |
| Prompt inventory | `27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d` | true |
| Package inventory | `b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c` | true |
| Full experiment inventory | `448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138` | true |
| H1 acceptance record | `39a8c7e8a88335b79360326e5f6d634fca83399193fcea101950d75936993af7` | true |
| Human checklist | `4af9f37db6861740876d4a28bdd6a42a73c5e3664594093470764d9913658dc3` | true |

No accepted package, Prompt, fixture, manifest, Source, config, or runtime file was modified.

## 6. Runtime and wrapper preflight

- Dreamina executable: `C:/Users/msjpurf/bin/dreamina.exe`
- repaired wrapper: `app/ai_video_pipeline/execution/dreamina_evidence.py`
- wrapper no-live tests: 13 passed
- every Dreamina invocation used the repaired durable evidence wrapper
- per-task `version`, `user_credit`, and target-command help checks: passed
- target command families checked: `image2video`, `frames2video`, `multimodal2video`
- logger Access Denied: false
- login/auth/account anomaly: false
- Web-confirmation or safety prerequisite: false
- command-contract mismatch: false
- package/Prompt/fixture binding mismatch: false

Raw sanitized envelopes remain local under `experiments/CAL-001/execution_records/P3B_R2_T4/evidence/` and are intentionally unstaged.

## 7. Exact six-task order

1. `CAL001-F02-P2-R1`
2. `CAL001-F03-P2-R1`
3. `CAL001-F04-P2-R1`
4. `CAL001-F05-P2-R1`
5. `CAL001-F06-P2-R1`
6. `CAL001-F07-P2-R1`

No task was reordered, skipped, replaced, or executed concurrently.

## 8. Counter and credit ledger

| Experiment | Submit attempts | Created | Queries | Downloads | Pre-credit | Post-credit | Final credit | Cost |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F02 | 1 | 1 | 2 | 1 | 6377 | 6307 | 6307 | 70 |
| F03 | 1 | 1 | 2 | 1 | 6307 | 6237 | 6237 | 70 |
| F04 | 1 | 1 | 2 | 1 | 6237 | 6167 | 6167 | 70 |
| F05 | 1 | 1 | 1 | 1 | 6167 | 6097 | 6097 | 70 |
| F06 | 1 | 1 | 2 | 1 | 6097 | 6027 | 6027 | 70 |
| F07 | 1 | 1 | 2 | 1 | 6027 | 5957 | 5957 | 70 |
| T4 total | 6 | 6 | 11 | 6 | 6377 | 5957 | 5957 | 420 |

- retry_count: 0
- resubmit_count: 0
- remaining-six budget limit: 420
- observed T4 delta: 420
- cumulative seven-family cost including F01: 490

## 9. Per-task pre-submit gates

Every task passed all of the following immediately before its one submit:

- branch and starting HEAD unchanged;
- `sources/` clean;
- no tracked or staged drift;
- accepted immutable hashes matched;
- all earlier T4 tasks were fully complete;
- no prior submit or run directory existed for the current experiment;
- current package, Prompt file, provider-prompt payload, fixture order, and fixture hashes matched;
- target-command help contained the required flags;
- live credit met the task-specific threshold.

Thresholds were F02 6370, F03 6300, F04 6230, F05 6160, F06 6090, and F07 6020. Each gate passed.

## 10. Submit evidence

| Experiment | submit_id | logid | Submit state | credit_count |
|---|---|---|---|---:|
| F02 | `bc30902f-2636-4ac9-867b-549eea6319d0` | `202607181925541692540470083191497` | querying | 70 |
| F03 | `72e47447-bcc0-4e21-bd6d-02fcb8fbf22d` | `20260718193551169254047008790B434` | querying | 70 |
| F04 | `2ea258b6-33b3-4b48-a01e-01302891de35` | `202607181945431692540470081122960` | querying | 70 |
| F05 | `c1ce88e5-3849-4279-973a-dc7eaa09aa0d` | `202607181957341692540470085868EB8` | querying | 70 |
| F06 | `9331ef8d-6f1f-4531-913a-dc844293d509` | `2026071820030116925404700828337C4` | querying | 70 |
| F07 | `5a3da27e-3a70-4410-9824-1116678464fc` | `20260718201304169254047008190DA7C` | querying | 70 |

Each submit had exit code 0, a nonempty unique submit ID and log ID, numeric cost at or below 70, and a durable sanitized subprocess envelope plus parsed task-creation evidence.

## 11. Query evidence

- Query schedule was bounded and non-polling: approximately 120 seconds before Query 1, then approximately 240 seconds before Query 2 when needed.
- F05 reached terminal success on Query 1.
- F02, F03, F04, F06, and F07 reached terminal success on Query 2.
- Query 3 was not needed for any task.
- total query-only count: 11
- all final states: `success / Finish`
- signed URLs were not printed or copied into the report.

Each query envelope and separately parsed query evidence is hashed and referenced from its consolidated technical record.

## 12. Result-count gates

Every successful task returned exactly:

- result_images_count: 0
- result_videos_count: 1
- result_output_count: 1
- download_url_present: true

Result-count match: true for all six tasks.

## 13. Download evidence

- one authorized download was executed for each successful submit ID;
- total download count: 6;
- each download returned the same submit ID and terminal `success / Finish` state;
- each task directory received exactly one MP4 file;
- no task was downloaded more than once.

Download envelopes and parsed download evidence are referenced by the six technical records. Provider media remains untracked and uncommitted.

## 14. Technical media validation

| Experiment | Dimensions | FPS | Decoded/reported frames | Duration | SHA256 | Valid |
|---|---:|---:|---:|---:|---|---:|
| F02 | 720x1280 | 24.1196 | 121/121 | 5.0167s | `6d1297d1b34e8998c0f83f4c1be6299652d76ba786b403011af049857a257b69` | true |
| F03 | 1280x720 | 24.1196 | 121/121 | 5.0167s | `3eae1d0d07490d884c1fd5a3473ce95edfee8347cff086e0d5650375a4e67327` | true |
| F04 | 1280x720 | 24.1196 | 121/121 | 5.0167s | `5fc8e692bbb85a54d909119d907f098dc4f6fcfaa2fb3d58febaff757aa3e32c` | true |
| F05 | 1280x720 | 24.1196 | 121/121 | 5.0167s | `06e771faa635fccc08f64b34fd01d279b12301b8bb3fbc5aebd3494c0ef5946c` | true |
| F06 | 1280x720 | 24.1196 | 121/121 | 5.0167s | `3bfd237ed2da9911ad6829335bb267471afa46dfa68e4ddccd0c0fa49119fb14` | true |
| F07 | 1280x720 | 24.1196 | 121/121 | 5.0167s | `e2912cca0acfcec913371b9dd62436c321632eff93e3e805b6b23a1665343412` | true |

Checks included nonzero file size, MP4 container, H.264 codec, full sequential decode, stable dimensions, reported-versus-decoded frame agreement, duration, and expected or explicit aspect ratio. This is technical validation only, not visual approval.

## 15. Credit reconciliation

- initial live credit before F02: 6377
- final live credit after F07: 5957
- observed T4 delta: 420
- submit-response costs: six times 70
- per-task pre/post/final deltas: all 70 and fully reconciled
- all task costs at or below 70: true
- remaining-six budget exceeded: false
- seven-family cumulative cost: 490, including F01's 70

## 16. Review-artifact creation

Each downloaded video received exactly eight local review paths:

- one review metadata JSON;
- frames at 0.00s, 1.00s, 2.00s, 3.00s, and 4.00s;
- one final readable frame;
- one 3x2 contact sheet.

Total review artifact paths: 48. No cut, visual score, winner selection, or finalization was created.

## 17. Technical-record creation

| Record | SHA256 |
|---|---|
| `CAL001-F02-P2-R1_technical_execution_record.json` | `633e9d13a9d5d442369b1671ce3d4e12c88bce30ca0c40e3f7284938a6f7660f` |
| `CAL001-F03-P2-R1_technical_execution_record.json` | `79b32a9558796ac3b96c2af564d4f4a928458da6e5a8a69ea31443b944adb9e5` |
| `CAL001-F04-P2-R1_technical_execution_record.json` | `963e96287627378da5d00c82c58465e729bf4f92b3339c0e9890b58bc7305b69` |
| `CAL001-F05-P2-R1_technical_execution_record.json` | `9dee836fe2e6f5cef1a4da7fc6923d7f58eca7e348cb665fdc6d93916a3b8962` |
| `CAL001-F06-P2-R1_technical_execution_record.json` | `52dd3a1c69c440b1fac7bf2b5568e9c25a7e617e38ad02d123cc7658815644e5` |
| `CAL001-F07-P2-R1_technical_execution_record.json` | `a5bd525cc8a2f825c25a623144408453f40b287cb7ea509cc3e77ba16f6559da` |

These hashes were captured after authority closure fields were set to false. Final validation may recompute them before commit.

## 18. Dataset updates

- dataset: `experiments/CAL-001/datasets/CAL001_experiment_results_template.csv`
- CSV row count: 84
- CSV readable: true
- changed rows: exactly F02-P2-R1 through F07-P2-R1
- F01 row unchanged: true
- visual scores and labels in the six updated rows: blank
- human review status: `not_started`
- candidate status: `unreviewed`
- `CAL001_visual_review_template.jsonl`: unchanged

Only technical execution fields were populated.

## 19. Stop-condition evaluation

- stop_condition_triggered: false
- stop_condition_reason: null
- repository/Source/hash/wrapper/command/login/logger/upload/provider/safety/account anomalies: none
- credit anomalies: none
- query-limit or terminal-state anomalies: none
- result-count/download/media-validation anomalies: none

One F06 upload took longer than the initial tool yield, but its original PTY session completed normally and persisted the required wrapper evidence. No duplicate submit was issued.

## 20. Completed and unattempted tasks

Completed T4 tasks:

- `CAL001-F02-P2-R1`
- `CAL001-F03-P2-R1`
- `CAL001-F04-P2-R1`
- `CAL001-F05-P2-R1`
- `CAL001-F06-P2-R1`
- `CAL001-F07-P2-R1`

Unattempted authorized T4 tasks: none.

## 21. A15 actual-cost conclusion

`A15_actual_per_task_cost_status=confirmed_70_credits_for_each_F02_through_F07_and_all_seven_family_canaries`

All six T4 tasks cost exactly 70 credits. Combined with F01, all seven fixed-family canaries cost exactly 490 credits.

## 22. A16 provider-behavior conclusion

`A16_provider_behavior_status=technical_success_confirmed_for_image2video_frames2video_and_multimodal2video_under_bounded_canary_contract`

- image2video: F02-F04 each produced one technically valid video;
- frames2video: F05 produced one technically valid video;
- multimodal2video: F06-F07 each produced one technically valid video;
- all tasks completed within one or two bounded queries;
- no technical provider failure occurred.

This conclusion does not claim Prompt quality, visual success, family superiority, or production readiness.

## 23. Remaining authority state

- authorization_scope_active: false
- execution_authority_active: false
- remaining_noncanary_tasks_authorized: false
- CAL001B_authorized: false
- visual_scoring_authorized: false
- retry_authorized: false
- resubmit_authorized: false
- final_master: false
- locked: false

## 24. Media/Git boundary

All downloaded MP4 files, extracted PNG frames, contact sheets, review metadata in run directories, and raw wrapper evidence remain local and unstaged. Only authorized technical JSON, CSV, and Markdown evidence may be staged.

## 25. Explicit non-actions

- no F01 re-execution;
- no retry or resubmit;
- no replacement task;
- no Prompt rewrite;
- no manifest or batch expansion;
- no Source modification;
- no visual scoring or visual approval;
- no candidate classification;
- no family winner or global Prompt architecture selection;
- no final or lock;
- no media staging.

## 26. Recommended next phase

`CAL-001-P3B-R2-T5_SIX_FAMILY_VISUAL_REVIEW_AND_POST_CANARY_DECISION`

The next phase requires separate authority. It should review the six local videos/contact sheets and record visual judgments without inheriting live execution authority.

## 27. Final verdict

`CAL001_P3B_R2_REMAINING_SIX_FAMILY_CANARY_COMPLETED_READY_SIX_FAMILY_VISUAL_REVIEW`
