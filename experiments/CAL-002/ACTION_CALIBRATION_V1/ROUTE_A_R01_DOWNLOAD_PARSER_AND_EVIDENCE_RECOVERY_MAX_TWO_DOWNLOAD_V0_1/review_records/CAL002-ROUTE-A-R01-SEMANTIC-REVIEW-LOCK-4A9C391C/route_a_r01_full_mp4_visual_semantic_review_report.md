# CAL-002 Route A R01 完整 MP4 视觉与语义审查

## 总体结论

- 完整 MP4 审查：`2 / 2`
- 语义闸门：`CANARY_REFERENCE_OVERDOMINANT_ROUTE_A_BLOCK`
- `R02_blocked=true`
- `automatic_expansion=false`
- `Route_A_capability_proven=false`
- `motion_only_behavior_verified=false`
- `production_approved=false`
- `fixed_task_completion=false`
- `final_master=false`
- `locked=false`

用户关于“五秒可以容纳更多动作”的判断成立。当前两条输出都严重浪费了时长：PUSH 的明显动作不足约 0.2 秒，IMPACT 的核心动作约 0.7 秒，其余部分基本停滞。

## ROUTEA_PUSH_R01

- 视频首帧已经像动作末态，攻击者双臂处于伸出状态。
- 约 `0.00–0.18s` 主要只看到攻击者收臂。
- 接触起点不清楚。
- 接收者没有可读的接触后反应、胸肩后移或后脚结果。
- 约 `0.20–5.06s` 基本静止。

正式结果：

```yaml
action_family_match: FAIL
onset: FAIL_STARTS_MID_ACTION
contact_onset: ABSENT_OR_UNREADABLE
post_contact_causality: FAIL
foot_result_count: 0
ending_motion: FAIL_LONG_STATIC_TAIL
motion_reference_adherence: WEAK_FRAGMENT_ONLY
strict_primary_pass: false
```

## ROUTEA_IMPACT_R01

- 约 `0.38s` 开始紧凑启动。
- 约 `0.66–0.75s` 出现短促接触。
- 接触后有可读 recoil。
- 接收者完成恰好一次后脚 recoil step。
- 攻击者及时收回。
- 约 `1.10–5.09s` 基本静止。

核心动作是正信号，但接触瞬间明确复制了参考动画中的黄色圆形接触标记。

正式结果：

```yaml
action_family_match: PASS
contact_duration: BRIEF
post_contact_causality: PASS
foot_result_count: 1
release_retraction: PASS
ending_motion: FAIL_LONG_STATIC_TAIL
motion_reference_adherence: STRONG_CORE_MOTION_SIGNAL
CONTACT_MARKER_COPY:
  present: true
  material: true
reference_overdominance: true
strict_primary_pass: false
```

## 哨兵规则

四类哨兵：

- `CONTACT_MARKER_COPY`
- `MANNEQUIN_STYLE_COPY`
- `GRID_SCENE_COPY`
- `FIXED_CAMERA_COMPOSITION_COPY`

本轮 `CONTACT_MARKER_COPY` 已经 material 触发。因此：

```yaml
R02_blocked: true
automatic_expansion: false
fresh_human_decision_required: true
```

## 五秒动作密度

建议下一版使用：

- `0.0–0.6s`：准备与接近
- `0.6–1.4s`：第一次接触
- `1.4–2.3s`：反应与脚步结果
- `2.3–3.2s`：释放、反制或第二动作节拍
- `3.2–4.2s`：重新站位
- `4.2–5.0s`：动态戒备或退出

五秒内更适合 `2–3 个完整因果动作节拍`，或 `4–6 个相互连贯的微动作节拍`，而不是一个不足一秒的动作后静止。

## 下一步建议

1. 锁定本次完整 MP4 审查结论。
2. 不执行原 R02。
3. 设计项目自有参考 `V0.2`：
   - 删除黄色接触标记；
   - 删除网格和明显校准场景提示；
   - 参考本身覆盖接近完整五秒；
   - 在整个时间段持续运动；
   - 使用多节拍因果编排。
4. 新参考完成后重新进行完整 MP4 人工审查，再决定是否申请新的修正版 canary。
