# PHASE K253 - SHOT-04 R02 Identity-Anchored Multimodal2Video No-Submit Package

## 1. Purpose

Create a no-submit identity-anchored `multimodal2video` package for SHOT-04 R02 near-wall guard-clash.

K253 addresses the K251R identity-lock correction: the K245/K250 prompt-only text2video output had `active_refs_count=0`, failed identity for primary use, and remains motion/failure evidence only.

K253 created only:

- one prompt txt file
- one package JSON file
- one manifest CSV file
- this text report

K253 did not run Dreamina, submit, query, download, retry, resubmit, batch, generate media, cut video, extract frames, create contact sheets, mark final, or lock.

## 2. ChatGPT Module Recommendation

- Current ChatGPT module for reviewing this Codex K253 result: ChatGPT Think
- K252 route planning module: ChatGPT Think
- Recommended next module for K254 independent package review: ChatGPT Think
- Recommended future module for visual review after new generated media exists: ChatGPT Pro
- Pro Extended needed now: false
- Reason: K253 creates a no-submit package. It is not a live submit, visual review, Source synthesis, or macro-pipeline redesign.

## 3. Boundaries

- No Dreamina command was run.
- No submit was run.
- No query was run.
- No download was run.
- No retry or resubmit was run.
- No batch execution was run.
- No media was created.
- No video was cut.
- No frames were extracted.
- No contact sheets were created.
- No `sources/` files were modified.
- No shot records were modified.
- No runtime/config/auth/session/token/key/env files were modified or printed.
- No media files were staged.
- No asset/reference files were staged.
- No K250 cut candidates were staged.
- `final_master=false`.
- `locked=false`.
- `visual_success_claimed=false`.
- No final or approval is claimed.

## 4. Git / Source Preflight

Commands run:

```powershell
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
```

Result:

- branch status: `## main...origin/main`
- `sources/`: clean
- known allowed workspace noise present:
  - `.vs/`
  - `reports/context_recovery/`
  - `productions/chi_yan_tian_qiong/edits/`

K253 was not blocked by dirty sources.

## 5. K251R / K252 Lineage Verification

Read:

- `reports/PHASE_K251R_SHOT04_R02_IDENTITY_LOCK_CORRECTION_AND_ROUTE_DECISION.md`
- `reports/PHASE_K252_SHOT04_R02_IDENTITY_ANCHORED_ROUTE_PLANNING_NO_SUBMIT.md`
- `reports/PHASE_K249_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_VISUAL_REVIEW.md`
- `reports/PHASE_K250_SHOT04_R02_NEAR_WALL_GUARD_CLASH_LOCAL_CUT_WINDOW_DIAGNOSTIC.md`

Verified:

- submit_id: `37d02a39-7ca3-4141-b5ce-3e578622843e`
- K245 logid: `202606301414371692540470086459864`
- K247/K250 video sha256: `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418`
- K251R identity_lock: `failed_for_primary`
- K251R character_fixed: `false`
- K251R usable_as_SHOT04_R02_primary: `false`
- K251R final_master: `false`
- K251R locked: `false`
- K252 recommended next phase: `K253_SHOT04_R02_IDENTITY_ANCHORED_MULTIMODAL2VIDEO_NO_SUBMIT_PACKAGE`
- K252 recommended task_type: `multimodal2video`
- K252 recommended active refs count: `2`
- K252 excluded by default: Shuangji full-body support ref, scene/wall refs, K247 full video, K250 CUT_A, K250 CUT_B, and K248 contact sheet

## 6. Source Files Consulted

Read-only Source files consulted:

- `sources/AI视频制作_Source索引与使用优先级_V1.8.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`
- `sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `sources/dreamina_cli_help_latest.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`

Applicable conclusions:

- `multimodal2video` supports repeated `--image` inputs and the Seedance 2.0 family.
- K253 is L2 no-submit package creation only.
- Submit/query/download/retry/resubmit remain separate explicit authorizations.
- Package success is not visual success, final, or lock.
- Identity reference duties must stay narrow.
- Result-first action wording must come before reference duties.

## 7. Active Ref Verification Table

| Alias | Path | Expected SHA-256 | Actual SHA-256 | Status | Duty |
|---|---|---|---|---|---|
| `@FENSHOU_LOCKED_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | pass | Fenshou identity, red-black armor/costume, body silhouette, male warrior identity only |
| `@SHUANGJI_LOCKED_REF` | `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | pass | Shuangji identity, silver-blue styling, face/upper-body identity anchor, female warrior identity only |

Active ref status:

- active_refs_count: `2`
- active image refs: `2`
- active video refs: `0`
- active audio refs: `0`
- active scene refs: `0`

## 8. Excluded Refs And Reasons

- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
  - reason: useful body support, but a third character ref may split Shuangji attention or weaken action.
- `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png`
  - reason: broad scene ref may overpower identity/action and is not side-wall specific.
- `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
  - reason: side-wall candidate is not locked and should be reviewed before active use.
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_wall_panel_arch_ref_upload_safe.jpg`
  - reason: older wall-impact route derivative may reintroduce forbidden wall-contact or wall-hit attention.
- K247 full video
  - reason: motion/failure evidence has failed identity and must remain evidence-only by default.
- K250 CUT_A and CUT_B
  - reason: diagnostic motion evidence only, not active input.
- K248 contact sheet
  - reason: review evidence only, not generation input.

## 9. Prompt Path And SHA-256

Prompt path:

```text
productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-V-IDENTITY-ANCHORED-NEAR-WALL-GUARD-CLASH-M2V-001_multimodal2video_no_submit_prompt.txt
```

Prompt SHA-256:

```text
07ca71a2defb0c75dca234e3a1a7dfde99532a16f4998c472e8e08bec98b60be
```

Prompt word count: `234`

## 10. Package JSON Path And SHA-256

Package JSON path:

```text
productions/chi_yan_tian_qiong/packages/SHOT-04-R02-identity-anchored-near-wall-guard-clash/K253/SHOT-04-R02-V-IDENTITY-ANCHORED-NEAR-WALL-GUARD-CLASH-M2V-001_package.json
```

Package JSON SHA-256:

```text
735a1298873ea39774bba25efa81b510227519a92e64d559126e872b8041c598
```

## 11. Manifest CSV Path And SHA-256

Manifest CSV path:

```text
productions/chi_yan_tian_qiong/packages/SHOT-04-R02-identity-anchored-near-wall-guard-clash/K253/SHOT-04-R02-V-IDENTITY-ANCHORED-NEAR-WALL-GUARD-CLASH-M2V-001_manifest.csv
```

Manifest CSV SHA-256:

```text
fdf88381baeeff0f4deed91e68a6ee69e9e0ca2b9c6af6c23999bd7d8a0c9ee7
```

## 12. Prompt Text

```text
Fenshou and Shuangji are already in close-range combat in the first frame: Fenshou drives compact shoulder-and-forearm body-line pressure from center-left into Shuangji's crossed guard at center-right, forcing her guard to compress, her weight to shift, and her boots to skid slightly across the wet stone floor while rain spray reacts around them.

