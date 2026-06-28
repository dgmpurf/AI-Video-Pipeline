# PHASE K191P - Prompt Pipeline and Result-First Action Grammar Audit

## 1. Purpose

This report audits the current Chi Yan Tian Qiong prompt generation, review, package, and submit workflow after the SHOT-04 Route A visual failure.

The goal is not to prepare a new package. The goal is to identify why a package can pass source/package compliance while still failing the visual target, and to define a better prompt-compilation layer for future SHOT-04 terrain/architecture interaction work.

Final target of this audit:

- convert Source rules into visible outcome requirements
- reduce prompt dilution from reference duties and negative constraints
- enforce result-first action grammar before package creation
- support a K192 route decision instead of blindly packaging another prompt

## 2. Authorization and Boundaries

Authorization level: L0 report-only macro-run.

Boundaries honored:

- No Dreamina command was run.
- No submit/query/download was run.
- No retry/resubmit/batch action was run.
- No media was created or edited.
- No frames, contact sheets, or cut MP4 files were created.
- No package JSON, manifest CSV, prompt TXT, or shot record was modified.
- No runtime code or `configs/providers.json` was modified.
- No files under `sources/` were modified, staged, committed, renamed, moved, or deleted.
- No final-master or locked state was set.

## 3. Files Inspected

Reports inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K190_SHOT04_ROUTE_A_VISUAL_REVIEW_FAILURE_AND_PROMPT_CORRECTION.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K189_SHOT04_ROUTE_A_DOWNLOAD_RESULT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K186_SHOT04_ROUTE_A_PACKAGE_REVIEW_FOR_HUMAN_SUBMIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K185_SHOT04_ROUTE_A_L2_NO_SUBMIT_PACKAGE_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K184_SHOT04_ROUTE_A_BLUEPRINT_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K183_SHOT04_ROUTE_A_COMPOSITION_MATRIX_AND_PROMPT_BLUEPRINT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K138_SHOT03_V006_HUMAN_AND_CHATGPT_REVIEW_FAILED_FORCE_CHAIN_AND_TERRAIN_ANCHOR.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K139_SHOT03_V004_V005_V006_COMPARATIVE_STRATEGY_REVIEW.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K130_SHOT03_V005_SOURCE_COMPLIANCE_AND_V006_FORCE_CHAIN_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K131_SHOT03_V006_FORCE_CHAIN_PROMPT_DRAFT_READY_FOR_CHATGPT_AUDIT.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K165_SHOT03_SPLIT02_POSE_KF_VISUAL_REVIEW_FAILED_IDENTITY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K175_SHOT03_SPLIT02_POSE_KF_R02_VISUAL_REVIEW_FAILED_BLOCKING.md`

SHOT-04 Route A package files inspected:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/shot_04_v001_routeA_railing_lattice_impact_rebound_multimodal2video_package_no_submit.json`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-04-V001_routeA_no_submit.csv`

Sources read as read-only references:

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.6.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.9_空间调度与远近站位控制_完整版_修正版_V1_9_2.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化宏流程与授权等级_V0.1.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`

## 4. Source Governance Confirmation

`sources/` is official human-controlled project Source.

Codex used Source files only as read-only reference material. This report is evidence and recommendation material under `reports/`; it is not an official Source update. Any future official Source update should be generated/reviewed by ChatGPT and manually applied by the human user.

Confirmed invariant for future automation:

- `source_read_allowed=true`
- `source_recommendation_allowed=true`
- `source_draft_allowed=true`
- `source_write_allowed=false`
- `source_stage_allowed=false`
- `source_commit_allowed=false`
- `official_source_update_requires_human_manual_action=true`

## 5. Current Pipeline Map

Current working pipeline:

