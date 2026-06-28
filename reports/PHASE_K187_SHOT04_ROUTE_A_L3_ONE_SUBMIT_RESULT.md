# PHASE K187 - SHOT-04 Route A L3 One-Submit Result

## 1. Purpose

Submit the reviewed SHOT-04 Route A package exactly once and record the result.

This report is the canonical K187 L3 one-submit record for:

- `project_name=chi_yan_tian_qiong`
- `shot_id=SHOT-04-V001`
- `variant_id=routeA_railing_lattice_impact_rebound`
- `task_type=multimodal2video`

Important boundary note: the live submit already occurred once in K187 and returned a valid `submit_id`. This report records that same submit result. No second submit was run for this canonical report.

## 2. Authorization Level

Authorization level: `L3 one-submit only`

Allowed:

- corrected Dreamina preflight
- exactly one submit
- `--poll 0`
- text-only submit report

Forbidden:

- query_result
- download
- retry
- resubmit
- batch
- final decision
- lock decision
- source modification
- media staging

## 3. Human Authorization Quote

The human authorized K187:

> 授权 K187：对 SHOT-04 Route A package 执行 L3 one-submit only。允许 corrected Dreamina preflight：dreamina version、dreamina user_credit、dreamina multimodal2video -h；允许使用 K185 已通过的 package 执行 exactly one submit，--poll 0。禁止 query、download、retry、resubmit、batch、final、lock、修改 sources/、stage media。提交后只记录 submit_id/logid/gen_status/credit_count/fail_reason，并创建 K187 submit report。

## 4. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K186_SHOT04_ROUTE_A_PACKAGE_REVIEW_READY_FOR_HUMAN_SUBMIT_DECISION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K185_SHOT04_ROUTE_A_L2_NO_SUBMIT_PACKAGE_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_v001_routeA_railing_lattice_impact_rebound_multimodal2video_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-V001_routeA_no_submit.csv`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K187_SHOT04_ROUTE_A_SINGLE_SUBMIT_RESULT.md`

## 5. Source Governance Confirmation

- `sources/` was clean at preflight.
- `sources/` was not modified.
- `sources/` was not staged.
- Official Source authority remains with the human user.
- This report is evidence only, not official Source.

## 6. Package Review Carry-Forward

K186 package review status:

`pass_ready_for_human_K187_submit_authorization_decision`

Package hashes verified:

| artifact | path | sha256 |
|---|---|---|
| prompt txt | `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt` | `dfbbc3c03ceede3c134d5464aaad8faf5bdcf38ddbe5cbf8277e6abcc70517e1` |
| package JSON | `productions/chi_yan_tian_qiong/prompts/shot_04_v001_routeA_railing_lattice_impact_rebound_multimodal2video_package_no_submit.json` | `c853c3158d4bf2f45e47309efcc70226d859f30edbf1f7dac6c5ae903b9d7834` |
| manifest CSV | `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-V001_routeA_no_submit.csv` | `856b35781c1c3953710145f5487dae3a5292c3b14698721936dd73ae715979ce` |

Safety flags before explicit K187 submit authorization:

- `submit_allowed=false`
- `query_allowed=false`
- `download_allowed=false`
- `retry_allowed=false`
- `resubmit_allowed=false`
- `final_master=false`
- `locked=false`

The explicit K187 human authorization permitted exactly one submit despite the no-submit package state. It did not authorize query or download.

## 7. Reference Validation

| label | path | exists | sha256 | sha256_matches_expected |
|---|---|---:|---|---:|
| `FENSHOU_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | true | `70c01dec0bc3aa0eadd9f554c731be4991320b742cb2f9a2f1195a0d4f08bed3` | true |
| `SHUANGJI_IDENTITY_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | true | `fbc0e674e19d74c9ba4b8488e2c4da79f0a415e1c6811d0613803150bd9bad1d` | true |
| `RAINY_TEMPLE_SCENE_REF` | `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg` | true | `f2117d0ac806179dd2ac5f009d3483184b500ba2489512894059379c73bc531b` | true |

## 8. Corrected Dreamina Preflight

Dreamina executable path:

`C:/Users/msjpurf/bin/dreamina.exe`

Dreamina version:

```json
{
  "version": "46b5b0e-dirty",
  "commit": "46b5b0e",
  "build_time": "2026-06-03T19:39:25Z"
}
```

User credit summary:

```json
{
  "total_credit": 1830,
  "user_id": 1611200923726843,
  "user_name": "",
  "vip_level": "maestro"
}
```

`multimodal2video -h` checked: true

Command contract:

| requirement | status |
|---|---|
| `--image` repeated | valid |
| `--prompt` | valid |
| `--duration` | valid |
| `--ratio` | valid |
| `--video_resolution` | valid |
| `--model_version` | valid |
| `--poll` | valid |
| `seedance2.0_vip` | valid |
| duration `5` | valid |
| ratio `16:9` | valid |
| video_resolution `720p` | valid |

`command_contract_valid=true`

## 9. Exact Submit Command Used

The prompt was read from the approved K185 prompt txt with UTF-8 encoding.

```powershell
$prompt = Get-Content -Raw -Encoding UTF8 "productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt"
C:\Users\msjpurf\bin\dreamina.exe multimodal2video `
  --image "productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg" `
  --image "productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg" `
  --image "productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg" `
  --prompt "$prompt" `
  --model_version seedance2.0_vip `
  --duration 5 `
  --ratio 16:9 `
  --video_resolution 720p `
  --poll 0
```

## 10. Submit Result

| field | value |
|---|---|
| submit_attempted | true |
| submit_count | 1 |
| submit_id | `39f10fdc-50c8-4d03-ae59-c1189447300b` |
| logid | `20260628134823169254047008236EE77` |
| gen_status | `querying` |
| credit_count | `70` |
| fail_reason | none returned |

Raw response summary:

```json
{
  "submit_id": "39f10fdc-50c8-4d03-ae59-c1189447300b",
  "logid": "20260628134823169254047008236EE77",
  "gen_status": "querying",
  "credit_count": 70
}
```

## 11. Boundary Confirmation

| boundary | value |
|---|---:|
| query_run | false |
| download_run | false |
| retry_run | false |
| resubmit_run | false |
| batch_run | false |
| media_created | false |
| media_staged | false |
| final_master | false |
| locked | false |

## 12. Recommended Next Phase

K188 should be a one-query authorization decision for existing submit id:

`39f10fdc-50c8-4d03-ae59-c1189447300b`

K188 must not download unless separately authorized by the human.

## 13. What Not To Do

- Do not query without explicit K188 authorization.
- Do not download without explicit authorization.
- Do not retry.
- Do not resubmit.
- Do not mark final.
- Do not lock.
- Do not update Source.
- Do not stage media.

## 14. Safety Confirmation

- Corrected preflight completed.
- Exactly one submit was run.
- No second submit was run for this canonical report.
- `--poll 0` was used.
- No query was run.
- No download was run.
- No retry was run.
- No resubmit was run.
- No batch was run.
- No media was staged.
- `final_master=false`
- `locked=false`

## 15. Final Verdict

SHOT04_ROUTE_A_L3_SUBMITTED_NO_QUERY_NO_DOWNLOAD_READY_K188_QUERY_AUTHORIZATION
