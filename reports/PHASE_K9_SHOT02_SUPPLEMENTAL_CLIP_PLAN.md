# PHASE K9: SHOT-02 Supplemental Clip Plan

Date: 2026-06-19

## Scope

- Create a planning report for supplemental SHOT-02 clips around the approved shockwave highlight direction.
- Record package skeletons as planning-only entries inside this report.
- Do not create live Dreamina prompt, manifest, shot record, or readiness package files for V007/V008/V009 yet.
- Do not run Dreamina, submit, query, download, generate media, commit, lock, or mark any clip as final master.

## Current SHOT-02 Material Inventory

| Asset | Status | Role | Path / Notes |
| --- | --- | --- | --- |
| SHOT-02 locked keyframe | locked_official_keyframe | Official first-clash source image | `productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png` |
| SHOT-02-V001 | success_usable_candidate | Stable low-motion fallback clip | `productions/chi_yan_tian_qiong/runs/live/SHOT-02-V001_20260617_230616/SHOT-02-V001_stable_first_clash_motion.mp4`; 5.0167s, 1280x720; fallback_motion_clip=true |
| SHOT-02-V004 | human_review_usable_candidate | Strong partial success / usable rain pressure candidate | `productions\chi_yan_tian_qiong\runs\live\SHOT-02-V004_20260618_221001\SHOT-02-V004_rain_pressure_shell_camera_reaction_motion.mp4`; best segment approx 1.00s-2.30s |
| SHOT-02-V005 | human_review_partial_success_direction_validated | Direction reference only | `productions/chi_yan_tian_qiong/runs/live/SHOT-02-V005_20260619_133555/SHOT-02-V005_spherical_rain_shockwave_reveal_motion.mp4`; validated strong trigger wording, but shockwave scale too small |
| SHOT-02-V006 full clip | human_review_impact_edit_tests_ranked | Source clip only, not used directly | `productions/chi_yan_tian_qiong/runs/live/SHOT-02-V006_20260619_165923/SHOT-02-V006_giant_rain_shockwave_lens_pass_motion.mp4`; full_clip_usable=false |
| SHOT-02-V006 CUT01 | long_full_shockwave_backup | Longer large shockwave backup | `productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT01_2p00_to_4p00_giant_shockwave_extract.mp4` |
| SHOT-02-V006 CUT02 | tight_impact_extract_candidate | Fast impact extract candidate | `productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT02_2p00_to_3p50_tight_shockwave_extract.mp4` |
| SHOT-02-V006 CUT03 | preferred_full_shockwave_short_extract_candidate | Preferred short full-shockwave extract | `productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4`; approx 1.325s |
| SHOT-02 impact TEST_A | fast_impact_backup | Fast 0.35s keyframe hold + CUT03 backup edit | `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-impact-cut/SHOT-02_IMPACT_TEST_A_0p35s_hold_plus_CUT03.mp4` |
| SHOT-02 impact TEST_B | preferred_impact_edit_candidate | Preferred current impact edit test | `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-impact-cut/SHOT-02_IMPACT_TEST_B_0p50s_hold_plus_CUT03.mp4` |

Current decision:

- Preferred impact edit: TEST_B.
- Preferred full shockwave short extract: CUT03.
- V006 full clip is not used directly.
- Further Dreamina generation for the shockwave itself is not needed at the moment.
- No clip is locked as final master.

## Why The Material Pool Is Too Small

The current pool can sell the central shockwave beat, but it does not yet give the edit enough surrounding tissue. TEST_B solves the immediate contact-to-shockwave moment, yet SHOT-02 still lacks coverage before and after that impact.

Missing coverage:

- Pre-impact pressure build-up: the contact moment needs a short breath before the shockwave so the hit feels motivated rather than appearing suddenly.
- Post-impact rain/mist recovery: after the shockwave, the edit needs falling droplets, returning rain, mist, and wet floor reflections to land the consequence.
- Body/footwork reaction detail: the characters need a small physical response beat so the impact feels connected to bodies, not only to water effects.
- Transition into next combat beat: the sequence needs a handoff option, either a pressure reset or a directional movement cue.

