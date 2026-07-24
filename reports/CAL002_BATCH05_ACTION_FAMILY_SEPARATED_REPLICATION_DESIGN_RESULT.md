# CAL-002 Batch05 Action-Family-Separated Replication Design Result

## 1. Executive Decision

- Decision: `REVIEW_DERIVATION_INTEGRITY_FIX_APPLIED_PENDING_INDEPENDENT_AUDIT`
- Original design decision: `CAL002_BATCH05_DESIGN_READY_FOR_INDEPENDENT_NO_LIVE_AUDIT`
- Independent audit finding: `CAL002_BATCH05_DESIGN_NEEDS_FIX_BLIND_REVIEW_SCHEMA`
- Re-audit finding: `CAL002_BATCH05_TARGETED_FIX_NEEDS_SECOND_BOUNDED_SCHEMA_FIX`
- Goal identity: `CAL002_BATCH05_ACTION_FAMILY_SEPARATED_REPLICATION_DESIGN_V0_1`
- Task type: complete no-live experimental design
- Fixed Phase-1 tasks: `8`
- Provider execution authority created: `false`

## 2. Repository Preflight

- Repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- Branch: `main`
- Starting HEAD: `f23d9511c5b13c877a9773fe10d68d1772ca3be8`
- Locally recorded `origin/main`: `f23d9511c5b13c877a9773fe10d68d1772ca3be8`
- HEAD/origin aligned before write: `true`
- Tracked modifications before write: `0`
- Staged files before write: `0`
- `sources/` tracked or staged modifications before write: `0`
- Existing untracked evidence and media were left untouched.

## 3. Human-Confirmed Active Project Source State

```yaml
active_project_source_index: V1.13
active_prompt_compiler: V0.3
active_rolling_state: V0.1
active_by_current_human_instruction: true
embedded_candidate_status_text_stale: true
local_source_sync_authorized: false
```

Active names:

- `AI视频制作_Source索引与使用优先级_V1.13.md`
- `AI视频制作_Prompt编译器与结果优先动作语法_V0.3.md`
- `AI视频制作_当前项目状态与双轨切换_V0.1.md`

## 4. Stale Embedded Candidate-Status Note

The human explicitly confirmed that embedded candidate or pending-application
status text in the active Project Sources is stale and non-blocking. This
phase does not correct those labels and does not synchronize local
`sources/`.

`ACTION_RULE_V0.4` remains provisional experimental evidence:

```yaml
official_source_status: false
stable_general_rule: false
not_general_default: true
```

## 5. Batch04 Evidence Interpretation

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

Batch05 separates the next experiment into
`push_reaction_family_compiler_bundle_v0_3` and
`brief_impact_recoil_family_compiler_bundle_v0_3`. Neither compound family
bundle permits component-level attribution.

## 6. Exact Research Questions

Push: does the V0.3 push-reaction family compiler bundle repeatably improve a
visible contact-to-reaction-to-one-foot-recovery sequence over a matched
baseline?

Impact: does the V0.3 brief-impact/recoil family compiler bundle repeatably
improve a brief-contact-to-recoil-to-one-step-to-retract sequence over a
matched baseline?

## 7. Fixed 2 x 2 x 2 Design

- Action families: `2`
- Treatments per family: `2`
- Replicates per cell: `2`
- Phase-1 tasks: `8`
- Automatic expansion: `false`

## 8. Eight Exact Task Identities

1. `CAL002-B05-PUSH-CONTROL-R01`
2. `CAL002-B05-PUSH-CONTROL-R02`
3. `CAL002-B05-PUSH-CANDIDATE-R01`
4. `CAL002-B05-PUSH-CANDIDATE-R02`
5. `CAL002-B05-IMPACT-CONTROL-R01`
6. `CAL002-B05-IMPACT-CONTROL-R02`
7. `CAL002-B05-IMPACT-CANDIDATE-R01`
8. `CAL002-B05-IMPACT-CANDIDATE-R02`

No ninth task exists.

## 9. Standardized Calibration Scene

All tasks share two adult professional stunt performers in a controlled
non-injury rehearsal on a neutral indoor stage, matte gray floor, neutral
rear wall, fixed dark-charcoal attacker clothing, fixed light-gray receiver
clothing, semi-realistic cinematic action previs, soft neutral lighting, and
no props, crowd, destruction, supernatural effects, text, or logos.

Camera is locked, medium-wide full-body, three-quarter side view. Both
performers and both feet remain visible, with moderate distance and clear
lateral/depth separation. There are no cuts or camera moves.

