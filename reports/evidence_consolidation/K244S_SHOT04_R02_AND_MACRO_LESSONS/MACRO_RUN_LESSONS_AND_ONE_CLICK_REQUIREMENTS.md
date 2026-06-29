# Macro-Run Lessons and One-Click Requirements

## Purpose

This file converts SHOT-04 R02 K201-K244 failure/success evidence into future macro-run and one-click-ish workflow requirements. It is evidence-only. It does not modify Source and does not authorize Dreamina, submit, query, download, retry, resubmit, media creation, package edits, prompt edits, manifest edits, staging, commit, or push.

## Operating Principle

One-click-ish must not mean one unbounded execution. It should mean one orchestrated workflow that creates named phase artifacts, honors authorization boundaries, records evidence, and stops at configured gates.

Required global rules:

- No final/lock without human approval.
- No Source modification by Codex.
- Submit, query, download, retry, and resubmit remain separate unless explicitly macro-authorized.
- If remote final-generation failure repeats across two structurally distinct routes, stop retrying and route reset.
- If visual failure occurs but media exists, build review artifacts and compare against action reference and timing.
- If still-keyframe routes fail remotely but video has produced media before, consider video-first route.
- If video output exists, human visual review is required before final use.
- User reviews images/videos by default, not prompts.
- Prompt review only after repeated failure, major route change, or explicit user request.
- Periodically consolidate failure/success ledgers into Source update candidates.

## A. Input/Story Compiler

Requirements:

- Accept story intent, shot goal, character duties, location duties, and hard exclusions as structured inputs.
- Preserve `final_master=false` and `locked=false` until human approval.
- Emit a story/shot intent record before any prompt or package work.
- Detect when the requested beat depends on brittle geometry such as exact body-wall contact, two-character close combat, or fast rebound timing.
- Track whether the user wants image/video review only or also wants prompt review for that run.

SHOT-04 R02 lesson:

- The original wall-impact intent was creatively clear but provider-fragile. The compiler should flag exact body-wall contact and force-transfer causality as high-risk before package creation.

## B. Script/Shot Compiler

Requirements:

- Translate story intent into shot phases, action beats, timing windows, and review checkpoints.
- Separate technical phases from creative approval phases.
- Record when a legal 5s output is really targeting a 0.8s-1.5s useful edit window.
- Generate a "what not to do" list for each phase.
- Never infer final/lock from successful package review, submit, query, download, or artifact generation.

SHOT-04 R02 lesson:

- K220B showed that a legal 5s clip can waste time on approach and pose-out. Future shot compilers should front-load decisive action and treat later seconds as continuation handles.

## C. Asset Planner A/L/C/HC/CTRL/SHOT

Requirements:

- Create an asset-duty map for Architecture, Location, Character, Human-control, Control/layout, and Shot-specific refs.
- Duty-limit architecture refs so they do not become action/final/lock refs accidentally.
- Detect reference attention conflict, especially mixed landscape architecture refs with portrait identity refs.
- Prefer upload-safe package-local refs for live submits using media inputs.
- Keep layout/control assets separate from final art unless human-approved.

SHOT-04 R02 lesson:

- The wall-panel image succeeded as architecture reference only. Later 4-ref and 3-ref close-contact routes showed that refs can be structurally valid yet still too brittle for the model.

## D. Prompt Compiler

Requirements:

- Lead with the visible P0 result, not asset IDs, process notes, or reference-duty prose.
- Keep primary action, timing, contact/proximity, and hard negatives compact and ranked.
- Remove old failed constraints when a route changes. For K238/K243V this meant no body-wall contact, no wall hit, no wall damage.
- Default human review surface is images/videos, not prompts.
- Prompt review is triggered only by repeated failures, major route changes, package-review defects, or explicit user request.
- Keep generation prompt bodies free of internal phase/process/final/lock/source/report wording unless a package format requires metadata outside the generation prompt.

SHOT-04 R02 lesson:

- K221 explicitly required dominant visual-result wording after K220B failed. K244 passed a motion-first prompt but kept high-risk notes rather than pretending prompt review guaranteed output success.

## E. Package Builder

Requirements:

- Build no-submit packages first.
- Include package JSON, manifest CSV, prompt path/hash, reference map, permissions flags, and risk labels.
- Keep `submit_allowed=false`, `query_allowed=false`, `download_allowed=false`, `retry_allowed=false`, `resubmit_allowed=false` until a live phase is explicitly authorized.
- Do not modify existing prompt/package/manifest files outside the authorized phase scope.
- Preserve package readiness separately from live execution readiness.

SHOT-04 R02 lesson:

- K210 caught prompt/package gaps before live authorization; K212 re-reviewed after a narrow fix. Package review is useful, but K213/K220B/K226 showed it cannot guarantee upload, remote generation, or visual success.

