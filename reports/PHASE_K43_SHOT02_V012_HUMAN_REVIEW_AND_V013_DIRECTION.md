# PHASE K43 SHOT-02 V012 Human Review And V013 Direction

Date: 2026-06-23
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope And Boundary Confirmation

This report records the human review result for SHOT-02-V012 and prepares the correction direction for SHOT-02-V013 only.

- Dreamina was not run.
- No submit, query_result, download, retry, resubmit, or batch action was performed.
- No media was generated, moved, deleted, staged, or committed.
- No runtime code, configs/providers.json, Project Source, or prompt source files were modified.
- SHOT-02-V012 is not final master and is not locked.
- Final video approval still requires human review.

## Files Inspected

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V012.json
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K42_SHOT02_V012_VISUAL_REVIEW.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K41_SHOT02_V012_QUERY_DOWNLOAD_RESULT.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K37_SHUANGJI_IDENTITY_ANCHOR_HUMAN_APPROVED_LOCKED.md

## V012 Human Review Result

SHOT-02-V012 is rejected for final use.

Shuangji identity improved compared with V010/V011. The character no longer shows the earlier obvious male-coded drift, and the two-character setup is cleaner than V011 where applicable.

The remaining blocker is not identity. The failure is action rhythm, power, contact density, and tail continuation. V012 should not be used as final footage.

## What Improved

- Shuangji female identity is better preserved.
- The result is no longer strongly male-coded.
- The two-character relationship is cleaner than the earlier V011 attempt where applicable.
- The A-CH-B-IDENTITY-002 Shuangji identity anchor strategy remains useful.

## What Failed

- Fight speed is too slow and should feel roughly 2x faster.
- Contact density is too low.
- The clip does not contain enough short contact beats.
- Power and impact feel are insufficient.
- Action is not forceful enough.
- Slow motion should not be used as the solution.
- The final roughly 1 second eases off or settles instead of continuing the fight.
- The action reads too much like a demonstration or controlled exchange instead of a sharp close-range clash.

## V013 Direction

V013 should preserve the improved identity strategy while redesigning the action rhythm around higher beat density, stronger contact, and continued motion through the tail.

Keep:

- Shuangji identity anchor:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
- Fenshou locked reference.
- Temple scene reference.

Continue excluding:

- V009 frame references.
- V010 frame references.
- V011 frame references.

V012 may be treated only as limited text guidance or loose composition context. It is not a final video, not an identity reference, and not an action reference for direct copying.

## V013 Action Design Notes

The first second must immediately deliver dense close-range fighting, not a pause or slow setup.

- 0.0s-1.0s should contain about four quick contact beats.
- Beat 1: hard step-in and abrupt forearm or wrist contact.
- Beat 2: immediate slap-away or deflection with visible rebound.
- Beat 3: re-entry with shoulder or forearm pressure burst, not a hold.
- Beat 4: short palm, elbow-line interruption, or quick counter beat.
- 1.0s-4.0s should continue into another chain, not settle down.
- The last roughly 1 second must continue attacking and defending instead of posing out.

The desired feeling is a faster "da-da-da-da" close-range exchange with multiple short collision beats.

## Force And Impact Language

Use physical action language that pushes Dreamina toward sharper combat rhythm:

- Sharp stop-start footwork.
- Strong weight transfer.
- Sudden acceleration and abrupt redirection.
- Visible body recoil on contact.
- Shoe skid on wet stone.
- Small splashes kicked sideways.
- Sleeve snap, robe snap, and hair whip.
- Short impact followed by immediate rebound.

Avoid:

- Long arm-lock.
- Slow pushing.
- Pose-to-pose demonstration sparring.
- Slow motion impact cheat.
- Static camera pullback while fighters remain frozen.
- Tail section that settles into a poster-like pose.

## Suggested V013 Package Strategy

Recommended R01 reference count: exactly 3 refs.

1. Fenshou identity reference:
   G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png
2. Shuangji highest-priority identity reference:
   G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-CH-B-IDENTITY-002_locked_shuangji_face_upper_body_identity_anchor.png
3. Scene/world reference:
   G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/locked_refs/A-SC-TEMPLE-COURTYARD-004_locked_main_hall_true_frontal_axis_stage.png

Recommended task direction:

- Use V013 as a new generation path.
- Prioritize identity-protected fast close-range combat.
- Keep reference duties clean: identity refs for character identity, scene ref for world/frontal-axis continuity.
- Do not use V009/V010/V011/V012 frames as primary video-driving references for this correction.

## Local Edit Recommendation

Do not treat V012 as final.

An optional future speed-test of V012 can exist only as a secondary experiment, but the primary path should be V013 new generation rather than forcing V012 in edit.

## Optional V013 Package Planning Stub

Planned task id: SHOT-02-V013

Package status: planning_only_no_submit

Expected concept: identity_locked_fast_close_quarters_followup_attack

Target correction:

- Faster rhythm.
- Higher contact density.
- Stronger collision and recoil.
- Continuous attack/defense through the final second.
- Preserve Shuangji identity using A-CH-B-IDENTITY-002.

## Metadata Updates

SHOT-02-V012 shot record should reflect:

- status=rejected_for_final_due_to_rhythm_and_impact_insufficient
- human_review_status=rejected
- final_master=false
- locked=false
- usable_for_final=false
- official_video_candidate=false
- usable_video_candidate=false
- identity_result=improved_pass
- action_result=failed
- usable_as_identity_reference=false
- usable_as_action_reference=false
- usable_as_visual_reference_for_next_generation=limited_text_guidance_only
- usable_as_loose_composition_reference=true
- rejection_reason=identity_improved_but_speed_impact_and_tail_continuation_failed

Final verdict:
SHOT_02_V012_HUMAN_REJECTED_V013_DIRECTION_READY
