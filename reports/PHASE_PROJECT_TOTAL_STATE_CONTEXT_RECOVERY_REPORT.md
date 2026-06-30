# PHASE_PROJECT_TOTAL_STATE_CONTEXT_RECOVERY_REPORT

## 1. Executive Summary

This is a repo-inspection context recovery report for `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`.

The repository began as a clean Python skeleton for an AI video production pipeline, but the current working project is now also a large operational evidence repository for the `chi_yan_tian_qiong` AI-video production. It contains:

- Python pipeline code under `app/ai_video_pipeline/`.
- Official human-controlled Source files under `sources/`.
- Production assets, prompts, packages, manifests, shot records, live runs, review artifacts, and edit diagnostics under `productions/chi_yan_tian_qiong/`.
- Hundreds of phase reports under `reports/`, especially K-phase reports documenting Dreamina execution, package review, visual review, failure diagnosis, and route decisions.

Current important production state:

- SHOT-04 R02 has not reached final approval.
- `final_master=false` and `locked=false` remain the correct state.
- The latest route decision is K262: stop the sustained near-wall guard-clash / sustained-push route and move toward a hit-stop plus explosive knockback / wall-impact two-shot route.
- The recommended next phase is `K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE`.

This report is not official Source, not a package, not a prompt, not a manifest, not a shot record, not media, not a Dreamina execution phase, not visual approval, not final, and not locked.

## 2. Repo Structure Map

Top-level directories observed:

| Path | Current role |
|---|---|
| `.agents/` | Agent-side workspace support; no production authority inferred. |
| `.agent_tmp_home/` | Temporary agent home data. |
| `.benchmarks/` | Benchmark placeholder or support directory. |
| `.codex/` | Codex-side project support. |
| `.pytest_cache/` | Test cache. |
| `.vs/` | Visual Studio workspace noise; should not be staged for these phases. |
| `app/` | Python application package and pipeline modules. |
| `configs/` | Runtime defaults, provider config, and path-policy config. |
| `docs/` | Documentation placeholder area. |
| `live_outputs/` | Live-output holding area. |
| `manual_imports/` | Manual import holding area. |
| `manual_tests/` | Manual test area. |
| `mock_outputs/` | Mock execution output area. |
| `productions/` | Main production workspace, including `chi_yan_tian_qiong`. |
| `reports/` | Phase reports, evidence packs, recovery reports, reviews, and route decisions. |
| `sources/` | Official Project Source files; human-controlled. |
| `staging/` | Internal staging area. |
| `tests/` | Python test suite. |

Current file-count snapshot from repo inspection:

| Directory | File count |
|---|---:|
| `app/` | 105 |
| `configs/` | 4 |
| `productions/` | 1070 |
| `reports/` | 367 |
| `sources/` | 24 |
| `staging/` | 12 |
| `tests/` | 75 |

The README and `PROJECT_STATUS.md` still describe the early Phase A skeleton. They are historically accurate for the original codebase but no longer describe the full operational state of the AI-video production workflow.

## 3. Source Status

`sources/` is the official human-controlled knowledge base. Codex may read these files, generate evidence and candidate updates, and prepare upload lists, but must not directly modify official Source files unless the human explicitly changes that governance model.

Source governance observed:

- Official Source updates are controlled by the human user.
- Codex-generated candidate Source updates are evidence only until reviewed and accepted by the human / ChatGPT Pro Extended.
- Source files should not be created, edited, deleted, renamed, moved, staged, committed, or pushed by Codex during ordinary production phases.

Key Source categories currently present:

- Source index and priority:
  - `AI视频制作_Source索引与使用优先级_V1.8.md`
- Automation and authorization:
  - `AI视频制作_自动化治理与Source权限规则_V0.1.md`
  - `AI视频制作_自动化宏流程与授权等级_V0.2.md`
- Prompt/action rules:
  - `AI视频制作_Prompt编译器与结果优先动作语法_V0.2.md`
  - `AI视频制作_动作参考视频库与审片标准_V0.1.md`
