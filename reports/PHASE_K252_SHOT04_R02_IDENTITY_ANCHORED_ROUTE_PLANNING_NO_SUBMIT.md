# PHASE K252 - SHOT-04 R02 Identity-Anchored Route Planning No Submit

## 1. Purpose

Plan the next SHOT-04 R02 near-wall guard-clash route after K251R corrected the K245/K250 output from limited motion evidence to identity-blocked and not primary.

K252 is report-only route planning. It inventories existing local identity, scene, and motion-evidence files and recommends the safest no-submit K253 package direction. It does not run Dreamina, create prompts, create packages, create manifests, create media, cut video, extract frames, submit, query, download, retry, resubmit, mark final, or lock.

## 2. ChatGPT Module Recommendation

- Current ChatGPT module for reviewing this K252 Codex result: ChatGPT Think
- Recommended K253 package/report review module: ChatGPT Think
- Recommended future visual review module after new media exists: ChatGPT Pro
- Pro Extended needed now: false
- Reason: K252 is local route planning and report validation only. Visual judgment comes after media exists. Source synthesis or macro-pipeline redesign is not currently active.

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
- No prompt txt file was created or modified.
- No package JSON file was created or modified.
- No manifest CSV file was created or modified.
- No `sources/` file was created, modified, staged, committed, or pushed.
- No shot record was modified.
- No runtime/config/auth/session/token/key/env file was modified or printed.
- Existing media, K250 cuts, review artifacts, asset files, `sources/`, `.vs/`, and `reports/context_recovery/` were not staged.
- `final_master=false`.
- `locked=false`.
- No visual success, final approval, or production approval is claimed.

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

K252 was not blocked by dirty sources.

## 5. K251R Lineage And Corrected Identity Status

Read:

- `reports/PHASE_K249_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_VISUAL_REVIEW.md`
- `reports/PHASE_K250_SHOT04_R02_NEAR_WALL_GUARD_CLASH_LOCAL_CUT_WINDOW_DIAGNOSTIC.md`
- `reports/PHASE_K251R_SHOT04_R02_IDENTITY_LOCK_CORRECTION_AND_ROUTE_DECISION.md`

Verified:

- submit_id: `37d02a39-7ca3-4141-b5ce-3e578622843e`
- K245 logid: `202606301414371692540470086459864`
- video sha256: `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418`
- K251R identity_lock: `failed_for_primary`
- K251R character_fixed: `false`
- K251R usable_as_SHOT04_R02_primary: `false`
- K251R usable_as_final: `false`
- K251R CUT_A/CUT_B status: diagnostic / motion evidence only unless later explicitly reviewed
- K251R recommended next route: K252 identity-anchored near-wall guard-clash route planning

Conclusion:

The K245/K247 video is useful as motion and failure evidence, but not as SHOT-04 R02 primary, final, locked media, or official edit candidate.

## 6. Source Conclusions

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

- Source governance remains human-controlled. Codex must not modify official `sources/`.
- Package/review success is not submit authorization; submit/query/download/retry/resubmit remain separate unless macro-authorized.
- Visual success is not final/lock; final/lock must be explicit human approval.
- SHOT-04 R02 failures should be evaluated through route reset, prompt priority, reference attention, identity drift, and visual execution categories.
- Result-first action syntax should put the visible action result before reference duties, audit language, and negative constraints.
- Identity references should be assigned narrow duties; identity refs should not be asked to solve composition, staging, or scene geometry.
- Action reference videos should be treated as action grammar and review evidence by default, not active generation input unless explicitly chosen.
- `dreamina_cli_help_latest.md` documents `multimodal2video` as the all-around reference / formerly ref2video mode, with repeated `--image`, `--video`, and `--audio` inputs; at least one image or video is required; Seedance 2.0 family models and 4-15 second duration are supported.

## 7. Asset Inventory Method

