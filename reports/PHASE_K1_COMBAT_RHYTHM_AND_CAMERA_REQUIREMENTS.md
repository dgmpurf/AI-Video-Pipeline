# PHASE K1: Combat Rhythm and Camera Requirements Planning Report

Date: 2026-06-18

## Scope

- Register the imported Combat Rhythm Planning agent report as a project planning report only.
- Input report: manual_imports/agent_reports/Combat Rhythm Planning.docx
- Output report: reports/PHASE_K1_COMBAT_RHYTHM_AND_CAMERA_REQUIREMENTS.md
- Classification: planning_reference / C-level external-informed planning.
- Stability status: pending project validation; do not treat as stable Source.
- Source policy: this report does not modify, replace, or promote any Source file.
- Execution policy: no Dreamina submit, query, download, media generation, runtime code change, or configs/providers.json change.

## Planning Status

- SHOT-02 official keyframe is already locked locally:
  productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- SHOT-02-V001 has been generated and registered as:
  - status: success_usable_candidate
  - usable_video_candidate: true
  - fallback_motion_clip: true
  - final_master: false
  - locked: false
- V001 role: stable low-motion extension / fallback motion clip, not the final high-impact combat rhythm.

## Project-Specific Corrections

The imported agent report is useful for planning, but the following project corrections override its timing and mode assumptions:

- Current Dreamina video duration can start from 1 second and duration is integer-based.
- For action highlight clips, do not default to 4-5 seconds.
- Recommended project timing:
  - 1-2s for impact/highlight beats.
  - 2-3s for quick combat transitions.
  - 4-5s for stable motion extensions.
  - 6-12s only for long movement, geography, or emotional pressure.
- Avoid weapon wording unless explicitly required by the locked reference or shot design.
- For SHOT-02-V002, first test image2video from the official locked keyframe.
- Use multimodal2video only if a CTRL-CAM reference or water-effect reference is introduced later.

## Combat Rhythm Summary

The planning report recommends a rhythm made of short high-impact beats, quick transitions, and occasional stable breathing moments. The key lesson for SHOT-02 is that the sequence should not rely on one long continuous generated fight. Instead, it should be built as modular clips with clear roles:

- Stable pose extension: holds continuity and preserves scene/character readability.
- Impact highlight: short, controlled, visually decisive.
- Reaction/follow-up: shows consequence without losing spatial clarity.
- Transition beat: connects to the next shot or changes visual pressure.

For this project, the highest priority is preserving the locked SHOT-02 keyframe composition: frontal main-hall axis, wet stone floor, exactly two characters, Fenshou left, Shuangji right, and one readable close-contact arm point.

## SHOT-02 Clip Breakdown

| Clip ID | Planning Role | Project Timing | Recommended Mode | Notes |
| --- | --- | --- | --- | --- |
| SHOT-02-V001 | Stable extension / fallback motion clip | Existing 5s generated clip, usable as a fallback; likely trim shorter in edit | image2video | Already registered as usable candidate. Keeps continuity but is not the final high-impact rhythm. |
| SHOT-02-V002 | First high-impact contact highlight | 1-2s preferred for first test | image2video from official locked keyframe | Focus on contact pressure, rain response, held bodies, and readable arm contact. Do not create a new fight sequence. |
| SHOT-02-V003 | Follow-up movement or reaction | 2-3s | image2video or frames2video if extra key poses exist | Use only after V002 direction is validated. Keep character identity and feet/floor contact stable. |
| SHOT-02-V004 | Optional transition to next combat beat | 2-3s, or longer only if geography must be shown | image2video, frames2video, or multimodal2video if references exist | Use for pull-back, pressure reset, or transition, not as an automatic next step. |

## Timing Guidance

Impact and highlight beats should be short. For SHOT-02-V002, begin with a 1-2 second image2video test rather than a 4-5 second default. The clip should read as a concentrated moment of pressure, not a complete exchange.

