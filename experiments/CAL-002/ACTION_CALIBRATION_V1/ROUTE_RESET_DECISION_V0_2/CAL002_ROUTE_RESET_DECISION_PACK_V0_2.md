# CAL-002 Batch05 Route Reset Decision Pack V0.2

## 1. 给人的简明结论

Batch05 的四组盲审配对中，Candidate 四次全部输给对应 Control；但 Candidate 和 Control 都没有任何一次达到严格 primary pass。这说明问题不只是 Candidate 写法变差，也不是再换几个词就能解决，而是当前这条“纯文本、单个五秒连续镜头、一次完成完整双人因果动作链”的路线，在已测试的 `push_reaction` 和 `brief_impact_recoil` 范围内不再值得继续重试。

因此，本包只关闭这条已测试路线，不关闭整个 CAL-002，也不宣布所有 text2video 或 Seedance 动作生成都失败。下一步应换控制手段。Route A 动作参考运动控制最直接针对时序、接触时长、脚步、后坐、收手和尾段运动，因此被推荐为优先研究路线；但它尚未被证明可用，Provider 能力、版权来源、身份和场景泄漏仍需分别验证。

本包没有选择路线，没有激活路线，没有授权生成，也没有允许回到《赤焰对天穹》生产。人类需要在文末四个选项中明确选择下一步。

## 2. What Batch05 Proved

- Four of four valid matched comparisons were `CONTROL_CLEAR_ADVANTAGE`.
- Candidate pair wins: `0`.
- Control pair wins: `4`.
- Candidate strict primary passes: `0`.
- Control strict primary passes: `0`.
- Both tested action families frequently failed under both treatments.
- `push_reaction = ROUTE_RESET_REQUIRED`.
- `brief_impact_recoil = ROUTE_RESET_REQUIRED`.
- Candidate underperformance is negative evidence but does not override the Rule 1 route-reset result.
- The tested route is unsupported for the two tested families under the exact Batch05 conditions.
- Another same-route Prompt revision is not a justified next experiment.

## 3. What Batch05 Did Not Prove

Batch05 did not prove:

- statistical significance;
- causal responsibility of one Prompt clause;
- failure of every text2video workflow;
- failure of every structured Prompt;
- universal Provider or model incapability;
- failure of every action family;
- success of any reference-assisted route;
- production readiness;
- Source adoption authority.

The treatment was a compound compiler bundle, so component-level causal attribution is not permitted.

## 4. Exact Closed-Route Scope

| Field | Closed scope |
| --- | --- |
| route_id | `CAL002_TEXT_ONLY_ACTION_FAMILY_COMPILER_ROUTE_BATCH05` |
| route_status | `CLOSED_NOT_SUPPORTED_WITHIN_TESTED_SCOPE` |
| task_type | `text2video` |
| generation_reference_strategy | text only, no active generation reference |
| model_target | `seedance2.0_vip` |
| duration | 5 seconds |
| camera_strategy | locked medium-wide single continuous shot |
| treatment_unit | compound action-family Prompt compiler bundle |
| tested_action_families | `push_reaction`, `brief_impact_recoil` |
| tested_objective | one complete causal physical action chain in one generated clip |

Within this scope:

- same-route retry is prohibited;
- Prompt-only wording reshuffle is prohibited;
- synonym replacement is not a route change;
- another Batch05 replicate is prohibited;
- adding more negative wording is not an approved rescue;
- Candidate family compilers are not approved for production.

Outside this scope, no broad model, Provider, action-family, or text2video conclusion is established.

## 5. Consolidated Failure Taxonomy

