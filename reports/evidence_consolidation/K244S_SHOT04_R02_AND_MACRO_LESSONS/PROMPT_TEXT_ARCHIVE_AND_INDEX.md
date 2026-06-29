# Prompt Text Archive and Index

## Purpose

This archive indexes the main SHOT-04 / SHOT-04 R02 prompts used in the K185-K244 route chain. It is evidence-only for ChatGPT Pro Extended Source synthesis. It does not authorize Dreamina, submit, query, download, retry, resubmit, media creation, package edits, prompt edits, manifest edits, or Source edits.

## Entry Count

`prompt_archive_entries=8`

## Entry 1 - K185/K190 Route A Multimodal2Video Prompt

- phase: K185 package, K187 submit, K188 query, K189 download, K190 visual failure
- asset_id: `SHOT-04-V001`
- variant_id: `routeA_railing_lattice_impact_rebound`
- task_type: `multimodal2video`
- model_version: `seedance2.0_vip`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-V001_routeA_railing_lattice_impact_rebound_no_submit_prompt.txt`
- prompt sha256: `dfbbc3c03ceede3c134d5464aaad8faf5bdcf38ddbe5cbf8277e6abcc70517e1`
- word count: `657`
- outcome: technical success, downloaded video, visual failure in K190
- why important: K190 showed that package review and clause-level Source compliance did not guarantee visual success when the prompt was too reference-duty / audit oriented.

First sentence:

```text
@FENSHOU_IDENTITY_REF:
Use only for Fenshou identity: black-red male fighter face, hair, armor, silhouette, and costume language.
```

Core action paragraph:

```text
This is one clear architecture-as-combat interaction: Fenshou drives Shuangji's guard and shoulder-back into the right-side railing / wooden lattice, the local structure reacts only at the exact contact point, Shuangji rebounds quickly and counters, and Fenshou recoils and re-enters instead of holding her pinned.
```

Timing paragraph:

```text
0.00s-0.25s: First contact. Fenshou's shoulder and forearm crash into Shuangji's guard near the right-side railing / lattice. Shuangji's torso turns from the impact and her rear foot skids on the wet stone.

0.25s-0.90s: Shuangji redirects the first pressure line. Fenshou recoils half a beat and immediately re-enters with a short, hard shoulder-line pressure. No slow display. No sustained shove.

0.90s-1.80s: Fenshou compresses Shuangji's guard toward the railing / lattice. The railing / lattice is still intact and standing. No crack or splinter appears before body / guard contact.

1.80s-2.80s: Architecture contact beat. Shuangji's shoulder-back and guard touch the railing / lattice. Only the exact contact point flexes locally; a rain / water burst and two tiny splinters move outward in the same force direction. Optional very short hairline mark at the contact point only. No railing collapse.

2.80s-3.80s: Rebound beat. Shuangji rebounds off the railing / lattice and counters into Fenshou's guard or shoulder line. Fenshou recoils, turns off-line, and re-guards while staying engaged.

3.80s-5.00s: Re-entry and cut. Both fighters continue attack / defense / rebound motion. Final frame cuts mid-exchange. No pose-out, no idle tail, no stare-down.
```

Negative constraints paragraph:

```text
Core negative constraints:
No third person. No duplicate Fenshou. No duplicate Shuangji. No role swap. No body fusion. No extra limbs. No weapons. No flying. No giant jump. No roof route. No wall run. No whole temple destruction. No railing collapse. No wall collapse. No unrelated column breakage. No random background damage. No crack before contact. No sustained wrestling hold. No static pushing pose. No beauty pose. No Shuangji masculinization. No text. No watermark.
```

## Entry 2 - K197T/K202 Architecture-Only Wall-Panel Prompt

- phase: K197T package, K198 review, K199 submit, K200 query, K201 download, K202 visual review
- asset_id: `A-SC-TEMPLE-SIDE-WALL-PANEL-002`
- variant_id: `text2image_wall_panel_target_ref`
- task_type: `text2image`
- model_version: `4.7`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/A-SC-TEMPLE-SIDE-WALL-PANEL-002_text2image_wall_panel_target_ref_no_submit_prompt.txt`
- prompt sha256: `1f25b55c4788fef419b9f9a3ab0289ee4f1e44e59efdff7f4fe164d7cd763e19`
- word count: `203`
- outcome: success; image downloaded and kept as architecture reference only
- why important: this noncombat architecture-target prompt succeeded and became the visual wall-panel reference for later R02 work.