Quick combat transitions can use 2-3 seconds when the purpose is to connect one beat to the next. These are useful when a motion needs to start, resolve, and hand off without creating a full new choreography passage.

Stable motion extensions can use 4-5 seconds when the intent is to preserve a keyframe, hold mood, and gather usable atmospheric motion. SHOT-02-V001 belongs in this category.

Long clips of 6-12 seconds should be reserved for long movement, geography, or emotional pressure. They are not the default for close combat impact clips because extra duration increases drift, body fusion, and unintended action risk.

## Camera Technique Table

| Technique | Best Use | Risks | Project Recommendation |
| --- | --- | --- | --- |
| Locked hit-stop | Emphasize the exact contact moment while preserving pose clarity | Over-freezing can feel artificial; long holds can cause drift | Good candidate for V002 if phrased softly as a brief held pressure moment. |
| Micro handheld shake | Add subtle physical impact and rain atmosphere | Too much shake can break composition or cause viewer fatigue | Use only as very small vibration; keep main hall axis readable. |
| Slow push-in | Preserve composition while adding tension | Too much zoom can become a poster reset or lose the background | Safe for V002/V003 if extremely subtle. |
| Low-angle pressure | Increase power and mass in the contact pose | Too low may distort bodies or obscure feet | Use cautiously; official keyframe framing should remain the anchor. |
| Lateral dolly | Show footwork or a side-following motion | Can become side-scrolling/game-like | Avoid for V002 unless later tests prove it preserves the frontal main-hall anchor. |
| Short orbit | Add dimensionality around the contact | Orbit can cause scene/identity drift | Not recommended for first V002 test. Consider only with CTRL-CAM later. |
| Crash/snap zoom | Add impact punctuation | Can look comedic or generate artifacts | Avoid as default. If used later, keep very brief and controlled. |
| Whip pan | Transition between focal points | Can blur, disorient, or create new staging | Not recommended for V002. Save for later transition planning. |
| Pull-back reveal | Show aftermath or geography | Can weaken the close-contact beat | Better suited for V004 or later geography shots. |
| Speed ramp | Highlight impact and resume motion | Overuse can feel synthetic and destabilize limbs | Use only as a brief pressure/slowdown concept, not a complex timing demand. |

## CTRL-CAM Library Proposal

The imported report proposes building a generic CTRL-CAM reference library for complex camera paths. This is useful as future planning only. It is not required for SHOT-02-V002 unless a later package explicitly introduces CTRL-CAM or multimodal references.

Recommended generic library candidates:

| Ref ID | Proposed Purpose | Suggested Duration | Project Use |
| --- | --- | --- | --- |
| CAM-001_LockedHitStop | Static or nearly static contact hold with a brief pause | 3-4s | Reference hit-stop timing without scene drift. |
| CAM-002_MicroShake_Short | Subtle handheld vibration | 3-5s | Add physical pressure while retaining framing. |
| CAM-003_SlowPushIn | Very slow forward camera movement | 4-6s | Stable tension extension from locked keyframes. |
| CAM-004_LateralDolly | Smooth side movement | 4-8s | Use only when side movement is desired and not side-scrolling. |
| CAM-005_ShortOrbit45 | Limited 30-45 degree orbit | 4-5s | Later reaction/follow-up tests; not first V002. |
| CAM-006_PullBackReveal | Controlled dolly-out | 5-7s | Aftermath or geography reveal. |
| CAM-007_WaterRippleReference | Rain puddle ripple / splash reference | 2-5s | Candidate multimodal reference if V002 needs water-effect control. |

CTRL-CAM references should avoid IP-specific imagery, branded content, actor likeness dependencies, and busy backgrounds. Use abstract camera movement, neutral silhouettes, or clean environmental motion only.

## Generation Mode Recommendations

