# PHASE K83 - SHOT-02-V018 Upload-Safe Hard-Impact Fast Upper-Body Package Ready

## Why V018 Is Being Prepared

SHOT-02-V017 was reviewed as positive-with-notes but slow/soft. V017 improved camera, framing, two-character combat readability, and upper-body focus compared with V016, but it still lacked hard impact.

Human review diagnosis:

- Speed contributes to the weak impact.
- Prompt/action design also contributes.
- V017 over-emphasized checks, redirects, deflections, and controlled exchange motifs.
- V018 should focus on hard-impact fast upper-body combat, not particle improvement.

## Current Policy State

- V013 CUT01 remains the locked current SHOT-02 passed segment.
- V014-R02 remains the stronger positive enhancement candidate.
- V015 remains a rejected failure reference.
- V016 remains positive-with-notes / possible edit-insert candidate.
- V017 is positive-with-notes but slow/soft; it is not final and not locked.
- V018 is an optional correction experiment, not an automatic replacement.
- V018 cannot replace locked V013 CUT01 unless the human explicitly approves a future replacement.

## V018 Purpose

- Shot id: `SHOT-02-V018`
- Variant id: `uploadsafe_hard_impact_fast_upperbody`
- Task type: `multimodal2video`
- Provider: `dreamina_cli`
- Model version: `seedance2.0_vip`
- Duration: `5`
- Video resolution: `720p`
- Ratio: `16:9`
- Submit allowed: `false`
- Query allowed: `false`
- Download allowed: `false`
- Final master: `false`
- Locked: `false`
- Human review required: `true`

V018 is a hard-impact fast upper-body correction clip for the possible SHOT-02 long fast-combat multi-clip section.

## V018 Action Summary

V018 should show fast collision-based upper-body close combat.

Timing intent:

- `0.00s-0.30s`: immediate close-range start, no stare-down.
- `0.30s-1.50s`: at least four quick hard contact beats.
- `1.50s-2.60s`: guard-collapse / forced-off-line phase.
- `2.60s-3.60s`: counter-re-entry phase.
- `3.60s-4.30s`: one clear strong contact beat with an extremely short key-contact hit-stop.
- `4.30s-5.00s`: rapid continuation through final second, no pose-out.

## V018 Force / Impact Summary

Required impact language:

- crash into guard
- jam the forearm line
- snap contact and rebound
- guard buckles inward
- shoulder jolts back
- torso forced off-line
- rear foot skids on wet stone
- palm strike lands on armor / shoulder guard
- forearm collision stops abruptly then rebounds
- defender forced half-step back
- attacker immediately re-enters
- hit-stop only at contact, then fast continuation

Every contact beat should include:

- attack path
- contact point
- defender reaction
- environment feedback
- immediate rebound

Avoid:

- gentle check
- soft redirect
- elegant deflection
- slow parry
- long bind
- held forearm contact
- push-hands rhythm
- demonstration-style exchange

## V018 Particle / VFX Summary

Particle / VFX should be lower priority than impact.

Allowed only as tiny contact/environment feedback:

- tiny contact flecks from armor/forearm collision
- brief cold rain mist cut by force
- tiny dark-red ember dust at Fenshou contact
- tiny silver-blue frost specks at Shuangji block edge
- particles fade within `0.2s`

Forbidden:

- large glow
- aura
- spell
- shield
- circular water shield
- energy dome
- giant shockwave
- second explosion
- large magic beam

## V018 Camera / Rhythm Summary

- Medium close combat framing.
- Both characters visible enough for hands, shoulders, torsos, and partial footwork.
- Rainy ancient temple frontal axis remains readable.
- Subtle combat-following micro-adjustment.
- Slight micro-push allowed.
- No spinning camera.
- No beauty portrait drift.
- No static poster drift.
- No fast cuts that destroy body mechanics.
- No horizontal side-scroller game look.
- No stage-sparring wide pose showcase.

## Reference-Duty Map

Use exactly three upload-safe JPG references as active image references.

1. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-A-SUBJECT-001_fenshou_uploadsafe_q92.jpg`
   - Duty: Fenshou identity only.
   - Use for black/red armored male warrior identity: face, hair, armor, silhouette, body type, aggressive forward pressure.

2. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-CH-B-IDENTITY-002_shuangji_identity_uploadsafe_q92.jpg`
   - Duty: Highest-priority Shuangji female identity protection only.
   - Use for female face, female identity, silver-blue high ponytail, blue-silver armor collar/shoulders, white-blue robe panels, calm sharp expression.
   - Do not use as action/rhythm/scene/camera reference.

3. `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/working_refs/upload_safe/SHOT-02-V014-R02/A-SC-TEMPLE-COURTYARD-004_scene_uploadsafe_q92.jpg`
   - Duty: Rainy ancient temple courtyard scene/world only.
   - Use for frontal main-hall axis, wet stone floor, cold gray-blue rain light, cinematic environment.
   - Do not use as character identity reference.

## Active Reference Exclusions

Confirmed not active visual references:

- Original PNG locked refs.
- V014-R02 MP4/contact sheet.
- V015 MP4/contact sheet.
- V016 MP4/contact sheet.
- V017 MP4/contact sheet.
- Prior V009/V010/V011/V012/V013 frames/media.
- V013 CUT01/CUT02 frames/contact sheets.

Reason: V014-R02, V016, and V017 are text/action-quality references only. V015 is a failure reference only. V018 does not increase upload complexity by adding video/media refs.

## Package Files

- Manual prompt: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V018_uploadsafe_hard_impact_fast_upperbody_prompt.txt`
- Prompt JSON: `productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V018_uploadsafe.json`
- Manifest CSV: `productions/chi_yan_tian_qiong/manifests/production_multimodal2video_SHOT-02-V018_uploadsafe.csv`
- Shot record: `productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V018_uploadsafe.json`

## Package Validation Checklist

- Prompt JSON parses.
- Shot record JSON parses.
- Manifest CSV reads.
- All three upload-safe JPG selected reference paths exist locally.
- Manifest contains exactly three active image references.
- Manifest uses upload-safe JPG refs, not original PNG locked refs.
- Prompt JSON and manifest do not include prior V009/V010/V011/V012/V013 frame/media paths.
- V014-R02, V015, V016, and V017 media/contact sheets are not active refs.
- `submit_allowed=false`.
- `final_master=false`.
- `locked=false`.
- Manual prompt includes upload-safe `@` reference-duty map.
- Manual prompt requires at least four quick hard contact beats within first `1.5s`.
- Manual prompt includes attack path + contact point + defender reaction + environment feedback + rebound for contact beats.
- Manual prompt includes hard-contact vocabulary: crash into guard, jam the forearm line, snap contact and rebound, guard buckles inward, shoulder jolts back, torso forced off-line, rear foot skids, armor plate shake.
- Manual prompt avoids overusing soft terms: gentle check, soft redirect, elegant deflection, slow parry, long bind, held forearm contact, push-hands rhythm, demonstration-style exchange.
- Manual prompt says particles are lower priority than hard impact.
- Negative constraints include slow-motion-only impact, soft fast motion, held-contact choreography, push-hands rhythm, final pose-out, male-coded Shuangji, role swap, duplicate characters, extra limbs, weapons, flying, big jump, big flying kick, acrobatic spin kick, giant shockwave, second explosion, shield/dome, text, watermark.

## Safety Confirmation

- No Dreamina command was run.
- No submit/query/download happened.
- No media was created or edited.
- No media was staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- V013 shot record was not modified.
- V014-R02 shot record was not modified.
- V015 shot record was not modified.
- V016 shot record was not modified.
- V017 shot record was not modified.
- V018 `final_master=false`.
- V018 `locked=false`.
- Human review is required after any future download.

## Final Verdict

SHOT_02_V018_UPLOADSAFE_HARD_IMPACT_FAST_UPPERBODY_PACKAGE_READY_NO_SUBMIT