Read-only inventory searched existing local files under `productions/chi_yan_tian_qiong` with media extensions:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.mp4`
- `.mov`

Search terms included Fenshou/FenShou/black-red/male warrior/A-CH-A, Shuangji/ShuangJi/silver-blue/female warrior/A-CH-B, temple/corridor/side wall/wall panel/rain/wet/architecture/A-SC-TEMPLE/SHOT-04, and the known K247/K248/K250 motion evidence.

For relevant candidates, K252 records repo-relative path, type, byte size, sha256, inferred role, and risk notes. This is an inventory only; no file was opened for visual approval and no media was modified.

## 8. Fenshou Identity Reference Candidates

| Candidate | Type | Bytes | SHA-256 | Inferred role | Risk notes |
|---|---:|---:|---|---|---|
| `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png` | `.png` | `1959523` | `83e21fe549d737a4ac7fdbc23d9b883526f5aebc668bdb1e107a149244a13d2f` | primary Fenshou identity/body ref | Strongest Fenshou local locked ref found. Should carry identity/body only, not staging. |
| `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_fenshou_identity_upload_safe.jpg` | `.jpg` | `264243` | `5858915575eb0fef7dea1448aa149ee3543ec0af3581acbeab07d9bd0bb06743` | prior upload-safe Fenshou derivative | Useful if package needs smaller upload-safe refs, but it belongs to older wall-impact route and should be rechecked before reuse. |
| `productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg` | `.jpg` | `385741` | `70c01dec0bc3aa0eadd9f554c731be4991320b742cb2f9a2f1195a0d4f08bed3` | older upload-safe Fenshou derivative | Older SHOT-02 derivative; lower priority than locked ref and K253-specific derivative. |

Fenshou availability conclusion:

At least one plausible primary Fenshou identity ref exists. Identity asset repair is not required before a no-submit K253 package.

## 9. Shuangji Identity Reference Candidates

| Candidate | Type | Bytes | SHA-256 | Inferred role | Risk notes |
|---|---:|---:|---|---|---|
| `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png` | `.png` | `3874061` | `15339627a18d20c00ffbf1321696c175c451f00cff621e3e20d1162ec5890e11` | primary Shuangji identity anchor | Best identity lock candidate for Shuangji; may under-specify full-body combat silhouette if used alone. |
| `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png` | `.png` | `1752299` | `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a` | Shuangji full-body/body support | Useful support if K253 chooses 3 refs, but adding a second Shuangji ref increases reference attention conflict. |
| `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_identity_anchor_upload_safe.jpg` | `.jpg` | `386471` | `036760c0d8fd48a5d010328396c29d95392ec380a38039dd0a2ad4963aaf52b9` | prior upload-safe Shuangji identity derivative | Potential upload-safe derivative, but belongs to older wall-impact route. |
| `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_shuangji_full_body_upload_safe.jpg` | `.jpg` | `248965` | `db80fd001611f19762593cacbb8ba225a09a9d2db59a53ce355aa28cb8794086` | prior upload-safe Shuangji body derivative | Potential support ref only; lower priority than locked refs. |
| `productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg` | `.jpg` | `711550` | `fbc0e674e19d74c9ba4b8488e2c4da79f0a415e1c6811d0613803150bd9bad1d` | older upload-safe Shuangji derivative | Older SHOT-02 derivative; use only if K253 needs an upload-safe fallback. |

Shuangji availability conclusion:

At least one plausible primary Shuangji identity ref exists, with a full-body support ref available. Identity asset repair is not required before a no-submit K253 package.

## 10. Scene / Wall / Rain Reference Candidates

| Candidate | Type | Bytes | SHA-256 | Inferred role | Risk notes |
|---|---:|---:|---|---|---|
| `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png` | `.png` | `4147285` | `831c8743c019d37334b64a5843c7e595b909f75090de15ba55ff4730891af452` | locked temple stage / rain environment | General temple-stage ref, not side-wall specific. Could overpower identity/action. |
| `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png` | `.png` | `3563257` | `f5ff8003157bf6cfc86a3df9bd128cb094fa81e3a623bd74c25bfc6dde9bcbb0` | locked rainy temple environment | Broad courtyard environment; likely too general for near-wall combat. |
| `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png` | `.png` | `4196828` | `0a319ac0b8ebd060869d6dec0bebfe260a017df85b18c9500f1c1b5a5ecc1f5d` | side-wall panel scene candidate | Closest side-wall candidate found, but not in `locked_refs/` and needs review before becoming active. |
| `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_wall_panel_arch_ref_upload_safe.jpg` | `.jpg` | `413694` | `1fb81bb7dadf476b82dd675b7942ff22acf0f520433a838826b06a3307c836cc` | prior upload-safe wall architecture derivative | Comes from older wall-impact route; may reintroduce body-wall/contact attention. |

Scene availability conclusion:

Scene evidence exists, including a side-wall candidate, but K252 recommends excluding scene refs from the first K253 active ref set unless the package review explicitly shows that identity-only refs cannot preserve near-wall spatial logic.

## 11. Motion Evidence Only

| Evidence | Type | Bytes | SHA-256 | Inferred role | Active generation input? |
|---|---:|---:|---|---|---|
| `productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437/37d02a39-7ca3-4141-b5ce-3e578622843e_video_1.mp4` | `.mp4` | `11431647` | `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418` | K247 full motion/failure evidence | No, evidence only by default. |
| `productions/chi_yan_tian_qiong/edits/shot04_r02_near_wall_guard_clash_cut_candidates/K250/SHOT-04-R02-K250_CUT_A_0p10_0p65_near_wall_pressure_insert.mp4` | `.mp4` | `843385` | `583f5a667097b381bb97ff12a4abba106df6f80ab934fcb81d56697c65df50bf` | best diagnostic near-wall pressure micro-window | No, evidence only by default. |
| `productions/chi_yan_tian_qiong/edits/shot04_r02_near_wall_guard_clash_cut_candidates/K250/SHOT-04-R02-K250_CUT_B_4p25_5p00_tail_motion_diagnostic.mp4` | `.mp4` | `687657` | `072cc3028dc74fecf6e96f6368031bbed001560940af39feba2dece365487369` | secondary tail-motion diagnostic window | No, evidence only by default. |
| `productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_near_wall_guard_clash_text2video_K245_20260630_141437/review_artifacts/K248/contact_sheet_K248_SHOT04_R02_near_wall_guard_clash.jpg` | `.jpg` | `296375` | `95e76d85878d0f06b073a872a02d092de5a2648dc6f59f73724eebdf1f1925d8` | visual review/contact-sheet evidence | No, evidence only. |

Motion evidence conclusion:

K247/K250/K248 should guide timing, prompt wording, and future visual review rubrics, but should not be active Dreamina input by default. The existing K247 video has the wrong identity and could teach the model to preserve the bad identity if supplied as a video ref.

## 12. Option A - Identity-Anchored Multimodal2Video No-Submit Package

Assessment:

- Recommended as the next route, but only as K253 no-submit package preparation.
- Uses existing identity refs to directly address the K251R blocking failure.
- Better aligned with K245/K250 evidence than prompt-only text2video because it preserves the useful motion lesson while adding identity anchors.
- Stronger than retrying text2image keyframes because multiple still/keyframe routes already showed brittleness or remote failure.

Recommended Option A constraints:

- `task_type=multimodal2video`
- no live submit in K253
- model family to plan around: Seedance 2.0 family, likely `seedance2.0_vip`
- video duration target: 5 seconds unless K253 package review finds a reason to change
- video resolution target: 720p unless separately authorized
- ratio target: 16:9
- active refs count target: 2 identity refs first
- no active motion video ref by default
- no active scene ref by default on first identity-anchored package
- result-first action sentence must appear before reference duties
- reference duties must be narrow and explicit
- final_master=false
- locked=false

Main risks:

- Reference attention conflict if too many refs are active.
- Identity refs may stabilize characters but weaken action intensity.
- Multimodal mode may still drift toward posing unless the prompt is motion-first and front-loaded.
- K253 package should still undergo independent package review before any submit authorization.

## 13. Option B - Manual Layout / Keyframe Then Image2Video Or Frames2Video

Assessment:

- Not the default next route, but remains the strongest fallback if Option A package review shows identity/action conflict cannot be controlled.
- Manual layout could force left/right identity placement, guard crossing, near-wall geometry, and first-frame closeness.
- However, SHOT-04 R02 still/keyframe routes have shown text2image and dual-character combat brittleness, including remote final-generation failure and visual execution risk.

Use Option B if:

- K253 cannot define clean reference duties with 2 identity refs.
- Identity refs cannot preserve character separation.
- The route needs a human-approved composition/layout before animation.
- A future first-frame route has explicit human authorization.

## 14. Option C - Action-Reference-Library-First

Assessment:

- Useful as a supporting route, not the immediate default.
- Best for improving pressure, timing, wet-floor feedback, received-force, and avoiding static push/hold.
- Does not solve identity by itself.
- Source guidance treats action reference video as action grammar and review evidence by default, not active generation input.

Use Option C if:

- Option A produces identity stability but weak or static action.
- The next visual review needs a sharper rubric for guard compression, skid/recoil, wet-floor feedback, and edit-window usefulness.
- Human authorizes building or selecting reference videos before another generation package.

## 15. Recommended K253 Route

Recommended next phase:

`K253_SHOT04_R02_IDENTITY_ANCHORED_MULTIMODAL2VIDEO_NO_SUBMIT_PACKAGE`

K253 should create and validate a no-submit package only. It should not run Dreamina, submit, query, download, retry, resubmit, create media, mark final, or lock.

Recommended K253 package intent:

Create a result-first, identity-anchored, near-wall guard-clash `multimodal2video` package using two active character refs and no active scene/motion refs by default.

Recommended K253 package review checks:

- P0 visible action result is first.
- Fenshou and Shuangji identity duties are narrow.
- Prompt says identity refs control character identity/costume only.
- Prompt says the model must not copy pose, camera, scene, or composition from identity refs.
- Near-wall pressure is spatially stated without body-wall contact, wall hit, wall mark, wall damage, or wall collapse.
- Shuangji receives force through guard compression, weight shift, skid/recoil, and wet-floor feedback.
- First 1.0-1.5 seconds contain the main usable edit window.
- No final/lock language exists in the package.

## 16. Recommended Active Refs For K253

Recommended active refs, if K253 proceeds:

1. `productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png`
   - duty: Fenshou identity, red-black costume, body silhouette, male warrior identity
   - do not copy: source pose, source camera, source scene, standalone portrait framing

2. `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png`
   - duty: Shuangji identity, silver-blue styling, face/upper-body identity anchor, female warrior identity
   - do not copy: portrait composition, pose, camera, static expression, scene

Recommended active refs count:

- safest first count: `2`
- `3` refs allowed only if K253 package review determines Shuangji full-body support is required and the reference attention audit remains acceptable.

## 17. Excluded Refs For First K253 Package

Exclude by default:

- `productions/chi_yan_tian_qiong/locked_refs/A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png`
  - reason: useful body support, but a third character ref may split Shuangji attention or weaken action.

- `productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png`
  - reason: broad scene ref, not side-wall specific; may overpower the identity/action prompt.

- `productions/chi_yan_tian_qiong/runs/live/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_20260628_205403/a3e497d9-f914-4c09-a6b3-b296797b7fb4_image_1.png`
  - reason: closer side-wall candidate, but not locked and should be reviewed before active use.

- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02-wall-impact/upload_refs/shot04_r02_wall_panel_arch_ref_upload_safe.jpg`
  - reason: older wall-impact route derivative; may reintroduce forbidden wall-contact / wall-hit attention.