Full prompt:

```text
Empty rainy ancient temple side corridor, with a clear dark wet wooden wall-panel / wooden lattice wall target on the right-midground, and an open wet stone skid zone directly in front of it.

The wall target is a stable vertical side-wall surface made of dark rain-soaked wood, with visible frame lines, rectangular wooden panels, and subtle lattice structure. It is close and readable enough to become a future body-impact reference surface, but this image shows no impact yet. The wall is intact, standing, and undamaged.

The floor in front of the wall is open wet stone, with shallow rain puddles, reflective stone texture, and enough empty midground space for two fighters to be added later. The corridor has wooden eaves, side pillars kept away from the wall target, cold gray-blue rain light, wet wood, wet stone, low-saturation cinematic wuxia atmosphere, Chinese ancient temple architectural material language, semi-realistic 3D environment art.

Architecture-only clean reference image. No people, no human silhouettes, no warriors, no monks, no guards, no animals, no weapons as focus, no fighting, no wall impact, no cracks, no splinters, no broken wall, no collapse, no fire, no explosion, no magic effects, no text, no watermark, no labels, no poster layout, no concept sheet.
```

## Entry 3 - K211/K220B Wall-Panel Shoulder-Check Video Prompt

- phase: K211 fixed prompt, K217 submit, K218 query, K219 download, K220B visual failure
- asset_id: `SHOT-04-R02_wall_panel_shoulder_check_rebound_no_submit`
- variant_id: `wall_panel_shoulder_check_rebound`
- task_type: `multimodal2video`
- model_version: `seedance2.0_vip`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual_SHOT-04-R02_wall_panel_shoulder_check_rebound_prompt.txt`
- prompt sha256: `609447d1cc36a908d70410e0d0c2806e0aa717d853b24c47ea4ae23ac7c17d22`
- word count: `832`
- outcome: technical success and downloaded MP4, then visual failure in K220B
- why important: proves video route can return media but still fail the visual action target.

First sentence:

```text
[DRAFT NO-SUBMIT PROMPT - HUMAN REVIEW REQUIRED]
This draft is not final and not locked.
```

Core action paragraph:

```text
Result-first action target:
Fenshou drives an explosive shoulder-check into Shuangji's crossed guard. Shuangji absorbs the hit, slides backward, and her right shoulder / upper back is driven into a mid-height wet wooden wall panel. The impact center is between pillars and must remain visible; the fighters' bodies must not hide the wall impact center. The wall reacts only after Shuangji's shoulder / upper-back contact, with localized flex, short cracks, small splinters, and rain spray. Shuangji immediately rebounds from the wall and re-enters guard. This is a compact wall-impact combat beat, not a building-destruction shot.
```

Timing paragraph:

```text
0.00-0.70s: The shot begins already in motion. Fenshou is advancing from the corridor side with compressed knees, rear-foot drive, hip-to-shoulder force, and forward shoulder pressure. Shuangji is close in front of the wall, crossed forearms raised, female-coded face and hairstyle stable. No waiting pose.

0.70-1.60s: Fenshou's shoulder and forearm collide with Shuangji's crossed guard. The hit has a clear body result: Shuangji's guard compresses, shoulders jolt, torso shifts backward, and shoes skid on the wet stone floor. Rain sprays from the point of contact and the floor.

1.60-2.70s: Shuangji is driven backward into the wall panel between pillars. Her right shoulder / upper back hits the wet wooden panel at mid-height. The wall flexes only at the impact center, with short cracks, tiny splinters, and rainwater shaken loose after contact. Keep the wooden wall intact overall. Do not collapse the wall.

2.70-3.80s: The hit-stop lasts only at the contact moment, about 0.10-0.15 seconds. Shuangji immediately rebounds from the wall, drops her weight, and re-enters guard. Fenshou follows with pressure but does not launch a new giant effect. Both fighters remain grounded and physically connected to the wet floor.

