# Phase F6 Production Text2Image Live-run Report

## 1) Pre-submit check result
- Status: passed (59 checks).
- Manifest contains exactly one task for `A-SC-TEMPLE-COURTYARD-001`.
- Submit argv is a Python list and excludes pipeline-only fields.
- Run directory basename contains exactly one timestamp.

## 2) Live authorization result
- Scoped one-shot authorization matched the exact production task only.
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
  "A cinematic semi-realistic 3D ancient Chinese temple courtyard in light rain, wet stone ground with clear reflections, dark wooden main hall in the background, distant bell tower, hanging prayer flags moving slightly in misty wind, cool blue-gray atmosphere, low saturation, subtle ink-wash mood, deep spatial perspective, no characters, no animals, no text, no watermark, no modern objects, no neon lights, no sci-fi elements.",
  "--resolution_type",
  "2k"
]
```

## 4) submit_id / provider_task_id
- submit_id: `821c2865-26da-4c70-939f-07b4eb5a96d8`
- provider_task_id: `821c2865-26da-4c70-939f-07b4eb5a96d8`

## 5) Submit stdout / stderr summary
- Submit returncode: `0`
- stdout summary: `{
  "submit_id": "821c2865-26da-4c70-939f-07b4eb5a96d8",
  "logid": "20260613224850169254047008512F81F",
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
- querying_tasks.csv path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\querying_tasks.csv`
- raw query response path: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\raw_responses\query_response.json`
- Next allowed action: query existing submit_id only.

## 9) Run artifacts
- run_dir: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001`
- provider_requests.jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\provider_requests.jsonl`
- provider_responses.jsonl: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\provider_responses.jsonl`
- job_store.json: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\job_store.json`
- execution_log.txt: `G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260613_144850_A-SC-TEMPLE-COURTYARD-001\execution_log.txt`

## 10) Safety proof
- Exactly one real submit was attempted for the authorized production task.
- No batch run happened.
- No parallel run happened.
- No retry happened.
- No auto-continue happened.
- No old project path was accessed by this executor.
- All run writes were constrained by `PathPolicy` to the workspace.
- `configs/providers.json` was not permanently enabled for live-run.
- `locked_refs` and `locked_videos` were not written.
- This run did not register a production asset; human review remains a later step.

## 11) Pytest result
- Result: passed with exit code 0 after live submit/query persistence.

## 12) Final verdict
- `PHASE_F6_SUBMITTED_QUERYING`

