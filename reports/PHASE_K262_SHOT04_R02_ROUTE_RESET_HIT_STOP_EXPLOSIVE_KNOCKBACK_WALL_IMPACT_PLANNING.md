# PHASE K262 - SHOT-04 R02 Route Reset: Hit-Stop, Explosive Knockback, Wall Impact Planning

## 1. Phase Summary

K262 is a report-only route reset planning phase for SHOT-04 R02.

K261 determined that the K260 `CUT_A` and `CUT_B` candidates should not continue as primary or edit candidates. They improved identity evidence, but the action still reads as sustained push / pressure instead of the user's desired rhythm:

```text
brief contact hit-stop / slow impact moment -> immediate fast explosive knockback -> possible wall impact / wall hole / through-wall result
```

K262 compares route options and recommends the next no-submit planning/package direction. K262 is not a submit package and does not create any executable Dreamina package.

## 2. Authorization And Boundaries

Authorization level: report-only / planning-only.

Allowed:

- read existing reports and Source files as evidence
- create one standalone K262 markdown planning report under `reports/`
- stage, commit, and push only the K262 text report if validation passes

Forbidden in K262:

- no Dreamina
- no submit
- no query_result
- no download
- no retry
- no resubmit
- no batch
- no video cutting
- no frame extraction
- no contact sheet creation
- no media generation
- no new Dreamina prompt package
- no prompt txt files
- no package JSON files
- no manifest CSV files
- no K263 package
- no `sources/` modification, creation, deletion, rename, move, stage, commit, or push
- no `final_master=true`
- no `locked=true`
- no tag
- no media staging
- no `.vs/` staging
- no `productions/chi_yan_tian_qiong/edits/` staging
- no `reports/context_recovery/` staging
- no runtime/config/auth/session/token/key/env file access or edits

## 3. Git / Source Preflight

Commands run:

```powershell
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
git diff --name-only
git diff --cached --name-only
```

Result:

- branch status: `## main...origin/main`
- `sources/`: clean
- tracked working tree changes before K262: none
- staged files before K262: none
- known allowed untracked noise present:
  - `.vs/`
  - `reports/context_recovery/`
  - `productions/chi_yan_tian_qiong/edits/`

K262 was not blocked by dirty sources or unexpected tracked changes.

## 4. Evidence Read

Reports read:

- `reports/PHASE_K261_SHOT04_R02_IDENTITY_ANCHORED_M2V_CUT_VISUAL_REVIEW.md`
- `reports/PHASE_K260_SHOT04_R02_IDENTITY_ANCHORED_M2V_LOCAL_CUT_WINDOW_DIAGNOSTIC.md`
- `reports/PHASE_K259_SHOT04_R02_IDENTITY_ANCHORED_MULTIMODAL2VIDEO_VISUAL_REVIEW.md`
- `reports/PHASE_K258_SHOT04_R02_IDENTITY_ANCHORED_MULTIMODAL2VIDEO_REVIEW_ARTIFACTS_READY.md`
- `reports/PHASE_K257_SHOT04_R02_IDENTITY_ANCHORED_MULTIMODAL2VIDEO_DOWNLOAD_RESULT.md`

Read-only Source context inspected:

- `sources/AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_Source索引与使用优先级_V1.8.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`
- `sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`
- `sources/Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
- `sources/Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
- `sources/dreamina_cli_help_latest.md`

Source conclusions used:

- Codex may read Source but must not modify official `sources/`.
- Reports are evidence, not official Source.
- Submit, query, download, retry, resubmit, visual review, final, and lock are separate gates.
- Visual success does not automatically become final/lock.
- Visual action failure should be diagnosed and may require route reset rather than retry.
- High-risk action prompts need visible result-first action, contact/timing structure, and review criteria.
- Short hit-stop should be brief; sustained slow motion risks making action feel dragged.

## 5. K261 Route Reset Trigger

K261 recorded:

- best_cut: `none_for_primary`
- usable_as_edit_candidate: `no_or_very_limited`
- usable_as_SHOT04_R02_primary: `false`
- final_master: `false`
- locked: `false`

K261 failure classes:

- `desired_impact_timing_mismatch`
- `sustained_push_instead_of_hit_stop_burst`
- `insufficient_explosive_knockback`
- `insufficient_received_force_displacement`
- `current_no_wall_contact_constraint_conflicts_with_new_human_goal`
- `wet_floor_feedback_weak`

Route reset trigger:

The K255-K260 identity-anchored M2V route improved identity, but its usable motion remains the wrong action. CUT_A and CUT_B read as sustained pressure / pushing, not a brief hit-stop followed by fast displacement.

