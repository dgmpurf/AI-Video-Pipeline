# PHASE K207 - SHOT-04 R02 Reference Set Freeze Planning

## 1. Purpose

K207 freezes the intended reference set and reference-duty map for future SHOT-04 R02 wall-impact package planning.

In this report, "freeze" means reference-set planning freeze only. It does not mean final frame lock, media lock, `final_master=true`, `locked=true`, or human final approval.

K207 does not create package files, prompt files, manifests, media, contact sheets, review frames, or Dreamina tasks.

## 2. Inputs Inspected

K202-K206 reports:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K202_SHOT04_R02_WALL_PANEL_VISUAL_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K203_SHOT04_R02_WALL_IMPACT_REFERENCE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K204_SHOT04_R02_WALL_IMPACT_PACKAGE_DRAFT_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K205_SHOT04_R02_CONTACT_CHARACTER_REFERENCE_SELECTION_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K206_SHOT04_R02_ACTION_COMPOSITION_PLANNING.md`

Reference registry / metadata inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/assets/asset_registry.json`

Reference paths checked locally:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`

Source governance check:

- `sources/` was checked through git status and remained clean.
- No `sources/` file was created, edited, deleted, renamed, moved, staged, committed, or pushed.

## 3. Carry-Forward Action Concept

K206 action grammar for future package planning:

`Fenshou explosive shoulder-check into Shuangji crossed guard -> Shuangji right shoulder / upper back hits mid-height wet wooden wall panel -> localized wet-wood flex/cracks/splinters/rain spray -> immediate rebound.`

This action grammar is the future package's text-controlled contact event. It should be treated as action composition, not as a separate visual reference.

Core readability target:

- Fenshou drives the action from left-center / corridor side.
- Shuangji is compressed or redirected toward the wall on right-center / wall side.
- The impact happens at one mid-height panel between pillars.
- The wall response is small, local, wet, and caused only by Shuangji shoulder / upper-back contact.
- The action must not become sustained pushing, wrestling, static body pinning, wall run, roof route, or broad destruction.

## 4. Candidate Reference Inventory

### 4.1 Architecture Reference

- logical_id: `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- source evidence: K201/K202/K203/K204/K205/K206 reports
- status for future package: required
- intended duty: architecture / environment / wall target reference
- risks: may over-control the frame into empty architecture if not balanced with character identity refs and action grammar
- usage limitations:
  - not a contact keyframe
  - not character identity
  - not action composition
  - not damage pattern
  - not final or locked

### 4.2 Fenshou Identity Reference

- logical_id: `A-CH-A-SUBJECT-001`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- source evidence: asset registry and K205 carry-forward from Fenshou locked asset reports
- registry status: `locked_after_human_review`, `review_status=approved`
- status for future package: required
- intended duty: Fenshou identity-only reference
- risks: may pull neutral full-body subject pose into action if over-weighted
- usage limitations:
  - not architecture
  - not impact center
  - not wall damage
  - not action timing

### 4.3 Shuangji Full-Body Identity Reference

- logical_id: `A-CH-B-SUBJECT-001`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- source evidence: asset registry and K205 carry-forward from Shuangji subject lock reports
- registry status: `locked_after_human_review`, `review_status=approved`
- status for future package: recommended if reference budget supports it
- intended duty: Shuangji full-body costume / silhouette / body-frame identity reference
- risks: increases reference count and may compete with the Shuangji face / upper-body anchor
- usage limitations:
  - not architecture
  - not action composition
  - not wall damage
  - not camera framing

### 4.4 Shuangji Face / Upper-Body Identity Anchor