## Recommended Edit Structure

| Segment | Target Duration | Current / Planned Source | Purpose |
| --- | ---: | --- | --- |
| Short contact / hit-stop beat | 0.3s-0.6s | TEST_B currently uses 0.50s hold | Establish one readable contact point before the shockwave reveal. |
| Shockwave reveal | approx 1.3s | CUT03 / TEST_B | Use the preferred large shockwave reveal without the slow V006 tail. |
| Aftershock / rain recovery | 0.8s-1.5s | Planned SHOT-02-V008 | Let rain, mist, puddles, and robes settle so the impact has aftermath. |
| Body / footwork reaction | 0.6s-1.2s | Planned SHOT-02-V009 | Show weight transfer, planted feet, shoulder recoil, and wet stone contact. |
| Transition | 0.5s-1.5s | Planned later or extracted from V008/V009 | Prepare the next combat beat without starting an unplanned combo. |

Recommended rough edit order:

```text
0.50s locked contact hold
-> CUT03 shockwave reveal
-> short rain/mist recovery beat
-> body or footwork reaction insert
-> optional transition cue into next combat beat
```

## CLI Contract Reminder

Current local Dreamina CLI contract for `image2video + seedance2.0_vip`:

- duration: 4-15 seconds.
- video_resolution: 720p or 1080p.
- ratio: omitted for image2video.
- input: exactly one `--image`.

Therefore all planned CLI packages below use duration=4 as the shortest legal image2video duration, then target only the strongest subrange in edit. Any 1-2 second final clip must be made by trimming the generated 4-second source or by a separate manual_web_run route that is explicitly documented later.

## Package Skeletons

These are planning skeletons only. No prompt txt, manifest csv, shot record json, readiness review, or live-submit package file has been created in this step.

### SHOT-02-V007_preimpact_pressure_charge

| Field | Planned Value |
| --- | --- |
| task_id | SHOT-02-V007 |
| package_name | SHOT-02-V007_preimpact_pressure_charge |
| status | planned_no_package |
| no_submit | true |
| final_master | false |
| locked | false |
| goal | Create a short pre-impact pressure charge before TEST_B / CUT03. The beat should make the contact feel loaded before the shockwave releases. |
| input source recommendation | Official locked keyframe: `productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png` |
| task_type recommendation | image2video |
| CLI duration recommendation | 4s, current CLI-legal minimum for seedance2.0_vip image2video |
| final edit target duration | 0.4s-0.8s |
| output role | Pre-impact build-up insert before TEST_B or before CUT03. |

Draft prompt direction:

- Use the locked keyframe as the only first frame and composition anchor.
- Keep Fenshou left, Shuangji right, one central arm/contact point, and the frontal rainy main-hall axis.
- No shockwave yet. Build pressure through subtle body tension, rain lines bending slightly around the contact area, suspended droplets, robe edges tightening, shallow puddles trembling, and a tiny held breath in the camera.
- Keep feet planted on wet stone; do not create a new strike, jump, weapon focus, or second exchange.

Risk notes:

- The model may trigger the shockwave too early.
- Pre-impact tension may become too static if the prompt is too soft.
- Any camera motion must remain tiny so it does not break the current contact framing.

### SHOT-02-V008_aftershock_rain_recovery

| Field | Planned Value |
| --- | --- |
| task_id | SHOT-02-V008 |
| package_name | SHOT-02-V008_aftershock_rain_recovery |
| status | planned_no_package |
| no_submit | true |
| final_master | false |
| locked | false |
| goal | Create a post-shockwave recovery beat: rain falls back, mist clears, puddles settle, and the temple space breathes after the impact. |
| input source recommendation | Preferred: a later approved still from CUT03 / TEST_B ending if extracted later. Fallback: official locked keyframe if no post-impact still is approved. |
| task_type recommendation | image2video from an approved still; multimodal2video only if a video reference is intentionally introduced later. |
| CLI duration recommendation | 4s for image2video seedance2.0_vip; 4-15s if multimodal2video is used later. |
| final edit target duration | 0.8s-1.5s |
| output role | Aftershock / rain recovery insert after TEST_B. |