## 10. Provider Target Fields

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

These are design targets, not current runtime claims.

## 11. Control Definitions

Push Control states a controlled two-hand push, receiver backward movement,
balance recovery, and safe readable action.

Impact Control states a controlled forearm impact, receiver reaction and
backward step, and a safe finish.

Controls are matched high-level baselines. They are not no-action or
intentionally defective Prompts, and they omit the complete Candidate family
compiler contracts.

## 12. Candidate Family Bundles

Push Candidate adds the complete separated-start, visible contact,
post-contact-only torso response, exactly-one rear-foot placement, early
stabilization, pressure-release, prolonged-contact prohibition, and
static-tail prohibition bundle.

Impact Candidate adds the complete separated-start, visible brief-contact,
immediate recoil, exactly-one rear-foot step, prompt retract, prolonged-push
prohibition, and static-tail prohibition bundle.

## 13. Clause-Level Treatment Difference

`batch05_treatment_diff_matrix.json` classifies clauses as:

- `shared_constant`
- `control_only`
- `candidate_only`
- `semantic_equivalent`
- `forbidden_difference`

The only allowed systematic difference is the action-family causal compiler
treatment. Performer, costume, scene, lighting, camera, framing, style,
provider target, duration, safety, reference strategy, and general negatives
are fixed.

## 14. Replicate Byte-Identity

R01 and R02 within each experimental cell use the same planned Prompt
blueprint bytes. Task IDs, replicate IDs, and blind aliases are metadata and
are excluded from future provider Prompt text. No seed is invented.

## 15. Primary Endpoints

Push pass requires visible separated first frame, visible initiation and
contact onset, reaction only after contact, torso/shoulder displacement,
exactly one rear-foot recovery placement, stabilization, pressure release,
and no multi-step retreat, prolonged contact, or long static tail.

Impact pass requires visible separated first frame, compact initiation,
readable brief contact, immediate recoil, exactly one rear-foot step, prompt
attacker retract, and no prolonged push or long static tail.

First-frame contact invalidates onset evaluation in either family.

## 16. Secondary Review Schema

`batch05_visual_review_schema.json` defines explicit enums for all requested
motion, foot-result, contact, ending, action-family, identity, camera,
technical-validity, and usability fields. Free-form notes are supplementary,
not the sole score.

## 17. Blind Review Plan

Eight reviewer-facing aliases are defined without treatment labels. Treatment
mapping is held in the design manifest and task matrix, separate from the
review-facing schema. Complete MP4 review is mandatory; contact sheets and
comparisons cannot replace it.

The second bounded no-live fix preserves the two-stage review boundary and
closes the remaining derivation-integrity gaps:

1. Blind schema V0.3 fixes all eight aliases and four pair IDs in exact order,
   binds each alias to its action family, and rejects inconsistent
   validity/preference combinations.
2. The finalized blind record uses strict deterministic UTF-8 JSON and is
   hashed from exact file bytes before unblinding.
3. `batch05_review_derivation.py` reads the committed manifest and task matrix
   from both the worktree and `HEAD`, rejects drift or mapping disagreement,
   and calculates mapping bindings itself.
4. Pair derivations are generated from the sealed blind values and verified
   Candidate/Control mapping. They are not manually authored.
5. Family counts, flags, decisions, and rationales are generated through one
   fixed precedence.
6. Verify mode re-derives the complete output and requires exact byte equality,
   blocking blind-record substitution, mapping substitution, contradictory
   pair outcomes, and contradictory family decisions.

The reviewer-facing package must contain only alias-labeled media, metadata,
review aids, the blind schema, and a blank blind record. It must exclude the
design manifest, task matrix, treatment diff, design specification, budget
plan, post-unblinding schema, evidence manifest, all design/audit/fix reports,
treatment-labeled package files, and filenames containing `CONTROL` or
`CANDIDATE`.

Targeted-fix invariants:

- Prompt blueprints unchanged: `true`
- Tasks unchanged: `true`
- Provider targets unchanged: `true`
- Budget unchanged: `true`
- Authority unchanged: `true`
- Exact blind identities enforced: `true`
- Blind validity/preference consistency enforced: `true`
- Deterministic committed-mapping verification added: `true`
- Manual post-unblinding authoring permitted: `false`
- Blind-record substitution blocked by verify mode: `true`
- Mapping substitution blocked by verify mode: `true`

## 18. Family-Level Decision Matrix

