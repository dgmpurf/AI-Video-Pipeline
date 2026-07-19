# PHASE CAL-001-P3D-W01 F06 Recovery One-Download-Only Result

## 1. Phase summary

- phase_id: `CAL-001-P3D-W01_F06_RECOVERY_ONE_DOWNLOAD_ONLY`
- program_id: `CAL-001`
- macro_id: `CAL-001A`
- wave_id: `W01`
- experiment_id: `CAL001-F06-P1-R1`
- recorded_at: `2026-07-19T16:08:42.1283068Z`
- executed: true
- status: `success_downloaded_metadata_validated_review_artifacts_not_authorized`
- decision: `ready`
- starting_head: `610892ddc6818f3fa85f4bbe7edd0c3ba492b1c8`
- download invocation count: 1
- query-only invocation count: 0
- final_master: false
- locked: false

## 2. Canonical authorization

The exact canonical text supplied for this Goal was the sole authorization source. All serialization evidence was derived locally from that continuous string.

- encoding: UTF-8
- BOM: false
- CR/LF: absent
- trailing whitespace: absent
- byte length: 607
- SHA-256: `e56a37cc5e7f17aaa691ec4e5862fa9253e1a0273221523f9b2a2c172601ff4a`
- locally generated Base64 length: 812
- locally generated Base64 decode count: 1
- decoded bytes matched original bytes: true
- decoded SHA-256 matched: true
- last byte hexadecimal: `2E`
- authorization_verified: true

Authorization record:

`experiments/CAL-001/authorizations/CAL001_P3D_W01_F06_recovery_one_download_only_authorization.json`

The local PowerShell runtime did not provide `Convert.ToHexString`. That first compatibility attempt failed before any Dreamina command. Recalculation with `SHA256.ComputeHash` plus `BitConverter` passed all required checks.

## 3. Repository and Source preflight

- repository: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE`
- branch: `main`
- required starting checkpoint: `610892ddc6818f3fa85f4bbe7edd0c3ba492b1c8`
- local HEAD before live execution: `610892ddc6818f3fa85f4bbe7edd0c3ba492b1c8`
- origin/main before live execution: `610892ddc6818f3fa85f4bbe7edd0c3ba492b1c8`
- HEAD/origin aligned: true
- staged files before phase: 0
- unrelated tracked modifications before phase: 0
- sources clean: true
- sources touched: false
- existing unrelated untracked noise left untouched: true

## 4. Prior success and submit-ID binding

The committed R2 result passed 66 success, submit, quarantine, and package assertions.

- prior phase: `CAL-001-P3D-W01_F06_RECOVERY_ONE_QUERY_ONLY_REAUTHORIZED_EXECUTION_R2`
- authorized submit_id: `f40d2e79-ba98-4873-b92d-539ccc35d2ee`
- returned submit_id matched: true
- prior query invocation count: 1
- prior download invocation count: 0
- prior media downloaded: false
- gen_status: `success`
- queue_status: `Finish`
- fail_reason present: false
- provider credit count: 70
- prior result images/videos/outputs: 0/1/1
- expected result shape matched: true
- prior download URL present: true
- prior signed URL count: 1
- prior video metadata: 1280x720, 24 fps, MP4, 5.042 seconds
- prior_R2_success_binding_verified: true

## 5. Old-handle quarantine and fixed package

Old quarantined handle:

- submit_id: `cabfa6ab-cc61-4d29-8630-da01dfdeef65`
- provider task created/proven: false/false
- created task count: 0
- state: `orphaned_after_upload_transport_failure`
- quarantined: true
- query recovery eligible: false
- download eligible: false
- reuse/query/download authorized: false/false/false
- confirmed credit cost: null
- credit classification: `credit_consumption_unresolved`
- old-handle live calls in this phase: 0

Fixed package:

- path: `experiments/CAL-001/packages/F06/CAL001-F06-P1-R1_package.json`
- SHA-256: `4f0f8356b2d0c04f03f1eb6d3f403259795e24b413031c883491856d25366710`
- task/model: `multimodal2video` / `seedance2.0_vip`
- duration/ratio/resolution: 5 / 16:9 / 720p
- expected images/videos/outputs: 0/1/1
- package modified: false

## 6. Destination preflight

- authorized directory: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/experiments/CAL-001/runs/CAL001-F06-P1-R1`
- resolved under repository: true
- directory existed before phase: false
- preexisting file count: 0
- preexisting media count: 0
- planned output collision: false
- prior downloaded F06 video present: false
- destination state unambiguous: true

## 7. Dreamina canary and command contract

