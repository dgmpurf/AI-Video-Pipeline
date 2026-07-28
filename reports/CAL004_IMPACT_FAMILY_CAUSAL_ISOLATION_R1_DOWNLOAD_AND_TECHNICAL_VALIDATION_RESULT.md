# CAL-004 Impact-Family Causal Isolation R1 Download and Technical Validation Result

## Decision

- Decision: `CAL004_R1_ALL_MEDIA_DOWNLOADED_AND_TECHNICALLY_VALID`
- Starting HEAD: `a32cb9d940a720b7b012b9d1207f05a1f731ce21`
- Authorization: bytes `1279`; SHA-256 `d2f8ca7e36417b5f5f16b0eee96d746bed4f9f3083fcd85ad90d22c7a4156886`; Base64 characters `1708`
- Authorization activated/consumed/reusable: `true / true / false`
- Download tasks attempted: `18`
- Download invocations: `18`
- Successful/failed downloads: `18 / 0`
- Technically valid/invalid: `18 / 0`

## Preflight

- Branch and HEAD/origin alignment: `main / PASS`
- Tracked/staged/Source changes: `0 / 0 / 0`
- Query evidence: `18/18 terminal success`, exactly one video result each
- Existing final media conflicts: `0`
- Repository output conflicts: `0`
- `dreamina query_result -h`: `PASS`
- ffprobe/ffmpeg: `PASS / PASS`
- `user_credit` called: `false`

One local pre-activation correction captured complete ffmpeg version output
before selecting its first line, avoiding a PowerShell broken-pipe false
positive. It did not consume download authority.

## Media Results

