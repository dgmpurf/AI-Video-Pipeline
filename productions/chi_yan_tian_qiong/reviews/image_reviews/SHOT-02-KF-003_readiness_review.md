# SHOT-02-KF-003 Image2Image Readiness Review

Task: SHOT-02-KF-003
Shot: SHOT-02
Status: submitted_querying
Concept: peak_spherical_rain_shockwave

## Scope

- Create a peak-impact keyframe package only.
- Do not submit Dreamina.
- Do not query, download, generate media, batch, retry, lock, or auto-continue.
- Preserve all SHOT-02-KF-002 / V003 / V004 history.

## References

- Primary composition/reference image: productions/chi_yan_tian_qiong/locked_refs/SHOT-02-KF-002_locked_main_hall_first_clash.png
- Optional effect reference source: manual_imports/effect_refs/jimeng_spherical_shockwave_example.mp4
- Optional effect reference present locally: false
- Effect reference still used: false

Because the optional effect reference video is not present locally, this package uses only the official locked SHOT-02 keyframe as the image2image reference.

## Dreamina Settings

- task_type: image2image
- provider: dreamina_cli
- model_version: 4.7
- ratio: 16:9
- resolution_type: 2k
- reference image count: 1

## Submission State

- status: submitted_querying
- submit_id: 1065e52f-abd8-4c97-a1d5-dd289906b7b1
- logid: 202606190009131692540470083719378
- credit_count: 1
- command_contract_valid: true
- first_query_status: querying
- queue_status: Generating
- downloaded: false
- output_path: null
- official_keyframe: false
- locked: false
- human_review_required_after_download: true

## Prompt Strategy

- Chinese prompt.
- Short, direct, result-oriented wording.
- Primary target: peak-impact central contact-point spherical shockwave.
- Preserve the locked keyframe scene, characters, and composition.
- Avoid the previous long over-explained prompt style.

## Required Visual Checks After Generation

- Fenshou remains on the left and Shuangji remains on the right.
- Main hall frontal axis, door, stone steps, wet stone floor, and rainy wuxia atmosphere remain legible.
- Central contact point is the origin of the shockwave.
- Large spherical shockwave and circular rain curtain are visible in frame.
- The effect does not become only ground splash or only foot-level water.
- Exactly two characters only.
- Bodies remain separated and readable.
- No duplicated characters, third person, fused bodies, extra limbs, scene change, modern city, side-scroller framing, text, or watermark.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-KF-003_peak_spherical_rain_shockwave_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/shot_02_keyframe_prompt_SHOT-02-KF-003.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_SHOT-02-KF-003.csv
- Shot record: productions/chi_yan_tian_qiong/shots/shot_02_keyframe_record_SHOT-02-KF-003.json
- Package report: reports/PHASE_K6_SHOT02_KF003_PEAK_SPHERICAL_RAIN_SHOCKWAVE_PACKAGE_REPORT.md

## Decision

SHOT_02_KF_003_SUBMITTED_QUERYING