1. Human or Codex identifies creative target and current shot state.
2. Source files are read as rule references.
3. Planning reports define route, reference duties, and package strategy.
4. Manual prompt draft is prepared.
5. Package JSON / manifest / review report is prepared.
6. Independent package review checks technical and textual compliance.
7. Human authorizes a single live submit.
8. Query/download happens in separately authorized phases.
9. Local review artifacts are created.
10. Human and/or ChatGPT visual review records the result.
11. Route decision or correction direction is recorded.

This pipeline is strong at operational safety and bookkeeping. It is weaker at ensuring that prompt text compiles into the specific visible result before submit.

## 6. What Works Well

- Phase isolation is strong: planning, package, submit, query, download, review, and route decisions are separated.
- Dreamina boundaries are usually explicit and auditable.
- Package reviews catch many technical risks before submit.
- Reference-duty maps reduce accidental identity/scene reference mixing.
- Human review is consistently recorded before final/lock decisions.
- Media is kept out of git staging.
- Source governance is clear: Source read is allowed, Source write is forbidden.

## 7. Weak Points

The main weakness is not lack of Source. The weakness is translation from Source rules into a short, dominant, visual-result-first prompt.

Observed weak points:

- Source compliance often checks whether a rule is present, not whether it dominates the prompt.
- Prompt text can be technically compliant but visually low-priority.
- Reference duties and negative constraints can occupy the front of the prompt and push the action result later.
- Action verbs may describe pressure or intent instead of final visible results.
- Negative constraints are numerous but not always compressed into a priority-safe block.
- Package review can pass even if the first visible action sentence is too soft.
- Visual review happens after paid generation, while prompt priority risk is often not scored before submit.

## 8. Case Study A - SHOT-04 Route A Failure

Route A was designed as a railing/lattice impact and rebound shot. Package review passed, and the submit/download pipeline succeeded. The visual result failed because the generated clip did not strongly realize the intended architecture-as-weapon beat.

K190 diagnosis indicates the result read closer to pushing/holding near a railing/lattice than to a hard, result-first body impact into architecture followed by rebound.

Likely prompt-level causes:

- The prompt began with reference duties and scene/camera setup before the dominant result.
- The action phrase "compresses guard toward railing/lattice" was softer than "body/shoulder hits railing/lattice and rebounds."
- The prompt had many guardrails but the positive desired result was not front-loaded enough.
- The damage/impact causality was technically present but not the first thing the model had to solve.
- The scene/action reference stack may have diluted the route's one required visual outcome.

## 9. Actual Route A Prompt Analysis

Route A prompt metadata:

- Prompt path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt`
- Word count: 655
- SHA256: `dfbbc3c03ceede3c134d5464aaad8faf5bdcf38ddbe5cbf8277e6abcc70517e1`

The first part of the prompt is dominated by reference duties and scene/camera framing:

```text
@FENSHOU_IDENTITY_REF: Use only for Fenshou identity...
@SHUANGJI_IDENTITY_REF: Use only for Shuangji identity...
@RAINY_TEMPLE_SCENE_REF: Use only for the rainy ancient temple world...
Create a 5-second cinematic semi-realistic 3D wuxia combat video...
...No beauty portrait framing.
```

The first dominant action appears only after reference duties, scene framing, camera setup, and safety framing.

Measured prompt positions:

- `ACTION_INDEX_COMPRESS=1562`
- `ACTION_INDEX_FENSHOU=1616`
- `ACTION_INDEX_SHOULDER=1652`

Interpretation: the model sees identity/scene/camera/safety before it sees the central visible result. This does not guarantee failure, but it raises risk when the shot requires one specific physical outcome.

Specific prompt risk:

- "Compresses guard toward railing/lattice" can become a push, hold, or soft crowding action.
- "Railing/lattice impact rebound" was the title, but the early prompt body did not enforce the visual result in the first 1-3 action sentences.
- Dense negative constraints may have reduced room for positive physical causality.

## 10. Case Study B - SHOT-03 V006 Prompt-Only Limitation

SHOT-03 V006 attempted to correct V005 soft-force failure through stronger prompt text. It improved explicit force-chain language, but visual review still found limits in using prompt-only language to force readable body mechanics and terrain affordance.

This matches K130/K138/K139:

- Source rules were read.
- The prompt added force-chain concepts.
- The generation still struggled with physical clarity.
- Prompt-only correction was not enough without better reference planning, shorter goal scope, and visual-result-first action grammar.

Lesson: adding more rules does not necessarily increase visible compliance. Rules must be prioritized, compressed, and translated into result clauses.

## 11. Case Study C - SPLIT-02 R01/R02 Identity vs Blocking

SPLIT-02 R01/R02 image2image attempts showed another prompt-pipeline limit.

The packages improved identity-lock intent and reference-duty planning, but the visual result still failed around blocking, identity preservation, and shot usability.

Lesson:

- Identity references need clear priority, but identity priority alone can conflict with pose/action transformation.
- If the requested output needs both identity repair and action/blocking transformation, the package must decide which visual result is primary.
- A reference stack can be correct on paper and still overconstrain or confuse the model.

## 12. Prompt Compiler / Prompt Director Definition

The project needs an explicit Prompt Compiler or Prompt Director layer between Source reading and package creation.

Definition:

The Prompt Compiler is a pre-package transformation step that converts planning intent and Source rules into a short ranked prompt structure where the intended visual result appears first, dominates the action block, and remains testable after generation.

The Prompt Director is the human/ChatGPT judgment role that decides which visual outcome is most important when identity, scene, action, camera, damage, and safety constraints compete.

The Prompt Compiler should not merely include rules. It should decide prompt priority.

## 13. Proposed Prompt Hierarchy V0.1

Recommended hierarchy for high-risk action shots:

1. Visual result headline: one sentence stating the exact visible outcome.
2. First-frame continuity: what must be preserved from the start frame or refs.
3. Primary action beat: the required physical cause and effect.
4. Secondary action beat: rebound/re-entry/follow-through.
5. Character identity guardrails: short, role-specific, non-competing.
6. Scene/space guardrails: only what is necessary for the shot.
7. Camera constraints: concise and compatible with action.
8. Negative constraints: compressed by risk priority.
9. Final continuity hook: where the shot should cut out.

For architecture interaction shots, the first visible result should appear before all long reference-duty prose.

Example result-first opening pattern:

```text
Visible result: in the first second, Fenshou's shoulder and forearm drive Shuangji's guarded upper body into the side railing/lattice, the structure reacts from real body contact, and Shuangji rebounds into a counter-guard without stopping.
```

## 14. Result-First Grammar Rules

Required grammar for future hard action prompts:

- Start with the result: what the viewer must see.
- Then state the cause: which body part creates the force.
- Then state the contact: where it lands.
- Then state the consequence: body displacement, guard compression, skid, rebound, damage, dust, or water response.
- Then state continuation: no poster hold, no dead tail.

Preferred form:

```text
Actor body-part -> target contact-point -> immediate visible result -> continuation.
```

Example:

```text
Fenshou plants his rear foot, drives shoulder and forearm into Shuangji's crossed guard, compresses her into the wet railing support, makes the railing shake only from contact, then both rebound back into close-range guard.
```

Avoid soft verbs as primary result verbs:

- approaches
- presses
- crowds
- compresses toward
- moves around
- uses the environment
- shows tension

Prefer result verbs:

- hits
- rebounds
- skids
- jams
- checks
- deflects
- slams guard into
- shoulder-drives into
- snaps back into guard

## 15. Prompt Priority Audit Table Proposal

Before packaging, every high-risk prompt should include a priority audit table.

| Priority | Prompt element | Must appear before word/character | Pass criterion |
| --- | --- | --- | --- |
| P0 | Main visible result | first 60-90 words or first 300-450 chars | A reviewer can name the exact shot result from the opening alone |
| P0 | Primary physical cause | same first action block | Body part, support foot, and target are named |
| P0 | Immediate consequence | same first action block | Displacement/rebound/damage/water reaction is named |
| P1 | Identity anchors | after result headline or in compact tags | Do not overtake action priority |
| P1 | Scene continuity | after action result | Only needed scene facts |
| P2 | Negative constraints | late compressed block | No more than needed; no positive action dilution |

For SHOT-04 Route A, this table would likely have flagged the late dominant action and soft result verb before submit.

## 16. Visual Result Compliance Table Proposal

After generation, review should score visible results, not only general quality.

| Requirement | Expected visible evidence | Review status |
| --- | --- | --- |
| First-second architecture contact | Body/guard hits railing/lattice in first second | pass/fail/partial |
| Physical causality | Structure reacts only after body contact | pass/fail/partial |
| Rebound | Character rebounds/re-enters instead of holding | pass/fail/partial |
| Identity stability | Fenshou/Shuangji roles remain readable | pass/fail/partial |
| No soft push | Contact has impact, not posing | pass/fail/partial |
| No prompt drift | No weapon/flying/wall-run/extra character | pass/fail/partial |

This table should become the bridge between prompt intent and human/ChatGPT visual review.

## 17. Negative Constraint Compression Audit

Negative constraints are necessary, but they can dilute the positive shot if they dominate the prompt.

Recommended audit:

- Count negative clauses.
- Group by risk: identity, scene, motion, safety, artifact.
- Remove duplicate negatives.
- Keep the main visual result positive and first.
- Convert some negatives into positive replacements.

Example:

Instead of:

```text
Do not make a full wall-run, do not fly, do not jump, do not go to roof.
```

Use:

```text
Keep both fighters grounded on the wet corridor floor; footwork stays short and forceful.
```

Then keep only the highest-risk negatives at the end.

## 18. Reference Duty Attention Audit

Reference duties are essential, but when listed first in long blocks they can consume the opening attention budget.

Recommended audit:

- Identify each reference duty.
- Rank references by the shot's primary goal.
- Move only the most essential continuity constraint near the opening.
- Keep detailed identity duties compact.
- Avoid making action/composition refs compete with identity refs.
- For high-risk action, state "identity refs preserve character design; action result is governed by the action block."

Reference-duty table proposal:

| Ref | Duty | Priority | Risk |
| --- | --- | --- | --- |
| Fenshou identity | identity only | P1 | Can overtake action if too verbose |
| Shuangji identity | identity only | P1 | Must prevent gender/role drift |
| Scene/world | environment only | P2 | Can dilute action if over-described |
| Action/composition | motion/blocking only | P0/P1 depending shot | Must not become identity reference |

## 19. Prompt Outcome Dataset Proposal

Create a lightweight dataset across reports:

- shot_id
- phase
- prompt_sha256
- package_type
- primary visual target
- first dominant action position
- negative constraint density
- reference count
- submit result
- review verdict
- visual failure category
- reusable prompt lesson

This can be maintained in reports first, without becoming official Source.

Useful categories:

- identity_drift
- soft_force
- no_terrain_affordance
- architecture_contact_missing
- reference_attention_conflict
- prompt_priority_failure
- overconstrained_negative_block
- action_result_too_late

## 20. Required Pre-L2 Checklist

Before future L2 no-submit packages for high-risk action shots:

1. Main visible result appears in the first action sentence.
2. Result clause includes body part, target, contact point, consequence, continuation.
3. Dominant action appears before long reference duties or scene prose.
4. Negative constraints are compressed and non-duplicative.
5. Reference-duty map states which refs must not control identity/action.
6. Prompt Priority Audit table is completed.
7. Visual Result Compliance table is drafted before submit.
8. If no visual target ref exists for the desired action, mark prompt-only risk explicitly.

## 21. K192 Decision Framework

K192 should decide whether SHOT-04 continues with another prompt-only Route A or changes strategy.

Recommended default:

- Do not blindly package another prompt-only Route A.
- Prefer Route B or Route C if no wall-panel/railing impact reference exists.
- Route A may still be allowed as a high-risk prompt-only test only if speed is prioritized and the human explicitly accepts the risk.

Route options:

| Route | Meaning | Recommendation |
| --- | --- | --- |
| A | Direct prompt-only architecture impact retry | High risk unless result-first prompt compiler is applied |
| B | Create/select stronger visual target reference first | Preferred if the architecture contact is essential |
| C | Split SHOT-04 into smaller micro-shots | Preferred if one 5s shot is overburdened |

For SHOT-04, the desired result is not "more combat." It is architecture-as-weapon with causal body contact and visible rebound. If that is the must-have, reference planning may matter more than prompt length.

## 22. Future Source Candidate Names and Rules

This report is not Source. It can support future ChatGPT-generated Source candidates such as:

- `AI视频制作_提示词编译器与结果优先动作语法_V0.1.md`
- `AI视频制作_视觉结果合规表与Prompt优先级审计_V0.1.md`
- `AI视频制作_引用职责注意力与负面约束压缩规则_V0.1.md`

Candidate rules for future Source:

- Source compliance is not rule inclusion; it is visible-result prioritization.
- High-risk action prompts must begin with the visible result.
- Every contact beat must state cause, contact, consequence, and continuation.
- Reference duties must not push the main action below the opening priority band.
- Negative constraints must be compressed after positive action grammar.
- Prompt-only retries should be labeled high risk when the desired physical result lacks visual reference support.

## 23. Codex Role Update

Codex should continue to:

- read official Source as read-only material
- create reports, audits, and package files only when authorized
- preserve submit/query/download phase boundaries
- avoid modifying official Source files
- stage only explicitly authorized text artifacts

Codex should add:

- prompt priority audit before package readiness claims
- visual-result compliance table before submit review
- explicit prompt-only risk labels when references do not support the desired result
- result-first grammar checks on any high-risk action prompt

## 24. Concrete Prompt Compiler V0.1 Checklist

Use this before K192/K193 package work:

1. Name the one required visible result.
2. Put that result in the first 1-2 prompt sentences.
3. Use the grammar: actor body-part -> contact target -> visible consequence -> continuation.
4. Check that the first dominant action appears before long reference/scene/camera blocks.
5. Replace soft verbs with result verbs.
6. Compress negatives.
7. Keep reference duties short and ranked.
8. Draft the visual compliance table before submit.
9. Decide whether prompt-only is enough or whether a visual target reference is needed.
10. Mark final_master=false and locked=false until human review.

## 25. Recommended Next Phase K192

K192 should be a route decision and prompt-compiler application phase.

Recommended K192 output:

- decide Route A/B/C for SHOT-04 R02
- apply result-first grammar to the selected route
- state whether a new visual reference is required
- do not submit unless separately authorized

Suggested K192 title:

`SHOT-04 R02 route decision and result-first prompt compiler application`

## 26. What Not To Do

Do not:

- run another prompt-only submit just because the package can pass compliance
- treat Source reading as proof that the prompt will generate the desired result
- allow the prompt opening to be dominated by reference duties when the shot requires a specific physical outcome
- expand negative constraints until they crowd out the positive result
- mark Route A failure as a Dreamina or remote-generation problem
- update official Source directly from Codex

## 27. Safety Confirmation

- No Dreamina command was run.
- No submit/query/download was run.
- No media was created, edited, staged, or committed.
- No prompt/package/manifest/shot-record file was modified.
- No files under `sources/` were modified, staged, committed, renamed, moved, or deleted.
- Runtime code and `configs/providers.json` were not modified.
- Auth/session/token/key/env contents were not opened or printed.
- `final_master=false` remains the required state.
- `locked=false` remains the required state.

## 28. Final Verdict

PROMPT_PIPELINE_AUDIT_READY_FOR_CHATGPT_PROMPT_COMPILER_UPDATE_AND_K192_ROUTE_DECISION