- Empirical rule library:
  - `AI视频制作_实测规则库_V1.1.md` through later focused addenda, including V1.12 failure-ledger and route-reset rules.
- Dreamina CLI contracts and help:
  - `dreamina_cli_help_latest.md`
  - `Dreamina_CLI工作流与执行规范_V1.1_官方Help校正版.md`
  - `Dreamina_CLI执行契约_V1.2_命令预检与网页CLI差异补丁.md`
  - `Dreamina_CLI执行契约_V1.3_Agent环境登录态日志与Canary补丁.md`
  - `DreaminaBatcher_manifest_schema_V1.1_官方Help校正版.md`
- Seedance / video-production manuals:
  - `Seedance2_AI视频制作综合使用手册_V0.3_三层描述增强版.md`

Source priority principles relevant to the current project:

- Human approval is required for final/lock.
- Submit, query, download, retry, resubmit, review, final, and lock are separate gates.
- Download success is not visual success.
- Visual success is not final approval.
- Repeated structurally meaningful failures should trigger route reset rather than blind retry.

Current preflight status for this report:

- `sources/` is clean.
- No Source file was modified for this report.

## 4. Reports / K-Phase History

Reports are the operational ledger for the project. Current report inventory:

| Report group | Count |
|---|---:|
| Total files directly under `reports/` | 367 |
| `PHASE_K*` files | 268 |
| SHOT-02-related report files | 97 |
| SHOT-03-related report files | 80 |
| SHOT-04-related report files | 90 |
| K245-K262 recent SHOT-04 R02 chain | 18 |

Major report history by project maturity:

- Early phases A-J established the Python pipeline skeleton, path policy, manifest parsing, Dreamina command construction, mock/live provider boundaries, and test scaffolding.
- SHOT-01 and SHOT-02 phases exercised keyframe/video workflows, package records, live execution boundaries, review artifacts, and cut/lock planning.
- SHOT-03 phases expanded route experimentation and video-record handling.
- SHOT-04 phases, especially K185-K262, form the densest current evidence chain around a difficult two-character close-combat action.
- K244S created a dedicated SHOT-04 R02 failure ledger and macro-run lessons evidence pack for ChatGPT Pro Extended synthesis.

Recent repo history shows the project is actively recording a high-granularity operational trail:

- K245 text2video submit
- K246 query result
- K247 download
- K248 local review artifacts
- K249 visual review
- K250 cut-window diagnostic
- K251 identity correction / route decision
- K252 identity-anchored route planning
- K253 no-submit M2V package
- K254 independent package review
- K255 M2V submit
- K256 query result
- K257 download
- K258 review artifacts
- K259 visual review
- K260 cut-window diagnostic
- K261 cut visual review
- K262 route reset planning

## 5. Current Chi Yan Tian Qiong Production State

Primary production root:

`productions/chi_yan_tian_qiong/`

Observed file-extension counts:

| Extension | Count |
|---|---:|
| `.csv` | 225 |
| `.jpg` | 282 |
| `.json` | 210 |
| `.md` | 38 |
| `.mp4` | 82 |
| `.png` | 92 |
| `.txt` | 80 |

Observed subdirectory counts:

| Subdirectory | File count |
|---|---:|
| `assets/` | 3 |
| `derived_refs/` | 14 |
| `edits/` | 86 |
| `exports/` | 1 |
| `locked_refs/` | 7 |
| `manifests/` | 59 |
| `packages/` | 8 |
| `plans/` | 8 |
| `prompts/` | 111 |
| `review_artifacts/` | 13 |
| `reviews/` | 267 |
| `runs/` | 430 |
| `shots/` | 40 |
| `working_refs/` | 6 |

Important interpretation:

- `productions/chi_yan_tian_qiong/` is not just output storage. It is an operational state store for packages, prompts, manifests, shot records, review evidence, run evidence, and edit diagnostics.
- `productions/chi_yan_tian_qiong/edits/` currently contains untracked or locally generated diagnostic material and should not be staged by unrelated report phases.
- The current production is still iterative. The most important active unit is SHOT-04 R02, but the repo contains broader SHOT-01, SHOT-02, and SHOT-03 history.