| Precedence | Condition | Decision |
| ---: | --- | --- |
| 1 | Both treatments pass `0/2`, or both pairs are invalid for uncontrolled variation | `ROUTE_RESET_REQUIRED` |
| 2 | Candidate repeatedly routes to the wrong family, or Candidate is worse than Control | `CANDIDATE_FAMILY_COMPILER_REGRESSION` |
| 3 | Candidate passes `2/2`, both pairs are valid, and Candidate wins `2/2` | `FAMILY_SPECIFIC_REPLICATED_POSITIVE_SIGNAL` |
| 4 | Both treatments pass `2/2`, both pairs are valid, and both show no clear advantage | `BOTH_TREATMENTS_SUCCESSFUL_NO_CLEAR_CANDIDATE_ADVANTAGE` |
| 5 | No higher-precedence rule applies | `INCONCLUSIVE_REPLICATION` |

No statistical-significance, single-component, or cross-action-generalization
claim is permitted.

## 19. Budget Estimate and Limitations

Batch04 submit evidence records `70, 70, 70, 70` credits:

- Observed minimum: `70`
- Observed maximum: `70`
- Observed mean: `70`
- Observed total: `280`
- Planned tasks: `8`
- Provisional Phase-1 base estimate: `560`
- Provisional conservative ceiling: `560`
- Fresh current credit checked: `false`

No historical balance is presented as current. Future live work requires a
fresh `user_credit` canary and separate human budget decision.

## 20. Proposed Future Authority Boundary

```yaml
phase1_fixed_submit_max: 8
query_max: requires_separate_future_authorization
download_max: requires_separate_future_authorization
retry_max: 0
resubmit_max: 0
batch_retry_max: 0
automatic_task_expansion: false
tie_breaker_authorized: false
```

This is proposed future scope, not active authority.

## 21. Explicit No-Live Statement

- Dreamina called: `false`
- Provider called: `false`
- Provider command count: `0`
- Submit/query/download/retry/resubmit/batch: `0`
- Login/checklogin/logout/relogin: `0`
- Live authority created: `false`

## 22. Explicit No-Source-Change Statement

- Local Source synchronization authorized: `false`
- Source files created or modified: `0`
- Source files staged: `0`
- `sources_changed=false`

## 23. Explicit No-Prompt-Package Statement

- Executable Prompt `.txt` files created: `0`
- Execution packages created: `0`
- Live manifests created: `0`
- Provider commands or scripts created: `0`
- Canonical authorization text created: `0`
- `Prompt_package_created=false`

## 24. Explicit No Automatic Tie-Breaker

- Automatic task expansion: `false`
- Tie-breaker created: `false`
- Tie-breaker reserved: `false`
- Tie-breaker authorized: `false`

Any tie-breaker requires a separate future no-live design and human decision.

## 25. Validation and Next Phase

- JSON strict parse: `PASS`
- JSON duplicate-key rejection: `PASS`
- JSON non-finite-value rejection: `PASS`
- JSON deterministic UTF-8/LF format: `PASS`
- CSV explicit headers and stable column order: `PASS`
- Task matrix row count: `8`
- Task identity uniqueness: `PASS`
- Replicate planned Prompt-byte identity: `PASS`
- Control/Candidate variable isolation: `PASS`
- Protected pre-existing snapshot: `PASS_UNCHANGED`
- Evidence manifest non-self artifact count: `11`
- Blind schema V0.3 exact identities: `PASS`
- Blind validity/preference combinations: `PASS`
- `candidate_clear_advantage` removed from blind record: `true`
- Pair rationale universally required: `true`
- Post-unblinding derived-analysis schema V0.2: `PASS`
- Deterministic derivation tool added: `true`
- Derive and verify modes tested: `PASS`
- Pair truth-table regression probes: `PASS`
- Blind-substitution regression probes: `PASS`
- Mapping-substitution regression probes: `PASS`
- Family-decision regression probes: `PASS`
- Deterministic byte-output regression probes: `PASS`
- Reviewer-package exclusions defined: `true`
- Prompt blueprints/tasks/budget/authority unchanged: `true`

Next phase:

`CAL002_BATCH05_REVIEW_DERIVATION_INTEGRITY_FIX_INDEPENDENT_NO_LIVE_AUDIT`

Final verdict:

`REVIEW_DERIVATION_INTEGRITY_FIX_APPLIED_PENDING_INDEPENDENT_AUDIT`

Safety state:

```yaml
production_approved: false
fixed_task_completion: false
final_master: false
locked: false
```
