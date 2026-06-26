# PHASE K132 - SHOT-03 V006 Prompt Patch After ChatGPT Audit

## Purpose

Apply the ChatGPT-audited full revised manual prompt for SHOT-03 V006, focused on force-chain compliance, contact density, short-burst terrain trigger behavior, and avoidance of soft-force failure patterns.

This phase is prompt patch only. It does not create the V006 package JSON, manifest CSV, or shot record JSON. It does not run Dreamina and does not submit, query, download, retry, resubmit, or generate media.

## Files Inspected

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K130_SHOT03_V005_SOURCE_COMPLIANCE_AND_V006_FORCE_CHAIN_AUDIT.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K131_SHOT03_V006_FORCE_CHAIN_PROMPT_DRAFT_READY_FOR_CHATGPT_AUDIT.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V006_uploadsafe_short_burst_column_trigger_force_chain_prompt.txt
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.5.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md

The Source files were read only. No Source file was modified, moved, deleted, or staged.

## What Previous Automation Got Wrong

- Source-read did not equal source-compliance: the earlier draft showed that the correct Source files were consulted, but some rules remained broad intent rather than executable prompt clauses.
- V1.2 and V1.11 rules were only partially translated: action density, contact consequence, rhythm, and impact-causality rules existed in concept, but not all were enforced as timing-specific hard constraints.
- The column-base foot point could still become a display subject: without stronger wording, the model could interpret the terrain affordance as a pose, jump, or parkour demonstration instead of a split-second force trigger.
- Hit-stop was not separated sharply enough from slow motion or pose-hold: the revised prompt now limits hit-stop to a 0.10s-0.15s perceptual impact accent.
- Anti-soft-force language was too weak: the prompt needed explicit bans on wind-up, obvious preparation, turn-based exchange, one-move-pause rhythm, planted static fighting, soft push-blocking, and long adjustment gaps.
- Contact consequences were under-specified: each contact beat must now produce visible physical results such as guard compression, shoulder-line displacement, torso offset, foot skid, recoil, or immediate re-entry.
- Terrain clarity was overprotected while impact brutality was underweighted: V006 now prioritizes burst close combat first, with the column/base terrain used only as a short trigger.

## Automation Lesson

Future prompt automation must perform clause-level Source compliance, not only Source lookup. For every relevant Source rule, the package-prep process should record:

- source rule
- prompt clause implementing it
- timing location in the prompt
- status: missing, weak, or present
- failure risk if omitted

Reading the Source is not enough. The rule must become a concrete prompt instruction with timing, body mechanics, visual evidence, and a failure-prevention clause.

## Revised V006 Prompt Changes

- Added first-priority framing: high-burst, continuous, hard-collision close pressure comes before terrain display.
- Converted the column-base foot point into a 0.10s-0.18s short-burst trigger, not an independent action or pose.
- Added explicit no wind-up / no obvious prep / no exaggerated charge rules.
- Defined hit-stop as only a 0.10s-0.15s impact accent, not slow motion, not pose-hold, not a dragged-out shot.
- Required no more than 0.20s-0.25s of pure adjustment or empty movement between contact beats.
- Required at least 6 clear contact beats in 5 seconds.
- Required every contact beat to include attack path, contact point, defensive reaction, body or foot result, rebound, and immediate re-entry.
- Required visible body consequences for each contact beat.
- Rewrote the force chain as one continuous body-power transfer: support foot and column-base trigger, knee compression, hip twist, shoulder drive, forearm hammer-line impact, guard compression, foot skid, then immediate re-entry.
- Added explicit bans on slow exchange, turn-based rhythm, planted static fighting, long hand-binding, soft push-blocking, floating, jumping display, and parkour display.
- Preserved no-structural-breakage rules: railing motion is only allowed when caused by real body, shoulder, or forearm pressure; no cracks, holes, broken railings, wood splinters, or self-damaging background structure.
- Strengthened face and identity stability rules for Fenshou and Shuangji, including mid-shot readable 3/4 faces and avoidance of prolonged occlusion.

## Files Updated

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V006_uploadsafe_short_burst_column_trigger_force_chain_prompt.txt
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K132_SHOT03_V006_PROMPT_PATCH_AFTER_CHATGPT_AUDIT.md

## Files Not Created

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_03_video_prompt_SHOT-03-V006_uploadsafe.json
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-03-V006_uploadsafe.csv
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_03_video_record_SHOT-03-V006_uploadsafe.json

## Safety

- Dreamina was not run.
- No submit, query_result, download, retry, resubmit, or batch command was run.
- No media was generated.
- No package JSON, manifest CSV, or shot record JSON was created.
- No Source file was modified.
- Runtime code was not modified.
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/configs/providers.json was not modified.
- final_master was not set.
- locked was not set.

## Next Step

Prepare the SHOT-03 V006 no-submit package in a later phase only after this patched manual prompt is accepted as the prompt basis.

## Final Verdict

SHOT03_V006_PROMPT_PATCHED_AFTER_CHATGPT_AUDIT_READY_FOR_PACKAGE_NO_SUBMIT
