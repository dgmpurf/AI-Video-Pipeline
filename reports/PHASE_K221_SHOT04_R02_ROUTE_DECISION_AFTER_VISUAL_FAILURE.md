# PHASE K221 - SHOT-04 R02 Route Decision After Visual Failure

## 1. Purpose

Decide the next route for SHOT-04 R02 after K220B confirmed that the downloaded SHOT-04 R02 wall-impact video failed the core action.

K221 is a report-only route decision. It does not create a package, prompt, manifest, shot record update, media artifact, or Dreamina task.

## 2. Authorization And Boundaries

- Authorization level: L0 report-only route decision
- Dreamina: not run
- Submit/query/download: not run
- Retry/resubmit/batch: not run
- Media creation: none
- Frames/contact sheets: none created
- Prompt txt: not created or modified
- Package JSON: not created or modified
- Manifest CSV: not created or modified
- Shot records: not modified
- Runtime code: not modified
- `configs/providers.json`: not modified
- `sources/`: read-only only, not modified or staged
- Auth/session/token/key/env files: not opened, copied, printed, staged, or committed
- `final_master=false`
- `locked=false`

## 3. Files Inspected

### K201-K220B Reports

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K220A_SHOT04_R02_REVIEW_ARTIFACTS_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K219_SHOT04_R02_DOWNLOAD_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K218_SHOT04_R02_SUBMIT_STATUS_QUERY_RESULT_NO_DOWNLOAD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K217_SHOT04_R02_L3_DREAMINA_RESUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K216_SHOT04_R02_UPLOAD_SAFE_PACKAGE_SUBMIT_READINESS_REVIEW_NO_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K215_SHOT04_R02_UPLOAD_SAFE_REFERENCE_PACKAGING_NO_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K214_SHOT04_R02_SUBMIT_FAILURE_TRIAGE_UPLOAD_PATH_REMEDIATION_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K213_SHOT04_R02_L3_DREAMINA_SUBMIT_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K212_SHOT04_R02_PACKAGE_FILE_SUBMIT_READINESS_REVIEW_NO_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K211_SHOT04_R02_PACKAGE_PROMPT_FIX_NO_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K210_SHOT04_R02_PACKAGE_FILE_HUMAN_REVIEW_SUBMIT_READINESS_NO_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K209_SHOT04_R02_PACKAGE_FILE_DRAFT_NO_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K208_SHOT04_R02_TEXT_ONLY_ACTION_PACKAGE_DRAFT_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K207_SHOT04_R02_REFERENCE_SET_FREEZE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K206_SHOT04_R02_ACTION_COMPOSITION_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K205_SHOT04_R02_CONTACT_CHARACTER_REFERENCE_SELECTION_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K204_SHOT04_R02_WALL_IMPACT_PACKAGE_DRAFT_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K203_SHOT04_R02_WALL_IMPACT_REFERENCE_PLANNING.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K202_SHOT04_R02_WALL_PANEL_VISUAL_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K201_SHOT04_R02_WALL_PANEL_TEXT2IMAGE_DOWNLOAD_READY.md`

### Read-Only Source References

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.7.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化宏流程与授权等级_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/dreamina_cli_help_latest.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`

## 4. Source Governance Confirmation

Preflight confirmed `sources/` is clean.

Official Project Source files remain controlled only by the human user. Codex and local automation may read `sources/` as reference material and may create recommendations inside `reports/`, but must not create, edit, delete, rename, move, stage, commit, or push files under `sources/`.

K221 did not modify Source. Any Source update notes below are candidate evidence only, not official Source.

## 5. K220B Carry-Forward

- `visual_status=failed_core_action`
- `identity_status=partially_passed`
- `impact_status=failed`
- `received_force_status=failed`
- `wall_contact_causality_status=failed_or_weak`
- `reaction_speed_status=too_slow`
- `action_density_status=failed`
- `architecture_interaction_status=failed_as_primary_goal`
- `damage_causality_status=failed_or_decorative`
- `rebound_counter_status=failed_or_too_late`
- `tail_status=pose_out_or_static_showdown_tendency`
- `usable_as_final=false`
- `usable_as_locked=false`
- `usable_as_SHOT04_R02_primary=false`
- `usable_as_failure_evidence=true`
- `final_master=false`
- `locked=false`

