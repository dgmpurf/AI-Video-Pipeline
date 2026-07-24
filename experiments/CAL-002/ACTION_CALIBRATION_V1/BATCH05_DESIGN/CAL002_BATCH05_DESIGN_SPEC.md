# CAL-002 Batch05 Action-Family-Separated Replication Design V0.1

## 1. Scope

Goal identity:
`CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_V0_1`

Task label:
`CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_NO_LIVE`

This is a no-live experimental design. It defines exactly eight fixed Phase-1
tasks across two action families, two treatments, and two replicates. It does
not create executable Prompt files, provider packages, commands, claims,
authorization text, media, review artifacts, or live authority.

## 2. Human-Confirmed Project Source State

The following state is active by current human instruction:

```yaml
active_project_source_index: V1.13
active_prompt_compiler: V0.3
active_rolling_state: V0.1
active_by_current_human_instruction: true
embedded_candidate_status_text_stale: true
local_source_sync_authorized: false
```

The active Project Source names are:

- `AI视频制作_Source索引与使用优先级_V1.13.md`
- `AI视频制作_Prompt编译器与结果优先动作语法_V0.3.md`
- `AI视频制作_当前项目状态与双轨切换_V0.1.md`

The stale embedded candidate or pending-application text is non-blocking by
current human instruction. This design does not edit or synchronize local
`sources/`.

`ACTION_RULE_V0.4` remains provisional experimental evidence only:

```yaml
official_source_status: false
stable_general_rule: false
not_general_default: true
```

## 3. Evidence Basis

| Evidence | Path | SHA-256 |
| --- | --- | --- |
| Batch04 post-visual evidence pack | `reports/CAL002_BATCH04_POST_VISUAL_REVIEW_SOURCE_UPDATE_EVIDENCE_PACK.md` | `ccba5ed2d0c4c98ca3135ec8e4cb2bf995ca552ee20bb854bd1e3472797519e0` |
| Batch04 download result | `reports/CAL002_BATCH04_DOWNLOAD_EXECUTION_RESULT.md` | `10659a82920bca49111f74a2a1543cfefe3dcff6e068519c200d94850789def7` |
| Batch04 reconciliation | `reports/CAL002_BATCH04_DOWNLOAD_AUTHORIZATION_EXECUTION_RECONCILIATION_RESULT.md` | `3b8b5c555cf7cb7621430660779e474bd70354d7e7ddd4680f23220377c130b3` |
| Batch04 query result | `reports/CAL002_BATCH04_QUERY_EXECUTION_RESULT.md` | `3385cb0b0b8afa33882e7cb59605234d50920acf0d4d951b64b6ef6386498e46` |
| Batch04 design manifest | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH04_DESIGN/batch04_design_manifest.json` | `f2b12c4109b609c45c4659587be2814872e4b3751573bda09ec9629f5ec2f7ed` |
| Batch04 execution manifest | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH04_EXECUTION/batch_manifest.json` | `29fa8519d86b453bd4f6d9938f80b7b0fc89dcec533b4b18cad5f2cf1b394254` |
| ACTION_RULE V0.1 | `experiments/CAL-002/ACTION_CALIBRATION_V1/RULES/ACTION_RULE_V0.1.md` | `a10d28af271155b0fb32c3c8feb204ca487a82c9a60822884ffc576e19126337` |
| ACTION_RULE V0.2 | `experiments/CAL-002/ACTION_CALIBRATION_V1/RULES/ACTION_RULE_V0.2.md` | `a91d654b9cf961300f5ad9a6f7d06485bc51032da4c78ef9931664d356ef7cb6` |
| ACTION_RULE V0.3 | `experiments/CAL-002/ACTION_CALIBRATION_V1/RULES/ACTION_RULE_V0.3.md` | `0fdda04117d076fcb8e05f2a9a094d4302112c5539b3d1ddf878ed5c03c93464` |
| Local read-only Prompt Compiler context | `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md` | `f7eb4655dc2d5ab3164bf1c515d85b6362f3e076c0833b6170a3b3a144e8aa52` |

The human-confirmed active V0.3 Project Source state takes precedence for
design reasoning. The local V0.2 file is read-only context and is not treated
as proof that the Project Source remains at V0.2.

## 4. Batch04 Interpretation

```yaml
CAL002_formally_closed: false
Batch04_visual_outcome: MIXED
A01_candidate_superiority: true
A04_candidate_superiority: false
bundle_supported_as_general_default: false
bundle_has_action_specific_signal: true
treatment_bundle_screening: true
component_level_causal_attribution_permitted: false
```

