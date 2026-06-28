# PHASE K195 - SHOT-04 R02 Wall-Panel Architecture Reference L3 Submit Result

## 1. Purpose

Submit `A-SC-TEMPLE-SIDE-WALL-PANEL-001` wall-panel architecture reference `image2image` package exactly once.

This is an architecture-only reference image generation for later SHOT-04 R02 wall-panel / side-wall contact planning. It is not SHOT-04 R02 combat, not a contact keyframe, not a video package, not a final keyframe, and not locked.

Collected at: `2026-06-28 17:00:35 +08:00`

## 2. Authorization Level

Authorization level: `L3 one-submit only`

Human authorization allowed:

- corrected Dreamina preflight,
- exactly one `image2image` submit,
- `--poll 0`,
- one K195 submit result report.

Forbidden and not performed:

- query,
- download,
- retry,
- resubmit,
- batch,
- final/lock,
- media creation,
- media staging,
- package rewrite,
- source update.

The K193 package metadata still says `submit_allowed=false`; that metadata remains unchanged. K195 human authorization overrides only this phase's live action boundary for exactly one submit. Query, download, retry, resubmit, final, and lock remain forbidden.

## 3. Human Authorization Quote

The human explicitly authorized K195 to run corrected Dreamina preflight and submit exactly one `image2image` task for the K193/K194-approved package:

`A-SC-TEMPLE-SIDE-WALL-PANEL-001`

## 4. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K194_SHOT04_R02_WALL_PANEL_ARCH_REF_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K193_SHOT04_R02_WALL_PANEL_ARCH_REF_L2_PACKAGE_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/A-SC-TEMPLE-SIDE-WALL-PANEL-001_wall_panel_target_ref_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/a_sc_temple_side_wall_panel_001_image2image_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_A-SC-TEMPLE-SIDE-WALL-PANEL-001_no_submit.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.7.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化宏流程与授权等级_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`

## 5. Source Governance Confirmation

`sources/` was checked before live execution and was clean. Sources were read only as reference material.

- `source_read_allowed=true`
- `source_recommendation_allowed=true`
- `source_write_allowed=false`
- `source_stage_allowed=false`
- `source_commit_allowed=false`
- `source_push_allowed=false`
- `official_source_update_requires_human_manual_action=true`

No official Source update was created, edited, staged, committed, or pushed.

## 6. K194 Carry-Forward

K194 package review status:

`package_review_status=pass_with_minor_notes_ready_for_human_K195_submit_authorization_decision`

K194 final verdict:

`SHOT04_R02_WALL_PANEL_ARCH_REF_PACKAGE_REVIEW_PASS_WITH_MINOR_NOTES_READY_K195_SUBMIT_DECISION`

K194 non-blocking note:

The prompt begins with the asset id, but the prompt also explicitly says no text, no watermark, and no labels. This was not considered blocking, and K195 did not revise the prompt.

K194 recommended K195 as L3 one-submit-only `image2image`, with canary/preflight first and no query/download/retry/resubmit.

## 7. Package Validation

| item | value | status |
|---|---|---|
| prompt path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/A-SC-TEMPLE-SIDE-WALL-PANEL-001_wall_panel_target_ref_no_submit_prompt.txt` | exists, UTF-8 readable |
| prompt sha256 | `4da536ec98ffbe26c409b34b6d9c237272bf586add3863f3b987ccc5d09d98c9` | matches expected |
| package JSON path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/a_sc_temple_side_wall_panel_001_image2image_package_no_submit.json` | exists |
| package JSON sha256 | `668a8c87846838ee4a18705e901468b7e41337b076f5e92da13f04ac9594cfd7` | matches expected |
| package JSON parse | pass | valid |
| manifest CSV path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_image2image_A-SC-TEMPLE-SIDE-WALL-PANEL-001_no_submit.csv` | exists |
| manifest CSV sha256 | `7273a2bafae22545f09c2c82e67a577537fd7b6ccae70db68175d831409988f2` | matches expected |
| manifest CSV row count | 1 | pass |
| K193 report sha256 | `1ba03884b968e5482613fb8b451071644954f002e2b7085c306ae5dffac22352` | matches expected |

Package settings:

| setting | value | status |
|---|---|---|
| `task_type` | `image2image` | pass |
| `model_version` | `4.7` | pass |
| `ratio` | `16:9` | pass |
| `resolution_type` | `2k` | pass |
| `poll` | `0` | pass |
| `package_status` | `package_ready_no_submit` | pass |
| `submit_allowed` before K195 authorization | false | pass |
| `query_allowed` | false | pass |
| `download_allowed` | false | pass |
| `retry_allowed` | false | pass |
| `resubmit_allowed` | false | pass |
| `final_master` | false | pass |
| `locked` | false | pass |

Manifest settings:

| setting | status |
|---|---|
| image field contains exactly the `RAINY_TEMPLE_SCENE_REF` path | pass |
| video field empty | pass |
| audio field empty | pass |
| status is `package_ready_no_submit` | pass |

Package/ref validation result:

`pass`

## 8. Input Reference Validation

| field | value |
|---|---|
| label | `RAINY_TEMPLE_SCENE_REF` |
| path | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` |
| exists | true |
| expected sha256 | `f2117d0ac806179dd2ac5f009d3483184b500ba2489512894059379c73bc531b` |
| actual sha256 | `f2117d0ac806179dd2ac5f009d3483184b500ba2489512894059379c73bc531b` |
| sha256 matches expected | true |
| duty | rainy temple world/material/rain/light reference only; not exact composition, not character identity, not combat, not damaged wall, not final blocking |

