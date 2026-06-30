# PHASE K251R - SHOT-04 R02 Identity-Lock Correction and Route Decision

## 1. Purpose

Record the human correction that the K245/K250 SHOT-04 R02 near-wall guard-clash text2video result does not have stable enough character identity for primary or final use.

This report also records the route decision after K249/K250:

- upgrade the identity issue from a weak/partial note to a primary-blocking issue;
- downgrade CUT_A and CUT_B from possible edit candidates to diagnostic / motion evidence only unless later explicitly reviewed;
- stop advancing the K245/K250 prompt-only output as a production candidate;
- recommend K252 identity-anchored near-wall guard-clash video-first planning/package route.

## 2. Human Correction Context

The human noticed that character identity is not fixed enough.

This correction changes the interpretation of K245/K249/K250 from:

- partial motion probe success with weak identity note;

to:

- partial motion probe success, but identity-blocked and not primary.

This is a report-only correction. It does not create new media, run Dreamina, create a package, mark final, or lock.

## 3. ChatGPT Module Recommendation

- Current ChatGPT module for reviewing this Codex K251R report: ChatGPT Think
- K249 visual review module used: ChatGPT Pro
- K250 local cut diagnostic module: ChatGPT Think
- Recommended next module for K252 identity-anchored route planning: ChatGPT Think
- Recommended module for future visual review after new media exists: ChatGPT Pro
- Pro Extended needed now: false
- Reason: K251R is a report-only correction and route decision record. It is not Source synthesis or macro-pipeline redesign.

## 4. Boundaries

- No Dreamina command was run.
- No submit was run.
- No query was run.
- No download was run.
- No retry or resubmit was run.
- No batch execution was run.
- No media was created.
- No video was cut.
- No frames were extracted.
- No contact sheets were created.
- No `sources/` files were modified.
- No prompt txt files were modified.
- No package JSON files were modified.
- No manifest CSV files were modified.
- No shot records were modified.
- No runtime/config/auth/session/token/key/env files were modified or printed.
- No media, cut candidate MP4 files, review artifacts, or artifact index JSON were staged.
- `final_master=false`.
- `locked=false`.
- `visual_success_claimed=false`.
- No final approval is claimed.

## 5. Git / Source Preflight

Commands run:

```powershell
git -c core.quotepath=false status --short --branch
git -c core.quotepath=false status --short -- sources/
```

Result:

- branch status: `## main...origin/main`
- `sources/`: clean
- known allowed workspace noise present:
  - `.vs/`
  - `reports/context_recovery/`
  - `productions/chi_yan_tian_qiong/edits/shot04_r02_near_wall_guard_clash_cut_candidates/K250/`

K251R was not blocked by dirty sources.

## 6. K247 / K248 / K249 / K250 Lineage

Read:

- `reports/PHASE_K247_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_DOWNLOAD_RESULT.md`
- `reports/PHASE_K248_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_REVIEW_ARTIFACTS_READY.md`
- `reports/PHASE_K249_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_VISUAL_REVIEW.md`
- `reports/PHASE_K250_SHOT04_R02_NEAR_WALL_GUARD_CLASH_LOCAL_CUT_WINDOW_DIAGNOSTIC.md`
- `sources/AI视频制作_Source索引与使用优先级_V1.8.md`
- `sources/AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `sources/AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
- `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md`
- `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md`
- `sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md`

Verified:

- submit_id: `37d02a39-7ca3-4141-b5ce-3e578622843e`
- video sha256: `04d89796348c9915f583318ef189c13ed1aee3b73b7c242e686497ce61c32418`
- K249 visual_status: `partial_motion_probe_success_but_not_primary`
- K249 usable_as_SHOT04_R02_primary: `false`
- K249 usable_as_edit_candidate: `limited`
- K249 failure category included identity_lock: `weak`
- K250 created CUT_A and CUT_B as diagnostic artifacts only
- K250 final_master: `false`
- K250 locked: `false`

## 7. Corrected Identity Status

Human correction:

The character identity is not fixed enough.