Current state:

- K219 downloaded and validated the existing successful SHOT-04 R02 video.
- K220A created review frames and contact sheet.
- K220B recorded human + ChatGPT visual review failure.
- No final/lock state exists.
- No retry/resubmit is authorized.
- The current K219 video is failure evidence only.

## 6. Problem Diagnosis

The failed route attempted to use a full 5-second `multimodal2video` generation to produce a precise wall-impact choreography:

1. Fenshou drives a compact shoulder/forearm impact.
2. Shuangji's crossed guard absorbs force.
3. Shuangji's shoulder-back / upper back visibly slams into the wet wooden wall panel.
4. The wall shows a local, causally connected response at the exact contact point.
5. Shuangji immediately rebounds into a counter-ready state.

The actual video produced:

1. approach/setup;
2. weak guard contact / push;
3. Shuangji remaining upright near the wall;
4. wall feedback that reads delayed or decorative;
5. slow reaction and pose-out tail.

This confirms that the full 5-second prompt route is not reliably producing the required micro-impact. The model is spending the legal duration on setup, weak contact, and tail behavior instead of forcing the physically decisive hit into the edit-useful first second.

The issue is not that the Source chain was absent. K201-K220B evidence shows a valid process chain, but process validity did not translate into visible physical causality in the model output.

## 7. Route Comparison

| Route | Description | Recommendation | Reason |
|---|---|---|---|
| A. Direct retry / resubmit same package | Submit the same or nearly same full 5-second multimodal package again. | Reject | Repeats the same failure pattern, is not authorized, and does not structurally solve the missing contact frame. |
| B. Speed-up / edit existing K219 video | Apply speed change or trim to the failed downloaded video. | Reject as primary | Speed cannot fix missing impact causality, weak received force, delayed/decorative wall feedback, or absent rebound/counter. |
| C. Micro-impact keyframe route | First create or plan a contact-impact still/keyframe where the missing result is already visible. | Primary | Directly locks the hardest visual result: Fenshou pressure into crossed guard, Shuangji shoulder-back contacting wall, visible contact point, local wall response. |
| D. frames2video / multiframe route | Use multiple key states: close guard, impact into wall, rebound from wall. | Secondary after keyframes exist | More explicit state control, but requires strong keyframes and must respect CLI/task constraints. |
| E. 4-5s video with 0.8s-1.2s edit-window target | Submit a legal-duration video but force complete wall impact into first 0.35s-0.55s; treat later seconds as discardable handle. | Optional after contact keyframe / micro-impact prompt package | Better timing logic, but still risky if the decisive contact frame is not visually anchored first. |
| F. Stop wall-impact route and move to another SHOT-04 action | Abandon exact wall-impact if controllability remains too low. | Fallback only | Use only if exact body-wall impact remains non-negotiable and cannot be controlled after keyframe-first attempts. |

## 8. Route Decision

`route_decision=MICRO_IMPACT_CONTACT_KEYFRAME_FIRST_THEN_SHORT_EDIT_WINDOW`

Meaning:

- Stop full 5-second direct multimodal action retries.
- First create or package a contact-impact keyframe / still image.
- The keyframe must show the missing result directly:
  - Fenshou shoulder/forearm drive into Shuangji's crossed guard.
  - Shuangji shoulder-back or upper back already contacting the wet wooden wall panel.
  - Wall contact point visible.
  - Local shallow dent, short crack, rain burst, and two or three tiny splinters.
  - Wall remains intact.
  - No collapse.
  - No body-wall fusion.
- After keyframe review, consider short video, frames route, or edit-window route.

## 9. Recommended K222

K222 should be:

`K222 = SHOT-04 R02 micro-impact contact keyframe blueprint / no-submit package planning`