3.80-5.00s: The camera holds the side-wall corridor geography clearly: wall panel behind Shuangji, Fenshou in front/side pressure, pillars and wet stone floor visible. The action ends in continued close-range combat readiness, not a static poster. The wall damage remains localized and causally tied to Shuangji's shoulder / upper-back impact.
```

Negative constraints paragraph:

```text
Negative constraints:
No giant spherical shockwave, no second explosion, no magic shield, no circular water wall, no flying, no big jump, no wall-run showcase, no weapons, no modern city, no third person, no duplicate characters, no extra fighters, no extra limbs, no body fusion, no gender drift, no role swap, no long slow-motion posing, no static poster ending, no final-frame language, no locked-frame language, no text, no watermark.
```

## Entry 4 - K223 Four-Ref Image2Image Micro-Impact Prompt

- phase: K223 package, K224 review, K225 submit, K226 query failure
- asset_id: `SHOT-04-R02-KF-MICRO-IMPACT-001`
- variant_id: `micro_impact_contact_keyframe`
- task_type: `image2image`
- model_version: `4.7`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-MICRO-IMPACT-001_contact_keyframe_no_submit_prompt.txt`
- prompt sha256: `222bd10622383535dcd817609d8b163ee0038151ff11b9d06cd5224f3c454e40`
- word count: `405`
- outcome: valid submit, remote final-generation failure, no image result
- why important: first keyframe-first route failed remotely despite result-first wording and package review.

Full prompt:

```text
Fenshou lands one short explosive shoulder-check into Shuangji's crossed guard and drives her shoulder-back into the wet wooden wall panel at the hit-stop moment. Her upper back hits the panel hard; the wall panel makes only a shallow local dent and short crack at the exact contact point; rainwater bursts outward and two or three tiny splinters fly in the force direction; Shuangji is not embedded in the wall; the wall does not collapse.

Create a single cinematic still keyframe, not a video sequence. The image is frozen at the decisive impact moment. Fenshou is on the left-midground, lunging rightward with his shoulder line and forearm driving into Shuangji's crossed guard. Shuangji is on the right-midground, knees bent, rear foot skidding on the wet stone floor, crossed guard compressed inward, right shoulder and upper back visibly contacting the wet wooden wall panel.

The wall contact point must be readable. The local dent and short crack appear exactly behind Shuangji's right shoulder / upper back, not elsewhere on the wall. The wet wooden wall panel remains standing and intact except for the small local contact mark. Rain droplets and tiny splinters move from right to left / outward from the impact point following the force direction.

Use the wall-panel architecture reference only for the rainy temple side corridor, wet wooden panel, wet stone floor, pillars, and cold blue rainy lighting. Use the Fenshou reference only for black-red armor, male-coded Fenshou identity, and silhouette. Use the Shuangji identity anchor as the highest-priority Shuangji face and upper-body identity reference. Use the Shuangji full-body reference only for silver-blue costume silhouette, lower-body armor, and body proportions.

Camera: 16:9 medium or medium-wide shot, three-quarter front-left angle, eye-level or slightly low. Both characters are in the midground, in the same physical plane. Keep the exact wall contact point visible between bodies. Both faces may remain readable, but the physical impact result is higher priority than perfect portrait beauty.

Rainy ancient temple side corridor, wet dark wooden panels, wet stone floor, cold gray-blue low-saturation rain light, cinematic semi-realistic 3D wuxia action keyframe.

No body-wall fusion. No embedding into the wall. No wall collapse. No large hole. No full wall breakage. No magical shockwave replacing physical contact. No energy blast. No gore. No severe injury. No wrestling hold. No static slow push. No pose-out. No extra characters. No duplicate bodies. No extra limbs. No text, watermark, labels, poster layout, or concept sheet.
```

## Entry 5 - K227R Three-Ref Image2Image Micro-Impact Prompt

- phase: K227R package, K228 review, K229 submit, K230 query failure
- asset_id: `SHOT-04-R02-KF-MICRO-IMPACT-001-R02`
- variant_id: `micro_impact_contact_keyframe_3ref_r02`
- task_type: `image2image`
- model_version: `4.7`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-MICRO-IMPACT-001-R02_contact_keyframe_3ref_no_submit_prompt.txt`
- prompt sha256: `9d02922f13935dca8f51666b166d7cd4f418158045d8286fbc66096a286bb56e`
- word count: `311`
- outcome: valid submit, remote final-generation failure, no image result
- why important: ref-count reduction did not solve the exact body-wall contact failure.

Full prompt:

```text
Fenshou lands one compact explosive shoulder-check into Shuangji's crossed guard, driving her shoulder-back against the wet wooden wall panel at the hit-stop moment. The panel flexes with a shallow contact dent and a short hairline crack exactly behind her upper back; rainwater flicks outward and two tiny splinters fly along the force line. Shuangji stays separate from the wall; the wall remains standing.

