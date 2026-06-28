# PHASE K205 - SHOT-04 R02 Contact / Character Reference Selection Planning

## 1. Purpose

K205 defines the reference-selection plan for a future SHOT-04 R02 wall-impact / contact-keyframe package.

This phase does not create a package, prompt, manifest, shot-record update, media artifact, or Dreamina task. It only identifies which existing references are appropriate candidates, what each reference may control, and what remains unresolved before package assembly.

The planning goal is to prevent reference-duty conflict before any future wall-impact package is created:

- the architecture reference should control wall/corridor environment only
- character references should control identity only
- action-composition references should control body/contact geometry only
- damage-pattern references should be optional and tightly limited

## 2. Inputs Inspected

Reports:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K202_SHOT04_R02_WALL_PANEL_VISUAL_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K203_SHOT04_R02_WALL_IMPACT_REFERENCE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K204_SHOT04_R02_WALL_IMPACT_PACKAGE_DRAFT_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_G2_3_FENSHOU_LOCKED_ASSET_BASELINE_REPORT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_G2_2_CHARACTER_SUBJECT_ASSET_LOCK_REPORT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_G4_3_LOCK_SHUANGJI_SUBJECT_ASSET_REPORT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_G4_4_CORE_ASSET_BASELINE_REPORT.md`

Registry / metadata:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/assets/asset_registry.json`

Local reference existence checks:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`

Source governance check:

- `sources/` was checked as clean in git preflight.
- `sources/` was not modified, staged, committed, or pushed.

## 3. Current Fixed Architecture Reference

Architecture reference:

- logical_id: `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
- K202 verdict: `KEEP_AS_ARCHITECTURE_REFERENCE`
- metadata carried from K202/K204:
  - format: PNG
  - resolution: 2560x1440
  - sha256: `0a319ac0b8ebd060869d6dec0bebfe260a017df85b18c9500f1c1b5a5ecc1f5d`

Allowed duties:

- rainy temple side-wall architecture
- wooden wall-panel target
- pillars, eaves, wet stone floor, cold blue rain atmosphere
- wall-plane geometry for future impact staging
- environmental continuity for SHOT-04 R02 planning

Forbidden duties:

- not a contact keyframe
- not a combat output
- not character identity reference
- not action/composition reference
- not a damage-pattern reference
- not final
- not locked
- not a direct Dreamina submit input without a later authorized package phase

## 4. Character Reference Selection Needs

SHOT-04 R02 will need strong character identity protection if Fenshou and Shuangji are placed into a wall-impact scene. SHOT-02 and SHOT-03 history shows that identity drift can become more likely when the prompt asks for fast contact, environmental interaction, or physical compression. Character references should therefore be selected before package assembly, but kept duty-limited.

### Fenshou Candidate

Recommended Fenshou identity reference:

- logical_id: `A-CH-A-SUBJECT-001`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
- status evidence:
  - `status=locked_after_human_review`
  - `review_status=approved`
  - reports: `PHASE_G2_3_FENSHOU_LOCKED_ASSET_BASELINE_REPORT.md`, `PHASE_G2_2_CHARACTER_SUBJECT_ASSET_LOCK_REPORT.md`

Recommended role:

- Fenshou identity-only reference.

Allowed duties:

- black/red male character identity
- face structure
- hair and silhouette
- armor and costume language
- body proportion / full-body silhouette continuity

Forbidden duties:

- does not control wall architecture
- does not control action choreography
- does not define impact center
- does not define damage or debris
- does not imply final/locked SHOT-04 output

### Shuangji Full-Body Candidate

Recommended Shuangji full-body identity reference:

- logical_id: `A-CH-B-SUBJECT-001`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
- status evidence:
  - `status=locked_after_human_review`
  - `review_status=approved`
  - reports: `PHASE_G4_3_LOCK_SHUANGJI_SUBJECT_ASSET_REPORT.md`, `PHASE_G4_4_CORE_ASSET_BASELINE_REPORT.md`

Recommended role:

- Shuangji full-body / costume / silhouette identity reference.

Allowed duties:

- female character body frame
- silver-blue high ponytail
- blue/silver armor and robe silhouette
- full-body costume continuity
- broad character identity preservation

Forbidden duties:

- does not control wall architecture
- does not control action choreography
- does not define impact center
- does not define damage or debris
- does not override the Shuangji face/upper-body identity anchor if that anchor is included later

### Shuangji Face / Upper-Body Identity Anchor Candidate

Recommended high-priority Shuangji identity anchor:

- logical_id: `A-CH-B-IDENTITY-002`
- path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`
- registry evidence:
  - `status=locked`
  - `review_status=approved`
  - `human_review_status=approved`
  - `locked=true`
  - reference duty recorded as identity-only

Recommended role:

- highest-priority Shuangji face / upper-body identity anchor.

Allowed duties:

- Shuangji face structure
- feminine identity stability
- silver-blue high ponytail
- upper-body armor collar and shoulder language
- identity correction against male-coded drift

Forbidden duties:

- not full action pose control
- not scene architecture
- not wall impact
- not damage pattern
- not camera framing
- not final/locked SHOT-04 frame

K205 note:

Future package planning should decide whether to include both `A-CH-B-SUBJECT-001` and `A-CH-B-IDENTITY-002` or only the identity anchor plus a concise full-body wording constraint. Including both may improve identity protection, but it also increases reference complexity. This should be resolved before package creation.

## 5. Character Reference Duties

Character references may control:

- who each fighter is
- face structure and gender coding
- hair, armor, robe, silhouette, and costume language
- broad body proportion continuity
- role continuity if the future action plan explicitly assigns attacker/defender roles

Character references may not control:

- rainy side-wall architecture
- wall-panel material or corridor layout
- action timing
- contact direction
- impact center
- crack/splinter/debris shape
- camera placement
- final-master status
- locked status

Reference-duty priority recommendation:

1. Architecture reference controls environment and wall target.
2. Character identity references control Fenshou/Shuangji identity only.
3. Action-composition planning controls the contact event.
4. Optional damage reference controls only localized breakage texture after cause-effect is defined.

## 6. Contact / Action-Composition Reference Needs

K205 does not find a fixed action-composition reference ready for immediate package use.

Future SHOT-04 R02 still needs a clear contact/action plan before package creation:

- which fighter drives the wall impact
- which fighter receives or redirects the impact
- whether the wall contact is shoulder-to-wall, guard-to-wall, back/side-body-to-wall, or elbow/fist/knee into guard near the wall
- exact wall impact center
- camera side-corridor orientation
- character distance from the wall before contact
- how body momentum creates the wall response
- how rain, wet floor, and wall-panel material react to the impact

Potential action-composition source options for K206:

- text-only action-composition plan, safest if no clean local frame exists
- a still frame from existing SHOT-03 corridor combat if it provides useful body spacing, not identity
- a manually selected action reference from V004/V005/V006 only if it is duty-limited to motion layout
- a future keyframe plan if the wall-contact pose must be staged separately

Action-composition references must not:

- override Fenshou/Shuangji identity
- override the wall-panel architecture target
- introduce a different location
- imply uncontrolled structural collapse
- be treated as a final keyframe without human approval

## 7. Damage-Pattern Reference Needs

Damage-pattern reference is optional and should not be selected before contact geometry is stable.

Possible future damage duties:

- localized wet-wood cracks
- small splinters from the impact center
- slight panel flex
- rain spray and dust/mist around the contact point
- small debris direction consistent with body/guard impact

Damage-pattern references must not allow:

- entire wall collapse
- large hole without visible cause
- spontaneous cracks before body contact
- exploding wall or magical blast
- debris unrelated to the impact center
- style drift away from the rainy temple side-wall reference

K205 recommendation:

Do not include a damage-pattern reference in the next package until K206 has chosen one primary wall-contact action. Early damage references risk over-driving collapse or visual noise.

## 8. Proposed Future Reference Duty Map

| Reference Slot | Candidate / Status | Proposed Duty | Required For Package? | Forbidden Duties |
|---|---|---|---|---|
| architecture target | `A-SC-TEMPLE-SIDE-WALL-PANEL-002` at `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png` | rainy side-wall, wall panel, pillars, eaves, wet floor, cold rain atmosphere | yes | identity, action, damage, final/lock |
| Fenshou identity | `A-CH-A-SUBJECT-001` at `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | Fenshou identity, face, hair, armor, silhouette | yes if Fenshou appears | architecture, wall impact, damage, final/lock |
| Shuangji full-body identity | `A-CH-B-SUBJECT-001` at `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | Shuangji full-body identity, costume, silhouette | recommended if Shuangji appears | architecture, wall impact, damage, final/lock |
| Shuangji high-priority identity anchor | `A-CH-B-IDENTITY-002` at `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | Shuangji face / upper-body identity stability | recommended due prior identity drift | architecture, action, damage, final/lock |
| action-composition | unresolved | body/guard contact relation, wall impact direction, impact center | required before package assembly as text plan or ref | identity, architecture replacement, damage style |
| damage-pattern | unresolved / optional | localized cracks, splinters, rain spray only after contact | optional later | collapse, spontaneous breakage, magic blast |
| camera-layout | unresolved / optional | side-corridor framing if needed | optional | identity, damage, action outcome |

## 9. Recommended K206 Path

Recommended next phase:

`K206 = SHOT-04 R02 Action-Composition Planning`

Reason:

The core identity and architecture candidates are now found and duty-limited, but the wall-impact event itself is still unresolved. The safest next step is not package creation. K206 should first define one primary action-composition choice:

- attacker / defender roles
- contact body part
- impact direction
- wall impact center
- camera orientation
- allowed visible wall response
- whether a separate action-composition reference is needed

This avoids building a package with too many unresolved reference duties and prevents the damage pattern from taking over the scene before the physical cause-effect is clear.

Alternative path:

`K206 = SHOT-04 R02 Wall-Impact Package Reference Set Planning`

This is acceptable only if the human wants to freeze a reference list before action design. K205 recommends action-composition planning first because the key creative risk is not missing identity references; it is an unclear wall-impact event.

Not recommended yet:

`K206 = SHOT-04 R02 Package File Draft`

Package file creation should wait until action-composition is defined.

## 10. Boundaries

K205 boundary confirmation:

- no Dreamina submit
- no Dreamina query
- no Dreamina download
- no retry
- no resubmit
- no batch
- no package creation
- no prompt creation
- no manifest creation
- no shot-record modification
- no media generation
- no contact sheet
- no review frames
- no media staging
- no `sources/` modification
- no official Source update
- no runtime code modification
- no `configs/providers.json` modification
- no auth/session/token/key/env file opened, copied, printed, staged, or committed
- `final_master=false`
- `locked=false`

## 11. Final Verdict

SHOT04_R02_CONTACT_CHARACTER_REFERENCE_SELECTION_PLANNING_READY_K206_REFERENCE_SET_OR_ACTION_PLANNING
