# PHASE K115 - SHOT-03 V004 Actual Prompt Draft Ready For ChatGPT Audit

## Purpose

This phase creates only the actual manual prompt draft for `SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage`.

This is not a package phase. No prompt JSON, manifest CSV, shot record JSON, package review report, Dreamina output, or media file was created in this phase.

## Sources Inspected

The following local project references were inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.5.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.10_视角纠偏与场景锚点重构增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K113_SHOT03_V003_HUMAN_REVIEW_AND_PROMPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K108_SHOT03_V002_HUMAN_REVIEW_AND_V003_DIRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K103_SHOT03_V001_HUMAN_REVIEW_AND_V002_DIRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V003_uploadsafe_simplified_exterior_column_corridor_prompt.txt`

The `sources/` directory was treated as read-only reference material. No source file was modified, staged, moved, deleted, or recreated.

## V003 Failure Being Fixed

`SHOT-03-V003` failed because simplifying the location was not enough. The actual prompt audit identified these issues:

- Setup-heavy opening.
- No mandatory first contact within `0.15s-0.30s`.
- No required contact-beat count.
- Generic actor language instead of explicit Fenshou / Shuangji causality.
- Wrong wood-crack causality.
- Idle tail in the final section.
- Weak impact and too much leg-only movement.

## V004 Prompt Design

The V004 draft uses one stable combat zone:

`rainy ancient temple exterior veranda / column corridor / railing / wet stone floor`

Core design choices:

- First contact is required within `0.15s-0.30s`.
- The 5-second clip contains at least 6 explicit contact beats.
- Each beat names attack path, contact point, defender reaction, rebound, and immediate continuation.
- Fenshou and Shuangji actions are actor-specific throughout.
- No structural breakage is allowed in V004.
- Environment feedback is limited to non-structural reactions: water splash, sleeve snap, hair whip, armor droplets, railing shake without cracking, column close-pass occlusion, and hanging cloth / lantern movement.
- The last `0.8s` continues fighting and cuts mid-exchange.
- Medium / medium-wide camera protects face stability while preserving readable combat contact.

## Why No Structural Damage

V003 produced a wrong wooden crack because the prompt allowed local architecture damage without a strict cause-effect chain.

V004 therefore prioritizes contact density and removes structural damage entirely. This reduces the risk of unexplained cracks, roof-tile breakage, or background structure damage.

If V004 succeeds in action density and identity stability, a later V005 can test one small causally bound breakage event as a separate design problem.

## ChatGPT Content Audit Checklist

Before any future V004 package or submit approval, ChatGPT should audit the prompt for:

- First contact timing: does it force contact inside `0.15s-0.30s`?
- Contact beat count: does it clearly define at least `5-6` contact beats?
- Final `0.8s` action: does the prompt keep fighting through the final frame?
- Actor-specific causality: are Fenshou and Shuangji named in each beat?
- Environment feedback safety: are all reactions non-structural or explicitly no-crack?
- Face / identity risk: does the camera avoid extreme face close-ups while keeping identities readable?
- Idle-tail risk: is there any wording that creates a pose-out, stare, or readable ending?
- Overlong negative risk: are negatives strong enough without overwhelming the positive action schedule?

## Files Created

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V004_uploadsafe_contact_density_no_structural_breakage_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K115_SHOT03_V004_ACTUAL_PROMPT_DRAFT_READY_FOR_CHATGPT_AUDIT.md`

## Safety

- Dreamina was not run.
- No submit was performed.
- No query_result was performed.
- No download was performed.
- No media was created, edited, moved, or staged.
- No `sources/` file was modified or staged.
- No package JSON was generated.
- No manifest CSV was generated.
- No shot record JSON was generated.
- `final_master` was not touched.
- `locked` was not touched.
- SHOT-02 / V013 / V018 lock states were not touched.

## Final Verdict

`SHOT03_V004_ACTUAL_PROMPT_DRAFT_READY_FOR_CHATGPT_AUDIT_NO_PACKAGE_NO_SUBMIT`
