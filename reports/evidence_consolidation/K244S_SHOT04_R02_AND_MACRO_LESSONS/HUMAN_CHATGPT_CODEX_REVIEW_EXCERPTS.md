# Human, ChatGPT, and Codex Review Excerpts

## Purpose

This file consolidates selected human review, ChatGPT visual review, route decision, Codex report, and process feedback excerpts from the SHOT-04 R02 K201-K244 chain plus current conversation-context rules. It is evidence-only for ChatGPT Pro Extended Source synthesis. It does not authorize Dreamina, submit, query, download, retry, resubmit, media creation, prompt edits, package edits, manifest edits, Source edits, staging, commit, or push.

## Human Review Excerpts

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| `reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | K220B | "Operational summary of the human review: the candidate has a major problem; received-impact feedback is muddy, character reaction is slow, the wall-impact intent is not readable, the shot appears to waste the 5 second duration on too little core action..." | Establishes that the downloaded video failed visually even though submit, query, download, and review artifact creation succeeded. | visual_failure |
| `reports/PHASE_K225_SHOT04_R02_MICRO_IMPACT_KEYFRAME_L3_SUBMIT_RESULT.md` | K225 | "The human explicitly authorizes K225 to run corrected Dreamina preflight and submit exactly one image2image task for the K223/K224-approved package." | Shows live execution is human-gated and phase-specific, even when package metadata remains no-submit. | human_choice |
| `reports/PHASE_K226_SHOT04_R02_MICRO_IMPACT_KEYFRAME_QUERY_RESULT_NO_DOWNLOAD.md` | K226 | "K226 is query-only. Do not use --download_dir. Do not download even if the result is success. Do not retry or resubmit if the result fails." | Captures the separate query/download/retry boundary that future macro-runs must preserve. | process_feedback |
| conversation context | K244S Part 3 | "User reviews images/videos by default, not prompts." | Defines the default human review surface for future automation: visual media first, prompt text only when needed. | prompt_logic |

## ChatGPT Visual Review Excerpts

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| `reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | K220B | "The human review is valid. This SHOT-04 R02 candidate fails the core action. It is not a minor fix." | Distinguishes a blocking visual failure from a small edit or speed issue. | visual_failure |
| `reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | K220B | "`impact_status=failed`, `received_force_status=failed`, `wall_contact_causality_status=failed_or_weak`, `reaction_speed_status=too_slow`, `tail_status=pose_out_or_static_showdown_tendency`." | Converts visual judgment into reusable status fields for ledgers and review tooling. | visual_failure |
| `reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | K220B | "Speed-up cannot repair missing body-wall causality or convert a weak push into a readable impact." | Prevents a misleading local edit from masking a structural generation failure. | route_decision |
| `reports/PHASE_K241F_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_FAILURE_REVIEW.md` | K241F | "This is no longer only exact body-wall contact brittleness." | Broadens diagnosis after the no-wall-contact near-wall guard-clash still route also failed remotely. | source_update_candidate |

## ChatGPT Route Decision Excerpts

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| `reports/PHASE_K221_SHOT04_R02_ROUTE_DECISION_AFTER_VISUAL_FAILURE.md` | K221 | "`route_decision=MICRO_IMPACT_CONTACT_KEYFRAME_FIRST_THEN_SHORT_EDIT_WINDOW`" | After visual video failure, the route changed from full 5s direct video to result-first micro-impact state control. | route_decision |
| `reports/PHASE_K226F_SHOT04_R02_MICRO_IMPACT_KEYFRAME_FAILURE_REVIEW_AND_ROUTE_DECISION.md` | K226F | "`route_decision=K227R_SIMPLIFY_TO_3REF_MICRO_IMPACT_KEYFRAME_PACKAGE_NO_SUBMIT`" | The first remote final-generation failure led to structural simplification rather than same-package retry. | route_decision |
| `reports/PHASE_K230F_SHOT04_R02_REPEATED_IMAGE2IMAGE_FAILURE_REVIEW_AND_ROUTE_RESET.md` | K230F | "`route_decision=K231_ROUTE_RESET_COMPARE_SOFTENED_IMAGE2IMAGE_VS_TEXT2IMAGE_NO_SUBMIT`" | The second structurally related image2image remote failure triggered route reset. | route_decision |
| `reports/PHASE_K235F_SHOT04_R02_TRIPLE_REMOTE_FAILURE_ROUTE_DECISION.md` | K235F | "`route_decision=K236_MANUAL_LAYOUT_OR_ALTERNATE_ACTION_HUMAN_DECISION_PLANNING`" | After 4-ref image2image, 3-ref image2image, and softened text2image all failed remotely, the next step became a human strategy choice. | route_decision |
| `reports/PHASE_K242V_SHOT04_R02_NEAR_WALL_GUARD_CLASH_VIDEO_ROUTE_PLANNING.md` | K242V | "`route_decision=K243V_TEXT2VIDEO_NEAR_WALL_GUARD_CLASH_NO_SUBMIT_PACKAGE`" | The route returned to video because video had produced media before, while still/keyframe routes were failing remotely. | route_decision |