Create one cinematic still keyframe, frozen at the decisive impact. Fenshou is in the left-midground, lunging rightward, shoulder line forward, forearm pressing into Shuangji's crossed guard. Shuangji is in the right-midground, knees bent, crossed guard compressed inward, right shoulder and upper back visibly touching the wall panel. Her rear foot skids on the wet stone floor.

Keep the exact wall contact point readable between the two bodies. The dent, hairline crack, rain splash, and tiny splinters must originate only from that contact point, not elsewhere on the wall.

Use the wall reference only for the rainy temple side corridor, wet wooden panel, pillars, wet stone floor, and cold blue rain light. Use the Fenshou reference only for black-red armor, male-coded identity, and silhouette. Use the Shuangji identity reference as the main face and upper-body identity anchor; describe her silver-blue costume continuity through the prompt, without an extra full-body reference.

Camera: 16:9 medium or medium-wide shot, three-quarter front-left angle, eye-level or slightly low. Both characters are in the same physical plane. Faces may remain readable, but the impact result has priority over portrait beauty.

Rainy ancient temple corridor, wet dark wooden panels, cold gray-blue low-saturation lighting, cinematic semi-realistic 3D wuxia action keyframe.

No body-wall fusion, no embedding, no wall collapse, no large hole, no magic shockwave, no energy blast, no gore, no severe injury, no wrestling hold, no static slow push, no pose-out, no extra characters, no duplicate bodies, no extra limbs, no text, no watermark.
```

## Entry 6 - K232 Softened Text2Image Wall-Contact Prompt

- phase: K232 package, K233 review, K234 submit, K235 query failure
- asset_id: `SHOT-04-R02-KF-SOFT-CONTACT-T2I-001`
- variant_id: `softened_contact_text2image_geometry_probe`
- task_type: `text2image`
- model_version: `5.0`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-SOFT-CONTACT-T2I-001_text2image_no_submit_prompt.txt`
- prompt sha256: `7531b10db0fe2dbedbf68682557b8f158c8282cf538a79bbcddb539bdbdc6d6b`
- word count: `204`
- outcome: valid submit, remote final-generation failure, no image result
- why important: removing active refs and softening wall-contact language still failed.

Full prompt:

```text
One cinematic still keyframe in a rainy ancient temple side corridor: Fenshou, a black-red armored male warrior, drives from the left-midground into Shuangji's crossed guard with compact shoulder-and-forearm pressure. Shuangji, a silver-blue armored female warrior, is in the right-midground with knees bent, crossed guard compressed inward, her upper back and right shoulder pressed against a rain-soaked wooden wall panel. The wall remains intact.

The action geometry must be clear: Fenshou's forward shoulder line, his forearm pressure, Shuangji's crossed guard absorbing the force, her rear foot skidding on the wet stone floor, and the exact wall contact zone visible behind her shoulder-back. At the contact zone, show rain splash, a shallow wet pressure mark on the wood, and droplets moving along the force direction.

Environment: wet dark wooden side-wall panels, temple pillars, cold gray-blue rain light, reflective stone floor, semi-realistic 3D wuxia film style. Camera: 16:9 medium-wide, three-quarter front-left angle, eye-level or slightly low.

This is an action keyframe, not a poster layout or character sheet. No wall collapse, no open wall gap, no magic blast, no shockwave, no body-wall fusion, no embedding, no gore, no severe injury, no extra characters, no duplicate bodies, no extra limbs, no text, no watermark.
```

## Entry 7 - K238T Near-Wall Guard-Clash Text2Image Prompt

