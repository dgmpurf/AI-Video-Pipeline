# PHASE K104 - SHOT-03 V002 Upload-Safe Continuity-Fix Package Ready

## Purpose

This phase creates the SHOT-03 V002 upload-safe continuity-fix no-submit package.

No Dreamina command was run. No submit/query/download happened. No AI media was generated. No media files were created, edited, moved, deleted, or staged.

This is a package-only phase. Final approval requires later human review.

## V001 Problem Being Fixed

SHOT-03 V001 was reviewed as `mixed_positive_needs_continuity_fix`.

What worked:

- Early combat was acceptable.
- Temple architecture appeared.
- Column/corridor, wet stairs, eaves/roofline, railings, and temple elements appeared.

Problems to fix:

- V001 appeared to start too deep inside the hall or corridor without an entry beat.
- The ending near the eaves / roof position felt abrupt.
- The route was useful, but compressed, creating a jumpy spatial feeling.

V002 uses V001 only as a text-only failure/correction reference. V001 MP4, contact sheet, and review frames are not active visual references.

## V002 Route

Selected V002 route:

`exterior veranda / column corridor edge start -> wet stone stairs midpoint -> eaves / roof-edge endpoint`

The main correction is exterior/semi-exterior spatial clarity. V002 should begin under the eaves or at the exterior veranda / column corridor edge, with courtyard/rain/exterior corridor relationship readable from the start.

Controlled local breakage is allowed:

- railing cracks
- wood panel / door lattice breaks
- door or window lattice damage
- a few roof tiles slide or scatter
- eaves wood splinters
- lantern or banner gets knocked aside
- rainwater and splinters react to impact

Large collapse and temple destruction remain reserved for later SHOT-04 / SHOT-05.

## Package Files

- Manual prompt: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V002_uploadsafe_continuity_fix_exterior_veranda_stairs_eaves_prompt.txt`
- Prompt JSON: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V002_uploadsafe.json`
- Manifest CSV: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V002_uploadsafe.csv`
- Shot record JSON: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V002_uploadsafe.json`

## Active References

Exactly three active visual references are specified:

1. Fenshou identity:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
2. Shuangji identity:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
3. Temple scene/world:
   `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`

Original PNG locked refs were not used as active visual refs.

SHOT-03 V001 MP4/contact sheet/review frames were not used as active visual refs.

Prior SHOT-02 / V013 / V014-R02 / V015 / V016 / V017 / V018 MP4s, contact sheets, and review frames were not used as active visual refs.

The upload-safe JPG files were not staged.

## Prompt Design Summary

### Beat 01 - Exterior Veranda / Column Corridor Edge Start

Time range: `0.00s-1.40s`

Purpose:

- Begin outside or semi-outside, not deep inside the hall.
- Make courtyard, rain, exterior corridor edge, column line, eaves, and railing readable.
- Continue from SHOT-02 courtyard combat.
- Let columns and railing shape movement.
- Keep contact hard, brief, clear, and rebounding.

### Beat 02 - Wet Stone Stair Height-Difference Combat

Time range: `1.40s-3.30s`

Purpose:

- Move naturally onto wet stone steps.
- Keep step edges and height difference readable.
- Show traction, foot skid, slip recovery, pivot, and forced sidestep.
- Let one fighter nearly lose footing, then recover and counter.
- Allow local railing or wood panel cracking from body contact.

### Beat 03 - Eaves / Roof-Edge Endpoint With Controlled Local Damage

Time range: `3.30s-5.00s`

Purpose:

- Reach eaves or roof-edge area.
- Show roofline, tiles, wooden eaves, railing, door/window lattice, lantern, or banner as clear anchors.
- Allow a few tiles to slide or scatter, eaves wood to splinter, or a lantern/banner to get knocked aside.
- End by implying SHOT-04 structural escalation, but do not perform it.
- Avoid full temple collapse, full roof duel, and snow transition.

## Settings

- `task_type=multimodal2video`
- `model_version=seedance2.0_vip`
- `duration=5`
- `ratio=16:9`
- `video_resolution=720p`
- `submit_allowed=false`
- `query_allowed=false`
- `download_allowed=false`
- `final_master=false`
- `locked=false`
- `human_review_required=true`

## Validation

- Prompt file exists: passed.
- Prompt JSON parses: passed.
- Shot record JSON parses: passed.
- Manifest CSV reads: passed.
- All active references exist: passed.
- Prompt JSON records `task_type=multimodal2video`, `model_version=seedance2.0_vip`, `duration=5`, `ratio=16:9`, and `video_resolution=720p`.
- Shot record keeps `status=package_ready_no_submit`, `final_master=false`, and `locked=false`.
- No media staged: to be confirmed immediately before commit.
- Upload-safe JPGs not staged: to be confirmed immediately before commit.
- `.vs/` not staged: to be confirmed immediately before commit.

## Next Step

Recommended next phase:

`PHASE_K105_SHOT03_V002_PACKAGE_REVIEW`

K105 should review the package before any live work.

Do not submit unless the human explicitly authorizes a later live submit phase.

## Safety Confirmation

- No Dreamina command was run.
- `dreamina version` was not run.
- `dreamina user_credit` was not run.
- No submit/query/download happened.
- No retry/resubmit/batch happened.
- No AI media was generated.
- No media files were created, edited, moved, deleted, or staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- Project Source files were not modified.
- SHOT-02 / V013 / V018 lock states were not altered.

## Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K103_SHOT03_V001_HUMAN_REVIEW_AND_V002_DIRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K102_SHOT03_V001_QUERY_DOWNLOAD_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K100_SHOT03_V001_PACKAGE_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K99_SHOT03_V001_UPLOADSAFE_ROUTE_AB_HYBRID_PACKAGE_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K98_SHOT03_ROUTE_AB_HYBRID_PACKAGE_DESIGN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/plans/SHOT-03_route_AB_hybrid_package_design.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/assets/asset_registry.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/`

## Final Verdict

SHOT03_V002_UPLOADSAFE_CONTINUITY_FIX_PACKAGE_READY_NO_SUBMIT
