# SHOT-01-V001 Single Task Image-to-Video Submit Report

## Task
- task_id: SHOT-01-V001
- task_type: image2video
- run_dir: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_114203_SHOT-01-V001

## Exact CLI command used
```bash
C:\Users\msjpurf\bin\dreamina.exe image2video --model_version seedance2.0 --prompt "Create a light-motion image-to-video test from the locked SHOT-01 keyframe.

Preserve the locked spatial composition exactly. Both characters must remain in their current positions. Fenshou is the only black-red male figure on the left. Do not create any second black-red male silhouette. Shuangji remains on the right and faces left toward Fenshou. The middle open wet stone courtyard must remain visible. The camera position, temple background, courtyard layout, character scale, and left-right blocking must stay stable.

Allowed motion only: fine rain movement, subtle mist drift, wet stone reflection shimmer, very subtle clothing and hair movement, slight breathing and stillness tension, and optional extremely slow camera push-in.

Forbidden motion: no charging, no fighting, no character displacement, no new characters, no second Fenshou, no second Shuangji, no camera orbit, no dramatic zoom, no scene transition, no cutting to close-up, no changing character positions, and no changing courtyard layout.

The mood should remain quiet, tense, cinematic, rain-soaked, cool blue-gray, and restrained. Keep the shot as a stable standoff keyframe with only ambient motion." --duration 5 --video_resolution 720p --image G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\SHOT-01-KF-004-rerun-03_locked_official_shot_01_keyframe.png
```

## Submit and query result
- submit_id: 4beb7d87-ee4d-4703-af8b-abc232425e95
- query_status: querying
- download_happened: False
- output_path: not downloaded
- integrity: not available

## Artifacts
- provider_requests.jsonl: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_114203_SHOT-01-V001\provider_requests.jsonl
- provider_responses.jsonl: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_114203_SHOT-01-V001\provider_responses.jsonl
- job_store.json: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_114203_SHOT-01-V001\job_store.json
- execution_log.txt: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_114203_SHOT-01-V001\execution_log.txt
- raw query response: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260616_114203_SHOT-01-V001\raw_query_response_I2.json
- raw download response: not created

## Safety confirmations
- exactly one image2video submit: yes
- exactly one query_result after submit: yes
- ratio omitted for image2video: yes
- no retry: yes
- no resubmit: yes
- no batch: yes
- no parallel task: yes
- no auto-continue: yes
- runtime code modification: no
- configs/providers.json modification: no
- source files modification: no
- writes remained inside workspace: yes

## Final verdict
SHOT01_V001_SUBMITTED_QUERYING