Batch05 does not retest the entire Batch04 bundle as a universal treatment.
It tests two narrower compound treatment units:

- `push_reaction_family_compiler_bundle_v0_3`
- `brief_impact_recoil_family_compiler_bundle_v0_3`

No result may be attributed to an individual component.

## 5. Research Questions

### 5.1 Push reaction

Does the V0.3 push-reaction family compiler bundle repeatably improve the
visible causal sequence compared with a matched baseline action Prompt under
the same calibration conditions?

Target sequence:

`visible separation -> visible initiation -> readable contact -> receiver
reaction only after contact -> torso/shoulder displacement -> exactly one
rear-foot recovery placement -> early stabilization -> pressure release or
continued recovery motion -> no prolonged static contact tail`

### 5.2 Brief impact/recoil

Does the V0.3 brief-impact/recoil family compiler bundle repeatably improve
the visible impact/recoil chain compared with a matched baseline action Prompt
under the same calibration conditions?

Target sequence:

`visible separation -> compact initiation -> readable brief contact ->
immediate upper-body recoil -> exactly one rear-foot step -> prompt attacker
retract -> short stabilization or continued guard motion -> no prolonged push
-> no long static tail`

## 6. Fixed 2 x 2 x 2 Design

```yaml
action_families: 2
treatments_per_family: 2
replicates_per_cell: 2
phase1_task_count: 8
automatic_task_expansion: false
```

Exact tasks:

1. `CAL002-B05-PUSH-CONTROL-R01`
2. `CAL002-B05-PUSH-CONTROL-R02`
3. `CAL002-B05-PUSH-CANDIDATE-R01`
4. `CAL002-B05-PUSH-CANDIDATE-R02`
5. `CAL002-B05-IMPACT-CONTROL-R01`
6. `CAL002-B05-IMPACT-CONTROL-R02`
7. `CAL002-B05-IMPACT-CANDIDATE-R01`
8. `CAL002-B05-IMPACT-CANDIDATE-R02`

There is no ninth task. No tie-breaker is created, reserved, or authorized.

## 7. Fixed Provider Design Target

```yaml
task_type: text2video
model_version: seedance2.0_vip
duration: 5
ratio: 16:9
video_resolution: 720p
reference_strategy: text_only_no_active_generation_reference
active_generation_reference_count: 0
prompt_language: English
```

These are future design targets only. A later no-live package phase must
independently compare them with then-current runtime help.

## 8. Canonical Blueprint Layers

The manifest stores the canonical strings for these layers:

1. `SHARED_VISUAL_CONSTANT_BLOCK`
2. `SHARED_SAFETY_AND_CAMERA_BLOCK`
3. one `ACTION_FAMILY_CONTROL_BLOCK` or `ACTION_FAMILY_CANDIDATE_BLOCK`
4. `SHARED_COMPACT_NEGATIVE_BLOCK`
5. `REVIEW_CONTRACT_BLOCK`, which is review-only and excluded from provider
   Prompt assembly

Future provider Prompt assembly is deterministic:

```text
SHARED_VISUAL_CONSTANT_BLOCK

SHARED_SAFETY_AND_CAMERA_BLOCK

SELECTED_ACTION_FAMILY_TREATMENT_BLOCK

SHARED_COMPACT_NEGATIVE_BLOCK
<one final LF>
```

Encoding is UTF-8 without BOM. Block separators are exactly two LF bytes.
Replicate IDs and task IDs are excluded from future provider Prompt text.

The shared visual block describes:

- two adult professional stunt performers;
- controlled non-injury action rehearsal;
- semi-realistic cinematic action previs;
- neutral indoor rehearsal stage;
- plain matte gray floor and neutral rear wall;
- fixed dark-charcoal attacker and light-gray receiver clothing;
- no props, crowd, destruction, supernatural effects, text, or logos.

The shared camera and safety block fixes:

- locked camera;
- medium-wide full-body framing;
- three-quarter side view;
- both performers and both feet visible;
- moderate physical distance;
- clear lateral and depth separation;
- no cut, zoom, pan, orbit, or handheld shake;
- soft neutral studio lighting;
- no dramatic beam, strong motion blur, particles, or smoke.

## 9. Control Definitions

Control remains a matched high-level action baseline. It is not a no-action or
intentionally defective Prompt.

Push Control states one controlled two-hand push, receiver backward movement
and balance recovery, and safe readable action. It omits the complete
post-contact-only torso chain, exact one-foot contract, pressure-release
contract, static-tail control, and full audit-oriented result sequence.

Impact Control states one controlled forearm impact, receiver reaction and
backward step, and a safe finish. It omits the complete brief-contact,
immediate-recoil, exact one-foot, prompt-retract, prolonged-push, and
ending-duration contracts.

