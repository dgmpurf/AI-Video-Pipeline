# PHASE K270F - SHOT-04 R02A2 Dynamic Fly-Out Variant Selection And Submit Authorization Decision

## 1. Phase summary

- phase_id: K270F_SHOT04_R02A2_DYNAMIC_FLYOUT_VARIANT_SELECTION_AND_SUBMIT_AUTHORIZATION_DECISION
- purpose: record report-only variant selection and future one-submit-only authorization for SHOT-04 R02A2 dynamic fly-out B3 primary variant.
- authorization_recorded: true
- selected_variant_for_submit: B3_RESULT_ONLY_FLYOUT_AFTER_HIT
- selected_asset_id: SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001
- backup_variant: B1_WIDE_SIDE_FLYOUT_RESULT_SHOT
- backup_variant_submit_authorized: false
- K270F_submit_executed: false
- final_master: false
- locked: false

## 2. UTF-8 authorization reconstruction and SHA256 verification

- authorization_source: AUTHORIZATION_TEXT_UTF8_BASE64 from K270F request.
- decoded_as: UTF-8
- expected_sha256: `fef6e5899c2f0f7be28ecf62f94ed6852ea0b19c7c6fd0891a757fcc6de42865`
- actual_decoded_utf8_sha256: `fef6e5899c2f0f7be28ecf62f94ed6852ea0b19c7c6fd0891a757fcc6de42865`
- decoded_authorization_sha256_match: true
- decoded_text_begins_with: `我授权 K270F`
- required_phrases_present: true
- forbidden_mojibake_markers_present: false

## 3. Human authorization text

```text
我授权 K270F：选择 K270E 推荐的 B3_RESULT_ONLY_FLYOUT_AFTER_HIT（SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001）进入 one-submit-only 授权记录。只允许下一阶段对 B3 执行一次 multimodal2video submit；B1_WIDE_SIDE_FLYOUT_RESULT_SHOT 仅保留为备选，不授权 submit。不允许 query/download/retry/resubmit/batch/final/lock。
```

## 4. Authorization interpretation

- K270F records authorization only.
- K270F does not execute submit.
- K270F selects B3_RESULT_ONLY_FLYOUT_AFTER_HIT for a future one-submit-only phase.
- Future K270G may execute exactly one Dreamina multimodal2video submit for B3 only if fresh preflight/canary and command-contract checks pass.
- B1_WIDE_SIDE_FLYOUT_RESULT_SHOT remains backup only and is not authorized for submit.
- Query, download, retry, resubmit, batch, final, and lock are not authorized.

## 5. K270E package review carry-forward

- K270E_review_outcome: package_review_pass_with_nonblocking_notes
- K270E_variants_reviewed:
  - B3_RESULT_ONLY_FLYOUT_AFTER_HIT
  - B1_WIDE_SIDE_FLYOUT_RESULT_SHOT
- K270E_recommended_variant_order: B3 primary, B1 backup
- K270E_selected_variant_for_future_authorization: B3_RESULT_ONLY_FLYOUT_AFTER_HIT
- K270E_backup_variant: B1_WIDE_SIDE_FLYOUT_RESULT_SHOT
- K270E_hash_verification_summary: all K270D prompt/package/manifest/notes/ref hashes matched expected values.
- K270E_no_submit_gate_summary: no_submit=true; submit/query/download/retry/resubmit/batch/final/lock all false.
- K270E_is_submit_authorization: false

## 6. Selected B3 variant identity

- variant_id: B3_RESULT_ONLY_FLYOUT_AFTER_HIT
- asset_id: SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001
- semantic_label: R02A2_DYNAMIC_FLYOUT_RESULT_ONLY_AFTER_HIT
- task_type: multimodal2video
- model_version: seedance2.0_vip
- duration: 5
- ratio: 16:9
- video_resolution: 720p
- poll: 0
- no_submit_currently: true
- future_submit_authorization: exactly one submit only in K270G if K270G preflight passes.

## 7. B1 backup status and non-authorization

- backup_variant_id: B1_WIDE_SIDE_FLYOUT_RESULT_SHOT
- backup_asset_id: SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B1-WIDE-SIDE-M2V-001
- backup_status: backup only
- submit_authorized: false
- K270F_explicit_non_authorization: B1 is not authorized for submit.
- future_use: B1 may be considered only through a separate future authorization phase.

## 8. B3 prompt/package/manifest carry-forward

