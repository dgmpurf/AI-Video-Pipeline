# PHASE K141 - SHOT-03 Split-Shot Micro-Sequence Plan

Text-only planning phase for SHOT-03 after the K140 route decision.

No Dreamina command was run. No submit, query_result, download, retry, resubmit, media generation, review artifact generation, live package preparation, prompt package JSON, manifest CSV, or shot record JSON was created in this phase.

## 1. Purpose

Plan a SHOT-03 micro-sequence route that preserves the proven V004-style clean corridor combat baseline while avoiding another single 5-second prompt-only terrain-force-chain attempt.

The plan splits terrain affordance into smaller, editable units. Each unit has one physical job, one review gate, and a clear go/no-go condition before any future Dreamina execution.

## 2. Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K140_SHOT03_ROUTE_DECISION_RECORD.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K139_SHOT03_V004_V005_V006_COMPARATIVE_STRATEGY_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K138_SHOT03_V006_HUMAN_AND_CHATGPT_REVIEW_FAILED_FORCE_CHAIN_AND_TERRAIN_ANCHOR.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K121_SHOT03_V004_HUMAN_REVIEW_AND_V005_TERRAIN_AFFORDANCE_DIRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K128_SHOT03_V005_HUMAN_REVIEW_SOFT_FORCE_AND_SPEED_DIAGNOSTIC_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K130_SHOT03_V005_SOURCE_COMPLIANCE_AND_V006_FORCE_CHAIN_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V004_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V005_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V006_uploadsafe.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

## 3. Source Governance Confirmation

- `sources/` was read only.
- No official Source file was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- Current Source governance rule is active:
  - `source_read_allowed=true`
  - `source_recommendation_allowed=true`
  - `source_draft_allowed=true`
  - `source_write_allowed=false`
  - `source_stage_allowed=false`
  - `source_commit_allowed=false`
  - `official_source_update_requires_human_manual_action=true`
- Any future Source update should be generated/reviewed by ChatGPT and manually applied by the human user.

## 4. Route Decision Basis

K140 route decision:

- Primary route: **B. Split terrain assist into multiple shorter edited shots using V004-style clean corridor combat as the baseline.**
- Fallback route: **A + D. Preserve V004 as the SHOT-03 clean corridor baseline/fallback, and move heavier architectural interaction/building impact escalation to SHOT-04.**
- Stop pure prompt-only V007 for now.

Reasoning:

- V004 is stable enough to preserve as the clean corridor combat baseline.
- V005 made the terrain idea visible but softened force, speed, and contact density.
- V006 was clause-level source-compliant but still failed the terrain anchor and choreography. It is evidence that precise column-base force-chain choreography is unreliable as a single 5-second prompt-only generation target.
- SHOT-03 should now use split-shot design rather than another prompt-only V007.

## 5. Evidence Summary

### V004 Strengths

- Positive clean corridor combat candidate.
- Better rhythm, continuity, identity stability, and exterior corridor readability than V003.
- No wrong structural crack or unexplained building breakage.
- Usable as clean corridor combat baseline and terrain/world reference.
- Not final and not locked.

### V004 Limitation

- Still ordinary corridor close combat.
- Does not yet strongly use temple architecture, columns, railings, or wet floor as tactical fighting tools.
- Not a complete SHOT-03 terrain-affordance solution.

### V005 Failure

- Terrain-affordance idea was visible.
- Force felt soft.
- Punch and leg speed did not match real force generation.
- Terrain setup diluted contact density and power.
- Foot plant / rebound read closer to soft jump, pose, or slow exchange than compact explosive terrain-triggered impact.
- Speed diagnostics cannot repair a structurally weak force chain.

### V006 Failure

- V006 encoded real speed, quick attack/guard/counter, short hit-stop, dense contact beats, no full slow motion, and explicit force-chain language.
- Human and ChatGPT review both found the terrain/foot moment wrong.
- The column-base / foot-trigger anchor did not read as credible architecture.
- Overall choreography still read like ordinary guard-punch exchange rather than convincing martial force-chain motion.
- Conclusion: prompt-only terrain-triggered force-chain control is unreliable for this shot type.

## 6. Proposed Split-Shot Table