## 6. SHOT-04 R02 State

SHOT-04 R02 has gone through multiple route families:

- Wall-impact multimodal2video routes.
- Upload-safe multimodal2video variants.
- Four-reference and three-reference image2image keyframe routes.
- Softened text2image routes.
- Near-wall guard-clash text2image routes.
- Near-wall guard-clash text2video routes.
- Identity-anchored multimodal2video routes.
- Local cut-window diagnostics and human visual review.
- Latest route reset toward hit-stop plus explosive knockback / wall-impact split-shot planning.

Key consolidated evidence:

- K244S classified repeated remote final-generation failures and visual-action failures.
- Text2image/keyframe routes were brittle for dual-character close-combat/contact staging.
- Video routes could produce media, but media existence did not mean the action was correct.
- Identity anchoring improved character identity and separation in K255-K259, but the motion still read as sustained push rather than the user's desired brief hit-stop plus immediate explosive displacement.

Most recent concrete chain:

- K253 created the identity-anchored multimodal2video no-submit package.
- K254 independently reviewed the package and preserved high-risk notes.
- K255 submitted exactly once and recorded submit evidence.
- K256 queried once and recorded `gen_status=success` with a download URL present, without downloading.
- K257 downloaded the video only after authorization.
- K258 created local review artifacts.
- K259 recorded visual review: improved identity and motion candidate, but not final and not locked.
- K260 created local diagnostic cut candidates from the downloaded video.
- K261 recorded that no cut should become primary; the action remained a sustained push rather than the desired hit-stop / burst.
- K262 performed report-only route reset planning and recommended a two-shot edit route.

K255/K257 important media evidence:

- K255 submit id: `87226743-d3c0-4a0a-afd5-6ded908766cf`
- K255 logid: `202606301938451692540470086982151`
- K257 downloaded video:
  - `productions/chi_yan_tian_qiong/runs/live/SHOT-04-R02_identity_anchored_near_wall_guard_clash_m2v_K255_20260630_193845/87226743-d3c0-4a0a-afd5-6ded908766cf_video_1.mp4`
  - SHA256: `95d8a4951d87a3cdb5254f3c5b18baefd4bbf43b000c41c28a78fa1b24675c69`
  - 1280x720
  - about 5.0167 seconds
  - about 24.1196 fps
  - 121 frames

K260 diagnostic cuts:

- CUT_A:
  - `productions/chi_yan_tian_qiong/edits/shot04_r02_identity_anchored_m2v_cut_candidates/K260/SHOT-04-R02-K260_CUT_A_0p35_1p50_identity_anchored_primary_diagnostic.mp4`
  - SHA256: `1a2aa1aa0a29f967f018b46637a168cb22ae64635ca249cf37ee0811987373fa`
  - about 1.1609 seconds
- CUT_B:
  - `productions/chi_yan_tian_qiong/edits/shot04_r02_identity_anchored_m2v_cut_candidates/K260/SHOT-04-R02-K260_CUT_B_0p65_2p00_stronger_pressure_wall_risk_diagnostic.mp4`
  - SHA256: `397154ef543d3fa9ea0e90a485e05290b41f46611be0da61840c8175cf92a0f4`
  - about 1.3267 seconds

K261 result:

- best cut: none for primary
- usable as edit candidate: no or very limited
- usable as SHOT-04 R02 primary: false
- final_master: false
- locked: false

K262 recommendation:

`K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE`

Recommended route:

- Split SHOT-04 R02 into R02a and R02b.
- R02a focuses on contact / brief hit-stop.
- R02b focuses on fast knockback / wall impact aftermath.
- Avoid making one generation solve identity, contact, hit-stop, explosive displacement, wall destruction, and continuity all at once.

## 7. Automation / Tooling Inventory

The Python package is under:

`app/ai_video_pipeline/`

