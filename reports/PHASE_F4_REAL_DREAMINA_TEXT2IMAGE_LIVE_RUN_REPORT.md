# Phase F4 Real Dreamina Text2Image Live-run Report

## 1) Pre-submit check result
- Status: passed (61 checks).
- Manifest contains exactly one task for `DREAMINA-PREFLIGHT-TEXT2IMAGE-001`.
- Submit argv is a Python list and excludes pipeline-only fields.
- Run directory basename contains exactly one timestamp.

## 2) Live authorization result
- Scoped one-shot authorization matched the exact task only.
- Authorization was consumed immediately after submit returned.
- Batch, parallel, retry, and auto-continue were not allowed.

## 3) Actual submit argv list
```json
[
  "C:/Users/msjpurf/bin/dreamina.exe",
  "text2image",
  "--model_version",
  "5.0",
  "--ratio",
  "16:9",
  "--prompt",
  "A simple cinematic ancient temple courtyard in light rain, wet stone ground, wooden hall, prayer flags, cool misty atmosphere, no characters, no text, no watermark.",
  "--resolution_type",
  "2k"
]
```

## 4) submit_id / provider_task_id
- submit_id: `68d6ccb1-6554-4db7-bb81-829ec5701432`
- provider_task_id: `68d6ccb1-6554-4db7-bb81-829ec5701432`

## 5) Submit stdout / stderr summary
- Submit returncode: `0`
- stdout summary: `{
  "submit_id": "68d6ccb1-6554-4db7-bb81-829ec5701432",
  "logid": "202606132214561692540470087748CA6",
  "gen_status": "querying",
  "credit_count": 3
}
`
- stderr summary: ``

## 6) credit_count / gen_status
- credit_count: `3`
- gen_status: `querying`

## 7) Query status
- Query status: `querying`
- Query returncode: `0`

## 8) Querying result
- querying_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\querying_tasks.csv`
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\raw_responses\query_response.json`
- Next allowed action: query existing submit_id only.

## 9) Run artifacts
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001`
- provider_requests.jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\provider_requests.jsonl`
- provider_responses.jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\provider_responses.jsonl`
- job_store.json: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\job_store.json`
- execution_log.txt: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_141456_DREAMINA-PREFLIGHT-TEXT2IMAGE-001\execution_log.txt`

## 10) Safety proof
- Exactly one real submit was attempted for the authorized task.
- No batch run happened.
- No parallel run happened.
- No retry happened.
- No auto-continue happened.
- No old project path was accessed by this executor.
- All run writes were constrained by `PathPolicy` to the workspace.
- `configs/providers.json` was not permanently enabled for live-run.

## 11) Pytest result
- Result: passed with exit code 0 after live submit/query persistence.

## 12) Final verdict
- `PHASE_F4_SUBMITTED_QUERYING`

