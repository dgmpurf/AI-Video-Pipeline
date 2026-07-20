# AI视频制作_正式授权序列化与完整性校验规则_V0.1

> 项目：AI视频制作 / AI_VIDEO_PIPELINE  
> 类型：P0 治理 Source / 正式授权序列化 / 完整性校验 / Authority Activation Gate  
> 版本：V0.1  
> 生成日期：2026-07-20  
> 状态：待人类审阅并手动应用  
> 适用范围：submit、query、download、retry、resubmit、batch、macro-run、Source update、final、lock 等正式授权  
> 证据来源：CAL-001 F06 recovery query R1 授权 Base64 漂移 safe-block，以及 R2 / download / review-artifact / visual-review record-only 阶段的确定性序列化修正。  
> 重要说明：本文件不授权任何 live 操作，不替代 Source 权限、Dreamina CLI、预算、媒体、final/lock 或人工审核规则。

---

## 0. 一句话结论

```text
canonical_authorization_text 是唯一权威授权内容。
byte_length、SHA-256、Base64 和 round-trip 结果都是从同一份 canonical UTF-8 bytes 确定性派生的证据，不是可独立编辑的授权副本。
```

---

## 1. 为什么需要本规则

CAL-001 F06 recovery query R1 暴露出一种可重复的结构性风险：

```text
canonical 文本、byte length 和 SHA-256 相互一致，
但 Prompt 中附带的 Base64 解码成了另一段同字节长度文本。
```

由于两段文本长度相同，仅检查 byte length 无法识别漂移。最终依靠：

```text
decoded bytes == canonical bytes
decoded SHA-256 == canonical SHA-256
```

触发 safe-block，并在任何 Dreamina 命令前停止。

本规则吸收的是可重复风险与防复发 invariant，不把一次性事故细节写成通用 Source。

---

## 2. 唯一事实源

正式授权必须指定：

```yaml
authority_source: exact_canonical_text
canonical_authorization_text: <exact text>
```

硬规则：

1. canonical text 是唯一权威输入。
2. 不得从 Base64、hash、历史 record 或 memory 反向重建授权范围。
3. byte length、SHA-256、Base64、last byte、round-trip 仅为派生证据。
4. 派生证据与 canonical text 冲突时，授权验证失败。
5. 不得选择“相信其中一份”；必须 safe-block。

---

## 3. Canonical byte profile

默认正式授权字节规范：

```yaml
encoding: UTF-8
bom: false
trailing_carriage_return: false
trailing_newline: false
trailing_space: false
markdown_fence_included: false
```

授权记录还应明确：

```yaml
last_character:
last_byte_hex:
byte_length:
sha256:
base64_character_count:
round_trip_verified:
```

不得静默执行：

- Unicode normalization；
- 大小写变换；
- 全角/半角替换；
- 智能引号替换；
- 标点重写；
- 多余空格压缩；
- CRLF/LF 转换；
- Markdown code fence 拼接；
- 尾部换行追加。

如确实需要 normalization，必须形成新的 canonical text 并重新获得人类授权。

---

## 4. 人机职责

### 4.1 Human

人类负责批准：

```text
exact canonical authorization text
```

人类不需要手工批准或复制：

```text
Base64
SHA-256
byte length
```

这些值由确定性工具派生。

### 4.2 ChatGPT / Work

可以：

- 编写授权范围；
- 明确 checkpoint、task、submit_id、操作次数、停止条件；
- 生成 official Source 候选；
- 审核 compiler 输出。

不得：

- 将手工拼接的 Base64 当作正式授权事实；
- 同时维护多份可编辑授权表示；
- 让 Base64 覆盖 canonical text；
- 因为 derived value 看起来合理而跳过本地 round-trip。

### 4.3 Codex / Automation

必须：

1. 从 exact canonical text 本地生成 UTF-8 bytes。
2. 本地计算 byte length。
3. 本地计算 SHA-256。
4. 本地生成 Base64。
5. Base64 decode exactly once。
6. 验证 decoded bytes 与 original bytes 完全一致。
7. 在 authority activation 前持久化验证结果。
8. 任一检查失败时 safe-block。

不得：

- 复制历史 Base64；
- 信任 Prompt 中的 Base64 作为独立权威；
- 在验证前激活 submit/query/download authority；
- 在验证失败后继续调用 provider。

---

## 5. 标准确定性编译流程

```text
exact canonical text
→ UTF-8 encode
→ byte-profile checks
→ byte length
→ SHA-256
→ Base64 encode
→ Base64 decode once
→ byte-for-byte equality
→ decoded SHA-256 equality
→ authorization record
→ authority activation
```

推荐记录：

