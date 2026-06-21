# PHASE_K21_SHOT02_TIGHT_IMPACT_V009_EDIT_TESTS

- project: Chi Yan Tian Qiong
- shot: SHOT-02
- task: local tight impact edit tests using existing media
- status: ready_for_human_review

## Human Review Context

Human reviewed `SHOT-02_FULL_TEST_B_plus_V009_CUT01` and confirmed that V009 can connect after FULL_B.

Review notes:
- The first preimpact beat is only passable.
- The aftershock recovery lingers too long.
- The edit should move faster: contact/hit -> shockwave -> very short aftershock -> body recovery -> next attack setup.

No Dreamina generation, submit, query, or download was run for this phase.

## Source Inputs

- V007 preferred preimpact source: `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V007/SHOT-02-V007_PREVIEW_C_0p50_to_1p30.mp4`
- V006 CUT03 shockwave source: `productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V006/SHOT-02-V006_CUT03_2p00_to_3p35_short_full_shockwave_extract.mp4`
- V008 preferred aftershock source: `productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V008/SHOT-02-V008_PREVIEW_B_0p25_to_1p50.mp4`
- V009 body recovery source: `productions/chi_yan_tian_qiong/edits/extracts/SHOT-02-V009/SHOT-02-V009_CUT01_0p50_to_2p00_body_footwork_reaction_extract.mp4`
- Conservative source combo: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-full-combo-v009/SHOT-02_FULL_TEST_B_plus_V009_CUT01.mp4`

## Edit Tests

### TEST_TIGHT_A

Structure:
- V007C tail: 0.35s-0.80s
- V006 CUT03: full / near-full shockwave
- V008B bridge: 0.00s-0.45s
- V009 CUT01: 0.00s-1.00s

Goal: fastest version that still reads as contact -> shockwave -> recovery.

Output:
- video: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_A_short_preimpact_full_shockwave_short_aftershock_v009.mp4`
- contact_sheet: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_A_contact_sheet.jpg`

Validation:
- exists: true
- duration_sec: 3.208333
- resolution: 1280x720
- fps: 24
- frame_count: 77
- file_size_bytes: 2022108
- sha256: 59678463e72f6d53c4d8f52ca15c7e9c083eb562ea870bbbb982ac151fc5025d
- contact_sheet_size_bytes: 73824
- contact_sheet_sha256: 71c75d046f44d144f0528f975bba1a5cdb03013eedf237e7cd2edf3172c999a7

### TEST_TIGHT_B

Structure:
- V007C tail: 0.50s-0.80s
- V006 CUT03: full / near-full shockwave
- V008: skipped
- V009 CUT01: 0.00s-0.90s

Goal: most aggressive transition into the next attack.

Output:
- video: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_B_aggressive_v007_tail_cut03_v009.mp4`
- contact_sheet: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_B_contact_sheet.jpg`

Validation:
- exists: true
- duration_sec: 2.500000
- resolution: 1280x720
- fps: 24
- frame_count: 60
- file_size_bytes: 1590318
- sha256: b138e0357247780bd099fcd02922a6377e92b51d82ed327c4212663c86f237f9
- contact_sheet_size_bytes: 66126
- contact_sheet_sha256: 822a6171e85277c9a1e598655ecdfab18ab4b643597063bd3a25769e83d6c62f

### TEST_TIGHT_C

Structure:
- Source: existing `SHOT-02_FULL_TEST_B_plus_V009_CUT01`
- Trim: starts at 0.30s
- Duration target: 3.70s

Goal: conservative tightened version of the current combo.

Output:
- video: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_C_trimmed_existing_full_b_plus_v009.mp4`
- contact_sheet: `productions/chi_yan_tian_qiong/edits/tests/SHOT-02-tight-impact-v009/SHOT-02_TIGHT_TEST_C_contact_sheet.jpg`

Validation:
- exists: true
- duration_sec: 3.708333
- resolution: 1280x720
- fps: 24
- frame_count: 89
- file_size_bytes: 1979374
- sha256: 22953210e7122a680838f92f49f8ffafcdb3cc8cd333a888eebfa93ac918037d
- contact_sheet_size_bytes: 80963
- contact_sheet_sha256: c3f128343c35c27404a8206a61e71799769ecb1b95e597d00e3a7054291c274d

## Recommendation

Human should review the three tight edit videos and contact sheets next:
- TEST_TIGHT_A for the fastest version that still keeps a short aftershock bridge.
- TEST_TIGHT_B for the most aggressive pacing and quickest move into V009 body recovery.
- TEST_TIGHT_C for the conservative tightened version of the previously reviewed combo.

No final master or locked status should be assigned until human review selects a preferred tight edit.