## 9. Corrected Dreamina Preflight

Dreamina executable path:

`C:/Users/msjpurf/bin/dreamina.exe`

Version output summary:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

User credit result summary:

```json
{
  "total_credit": 1760,
  "user_id": 1611200923726843,
  "vip_level": "maestro"
}
```

No logger Access denied occurred. No login/auth failure occurred.

`dreamina image2image -h` result:

- command available,
- supports `--images`,
- supports `--prompt`,
- supports `--model_version`,
- supports `--ratio`,
- supports `--resolution_type`,
- supports `--poll`,
- supports model version `4.7`,
- supports ratio `16:9`,
- supports resolution type `2k`,
- confirms `--poll 0` disables polling.

Command contract:

`command_contract_valid=true`

Command contract notes:

- This is `image2image`.
- Input image must be supplied through `--images`, not `--image`.
- K195 used one image reference.
- No query/download was included in the command.

## 10. Exact Submit Command Used

Command shape used:

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/A-SC-TEMPLE-SIDE-WALL-PANEL-001_wall_panel_target_ref_no_submit_prompt.txt"
C:/Users/msjpurf/bin/dreamina.exe image2image `
  --images "G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg" `
  --prompt "$prompt" `
  --model_version 4.7 `
  --ratio 16:9 `
  --resolution_type 2k `
  --poll 0
```

Prompt file path and sha256 were used instead of rewriting the prompt in this command section:

- prompt path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/A-SC-TEMPLE-SIDE-WALL-PANEL-001_wall_panel_target_ref_no_submit_prompt.txt`
- prompt sha256: `4da536ec98ffbe26c409b34b6d9c237272bf586add3863f3b987ccc5d09d98c9`

## 11. Submit Result

| field | value |
|---|---|
| submit_attempted | true |
| submit_count | 1 |
| submit_id | `b5c17ce3-0541-42a7-914f-5ea3740d7d60` |
| logid | `20260628170014169254047008997B0E4` |
| gen_status | `querying` |
| credit_count | 1 |
| fail_reason | not returned |
| submit_exit_code | 0 |

Raw response summary:

Dreamina accepted the `image2image` submit and returned a real `submit_id`, `logid`, `gen_status=querying`, and `credit_count=1`. The response also echoed the prompt text; this report records the prompt path and prompt sha256 instead of duplicating the full prompt body here.

## 12. Boundary Confirmation

| boundary | value |
|---|---|
| query_run | false |
| download_run | false |
| retry_run | false |
| resubmit_run | false |
| batch_run | false |
| second_submit_run | false |
| media_created | false |
| media_staged | false |
| final_master | false |
| locked | false |
| prompt_modified | false |
| package_modified | false |
| manifest_modified | false |
| shot_record_modified | false |
| sources_modified | false |
| runtime_code_modified | false |
| configs/providers.json_modified | false |
| auth/session/token/key/env_opened_or_staged | false |

## 13. Recommended Next Phase

Recommended next phase:

`K196 = one-query-only authorization decision for the existing submit_id`

K196 should query only:

`submit_id=b5c17ce3-0541-42a7-914f-5ea3740d7d60`

K196 must not download unless the human separately authorizes download or the phase explicitly includes download permission.

## 14. What Not To Do

- Do not query without explicit K196 authorization.
- Do not download without explicit authorization.
- Do not retry.
- Do not resubmit.
- Do not batch.
- Do not mark final.
- Do not lock.
- Do not update Source.
- Do not stage media.

## 15. Safety Confirmation

- Corrected Dreamina preflight was run.
- Exactly one submit was run.
- No query was run.
- No download was run.
- No retry/resubmit/batch was run.
- No media was created or staged.
- No package/prompt/manifest/shot-record file was modified.
- No Source file was modified or staged.
- No runtime/config file was modified.
- No auth/session/token/key/env file was opened or staged.
- `final_master=false`
- `locked=false`

## 16. Final Verdict

SHOT04_R02_WALL_PANEL_ARCH_REF_L3_SUBMITTED_NO_QUERY_NO_DOWNLOAD_READY_K196_QUERY_AUTHORIZATION
