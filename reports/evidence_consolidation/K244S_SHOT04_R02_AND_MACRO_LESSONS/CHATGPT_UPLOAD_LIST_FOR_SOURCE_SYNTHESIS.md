# ChatGPT Upload List for Source Synthesis

## Purpose

Tell the human exactly which K244S files to upload to ChatGPT Pro Extended for later Source synthesis. These files are evidence/prep files, not official Source. Uploading them does not authorize Codex to modify `sources/`.

Project root:

```text
G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE
```

## MUST_UPLOAD

| File | Full Windows path | Repo-relative path | Why it matters | safe_to_upload | sensitive_risk | Upload priority |
| --- | --- | --- | --- | --- | --- | --- |
| `README_FOR_CHATGPT_PRO_EXTENDED.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\README_FOR_CHATGPT_PRO_EXTENDED.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/README_FOR_CHATGPT_PRO_EXTENDED.md` | Sets context, current K244/K245 state, and boundaries. | true | low: local paths and workflow state only | 1 |
| `SHOT04_R02_FAILURE_LEDGER.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\SHOT04_R02_FAILURE_LEDGER.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/SHOT04_R02_FAILURE_LEDGER.md` | Narrative failure history and route decisions. | true | low: no signed URLs or secrets expected | 2 |
| `SHOT04_R02_FAILURE_LEDGER.csv` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\SHOT04_R02_FAILURE_LEDGER.csv` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/SHOT04_R02_FAILURE_LEDGER.csv` | Structured failure rows for analysis. | true | low: phase/task metadata only | 3 |
| `PROMPT_OUTCOME_DATASET.csv` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\PROMPT_OUTCOME_DATASET.csv` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/PROMPT_OUTCOME_DATASET.csv` | Links prompts, settings, outcomes, and next-route decisions. | true | medium-low: includes prompt paths and hashes, no secrets | 4 |
| `HUMAN_CHATGPT_CODEX_REVIEW_EXCERPTS.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\HUMAN_CHATGPT_CODEX_REVIEW_EXCERPTS.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/HUMAN_CHATGPT_CODEX_REVIEW_EXCERPTS.md` | Captures human/ChatGPT/Codex review excerpts and process rules. | true | medium: contains conversation-context rules and local report references | 5 |
| `MACRO_RUN_LESSONS_AND_ONE_CLICK_REQUIREMENTS.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\MACRO_RUN_LESSONS_AND_ONE_CLICK_REQUIREMENTS.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/MACRO_RUN_LESSONS_AND_ONE_CLICK_REQUIREMENTS.md` | Converts evidence into macro-run requirements and stop gates. | true | low: process rules only | 6 |
| `SOURCE_UPDATE_CANDIDATES.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\SOURCE_UPDATE_CANDIDATES.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/SOURCE_UPDATE_CANDIDATES.md` | Direct candidate rules for ChatGPT Pro Extended to transform into Source drafts. | true | low: no official Source mutation, candidates only | 7 |

## SHOULD_UPLOAD

