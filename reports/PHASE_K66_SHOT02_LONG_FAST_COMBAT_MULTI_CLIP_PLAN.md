# PHASE K66 - SHOT-02 Long Fast-Combat Multi-Clip Plan

Date: 2026-06-24
Project root: G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE

## Scope

This pass creates a planning-only direction package for SHOT-02 V015/V016/V017 long fast-combat development.

- Dreamina was not run.
- No submit/query/download happened.
- No retry or resubmit happened.
- No media was created, edited, moved, deleted, staged, or committed.
- No submit-ready V015/V016/V017 manifests were created.
- Runtime code, configs/providers.json, and Project Source files were not modified.
- V013 shot record was not modified.
- V014-R02 shot record was not modified.

## Files Inspected

- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K65_SHOT02_V014_R02_HUMAN_REVIEW_AND_LONG_FAST_COMBAT_DIRECTION.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K64_SHOT02_V014_R02_DOWNLOAD_RESULT.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K60_SHOT02_V014_UPLOAD_FAILURE_DIAGNOSTIC_AND_R02_PACKAGE.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K54_SHOT02_V013_CUT01_LOCKED_CURRENT_PASS.md
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V014-R02_uploadsafe.json
- G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V013.json

## Current Status

SHOT-02-V013 CUT01 is locked as the current SHOT-02 passed segment version.

Locked baseline:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V013/SHOT-02-V013_CUT01_0p00_to_2p20_best_close_combat_candidate.mp4

SHOT-02-V014-R02 is a positive human-reviewed enhancement candidate. It is not final, not locked, and not a V013 replacement.

V014-R02 media:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V014-R02_20260624_143551/SHOT-02-V014-R02_uploadsafe_legwork_hand_foot_combo.mp4

V014-R02 contact sheet:

G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V014-R02/SHOT-02-V014-R02_contact_sheet.jpg

## V014-R02 Human Review Summary

The human review found V014-R02 good and realistic, with a strong 1980s-style hand-to-hand fight feeling. Its fast-combat texture is comfortable and worth polishing.

Positive points:

- good and realistic
- 1980s-style hand-to-hand fight feeling
- comfortable fast-combat texture
- worth polishing
- stable enough to become a development direction

Remaining limitations:

- lacks some xuanhuan / fantasy / particle effects
- action event feels slightly cut off
- fight speed could optionally be 10%-20% faster
- longer duration needs better camera and action progression

The human noted this kind of fight could support 10s or even 15s if camera and action progression are handled well. Multiple short fight clips edited together are acceptable and likely more stable than one long generation.

## Core Fast-Combat Power Principle

Power must not rely mainly on slow motion. Slow motion is allowed selectively, but not as the primary source of impact.

Power should come from:

- grounded stance
- rear-foot push
- hip/waist rotation
- shoulder-driven compact strikes
- short contact and immediate rebound
- very short hit-stop, about 0.1s-0.2s only at key contacts
- footwork pressure
- wet stone shoe skid
- water splash
- robe/sleeve snap
- hair whip
- balance recovery and re-entry
- continuous pressure

The target is power and impact at real speed: not soft fast motion, and not slow-motion-only heaviness.

## Recommended Structure

Default recommendation: use a multi-clip route.

| Clip | Target | Purpose |
|---|---|---|
| V015 | 4s-5s | fast hand exchange plus subtle fantasy particles |
| V016 | 4s-5s | hand-foot escalation with low kick, shin check, knee line seal, foot sweep threat |
| V017 | 4s-5s | disadvantage and counter-recovery; one fighter briefly loses balance, then re-enters and retakes pressure |

This route can be edited into a 10s-15s section.

It is safer than one single 10s-15s generation because identity/action stability is easier to preserve in shorter clips.

A future continuous 10s-15s single generation can be tested later only if the short clips remain stable.

## V015 Planning Direction

Purpose: fast hand exchange with subtle fantasy micro-feedback.

Action:

- true-speed wrist slap / forearm parry / compact palm / shoulder pressure
- short contact and immediate rebound
- red/blue micro sparks at forearm collision
- silver-blue light streaks on Shuangji blocks
- dark-red ember traces on Fenshou pressure attacks
- no large VFX
- no new shockwave
- no shield dome
- no explosion
- continue fighting through the final second

Camera:

- medium close combat framing
- both characters visible enough for hands and upper body
- subtle handheld combat-follow micro-adjustment
- no spinning camera
- no beauty portrait drift

## V016 Planning Direction

Purpose: escalate from hand exchange to hand-foot coordination.

Action:

- one side cannot break through with hands
- front-foot cut-in
- diagonal outside-angle step
- low kick attempt
- shin check / lower-leg block
- knee lift to seal the line
- ankle / foot sweep threat without acrobatics
- upper-body parry continues during lower-body attack
- wet stone side splash from low steps
- robe hem flicks with knee lift

Camera:

- slightly wider or slight dip when legwork begins
- keep upper body to knees visible
- frontal rainy temple axis remains readable

## V017 Planning Direction

Purpose: disadvantage and counter-recovery beat.

Action:

- one fighter is pushed off-line or loses balance briefly
- shoe skids on wet stone
- water splashes sideways
- losing fighter stabilizes with a low stance or side step
- immediate counter-re-entry with palm/forearm and footwork pressure
- no pose-out
- no final freeze
- the end should feel like the fight continues into the next clip

Camera:

- short tracking or micro push
- keep both fighters in frame
- avoid fast cuts that destroy body mechanics

## Reference Strategy For Future Packages

Use upload-safe JPG refs as active image references because original PNG refs caused upload failures.

Active future ref candidates:

- Fenshou upload-safe identity JPG:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg
- Shuangji upload-safe identity JPG:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg
- Temple upload-safe scene JPG:
  G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg

Do not use V009/V010/V011/V012/V013 frames as visual refs.

Use V014-R02 as text baseline and optional action-rhythm observation, not as a mandatory visual reference in the first V015 package.

If video reference is considered later, record it as a separate experiment because it increases upload complexity.

## Duration Strategy

- Each clip: 4s-5s.
- Total edited section: 10s-15s.
- Avoid one-shot 15s generation as first attempt.
- If a single 10s clip is tested later, it must include internal action progression and camera variation.

## Speed Strategy

- Baseline true speed.
- Optional 10%-20% faster perceived rhythm.
- No whole-clip slow motion.
- Micro hit-stop only at key contact points.
- Local speed diagnostic can be done later after download if needed.

## Fantasy / Particle Constraints

Allowed:

- micro sparks
- silver-blue short light streaks
- dark-red ember traces
- cold glowing rain splashes
- brief light flicker at contact
- subtle particle residue that lasts less than 0.2s

Forbidden:

- giant shockwave
- second explosion
- circular water shield
- energy shield dome
- full-body aura burst
- flying
- big jump
- big flying kick
- acrobatic spin kick
- weapons
- sword
- spear

## Identity And Safety Constraints

- exactly two characters: Fenshou and Shuangji
- no male-coded Shuangji
- no white-haired male cultivator Shuangji
- no role swap
- no duplicate characters
- no third person
- no extra limbs
- no fused bodies
- no text/watermark/logo

## Recommended Next Steps

A. Prepare V015 package only, no submit.

B. Prepare V015/V016/V017 package set only, no submit.

C. Run local V014-R02 speed diagnostics at 1.10x and 1.20x, no Dreamina.

D. Pause and keep V014-R02 as positive candidate.

Recommendation: prepare V015 package first, then review it. After V015 passes, prepare V016 and V017 separately. Do not create all three submit packages at once unless the human explicitly asks.

## Safety Boundaries

- No Dreamina command was run.
- No submit/query/download happened.
- No media was created or staged.
- `.vs/` was not staged.
- V013 shot record was not modified.
- V014-R02 shot record was not modified.
- No submit-ready V015/V016/V017 manifests were created.
- dreamina_submit_allowed=false in the structured plan.
- human_review_required=true in the structured plan.

Final verdict:
SHOT_02_LONG_FAST_COMBAT_MULTI_CLIP_PLAN_READY