## F. Independent Package Review

Requirements:

- Review package structure, hashes, manifest row count, command contract, reference duties, and visual-target completeness.
- Emit `package_review_status` plus high-risk notes.
- Passing review means ready for a human authorization decision, not ready for automatic submit.
- If review finds a blocking defect, route to package fix, not live submit.

SHOT-04 R02 lesson:

- K244 found the text2video package structurally ready but high-risk. That is the right state: ready for K245 decision, not already executed.

## G. Human Authorization Gate

Requirements:

- Separate authorization for submit, query, download, retry, resubmit, media creation, Source update, final, and lock.
- Record the exact human authorization text when a live phase happens.
- One-submit-only and one-query-only boundaries must be enforced literally.
- Package metadata may remain no-submit while a specific phase receives human authorization; record the distinction.
- If human review is optional/configurable in a macro-run, the macro must still stop before final/lock unless human approval exists.

SHOT-04 R02 lesson:

- K225 and K226 are good examples of exact live scopes: one submit, then one query, with no download or retry.

## H. Dreamina Execution Layer

Requirements:

- Run current command-contract preflight only when live execution is authorized for that phase.
- Use exact task type help: `multimodal2video -h`, `image2image -h`, `text2image -h`, or `text2video -h` as applicable.
- Submit exactly once when one-submit is authorized.
- Do not query, download, retry, resubmit, or batch from a submit-only phase.
- Treat `submit_id` plus `gen_status=fail` as failure, not queued success.
- Redact or avoid signed URLs/secrets in reports.

SHOT-04 R02 lesson:

- K213 returned a submit ID but failed in upload. K225 returned `querying`, then K226 later returned final-generation failure. These are distinct states.

## I. Query/Download Layer

Requirements:

- Query only when authorized for a specific submit ID.
- Do not use `--download_dir` during query-only phases.
- Download only if separately authorized and only when a result/download URL exists.
- If query returns fail with no result media, do not attempt download.
- If query still returns querying, do not loop unless macro-authorized.

SHOT-04 R02 lesson:

- K226, K230, K235, and K241 each preserved query/download boundaries and recorded no media where no result existed.

## J. Review Artifact Builder

Requirements:

- If media exists, create review frames/contact sheets only when authorized.
- Store review artifacts with hashes, dimensions, frame counts, and source media lineage.
- Review artifacts are evidence, not approval.
- Do not create review artifacts for remote failures with no media.

SHOT-04 R02 lesson:

- K220A enabled K220B visual diagnosis after K219 download. The workflow should build artifacts before asking for final visual judgment.

## K. Human Visual Review Recorder

Requirements:

- Record human image/video review as the default creative review surface.
- Capture visual status fields: action, identity, force transfer, timing, tail, environment, final/lock usability.
- Preserve exact human quotes when usable; when encoding is damaged, preserve the raw quote separately and provide an operational summary.
- If video output exists, human visual review is required before final use.
- Prompt review is not the default substitute for image/video review.

SHOT-04 R02 lesson:

- K220B correctly recorded a failed downloaded video as failure evidence only, not as final/locked media.

## L. Failure/Success Ledger Writer

Requirements:

- Maintain separate failure ledger and success/partial-success ledger.
- Separate package success, submit success, query success, download success, review-artifact success, visual success, and final/lock success.
- Classify failures using stable categories: upload transport, remote final generation, visual execution, prompt priority, reference conflict, route reset, and so on.
- If two structurally distinct routes fail remotely, write a route-reset recommendation instead of another blind retry.

SHOT-04 R02 lesson:

- K244S Part 1 and Part 2 now show that technical successes and creative failures can coexist. The macro-run must preserve that distinction automatically.

## M. Source Update Recommender

Requirements:

- Codex may create Source update candidates under reports, but must not modify official Source.
- ChatGPT Pro Extended or the human should synthesize and approve official Source changes.
- Periodically consolidate failure/success ledgers into candidate Source notes.
- Candidate Source notes should include evidence, trigger conditions, recommended action, and what not to do.
- Source updates should be based on patterns, not isolated failures.

SHOT-04 R02 lesson:

- The pattern is now broad enough for Source candidates: repeated still/keyframe remote final-generation failures, dual-character close-combat brittleness, video technical success with visual failure, and the need for human-configurable macro gates.

## Minimum One-Click-ish Macro Stop Points

The macro must stop at these points unless explicitly configured and authorized to continue:

1. Dirty `sources/` preflight.
2. Package defect or command-contract mismatch.
3. Need for live submit authorization.
4. Submit-only phase completed.
5. Query-only phase completed.
6. Download needed but not authorized.
7. Media exists and visual review is required.
8. Repeated remote final-generation failure triggers route reset.
9. Creative direction changes, such as wall-contact to near-wall guard-clash.
10. Any proposed final/lock or official Source update.