| Mode | Use When | SHOT-02 Recommendation |
| --- | --- | --- |
| image2video | Starting from one locked keyframe and preserving composition is the main priority | First choice for SHOT-02-V002. Use the official locked keyframe as the single image. |
| frames2video | Multiple validated key poses exist and need interpolation | Consider later for follow-up motion if new validated frames are created. |
| multimodal2video | Additional references are needed for camera path, water effects, or other controlled motion | Use only if CTRL-CAM or a water-effect reference is introduced later. Not first V002 default. |

Important CLI constraint already established in the project: image2video uses exactly one --image and should not set ratio.

## SHOT-02-V002 Prompt Direction

SHOT-02-V002 should be planned as a short, controlled image2video test from the official locked SHOT-02 keyframe.

Prompt direction:

- Use the locked keyframe as the only visual anchor.
- Preserve the frontal main-hall axis, main door, stone steps, rain, wet stone reflections, and cold gray-blue lighting.
- Preserve exactly two characters: Fenshou on the left and Shuangji on the right.
- Preserve the single clear arm contact or near-contact point.
- Preserve readable separated bodies and both feet planted on wet stone.
- Add only a brief increase in contact pressure, rain movement, puddle ripples, small clothing/hair motion, and slight water response around the contact/feet.
- Keep duration short: 1-2 seconds for the first V002 test.
- Avoid weapon wording unless explicitly required.
- Avoid a new strike, jump, spin, chase, cut to another angle, large camera orbit, or second exchange.

Potential safe wording direction:

```text
Use the locked SHOT-02 keyframe as the only first frame and composition anchor. Preserve the rainy ancient temple main hall frontal axis, centered door, stone steps, wet stone floor reflections, and the two-character close-contact pose. Fenshou remains on the left, Shuangji remains on the right. Keep one clear arm contact or near-contact point in the center, with separated readable bodies and both feet planted on the wet stone floor. Create a very short 1-2 second motion highlight: rain continues, puddles ripple, clothing and hair move slightly, the contact point shows a brief held pressure and small water response. Camera stays locked or makes an extremely subtle push-in. No new characters, no duplicated bodies, no extra limbs, no scene change, no side-scrolling movement, no large repositioning, no new exchange, no text or watermark.
```

This is only a direction note. Do not create the SHOT-02-V002 package from this K1 registration step.

## Risks and Mitigation

| Risk | Why It Matters | Mitigation |
| --- | --- | --- |
| Character drift or fusion | Close-contact motion can merge bodies or change identity | Use short duration, preserve one contact point, keep bodies separated and readable. |
| Extra limbs | Fast contact motion can hallucinate hands/arms | Ask for one clear contact point and separated bodies; keep action restrained. |
| Unintended weapon or prop focus | Ambiguous combat language can create unwanted objects | Avoid weapon wording unless the shot explicitly requires it. |
| Side-scrolling composition | Lateral movement can flatten the main-hall staging | Keep the frontal main-hall axis and depth visible. |
| Overlong combat clip | Longer duration increases drift and unintended choreography | Use 1-2s for V002 impact/highlight test. |
| Camera over-motion | Orbits, whip pans, and crash zooms can break continuity | Start with locked camera or extremely slow push-in. |
| Water effect becoming fantasy explosion | Shockwave language can drift into magical effects | Prefer grounded rain, ripples, droplets, and small water response. |
| V001 mistaken as final master | V001 is usable but low motion | Keep V001 as fallback_motion_clip=true and final_master=false. |

## External References Named In Imported Report

The imported report cited external filmmaking/editing sources for general planning context. These citations are retained as input-report provenance only and are not promoted to project Source:

- Frame.io: editing action scenes and cutting on movement.
- StudioBinder: low angle shots, camera movement types, zoom/crash zoom usage, and tracking shots.
- Adobe: speed ramping / time remapping overview.

## Decision

- Combat rhythm report registered as planning_reference only.
- Classification: C-level external-informed planning, pending project validation.
- No Source file was modified.
- No SHOT-02-V002 package was created.
- No Dreamina action was run.

PHASE_K1_COMBAT_RHYTHM_PLANNING_RECORDED