- phase: K238T package, K239 review, K240 submit, K241 query failure
- asset_id: `SHOT-04-R02-KF-NEAR-WALL-GUARD-CLASH-T2I-001`
- variant_id: `near_wall_guard_clash_text2image_geometry_probe`
- task_type: `text2image`
- model_version: `5.0`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-KF-NEAR-WALL-GUARD-CLASH-T2I-001_text2image_no_submit_prompt.txt`
- prompt sha256: `782608075c05026daa6f55f247e5f407c0c661ad18f993037be36374d5e921a8`
- word count: `222`
- outcome: valid submit, remote final-generation failure, no image result
- why important: removing body-wall contact and wall damage still failed remotely, broadening the diagnosis to dual-character close-combat staging brittleness.

Full prompt:

```text
One cinematic action keyframe in a rainy ancient temple side corridor: Fenshou, a black-red armored male warrior, drives from center-left toward Shuangji with compact shoulder-and-forearm pressure into her crossed guard. Shuangji, a silver-blue armored female warrior, braces in center-right near a dark wooden corridor wall, close to the wall but not touching it.

The crossed guard is compressed at the center of the frame. Shuangji's rear foot skids across the wet stone floor; rain sprays from the floor and guard pressure; her cloak, hair, and armor edges react to the force. Fenshou's body line pushes forward from left to right, while Shuangji bends her knees and twists into counter-readiness.

The wall stays intact behind Shuangji as background danger only, with no contact between her body and the wall. The main physical proof is guard compression, wet-floor skid, rain spray, and Shuangji's counter-ready twist.

Camera: 16:9 medium-wide, three-quarter front-left angle, eye-level or slightly low. Wet dark wooden side panels, temple pillars, reflective stone floor, cold gray-blue rain light, cinematic semi-realistic 3D wuxia action style.

This is an action keyframe, not a poster layout or character sheet. No body-wall contact, no wall hit, no wall mark, no wall breakage, no magic blast, no shockwave, no static pose, no extra characters, no duplicate bodies, no extra limbs, no text, no watermark.
```

## Entry 8 - K243V Near-Wall Guard-Clash Text2Video Prompt

- phase: K243V package, K244 review
- asset_id: `SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001`
- variant_id: `near_wall_guard_clash_text2video_motion_probe`
- task_type: `text2video`
- model_version: `seedance2.0_vip`
- prompt path: `productions/chi_yan_tian_qiong/prompts/manual/SHOT-04-R02-V-NEAR-WALL-GUARD-CLASH-T2V-001_text2video_no_submit_prompt.txt`
- prompt sha256: `092757a60297391e467c2f402ae6173dda8cae87267d1f24f5b25ee2fcd15b82`
- word count: `261`
- outcome: package review pass with high-risk notes; K245 has not been submitted
- why important: current package-readiness state and next live route candidate after repeated still/keyframe remote failures.

Full prompt:

```text
A 5-second cinematic semi-realistic 3D wuxia action video in a rainy ancient temple side corridor: from the first frame, Fenshou, a black-red armored male warrior, is already close in center-left, driving forward with compact shoulder-and-forearm pressure into Shuangji's crossed guard. Shuangji, a silver-blue armored female warrior, braces center-right near a dark wooden corridor wall, close to the wall but not touching it.

The action starts immediately with no long approach. Fenshou's body line drives left to right. Shuangji's crossed guard compresses under the pressure; her rear foot skids across the wet stone floor; rain sprays from the floor and guard contact; her cloak, hair, and armor edges snap from the force. Keep both fighters in a readable medium or medium-wide three-quarter view.

0.00s-0.10s: already close, pressure entering from center-left. 0.10s-0.35s: shoulder-and-forearm pressure meets crossed guard. 0.35s-0.65s: Shuangji skids backward near the wall without touching it, rain spray and guard compression visible. 0.65s-1.00s: brief pressure lock, knees bend, armor and cloak react. 1.00s-1.35s: Shuangji twists out of the pressure and coils for a counter. 1.35s-1.50s: cut-worthy mid-exchange action moment.

After the main contact, keep motion alive with guard separation, footwork adjustment, rain occlusion, camera vibration, and Shuangji counter-initiation. The wall remains intact behind her as background danger only.

No body-wall contact, no wall hit, no wall damage, no wall mark, no long approach, no static pose-out, no poster pose, no magic blast, no shockwave, no extra characters, no duplicate bodies, no extra limbs, no text, no watermark.
```