| artifact | path | expected_sha256 | actual_sha256 | result |
|---|---|---|---|---|
| B3 prompt | `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001_multimodal2video_no_submit_prompt.txt` | `b730505bf810fcb4e66e008aafd723412ff22ffd1cc404fd3401241250ee53f0` | `b730505bf810fcb4e66e008aafd723412ff22ffd1cc404fd3401241250ee53f0` | pass |
| B3 package | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001_package.json` | `34b23610029f4d40da22d3c4595e0de1c185bff382f6fd30f915dfb8cddcb3d8` | `34b23610029f4d40da22d3c4595e0de1c185bff382f6fd30f915dfb8cddcb3d8` | pass |
| manifest | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-K270D_dynamic_flyout_no_submit_manifest.csv` | `379d1a248d3f8eb9ff06686f2e418bf85fcc13dc152a97949b2487658c5be100` | `379d1a248d3f8eb9ff06686f2e418bf85fcc13dc152a97949b2487658c5be100` | pass |
| review notes | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-K270D_dynamic_flyout_no_submit_review_notes.md` | `76927359d8962ae4e4e1d39038042fade3fa18d777dbcd2059a0e7471fa7b671` | `76927359d8962ae4e4e1d39038042fade3fa18d777dbcd2059a0e7471fa7b671` | pass |

- B3_package_json_parse: passed
- B3_no_submit: true
- B3_submit_authorized_current_package_flag: false
- B3_query_authorized: false
- B3_download_authorized: false
- B3_retry_authorized: false
- B3_resubmit_authorized: false
- B3_batch_authorized: false
- B3_final_master: false
- B3_locked: false

## 9. Reference carry-forward and validation

| alias | path | expected_sha256 | actual_sha256 | validation |
|---|---|---|---|---|
| @FENSHOU_LOCKED_REF | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | pass |
| @SHUANGJI_LOCKED_REF | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | pass |

- Fenshou duty: Fenshou identity only, black-red armored attacker / follow-through presence only.
- Shuangji duty: Shuangji identity only, blue-white-silver defender launched backward.
- refs_modified: false

## 10. Future K270G one-submit-only scope

Future K270G may:

1. Use PowerShell-visible CLI: `C:/Users/msjpurf/bin/dreamina.exe`
2. Run fresh canary/preflight:
   - `dreamina version`
   - `dreamina user_credit`
   - `dreamina multimodal2video -h`
3. Verify B3 command contract against current help.
4. Verify B3 prompt/package/manifest hashes.
5. Verify both local reference images exist and are readable.
6. Execute exactly one multimodal2video submit for B3.
7. Use `--duration 5`, `--ratio 16:9`, `--video_resolution 720p`, `--model_version seedance2.0_vip`, `--poll 0`.
8. Record submit_id / logid / gen_status / credit_count if returned.
9. Stop immediately after submit result.

Future K270G must not:

- submit B1
- run more than one submit
- query
- download
- retry
- resubmit
- batch
- create media review artifacts
- cut video
- extract frames
- create contact sheets
- final
- lock

## 11. Future K270G command-shape summary

Expected future B3 command shape:

```text
C:/Users/msjpurf/bin/dreamina.exe multimodal2video --prompt "<contents of B3 prompt_path>" --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png" --image "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png" --duration 5 --ratio 16:9 --video_resolution 720p --model_version seedance2.0_vip --poll 0
```

Command-shape cautions:

- Do not add `--download_dir`.
- Do not add `output_dir` as a submit flag.
- Do not query after submit.
- Submit success is not query success.
- Submit success is not download success.
- Submit success is not visual success.
- Query/download require later separate authorization.

## 12. Diagnostic intent

B3 is designed as Beat B after existing CONTACT_HITSTOP_SHORT Beat A.

The goal is result-only fast fly-out after hit-stop:

- Shuangji already being launched backward.
- visible travel distance.
- wet floor splash / rain spray / debris.
- no prolonged contact.
- no re-solving guard clash.
- no sustained pressure.
- no gentle shove.
- no delayed reaction.
- no small displacement.

K270F only records the authorization decision. K270G will test whether B3 can create the remote task.

## 13. Explicitly forbidden actions

Forbidden in K270F:

- run Dreamina
- run dreamina version/user_credit/help
- submit
- query
- download
- retry
- resubmit
- batch
- create media
- cut video
- assemble cuts
- modify any mp4
- extract frames
- create contact sheets
- create prompt files
- create package JSON
- create manifest CSV
- modify prompt files
- modify package JSON files
- modify manifest CSV
- modify review notes
- modify sources/
- stage media
- stage generated cuts
- stage review artifacts
- set final_master=true
- set locked=true
- tag
- print token/cookie/session/auth/env/signed URL contents

## 14. Git/source preflight

- branch_status: `## main...origin/main`
- sources_status: clean
- tracked_diff_preflight: none
- staged_diff_preflight: none
- known_untracked_noise_present: `.vs/`, `productions/chi_yan_tian_qiong/edits/`, `productions/chi_yan_tian_qiong/review_artifacts/`, `reports/context_recovery/`
- unexpected_tracked_changes: none
- block_status: not blocked