- atomic evidence wrapper: `app/ai_video_pipeline/execution/dreamina_evidence.py`
- wrapper SHA-256: `0da551983fce49f59fa0f880b93d1a80b07a192d94631acded2e9654ac7b15d4`
- bounded wrapper tests: 36 passed, 0 failed
- executable: `C:/Users/msjpurf/bin/dreamina.exe`
- executable SHA-256: `0d41930c93e3961b9eb017d5b5eedfa186f2b2025fa0037c19c3a29fc6249d10`
- version: `2a20fff-dirty`
- version invocation count: 1
- user_credit invocation count: 1
- query_result help invocation count: 1
- authenticated account confirmed: true
- private account identifiers redacted: true
- informational credit balance: 5625
- logger Access denied: false
- authentication failure: false
- help supports `--submit_id`: true
- help supports `--download_dir`: true
- download command contract valid: true

## 8. Exact one-download execution

The only result-download command executed was:

```text
C:/Users/msjpurf/bin/dreamina.exe query_result --submit_id f40d2e79-ba98-4873-b92d-539ccc35d2ee --download_dir G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/experiments/CAL-001/runs/CAL001-F06-P1-R1
```

- query_result with download_dir invocation count: 1
- submit_id flag count: 1
- download_dir flag count: 1
- query-only invocation count: 0
- polling/loop: false/false
- second provider call after download: false
- sanitized subprocess envelope persisted before semantic interpretation: true

A local PowerShell receipt object initially used `false` instead of `$false` after calculating the immediate gate. The corrected gate passed before provider invocation; the formatting failure launched no subprocess and consumed no download authority.

## 9. Provider response and local file discovery

- subprocess exit code: 0
- downloaded submit_id matched authorization: true
- gen_status: `success`
- queue_status: `Finish`
- fail_reason present: false
- provider credit count: 70
- response images/videos/outputs: 0/1/1
- new local image files: 0
- new local video files: 1
- actual filename: `f40d2e79-ba98-4873-b92d-539ccc35d2ee_video_1.mp4`
- actual repo-relative path: `experiments/CAL-001/runs/CAL001-F06-P1-R1/f40d2e79-ba98-4873-b92d-539ccc35d2ee_video_1.mp4`
- provider filename preserved without rename: true
- file size: 8,152,176 bytes
- file SHA-256: `02cec9d4966ef9a6b1cb70a902b423b060bb3e68cfefa267dd7ca3d8047d5079`
- raw signed URL persisted: false

## 10. Local metadata validation

No frame was decoded, extracted, rendered, or inspected. Metadata was read with OpenCV VideoCapture plus the MP4 `ftyp` signature.

- metadata readable: true
- container: MP4-compatible (`ftyp`, major brand `isom`)
- compatible brands: `isom`, `iso2`, `avc1`, `mp41`
- video codec: H.264
- primary video stream accessible: true
- audio stream count: unavailable with the bounded local metadata tool
- width: 1280
- height: 720
- measured fps: 24.119601328903656
- approximate fps difference from 24: 0.119601328903656
- frame-count metadata: 121
- measured duration: 5.016666666666667 seconds
- duration difference from 5.042: 0.025333333333333208 seconds
- duration tolerance: 0.25 seconds
- expected metadata matched: true
- frames decoded or extracted: 0
- visual inspection/scoring: false/false

`download_outcome = success_downloaded_metadata_validated_review_artifacts_not_authorized`

The first post-download counting expression matched all four `download-*` envelopes, including the three canaries. A corrected strict check used `operation_kind=download` and proved exactly one provider download envelope. This local statistics correction made no provider call.

## 11. Authority closure and media boundary

Download authority was closed immediately after the one invocation returned.

- download count: 1/1
- download_authorized_after: false
- download_authority_active_after: false
- execution_authority_active_after: false
- query_only_authorized: false
- retry/resubmit authorized: false/false
- second download/query authorized: false/false
- second recovery submit authorized: false
- F07 authorized: false
- frame extraction authorized: false
- contact sheet authorized: false
- visual scoring authorized: false
- media downloaded: true
- media tracked/staged/committed/pushed: false/false/false/false
- `.gitignore` modified: false
- final_master: false
- locked: false

## 12. Explicit non-actions

- query-only: false
- second query_result/download: false
- retry/resubmit: false/false
- second recovery submit: false
- old-handle query/download: false/false
- F07 or another CAL-001 task: false
- frames/contact sheet/thumbnail: false/false/false
- visual review/scoring: false/false
- transcode/rename/edit: false/false/false
- Prompt/package/fixture/manifest/inventory/dataset changes: false
- Source modification: false
- media stage/commit/push: false/false/false

## 13. Recommended next phase

`CAL-001-P3D-W01_F06_RECOVERY_REVIEW_ARTIFACT_AUTHORIZATION_DECISION`

A separate human authorization is required before frame extraction, contact-sheet creation, or any visual review. This phase does not authorize another Dreamina call, another download, F07, final, or lock.

## 14. Final verdict

`CAL001_P3D_W01_F06_RECOVERY_DOWNLOAD_SUCCESS_AUTHORITY_CLOSED_READY_REVIEW_ARTIFACT_AUTHORIZATION_DECISION`