Use @FENSHOU_LOCKED_REF only to preserve Fenshou's identity: a red-black armored male warrior with a strong dark body silhouette. Do not copy the reference pose, camera, background, or standalone portrait framing. Use @SHUANGJI_LOCKED_REF only to preserve Shuangji's identity: a silver-blue armored female warrior with her established face and upper-body styling. Do not copy the reference portrait composition, pose, camera, static expression, or scene.

The scene is a rainy ancient temple side corridor, medium-wide side view, cinematic 16:9. A dark wet wooden corridor wall is close behind Shuangji on the right, creating pressure, but she must not touch the wall. No body-wall contact, no wall hit, no wall mark, no wall damage, no wall crack, no wall collapse, and no wall fusion.

The main usable motion must happen within the first 1.0 to 1.5 seconds: crossed guard compression, Fenshou's body weight pushing through shoulder and forearm alignment, Shuangji's defensive recoil or skid, rain and wet-floor feedback tied to the clash. No long approach, no distant setup, no weak hand-push, no magic blast, no shockwave, no static poster pose-out, no identity swapping, no character merging.
```

## 13. Command Draft No-Submit

Documentation only. This command was not executed.

```bash
dreamina multimodal2video \
  --prompt "$(cat productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-V-IDENTITY-ANCHORED-NEAR-WALL-GUARD-CLASH-M2V-001_multimodal2video_no_submit_prompt.txt)" \
  --image productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png \
  --image productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png \
  --duration 5 \
  --ratio 16:9 \
  --video_resolution 720p \
  --model_version seedance2.0_vip \
  --poll 0
```

## 14. Package Static Validation

Static validation result: pass.

- prompt file exists: true
- prompt sha256 computed: true
- package JSON exists: true
- package JSON parses: true
- manifest CSV exists: true
- manifest CSV reads: true
- manifest CSV rows: `1`
- active_refs_count: `2`
- active ref hashes match K252: true
- command draft uses exactly two repeated `--image` inputs: true
- command draft includes no `--video`: true
- command draft includes no `--audio`: true
- no scene ref is active: true
- no motion evidence video is active: true
- no submit/query/download/retry/resubmit was run: true
- final_master=false: true
- locked=false: true
- visual_success_claimed=false: true

## 15. Reference Attention Audit

Result: pass with open risks.

- Ref duties are narrow: pass.
- Identity refs are not asked to solve camera: pass.
- Identity refs are not asked to solve scene: pass.
- Identity refs are not asked to solve pose: pass.
- Identity refs are not asked to solve wall geometry: pass.
- Identity refs are not asked to solve action mechanics: pass.
- Scene is text-described, not ref-driven: pass.
- K247/K250 bad-identity motion evidence is excluded from active input: pass.
- Prompt puts action result before reference duties: pass.
- Open risk: identity references may weaken action intensity; K254 should review whether the prompt preserves enough shoulder/forearm/body-line pressure and received-force reaction.

## 16. Risk Register

- Identity refs may stabilize characters but weaken action intensity.
- Two refs may under-specify Shuangji full-body combat silhouette.
- Text-only scene description may drift away from right-side wall geometry.
- Adding a scene ref later could improve wall logic but increase reference attention conflict.
- Adding K247/K250 motion video later could improve timing but risks copying bad identity.
- Dual-character close combat remains brittle.
- Wet-floor feedback, received-force reaction, and useful first 1.0-1.5 second edit window remain key visual risks.
- Future submit/query/download must remain separately authorized.

## 17. Recommended Next Phase

Recommended next phase:

`K254 independent package review no-submit`

K254 should independently review prompt, package JSON, manifest CSV, command draft, active ref duties, and no-submit boundaries before any human decision about a later live submit phase.

## 18. Final Master Status

- final_master: `false`

## 19. Locked Status

- locked: `false`

## 20. Final Verdict

`K253_IDENTITY_ANCHORED_NO_SUBMIT_PACKAGE_CREATED_READY_K254_REVIEW`
