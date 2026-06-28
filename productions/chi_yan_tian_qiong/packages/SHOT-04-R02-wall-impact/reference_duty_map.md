# SHOT-04 R02 Reference Duty Map

Status: upload_safe_refs_packaged_no_submit

## Reference Duties

| Label | Asset ID | Active Upload-Safe Path | Upload-Safe SHA256 | Original Source Path | Original SHA256 | Required | Duty | Prohibited Duty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `WALL_PANEL_ARCHITECTURE_REF` | `A-SC-TEMPLE-SIDE-WALL-PANEL-002` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_wall_panel_arch_ref_upload_safe.jpg` | `1fb81bb7dadf476b82dd675b7942ff22acf0f520433a838826b06a3307c836cc` | `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png` | `0a319ac0b8ebd060869d6dec0bebfe260a017df85b18c9500f1c1b5a5ecc1f5d` | yes | Architecture target reference only: rainy temple side-wall, wet wooden wall panels, pillars, eaves, wet stone floor, cold blue rain atmosphere, wall-plane geometry. | Not a contact keyframe, not combat action, not identity reference, not final/locked frame. |
| `FENSHOU_IDENTITY_REF` | `A-CH-A-SUBJECT-001` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_fenshou_identity_upload_safe.jpg` | `5858915575eb0fef7dea1448aa149ee3543ec0af3581acbeab07d9bd0bb06743` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | yes | Fenshou identity only: face, armor, body language, costume silhouette. | Not wall geometry, not impact damage pattern. |
| `SHUANGJI_IDENTITY_ANCHOR_REF` | `A-CH-B-IDENTITY-002` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_identity_anchor_upload_safe.jpg` | `036760c0d8fd48a5d010328396c29d95392ec380a38039dd0a2ad4963aaf52b9` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | yes | Shuangji highest-priority face and upper-body identity anchor: female-coded face, hair, expression, upper-body costume language. | Not wall geometry, not Fenshou identity, not action pose source. |
| `SHUANGJI_FULL_BODY_REF` | `A-CH-B-SUBJECT-001` | `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_full_body_upload_safe.jpg` | `db80fd001611f19762593cacbb8ba225a09a9d2db59a53ce355aa28cb8794086` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a` | yes | Shuangji full-body costume, silhouette, stance proportion, and lower-body continuity support. | Not wall geometry, not Fenshou identity, not damage pattern. |

## Use Rules

- The wall reference controls the environment only.
- Character references control identity only.
- The action is defined by the prompt, not by any single reference image.
- Localized wall damage may appear only where Shuangji makes causal body/guard contact with the wet wooden wall panel.
- No uncontrolled collapse, large building destruction, unexplained debris, or style drift is allowed.
- This map is not a submit authorization.
- Upload-safe refs are local submit-helper files only. Originals remain authoritative for lineage.
- Upload-safe refs are not final, not locked, and not media to stage or commit.
