# AI视频制作_结构化验证器与盲审冻结治理规则_V0.2

> 类型：P0 validator / privacy / blind-review / evidence-promotion governance  
> 版本：V0.2，替换 V0.1  
> 激活判定：本文件被用户手动加入或替换到 Project Source 后即为 active。  
> 本文件不授权 sealed open、mapping reveal、Source write、Provider、production、final 或 lock。

---

## 0. 核心原则

```text
敏感信息与结构化证据校验必须判断：
对象角色 + 精确字段路径 + 值类型/形状 + 允许位置 + producer schema + authority phase。
```

不得只判断 key 名、raw substring、文件名出现次数或“看起来像”的容器名。

## 1. 禁止的脆弱校验

不得把以下方式作为唯一判据：

- `set(item) & forbidden_keys`；
- whole-document substring blacklist；
- 合法 member name 的全局 occurrence count；
- 只因字段名包含 `raw_provider_response`、`canonical_filename`、`salt`、`mapping` 就判泄露；
- 将 `*_persisted=false`、`*_disclosed=false` 等治理断言当作 protected value；
- 在未知 producer schema 时递归寻找任意相似 key；
- 在 exact schema 已知时容忍 guessed fallback containers；
- 以 parser 成功代替 schema、语义和 authority 校验。

## 2. Path-aware / role-aware / schema-bound validator

验证器必须显式定义：

```yaml
object_role:
producer_schema_identity:
container_path:
field_path:
required_type:
allowed_value_shape:
forbidden_value_shape:
cardinality:
order_requirement:
authority_phase:
```

### 2.1 允许与禁止示例

允许：

```text
preflight.input_review_zip.canonical_filename
preflight.external_input_review_zip.canonical_filename
raw_provider_response_persisted=false
salt_disclosed=false
mapping_disclosed=true|false
```

禁止：

- frozen blind review 中出现 canonical media path；
- public alias record 中提前出现 task/condition/Prompt/replicate mapping；
- public manifest 中出现 salt value 或 raw private equivalence；
- 未允许位置出现 signed URL、submit ID、cookie、token 或 raw Provider response；
- sanitized output 中出现 raw sealed member bytes。

## 3. Producer-bound schema rule

当结构由本项目 producer 创建时，validator 应优先绑定：

1. producer source exact path 或 governed evidence path；
2. producer bytes / SHA-256 / Git blob；
3. exact container name；
4. exact record count、order、field set 与 value types；
5. exact nested field paths；
6. positive and negative producer-shaped fixtures。

不得：

- 猜测 `members`、`files`、`bindings` 等替代容器；
- 因某字段不存在而自动搜索相似字段；
- 用旧 schema 的 equivalence field name 验证新 producer output；
- 在 sealed activation 后临时扩展容器猜测。

CAL-005 形成的通用教训：producer schema 必须在 activation 前精确验证；schema mismatch 不是授权扩大理由。

## 4. 合法治理断言

以下治理断言本身不是泄露：

```text
mapping_disclosed=false
mapping_disclosed=true
salt_disclosed=false
raw_provider_response_persisted=false
signed_url_persisted=false
condition_inference_performed=false
experiment_level_conclusion_performed=false
mapping_remained_unrevealed=true
raw_sealed_bytes_persisted=false
```

validator 必须检查真实 protected value，而不是屏蔽字段名。

## 5. Pre-activation fixtures

高风险 validator 在 activation 前至少通过：

1. 合法 provenance / governance positive fixture；
2. producer-shaped valid container positive fixture；
3. canonical path / mapping / salt / signed URL negative fixture；
4. wrong container negative fixture；
5. wrong field path / type / count / order negative fixture；
6. duplicate/collision fixture；
7. malformed path fixture。

夹具必须 synthetic，不得包含真实 sealed mapping、salt、URL、token 或 Provider payload。

fixture pass 只证明 validator 对夹具按预期工作，不证明真实 package 已通过。

## 6. Blind review 输入文件名归一化

UI 可附加一个 terminal positive-integer suffix：

```text
(n)
 (n)
（n）
 （n）
```

仅当以下全部成立时允许归一化：

- 只有一个 suffix；
- extension 不变；
- normalization 后一对一；
- canonical 与 suffixed copy 不同时存在；
- bytes/SHA 与 manifest 完全一致；
- 无 unmatched extra file。

`canonical_filename` 在此表示 review input/archive provenance，不等于 canonical media identity。

## 7. Sealed mapping 生命周期

### 7.1 Freeze 前

只允许 outer identity：

- path；
- regular-file status；
- bytes；
- SHA-256；
- governed open count。

