# CAL-002 Route A Capability Audit V0.1

## 1. Executive Conclusion

The committed command evidence verifies a `multimodal2video` command surface that accepts repeated local video inputs. It also verifies the input limits, supported Seedance 2.0 model names, output-duration surface, resolution surface, and ratio surface described below.

The same evidence does not define or guarantee motion-only semantic transfer. It does not prove that an action reference can control timing, pose progression, weight transfer, footwork, contact duration, recoil, release, or continued movement while excluding identity, costume, scene, camera, composition, and style. It also does not prove reference weighting, deterministic repeatability, or production suitability.

Capability conclusion:

`COMMAND_SURFACE_SUPPORT_VERIFIED_MOTION_ONLY_BEHAVIOR_UNVERIFIED`

- Provider capability status: `UNVERIFIED_PENDING_FUTURE_AUTHORIZED_CAPABILITY_VALIDATION`
- Route A execution ready: `false`
- Route A activated: `false`
- Route A execution authorized: `false`

## 2. Evidence Hierarchy

- Level 1: committed official/local command evidence and governance documents. These can establish the local command surface and authorization boundary.
- Level 2: committed project-tested evidence and accepted project decisions. These can establish observed failures, route rationale, and project review rules.
- Level 3: committed planning or draft reference-library evidence. These can guide a design but cannot prove Provider behavior.

Uncommitted worktree content, memory, unstored external claims, marketing language, and assumptions were excluded from capability proof.

## 3. Exact Evidence Bindings

| Level | Relative path | Bytes | SHA-256 | Git blob | HEAD equality | Evidence role |
| --- | --- | ---: | --- | --- | --- | --- |
| 1 | `sources/dreamina_cli_help_latest.md` | 5614 | `f3e7cafc2437c02e0eaceffabe6b247d27b4ec892fa66473f44181dce3a61238` | `13db416380426b2f71af92a94a4752ee865dacad` | true | Current committed help summary and command limits |
| 1 | `sources/Dreamina_CLI工作流与执行规范_V1.2_20260701_官方Help校正版.md` | 4758 | `8b466cff8d14cd7dbd8ee1e5effdb320d6448267532acd7ff642e90fe569dfef` | `b5b248470dd68064aa50dbfafe7f27f3def7def5` | true | Official-help-corrected workflow facts |
| 1 | `sources/Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁.md` | 3354 | `fcda1654a51888188dfe29b256db71a5338fe3acdf8f9f7803b56d2abac5da52` | `77ad2e4bff302ce3561b00010ec21473744a9beb` | true | Current committed execution-contract successor |
| 1 | `sources/DreaminaBatcher_manifest_schema_V1.2_20260701_官方Help校正版.md` | 4084 | `328c2a738b4b45200dc7ca4547f03c2ad6f9adf193afe35c08f372796548c44b` | `e2454ea0f0e9bf3542f16d75f8f6fe3ab850787c` | true | Command-field and model-surface schema |
| 1 | `sources/AI视频制作_正式授权序列化与完整性校验规则_V0.1.md` | 9221 | `f5471b851c6966e6de73ea552b42f4cd00d06af6aec5164ccf47beb373368572` | `094be6b923d2e2d2f78a930be64dd3ad5feb2700` | true | No-live authority and activation boundary |
| 1 | `sources/AI视频制作_Source索引与使用优先级_V1.12.md` | 11038 | `e13a98c4a12fab8ba3267b3074acf103e1458798fb865b6363ee3e732d275022` | `c533386576332f0429fb637f890ef9d3c174bbec` | true | Highest committed Source index and evidence priority |
| 2 | `sources/AI视频制作_动作参考视频库与审片标准_V0.1.md` | 4144 | `39773c7efc29d35b5a4a8748d4f874dad9985e2b44a7ad1b63cf3bb11800e0d1` | `b5c72a49be997d15771a5510112c3393e55682bd` | true | Project action-reference duty and review rules |
| 2 | `sources/AI视频制作_实测规则库_V1.8_多模态提示词专家与IP资料安全增补稿.md` | 25091 | `5e6cf2fcd4809a5e014513a35e39dafe0b13a827944926617334c7b9d4c2651f` | `a7d552ecfd18adc6aaba95dcce652c65bfcba06a` | true | Multimodal role separation and IP safety |
| 2 | `sources/AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿.md` | 7583 | `bcf034b496bd0ad35c8fff48fb8de73105e823cd197338a4eea3ae6b10ac09d4` | `26700dcd924bfe2526ae2678506d3291abb5d854` | true | Route-reset and repeated-failure rules |
| 2 | `experiments/CAL-002/ACTION_CALIBRATION_V1/ROUTE_RESET_DECISION_V0_2/CAL002_ROUTE_RESET_DECISION_PACK_V0_2.md` | 20250 | `5032cc253836de503e3fd39429826c6c791959254149eb82334795c9c1392c8c` | `f4da49fa8df81c8fb2cf8a46466e725d0e95194a` | true | Route comparison, unknowns, and minimum-program basis |
| 2 | `reports/CAL002_BATCH05_EXPERIMENT_RESULT_ACCEPTANCE_AND_ROUTE_RESET_DECISION_V0_2_RESULT.md` | 13556 | `ddd7887c1afe60ec0a5afc44b2bf61fe7b67f66f39fd040668a197ed49b0b404` | `b56a4ec8ce82cc64e4ee0c9271ffb9815e25d6fe` | true | Accepted Batch05 result and route closure |
| 2 | `experiments/CAL-002/ACTION_CALIBRATION_V1/RULES/ACTION_RULE_V0.3.md` | 7533 | `0fdda04117d076fcb8e05f2a9a094d4302112c5539b3d1ddf878ed5c03c93464` | `b14e627bf2437493f2333ffed7d42b00f790e40f` | true | Action-causality capability boundary |
| 2 | `experiments/CAL-002/ACTION_CALIBRATION_V1/BATCH05_DESIGN/CAL002_BATCH05_DESIGN_SPEC.md` | 21749 | `09eb7f17fd6c346e99e6af65fb5a1c407293c4dd783c35d823ed64267ad412b5` | `0e42b50b64b013a8b559d9828cd9f32ad0faf85e` | true | Human-confirmed Project Source state and Batch05 controls |
| 3 | `reports/evidence_consolidation/K244S_SHOT04_R02_AND_MACRO_LESSONS/ACTION_REFERENCE_VIDEO_LIBRARY_PLAN.md` | 6412 | `514cf20fd36703ecf78a9d0823aa2edeef6f9c1db50af1e27fdfea30de8749fd` | `612c99956883fc625908ebd5c1de6ca0d933a0b1` | true | Draft action-grammar library plan |
| 3 | `docs/reference_library_v0_1/safety/04_AI视频制作_模仿参考库ReferenceDuty与安全规则_V0.1.md` | 24347 | `51dac29d529831e8721dc49d613e23366ae92510749c8132450b4a68877751a2` | `b7aff51e71593d23b57e489e1e91d749c5c53fc5` | true | Draft active-input safety and ReferenceDuty framework |

