# PHASE K269A - SHOT-04 R02a No-Submit Safe Variant Planning

## 1. Phase Summary

K269A is a no-submit package simplification and safe variant planning phase after repeated K266/K268 `multimodal2video` empty submit failures for:

- asset_id: `SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-001`
- shot_id: `SHOT-04-R02a`
- current package phase: `K263`
- current task_type: `multimodal2video`
- current model_version: `seedance2.0_vip`
- current duration: `5`
- current ratio: `16:9`
- current video_resolution: `720p`
- current active_refs_count: `2`

K269A does not run Dreamina, does not submit, does not query, does not download, does not create media, and does not create a live package. It analyzes safer no-submit variant routes and recommends the next planning/package phase.

No no-submit draft specs were created in K269A. This phase creates only this planning report.

## 2. Authorization And Boundaries

Authorization level:

- `L0/L2 no-submit planning only`
- no Dreamina
- no live operation
- no package execution

Allowed:

- read K268F/K268E/K268/K267X/K266R/K266F/K266/K265/K264/K263 reports
- read K263 prompt/package/manifest
- read `sources/` as read-only context
- compare safe route variants
- create one K269A planning report under `reports/`
- optionally create no-submit planning specs if clearly useful
- stage/commit/push only K269A planning outputs

Not authorized:

- Dreamina execution
- `dreamina version`
- `dreamina user_credit`
- Dreamina help
- submit
- query_result
- list_task
- download
- retry
- resubmit
- batch
- loop
- media creation
- local cutting
- frame extraction
- contact sheet creation
- official Source modification
- runtime/config/auth/session/token/key/env modification or printing
- signed URL printing
- media staging
- final
- lock
- visual success claim

Official Project Source files remain human-controlled. K269A reports are evidence/planning, not official Source.

## 3. Git / Source Preflight

Preflight commands run:

```text
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
git -c core.quotepath=false diff --name-only
git -c core.quotepath=false diff --cached --name-only
```

Observed branch state:

```text
## main...origin/main
?? .vs/
?? productions/chi_yan_tian_qiong/edits/
?? reports/context_recovery/
```

Preflight interpretation:

- `sources/` status output: empty
- tracked working tree diff: empty
- staged diff: empty
- known untracked workspace noise remained:
  - `.vs/`
  - `productions/chi_yan_tian_qiong/edits/`
  - `reports/context_recovery/`

K269A was not blocked by dirty sources or unrelated tracked/staged changes.

## 4. Files Read

Required evidence files read:

- `reports/PHASE_K268F_SHOT04_R02A_REPEAT_SUBMIT_FAILURE_ROUTE_DECISION.md`
- `reports/PHASE_K268E_SHOT04_R02A_SUBMIT_INVOCATION_AND_LOG_EVIDENCE.md`
- `reports/PHASE_K268_SHOT04_R02A_CONTACT_HIT_STOP_NEW_ONE_SUBMIT_RESULT.md`
- `reports/PHASE_K267X_SHOT04_R02A_NEW_ONE_SUBMIT_ATTEMPT_AUTHORIZATION_DECISION.md`
- `reports/PHASE_K266R_SHOT04_R02A_CONTACT_HIT_STOP_LOCAL_ARG_DIAGNOSTIC.md`
- `reports/PHASE_K266F_SHOT04_R02A_CONTACT_HIT_STOP_SUBMIT_FAILURE_TRIAGE.md`
- `reports/PHASE_K266_SHOT04_R02A_CONTACT_HIT_STOP_ONE_SUBMIT_RESULT.md`
- `reports/PHASE_K265_SHOT04_R02A_CONTACT_HIT_STOP_ONE_SUBMIT_AUTHORIZATION_DECISION.md`
- `reports/PHASE_K264_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE_REVIEW.md`
- `reports/PHASE_K263_SHOT04_R02A_CONTACT_HIT_STOP_NO_SUBMIT_PACKAGE.md`
- `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-001_multimodal2video_no_submit_prompt.txt`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A-contact-hit-stop/K263/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-001_package.json`
- `productions/chi_yan_tian_qiong/packages/SHOT-04-R02A-contact-hit-stop/K263/SHOT-04-R02A-V-CONTACT-HIT-STOP-M2V-001_manifest.csv`

K269A did not read or print token, cookie, session, auth, key, env, or signed URL contents.

## 5. K268F Carry-Forward

K268F repeated failure classification:

`repeated_dreamina_cli_multimodal2video_empty_failure`

Carry-forward facts:

- K266 and K268 both failed the same way.
- Both had exit code `1`.
- Both returned empty output.
- Neither returned parseable JSON.
- Neither returned `submit_id`, `logid`, `gen_status`, or submit `credit_count`.
- K268 used `powershell_argv_array`, reducing simple shell quoting suspicion.
- K268E confirmed external invocation and local file evidence were sane.
- Internal upload/provider/CLI boundary remains unresolved.
- Query/download are impossible without `submit_id`.
- Third blind submit of the same package is not the default.

K268F recommended:

`K269A_NO_SUBMIT_PACKAGE_SIMPLIFICATION_OR_SAFE_VARIANT_PLANNING`

## 6. Creative Goal Preservation

Creative goal to preserve for SHOT-04 R02a:

- Fenshou's compact strike lands into Shuangji's crossed guard at close range.
- Contact freezes for a split-second hit-stop.
- Shuangji begins to snap backward from received force.
- Motion reads as impact, not slow push.
- R02a is contact and brief hit-stop only.
- R02a is not full wall impact and not R02b wall destruction.

Planning principle:

- Preserve the contact/hit-stop/received-force intent.
- Reduce transport/internal submit risk before spending more live attempts.
- Keep identity quality as a priority, but do not let identity references force repeated failure on the same M2V upload path without a diagnostic alternative.

## 7. Current K263 Package Risk Assessment

Current K263 package facts:

- package_sha256: `8afc28b3ca323875c18309dd8cfa58b7d1f714d5501bde1a87f896a158e83bf7`
- manifest_sha256: `f55633d51aeedd97d906968d7592e86e3bb23eec76d6ba6da853b7499803f100`
- prompt_sha256: `5dbc5943cf5d6964cdf1f3c7762fbd1775ae61c327a3fd4baa267fd4dcfc493b`
- prompt length: `2035` characters, `299` words
- manifest rows: `1`
- task_type: `multimodal2video`
- model_version: `seedance2.0_vip`
- duration: `5`
- ratio: `16:9`
- video_resolution: `720p`
- active_refs_count: `2`
- no_submit: `true`
- query_authorized: `false`
- download_authorized: `false`
- final_master: `false`
- locked: `false`

Current risk assessment:

- Structure reviewed as pass-with-high-risk in K264.
- No blocking local package/arg/path/hash issue was found in K266R.
- External invocation and file evidence were sane in K268E.
- The same M2V package family failed twice before task creation.
- The current prompt is moderately long and includes shell-sensitive punctuation.
- The two-ref M2V route may still be the best identity-preserving route, but it also keeps the suspected multimodal upload/provider boundary unchanged.

Planning implication:

Do not submit the same K263 package a third time by default. Plan variants that either simplify the same M2V boundary or bypass that boundary for diagnosis.

## 8. Variant A: Simplified Same-Two-Ref M2V

Route ID:

`VARIANT_A_SIMPLIFIED_TWO_REF_M2V`

Task type:

- `multimodal2video`

Refs used:

- `@FENSHOU_LOCKED_REF`
- `@SHUANGJI_LOCKED_REF`

Prompt changes:

- drastically shorten prompt
- remove quotes and semicolons if possible
- keep one result-first action sentence
- state only the contact, split-second hit-stop, and Shuangji snap-back
- avoid extra continuity, wall, rain, and complex timing text unless essential

What it tests:

- whether a simpler prompt can pass the same M2V two-image path
- whether prompt/content/internal parsing risk contributed to the empty submit failure

Risk it reduces:

- prompt length risk
- punctuation/quoting risk
- prompt content/safety ambiguity
- internal parsing complexity

Creative quality sacrificed:

- less detailed action timing control
- weaker environment/continuity context
- may still drift into generic clash or pose

Needs package creation:

- yes, in a later no-submit phase

Needs human authorization before submit:

- yes

Recommended priority:

- high for identity-preserving route
- high risk for repeated M2V boundary failure

## 9. Variant B: Single-Ref M2V Diagnostic

Route ID:

`VARIANT_B_SINGLE_REF_M2V_DIAGNOSTIC`

Task type:

- `multimodal2video`

Refs used:

- one image ref only
- preferred diagnostic choice depends on identity priority:
  - Fenshou ref if attacker silhouette/strike identity is the anchor
  - Shuangji ref if defender identity is more critical

Prompt changes:

- simpler prompt
- explicitly describe both characters in text
- keep result-first contact/hit-stop sentence
- avoid punctuation and complex timing layers

What it tests:

- whether two-image upload/ref handling contributes to failure
- whether a one-image M2V path behaves differently from two-image M2V

Risk it reduces:

- two-image upload/ref load
- reference attention conflict
- possible internal multimodal packaging complexity

Creative quality sacrificed:

- weaker dual-character identity control
- higher risk of identity drift for the unreferenced character
- less reliable close-contact staging

Needs package creation:

- yes, in a later no-submit phase

Needs human authorization before submit:

- yes

Recommended priority:

- medium
- useful as a diagnostic if the team wants to stay within M2V but reduce refs

## 10. Variant C: Text2Video Upload-Bypass Diagnostic

Route ID:

`VARIANT_C_TEXT2VIDEO_UPLOAD_BYPASS_DIAGNOSTIC`

Task type:

- `text2video`

Refs used:

- none

Prompt changes:

- prompt-only version of R02a action
- shorter than K263 prompt
- no quote/semicolon-heavy phrasing
- preserve contact, split-second hit-stop, Shuangji snap-back, impact-not-push
- explicitly state R02a only, no full wall impact

What it tests:

- whether bypassing local image upload avoids the empty submit failure
- whether the failure boundary is specific to M2V image upload/internal multimodal handling

Risk it reduces:

- local image upload path risk
- two-ref multimodal provider boundary
- ref file handling risk
- reference attention conflict

Creative quality sacrificed:

- identity control weaker
- Fenshou/Shuangji visual continuity weaker
- may produce less usable final footage, but valuable as a diagnostic/fallback

Needs package creation:

- yes, in a later no-submit phase

Needs human authorization before submit:

- yes

Recommended priority:

- high as diagnostic upload-bypass route
- medium as final creative route unless identity can be restored elsewhere

## 11. Variant D: Keyframe-Driven Route

Route ID:

`VARIANT_D_KEYFRAME_DRIVEN_ROUTE`

Task type:

- `image2video`, `frames2video`, or another keyframe-driven route only if appropriate source keyframes exist or are planned

Refs used:

- existing approved keyframe or first/last frame assets if available
- no active use in K269A

Prompt changes:

- action prompt would be tied to keyframe transition rather than all-around M2V refs
- may simplify text because staging comes from keyframe(s)

What it tests:

- whether keyframe-driven generation can preserve staging while avoiding M2V all-around ref failure

Risk it reduces:

- M2V multimodal all-around ref boundary
- two independent identity refs competing for attention

Creative quality sacrificed:

- requires additional keyframe assets
- may overfit to still pose
- may not capture explosive received-force onset without strong keyframe planning

Needs package creation:

- yes, and likely needs asset/keyframe planning first

Needs human authorization before submit:

- yes

Recommended priority:

- medium-low for immediate next step
- higher if no-submit planning finds usable keyframe assets

## 12. Variant E: Pause / Route Shift

Route ID:

`VARIANT_E_PAUSE_OR_ROUTE_SHIFT`

Task type:

- none in immediate K269A continuation

Refs used:

- none

Prompt changes:

- none immediately

What it tests:

- no technical test; it is a project route decision

Risk it reduces:

- prevents further live spend on a route with repeated empty submit failure
- avoids compounding evidence confusion

Creative quality sacrificed:

- pauses progress on R02a
- may delay action continuity work

Needs package creation:

- no

Needs human authorization before submit:

- yes, for any later live work

Recommended priority:

- medium as a fallback if human does not want more submit attempts soon

## 13. Comparative Decision Table

| Variant | Preserves R02a Creative Goal | Reduces M2V Upload Boundary Risk | Reduces Prompt/Punctuation Risk | Identity Strength | Diagnostic Value | Submit Later Requires Human Auth | Recommended Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A simplified same-two-ref M2V | high | low | high | high | medium | yes | high |
| B single-ref M2V diagnostic | medium | medium | high | medium-low | medium-high | yes | medium |
| C text2video upload-bypass | medium | high | high | low | high | yes | high |
| D keyframe-driven route | medium-high if assets exist | medium-high | medium | medium-high if keyframes are strong | medium | yes | medium-low now |
| E pause / route shift | none immediate | high | high | none immediate | low technical, high governance | yes for later work | medium fallback |

Decision reading:

- If identity preservation remains highest priority, Variant A is the most direct next no-submit package plan, but it still uses the same M2V upload/provider boundary.
- If diagnosing the repeated empty submit boundary is highest priority, Variant C is strongest because it bypasses image upload entirely.
- If balancing creative progress and diagnostic clarity, create a no-submit package set with both Variant A and Variant C, then let the human choose which route to authorize later.

## 14. Recommended Default Next Phase

Recommended default next phase:

`K269B_NO_SUBMIT_SAFE_VARIANT_PACKAGE_SET`

Recommended K269B scope:

- no Dreamina
- no submit
- no query
- no download
- no media creation
- create no-submit planning/package drafts for two variants:
  1. simplified same-two-ref M2V identity-preserving variant
  2. text2video upload-bypass diagnostic variant
- preserve R02a contact/hit-stop creative goal
- keep all submit/query/download authorization false
- require later human choice before any live attempt

Why not only Variant A:

Variant A best preserves identity, but it retains the same M2V image upload/provider boundary that failed twice.

Why not only Variant C:

Variant C best diagnoses upload-boundary risk, but it weakens identity continuity.

Why package set:

A two-variant no-submit package set lets the next human decision choose between identity-preserving retry strategy and upload-bypass diagnostic strategy with clear tradeoffs.

## 15. What Not To Do Next

Do not do next:

- no third same-package submit
- no query
- no download
- no retry
- no resubmit
- no final
- no lock
- no Source modification
- no live diagnostic without explicit authorization
- no automatic K270/K269 live submit
- no media generation

Reason:

K266 and K268 already failed before task creation. K268E showed local external invocation was sane. A third blind same-package submit would likely spend another attempt without isolating the failure boundary.

## 16. Explicit Non-Actions

K269A did not:

- run Dreamina
- run `dreamina version`
- run `dreamina user_credit`
- run Dreamina help
- submit
- query_result
- list_task
- download
- retry
- resubmit
- batch
- loop
- create local media
- cut video
- extract frames
- create contact sheets
- modify official `sources/`
- modify runtime/config/auth/session/token/key/env files
- print token/cookie/session/auth/env contents
- print signed URLs
- stage media
- set `final_master=true`
- set `locked=true`
- tag
- claim visual success
- create no-submit draft specs
- modify K263 prompt/package/manifest

## 17. Safety Flags

- final_master: `false`
- locked: `false`
- visual_success_claimed: `false`
- k269a_dreamina_run: `false`
- k269a_submit_run: `false`
- k269a_query_run: `false`
- k269a_download_run: `false`
- k269a_retry_run: `false`
- k269a_resubmit_run: `false`
- k269a_batch_run: `false`
- k269a_media_created: `false`
- sources_modified: `false`
- prompt_modified: `false`
- package_modified: `false`
- manifest_modified: `false`
- no_submit_draft_specs_created: `false`

## 18. Final Verdict

`K269A_NO_SUBMIT_SAFE_VARIANT_PLANNING_COMPLETE_READY_K269B_NO_SUBMIT_SAFE_VARIANT_PACKAGE_SET`