## 10. Candidate Family Bundles

### 10.1 Push candidate

```yaml
action_family: push_reaction
start_mode: separated
contact_type: compact_two_hand_push
contact_onset_visible: required
receiver_reaction_after_contact_only: required
receiver_body_result: torso_and_shoulders_shift_backward
foot_result_required: true
foot_result_count: 1
foot_result_type: rear_foot_recovery_placement
stabilization_target: early_window
pressure_release_required: true
prolonged_contact_forbidden: true
static_tail_forbidden: true
```

Temporal blueprint:

- `0.00-0.20s`: visible separated start and attacker initiation.
- `0.20-0.60s`: readable contact.
- `0.50-1.00s`: receiver torso and shoulders move backward after contact.
- `0.80-1.30s`: exactly one rear-foot recovery placement.
- `1.20-1.60s`: receiver stabilizes.
- After stabilization: attacker reduces pressure; both retain small
  recovery/guard motion; no unchanged contact pose for the remaining clip.

### 10.2 Brief-impact candidate

```yaml
action_family: brief_impact_recoil
start_mode: separated
contact_type: compact_forearm_impact
contact_duration: brief
contact_onset_visible: required
receiver_body_result: immediate_upper_body_recoil
foot_result_required: true
foot_result_count: 1
foot_result_type: rear_foot_step
attacker_retract_required: true
prolonged_push_forbidden: true
static_tail_forbidden: true
```

Temporal blueprint:

- `0.00-0.20s`: visible separated start and compact initiation.
- `0.20-0.55s`: brief forearm contact.
- `0.30-0.80s`: immediate upper-body recoil.
- `0.50-1.10s`: exactly one rear-foot step.
- `0.50-1.00s`: attacker promptly retracts.
- `1.00-1.50s`: short stabilization with breathing and guard motion; no
  prolonged push or long idle tail.

## 11. Treatment Isolation

The following are shared constants within and across action-family pairs:

- performers and clothing;
- scene, lighting, camera, framing, style, and duration target;
- provider design target and text-only reference strategy;
- safety framing, number of performers, and compact general negatives.

Action identity is semantically equivalent within each family. The only
systematic Control/Candidate difference is the action-family causal compiler
treatment.

```yaml
component_level_causal_attribution_permitted: false
treatment_unit: complete_action_family_compiler_bundle
```

The clause-level classification is in
`batch05_treatment_diff_matrix.json`.

## 12. Replicate Policy

R01 and R02 are future independent generations using byte-identical Prompt
text within their cell:

```text
PUSH-CONTROL-R01 = PUSH-CONTROL-R02
PUSH-CANDIDATE-R01 = PUSH-CANDIDATE-R02
IMPACT-CONTROL-R01 = IMPACT-CONTROL-R02
IMPACT-CANDIDATE-R01 = IMPACT-CANDIDATE-R02
```

No provider seed is invented. Replicates measure consistency under
uncontrolled provider variation; they do not establish statistical
significance.

```yaml
statistical_significance_claim_permitted: false
single_component_claim_permitted: false
cross_action_generalization_claim_permitted: false
```

## 13. Primary Endpoints

Push primary pass requires every item:

- first frame visibly separated;
- initiation before contact;
- readable contact onset;
- reaction only after contact;
- readable torso/shoulder backward displacement;
- exactly one rear-foot recovery placement after contact;
- stabilization and pressure reduction/release;
- no multi-step retreat, prolonged unchanged contact, or long static tail;
- action remains `push_reaction`.

Impact primary pass requires every item:

- first frame visibly separated;
- compact initiation and readable contact onset;
- brief contact;
- immediate upper-body recoil;
- exactly one rear-foot step after contact;
- prompt attacker retract;
- no prolonged push or long static tail;
- action remains `brief_impact_recoil`.

First-frame contact makes onset evaluation invalid for either family.

## 14. Secondary Review Schema

The structured schema records explicit enums for:

`first_frame_state`, `action_onset_visible`, `contact_onset_visible`,
`contact_duration_class`, `post_contact_reaction_visible`,
`torso_displacement_strength`, `upper_body_recoil_strength`,
`foot_result_count`, `foot_result_type`, `foot_result_after_contact`,
`attacker_release_or_retract`, `prolonged_contact`,
`static_tail_start_time`, `static_tail_duration`,
`ending_contract_satisfied`, `action_family_match`,
`identity_consistency`, `full_body_visibility`, `camera_compliance`,
`technical_validity`, and `overall_visual_usability`.