- logical_id: `A-CH-B-IDENTITY-002`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`
- source evidence: asset registry
- registry status: `status=locked`, `review_status=approved`, `human_review_status=approved`, `locked=true`, `final_master=false`
- status for future package: required
- intended duty: highest-priority Shuangji face / upper-body identity anchor
- risks: may not fully protect lower-body costume / silhouette by itself
- usage limitations:
  - not action rhythm
  - not full-body pose
  - not architecture
  - not wall damage
  - not camera framing

### 4.5 Action-Composition Reference Slot

- logical_id: unresolved slot
- path: none selected
- source evidence: K206 decision
- status for future package: not included yet
- intended duty if later selected: motion layout / body-wall contact geometry only
- risks if included now: may import wrong identity, wrong architecture, failed Route A movement, or non-wall action
- usage limitations:
  - cannot override identity refs
  - cannot override wall architecture ref
  - cannot be failed Route A video without separate authorization

### 4.6 Damage-Pattern Reference Slot

- logical_id: unresolved slot
- path: none selected
- source evidence: K204/K205/K206 decision
- status for future package: not included yet
- intended duty if later selected: local wet-wood cracks / tiny splinters only
- risks if included now: may over-drive collapse, holes, debris blasts, or style drift
- usage limitations:
  - cannot imply full wall collapse
  - cannot create unexplained damage
  - cannot replace body-contact cause-effect

### 4.7 Camera-Layout Reference Slot

- logical_id: unresolved slot
- path: none selected
- source evidence: K206 camera/composition plan
- status for future package: not included yet
- intended duty if later selected: side-corridor framing only
- risks if included now: may compete with architecture reference or pull scene away from wall-panel target
- usage limitations:
  - cannot override architecture
  - cannot override character identity
  - cannot become a separate shot goal

## 5. Frozen Reference Set Recommendation

K207 freezes the following future package reference set recommendation.

Required:

1. `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
   - duty: architecture / environment / wall target
2. `A-CH-A-SUBJECT-001`
   - duty: Fenshou identity only
3. `A-CH-B-IDENTITY-002`
   - duty: Shuangji high-priority face / upper-body identity anchor

Recommended if reference budget supports it:

4. `A-CH-B-SUBJECT-001`
   - duty: Shuangji full-body costume / silhouette identity support

Not included yet:

- action-composition visual reference
- damage-pattern visual reference
- camera-layout visual reference

Reasoning:

The safest first future package should use the architecture reference for the wall target, Fenshou identity reference for Fenshou, and Shuangji identity anchor for the most fragile identity requirement. `A-CH-B-SUBJECT-001` is valuable and recommended if the future command contract and reference budget allow four references without confusing duties. Action, damage, and camera should remain text-controlled for the first package draft plan.

## 6. Reference-Duty Map

| Reference ID / Slot | Include Status | Primary Duty | Secondary Duty | Forbidden Duties | Priority Order | Package Risk If Omitted | Package Risk If Included |
|---|---|---|---|---|---:|---|---|
| `A-SC-TEMPLE-SIDE-WALL-PANEL-002` | required | rainy side-wall architecture / wall-panel target | wet floor, eaves, pillars, rain atmosphere | identity, action choreography, damage result, final/lock | 1 | wall target may drift back to generic courtyard or railing | may over-control empty architecture if not balanced |
| `A-CH-A-SUBJECT-001` | required | Fenshou identity | black/red armor, male silhouette, face/hair continuity | wall geometry, impact center, damage, camera | 2 | Fenshou identity may drift or role may weaken | neutral full-body pose may soften action if over-weighted |
| `A-CH-B-IDENTITY-002` | required | Shuangji face / upper-body identity | female-coded identity, hair, collar/shoulders | full action pose, wall geometry, damage, camera | 3 | Shuangji identity may drift male-coded or lose face stability | may not cover full-body silhouette alone |
| `A-CH-B-SUBJECT-001` | recommended if budget supports | Shuangji full-body identity | costume, robe silhouette, body frame | action, wall geometry, damage, camera | 4 | Shuangji lower-body/costume silhouette may drift | adds reference count and possible duty competition |
| action-composition slot | not included yet | none in first set | text grammar controls action | identity, architecture, damage style | text-only | if text is weak, action may soften | visual ref may import wrong identity/location |
| damage-pattern slot | not included yet | none in first set | text constrains local flex/cracks/splinters | collapse, random hole, magic blast | text-only | wall response may be subtle | may over-drive collapse/debris |
| camera-layout slot | not included yet | none in first set | text constrains side-corridor framing | identity, architecture replacement, action result | text-only | camera may drift | may fight architecture target ref |

## 7. Priority and Conflict Rules