Major module areas:

| Area | Representative files | Role |
|---|---|---|
| Assets | `assets/media_integrity.py`, `assets/registry.py`, `assets/staging.py` | Media checks, asset registry, staging helpers. |
| Core | `core/manifest.py`, `core/manifest_discovery.py`, `core/manifest_writer.py`, `core/models.py`, `core/validation.py` | Manifest parsing/writing/discovery, domain models, validation. |
| Execution | `execution/runner.py`, `execution/run_plan.py`, `execution/task_compiler.py`, `execution/job_store.py`, `execution/recorder.py`, `execution/resume.py` | Run planning, task compilation, execution recording, resume logic. |
| Dreamina execution helpers | `execution/dreamina_f4_live.py`, `dreamina_f6_live.py`, `dreamina_g2_live.py`, `dreamina_h2_live.py`, `dreamina_h2_query_existing.py`, `dreamina_h4_live.py` | Phase-specific Dreamina live/query helpers. |
| Providers | `providers/dreamina_cli.py`, `providers/dreamina_preflight.py`, `providers/fake_live_provider.py`, `providers/stubs.py` | CLI provider layer and preflight support. |
| Prompts | `prompts/prompt_factory.py`, `prompts/prompt_record.py`, `prompts/prompt_validation.py`, `prompts/reference_roles.py`, `prompts/negative_rules.py` | Prompt generation, prompt records, role handling, negative rule logic. |
| Review | `review/review_lock.py` | Review/lock support. |
| Shots | `shots/shot_registry.py`, `shots/interfaces.py` | Shot registry interfaces. |
| Path policy | `path_policy/policy.py` | Workspace path policy. |
| Storage | `storage/fs_plan.py` | Filesystem plan handling. |
| Story/script | `story/interfaces.py`, `script/interfaces.py` | Higher-level interfaces. |
| Tools | `tools/path_scan.py` | Repo/path inspection helper. |

Tests exist under `tests/`, including phase-focused test files and fixtures for manifests, media, registries, and shot prompts.

Important caution:

- Tooling supports many operations, but live Dreamina submit/query/download must remain gated by human authorization and phase-specific contracts.
- This report did not run tests, Dreamina, media processing, or live tooling.

## 8. Dreamina Execution Artifacts

Dreamina-related evidence appears in three places:

- Source files documenting CLI contracts and help.
- Python provider / execution modules.
- Phase reports and production run folders recording actual submit/query/download outcomes.

Important current contract rules:

- Run canary/preflight only when a phase authorizes Dreamina command use.
- Do not print secrets, tokens, auth/session values, or env contents.
- Do not query unless the phase authorizes query.
- Do not download unless the phase authorizes download.
- Do not retry/resubmit unless the human explicitly authorizes that action as a separate phase.
- Do not treat `submit_id` alone as success.
- Do not treat `download_url_present=true` as visual success.
- Do not treat downloaded media as final.

For this report:

- Dreamina was not run.
- No submit/query/download/retry/resubmit/batch occurred.
- No media was created, cut, extracted, or contacted-sheeted.

## 9. Package / Manifest / Prompt Structure

Production package and prompt evidence is spread across:

- `productions/chi_yan_tian_qiong/prompts/`
- `productions/chi_yan_tian_qiong/packages/`
- `productions/chi_yan_tian_qiong/manifests/`
- `productions/chi_yan_tian_qiong/runs/`
- `productions/chi_yan_tian_qiong/reviews/`
- `reports/`

Relevant SHOT-04 R02 package/prompt family examples:

- `shot_04_r02_kf_micro_impact_001_image2image_package_no_submit.json`
- `shot_04_r02_kf_micro_impact_001_r02_3ref_image2image_package_no_submit.json`
- `shot_04_r02_kf_soft_contact_t2i_001_text2image_package_no_submit.json`
- `shot_04_r02_kf_near_wall_guard_clash_t2i_001_text2image_package_no_submit.json`
- `shot_04_r02_v_near_wall_guard_clash_t2v_001_text2video_package_no_submit.json`
- `shot_04_r02_wall_panel_shoulder_check_rebound_package_no_submit.json`
- `SHOT-04-R02-identity-anchored-near-wall-guard-clash/K253/SHOT-04-R02-V-IDENTITY-ANCHORED-NEAR-WALL-GUARD-CLASH-M2V-001_package.json`