Corrected identity status:

- identity_lock: `failed_for_primary`
- identity_acceptable_for_motion_probe: `limited_or_barely`
- identity_acceptable_for_final: `false`
- identity_acceptable_for_primary: `false`
- character_fixed: `false`

This upgrades identity from a weak/partial note to a primary-blocking issue.

## 8. Corrected Usability Decision

Corrected overall status:

- visual_status_corrected: `partial_motion_probe_success_but_identity_blocked_and_not_primary`
- usable_as_SHOT04_R02_primary: `false`
- usable_as_final: `false`
- usable_as_locked: `false`
- usable_as_edit_candidate: `diagnostic_only_or_limited_pending_future_review`
- usable_as_motion_probe_evidence: `true`
- usable_as_failure_evidence: `true`
- final_master: `false`
- locked: `false`

## 9. CUT_A / CUT_B Decision

- Do not proceed to K251 Pro cut review as a primary/edit-candidate decision at this time.
- CUT_A and CUT_B remain untracked local diagnostic artifacts.
- CUT_A and CUT_B may be reviewed later only as motion grammar / micro-insert evidence if the human explicitly requests.
- CUT_A and CUT_B should not be treated as official SHOT-04 R02 edit candidates while identity is not fixed.
- CUT_A and CUT_B are not final, not locked, and not approved.

## 10. Main Interpretation

K245/K250 proves that prompt-only text2video can produce near-wall two-character guard-clash-like motion, but prompt-only `active_refs_count=0` is insufficient for stable character identity.

This is not:

- a remote generation failure;
- a CLI failure;
- a package failure;
- a Source sync failure.

It is a combined visual action-quality plus identity-lock failure for primary production use.

## 11. Route Decision

Stop advancing the K245/K250 prompt-only output as a production candidate.

Use the K245/K250 output as:

- motion evidence;
- failure evidence;
- route-learning evidence.

Do not use it as:

- SHOT-04 R02 primary;
- final candidate;
- locked media;
- official edit candidate while identity remains unfixed.

## 12. K252 Route Options

### Option A - Identity-Anchored Multimodal2Video No-Submit Package

Uses Fenshou identity ref plus Shuangji identity ref plus optional scene/wall ref with strict reference duties.

Pros:

- better identity control than prompt-only text2video.

Risks:

- reference attention conflict;
- action weakening;
- possible upload/remote risk.

### Option B - Manual Layout / Keyframe Route Then Image2Video Or Frames2Video

Pros:

- strongest identity/pose/control if layout succeeds.

Risks:

- previous still/keyframe routes had remote final-generation failures;
- dual-character staging remains brittle.

### Option C - Action-Reference-Library-First Route

Pros:

- may improve body mechanics, timing, pressure, and wet-floor feedback.

Risks:

- slower;
- does not itself solve identity unless combined with identity refs.

## 13. Recommended Default K252 Route

Recommended next phase:

`K252_IDENTITY_ANCHORED_NEAR_WALL_GUARD_CLASH_ROUTE_PLANNING_NO_SUBMIT`

Recommended default route:

Option A first, as no-submit planning/package review only, not live submit.

K252 preferred direction:

Plan a new identity-anchored video-first route, likely using a no-submit `multimodal2video` or other identity-reference-capable package, while preserving lessons from K245:

- keep first frame already close;
- keep no body-wall contact;
- keep no wall hit / no wall damage;
- preserve near-wall pressure and crossed guard;
- add identity reference strategy for Fenshou and Shuangji;
- avoid reference attention conflict;
- keep action P0 result first;
- preserve one-submit-only future boundary.

If K252 package review finds identity refs likely to overpower action or reintroduce old failures, route to Option B or Option C.

## 14. Final / Lock Status

- final_master: `false`
- locked: `false`
- visual_success_claimed: `false`
- final approval claimed: false

## 15. Final Verdict

`K251R_IDENTITY_LOCK_CORRECTION_RECORDED_READY_K252_IDENTITY_ANCHORED_ROUTE_PLANNING`
