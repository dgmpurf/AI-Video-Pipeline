# PHASE K208 - SHOT-04 R02 Text-Only Action Package Draft Planning

## 1. Purpose

K208 converts the frozen K207 reference set and the K206 action grammar into a text-only future package draft plan.

This report is not a package. It does not create prompt files, package JSON, manifest CSV, media, reference derivatives, contact sheets, review frames, or Dreamina tasks. It is a planning bridge so that a later K209 package-file draft can be created with clear reference duties and a result-first action structure.

K208 planning goal:

- choose the first-package reference strategy
- describe the future wall-impact package concept
- draft a result-first prompt skeleton for later review
- define negative constraints and anti-failure rules
- define what K209 may create if separately authorized

## 2. Inputs Inspected

Reports inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K202_SHOT04_R02_WALL_PANEL_VISUAL_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K203_SHOT04_R02_WALL_IMPACT_REFERENCE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K204_SHOT04_R02_WALL_IMPACT_PACKAGE_DRAFT_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K205_SHOT04_R02_CONTACT_CHARACTER_REFERENCE_SELECTION_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K206_SHOT04_R02_ACTION_COMPOSITION_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K207_SHOT04_R02_REFERENCE_SET_FREEZE_PLANNING.md`

Registry / metadata inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/assets/asset_registry.json`

Key carry-forward:

- K202 approved `A-SC-TEMPLE-SIDE-WALL-PANEL-002` as architecture reference only.
- K206 selected the R02 wall-impact action grammar.
- K207 froze required references and identified the 4-reference strategy as preferred if budget supports it.

## 3. Frozen Reference Set Carried Forward

### 3.1 Architecture Reference

- logical_id: `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- status: required
- duty: rainy temple side-wall / wet wooden wall panel / pillars / eaves / wet stone floor / cold rain atmosphere
- forbidden duties:
  - not character identity
  - not action composition
  - not damage pattern
  - not final frame
  - not locked frame

### 3.2 Fenshou Identity Reference

- logical_id: `A-CH-A-SUBJECT-001`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- status: required
- duty: Fenshou identity only
- forbidden duties:
  - not wall architecture
  - not action timing
  - not impact center
  - not damage pattern
  - not camera layout

### 3.3 Shuangji Face / Upper-Body Identity Anchor

- logical_id: `A-CH-B-IDENTITY-002`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`
- status: required
- duty: Shuangji face / upper-body identity stability only
- forbidden duties:
  - not full action pose
  - not wall architecture
  - not wall impact
  - not damage pattern
  - not camera layout

### 3.4 Shuangji Full-Body Identity Reference

- logical_id: `A-CH-B-SUBJECT-001`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- status: recommended fourth reference if budget supports it
- duty: Shuangji full-body costume / silhouette / body-frame identity support only
- forbidden duties:
  - not wall architecture
  - not action composition
  - not damage pattern
  - not camera layout

## 4. Future Package Reference Strategy

K208 chosen strategy:

`4-reference strategy preferred for the first package draft, with a 3-reference fallback if K209 discovers command/reference-budget constraints.`

Chosen first-package planning set:

1. `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
2. `A-CH-A-SUBJECT-001`
3. `A-CH-B-IDENTITY-002`
4. `A-CH-B-SUBJECT-001`

Reason:

SHOT-04 R02 is a two-character physical wall-impact shot. The action puts Shuangji under fast body compression, crossed-guard contact, shoulder/back wall impact, and immediate rebound. That is exactly the type of shot where prior project history suggests identity can drift. The 4-reference strategy gives Shuangji both face/upper-body identity stability and full-body costume/silhouette support while preserving the architecture target and Fenshou identity.

Risk control:

- K209 should still verify the future command contract and practical reference budget.
- If four references are judged too visually crowded or unsupported, fallback to the 3-reference set:
  - `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
  - `A-CH-A-SUBJECT-001`
  - `A-CH-B-IDENTITY-002`
- If 3-reference fallback is used, the prompt must explicitly describe Shuangji full-body costume and silhouette in text.

Not included in first package:

- action visual reference
- damage visual reference
- camera-layout visual reference

These remain text-controlled.

## 5. Text-Only Package Concept

Future package concept, prose only:

Create a rainy ancient temple side-corridor wall-impact combat beat. The environment is anchored by the K202-approved side-wall architecture reference: wet wooden wall panels, pillars, eaves, wet stone floor, and cold blue rain. Fenshou and Shuangji are the only two fighters in the shot.

Fenshou drives from the corridor side with one explosive shoulder-check and braced forearm pressure into Shuangji's crossed guard. Shuangji is already close to the wall; her guard compresses into her torso and her right shoulder / upper back hits one mid-height wet wooden wall panel between pillars. The contact point is visible and causal.

The wall response is local and controlled: the panel flexes or dents slightly at the exact contact point, with small wet cracks, tiny splinters, rain spray, and mist. The corridor remains intact. There is no wall collapse, no magic blast, no random hole, and no broad destruction.

Shuangji rebounds immediately from the wall impact into a counter-ready posture. The shot should end while the fight remains active, not as a static pose or final locked frame.

Identity preservation:

- Fenshou remains the black/red male fighter.
- Shuangji remains the female blue/silver fighter, protected by the identity anchor and full-body subject reference if included.
- No role swap, duplicates, extra characters, or identity drift.

No final/lock semantics:

- `final_master=false`
- `locked=false`
- human review required after any future generation

## 6. Result-First Prompt Skeleton

Draft skeleton only. This is not a production prompt and must not be saved as a prompt file in K208.

```text
[RESULT FIRST]
Fenshou lands one explosive shoulder-check into Shuangji's crossed guard, driving Shuangji's right shoulder and upper back into one mid-height wet wooden wall panel between pillars.

[ENVIRONMENT]
Rainy ancient temple side corridor, wet wooden wall panels, pillars, eaves, wet stone floor, cold blue rain light. Use the wall-panel architecture reference only for environment and wall target.

[CHARACTERS]
Fenshou is the black/red male fighter. Use the Fenshou reference only for identity.
Shuangji is the female blue/silver fighter. Use the Shuangji identity anchor for face and upper-body identity. If included, use the Shuangji full-body reference only for costume and silhouette.

[ACTION]
Fenshou drives from left-center / corridor side. His rear foot braces on wet stone, shoulder low, forearm braced into Shuangji's crossed guard.
Shuangji begins close to the wall. Her guard compresses into her torso; her right shoulder / upper back hits the wet wooden wall panel.

[WALL IMPACT]
Impact center is mid-height on one visible wall panel between pillars. The wall flexes or dents only at the contact point. Small wet cracks, tiny splinters, rain spray, and mist appear only after shoulder/back contact.

[REBOUND]
Shuangji immediately rebounds from the panel into counter-ready posture. Fenshou recovers from the shoulder-check. Both remain engaged; cut while combat is active.

[CAMERA]
Rainy side-corridor three-quarter perspective. Wall plane remains visible. Bodies do not hide the impact center. Wet floor and rain remain visible.

[NEGATIVE CONSTRAINTS]
No sustained pushing. No wrestling hold. No railing/lattice confusion. No full wall collapse. No random holes. No spontaneous debris. No magic blast. No generic courtyard drift. No interior hall drift. No roof route. No duplicate characters. No Shuangji masculinization. No empty architecture-only scene. No final frame language. No locked-frame language.
```

Skeleton priority:

1. wall-impact result
2. one explosive shoulder-check
3. crossed-guard compression
4. shoulder / upper-back contact with wall panel
5. localized causal wall response
6. immediate rebound
7. reference duties
8. negative constraints

## 7. Reference-Duty Prompt Notes

Future prompt should state reference duties explicitly:

- `A-SC-TEMPLE-SIDE-WALL-PANEL-002` controls only rainy temple side-wall, wet wooden wall panel, pillars, wet floor, eaves, and cold rain atmosphere.
- `A-CH-A-SUBJECT-001` controls only Fenshou identity, face, hair, armor, costume language, and black/red silhouette.
- `A-CH-B-IDENTITY-002` controls only Shuangji face / upper-body identity, female-coded identity stability, high ponytail, armor collar, and shoulder language.
- `A-CH-B-SUBJECT-001`, if included, controls only Shuangji full-body costume, robe silhouette, body frame, and blue/silver clothing language.
- Text action grammar controls movement, contact, impact, rebound, and timing.
- Text damage grammar controls local flex, cracks, tiny splinters, rain spray, and mist.