- K247 full video, K250 CUT_A, K250 CUT_B, and K248 contact sheet
  - reason: motion/failure evidence only; active video input could preserve the wrong identity from K245/K250.

## 18. Open Risks

- Identity refs may not be enough to preserve Shuangji full-body combat silhouette.
- Two-ref identity mode may weaken scene specificity and near-wall geometry.
- Adding a scene ref may improve wall logic but increase reference attention conflict.
- Adding motion video evidence may improve action but risks copying the identity-failed K245 output.
- Guard-clash dual-character close combat remains brittle.
- Wet-floor feedback and received-force reaction remain likely visual-failure points.
- Remote generation can still fail even if package review passes.
- Future submit/query/download must remain separately authorized.

## 19. K252H Help-Only Check Needed?

K252H help-only command-contract check is not required before K253 no-submit package creation.

Reason:

- `sources/dreamina_cli_help_latest.md` already documents `multimodal2video`, repeated `--image` inputs, optional `--video` inputs, Seedance 2.0 family support, duration range, and video resolution rules.
- K253 is no-submit package creation and does not need a live Dreamina help/canary command.

K252H or a live command-contract preflight should still be run before any later submit-authorized phase if the human authorizes live execution.

## 20. Final / Lock Status

- final_master: `false`
- locked: `false`
- visual_success_claimed: `false`
- final approval claimed: false

## 21. Stage / Commit Scope

K252 allowed stage scope:

- `reports/PHASE_K252_SHOT04_R02_IDENTITY_ANCHORED_ROUTE_PLANNING_NO_SUBMIT.md`

Do not stage:

- `.vs/`
- `reports/context_recovery/`
- `productions/chi_yan_tian_qiong/edits/`
- media files
- review artifacts
- asset files
- `sources/`
- prompt txt files
- package JSON files
- manifest CSV files
- shot records
- runtime/config/auth/session/token/key/env files

## 22. Final Verdict

`K252_ROUTE_PLANNING_READY_K253_IDENTITY_ANCHORED_NO_SUBMIT_PACKAGE`
