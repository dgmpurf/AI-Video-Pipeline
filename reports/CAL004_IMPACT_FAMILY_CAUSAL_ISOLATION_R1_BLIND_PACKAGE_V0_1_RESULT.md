# CAL-004 R1 Randomized Blind Package V0.1 Result

## Decision

`CAL004_R1_RANDOMIZED_BLIND_PACKAGE_READY_FOR_COMPLETE_MP4_REVIEW`

## Scope

- Canonical media validated: 18/18.
- Blind media created: 18/18.
- Review batches created: 3.
- Files per batch: 9/9/9.
- Semantic review performed: false.
- Scoring performed: false.
- Mapping disclosed: false.
- Salt disclosed: false.

## Technical Validation

- Target bytes: 8388608 per blind MP4.
- Size conformance: 18/18 PASS.
- ffprobe parse: 18/18 PASS.
- Full decode: 18/18 PASS.
- Video framemd5 equivalence: 18/18 PASS.
- Audio framemd5 equivalence: 18/18 PASS.
- Metadata safety: 18/18 PASS.
- Blind hashes unique: PASS.
- Blind hashes different from all canonical hashes: PASS.

## Review-Safe Alias Inventory

| Alias | Batch | Bytes | Duration | Dimensions | Streams | SHA-256 |
|---|---|---:|---:|---|---|---|
| B01 | A | 8388608 | 5.085011 | 1280x720 | 1V+1A | `6971bd63f880df5c12f5161a30dccb8fbe9313963a5aad6529400b230ee07da9` |
| B02 | A | 8388608 | 5.085011 | 1280x720 | 1V+1A | `de4d193e3cb961669e59bcc65ee251ef05d36e7957885f8b6254f1a3a2ad23f2` |
| B03 | A | 8388608 | 5.085011 | 1280x720 | 1V+1A | `c370961d02d7de8d3d5fe4c04b8a07994c479f903a82cd76336826a46c27931c` |
| B04 | A | 8388608 | 5.061995 | 1280x720 | 1V+1A | `8f166f7a041ed3dbbe943c461a668ed3a628be6ff1c83fa2237100ed8f259c4c` |
| B05 | A | 8388608 | 5.085011 | 1280x720 | 1V+1A | `d5a6ec91d7c8fcde8e7f90a56029f6b70720d99b547c02b0c5422b672510d78a` |
| B06 | A | 8388608 | 5.085011 | 1280x720 | 1V+1A | `86ece7770e9ed5e20d74826223ad86f797d60b7bb209beb4d4a293b37d08bd75` |
| B07 | B | 8388608 | 5.061995 | 1280x720 | 1V+1A | `30be8e5dc0a5934b5f6af4e2a6b433636a305fe9de8d699bfa6e90e7533603fa` |
| B08 | B | 8388608 | 5.085011 | 1280x720 | 1V+1A | `f4f1fae6cddff3b983d1e637947813c47a07111e58e3e7adde777d73d360b073` |
| B09 | B | 8388608 | 5.085011 | 1280x720 | 1V+1A | `d7e2ee7c8a3be2e7e079590734bff296dcc8a154ea5a2d0a96e27a5a339bba6e` |
| B10 | B | 8388608 | 5.085011 | 1280x720 | 1V+1A | `31cc7dc78c9f00b92740d14779837880c5bc29e47546423ecc6d1e6560f71b1d` |
| B11 | B | 8388608 | 5.061995 | 1280x720 | 1V+1A | `acca3ae8f36de4f3c6bddf9373a2980abdd65df98fafae33fcd2743f89398e2c` |
| B12 | B | 8388608 | 5.085011 | 1280x720 | 1V+1A | `c2ea0da1b547faabd297b977236c404e9f62e85f1a31261f2c56e8560e320922` |
| B13 | C | 8388608 | 5.085011 | 1280x720 | 1V+1A | `6fc9b6633af3c31c7650d2de77444fb9cbc52cff2f15b516e34004ce50749efd` |
| B14 | C | 8388608 | 5.061995 | 1280x720 | 1V+1A | `0f13aec57ef3dff7861ac31e8375b04583cec08c9b6cfbf9d57eb76435713c78` |
| B15 | C | 8388608 | 5.061995 | 1280x720 | 1V+1A | `a82315ff25ac25d45794ea7bf0064fe65483d4589dcc2abbae5044f34ff34bfc` |
| B16 | C | 8388608 | 5.061995 | 1280x720 | 1V+1A | `521599203a0dfb4942e6df205acfeca0ca7ed74dcc076433d909bfad20d26f0e` |
| B17 | C | 8388608 | 5.061995 | 1280x720 | 1V+1A | `9ed20e00eb6637fd65ce38d5f1e70a37493db1d595822975f3245ca96bfa730f` |
| B18 | C | 8388608 | 5.061995 | 1280x720 | 1V+1A | `ff8d310354ef10e7ecfc6bc1cd638ccfab61c2ed2bb93cfb4b86ef691ce0dd65` |

## Commitment And Sealed Package

- Public commitment: `8f1acc67acfc9d96a38b29762ce6c54949006f09d608c9548e00f9fbb96676b8`.
- Commitment formula: SHA256(canonical mapping bytes + LF + lowercase salt hex bytes).
- Four-way commitment equality: PASS.
- Sealed ZIP path: `G:/AICODING/AI_VIDEO/_sealed/CAL004_R1_BLIND_MAPPING_V0_1/CAL004_R1_BLIND_MAPPING_DO_NOT_OPEN_UNTIL_REVIEW_FREEZE_V0_1.zip`.
- Sealed ZIP bytes: 41207.
- Sealed ZIP SHA-256: `0eb2eb74397431799658103d1f3e9b03b476c2e5b49aa5bfd36aa0398412fb40`.
- Sealed member count/order/CRC: PASS.
- SHA256SUMS: 5/5 PASS.

## Governance

- Dreamina called: false.
- Provider called: false.
- Credit operation: false.
- Submit/query/download/retry/resubmit: 0/0/0/0/0.
- Source changed: false.
- Canonical media changed: false.
- Blind media staged: false.
- production_approved=false.
- fixed_task_completion=false.
- final_master=false.
- locked=false.

## Next Phase

`CAL004_R1_BLIND_COMPLETE_MP4_REVIEW_AND_RECORD_FREEZE_HUMAN_DECISION`
