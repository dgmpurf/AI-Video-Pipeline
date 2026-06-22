# PHASE K43 SHOT-02 V012 Human Review And V013 Direction

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope And Safety Boundaries

This pass records the SHOT-02-V012 human review result, integrates the Codex K42 usable-with-cut recommendation as a secondary local-test option, and prepares the SHOT-02-V013 direction only.

- Dreamina was not run.
- No submit, query_result, download, retry, resubmit, batch, image2video, image2image, or multimodal2video command was run.
- No media edit was created in this pass.
- No media was moved, deleted, staged, or committed.
- No runtime code, configs/providers.json, Project Source, prompt package files, or source files were modified.
- final_master=false.
- locked=false.
- Human review is required before any final or lock decision.

## Files Inspected

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V012.json
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K42_SHOT02_V012_VISUAL_REVIEW.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K41_SHOT02_V012_QUERY_DOWNLOAD_RESULT.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K39_SHOT02_V012_PACKAGE_REVIEW.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K38_SHOT02_V012_MULTIMODAL_PACKAGE_READY.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K37_SHUANGJI_IDENTITY_ANCHOR_HUMAN_APPROVED_LOCKED.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/assets/asset_registry.json

## V012 Final Human Decision

SHOT-02-V012 is rejected for final use.

Do not mark V012 final or locked. Human review overrides any automatic or Codex recommendation for final approval.

Codex K42 recommendation was usable_with_cut, not final pass. That recommendation is retained only as permission to run optional local cut/speed-up diagnostic tests later if useful. It does not mean the full 4s V012 clip passes final review.

Integrated V012 decision:

- status=human_rejected_for_final_usable_with_cut_test
- human_review_status=rejected_for_final
- final_master=false
- locked=false
- usable_for_final=false
- official_video_candidate=false
- usable_video_candidate=cut_test_only
- primary_next_path=SHOT-02-V013 new generation with stronger action choreography
- secondary_next_path=optional V012 local cut/speed-up test for review only

## What Improved In V012

- Shuangji identity improved significantly versus V010/V011.
- Female identity is much more stable.
- The A-CH-B-IDENTITY-002 Shuangji identity anchor strategy worked.
- Fenshou identity and two-character integrity are acceptable.
- The identity problem is largely solved compared with the earlier identity-drift attempts.

## What Still Failed

- Fight speed still needs to be at least roughly 2x faster.
- Contact density is too low.
- Impact and power are insufficient.
- The action lacks sharp collision-based force.
- More combat detail beats are needed.
- The final roughly 1 second settles or eases off instead of continuing to fight.
- Do not solve impact by using slow motion.
- The full 4s V012 clip is not useful as final.

## Codex K42 Integration

Codex K42 visual review verdict:

- Codex recommendation: usable_with_cut
- Shuangji identity: 5/5
- Fenshou identity: 5/5
- Character integrity: 5/5
- Action speed: 3/5
- Collision impact: 2/5
- Edit usability: 3/5
- Contamination risk: 2/5

K42 best cut candidates:

- 0.50s-1.50s
- 0.75s-1.75s

K42 speed-up tests recommended:

- 1.25x
- 1.5x

Interpretation:

- The K42 usable-with-cut result is useful as an edit diagnostic only.
- Cut/speed tests cannot replace the need for V013 if impact choreography is missing.
- V012 should not be used as a visual reference for next generation.
- V012 can be used as a text failure reference: identity improved, but speed, impact, contact density, and tail continuation failed.

## V013 Primary Direction

V013 should keep:

- Fenshou locked identity reference:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
- A-CH-B-IDENTITY-002 Shuangji identity anchor:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
- Temple scene anchor:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png
- Exclusion of V009/V010/V011 visual frames.

V013 must change:

- Action density.
- Speed.
- Impact mechanics.
- Tail continuation.

Primary path:

- Create a new SHOT-02-V013 generation package with stronger choreography.
- Do not force V012 into final use.
- Do not create full V013 package files in this pass.

## V013 Action Design Notes

Use concrete AI-video language:

- True-speed close-range combat, not slow motion.
- At least four quick contact beats in the first 1.0s.
- First beat: hard step-in and abrupt forearm/wrist contact.
- Second beat: immediate slap-away / deflection with visible rebound.
- Third beat: re-entry with shoulder/forearm pressure burst, not a hold.
- Fourth beat: short palm / elbow-line interruption / quick counter beat.
- 1.0s-4.0s continues into another chain, not a settled guard pose.
- Final roughly 1s must continue attacking/defending.
- Short impact, immediate rebound.
- Sharp stop-start footwork.
- Strong weight transfer.
- Sudden acceleration and abrupt redirection.
- Visible body recoil on contact.
- Shoe skid on wet stone.
- Small splashes kicked sideways.
- Sleeve snap, robe snap, hair whip.
- No long arm-lock.
- No slow pushing.
- No pose-to-pose demonstration sparring.
- No slow motion impact cheat.

Desired rhythm:

- Faster da-da-da-da close-range exchange.
- Multiple short contact beats.
- More physical force and collision.
- Continued fighting through the tail instead of pose-out.

## Local Edit Recommendation

V012 should not be final.

V012 may proceed to optional cut/speed-up testing as a secondary diagnostic only:

- 0.50s-1.50s at normal speed, 1.25x, and 1.5x.
- 0.75s-1.75s at normal speed, 1.25x, and 1.5x.

The local test should be evaluated only as a possible tiny bridge/extract. It should not be treated as a substitute for missing choreography.

Primary path remains V013 new generation with stronger choreography.

## Metadata Update Summary

SHOT-02-V012 shot record now records:

- codex_visual_review_recommendation=usable_with_cut
- human_review_overrides_codex_visual_review=true
- status=human_rejected_for_final_usable_with_cut_test
- human_review_status=rejected_for_final
- identity_result=improved_pass
- action_result=failed_for_final
- usable_video_candidate=cut_test_only
- usable_as_identity_reference=false
- usable_as_action_reference=false
- usable_as_visual_reference_for_next_generation=false
- usable_as_text_failure_reference_for_next_generation=true
- local_edit_candidate=true
- local_edit_candidate_type=cut_and_speed_test_only
- recommended_cut_tests=0.50s-1.50s; 0.75s-1.75s
- recommended_speed_tests=1.25x; 1.5x
- primary_next_path=SHOT-02-V013 new generation with stronger action choreography
- secondary_next_path=optional V012 local cut/speed-up test for review only
- rejection_reason=identity_improved_but_speed_impact_contact_density_and_tail_continuation_failed
- final_master=false
- locked=false

Final verdict:
SHOT_02_V012_HUMAN_REJECTED_V013_DIRECTION_READY_WITH_OPTIONAL_CUT_TEST
