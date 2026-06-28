# SHOT-04 R02 Wall-Impact Package Draft

Status: package_prompt_fixed_no_submit

This directory contains the K209 no-submit package draft for SHOT-04 R02 wall-impact planning. It is a planning/package draft only. It does not authorize Dreamina submit, query, download, retry, resubmit, batch execution, final-master marking, or locking.

## Lineage

- K202 approved `A-SC-TEMPLE-SIDE-WALL-PANEL-002` as an architecture target reference only.
- K203 planned wall-impact reference usage.
- K204 defined package-draft planning.
- K205 selected contact and character reference duties.
- K206 defined the action-composition grammar.
- K207 froze the intended reference set for planning.
- K208 selected the preferred 4-reference strategy for K209.
- K210 reviewed the package and found the structure safe but the prompt negative constraints not explicit enough for L3 submit-readiness.
- K211 patched the prompt gaps while keeping the same 4-reference strategy and no-submit boundary.

## Package Intent

The future SHOT-04 R02 action target is:

Fenshou explosive shoulder-check into Shuangji crossed guard -> Shuangji right shoulder / upper back hits mid-height wet wooden wall panel -> localized wet-wood flex, cracks, splinters, and rain spray -> immediate rebound.

The package keeps the wall impact readable as a cause-effect event. It must not become a general destruction shot, a final frame, or a locked master.

## Reference Strategy

Preferred 4-reference strategy:

| Reference | Duty |
| --- | --- |
| `A-SC-TEMPLE-SIDE-WALL-PANEL-002` | Architecture target reference only |
| `A-CH-A-SUBJECT-001` | Fenshou identity only |
| `A-CH-B-IDENTITY-002` | Shuangji face / upper-body identity anchor |
| `A-CH-B-SUBJECT-001` | Shuangji full-body costume / silhouette support |

Fallback 3-reference strategy is not used in this draft because existing multimodal2video package conventions support multiple references and K208 preferred the 4-reference strategy.

## Draft Files

- Manual prompt draft: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt`
- Package JSON: `productions/chi_yan_tian_qiong/prompts/shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit.csv`
- Reference duty map: `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/reference_duty_map.md`
- K209 report: `reports/PHASE_K209_SHOT04_R02_PACKAGE_FILE_DRAFT_NO_SUBMIT.md`

## Hard Boundaries

- `submit_allowed=false`
- `query_allowed=false`
- `download_allowed=false`
- `human_review_required=true`
- `final_master=false`
- `locked=false`
- No Dreamina command was run in K209.
- No media was created, edited, staged, or committed in K209.

## K211 Prompt Fix Summary

K211 added explicit constraints for impact-center visibility, anti-push / anti-wrestling behavior, wall/object confusion, damage causality, magic/energy suppression, body/wall safety, and not-final / not-locked language.

The revised prompt sha256 is:

`609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`

Recommended next phase:

K212 = SHOT-04 R02 package file submit-readiness re-review, no submit.