禁止 member list、CRC、mapping、salt、manifest、equivalence 或 SHA256SUMS 读取。

### 7.2 Freeze 后

Freeze complete 不等于自动 unblind authority。

受控揭盲必须：

- fresh human authorization；
- bind current HEAD、public commitment、freeze identity 和 sealed outer identity；
- exact maximum opens / member reads；
- long-lived process 或明确的 immutable-byte lifecycle；
- attempt-separated accounting；
- sanitized outputs；
- protected-value scan；
- no automatic production/final/lock implication。

## 8. Failure phase classification

### 8.1 Pre-activation failure

若在 sealed access 前失败：

```text
authority_activated=false
sealed_open=0
no partial governed output unless contract explicitly permits a preactivation receipt
no automatic retry
```

修复后必须重新 preflight；是否使用同一 Goal 由 scope 是否变化决定。

### 8.2 Post-activation failure

若 authority 已激活或 sealed package 已打开：

- 原 authority consumed / non-reusable；
- 不得把新执行伪装成原执行的继续；
- 不得自动 reopen 或重启；
- 必须保留 sanitized blocked evidence；
- raw mapping/salt/sealed bytes 不得持久化；
- fresh recovery authorization 必须明确绑定 prior attempt、failure class、current HEAD 和新 open/read 上限。

### 8.3 Recovery accounting

若 fresh recovery 明确允许新的 sealed open：

```yaml
attempt_1_open_count: exact
attempt_2_open_count: exact
cumulative_open_count: exact sum
attempt_member_reads: separate
cumulative_member_reads: exact sum
third_open_authority: false unless separately and explicitly granted
```

不得把 cumulative 2 次写成“总计 1 次”。历史的 `reopen_forbidden=true` 对原 authority 仍然成立；fresh recovery 是新的独立授权。

## 9. Same Goal / Fresh Goal

### 通常可复用同一 Goal

- 科学问题不变；
- exact inputs / outputs 不变；
- 仅修正确定性 validator/path/serialization；
- fresh recovery authorization 明确允许；
- prior attempt 历史完整保留。

### 必须 fresh Goal

- 新阶段；
- 扩大输入或输出；
- 改变科学问题、Gate、阈值或 outcome precedence；
- 新 Provider/media/Source/production authority；
- human final decision、Source synthesis 或 production re-entry。

## 10. Gate precedence（S01）

```text
单个 favorable sample、median uplift 或 directional delta，
不能覆盖失败的 pre-registered family Gate 或 condition Gate。
```

必须同时保存：

- sample result；
- aggregate Gate result；
- failed predicates；
- near-threshold status；
- `does_not_override_gate=true`。

不得用“接近阈值”改写正式 outcome。

## 11. Stable production promotion（S02）

Prompt、reference、route 或 action recipe 进入 stable production guidance 前必须：

1. 通过自身预注册 Gate；
2. 在 bounded comparable conditions 下完成跨实验复现；
3. 未被更高优先级安全、rights、quality 或 governance Gate 阻断；
4. 由 ChatGPT 完成 Source synthesis；
5. 由人类手动应用；
6. production authority 另行批准。

单一实验 PASS、一个 reference family PASS 或 median uplift 不足以自动提升。

## 12. Setup-bounded interpretation（S03）

Action-family calibration 结论默认必须写明：

```yaml
provider_scope:
model_version_scope:
route_scope:
reference_scope:
scene_scope:
actor_scope:
prompt_scope:
replicate_count:
statistical_claim:
unique_cause_status:
```

除非另有独立证据，不得声称：

- Provider-wide bias；
- model-wide universal behavior；
- scene/actor independence；
- Prompt-universal causality；
- statistical significance；
- 某动作家族不可能生成。

## 13. Source promotion boundary

```text
repository experiment evidence
→ bounded synthesis
→ stable/provisional/rolling/not-source classification
→ ChatGPT Source candidate
→ human manual application
```

Codex 不得：

- 写 Official Source；
- 将 provisional finding 改成 stable rule；
- 将 current HEAD/hash/alias score 写成永久规则；
- 根据报告生成成功自行授权 production。

## 14. Human / ChatGPT / Codex 角色

- Human：最终 authority holder 与 Official Source applier；
- ChatGPT：新阶段合同设计、独立验收、Source synthesis；
- Codex：受控本地执行与 read-only evidence pack；
- Temporary Chat / Work：仅按显式隔离合同执行审片或审计。

## 15. Authority boundary

本文件不自动授权 sealed open、mapping reveal、condition analysis、Source update、Dreamina、Provider、live operation、production、final 或 lock。
