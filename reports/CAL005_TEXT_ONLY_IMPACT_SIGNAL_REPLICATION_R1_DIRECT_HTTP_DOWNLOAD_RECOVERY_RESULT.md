# CAL005 R1 Direct Signed URL HTTP Download Recovery Result

- Decision: `CAL005_R1_DIRECT_HTTP_DOWNLOAD_RECOVERY_COMPLETE_ALL_SIX_TECHNICALLY_VALID`
- Starting checkpoint: `771ddbd31529ebd06e3873a4487a9e247f2bfdb4`
- Authorization activated UTC: `2026-07-29T14:21:42.558206Z`
- Authorization consumed: `true`
- Authorization reusable: `false`
- Accepted prior root cause: `DOWNLOAD_TRANSPORT_BODY_READ_TIMEOUT`
- Old `query_result --download_dir` route invoked in this phase: `false`
- Old CLI download route status: `EXHAUSTED`
- Fresh query-only invocations: `4`
- Direct HTTP recoveries technically successful: `4/4`
- Curl process invocations: `4`
- Resume transfers: `0`
- Signed result URLs persisted: `false`
- Signed result URL hashes persisted: `false`
- Semantic review/scoring/randomness: `false / false / 0`

## Route Results

| Position | Task | Query | URL in memory | Initial curl | Resume | Transfer | Technical |
|---:|---|---|---|---:|---:|---|---|
| 1 | `N0R-01` | `0` | `true` | `0` | `not_used` | `PASS` | `PASS` |
| 2 | `I0R-01` | `0` | `true` | `0` | `not_used` | `PASS` | `PASS` |
| 3 | `I0R-02` | `0` | `true` | `0` | `not_used` | `PASS` | `PASS` |
| 4 | `N0R-02` | `0` | `true` | `0` | `not_used` | `PASS` | `PASS` |

## Six-Media Technical State

| Position | Task | Bytes | SHA-256 | Duration | Dimensions | Codecs | Decode | Technical |
|---:|---|---:|---|---:|---|---|---|---|
| 1 | `N0R-01` | 4170601 | `3da6be0116fe5e3bd1bcc180dee4ae024aa473b9707304f487a3f57786fed8f8` | 5.06195 | 1280x720 | `h264 / aac` | `PASS` | `PASS` |
| 2 | `I0R-01` | 3560166 | `3f430ce95674faa73d1d5198017a59687271f7a315167d4fb131bb1698c2569d` | 5.06195 | 1280x720 | `h264 / aac` | `PASS` | `PASS` |
| 3 | `I0R-02` | 3762453 | `cb257b021f9793bbd6b368c942c875f8cafd9a66408cc3f26c5e9ebc84923b19` | 5.085011 | 1280x720 | `h264 / aac` | `PASS` | `PASS` |
| 4 | `N0R-02` | 3270117 | `2fd189900d8da8e32186339bc439488507eba1297c19b1797d47bf3a0fed9b6e` | 5.085011 | 1280x720 | `h264 / aac` | `PASS` | `PASS` |
| 5 | `N0R-03` | 4737910 | `8464de889293d8a92164ba8c81e59585afa3a037cbc03748ff687671bd860023` | 5.06195 | 1280x720 | `h264 / aac` | `PASS` | `PASS` |
| 6 | `I0R-03` | 3429867 | `83d26fc63b0d7e7ba8c3cac0114ac6124a43378ffa790c60e61078ccc898c3b7` | 5.06195 | 1280x720 | `h264 / aac` | `PASS` | `PASS` |

## Local Learning Candidates

1. Dreamina CLI version 2a20fff-dirty on the selected Windows environment produced repeatable body-read timeout failures near 34 seconds for four successful video results.
2. Nonzero partial MP4 output plus identical timeout errors establishes a download transport failure, not a generation or query failure.
3. After two exhausted query_result --download_dir attempts per task, the same route must not be tried again.
4. A fresh query-only URL may be handed directly and ephemerally to a longer-timeout HTTP transport without persisting the URL.
5. Result URLs must be passed through stdin or process memory rather than command-line arguments, files, logs or environment variables.
6. Direct HTTP transfers should use same-volume partial files and one bounded resume attempt.

These six entries are Source-update candidates only. `sources/` was not changed.

## Local Validator Correction

- The four downloads and six-media validation completed before a local postwrite scan stopped.
- Cause: a field-name-only predicate rejected the legitimate governance assertion `raw_provider_response_persisted=false`.
- Correction: reject raw response content fields while allowing an explicit false persistence assertion.
- The same eleven outputs passed the corrected read-only sensitive-data scan.
- Dreamina query and curl transfer operations were not repeated.

## Boundaries

- Dreamina calls for positions 5 and 6: `0`
- `query_result --download_dir`: `0`
- Submit / generation retry / resubmit / user credit: `0 / 0 / 0 / 0`
- Media staged or committed: `false`
- Production approved / fixed task completion / final master / locked: `false / false / false / false`
- Next phase: `CAL005_R1_ALL_MEDIA_TECHNICALLY_VALID_BLIND_PACKAGE_AUTHORIZATION_HUMAN_DECISION`