## 15. Files read

- `reports/PHASE_K270E_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_REVIEW.md`
- `reports/PHASE_K270D_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_CREATION_RESULT.md`
- `reports/PHASE_K270C_SHOT04_R02A2_DYNAMIC_FLYOUT_NO_SUBMIT_PACKAGE_AUTHORIZATION_DECISION.md`
- `reports/PHASE_K270B_SHOT04_R02A_STATIC_DYNAMIC_BURST_TWO_SHOT_ROUTE_PLANNING.md`
- `reports/PHASE_K270A_SHOT04_R02A_STATIC_DYNAMIC_BURST_ROUTE_DECISION.md`
- `reports/PHASE_K269Z_SHOT04_R02A_VARIANT_A_CUT_WINDOW_VISUAL_REVIEW.md`
- `reports/PHASE_K269Y_SHOT04_R02A_VARIANT_A_CUT_WINDOW_DIAGNOSTICS_ONLY_RESULT.md`
- `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001_multimodal2video_no_submit_prompt.txt`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-V-DYNAMIC-FLYOUT-B3-RESULT-ONLY-M2V-001_package.json`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-K270D_dynamic_flyout_no_submit_manifest.csv`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A2-dynamic-flyout/K270D/SHOT-04-R02A2-K270D_dynamic_flyout_no_submit_review_notes.md`
- `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`
- optional backup context: B1 prompt and B1 package JSON
- read-only Source context under `sources/`, including Dreamina help/schema context.

## 16. Encoding verification

- visible_authorization_line_may_be_corrupted: true
- base64_decoded_text_used_as_source_of_truth: true
- decoded_text_preserved_readably: true
- decoded_authorization_sha256_match: true
- actual_decoded_utf8_sha256: `fef6e5899c2f0f7be28ecf62f94ed6852ea0b19c7c6fd0891a757fcc6de42865`
- required_variant_terms_present: true
- required_no-action_terms_present: true
- forbidden_mojibake_markers_present: false

## 17. Source governance confirmation

- Official Project Source files remain human-controlled.
- Codex read Source context only.
- sources_modified: false
- source_updates_created: false
- source_updates_staged: false
- this_report_is_official_Source: false

## 18. Risk acknowledgement

- K270F is not submit execution.
- B3 submit may fail technically or remotely.
- Submit success is not query/download/visual success.
- B3 may still fail visually, including insufficient displacement, identity drift, floating, slow shove, weak rain/floor feedback, or static aftermath.
- B1 remains backup only and is not authorized.
- Query/download require later separate human authorization.
- Final/lock requires later explicit human approval.

## 19. Safety flags

- no_Dreamina: true
- no_submit_in_K270F: true
- no_query: true
- no_download: true
- no_retry_resubmit: true
- no_batch: true
- no_media_created: true
- no_video_cut: true
- no_video_modified: true
- no_frames_contact_sheets_created: true
- no_prompt_package_manifest_modified: true
- no_sources_modified: true
- B3_future_submit_count_limit: 1
- B1_submit_authorized: false
- final_master: false
- locked: false

## 20. Recommended next phase

- recommended_next_phase: K270G_SHOT04_R02A2_DYNAMIC_FLYOUT_B3_ONE_SUBMIT_ONLY

K270G should:

- be the actual one-submit-only execution phase.
- use PowerShell-visible CLI: `C:/Users/msjpurf/bin/dreamina.exe`
- run Dreamina canary/preflight.
- verify multimodal2video command contract.
- verify B3 prompt/package/manifest/ref hashes.
- submit exactly once for B3.
- not submit B1.
- not query.
- not download.
- not retry/resubmit/batch.
- not final/lock.

## 21. Final verdict

K270F_DYNAMIC_FLYOUT_B3_ONE_SUBMIT_AUTHORIZATION_RECORDED_READY_K270G