Reference hierarchy:

1. `A-SC-TEMPLE-SIDE-WALL-PANEL-002` controls environment and wall geometry only.
2. `A-CH-A-SUBJECT-001` controls Fenshou identity only.
3. `A-CH-B-IDENTITY-002` controls Shuangji face / upper-body identity only.
4. `A-CH-B-SUBJECT-001`, if included, controls Shuangji full-body costume and silhouette only.
5. Text action grammar controls the contact event.
6. Text damage grammar controls local wall response.

Conflict rules:

- Architecture reference must not erase characters or turn the frame into an empty scene.
- Character references must not move the scene away from the rainy side-wall corridor.
- Character references must not redefine wall geometry, impact center, or damage.
- Text action grammar must not override identity or architecture.
- Damage remains text-constrained only for the first package draft plan.
- No visual action reference should override identity/environment.
- No damage response appears before visible body-wall contact.
- No final/lock semantics are created by this reference-set freeze.

## 8. Reference Budget Risk

### 3-Reference Set

Set:

1. `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
2. `A-CH-A-SUBJECT-001`
3. `A-CH-B-IDENTITY-002`

Pros:

- cleanest duty separation
- lower reference complexity
- strongest protection for wall target and Shuangji face identity
- easier for a first package draft plan

Cons:

- Shuangji full-body costume / lower-body silhouette may rely mostly on prompt text
- risk of losing robe/body continuity during a physical wall-impact action

### 4-Reference Set

Set:

1. `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
2. `A-CH-A-SUBJECT-001`
3. `A-CH-B-IDENTITY-002`
4. `A-CH-B-SUBJECT-001`

Pros:

- stronger Shuangji full-body costume and silhouette protection
- better defense against identity drift in a two-character combat shot
- more complete identity stack for a physical body-wall impact

Cons:

- higher reference count
- possible competition between Shuangji full-body and face/upper-body identity anchor
- greater chance that identity references weaken wall/action attention

K207 decision:

For first package planning, use the 3-reference set as the minimum required set and mark the 4-reference set as the preferred set if the command contract and upload/reference budget are comfortable. The future K208 text-only package draft plan should explicitly evaluate both and recommend one before package files are created.

## 9. Upload-Safe Derivative Decision

K207 does not create upload-safe derivatives.

Decision:

Future package creation should check or create package-local upload-safe derivatives before any live submit phase, but not in K207.

Recommended K208/K209 handling:

- verify whether upload-safe derivatives already exist for each included reference
- if missing, plan package-local derivatives in a separate authorized package phase
- do not alter locked originals
- do not stage media unless a later task explicitly authorizes media staging, which is not expected for this workflow
- preserve the original locked reference paths as authoritative source refs

K207 status:

`upload_safe_derivatives_needed_for_future_package_check=true`

`upload_safe_derivatives_created_in_K207=false`

## 10. Package Readiness Assessment

Ready for:

- `K208 SHOT-04 R02 Text-Only Action Package Draft Planning`

Not ready for:

- direct package file creation
- Dreamina submit
- Dreamina query/download
- final/lock decision

Reason:

The reference set and action grammar are stable enough to write a text-only package draft plan. One more planning phase should translate the frozen reference set and K206 action grammar into a package blueprint before actual package files are created.

Package readiness status:

`ready_for_text_only_package_draft_planning_not_ready_for_package_files`

## 11. Recommended K208 Path

Recommended next phase:

`K208 SHOT-04 R02 Text-Only Action Package Draft Planning`

Reason:

The reference set and action grammar should be written into a package draft plan before creating package files or submitting anything. K208 should remain text-only and define:

- proposed task type
- final 3-ref vs 4-ref choice
- exact reference-duty wording
- result-first action grammar
- no-submit package blueprint
- validation checklist for later package creation
- whether upload-safe derivatives are needed in K209

K207 does not recommend immediate package file creation.

## 12. Boundaries

K207 boundary confirmation:

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

## 13. Final Verdict

SHOT04_R02_REFERENCE_SET_FREEZE_PLANNING_READY_K208_TEXT_ONLY_PACKAGE_DRAFT_PLANNING