Evidence counts: Level 1 = `6`; Level 2 = `7`; Level 3 = `2`; total actually used = `15`.

## 4. Successor and Governance-State Resolution

The highest committed Source index is V1.12. No V1.13 Source-index path is committed at the starting checkpoint. The committed Batch05 design specification separately records the human-confirmed active Project Source index as V1.13. This audit records that governance fact without inventing a repository path and without using unavailable V1.13 bytes as capability evidence.

The V1.4 execution contract is the committed successor used for current execution-contract facts. The official-help-corrected V1.2 workflow and manifest schema remain supporting command-surface evidence. No command-surface contradiction was found among the actually used Level 1 files.

Project reference-duty documents describe a desired semantic separation. They are not Provider guarantees. This difference in evidence authority is not silently merged.

## 5. Static CLI Command-Surface Findings

| Interface | Verified committed command-surface facts |
| --- | --- |
| `text2video` | Seedance 2.0 family model names; explicit ratio; 4-15 second duration; `seedance2.0_vip` lists 720p, 1080p, and 4k |
| `image2video` | One local image; ratio inferred from image; Seedance 2.0 family listed; VIP resolution surface listed |
| `frames2video` | First/last local images; ratio inferred from first frame; Seedance 2.0 family listed; 4-15 second Seedance duration surface |
| `multiframe2video` | 2-20 images; transition-oriented interface; no model-version or video-resolution override |
| `multimodal2video` | Repeated image/video/audio inputs; at least one image or video; image <= 9, video <= 3, audio <= 3; audio 2-15 seconds; Seedance 2.0 family including `seedance2.0_vip`; 4-15 second output; ratios 1:1, 3:4, 16:9, 4:3, 9:16, 21:9; VIP resolution 720p, 1080p, or 4k |

For `multimodal2video`:

- Repeated local image inputs accepted: `verified`
- Repeated local video inputs accepted: `verified`
- Repeated local audio inputs accepted: `verified`
- At least one image or video required: `verified`
- Maximum images/videos/audios: `9 / 3 / 3`
- `seedance2.0_vip` listed: `verified`
- Output duration surface: `4-15 seconds`
- VIP video-resolution surface: `720p / 1080p / 4k`
- Ratio surface: `1:1 / 3:4 / 16:9 / 4:3 / 9:16 / 21:9`
- Semantic duties for different references defined by help: `false`
- Motion-only transfer defined or guaranteed by help: `false`
- Identity or scene non-copying guaranteed by help: `false`
- Reference weighting or priority defined by help: `false`
- Exact motion replication guaranteed by help: `false`

