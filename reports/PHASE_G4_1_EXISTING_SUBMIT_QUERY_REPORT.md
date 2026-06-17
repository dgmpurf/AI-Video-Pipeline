# Phase G4.1 Existing Submit Query Report

## 1) Task
- task_id: `A-CH-B-SUBJECT-001`
- submit_id: `b381e6d4-c559-4689-a09c-03289ac63319`

## 2) Query command used
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "query_result",
  "--submit_id",
  "b381e6d4-c559-4689-a09c-03289ac63319"
]
```

## 3) Query status
- query status: `success`
- query returncode: `0`
- query stdout summary: `{"gen_status": "success", "submit_id": "b381e6d4-c559-4689-a09c-03289ac63319", "credit_count": 3}`
- query stderr summary: ``

## 4) Success download result
- raw_download_path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_055254_A-CH-B-SUBJECT-001\downloads\b381e6d4-c559-4689-a09c-03289ac63319_image_1.png`
- renamed output path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260614_055254_A-CH-B-SUBJECT-001\output\A-CH-B-SUBJECT-001_shuangji_full_body_subject.png`
- file_size: `1752299`
- width: `1440`
- height: `2560`
- format: `PNG`
- sha256: `f5c4f29083d9166466579f5af7387180bd8428f6071ba9b65b368873e5a7449a`
- Pillow status: `openable=True`

## 5) Safety proof
- No new submit happened.
- No retry happened.
- No batch or parallel action happened.
- No auto-continue happened.
- No external path was touched.
- providers.json dreamina_cli.allow_live_run: `false`
- providers.json was not modified.

## 6) Pytest result
- `python -m pytest -q` passed with exit code `0`.

## 7) Final verdict
- `PHASE_G4_1_SUCCESS_DOWNLOADED`
