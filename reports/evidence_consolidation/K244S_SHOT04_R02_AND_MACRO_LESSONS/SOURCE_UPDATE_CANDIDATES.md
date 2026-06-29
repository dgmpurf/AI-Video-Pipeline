# Source Update Candidates

## Purpose

Draft candidate official Source updates for ChatGPT Pro Extended to transform later. This file is not official Source. It is evidence-only preparation and does not authorize Codex to modify `sources/`, prompts, packages, manifests, media, runtime, config, auth, staging, commit, or push.

## Candidate 1 - Prompt Compiler and Result-First Action Syntax

- proposed Source file name: `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- proposed section title: `结果优先动作语法与P0视觉结果排序`
- evidence phases: K185/K190, K220B, K221, K242V, K243V, K244, K244S Part 2, K244S Part 3
- priority: high
- implementation impact: Prompt compiler should lead with the visible action result, front-load decisive motion, keep support clauses secondary, and avoid burying P0 under reference-duty/audit prose.
- draft rule text:

```text
For high-risk combat prompts, the first generation sentence must state the visible P0 action result. Identity, camera, environment, reference duty, and negative constraints support that result and must not precede or dilute it. If the prompt targets a legal 5s video but only needs a 1.0s-1.5s usable edit window, the prompt must say the action starts in the first frame and reaches the decisive contact/pressure beat inside the first 0.35s-0.65s.
```

## Candidate 2 - Failure Ledger and Root Cause Taxonomy

- proposed Source file name: `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- proposed section title: `失败台账字段与根因分类`
- evidence phases: K213/K214, K220B, K226/K226F, K230/K230F, K235/K235F, K241/K241F, K244S Parts 1-3
- priority: high
- implementation impact: Every macro-run should classify failure type before choosing the next route. Technical success, visual success, and final/lock approval must remain separate states.
- draft rule text:

```text
Every failed or partial generation route must be logged with a stable root cause class: package_defect, source_governance_block, preflight_block, command_contract_block, upload_transport_failure, remote_final_generation_failure, visual_execution_failure, prompt_priority_failure, reference_attention_conflict, dual_character_close_combat_staging_brittleness, body_wall_contact_brittleness, text2image_keyframe_brittleness, video_action_quality_failure, timing_tail_poseout_failure, identity_drift, route_reset_required, manual_layout_required, or alternate_action_required. A submit/query/download success is not visual success, and visual success is not final/lock approval.
```

## Candidate 3 - Route Reset Policy

- proposed Source file name: `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- proposed section title: `重复远端失败后的路线重置规则`
- evidence phases: K226F, K230F, K235F, K241F, K242V, K244S Part 1, K244S Part 3
- priority: high
- implementation impact: Prevents blind retries and forces structural route changes after repeated valid-submit failures.
- draft rule text:

```text
If remote final-generation failure repeats across two structurally distinct routes for the same shot goal, stop same-class retrying. Create a route reset report before any new package or submit. The reset must compare at least three options: simplify/soften the current route, switch task type, and use manual layout or alternate action. A same-package retry requires explicit human authorization and must be recorded as a new live attempt, not as an automatic continuation.
```

## Candidate 4 - Near-Wall Guard-Clash Fallback Pattern

- proposed Source file name: `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- proposed section title: `近墙格挡冲突作为身体撞墙失败后的替代动作`
- evidence phases: K235F, K236, K237A, K238, K238T/K241, K242V, K243V, K244
- priority: medium
- implementation impact: Gives the shot compiler a reusable fallback when exact body-wall contact is too brittle.
- draft rule text:

```text
When exact body-wall contact repeatedly fails or becomes too provider-fragile, consider a near-wall guard-clash fallback. Preserve the corridor pressure, crossed guard, wet-floor skid, rain spray, and counter-readiness, but remove body-wall contact, wall hit, wall mark, wall crack, splinter, dent, embedding, and wall damage as positive goals. Treat the wall as background danger unless a manual layout or external compositing route is explicitly chosen.
```

## Candidate 5 - Text2Image Brittleness for Dual-Character Combat