```json
{
  "authority_source": "exact_canonical_text",
  "encoding": "UTF-8",
  "bom": false,
  "trailing_carriage_return": false,
  "trailing_newline": false,
  "trailing_space": false,
  "byte_length": 0,
  "sha256": "",
  "base64": "",
  "base64_character_count": 0,
  "base64_decode_count": 1,
  "decoded_bytes_equal_original": true,
  "decoded_sha256_equal_original": true,
  "last_byte_hex": "",
  "authorization_verified": true
}
```

---

## 6. Authority activation gate

默认状态：

```yaml
authorization_verified: false
execution_authority_active: false
submit_authorized: false
query_authorized: false
download_authorized: false
retry_authorized: false
resubmit_authorized: false
```

只有当完整序列化校验通过后，才允许按人类授权范围激活对应 authority。

如果校验失败：

```yaml
decision: safe_block
provider_command_count: 0
authorized_operation_count_consumed: 0
execution_authority_active: false
```

校验失败本身不得消耗 submit/query/download 计数，除非 provider subprocess 已实际启动。

---

## 7. Checkpoint binding 与 reauthorization

正式授权绑定 repository checkpoint 时：

1. live 前必须验证 local HEAD 与 origin/main。
2. 两者必须等于授权绑定 checkpoint。
3. safe-block 报告若被 commit/push，repository checkpoint 会变化。
4. 旧 checkpoint-bound authorization 不自动迁移。
5. 若仍需同一操作，必须由人类重新绑定新 checkpoint。
6. 重新授权不得隐含扩大操作范围。

---

## 8. 不允许的多副本结构

禁止把以下四项作为四份可独立编辑的权威内容：

```text
canonical text
byte length
SHA-256
Base64
```

正确结构：

```text
canonical text = authority
其他三项 = deterministic derived evidence
```

当 Prompt 为交叉校验提供 expected hash/length 时：

- Codex 仍必须本地重新计算；
- expected value 只作 cross-check；
- 不得跳过 locally derived value；
- 不建议在 Prompt 中附带外部 Base64。

---

## 9. Authorization compiler / verifier 最小要求

项目应实现一个 checked-in、可测试、可哈希的确定性工具，至少支持：

```text
compile exact text → serialization JSON
verify exact text against serialization JSON
verify existing authorization record
```

最低输入模式：

```text
--text-file <path>
或
--stdin-exact
```

最低输出字段：

```text
encoding
bom
cr_present
lf_present
trailing_space
byte_length
sha256
base64
base64_character_count
decoded_bytes_equal_original
decoded_sha256_equal_original
last_byte_hex
authorization_verified
```

最低行为：

- 非零 exit code 表示验证失败；
- stdout/stderr 不泄漏秘密；
- 不修改 canonical text；
- 不调用 Dreamina；
- 不激活 authority；
- 输出可被 JSON parser 稳定读取。

---

## 10. 必须覆盖的回归测试

至少包括：

1. 正常 UTF-8 round-trip。
2. 单字符替换但总 byte length 不变。
3. 下划线替换为字母。
4. 尾部 LF。
5. 尾部 CRLF。
6. UTF-8 BOM。
7. 尾部空格。
8. Markdown code fence 污染。
9. supplied Base64 解码内容与 canonical text 不同。
10. SHA-256 匹配但 Base64 不匹配的模拟 fixture。
11. checkpoint 变化后旧授权失效。
12. safe-block 不消耗 provider-operation counter。

---

## 11. Source 与 report 的边界

进入 official Source 的是：

```text
可重复风险
防复发 invariant
确定性校验流程
authority activation gate
```

留在 reports 的是：

```text
具体哪一个字符出错
某一次 Prompt 的错误 Base64
一次性本地脚本错误
具体执行耗时或 token 用量
```

只有可能在未来再次触发的问题才升级为 Source。

---

## 12. 与其他 Source 的关系

本文件补充：

- `AI视频制作_自动化治理与Source权限规则_V0.1.md`
- `AI视频制作_自动化宏流程与授权等级_V0.2.md`
- `AI视频制作_模式选择与GPT5.6执行路由覆盖层_V0.1.md`

本文件不覆盖：

- Official Source 的 human-only 权限；
- submit/query/download 分离授权；
- Dreamina CLI runtime help；
- 预算与积分 gate；
- 媒体不入库；
- visual success 与 final/lock 分离；
- `final_master=false` / `locked=false` 默认边界。

---

## 13. Automation invariants

```yaml
canonical_authorization_text_is_sole_authority: true
derived_values_are_not_independent_authority: true
derived_values_must_be_deterministic: true
external_base64_required: false
local_round_trip_required: true
authorization_verification_precedes_activation: true
verification_failure_safe_blocks_before_provider: true
checkpoint_change_requires_reauthorization: true
failed_pre_provider_validation_does_not_consume_operation_count: true
```

---

## 14. Final verdict

```text
AUTHORIZATION_SERIALIZATION_AND_INTEGRITY_RULES_V0_1_READY_FOR_HUMAN_APPLICATION
```