Package lifecycle pattern:

1. No-submit package creation.
2. Independent package review.
3. Human authorization decision.
4. One-submit-only phase, if authorized.
5. Query-only phase, if authorized.
6. Download-only phase, if authorized.
7. Review artifact creation.
8. Human / ChatGPT visual review.
9. Route decision, ledger update, or Source candidate update.

Important policy:

- Existing prompt txt, package JSON, and manifest CSV files should not be modified during report-only phases.
- Submit-ready packages should not be created unless explicitly authorized.

## 10. Review Workflow

Current review workflow is evidence-first and gate-separated:

- Codex creates packages, reports, and review artifacts only within explicit phase permissions.
- Human authorizes each live boundary.
- Human reviews images/videos by default, not prompts.
- Prompt review occurs after repeated failure, major route change, or explicit human request.
- ChatGPT Pro is used for visual review support.
- ChatGPT Pro Extended is used when the task becomes Source synthesis or macro-pipeline redesign.
- Codex records outcomes and route decisions as reports, but must not claim visual success without review evidence.

Review artifact pattern:

- Downloaded media is followed by local artifact generation only when authorized.
- Contact sheets, frame indexes, and local diagnostics support review but do not equal approval.
- Visual review records must preserve final/lock state separately.

Current SHOT-04 R02 review status:

- Identity improved in the K255 route.
- Action remained insufficient.
- K260 cut diagnostics did not rescue the route.
- K261/K262 moved from edit salvage to route reset planning.

## 11. Failure Ledger / Source Update Practices

K244S is the current consolidated failure-ledger and macro-run evidence pack for SHOT-04 R02.

K244S outputs include:

- `README_FOR_CHATGPT_PRO_EXTENDED.md`
- `SHOT04_R02_FAILURE_LEDGER.csv`
- `SHOT04_R02_FAILURE_LEDGER.md`
- `SHOT04_R02_SUCCESS_AND_PARTIAL_SUCCESS_LEDGER.md`
- `PROMPT_OUTCOME_DATASET.csv`
- `PROMPT_TEXT_ARCHIVE_AND_INDEX.md`
- `HUMAN_CHATGPT_CODEX_REVIEW_EXCERPTS.md`
- `ROOT_CAUSE_TAXONOMY.md`
- `MACRO_RUN_LESSONS_AND_ONE_CLICK_REQUIREMENTS.md`
- `SOURCE_UPDATE_CANDIDATES.md`
- `ACTION_REFERENCE_VIDEO_LIBRARY_PLAN.md`
- `CHATGPT_UPLOAD_LIST_FOR_SOURCE_SYNTHESIS.md`
- `reports/PHASE_K244S_SHOT04_R02_FAILURE_LEDGER_AND_MACRO_RUN_LESSONS_READY.md`

Important K244S practices:

- Evidence packs are not official Source.
- Candidate Source updates should be transformed by ChatGPT Pro Extended and approved/applied by the human.
- Repeated failure and partial success should periodically feed Source update candidates.
- Failure categories include package defects, source governance blocks, upload transport failures, remote final-generation failures, visual execution failures, prompt priority failures, reference attention conflict, dual-character close-combat brittleness, identity drift, and route-reset requirements.

Current route-reset lesson:

- When media exists but the core visual action fails, review artifacts and human/ChatGPT review should guide route reset.
- Reusing a route only because it improved identity can be wrong if the core action grammar is still misaligned.

## 12. Current Maturity Assessment

Pipeline maturity:

- The repo has a mature evidence discipline: phase reports, explicit boundaries, staged authorization, and final/lock separation.
- The codebase has strong skeleton coverage for manifests, path policy, provider abstraction, and execution records.
- The production workflow has operational maturity around package review, live execution gates, and artifact-based visual review.

