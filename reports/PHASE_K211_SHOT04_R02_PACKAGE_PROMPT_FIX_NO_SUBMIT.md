# PHASE K211 - SHOT-04 R02 Package / Prompt Fix, No Submit

## Purpose

K211 applies a narrow no-submit prompt/package fix after K210 classified the SHOT-04 R02 package as `NEEDS_PACKAGE_FIX_BEFORE_AUTHORIZATION`. The fix strengthens prompt constraints while preserving the K209/K208 4-reference strategy and all no-submit/final/lock boundaries.

## Inputs Inspected

- `reports/PHASE_K210_SHOT04_R02_PACKAGE_FILE_HUMAN_REVIEW_SUBMIT_READINESS_NO_SUBMIT.md`
- `productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt`
- `productions/chi_yan_tian_qiong/prompts/shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit.csv`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/README.md`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/reference_duty_map.md`

## Files Modified

- `productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt`
- `productions/chi_yan_tian_qiong/prompts/shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit.csv`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/README.md`

## Files Created

- `reports/PHASE_K211_SHOT04_R02_PACKAGE_PROMPT_FIX_NO_SUBMIT.md`

## K210 Issue Summary

K210 found the package structure, JSON, CSV, reference paths, reference duties, task metadata, and no-submit/final/lock flags valid. The remaining blocker was prompt readiness: several L3 safety and visual-control constraints were missing or too implicit.

## Prompt Fix Summary

The manual prompt was patched to explicitly preserve the core action grammar while adding the missing K210 constraints. The reference set was not changed.

Revised prompt sha256:

`609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`

## Exact Missing Constraints Now Added

- Impact center is between pillars.
- Fighters' bodies must not hide the wall impact center.
- No sustained pushing.
- No wrestling hold.
- No slow static pressure.
- No body pin with no rebound.
- No railing/lattice confusion.
- No generic courtyard drift.
- No interior hall drift.
- No empty architecture-only scene.
- No random holes.
- No non-causal damage.
- No spontaneous debris before contact.
- Wall cracks/splinters/spray only after Shuangji shoulder / upper-back contact.
- No magic blast replacing body contact.
- No energy shockwave as main event.
- Body contact and wall reaction must be the main event.
- No body embedded inside wall.
- No body-wall fusion.
- No gore.
- This draft is not final.
- This draft is not locked.
- No final-frame language.
- No locked-frame language.
- Human review required after generation.

## JSON Validation Result

K211 validation passed:

- JSON parses successfully.
- `task_type=multimodal2video`.
- `model_version=seedance2.0_vip`.
- `duration=5`.
- `ratio=16:9`.
- `video_resolution=720p`.
- `manual_prompt_sha256=609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`.
- `package_status=package_prompt_fixed_no_submit`.
- `submit_allowed=false`.
- `query_allowed=false`.
- `download_allowed=false`.
- `no_submit_boundary=true`.
- `human_review_required=true`.
- `final_master=false`.
- `locked=false`.

## CSV Validation Result

K211 validation passed:

- CSV reads successfully.
- Exactly 1 row.
- Task metadata unchanged.
- 4 reference IDs remain unchanged.
- Prompt sha256 recorded and matches JSON / prompt file.
- `status=package_prompt_fixed_no_submit`.
- `submit_allowed=false`.
- `query_allowed=false`.
- `download_allowed=false`.
- `final_master=false`.
- `locked=false`.
- `human_review_required=true`.

## Reference Path / Duty Validation Result

The preferred 4-reference strategy remains unchanged:

| Reference | Duty |
| --- | --- |
| `A-SC-TEMPLE-SIDE-WALL-PANEL-002` | Architecture / wall target only |
| `A-CH-A-SUBJECT-001` | Fenshou identity only |
| `A-CH-B-IDENTITY-002` | Shuangji face / upper-body identity anchor |
| `A-CH-B-SUBJECT-001` | Shuangji full-body costume / silhouette support |

All four reference paths are locally present. Reference duties remain unchanged.

## No-Submit / Final / Lock Flag Validation

K211 does not authorize submit. All package flags remain no-submit and non-final:

- `submit_allowed=false`
- `query_allowed=false`
- `download_allowed=false`
- `final_master=false`
- `locked=false`

## Media / Source Governance Confirmation

- No Dreamina command was run.
- No submit, query, download, retry, resubmit, or batch action happened.
- No media was generated, edited, staged, or committed.
- No contact sheet or review frame was created.
- No `sources/` file was modified, staged, or committed.
- No runtime code or `configs/providers.json` was modified.
- No auth/session/token/key/env file was opened, printed, staged, or committed.

## Known Limitations

This is still a text-only package/prompt fix. It does not prove Dreamina will produce the intended result. The next phase must re-review package readiness before any human L3 submit authorization.

## Recommended K212

K212 = SHOT-04 R02 Package File Submit-Readiness Re-Review, No Submit.

## Final Verdict

SHOT04_R02_PACKAGE_PROMPT_FIX_NO_SUBMIT_READY_K212_SUBMIT_READINESS_REVIEW
