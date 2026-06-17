# PHASE A.1 Acceptance Audit

- Date: 2026-06-13
- Workspace: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE`

## 1. Pytest result
- `python -m pytest -q`: passed (20 passed).
- No real Dreamina execution in this phase.

## 2. Forbidden path scan
- `forbidden_path_scan_pass`: true
- No forbidden legacy paths found in workspace text files.

## 3. Path policy
- project_root in config: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- allowed_write_roots: `['G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE']`
- allow_external_staging: `False`
- allow_delete: `False`
- `path_policy_ok`: true

## 4. Provider config
- default_provider: `dreamina_cli`
- dreamina_cli.enabled: `True`
- dreamina_cli.allow_live_run: `False`
- stubs disabled: ['kling_api=False', 'hailuo_api=False', 'runway_api=False', 'midjourney_image=False']
- provider config check: `true`

## 5. Internal fixture creation
- Created files: ['G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\tests\\fixtures\\media\\ref_a.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\tests\\fixtures\\media\\ref_b.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\tests\\fixtures\\media\\scene.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\tests\\fixtures\\media\\keyframe.png']
- Sizes (bytes): {'ref_a.png': 3147861, 'ref_b.png': 3147861, 'scene.png': 3147861, 'keyframe.png': 3147861}
- `fixture_size_ok (>10KB each)`: true

## 6. Dry-run image2image
- Run id: `audit_i2i`
- provider_requests: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\audit_i2i\provider_requests.jsonl`
- command_preview: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\audit_i2i\command_preview.csv`
- argv: `['C:/Users/msjpurf/bin/dreamina.exe', 'image2image', '--model_version', '5.0', '--ratio', '16:9', '--resolution_type', '2k', '--images', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_a_0b35d7027e15.png', '--images', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_b_0bf38de3fdff.png', '--images', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\scene_6b03c4325e6c.png', '--prompt', 'test prompt', '--output_name', 'TEST-I2I_output']`
- checks passed: `true`
- staged refs: `(True, ['G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_a_0b35d7027e15.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_b_0bf38de3fdff.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\scene_6b03c4325e6c.png'])`

## 7. Dry-run multimodal2video
- Run id: `audit_m2v`
- provider_requests: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\audit_m2v\provider_requests.jsonl`
- command_preview: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\reports\audit_m2v\command_preview.csv`
- argv: `['C:/Users/msjpurf/bin/dreamina.exe', 'multimodal2video', '--model_version', 'seedance2.0fast_vip', '--ratio', '16:9', '--duration', '5', '--video_resolution', '720p', '--image', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\keyframe_c66cd3ae75dd.png', '--image', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_a_0b35d7027e15.png', '--image', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_b_0bf38de3fdff.png', '--image', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\scene_6b03c4325e6c.png', '--prompt', 'test video prompt', '--output_name', 'TEST-M2V_output']`
- checks passed: `true`
- staged refs: `(True, ['G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\keyframe_c66cd3ae75dd.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_a_0b35d7027e15.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\ref_b_0bf38de3fdff.png', 'G:\\AICODING\\AI_VIDEO\\AI_VIDEO_PIPELINE\\staging\\scene_6b03c4325e6c.png'])`

## 8. Mock-run verification
- Run id: `audit_mock_i2i`
- provider_requests exists: True
- submitted_tasks.csv exists: True
- completed_tasks.csv exists: True
- downloaded_files.csv exists: True
- execution_log.txt exists: True
- mock outputs under workspace: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\mock_outputs
- mock outputs include no locked_refs writes: `true`
- checks passed: `true`

## 9. Report quality check
- ASCII/garbled text check: `true`
- quality issues: `[]`

## 10. Live-run gate
- can_run_live: False
- run_mode_allowed(RunMode.live): False
- execute(RunMode.live) behavior: `safe fail`
- proof: ['execute(live) raised RuntimeError']

## 11. External path check
- external paths touched: `false`

## 12. Dreamina execution
- No Dreamina submit/query/download command was invoked in this audit.

## Final verdict: PHASE_A_ACCEPTED
