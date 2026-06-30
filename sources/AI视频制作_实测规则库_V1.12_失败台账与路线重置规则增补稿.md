# AI视频制作_实测规则库_V1.12_失败台账与路线重置规则增补稿

版本：V1.12 Draft  
来源：K244S SHOT-04 R02 evidence pack  
状态：Source 草案，需人类手动确认后才能进入 `sources/`

## 0. 适用范围

本增补稿用于规范 AI 视频制作中的失败分类、成功分类、路线重置和重复失败后的停止条件。它尤其针对以下场景：

- Dreamina 任务 valid submit 后远端 `final generation failed`。
- 技术上生成了图片/视频，但视觉动作失败。
- 同一路线或相近路线反复失败。
- 双人近身战斗、身体接触、护架压迫、湿地滑步、墙边空间压力等高风险动作场景。

## 1. 成功不等于可用

所有阶段必须区分下列状态：

| 层级 | 含义 | 是否可视为 final |
|---|---|---|
| package_success | prompt/package/manifest 可读、可解析、可审查 | 否 |
| submit_success | 远端接受任务，返回 submit_id | 否 |
| query_success | 远端返回 success 且有结果 | 否 |
| download_success | 本地下载并校验媒体 | 否 |
| review_artifact_success | 抽帧、contact sheet、metadata 完成 | 否 |
| visual_success | 人类/ChatGPT 视觉审核通过 | 仍不自动 final |
| final_lock_success | 人类明确 final/lock | 是 |

任何 submit/query/download 成功都不能自动升级为 visual success。任何 visual success 也不能自动升级为 final/lock。

## 2. 失败根因分类

每次失败必须写入 failure ledger，并至少选择一个主类。

### 2.1 package_defect

本地 package、prompt、manifest 或 review 信息存在缺陷。  
处理：修包、重审，不允许直接 submit。

### 2.2 source_governance_block

`sources/` 脏、或 Codex 需要创建/修改/stage/commit 官方 Source。  
处理：停止，Source 只允许人类手动治理。

### 2.3 preflight_block

Dreamina version、user_credit、task help、登录态或命令可用性预检失败。  
处理：停止，不能 submit。

### 2.4 command_contract_block

package 计划与当前 CLI help 不匹配，例如参数名、模型版本、分辨率、输入类型不支持。  
处理：按当前 help 修正包，不允许 live。

### 2.5 upload_transport_failure

submit 返回但未进入有效队列，或上传资源阶段失败。  
处理：改 upload-safe、本地包引用、格式/体积/路径，不把 submit_id 误判为成功排队。

### 2.6 remote_final_generation_failure

submit 有效，query 后远端返回 `gen_status=fail`，无结果图/视频，无 download URL。  
处理：禁止自动 retry。若两个结构不同路线都出现此类失败，必须 route reset。

### 2.7 visual_execution_failure

媒体生成成功，但动作、身份、因果、节奏或镜头目标失败。  
处理：生成 review artifacts，记录人审和 ChatGPT 审查，再决定修 prompt、转路线或停。

### 2.8 prompt_priority_failure

prompt 包含规则，但 P0 视觉结果没有被优先化，导致模型读成静态推搡、摆拍、装饰效果等。  
处理：结果优先改写，P0 放首句，动作链、接触点、时间窗、尾段运动明确。

### 2.9 reference_attention_conflict

多个参考图职责冲突，身份、场景、动作、构图互相争夺注意力。  
处理：减少 refs、明确 reference duty，或改 prompt-only / layout route。

### 2.10 dual_character_close_combat_staging_brittleness

双人近身、护架、身体线、压力、位移、遮挡、肢体清晰度同时要求过高，导致静帧或视频失败。  
处理：降复杂度、转 video-first、manual layout、单人插入镜头或替代动作。

### 2.11 body_wall_contact_brittleness

