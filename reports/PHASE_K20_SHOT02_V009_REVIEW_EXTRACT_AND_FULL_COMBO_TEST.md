# PHASE_K20_SHOT02_V009_REVIEW_EXTRACT_AND_FULL_COMBO_TEST

- collected_at: 2026-06-21 18:20:11
- project: Chi_Yan_Tian_Qiong SHOT-02
- objective: Cut best V009 extract and assemble FULL_B + V009 full-combo test

## Source Inputs

- V009 source: $manualPath
- Full-beat base input (FULL_B): $fullB

## Cut Settings

- preferred V009 segment: 0.50s to 2.00s
- cut output: $cutPath
- concat assembly output: $combo

## Validation Metadata

### Source V009 (manual download)
- exists: true
- path: $manualPath
- size_bytes: 6880052
- sha256: 44e724c924f57346428e0753fe784255a40ed47694ca00bced4520519795d195
- duration_sec: 4.063
- resolution: 1280x720
- fps: 60
- frame_count: 97

### V009 CUT01 (0.50s-2.00s)
- path: $cutPath
- exists: true
- size_bytes: 564340
- sha256: d285a946aa42271c3ecf4f207140f4383fb98817ebad008270d1319b4fde357f
- duration_sec: 1.500000
- resolution: 1280x720
- fps: 24
- frame_count: 36

### FULL_B combo base
- path: $fullB
- exists: true
- size_bytes: 3795951
- sha256: 262e6a3794326fdc88004e1f6df9909c9db4c0178d32cbc7d7d6d5f302146cfb
- duration_sec: 3.375000
- resolution: 1280x720
- fps: 24
- frame_count: 81

### FULL_B + V009_CUT01 Combined
- path: $combo
- exists: true
- size_bytes: 2380076
- sha256: c7b4b6e85eaec092a01c0d14acb55edd02e77f4a172b2c588902e503af05aa2c
- duration_sec: 4.875000
- resolution: 1280x720
- fps: 24
- frame_count: 117

## Contact Sheets

- V009 cut sheet: $sheetCut
  - size_bytes: 105918
  - sha256: 65abfa6ee5c0e33d76e84191d03fa2fe861baa14e4279abab2390759e1ffccd8
- FULL_B plus V009 sheet: $sheetCombo
  - size_bytes: 257112
  - sha256: 46d0c1f54b7de3e96cccb8097f0d5190f81432f4e9ea88a8791abe4cba549a27

## Review Notes

- Human review status confirmed: V009 contact sheet passed.
- Preferred segment: 0.50s to 2.00s.
- Functional role: body/footwork reaction and transition segment after shockwave sequence.

## Recommendation

- Human should review contact sheet and video of:
  - $combo
  - and optionally $sheetCombo
- Next step: evaluate this combined test before deciding final SHOT-02 V009 integration.