| Failure class | Evidence examples | Family | Observed in | Directly addressed by | Residual risk after route change | New route risks |
| --- | --- | --- | --- | --- | --- | --- |
| delayed_or_weak_reaction | `PUSH_PAIR_01_A` reacts only after delayed contact; `PUSH_PAIR_02_A` has weak torso displacement; `IMPACT_PAIR_01_A` has weak recoil | both | Candidate and Control | A timing reference; B explicit reaction state; C separate reaction shot | generated motion may still soften consequence | A reference leakage; B interpolation; C continuity |
| sustained_contact_no_release | `PUSH_PAIR_01_B`, `PUSH_PAIR_02_A`, and `IMPACT_PAIR_02_B` become held contact instead of a brief event | both | Candidate-dominant | A contact rhythm; B separated contact/release states; C cut at contact boundary | model may interpolate prolonged pressure | B morphing; C visible cut discontinuity |
| no_prompt_retract_or_extended_arm_freeze | several push and impact clips keep the attacking arm extended after contact | both | Candidate and Control | A release/retract motion; B explicit retract frame; C separate retract shot | retraction can still occur late or become a pose | B pose-to-pose stiffness; C identity mismatch |
| long_static_ending_or_early_completion | all reviewed outputs fail the ending contract; static tails range from about 0.7 to 4.5 seconds | both | Candidate and Control | A temporal continuation; B stable but active result state; C trim or replace the tail | route may still end in a frozen guard | C can hide rather than solve generation weakness |
| no_foot_result | `PUSH_PAIR_01_B`, `IMPACT_PAIR_01_A`, and `IMPACT_PAIR_02_B` show no required foot result | both | Candidate-dominant | A footwork reference; B exact foot-placement state; C dedicated recovery shot | foot may slide or be occluded | B anatomical distortion; C continuity burden |
| excessive_or_ambiguous_footwork | `PUSH_PAIR_01_A` and `PUSH_PAIR_02_B` replace one recovery placement with four-step retreat; `PUSH_PAIR_02_A` has only weak consequence | push | Candidate and Control | A single-step rhythm; B exact result pose; C isolate one recovery beat | extra steps or foot sliding can remain | B unstable interpolation; C screen-direction errors |
| framing_and_spatial_escape | `PUSH_PAIR_02_A` crops heads; `PUSH_PAIR_02_B` drifts partly out of frame | push | Candidate and Control | B layout anchors most directly; A separate camera controls; C shot-by-shot framing | action energy can still exceed composition | A reference-camera leakage; C cross-shot mismatch |
| brief_impact_routed_as_sustained_push | `IMPACT_PAIR_02_B` reads as multi-second straight-arm pressure | impact | Candidate | A brief-impact timing reference; B contact/recoil/retract states; C separate contact and recoil shots | family identity may still blur | A source-motion mismatch; B morphing |
| push_routed_as_static_contact_drill | `PUSH_PAIR_01_B` holds palm contact with no consequence | push | Candidate | A motion grammar; B result-state displacement; C split contact and response | contact can remain decorative | all routes still require strict full review |
| contact_without_receiving_body_consequence | `PUSH_PAIR_01_B` and `IMPACT_PAIR_02_B` show contact without torso or foot response | both | Candidate | A weight-transfer/recoil reference; B explicit receiver state; C dedicated consequence shot | visible consequence can remain weak | A identity leakage; B body deformation; C edit discontinuity |
| prompt_route_obedience_limit | exact contact duration, foot count, release timing, and ending duration were not reliably obeyed; Candidate bundles underperformed matched Controls | both | Candidate and Control | route-level intervention only | alternative routes remain unproven | each route adds preparation, capability, or continuity costs |

This taxonomy is decision evidence, not an adopted stable Source rule.

## 6. Route A Analysis: Action Reference Motion Control