身体与墙体接触、墙面反馈、无嵌入/无融合/无坍塌要求过高。  
处理：exact contact 必须时转 manual layout / compositing；否则改 near-wall pressure。

### 2.12 text2image_keyframe_brittleness

prompt-only still keyframe 在双人近身战斗上远端失败。  
处理：不要假设 text2image 比 video 更稳；考虑 video-first 或单人/布局路线。

### 2.13 video_action_quality_failure

video 产出媒体，但动作质量失败，例如反应慢、静态尾段、动作因果不清。  
处理：前置有效动作，设计 1.0–1.5s 可剪辑窗口，抽帧审查。

### 2.14 timing_tail_poseout_failure

视频合法时长内有长起手、长停顿、静态 pose-out，核心动作不足。  
处理：第一帧已经近身；核心动作 0.35–0.65s 内发生；1.35–1.50s 可剪；尾段保持运动。

### 2.15 identity_drift

身份、性别、服装、轮廓偏离。  
处理：作为独立审查维度，不用身份成功掩盖动作失败。

### 2.16 route_reset_required

同类失败累积到必须换路线。  
处理：写 route reset report，比较至少三种路线，不允许盲目 retry。

### 2.17 manual_layout_required

文字/refs 无法稳定表达空间关系，需要人工布局或外部工具。  
处理：先做 layout planning，不直接生成 final。

### 2.18 alternate_action_required

原动作过于脆弱或成本过高，需要保留戏剧目的但替换动作形式。  
处理：列明移除的旧约束，重新设计 beat。

## 3. Route Reset 触发规则

出现以下任一情况，必须 route reset：

1. 两个结构不同的路线都 valid submit 后 remote final-generation failure。
2. 同一动作目标在 image2image 和 text2image 均远端失败。
3. 媒体生成成功但视觉审查判定核心动作失败，并且 speed-up / crop 无法修复因果链。
4. 用户明确表达方向失望或疑问，例如“这真的是之前能做出流畅打戏的同一个项目吗”。
5. prompt 修改只是在删减词语，但没有改变失败的空间/动作结构。

Route reset report 必须回答：

- 什么失败了？
- 什么没有失败？
- 哪些原因被排除？
- 哪些原因被升级？
- 是否允许 retry？
- 是否需要 human route choice？
- 下一条路线是 video、manual layout、single-character insert、alternate action 还是 stop/rewrite？

## 4. Retry / Resubmit 规则

- 同包 retry 默认禁止。
- remote final-generation failure 后不得自动 retry。
- retry/resubmit 必须有显式人类授权。
- 如果失败原因是 upload_transport_failure，必须先做 upload-safe remediation，再考虑新 submit。
- 如果失败原因是 visual_execution_failure，必须先审片和路线判断，不能用 retry 代替诊断。

## 5. SHOT-04 R02 经验沉淀

SHOT-04 R02 证明：

- exact body-wall contact 极易失败。
- 4-ref / 3-ref image2image 均可能 valid submit 后远端失败。
- prompt-only text2image 在双人近身 guard clash 上也可能远端失败。
- video 路线至少曾经产出媒体，但可能视觉动作失败。
- 因此不能假设 still keyframe route 一定比 video route 安全。

## 6. Near-Wall Guard-Clash fallback pattern

当身体撞墙路线失败，可考虑 near-wall guard-clash：

保留：

- 雨夜走廊
- 墙边空间压力
- 双人近身
- crossed guard compression
- shoulder/forearm pressure
- wet-floor skid
- rain spray
- counter-readiness

移除：

- body-wall contact
- wall hit
- wall damage
- wall crack
- splinter
- wall dent
- wall mark
- embedding
- body-wall fusion
- body-to-wall collision

## 7. Source 更新策略

本文件仅为 Source 草案。进入官方 Source 前必须：

1. 由 ChatGPT Pro Extended 审查。
2. 由人类确认。
3. 人类手动应用到 `sources/`。
4. Codex 只做 read-only preflight，不自动改 Source。
