# SHOT-04 R02 Reference Duty Map

Status: package_file_draft_no_submit

## Reference Duties

| Label | Asset ID | Path | SHA256 | Required | Duty | Prohibited Duty |
| --- | --- | --- | --- | --- | --- | --- |
| `WALL_PANEL_ARCHITECTURE_REF` | `A-SC-TEMPLE-SIDE-WALL-PANEL-002` | `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png` | `0a319ac0b8ebd060869d6dec0bebfe260a017df85b18c9500f1c1b5a5ecc1f5d` | yes | Architecture target reference only: rainy temple side-wall, wet wooden wall panels, pillars, eaves, wet stone floor, cold blue rain atmosphere, wall-plane geometry. | Not a contact keyframe, not combat action, not identity reference, not final/locked frame. |
| `FENSHOU_IDENTITY_REF` | `A-CH-A-SUBJECT-001` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | yes | Fenshou identity only: face, armor, body language, costume silhouette. | Not wall geometry, not impact damage pattern. |
| `SHUANGJI_IDENTITY_ANCHOR_REF` | `A-CH-B-IDENTITY-002` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | yes | Shuangji highest-priority face and upper-body identity anchor: female-coded face, hair, expression, upper-body costume language. | Not wall geometry, not Fenshou identity, not action pose source. |
| `SHUANGJI_FULL_BODY_REF` | `A-CH-B-SUBJECT-001` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a` | yes | Shuangji full-body costume, silhouette, stance proportion, and lower-body continuity support. | Not wall geometry, not Fenshou identity, not damage pattern. |

## Use Rules

- The wall reference controls the environment only.
- Character references control identity only.
- The action is defined by the prompt, not by any single reference image.
- Localized wall damage may appear only where Shuangji makes causal body/guard contact with the wet wooden wall panel.
- No uncontrolled collapse, large building destruction, unexplained debris, or style drift is allowed.
- This map is not a submit authorization.