Per-video free-text notes are optional supporting evidence and never the sole
result field. A non-empty `reviewer_rationale` is required for every blind
pair judgment.

## 15. Blind Review

Complete MP4 review is mandatory. Contact sheets and synchronized comparisons
may assist but cannot replace complete-video review.

Reviewer-facing aliases:

- `PUSH_PAIR_01_A`, `PUSH_PAIR_01_B`
- `PUSH_PAIR_02_A`, `PUSH_PAIR_02_B`
- `IMPACT_PAIR_01_A`, `IMPACT_PAIR_01_B`
- `IMPACT_PAIR_02_A`, `IMPACT_PAIR_02_B`

Review uses two strictly separated stages.

### 15.1 Blind reviewer stage

The reviewer receives aliases and records only:

- `pair_id`;
- `comparison_validity`;
- A/B `preference`;
- a non-empty `reviewer_rationale`.

The blind reviewer does not record `candidate_clear_advantage` and must not
know Candidate/Control identity. The blind record is finalized and hashed
before treatment mapping is revealed.

The reviewer-facing package may contain only alias-labeled complete MP4 files,
alias-labeled technical metadata, alias-labeled review aids,
`batch05_visual_review_schema.json`, and a blank blind review record.
Review-facing media filenames must use blind aliases.

The reviewer package must exclude:

- `batch05_design_manifest.json`;
- `batch05_task_matrix.csv`;
- `batch05_treatment_diff_matrix.json`;
- `CAL002_BATCH05_DESIGN_SPEC.md`;
- `batch05_budget_and_authority_plan.json`;
- `batch05_post_unblinding_analysis_schema.json`;
- `batch05_design_evidence_manifest.json`;
- all design, audit, and fix reports;
- all package files containing treatment labels;
- every filename containing `CONTROL` or `CANDIDATE`.

This design rule does not create or authorize a review package.

### 15.2 Post-unblinding derived-analysis stage

Only after the blind record is finalized and its SHA-256 is recorded may the
sealed mapping in the design manifest and task matrix be revealed.
`batch05_post_unblinding_analysis_schema.json` then records:

- mapping-source path, byte-length, and SHA-256 bindings;
- Candidate and Control side derivation for each pair;
- derived `candidate_clear_advantage`;
- family-level decisions and non-empty rationales.

Candidate advantage is therefore derived after unblinding, never asserted by
the blind reviewer.

## 16. Phase-1 Decision Rules

| Condition | Family-level result |
| --- | --- |
| Candidate passes 2/2 and clearly outperforms Control in both replicate comparisons | `FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL` |
| Control passes 2/2 and Candidate passes 2/2 without clear Candidate advantage | `BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE` |
| Candidate passes 1/2 or replicate pair findings conflict | `INCONCLUSIVE_REPLICATION` |
| Candidate is worse than Control or repeatedly routes to the wrong family | `CANDIDATE_FAMILY_COMPILER_REGRESSION` |
| Both treatments frequently fail or uncontrolled variation prevents comparison | `ROUTE_RESET_REQUIRED` |

No extra task follows automatically. A tie-breaker requires a separate
no-live design and human decision.

## 17. Budget Design

Batch04 submit evidence records four observed unit costs:

```text
70, 70, 70, 70
```

```yaml
observed_minimum: 70
observed_maximum: 70
observed_mean: 70
observed_total: 280
planned_task_count: 8
provisional_phase1_base_estimate: 560
provisional_phase1_conservative_ceiling: 560
fresh_current_credit_checked: false
```

This estimate is not a current credit balance. A future live phase must run a
fresh `user_credit` canary and obtain a separate human budget decision.

## 18. Proposed Future Authority Boundary

```yaml
phase1_fixed_submit_max: 8
query_max: requires_separate_future_authorization
download_max: requires_separate_future_authorization
retry_max: 0
resubmit_max: 0
batch_retry_max: 0
automatic_task_expansion: false
tie_breaker_authorized: false
final_master: false
locked: false
```

This is a proposal for a later authorization phase, not active authority.

## 19. Current Boundaries

```yaml
Dreamina_called: false
provider_called: false
provider_command_count: 0
submit_authorized: false
query_authorized: false
download_authorized: false
retry_authorized: false
resubmit_authorized: false
batch_authorized: false
Prompt_package_created: false
media_created: false
review_artifacts_created: false
sources_changed: false
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```

## 20. Next Phase

`CAL002_BATCH05_DESIGN_TARGETED_FIX_INDEPENDENT_NO_LIVE_AUDIT`

The next phase may independently re-audit only the bounded blind-review schema
fix. It creates no live authority.
