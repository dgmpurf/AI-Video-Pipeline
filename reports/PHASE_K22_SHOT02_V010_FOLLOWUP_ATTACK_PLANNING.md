# PHASE_K22_SHOT02_V010_FOLLOWUP_ATTACK_PLANNING

- project: Chi Yan Tian Qiong
- shot: SHOT-02
- task_id: SHOT-02-V010
- package_concept: followup_forearm_clash_sidestep_counter
- status: planning_only_no_submit
- final_master: false
- locked: false

## Human Review Context

Human reviewed the SHOT-02 tight edit tests:

- TEST_B has the correct aggressive rhythm direction, but it does not pass final review.
- TEST_A is safer but still slightly slow.
- TEST_C is rejected.
- No final SHOT-02 combo is locked yet.

Why TEST_B is not final:

- Early frames have a different character/render style from the later shockwave material.
- Around the post-shockwave pullback, the camera moves backward while both characters look too static/frozen.
- A camera pullback is acceptable only if both fighters keep moving: sliding, recovering balance, guarding, redirecting force, or immediately starting the next exchange.

## V010 Purpose

SHOT-02-V010 should create the next active combat phrase after the shockwave beat. It is not another shockwave clip. The purpose is to replace frozen pullback energy with grounded body movement: footwork, balance recovery, force redirection, forearm contact, and the first short counter setup.

## Candidate Start Frames

Existing frames only were inspected. No new frames were created in this pass.

| Candidate | Path | Size | SHA256 | Notes |
|---|---|---:|---|---|
| V009 0.50s | `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_0p50s.jpg` | 23616 | `a1b0d94421fc7b47bc12258a7cc34f03bb1541d0c836163d0a756555f60f67ca` | More aggressive and earlier, but risks carrying too much shockwave/recovery ambiguity. |
| V009 1.00s | `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg` | 23924 | `adae6a1184e681e00fead33ba04ed53484ad7cef3ba94fa2165842ab9ddf3565` | Preferred. Best balance of post-shockwave timing, readable bodies, and room for active follow-up movement. |
| V009 1.50s | `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p50s.jpg` | 24668 | `7289947d7db9794442637dabed6f6bfb1510f738af70bfe611d246efbb558a1f` | Clearer recovery state, but risks feeling too settled/static as a start frame. |
| TIGHT_B contact sheet | `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_B_contact_sheet.jpg` | 66126 | `822a6171e85277c9a1e598655ecdfab18ab4b643597063bd3a25769e83d6c62f` | Useful rhythm reference only; not recommended as input image because it is a contact sheet. |

Preferred start frame:

- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg`

Backup start frame:

- `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_0p50s.jpg`

## V010 Action Concept

Concept label:

- post-shockwave forearm clash, sidestep deflection, short palm counter

Body-mechanics direction:

- The shockwave has just dispersed.
- Both fighters immediately continue moving instead of freezing.
- Fen Shou shifts weight forward; his rear foot pushes against the wet stone floor.
- Fen Shou's right shoulder drops slightly and his right forearm drives forward toward Shuang Ji's centerline.
- Shuang Ji slides her left foot backward and slightly toward screen right.
- Shuang Ji turns hips and torso sideways, places her left forearm against Fen Shou's wrist/forearm, and redirects the incoming force outward.
- Their forearms briefly cross and press against each other.
- Shoulders, elbows, wrists, hips, and feet visibly adjust.
- Shuang Ji sends a short right palm from in front of her chest toward Fen Shou's forearm or shoulder armor.
- Wet stone floor shows small water splashes from footwork.
- Hair and clothing whip briefly from fast movement.
- Keep real-speed action with only a tiny hit-stop at contact.

## Negative Constraints

- no new giant shockwave
- no weapons
- no flying
- no second explosion
- no frozen pullback
- no style shift
- no extra fighters
- no duplicate characters
- no body fusion
- no extra limbs
- no modern city
- no scene change
- no main hall frontal-axis change
- no poster reset
- no text or watermark

## Draft Execution Settings

- task_type: image2video
- provider: dreamina_cli
- model_version: seedance2.0_vip
- duration: 4
- video_resolution: 720p
- ratio: omitted
- input_count: exactly_one_image
- selected_input_image: `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg`
- command_contract_valid: true
- package_status: planning_only_no_submit
- final_edit_target: 0.8-1.5s

## Execution Recommendation

Package is ready for human review only. Do not submit yet.

Recommended review question:

- Does the selected V009 1.00s start frame give enough continuity while allowing V010 to produce active body/footwork movement?

If approved, submit only after explicit live-step authorization and command-contract preflight.