## 6. Human Creative Correction

human_review_summary:

- The cuts initially seemed to have some force.
- After repeated viewing, they did not satisfy the desired action.
- The current motion feels like Fenshou slowly pushing Shuangji.
- The desired feeling is "piu yi xia": a short hit moment and then immediate speed.

human_creative_correction:

- Fenshou may have a brief slow-motion / hit-stop at the strike impact.
- Immediately after that hit-stop, the action must burst fast.
- Shuangji should be knocked away suddenly.
- The next route may explicitly say Shuangji hits the wall, the wall breaks open / has a hole, or Shuangji is driven into or through the wall.

failure_type:

- timing failure
- impact causality failure
- received-force displacement failure
- old constraint conflict

next_route_implication:

The old no-wall-contact rule should no longer be the active creative target. It was useful when avoiding brittle wall contact, but it now blocks the user's desired wall-impact / wall-hole / through-wall result.

## 7. Current Route Stopped

Stopped route:

```text
near-wall guard-clash pressure without wall contact
```

Reason:

The route preserves some identity and character separation, but its action grammar is now misaligned with the creative direction. Continued edits of K260 CUT_A/CUT_B would likely optimize the wrong motion.

## 8. New Target Route

New target:

```text
hit-stop + explosive knockback / wall impact / wall hole / through-wall result
```

Target action grammar:

- contact begins already close or with minimal setup
- Fenshou's strike lands with a very brief hit-stop
- the hit-stop is short, not sustained slow motion
- Shuangji is displaced rapidly after contact
- wall impact / wall break / wall hole / through-wall aftermath is allowed
- the visual read must be decisive impact and launch, not slow pushing

High-level route prompt principles only:

- put the visible result first
- define hit-stop as momentary
- define immediate fast displacement after hit-stop
- make received-force displacement visible
- allow wall impact as the result, but do not overload one generation with every beat if split shots can carry it better

K262 does not create the K263 executable prompt, package, or manifest.

## 9. Option A Analysis: Identity-Anchored M2V Revision

Route:

```text
identity-anchored multimodal2video revision with explicit hit-stop + explosive wall impact
```

Strengths:

- Reuses the strongest identity gains from K255-K261.
- Keeps the proven active identity anchor strategy instead of returning to prompt-only identity.
- Can directly express the corrected action target in one route: hit-stop, fast knockback, and wall impact.
- May preserve continuity with existing SHOT-04 R02 visual direction.

Risks:

- High risk of repeating sustained push if the model interprets hit-stop / impact as continuous pressure.
- High risk of 5-second overload: identity + close contact + hit-stop + knockback + wall damage + continuity.
- Wall impact / wall hole may fight identity and character separation.
- One-shot package may produce technically impressive motion but still miss the exact "piu yi xia" timing.
- Reusing identity refs may again pull attention toward character preservation at the expense of action mechanics.

Identity gains from K255:

Useful. K255-K261 showed substantially improved identity and character separation compared with prompt-only routes. That gain should inform the next route, but it does not justify preserving the old action structure.

One-shot package assessment:

Not recommended as the default. It may be worth considering later if the user explicitly wants a single-shot attempt, but K262 should not default to another overloaded 5-second one-shot.

Priority:

Medium. Useful fallback or later route, but too risky as the immediate default.

## 10. Option B Analysis: First-Frame / Layout / Keyframe Route

Route:

```text
first-frame / layout / keyframe route for wall impact result
```

Strengths:

- Better suited to designing the wall-impact result as a clear still or aftermath state.
- Allows manual layout / compositing / storyboard keyframe planning before any Dreamina execution.
- Can make wall hole, broken wall panel, or through-wall aftermath visually explicit.
- Useful for SHOT-04-R02b, where the result is more important than continuous close-combat timing.

Risks:

- Still/keyframe routes have known brittleness for double-character close combat.
- A result frame may show aftermath but not the hit-stop-to-burst transition.
- If used for the whole action, it may return to static poster-like staging.
- Exact body-wall interaction remains brittle and may require manual layout or compositing.

Best use:

Better for `SHOT-04-R02b` wall impact aftermath than for the entire contact-to-impact action. This route can support the second shot after the contact/hit-stop shot has a stable action language.

Manual planning recommendation:

Before any Dreamina package, this option should use layout/storyboard planning to decide:

- wall side and impact point
- Shuangji's body direction after impact
- wall hole / broken panel shape
- whether Fenshou remains in frame or is implied by cut continuity

Priority:

Medium-high as support for R02b, but not best as a single-shot full-action solution.

## 11. Option C Analysis: Two-Shot Edit Route