| File | Full Windows path | Repo-relative path | Why it matters | safe_to_upload | sensitive_risk | Upload priority |
| --- | --- | --- | --- | --- | --- | --- |
| `PROMPT_TEXT_ARCHIVE_AND_INDEX.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\PROMPT_TEXT_ARCHIVE_AND_INDEX.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/PROMPT_TEXT_ARCHIVE_AND_INDEX.md` | Lets ChatGPT inspect prompt evolution without opening live prompt files. | true | medium: contains prompt text excerpts/full short prompts; no signed URLs or secrets expected | 8 |
| `ROOT_CAUSE_TAXONOMY.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\ROOT_CAUSE_TAXONOMY.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/ROOT_CAUSE_TAXONOMY.md` | Provides stable failure categories and recommended actions. | true | low: taxonomy only | 9 |
| `ACTION_REFERENCE_VIDEO_LIBRARY_PLAN.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\ACTION_REFERENCE_VIDEO_LIBRARY_PLAN.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/ACTION_REFERENCE_VIDEO_LIBRARY_PLAN.md` | Adds action-reference library plan, annotation template, and review rubric. | true | low: no media, no URLs required | 10 |
| `SHOT04_R02_SUCCESS_AND_PARTIAL_SUCCESS_LEDGER.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\evidence_consolidation\K244S_SHOT04_R02_AND_MACRO_LESSONS\SHOT04_R02_SUCCESS_AND_PARTIAL_SUCCESS_LEDGER.md` | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/SHOT04_R02_SUCCESS_AND_PARTIAL_SUCCESS_LEDGER.md` | Separates technical, boundary, package, artifact, and visual successes. | true | low: summary evidence only | 11 |

## OPTIONAL

| File | Full Windows path | Repo-relative path | Why it matters | safe_to_upload | sensitive_risk | Upload priority |
| --- | --- | --- | --- | --- | --- | --- |
| `PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | `reports/PHASE_K220B_SHOT04_R02_VISUAL_REVIEW_FAILED_CORE_ACTION.md` | Full visual failure review for downloaded video and action-quality diagnosis. | true | medium: includes local media/review artifact paths and human review text | 12 |
| `PHASE_K235F_SHOT04_R02_TRIPLE_REMOTE_FAILURE_ROUTE_DECISION.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\PHASE_K235F_SHOT04_R02_TRIPLE_REMOTE_FAILURE_ROUTE_DECISION.md` | `reports/PHASE_K235F_SHOT04_R02_TRIPLE_REMOTE_FAILURE_ROUTE_DECISION.md` | Full triple-failure route decision and manual-layout/alternate-action comparison. | true | low-medium: local paths and submit IDs | 13 |
| `PHASE_K241F_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_FAILURE_REVIEW.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\PHASE_K241F_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_FAILURE_REVIEW.md` | `reports/PHASE_K241F_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2IMAGE_FAILURE_REVIEW.md` | Full fourth remote-failure review and broadened dual-character close-combat diagnosis. | true | low-medium: local paths and submit IDs | 14 |
| `PHASE_K242V_SHOT04_R02_NEAR_WALL_GUARD_CLASH_VIDEO_ROUTE_PLANNING.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\PHASE_K242V_SHOT04_R02_NEAR_WALL_GUARD_CLASH_VIDEO_ROUTE_PLANNING.md` | `reports/PHASE_K242V_SHOT04_R02_NEAR_WALL_GUARD_CLASH_VIDEO_ROUTE_PLANNING.md` | Full video-first route planning and front-loaded timing design. | true | low: planning text and local paths | 15 |
| `PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md` | `reports/PHASE_K244_SHOT04_R02_NEAR_WALL_GUARD_CLASH_TEXT2VIDEO_PACKAGE_REVIEW.md` | Current package-review status and K245 one-submit-only boundary. | true | low-medium: package paths and hashes | 16 |
| `AI_VIDEO_K201_K218_HANDOFF_SUMMARY.md` | `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\context_recovery\K201_K218_handoff\AI_VIDEO_K201_K218_HANDOFF_SUMMARY.md` | `reports/context_recovery/K201_K218_handoff/AI_VIDEO_K201_K218_HANDOFF_SUMMARY.md` | Optional recovery context if ChatGPT asks how K201-K218 led into K219-K244. | true | medium: broader context recovery state and local paths | 17 |

## Upload Guidance

- Upload `MUST_UPLOAD` first.
- Add `SHOULD_UPLOAD` if ChatGPT needs more prompt/taxonomy/action-reference detail.
- Add `OPTIONAL` only if ChatGPT asks for original phase evidence or K201-K218 recovery context.
- Do not upload media files unless a separate rights/safety decision explicitly requests them.
- Do not upload auth/session/token/key/env files.
- Do not treat any uploaded candidate file as official Source until ChatGPT Pro Extended and the human transform and approve it.