Route ID: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`

Definition: a rights-safe action-reference video supplies motion timing, pose progression, contact rhythm, weight transfer, footwork, recoil, release/retract behavior, and temporal continuation only. Identity, costume, scene, camera, composition, and style remain separate controlled duties.

Control potential:

- Temporal sequence: `HIGH`.
- Contact duration: `HIGH`.
- Single-step footwork: `HIGH`.
- Recoil and weight transfer: `HIGH`.
- Release/retract: `HIGH`.
- Ending motion: `HIGH`.
- Spatial layout: `MEDIUM`, because motion reference alone does not guarantee framing.
- Reproducibility: potentially `HIGH` after capability and reference preparation are standardized.

Key risks:

- action-reference identity, costume, scene, or camera leakage;
- Provider may not support a native motion-only duty;
- reference motion may dominate project identity or composition;
- rights, performer consent, provenance, and downstream-use restrictions;
- preparation burden for clean, rights-safe references;
- false confidence from matching motion while identity or scene fails.

Prerequisite gates:

1. A rights-safe push reference and brief-impact reference exist.
2. Reference duty is explicitly motion-only.
3. Tool or Provider capability is independently verified.
4. Identity and scene leakage controls are designed.
5. No unsafe IP, personal-data, performer-rights, or redistribution issue remains.
6. No calibration output enters production before review passes.
7. Stopping conditions and cost ceiling are approved.

- Provider native capability status: `UNVERIFIED_REQUIRES_FUTURE_READ_ONLY_CAPABILITY_AUDIT`.
- Current price checked: `false`.
- Current credit checked: `false`.
- Recommended status: `PRIMARY_RESEARCH_ROUTE_RECOMMENDED_FOR_HUMAN_SELECTION`.
- Selected: `false`.
- Active: `false`.
- Production ready: `false`.

## 7. Route B Analysis: Manual Pose / Start-End Frame Control

Route ID: `CAL002_ROUTE_B_MANUAL_POSE_START_END_FRAME_CONTROL`

Definition: manually or deterministically construct start, launch, contact, receiver reaction, exact rear-foot placement, release/retract, and stable end states. A compatible image2video, frames2video, start/end-frame, pose, or layout mode may be considered only after capability verification.

Control potential:

- Start-state accuracy: `HIGH`.
- Result-state accuracy: `HIGH`.
- Actor spacing and contact geometry: `HIGH`.
- Exact foot placement: `HIGH`.
- Framing stability: `HIGH` when anchors are held.
- Temporal and contact-duration control: `MEDIUM`, because intermediate interpolation remains model-driven.
- Identity and costume consistency: `MEDIUM` risk.
- Intermediate-motion quality: `HIGH` risk.

Known project evidence supports frame selection, pose planning, explicit reference duties, and local pose/layout audits. It does not prove that a compatible future generation mode will produce physically correct intermediate motion.

Key risks:

- sliding, morphing, body deformation, or prolonged-contact interpolation;
- implausible transition between correct endpoint poses;
- still-image identity or scene mismatch;
- high manual still-generation and review burden;
- keyframes becoming poster-like static poses.

- Capability status: `UNVERIFIED_REQUIRES_FUTURE_READ_ONLY_CAPABILITY_AUDIT`.
- Recommended status: `SECONDARY_CONTROL_ROUTE`.
- Selected: `false`.
- Active: `false`.
- Production ready: `false`.

## 8. Route C Analysis: Editorial Action Decomposition

Route ID: `CAL002_ROUTE_C_EDITORIAL_ACTION_DECOMPOSITION`

Definition: replace one complete five-second causal chain with narrow shots, for example:

1. attacker initiation and brief contact;
2. receiver recoil and one recovery step;
3. release, stabilization, guard, reaction, or continuation.

Editing, sound, hit-stop, speed adjustment, shot order, and local cuts may construct the perceived complete action.

Strengths:

- lowers per-shot motion complexity;
- isolates failure states;
- permits regeneration of one failed sub-shot rather than the whole chain;
- makes static tails easier to remove;
- has partial support from existing local split-shot and cut-review evidence;
- gives fast, observable failure detection.

Risks:

- cross-shot identity, costume, scene, lighting, camera, and screen-direction drift;
- edit labor and continuity review;
- increased generated-clip count;
- a cut can hide rather than solve motion weakness;
- narrow shots may still fail their assigned action.

Historical planning anchor: Batch05 used 70 credits per five-second `seedance2.0_vip` text2video submit. This is historical evidence only and is not current pricing.

- Estimated generation cost: `planned_clip_count * then-current verified unit cost`.
- Current price checked: `false`.
- Current credit checked: `false`.
- Capability status: `PARTIALLY_SUPPORTED_BY_EXISTING_LOCAL_EDITORIAL_WORKFLOW_EVIDENCE`.
- Recommended status: `PRODUCTION_FALLBACK_AND_FASTEST_FEASIBLE_ROUTE`.
- Selected: `false`.
- Active: `false`.
- Production ready: `false`.

## 9. Comparison Matrix Explanation

The companion CSV contains one row per route and no aggregate numeric score.

Ordinal meanings:

- `HIGH`: the attribute, burden, dependency, or risk is expected to be a dominant route characteristic.
- `MEDIUM`: meaningful but bounded; it must be tested rather than assumed.
- `LOW`: secondary relative to the other routes, not zero.
- `NOT_APPLICABLE`: the characteristic does not materially apply to that route design.
- `UNVERIFIED`: current committed evidence does not prove the capability.
- `PARTIALLY_SUPPORTED`: local planning or editorial evidence exists, but production validation does not.

These ordinals support comparison only. They are not measured performance scores.

## 10. Recommendation Hierarchy

1. Primary research route: `ACTION_REFERENCE_MOTION_CONTROL`.
2. Secondary controlled-research route: `MANUAL_POSE_START_END_FRAME_CONTROL`.
3. Fastest production fallback: `EDITORIAL_ACTION_DECOMPOSITION`.

Route A is recommended because the dominant failures concern motion timing, contact duration, weight transfer, exact foot count, recoil, release/retraction, and continued motion. Those variables were not reliably controlled by text alone.

The recommendation is conditional on rights-safe references, verified capability, motion-only duty separation, acceptable identity and scene leakage, acceptable preparation burden, and an approved calibration ceiling.

Fallback logic:

- If Route A capability or rights gates fail, recommend Route B for the next controlled experiment.
- If Route B capability or intermediate motion also fails, recommend Route C as the practical production fallback.

- Recommended primary route: `CAL002_ROUTE_A_ACTION_REFERENCE_MOTION_CONTROL`.
- Route selected: `null`.
- Route activated: `false`.
- Route execution authorized: `false`.

## 11. Route Prerequisites and Unknowns

Route A unknowns:

- native motion-reference support and duty separation;
- accepted formats and reference behavior;
- identity, costume, scene, and camera leakage;
- rights-safe source availability;
- preparation time and then-current cost.

Route B unknowns:

- compatible start/end or frames2video capability;
- stability of endpoint adherence;
- interpolation quality;
- identity and scene consistency;
- still-preparation burden and then-current cost.

Route C unknowns:

- continuity drift across six narrow clips;
- edit workload;
- narrow-action success rate;
- then-current per-clip cost;
- whether the assembled action remains visually coherent.

No Provider call is authorized to resolve these uncertainties in this Goal.

## 12. Minimum Validation Programs

Route A:

- Inputs: one rights-safe push clip, one rights-safe brief-impact clip, and separate identity and scene controls.
- Outputs: two push replicates and two impact replicates, four total.
- Primary screen: at least one strict pass per family; no repeated identity or scene leakage; motion fidelity exceeds the text-only baseline.
- Stop on unsupported capability, unavailable rights-safe source, repeated leakage, repeated family failure, unacceptable burden, or exceeded cost ceiling.

Route B:

- Inputs: one controlled start/result-state pair for each family.
- Outputs: two outputs per family, four total.
- Primary screen: respected endpoints, at least one strict pass per family, no repeated sliding/morphing/prolonged interpolation, stable identity and framing.
- Stop on unavailable mode, unstable endpoint adherence, repeated causal failure, unacceptable still burden, or identity instability.

Route C:

- Design: three narrow shots per family.
- Outputs: six generated clips total and one local editorial assembly per family.
- Primary screen: each clip performs its one job; the assembled action reads causally; identity, scene, and screen direction remain coherent.
- Stop on narrow-shot failure, unusable continuity drift, excessive edit burden, or uneconomic volume.

All three programs are `PROPOSED_NOT_AUTHORIZED`. They create no live, media, or production authority.

## 13. Expected Human Workload

- Route A: `HIGH` reference search, rights confirmation, action annotation, leakage review, and full MP4 review.
- Route B: `HIGH` start/result still design, pose/layout audit, identity consistency review, and intermediate-motion review.
- Route C: `HIGH` editorial selection, continuity management, cut timing, sound/hit-stop design, and assembled-sequence review.

No route removes the need for human visual judgment.

## 14. Automation Potential

- Route A: `MEDIUM`; metadata, timeline annotation, reference-duty checks, and evidence packaging can be automated, but rights and final visual judgment cannot.
- Route B: `MEDIUM`; pose/layout manifests and technical frame checks can be automated, but still acceptance and motion review remain human.
- Route C: `MEDIUM`; clip inventory, cut candidates, synchronization, and technical validation can be automated, but continuity and production usefulness remain human judgments.

## 15. Cost Formulas and Uncertainty

No current price or credit balance was checked.

- Route A estimate: `4 * then-current verified unit cost + rights-safe reference preparation cost`.
- Route B estimate: `4 * then-current verified unit cost + start/result still preparation cost`.
- Route C estimate: `6 * then-current verified unit cost + editorial assembly cost`.

Different modes, durations, models, reference inputs, or Provider rules may change cost. Historical 70-credit evidence is not a current-price claim.

## 16. Risks and Stopping Conditions

Common stopping conditions:

- capability unavailable or materially different from the planned route;
- rights or provenance unresolved;
- identity, scene, costume, or camera leakage exceeds the approved threshold;
- repeated critical failure across both replicates of a family;
- preparation, generation, review, or editing cost exceeds the human-approved ceiling;
- no strict primary pass in the minimum program;
- evidence cannot support a route-level decision.

No automatic expansion, retry, resubmit, or fallback activation is allowed.

## 17. Future Source-Update Backlog

No Source is modified or authorized in this Goal.

Future backlog:

1. Correct stale candidate/pending wording in Source Index V1.13, Prompt Compiler V0.3, and Rolling Current State V0.1.
2. Record independently audited Batch05 negative evidence.
3. Close the tested text-only family-compiler route only for the two tested families and exact Batch05 conditions.
4. Preserve that CAL-002 remains open, ACTION_RULE V0.4 is not a stable default, no alternative route is proven, and recommendation is not activation.
5. Update the active route only after future human selection.

- Source update required later: `true`.
- Source update authorized now: `false`.
- Sources changed: `false`.

## 18. Production Re-Entry Gate

Production re-entry remains blocked until:

1. the human selects one route;
2. capability prerequisites pass;
3. rights and provenance prerequisites pass;
4. a separately authorized calibration design is approved;
5. reviewed calibration media exists;
6. at least one agreed action-family test passes;
7. human review explicitly approves production re-entry.

Production re-entry status: `BLOCKED_PENDING_ROUTE_SELECTION_CAPABILITY_VALIDATION_AND_CALIBRATION`.

No return to 《赤焰对天穹》 production is authorized.

## 19. Exact Human Decision Requested

No option is selected by this pack. The human choices are:

A. `SELECT_ACTION_REFERENCE_MOTION_CONTROL_FOR_NEXT_CAPABILITY_AND_CALIBRATION_DESIGN`

B. `SELECT_MANUAL_POSE_START_END_FRAME_CONTROL_FOR_NEXT_CAPABILITY_AND_CALIBRATION_DESIGN`

C. `SELECT_EDITORIAL_ACTION_DECOMPOSITION_FOR_NEXT_CALIBRATION_DESIGN`

D. `REQUEST_ROUTE_RESET_PACK_REVISION`

Next phase: `CAL002_ROUTE_RESET_ROUTE_SELECTION_DECISION`