Route:

```text
SHOT-04-R02a: contact / hit-stop
SHOT-04-R02b: fast knockback / wall impact aftermath
```

SHOT-04-R02a goal:

- brief contact
- impact freeze / hit-stop
- readable Fenshou strike
- readable Shuangji receiving force
- no long sustained push
- no slow dragging
- no wall destruction overload

SHOT-04-R02b goal:

- Shuangji rapidly displaced into wall
- wall hole / broken wall panel / through-wall aftermath
- clear consequence of the prior hit-stop
- no need to solve the same contact beat and identity setup in the same generation

Strengths:

- Best matches the desired "piu yi xia" dynamic contrast.
- Separates timing problems from wall-destruction problems.
- Reduces generation overload.
- Gives clearer visual review criteria for each sub-shot.
- Allows K263 to test only the contact / hit-stop language before committing to wall impact.
- Lets R02b use layout/keyframe planning if needed.

Risks:

- Requires edit continuity between R02a and R02b.
- Identity continuity must be tracked across two shots.
- If R02a overuses slow motion, the same sustained-push problem can reappear.
- If R02b over-focuses on wall damage, character readability may drop.

Why it better matches "piu yi xia":

The desired feeling is not a continuous pressure beat. It is a contrast beat: a tiny moment of impact suspension, then a sudden burst. Splitting the action lets one shot focus on the hit-stop and the next shot focus on fast displacement / wall impact.

K263 scope recommendation:

K263 should start with `SHOT-04-R02a contact / hit-stop no-submit package` first. R02a tests whether the new hit-stop/contact language avoids sustained push. R02b wall-impact planning should follow after R02a language is stable, unless the user explicitly wants both planned together.

Priority:

High. Recommended default.

## 12. Comparative Matrix

| Criterion | Option A: One-Shot Identity-Anchored M2V Revision | Option B: First-Frame / Layout / Keyframe | Option C: Two-Shot Edit Route |
|---|---|---|---|
| identity stability risk | Medium; can reuse K255 identity anchors, but action load may weaken identity | Medium-high for full action; better if used for R02b aftermath only | Medium; two shots require continuity, but each shot has lower action load |
| action timing risk | High; sustained push may repeat | High for full action, medium for aftermath-only | Lowest of the three; hit-stop and knockback are separated |
| wall impact risk | High; wall impact competes with identity and contact | Medium; result frame can clarify wall impact | Medium; R02b can focus on wall impact after R02a establishes cause |
| editability | Medium; one clip may still need trimming | Medium-high as result plate / aftermath | High; designed for editorial split |
| Source compliance | Medium; must avoid unauthorized package/submit and overclaiming | Medium; should remain planning/layout before execution | High; supports route reset and clear review gates |
| media generation complexity | High | Medium for R02b, high for full action | Lower per shot, higher project coordination |
| visual review clarity | Medium; too many goals in one output | Medium; clear result but weak transition | High; each sub-shot has narrower acceptance criteria |
| recommended priority | Medium | Medium-high as R02b support | High / default |

## 13. Recommended Default

Default recommendation:

```text
Prefer Option C: two-shot edit route
```

Reason:

One 5-second generation requiring identity stability, two-character contact, hit-stop, explosive knockback, wall destruction, and scene continuity is too high-risk. Two shorter shot goals are more likely to deliver the "piu yi xia" effect and make failure diagnosis cleaner.

## 14. Recommended Next Phase

Recommended next K phase:

```text
K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE
```

Reason:

Start with SHOT-04-R02a contact / hit-stop no-submit package first. R02a tests whether the hit-stop/contact can be made readable without reintroducing sustained push. R02b wall impact should follow only after R02a route language is stable, unless the user explicitly wants both planned together.

Allowed K263 scope if authorized later:

- no-submit package only
- selected route only
- explicit result-first hit-stop/contact language
- no submit/query/download unless separately authorized

K262 does not execute K263.

## 15. Explicit Non-Actions

K262 did not:

- run Dreamina
- submit
- query_result
- download
- retry
- resubmit
- batch
- create media
- cut video
- extract frames
- create contact sheets
- create prompt txt files
- create package JSON files
- create manifest CSV files
- create a K263 package
- modify `sources/`
- set final or lock

## 16. Safety Flags

- final_master: `false`
- locked: `false`
- no_submit: `true`
- no_query: `true`
- no_download: `true`
- no_retry: `true`
- no_resubmit: `true`
- no_source_change: `true`
- no_media_created: `true`

## 17. Final Verdict

`K262_ROUTE_RESET_PLANNING_READY_K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE`
