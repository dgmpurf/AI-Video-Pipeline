# SHOT-02-V001 Image2Video Readiness Review

Task: SHOT-02-V001
Shot: SHOT-02
Status: success_usable_candidate

## Source Keyframe

- Official keyframe: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Keyframe source task: SHOT-02-KF-002-R02_safe
- Lock status: source keyframe locked as official SHOT-02 keyframe

## Dreamina Settings

- task_type: image2video
- model_version: seedance2.0_vip
- duration: 5
- video_resolution: 720p
- ratio: omitted; image2video infers ratio from input image
- image input count: exactly 1

## Submit Metadata
- submit_id: b3c0d827-29e7-4c1c-b928-c044b765b15b
- logid: 202606172244121692540470081522881
- submit status: success
- query status: success
- queue status: Finish
- credit_count: 70
- run_dir: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V001_20260617_230616
- output_path: productions/chi_yan_tian_qiong/runs/live/SHOT-02-V001_20260617_230616/SHOT-02-V001_stable_first_clash_motion.mp4
- output_exists: true
- output_size_bytes: 7158147
- output_sha256: 9fb9e5a3734c374b64f098a9e9ff0972463e52cb68ad11f96f4611e3d2a2fefe
- video_duration: 5.016666666666667
- video_width: 1280
- video_height: 720
- video_fps: 24.119601328903656
- frame_count: 121
- probe_method: opencv

## Candidate Registration

- usable_video_candidate: true
- fallback_motion_clip: true
- final_master: false
- locked: false
- human_decision: SHOT-02-V001 is usable as a stable fallback / usable video candidate, but not the final high-impact combat beat.
- motion_role: stable low-motion extension; fallback motion clip; not final high-impact combat rhythm.

## Source Rules Applied

- Video prompt must define camera, blocking, eyeline, movement path, locked elements, and start state.
- Image2video uses exactly one --image and does not set --ratio.
- Single keyframe light-motion extension is appropriate for stable ambient motion and extremely slow push-in.
- Complex new fight choreography and complex camera motion are avoided.

## Readiness Checks

- Preserve exact locked keyframe composition.
- Preserve exactly two characters: Fenshou left, Shuangji right.
- Preserve central close-range arm contact or near-contact point.
- Preserve separated readable bodies and grounded feet.
- Preserve frontal main hall axis, centered door, stone steps, rain, wet reflections.
- Motion limited to rain, hair, robe edges, puddle ripples, tiny splashes, slight pressure tension, and optional extremely slow push-in.

## Risk Notes

- This is not a new fight sequence.
- Avoid any second exchange, jump, spin, chase, large repositioning, weapon emphasis, camera orbit, scene cut, or poster reset.
- Accepted keyframe risks remain present as source context: chain/whip-like hand element and slight horizontal-duel tendency.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V001_image2video_stable_first_clash_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V001.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V001.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V001.json

## Decision

SHOT_02_V001_QUERY_ONCE_DONE_NO_AUTO_CONTINUE
SHOT_02_V001_MARKED_AS_USABLE_CANDIDATE_NO_LOCK