| micro_shot_id | narrative function | visual goal | action goal | target edit duration | generation source duration if later generated | likely task_type candidate | reference needs | V004 reuse | keyframe/pose/action ref needed | main risks | human review criteria | go/no-go gate before Dreamina |
|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| SHOT-03A / SPLIT-01 | Re-establish clean corridor combat after SHOT-02 impact sequence | Exterior veranda / column corridor stays readable; rain, railings, wet stone floor, and identity refs remain stable | Dense close hand exchange with clear contact beats and no terrain trick | 1.5-2.5s | 5s | `multimodal2video` or local edit from V004 if enough material exists | Fenshou identity, Shuangji identity, temple corridor scene, optional V004 frame/action continuity | High. V004 may be cut/reused as baseline if pacing works | Optional; not required if using V004 cut | Too ordinary; no new terrain affordance | Stable identity, readable corridor, 5-6 contact beats, no idle tail, no random breakage | Confirm whether existing V004 clip/cuts already satisfy the needed baseline beat before generating anything |
| SHOT-03B / SPLIT-02 | Insert one small terrain-affordance beat | A single column, railing support, or wet-floor obstacle appears as tactical geometry, not spectacle | One quick obstruction/contact/re-angle: forearm shoved around column edge, shoulder compressed into railing line, or foot skid around wet stone; no full force-chain display | 0.5-1.0s | 5s if generated, then cut short | Prefer `multimodal2video` only with a selected start frame/action ref; pure prompt-only discouraged | Identity refs, corridor scene ref, selected still from V004/V005/V006/V004-style frame, possible pose/action reference | Medium. V004 provides world continuity, but not terrain action itself | Yes. Needs keyframe/pose/action ref before submit; do not rely only on text | Repeats V005/V006 soft pose failure; terrain becomes display; character drift | Terrain reads as brief tactical obstacle; contact has body consequence; no jump, no floating, no structural breakage | Human approves exact terrain micro-goal and reference frame/pose before package |
| SHOT-03C / SPLIT-03 | Return immediately to close combat after terrain insert | Same corridor zone, bodies stay near columns/railing but architecture is background/pressure line | Impact/reaction continuation: guard compression, torso displacement, short foot skid, immediate re-entry | 1.0-2.0s | 5s | `multimodal2video`, or local edit if V004/V006 has usable clean contact | Identity refs, V004-style corridor, optional continuation frame from SPLIT-02 if generated | Medium-high as style baseline | Preferred if SPLIT-02 is generated; continuation frame helps avoid spatial jump | Contact becomes soft or too defensive; camera loses corridor axis | At least two clear contact beats, visible body result, no idle recovery tail | Only proceed if SPLIT-02 cut point is known or choose V004 fallback close-combat continuation |
| SHOT-03D / SPLIT-04 | Aim bodies toward SHOT-04 without breaking architecture yet | Fighters are pushed toward railing / side-hall / wooden lattice direction while rain and corridor remain stable | Controlled pressure line toward architectural target; no breakage, just threat and setup | 1.0-2.0s | 5s | `multimodal2video` or local edit from clean corridor candidate | Identity refs, temple corridor scene, optional side-hall/lattice/railing reference if available | Medium. V004 can supply corridor baseline; may need new framing for side-hall direction | Possibly yes if the transition target must be precise | Accidentally breaks structure too early; over-wide camera; stalls into stare-down | Clear body pressure toward architecture, but no cracks/holes/splinters; cut before impact | Human confirms SHOT-04 target type before generating transition |
| SHOT-03E / SPLIT-05 | Optional bridge / safety fallback | Clean rain corridor combat or brief recovery if edit needs breathing room | A short re-entry, block, or reposition with one contact, not a new terrain idea | 0.5-1.2s | 5s only if needed | Local edit first; `multimodal2video` only if gap remains | V004/V004-style source, identity refs if generated | High | Usually no, unless continuity gap is severe | Filler shot weakens pace | It must solve a real edit gap and not dilute action | Use only after rough assembly shows a missing bridge |

## 7. Recommended Primary Plan

Primary K142 direction:

1. Build a text-only SHOT-03 split-shot candidate map from existing V004/V005/V006 media and reports.
2. Identify whether V004 can supply SPLIT-01 and possibly SPLIT-03 through local cuts.
3. Select exactly one terrain-affordance micro-goal for SPLIT-02:
   - short column-edge obstruction,
   - railing-line shoulder/guard compression,
   - or wet-floor foot skid causing immediate body displacement.
4. Require a start frame, pose frame, or action reference before any future SPLIT-02 Dreamina package.
5. Keep SPLIT-04 as transition toward SHOT-04 architecture, without breakage.

Recommended immediate plan:

- Do not generate V007 as another 5-second pure-text column-base force-chain.
- Do a K142 planning/review phase that chooses one SPLIT-02 micro-goal and one reference strategy.
- If a package is later created, it should be a very narrow package for one micro-shot only, not the entire terrain-combat solution.

## 8. Fallback Plan

If the human chooses progress over more SHOT-03 terrain work:

- Preserve V004 as SHOT-03 clean corridor baseline/fallback.
- Assemble SHOT-03 from V004-style clean corridor combat and any usable close-combat local cuts.
- Move architectural escalation to SHOT-04.
- SHOT-04 can then split the larger architectural idea into separate shots:
  - SHOT-04A: controlled body impact into railing / door / lattice / wall panel.
  - SHOT-04B: rain, dust, smoke, or broken-opening concealment.
  - SHOT-04C: object return / counterattack from or through the damaged opening.

## 9. What Not To Do Next

- Do not create prompt-only SHOT-03 V007 as another full 5-second terrain force-chain attempt.
- Do not try to pack column-base trigger, parkour, guard compression, body displacement, railing pressure, and transition into one prompt.
- Do not introduce roof combat, full wall-run, full building destruction, or side-hall breakage inside SHOT-03.
- Do not make SHOT-03 carry SHOT-04's architectural impact burden.
- Do not update official `sources/` from Codex.
- Do not mark V004, V005, V006, or any future split-shot as final or locked without explicit human approval.

## 10. Recommended K142 Options

Option A: **K142 Existing Media Split Review**

- Inspect V004/V005/V006 MP4s and existing contact sheets.
- Propose local cut windows for SPLIT-01 / SPLIT-03 / SPLIT-04.
- No Dreamina.
- Best if the human wants to see how much SHOT-03 can be assembled without more generation.

Option B: **K142 SPLIT-02 Reference Selection**

- Choose a single terrain-affordance insert goal.
- Select or extract candidate start/reference frames from V004/V005/V006.
- Decide whether an external pose/action reference is needed.
- No live package unless separately authorized.

Option C: **K142 SHOT-04 Escalation Preplan**

- Leave SHOT-03 as clean corridor baseline.
- Plan SHOT-04A/B/C architecture-impact sequence as separate shots.
- No SHOT-04 prompt/package yet unless later requested.

Recommended next human decision:

- Choose Option A if the priority is edit progress.
- Choose Option B if the priority is one more controlled terrain-affordance attempt.
- Choose Option C if the priority is moving architectural destruction into a better-suited shot family.

## 11. Source Update Recommendation

A future Source V1.12 may be useful, but Codex should not write official Source.

Candidate Source theme for later ChatGPT/human update:

- Terrain-assisted combat should be split into micro-shots when prompt-only choreography fails.
- A terrain affordance must have one physical job per shot.
- Precise column-base / wall / railing force-chain requires a reference frame, pose, or action reference before live generation.
- Prompt-only clause compliance is not proof of generated choreography quality.
- Architectural destruction should be deferred into separate shots with explicit contact causality.

This K141 report is evidence only. It is not official Source.

## 12. Safety Confirmations

- No Dreamina command was run.
- No submit, query_result, download, retry, resubmit, or batch operation happened.
- No media was generated, edited, moved, deleted, or staged.
- No review artifacts were created.
- No V007 prompt was created.
- No SHOT-04 prompt was created.
- No package JSON was created.
- No manifest CSV was created.
- No shot record JSON was created or modified.
- No runtime code was modified.
- `configs/providers.json` was not modified.
- `sources/` was read only and untouched.
- `.vs/` was not staged.
- `final_master=false`.
- `locked=false`.

## 13. Final Verdict

SHOT03_SPLIT_SHOT_MICRO_SEQUENCE_PLAN_READY_HUMAN_K142_DECISION_REQUIRED