Draft prompt direction:

- Start from a post-impact or contact-preserving frame in the same rainy temple space.
- Rain droplets and mist return from the shockwave edge, falling back into puddles and wet stone reflections.
- The circular rain curtain dissolves into normal heavy rain; the main hall remains legible.
- Characters stay readable and separated; no new attack and no additional shockwave.
- Keep the beat grounded in physical rain and wet stone, not magical energy.

Risk notes:

- If sourced from the original locked keyframe, the clip may not match post-shockwave continuity.
- If sourced from CUT03, an extracted still must be human-approved before it becomes an input.
- The recovery beat can become too atmospheric and slow; final edit should trim aggressively.

### SHOT-02-V009_body_footwork_reaction

| Field | Planned Value |
| --- | --- |
| task_id | SHOT-02-V009 |
| package_name | SHOT-02-V009_body_footwork_reaction |
| status | planned_no_package |
| no_submit | true |
| final_master | false |
| locked | false |
| goal | Add a physical reaction detail beat showing weight, planted feet, knees, shoulders, wet stone contact, robe movement, and small recoil after the impact. |
| input source recommendation | Official locked keyframe first; optional later still from TEST_B / CUT03 if a clearer post-impact body pose is approved. |
| task_type recommendation | image2video |
| CLI duration recommendation | 4s, current CLI-legal minimum for seedance2.0_vip image2video |
| final edit target duration | 0.6s-1.2s |
| output role | Character-body consequence insert; supports the water spectacle with martial weight and foot contact. |

Draft prompt direction:

- Preserve the same two characters and rainy main-hall courtyard.
- Emphasize knees, boots, wet stone, robe hems, shoulder tension, and a small recoil or bracing action after the impact.
- Keep both bodies separated and readable; feet must stay connected to the wet stone floor.
- Do not create a new combo, spin, jump, chase, weapon focus, or scene change.
- Camera should be locked or make a very small grounded reaction, with the main hall axis still readable.

Risk notes:

- Footwork prompts can cause side-scrolling movement or new choreography.
- Close body detail can create extra limbs if action is over-described.
- Keep it as a reaction insert, not a second fight beat.

## Optional Transition Strategy

No separate transition package is recommended yet. First review whether V008 or V009 can provide a natural handoff.

Potential transition directions:

- Rain recovery ends with both characters still locked in pressure, preparing the next motion.
- Footwork reaction reveals one character shifting weight without starting a new strike.
- Camera settles back to the frontal main-hall axis before the next combat beat.

If a separate transition package becomes necessary later, create it as SHOT-02-V010 only after V007-V009 are reviewed.

## Recommended Next Actions

1. Keep TEST_B as the current preferred impact edit candidate.
2. Preserve CUT03 as the preferred full-shockwave short extract.
3. Prepare SHOT-02-V007 first if the next need is tension before impact.
4. Prepare SHOT-02-V008 first if the edit feels abrupt after the shockwave.
5. Prepare SHOT-02-V009 first if the current beat lacks martial body weight.
6. Do not create or submit any Dreamina live package until the user chooses the next clip.

## Validation Notes

- Locked keyframe path exists at report time: true.
- TEST_A path exists at report time: true.
- TEST_B path exists at report time: true.
- CUT03 path exists at report time: true.
- V001, V004, V005, and V006 source video paths exist at report time: true.
- This report is planning-only and does not create executable package files.

## Decision

SHOT_02_SUPPLEMENTAL_CLIP_PLAN_READY
