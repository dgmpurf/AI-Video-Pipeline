# SHOT-02-V001 Image2Video Readiness Review

Task: SHOT-02-V001
Shot: SHOT-02
Status: submitted_querying

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
- submit status: querying
- query status: querying
- queue status: Generating
- credit_count: 70

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

## Submit Metadata
- submit_id: b3c0d827-29e7-4c1c-b928-c044b765b15b
- logid: 202606172244121692540470081522881
- submit status: querying
- query status: querying
- queue status: Generating
- credit_count: 70

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V001_image2video_stable_first_clash_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_video_prompt_SHOT-02-V001.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2video_SHOT-02-V001.csv
- Shot video record: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V001.json

## Decision

SHOT_02_V001_SUBMITTED_QUERYING_METADATA_RECORDED