| # | Task | Condition | Route | submit_id | Final path | Bytes | SHA-256 | Duration | Dimensions | Codecs | Streams | Decode | Technical |
|---:|---|---|---|---|---|---:|---|---:|---|---|---|---|---|
| 1 | N0-01 | N0 | text2video | `5ede7644-ecec-42bb-ac80-46eec0b4e539` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/001_N0-01.mp4` | 3836839 | `b6f728b3f24052985d3cc6c2c647a64b8c3a206622e67c9cd008ab355b3928a0` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 2 | II-01 | II | multimodal2video | `9f794478-badd-4c96-ace0-269b6a249217` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/002_II-01.mp4` | 2087416 | `c5e446f19445928441d6737b7fd06c280e927c3ad66696486e03a2898dc9a1b7` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 3 | NP-01 | NP | multimodal2video | `f85812b1-d3f3-4a11-979d-af869db66beb` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/003_NP-01.mp4` | 2876008 | `fbee1682148682405b0ed8cd2253386b4b99c023c2689ccd7f2ff21ee16958d7` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 4 | I0-01 | I0 | text2video | `52b93a7b-a2bc-408c-924a-e49324ddee9b` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/004_I0-01.mp4` | 4530876 | `23865256cc0eabb49973460606950e8f7d1213bf5c43fd16bcc17e972b224bc6` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 5 | NI-01 | NI | multimodal2video | `2c6ac89a-f197-43a6-99d0-a960c64aa097` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/005_NI-01.mp4` | 1981288 | `a72ee024b662858e8d35a705b852c9e127c85bec0f4422b5ff2866c94cdf453f` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 6 | IP-01 | IP | multimodal2video | `a7803e10-d5d2-4e72-bd72-938a77c36c14` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/006_IP-01.mp4` | 3180297 | `cacc11a20789e87e5224bc6c2968991c4b6e0961a597c751bbe891123f31eb28` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 7 | IP-02 | IP | multimodal2video | `8d56d2d8-85ef-4c63-ba1a-5a8981907294` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/007_IP-02.mp4` | 2146559 | `544899c508af9dcb1f8b442052384beef053ad1b653cd272dffeb7386968a9b6` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 8 | NI-02 | NI | multimodal2video | `a6639903-0c38-4013-886e-a3648385c1b7` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/008_NI-02.mp4` | 3507322 | `d49d98f5f7862aba2a512346ce85927f2810e1e7e258d591df16acb8102820b0` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 9 | I0-02 | I0 | text2video | `b30ff9af-932c-4654-b1d1-239ac6144edc` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/009_I0-02.mp4` | 4845910 | `89dc85d36f75d32563617e84285271aa55027beba2948be31886c440ff07a95a` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 10 | NP-02 | NP | multimodal2video | `f99be447-8edb-406a-82ba-fa577ec20aab` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/010_NP-02.mp4` | 2542322 | `4fc70823ab6b5383e9bf2951c271d1ef899de58f40af4ff5363d7f091fe2a135` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 11 | II-02 | II | multimodal2video | `fac76984-627a-440a-93ab-f588ff90a8fe` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/011_II-02.mp4` | 2476577 | `cef1efd9bd93be99d3d7cab4fb6c24e856f2850da8c9c77239970f6c6bdb084b` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 12 | N0-02 | N0 | text2video | `59cb2e47-7162-4317-94df-764a3f1eaec8` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/012_N0-02.mp4` | 3643763 | `ae63d22b3ecbf9b1fa6ba646ae42391ad65ba9bcb88d0391041382076e488925` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 13 | NP-03 | NP | multimodal2video | `83a4a012-09b9-40b5-bd64-1ed4c169e843` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/013_NP-03.mp4` | 2978086 | `198b7eba11c2745b2244e02f7597a21dc09532a8543dc740bd86e50081ccb403` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 14 | I0-03 | I0 | text2video | `0fbe85c5-3509-4e45-b52a-6208b8911964` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/014_I0-03.mp4` | 4019404 | `dc2911d30d639a172d4a2348649d22b063ba0e678413d66549278ce85e3868c9` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 15 | NI-03 | NI | multimodal2video | `e1d1353d-b17e-432f-b233-e3126474fe08` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/015_NI-03.mp4` | 2236832 | `49863212d71c80081e97cec0e315cf5b93c5082efc3f8ac9f4ee582d42aa4927` | 5.06195 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 16 | IP-03 | IP | multimodal2video | `189041c8-274c-47e4-9b82-8a3181c51f0c` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/016_IP-03.mp4` | 2107914 | `a4bb8ce6a71ce4f1ea3c66d66e1fb8c32e2e25d8ca4a3096fe3c759e218fcb45` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 17 | N0-03 | N0 | text2video | `43b1cc9e-3958-4604-89b3-b92124ed61c5` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/017_N0-03.mp4` | 3972175 | `7f1e69426f17ecba9590839797bbe1190dad0f6581fe1a228aaee68ee58c0b01` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |
| 18 | II-03 | II | multimodal2video | `f88d080b-167d-44be-ab21-a60e78d74ab7` | `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1/018_II-03.mp4` | 1714355 | `4bd8ff4642845006aa7e91284595f0aebb1674115dd724f4cda4ff78c8bdce49` | 5.085011 | 1280x720 | h264/aac | 2 (1V/1A) | PASS | PASS |

## Technical Summary

- Total media bytes: `54683943`
- Unique media hashes: `18`
- Duplicate hashes: `0`
- Final media paths present: `18/18`
- Unexpected external files: `0`
- Temporary directories remaining: `0`
- Planned duration: `5.0 seconds`; every observed duration is recorded separately and falls within `0.25 seconds` of plan.
- text2video coverage: `6/6 downloaded and technically valid`
- multimodal2video coverage: `12/12 downloaded and technically valid`

Technical validity means a regular nonempty file, parseable ffprobe metadata,
a valid video stream with positive dimensions and duration, and full-stream
decode without fatal error. It is not semantic or visual approval.

## Boundaries

- Submit/query-only/retry/resubmit: `0 / 0 / 0 / 0`
- Credits queried or consumed: `false / false`
- Semantic review/scoring: `false / false`
- Scientific result derived: `false`
- Randomness generated: `false`
- Signed URLs persisted or disclosed: `false`
- Media staged or committed: `false`
- Sources changed: `false`
- production_approved: `false`
- fixed_task_completion: `false`
- final_master: `false`
- locked: `false`

## Evidence

- External media root: `G:/AICODING/AI_VIDEO/_downloads/CAL004_IMPACT_FAMILY_CAUSAL_ISOLATION_V1_R1`
- Repository evidence root: `experiments/CAL-004/IMPACT_FAMILY_CAUSAL_ISOLATION_V1/R1_DOWNLOAD_V0_1`
- Task download records: `18`
- Repository outputs: `25`
- Temporary recovery attempts used: `1`

## Next Phase

`CAL004_R1_ALL_MEDIA_TECHNICALLY_VALID_BLIND_PACKAGE_AUTHORIZATION_HUMAN_DECISION`