- proposed Source file name: `AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- proposed section title: `双人近身战斗静帧/Text2Image脆弱性`
- evidence phases: K232/K235, K238T/K241, K241F, K242V, K244S Parts 1-3
- priority: high
- implementation impact: Stops the assumption that prompt-only still keyframes are automatically safer than video for dense two-character combat.
- draft rule text:

```text
Do not assume text2image is safer than video for dual-character close-combat staging. If prompt-only text2image fails remotely after valid submit/query, and the prompt already removed active refs, exact wall contact, and wall damage, broaden the diagnosis to dual-character close-combat/contact staging brittleness. Prefer route reset, video-first motion probe, manual layout, or simpler single-character insert over another same-class still keyframe.
```

## Candidate 6 - Text2Video Front-Loaded Edit-Window Strategy

- proposed Source file name: `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- proposed section title: `Text2Video前置动作与可剪辑窗口`
- evidence phases: K220B, K221, K241F, K242V, K243V, K244
- priority: high
- implementation impact: Defines how a legal-duration video prompt should target a short usable combat window.
- draft rule text:

```text
For 5s combat video probes, design the first 1.0s-1.5s as the likely usable edit window. The first frame should already be close to the action. The decisive pressure/contact beat should occur before 0.65s. The prompt must include continued motion after the cut window to avoid static tail or pose-out, but later seconds should be treated as continuation handles, not proof that the whole clip is final-use ready.
```

## Candidate 7 - Action Reference Video Library and Review Rubric

- proposed Source file name: `AI视频制作_动作参考视频库与审片标准_V0.1.md`
- proposed section title: `动作参考视频库的用途、命名、标注与审片评分`
- evidence phases: K220B, K242V, K244S Part 4
- priority: medium
- implementation impact: Creates a human-curated action grammar reference layer without using copyrighted/action refs as active generation inputs by default.
- draft rule text:

```text
Action reference videos are action grammar references, not active generation inputs by default. They should be used to describe timing, pressure, contact clarity, floor feedback, camera rhythm, and edit-window usefulness. They must not be uploaded into generation tools or treated as final assets unless a separate rights/safety decision explicitly allows that use. Visual review should compare outputs against the reference rubric, not copy the reference clip.
```

## Candidate 8 - Macro-Run Authorization Levels

- proposed Source file name: `AI视频制作_自动化宏流程与授权等级_V0.2.md`
- proposed section title: `宏流程中的提交、查询、下载、重试、重提授权分离`
- evidence phases: K213, K225, K226, K230, K235, K241, K244, K244S Part 3
- priority: high
- implementation impact: One-click-ish workflow becomes a gated orchestration, not an unbounded live execution.
- draft rule text:

```text
Macro-run automation must keep submit, query, download, retry, resubmit, media creation, Source update, final, and lock as separately authorized actions unless a specific macro authorization explicitly combines them. Submit-only does not imply query. Query-only does not imply download. Failure does not imply retry. Package review pass does not imply submit. Media output does not imply final or lock.
```

## Candidate 9 - Human Review Defaults

- proposed Source file name: `AI视频制作_自动化宏流程与授权等级_V0.2.md`
- proposed section title: `人工审查默认对象：图片/视频优先，Prompt按需`
- evidence phases: K220B, K244, K244S Part 3 conversation context
- priority: high
- implementation impact: Human workload is centered on visual outputs by default, while prompt review is reserved for known trigger conditions.
- draft rule text:

```text
By default, the human reviews images and videos, not prompts. Prompt review should occur after repeated failure, major route change, package-review defect, or explicit human request. A package can pass with high-risk notes without forcing prompt review if the next required human decision is visual or submit authorization. Video output requires human visual review before final use.
```

## Candidate 10 - Source Index and Evidence-Pack Use

- proposed Source file name: `AI视频制作_Source索引与使用优先级_V1.8.md`
- proposed section title: `证据包到Source更新的治理路径`
- evidence phases: K244S Parts 1-4
- priority: medium
- implementation impact: Clarifies that K244S files are upload/synthesis inputs for ChatGPT Pro Extended, not official Source.
- draft rule text:

```text
Evidence consolidation packs may recommend Source updates, but they are not official Source. ChatGPT Pro Extended or the human must transform evidence into Source drafts. The human must manually approve and apply official Source changes. Codex may collect ledgers, taxonomies, review excerpts, prompt archives, and candidate rules under reports, but must not directly modify sources/.
```