Prompt should not let:

- architecture reference erase the fighters
- character references change the scene
- identity references weaken the wall target
- action grammar override identity
- damage become larger than the body contact

## 8. Negative Constraints / Anti-Failure List

Future package prompt should explicitly prevent:

- sustained pushing
- wrestling hold
- slow static pressure
- body pin with no rebound
- railing/lattice confusion
- full wall collapse
- random hole
- spontaneous debris before contact
- magic blast replacing body contact
- energy shockwave as main event
- generic courtyard drift
- interior hall drift
- roof route
- wall run
- character identity drift
- Shuangji masculinization
- Fenshou/Shuangji role swap
- duplicate characters
- extra fighters
- empty architecture-only scene
- bodies hiding the wall impact center
- wall response appearing before visible shoulder/back contact
- body embedded inside wall
- body-wall fusion
- gore
- final-frame language
- locked-frame language

## 9. Package Artifact Plan for K209

If K209 is authorized, it may create package files only. It should remain no-submit.

Suggested package directory:

- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/`

Suggested future artifacts:

- package README:
  - `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/README.md`
- draft prompt file:
  - `productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt`
- package JSON:
  - `productions/chi_yan_tian_qiong/prompts/shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- manifest CSV:
  - `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit.csv`
- reference duty map:
  - `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/reference_duty_map.md`
- K209 report:
  - `reports/PHASE_K209_SHOT04_R02_PACKAGE_FILE_DRAFT_NO_SUBMIT.md`

Suggested package status fields:

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

No K209 live execution should occur unless separately authorized.

## 10. Upload-Safe Derivative Decision

K208 does not create derivatives.

K209 should check whether package-local upload-safe references are needed before future Dreamina submission.

Recommended K209 derivative policy:

- preserve locked originals as authoritative sources
- do not alter locked originals
- create or reference package-local upload-safe copies only if K209 is explicitly authorized to do so
- record any package-local derivative path and sha256 in the package metadata
- keep media unstaged unless a future task explicitly authorizes staging, which is not expected here
- verify reference count and command contract before any later live submit phase

K208 decision:

`upload_safe_derivatives_needed_for_future_package_check=true`

`upload_safe_derivatives_created_in_K208=false`

## 11. Package Readiness Assessment

K209 can create package files, still no submit, if separately authorized.

Ready:

- reference set selected
- preferred 4-reference strategy defined
- 3-reference fallback defined
- action grammar defined
- result-first skeleton drafted
- negative constraints defined
- K209 artifact plan defined

Still requiring K209 validation:

- exact command contract for the chosen task type
- final 4-ref vs 3-ref implementation based on contract/reference budget
- upload-safe reference availability or derivative plan
- JSON/CSV schema alignment
- prompt body review before any future submit
- no-submit metadata flags

Package readiness status:

`ready_for_K209_package_file_draft_no_submit`

## 12. Recommended K209 Path

Recommended next phase:

`K209 SHOT-04 R02 Package File Draft, still no submit`

Reason:

K208 stabilizes the text-only package plan enough for package files to be drafted. K209 should create the no-submit package artifacts, validate schema/contract assumptions, and preserve strict no-submit/no-query/no-download boundaries.

K209 must not submit to Dreamina unless a later phase gives explicit L3 human authorization.

## 13. Boundaries

K208 boundary confirmation:

- no Dreamina submit
- no Dreamina query
- no Dreamina download
- no retry
- no resubmit
- no batch
- no media generation
- no contact sheet
- no review frames
- no media staging
- no package file creation
- no prompt file creation
- no manifest creation
- no existing prompt/package/manifest/shot-record modification
- no `sources/` modification
- no official Source update
- no runtime code modification
- no `configs/providers.json` modification
- no auth/session/token/key/env file opened, copied, printed, staged, or committed
- `final_master=false`
- `locked=false`

## 14. Final Verdict

SHOT04_R02_TEXT_ONLY_ACTION_PACKAGE_DRAFT_PLANNING_READY_K209_PACKAGE_FILE_DRAFT_NO_SUBMIT