## 6. Input Acceptance Is Not Semantic Transfer

Four evidence classes remain separate:

1. Command-surface support: verified for local video input.
2. Provider behavior: unverified for the proposed Route A treatment.
3. Semantic reference-duty behavior: unverified as a Provider capability.
4. Production suitability: unverified and blocked.

The presence of a local video-input flag proves only that the command surface can accept a video. It does not prove that the Provider will treat the video as motion-only, preserve separate identity and scene references, follow exact foot counts, or reproduce action timing faithfully.

## 7. Verified Facts

- The committed CLI surface exposes `multimodal2video`.
- Repeated local video inputs are represented in the committed help.
- The committed video-input count limit is three.
- The command surface lists `seedance2.0_vip`.
- The command surface lists a 4-15 second output-duration range.
- The VIP command surface lists 720p, 1080p, and 4k.
- Project governance has explicit concepts for motion-only duty, prohibited copied duties, rights review, and human approval.
- Batch05 establishes a need for route-level change, not proof that Route A succeeds.

## 8. Unverified Facts

- Motion-only semantic transfer.
- Exact action timing, pose progression, weight transfer, footwork, contact duration, recoil, release, or continuation fidelity.
- Identity, body, costume, hairstyle, scene, architecture, prop, camera, composition, lighting, style, or story separation.
- Reference weighting or priority.
- Deterministic repeatability.
- Rights-safe reference availability for the two planned roles.
- Current Provider terms, accepted active-reference formats, input-duration limits, current price, current credit cost, and current account availability.
- Route A production suitability.

## 9. Conflicts and Missing Evidence

No conflict was found in the current committed command-surface facts actually used.

One governance availability gap remains: committed Source index V1.12 is present, while the Batch05 design records human-confirmed Project Source index V1.13 as active. The unavailable V1.13 bytes were not used.

The principal capability gap is not contradictory evidence; it is absent evidence. Project documents define a motion-only duty contract, but no committed Provider result proves that the Provider honors it.

## 10. Rights and Provenance Implications

A future active action reference must be project-owned, self-recorded with documented consent, explicitly licensed for generative-model input, or contractor-created with explicit generative-use rights. Unknown-rights, public-reference-only, third-party entertainment, unlicensed social-media, nonconsensual real-person, private, sensitive, gore, and unresolved upload-restriction material cannot become active input.

No real asset was discovered or approved by this audit. Rights-safe reference availability remains `UNVERIFIED`.

## 11. Reference-Duty Implications

The project can define an intended motion-only duty and an explicit do-not-copy list. That semantic contract is necessary for a future test but is not proof of Provider enforcement. If a future verified mode cannot separate action, identity, and scene duties, Route A must block rather than accept role conflict.

## 12. Route A Execution Readiness

Route A execution readiness: `UNVERIFIED`.

Blocking gates:

- Provider command behavior has not been validated with a rights-safe reference.
- Motion-only semantics are not proven.
- Identity and scene separation are not proven.
- Rights-safe reference assets are not established.
- Provider terms, input-format details, reference-duration limits, price, and credit cost are not fresh.
- No execution package, upload authority, media authority, or live authorization exists.

## 13. Required Future Capability Gate

Before any execution package or live authorization:

1. Revalidate current official command help and current Provider terms under a separately authorized read-only phase.
2. Confirm accepted video formats, file-size limits, input-duration constraints, mode/model compatibility, and reference-role behavior.
3. Bind two rights-safe reviewed references with complete provenance.
4. Confirm that action, identity, and scene duties can be represented separately.
5. Obtain a fresh human decision on calibration budget and risk.
6. Build and independently review a no-live execution package.
7. Obtain separate live authorization.

## 14. No-Live Confirmation

- Dreamina calls: `0`
- Provider calls: `0`
- Provider command count: `0`
- External network search: `0`
- Reference reads/uploads: `0 / 0`
- Media created/changed: `false / false`
- Prompt packages: `0`
- Provider manifests: `0`
- Executable commands: `0`
- Sources changed: `false`

## 15. Exact Capability Conclusion

`COMMAND_SURFACE_SUPPORT_VERIFIED_MOTION_ONLY_BEHAVIOR_UNVERIFIED`

Provider capability status:

`UNVERIFIED_PENDING_FUTURE_AUTHORIZED_CAPABILITY_VALIDATION`

Route A execution ready:

`false`