Still immature or high-risk areas:

- One-click automation is not yet safe as unrestricted execution; it must remain gated orchestration.
- Source updates are still partly manual and evidence-driven, not automatically applied.
- SHOT-04 R02 remains creatively unresolved.
- Dual-character close combat near walls remains brittle.
- Identity and action mechanics compete for model attention.
- Wall contact, wall destruction, and received-force timing are high-risk if compressed into one generation.

Best current operating model:

- Keep phase gates narrow.
- Keep reports explicit.
- Keep live operations separate.
- Use no-submit packages and independent review before live execution.
- Use visual artifacts before route claims.
- Use Source synthesis only after evidence consolidation.

## 13. Open Questions For ChatGPT / Human

Project-level:

- Should the README / `PROJECT_STATUS.md` be updated later to reflect the operational K-phase production reality, or remain as the original code skeleton snapshot?
- Should report counts and phase indexes be consolidated into a machine-readable project status index?
- Should K244S-style evidence packs become a recurring pattern after every major route reset?

Source-level:

- Which K244S Source candidates should become official Source first?
- Should the Source index add this project-total report as a context-recovery entry?
- Should the macro-flow Source define standard phase names for submit/query/download/review/cut/route-reset?

SHOT-04 R02:

- Should K263 create only R02a contact/hit-stop no-submit package, or plan R02a and R02b together?
- Should the new wall-impact route allow explicit wall break / wall hole / through-wall result from the start?
- Should identity anchors from K255 remain active for R02a, or be simplified to prioritize action timing?
- Should action-reference videos be gathered before K263 or after the first K263 package draft?

Human review:

- Should K263 prompt/package be reviewed by the human before live submit, given the major creative route change?
- Should ChatGPT Pro review any new reference video action grammar before package creation?

## 14. Recommended Next Steps

Recommended next phase:

`K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE`

Recommended scope for K263:

- Report/package creation only.
- No Dreamina.
- No submit/query/download.
- No media creation.
- No Source modification.
- Create a no-submit package for SHOT-04 R02a contact / brief hit-stop only.
- Preserve the two-shot route plan: R02a first, R02b later.
- Use result-first action syntax.
- Define hit-stop as brief, not sustained slow push.
- Define immediate fast displacement as the next beat.
- Keep final_master=false and locked=false.

Recommended parallel human/ChatGPT work:

- Use K244S evidence if Source synthesis is needed.
- Use K262 and this report as onboarding context for a new ChatGPT Pro Extended chat.
- Consider action-reference video planning before any new live submit.

Not recommended:

- Do not retry K260 cuts as primary.
- Do not submit a new one-shot overloaded wall-impact route without package review.
- Do not treat K255/K257 media as approved final.
- Do not modify Source directly from Codex.

## 15. Boundary Confirmations

For this report phase:

- Dreamina was not run.
- No submit occurred.
- No query occurred.
- No download occurred.
- No retry occurred.
- No resubmit occurred.
- No batch occurred.
- No media was created.
- No video was cut.
- No frames were extracted.
- No contact sheet was created.
- No file under `sources/` was created, edited, deleted, renamed, moved, staged, committed, or pushed.
- No prompt txt file was modified.
- No package JSON file was modified.
- No manifest CSV file was modified.
- No shot record was modified.
- No runtime/config/auth/session/token/key/env file was accessed or modified.
- `.vs/` was not staged.
- `reports/context_recovery/` was not staged.
- `productions/chi_yan_tian_qiong/edits/` was not staged.
- `final_master=true` was not set.
- `locked=true` was not set.
- No route decision requiring human approval was made.
- No submit-ready package or live manifest was created.

Final state represented by this report:

- `sources/` clean.
- Text-only report created under `reports/`.
- Recommended next phase remains `K263_NO_SUBMIT_SHOT04_R02A_CONTACT_HIT_STOP_PACKAGE`.