## Codex Report / Final Verdict Excerpts

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| `reports/PHASE_K210_SHOT04_R02_PACKAGE_FILE_HUMAN_REVIEW_SUBMIT_READINESS_NO_SUBMIT.md` | K210 | "`NEEDS_PACKAGE_FIX_BEFORE_AUTHORIZATION`" | Demonstrates a package-defect block caught before live execution. | prompt_logic |
| `reports/PHASE_K212_SHOT04_R02_PACKAGE_FILE_SUBMIT_READINESS_REVIEW_NO_SUBMIT.md` | K212 | "`READY_TO_REQUEST_HUMAN_L3_SUBMIT_AUTHORIZATION`" | Shows the package became review-ready only after a narrow fix and re-review. | process_feedback |
| `reports/PHASE_K214_SHOT04_R02_SUBMIT_FAILURE_TRIAGE_UPLOAD_PATH_REMEDIATION_PLANNING.md` | K214 | "Important interpretation: the returned `submit_id` is not a successful queued task because `gen_status=fail`." | Prevents false success classification when submit returns an ID but fails in upload. | process_feedback |
| `reports/PHASE_K226_SHOT04_R02_MICRO_IMPACT_KEYFRAME_QUERY_RESULT_NO_DOWNLOAD.md` | K226 | "`SHOT04_R02_MICRO_IMPACT_KEYFRAME_QUERY_FAILED_NO_RETRY_READY_REVIEW`" | Encodes one-query-only failure with no retry/download side effects. | process_feedback |
| `reports/PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md` | K244 | "`package_review_status=pass_with_high_risk_notes_ready_for_human_K245_submit_authorization_decision`" | Current state is package readiness, not generated media success. | macro_run_need |
| `reports/PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md` | K244 | "`SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW_PASS_WITH_HIGH_RISK_NOTES_READY_K245_SUBMIT_DECISION`" | Leaves K245 as a human-authorized one-submit decision, not an automatic continuation. | human_choice |

## Human Route Choices

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| `reports/PHASE_K236_SHOT04_R02_HUMAN_ROUTE_DECISION_PLANNING_AFTER_TRIPLE_FAILURE.md` | K236 | "The human should decide: Is exact body-wall contact still required?... Is it acceptable to change SHOT-04 R02 into a near-wall guard clash?" | Formalizes the point where route strategy moves from prompt iteration to human creative choice. | human_choice |
| `reports/PHASE_K236_SHOT04_R02_HUMAN_ROUTE_DECISION_PLANNING_AFTER_TRIPLE_FAILURE.md` | K236 | "`Option B = alternate near-wall guard-clash action beat`" | The recommended default after triple failure was to remove exact body-wall contact while keeping rainy corridor pressure. | human_choice |
| `reports/PHASE_K238_SHOT04_R02_ALTERNATE_GUARD_CLASH_ROUTE_DECISION.md` | K238 | "Human selected Option B." | Confirms the route reset was not only Codex inference; it reflects the selected creative direction. | human_choice |
| `reports/PHASE_K238_SHOT04_R02_ALTERNATE_GUARD_CLASH_ROUTE_DECISION.md` | K238 | "Exact body-wall contact route is stopped for now." | Prevents old failed wall-contact requirements from leaking into later near-wall guard-clash prompts. | route_decision |

## Process Feedback

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| `reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | K220B | "the reviewer questions why the existing Source/error-feedback chain did not prevent this result." | Source and package compliance are not enough; the system needs output-level review and periodic Source upgrade loops. | process_feedback |
| `reports/SHOT04_R02_SUCCESS_AND_PARTIAL_SUCCESS_LEDGER.md` | K244S Part 1 | "Separate technical success from visual/action success." | Macro-runs must not treat submit/query/download success as final creative success. | macro_run_need |
| `reports/SHOT04_R02_SUCCESS_AND_PARTIAL_SUCCESS_LEDGER.md` | K244S Part 1 | "Build review artifacts before visual verdicts so the failure diagnosis is inspectable." | If media exists, review artifacts should be built before human/ChatGPT visual judgment. | macro_run_need |
| conversation context | K244S Part 3 | "User wants future macro-run / one-click-ish workflow with human review optional/configurable." | A future macro-run can automate evidence production, but human review gates must remain configurable and explicit. | macro_run_need |
| conversation context | K244S Part 3 | "User wants periodic failure/success Source upgrades." | Ledgers should periodically roll up into Source update candidates rather than disappearing into phase reports. | source_update_candidate |
| conversation context | K244S Part 3 | "User wants Codex evidence collected and ChatGPT Pro Extended to synthesize Source updates." | Codex should collect evidence and recommendations, while official Source synthesis/application remains outside Codex report creation. | source_update_candidate |

## Prompt Review Policy Feedback

| Source | Phase | Excerpt | Why it matters | Category |
| --- | --- | --- | --- | --- |
| conversation context | K244S Part 3 | "Prompt review only after repeated failures, major direction changes, or explicit user request." | Prevents prompt-text review from becoming the default burden for the human. | prompt_logic |
| conversation context | K244S Part 3 | "User reviews images/videos by default, not prompts." | Keeps the normal review loop visual and production-oriented. | prompt_logic |
| `reports/PHASE_K210_SHOT04_R02_PACKAGE_FILE_HUMAN_REVIEW_SUBMIT_READINESS_NO_SUBMIT.md` | K210 | "Prompt submit-readiness gaps" included missing sustained-pushing, body-wall-fusion, magic-blast, and final/locked constraints. | Prompt review is most valuable when it catches a concrete live-execution risk before authorization. | prompt_logic |
| `reports/PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md` | K244 | "No K243VR revision is required before K245 unless the human or ChatGPT chooses to revise the prompt for creative reasons." | Package review can pass with high-risk notes without forcing prompt churn. | prompt_logic |