Authorization recommendation for K222:

- L0/L2 planning only unless separately authorized.
- No Dreamina.
- No submit/query/download.
- No final/lock.
- No Source modification.

K222 should produce:

- contact-impact keyframe blueprint;
- composition matrix;
- reference-duty map;
- prompt priority audit;
- visual result compliance checklist;
- negative constraint compression;
- risk register;
- recommendation on whether to assemble a no-submit package next.

## 10. Micro-Impact Timing Logic

Future SHOT-04 R02 wall impact should use micro-impact timing:

- Final edit target: `0.8s-1.2s`.
- Main impact must occur by `0.35s-0.55s`.
- No long approach.
- No 5-second single-hit storytelling.
- No pose-out tail.

Suggested timing if a later legal 4-5 second video is required:

- `0.00s-0.08s`: already close; Fenshou shoulder line entering; Shuangji crossed guard already raised.
- `0.08s-0.22s`: Fenshou short explosive shoulder-check / forearm drive hits crossed guard.
- `0.22s-0.40s`: Shuangji shoulder-back or upper back slams into wet wooden wall panel; foot skids on wet stone.
- `0.40s-0.55s`: very short hit-stop; only local shallow dent, short crack, rain burst, and two or three splinters at the exact contact point.
- `0.55s-0.85s`: Shuangji rebounds from wall and raises guard / starts counter.
- `0.85s-1.20s`: Fenshou re-enters or guards; cut here.
- later seconds: discardable continuation handle only.

## 11. Direct Wording Principle

Future package/prompt planning should lead with the dominant visual result, not with references or general atmosphere.

Recommended dominant result sentence:

> Fenshou lands one short explosive shoulder-check into Shuangji's crossed guard and drives her shoulder-back into the wet wooden wall panel within the first 0.35 seconds.

Required physical consequence wording:

> Her upper back hits the panel hard; the wall panel makes only a shallow local dent and short crack at the exact contact point; rainwater bursts outward and two or three tiny splinters fly in the force direction; Shuangji is not embedded in the wall; the wall does not collapse; she immediately rebounds and raises guard for counter.

This should be treated as the P0 visual result. Identity, camera, environment, and negative constraints support this result; they should not bury it.

## 12. Source Update Candidate Notes

Do not modify Source in K221.

Candidate future Source notes for ChatGPT/human Source governance:

- For one-hit wall-impact, the final edit target should be treated as a micro-impact shot around `0.8s-1.2s`.
- When CLI or model mode only allows 4-5 seconds, the prompt must front-load the impact into the first `0.35s-0.55s`.
- Full 5-second direct multimodal action prompt is high risk for precise body-wall impact unless supported by a contact keyframe.
- Speed-up cannot repair missing impact causality.
- Source compliance is not enough unless visual result compliance confirms the intended result is readable in the output.
- High-risk architecture/body contact needs a keyframe-first or multiframe state-control route when the exact contact event is non-negotiable.

## 13. What Not To Do

- Do not retry the same package.
- Do not resubmit the same package.
- Do not use speed-up as the primary fix.
- Do not mark this video final.
- Do not lock this video.
- Do not update official Source in K221.
- Do not use the current K219 video as approved primary reference.
- Do not continue with another full 5-second prompt-only wall-impact attempt without a contact keyframe or explicit human acceptance of high risk.

## 14. Safety Confirmation

- Dreamina was not run.
- No submit/query/download happened.
- No retry/resubmit/batch happened.
- No media was created.
- No frames/contact sheets were created.
- No media was staged.
- No prompt/package/manifest/shot-record/runtime/config file was modified.
- No auth/session/token/key/env file was opened, copied, printed, staged, or committed.
- `sources/` was read-only and remained clean.
- `final_master=false`.
- `locked=false`.

## 15. Final Verdict

`SHOT04_R02_ROUTE_DECISION_MICRO_IMPACT_KEYFRAME_FIRST_READY_K222_BLUEPRINT_PLANNING`
