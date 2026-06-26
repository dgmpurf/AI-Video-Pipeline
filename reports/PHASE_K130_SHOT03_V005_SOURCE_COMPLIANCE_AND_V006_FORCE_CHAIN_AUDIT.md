# PHASE K130 - SHOT-03 V005 Source Compliance and V006 Force-Chain Audit

## Purpose

Audit why SHOT-03 V005 failed as a terrain-combat solution even though the prompt read and partially applied the current Source rules.

This is a text-only source-compliance audit. No Dreamina command was run. No submit, query_result, download, package preparation, speed diagnostic, or media generation was performed.

## Files Inspected

- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/prompts/manual_SHOT-03-V005_uploadsafe_terrain_rebound_attack_prompt.txt`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K128_SHOT03_V005_HUMAN_REVIEW_SOFT_FORCE_AND_SPEED_DIAGNOSTIC_PLAN.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/reports/PHASE_K129_SHOT03_V005_SPEED_DIAGNOSTIC_READY.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.2_动作变身运镜增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_实测规则库_V1.11_连续战斗动作密度与环境破坏因果增补稿.md`
- `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/sources/AI视频制作_Source索引与使用优先级_V1.5.md`

`sources/` was inspected read-only. No Source file was created, modified, moved, deleted, or staged.

## V005 Failure Summary

Human review in K128 concluded that SHOT-03 V005 is a valid terrain-affordance attempt, but not a passed terrain-combat solution.

Observed failure pattern:

- Fight feels too soft.
- Punch and leg attack speed does not match real force generation.
- The intended "哒哒哒" fast burst rhythm is missing.
- Terrain setup is visible, but it diluted contact density and power.
- The foot plant / rebound did not read as a compact explosive force chain.
- Motion reads closer to soft jump / pose / slow exchange than short explosive terrain-triggered impact.

K129 created speed diagnostics at `1.12x`, `1.18x`, and `1.25x`, but the K128/K129 rationale already notes that speed-up can only help rhythm if the underlying action chain is structurally valid. It cannot repair a weak force-chain prompt.

## Source Rules Expected

From Source V1.2:

- Fast combat should not become full-clip slow motion.
- Prompt should ask for real speed, quick attacks, quick guards, quick evasions, quick counters, no per-move pause.
- Only the key impact moment should have very short hit-stop.
- Avoid whole-clip slow motion, turn-based display, and planted static fighting.
- Physical impact needs body results such as forearm/shoulder load, upper body displacement, backward foot slide, knee compression, short contact pause, and water/dust/spark feedback.

From Source V1.11:

- First clear contact should occur around `0.15s-0.30s`.
- A 5-second combat clip should have at least `5-6` clear contact beats.
- Each contact beat needs attack path, contact point, defensive response, foot/body result, rebound, and re-entry.
- Actor causality must be explicit, not generic.
- Environmental feedback or breakage must have a clear contact cause; if causality cannot be written, remove breakage.
- The tail must cut during action, with no idle tail.
- Local speed-up is only appropriate when the action chain and contact beats already exist; it cannot fix structural prompt failure.

From Source Index V1.5:

- For combat/action prompts, V1.11 contact density and environmental causality should be used alongside V1.2 fight physics / hit-stop rules.
- Local speed-up cannot repair missing contact, broken causality, or structural action failure.

## V005 Prompt Compliance Table

| Rule | Present? | Weak? | Missing? | Evidence |
|---|---:|---:|---:|---|
| Real speed / continuous combat | Yes | Yes | No | Prompt says "全片保持真实速度和连续攻防", but does not repeat fast attack / fast guard / fast counter as hard per-beat requirements. |
| Explicit fast attack / fast block / fast counter | Partial | Yes | Partial | Some beats say "快速接触节拍", "短促掌线", "短线回击", but the global rule does not require every strike, guard, and counter to be rapid. |
| Ban full slow motion | Partial | Yes | Partial | Prompt bans "慢速推手" and allows only brief hit-stop, but it does not explicitly ban "整段慢动作 / 长时间升格 / 持续慢放". |
| Ban turn-based / planted exchange | Partial | Yes | Partial | Prompt bans "不要停顿对视，不要站定" and "不要摆拍", but does not explicitly ban "回合制" or "站桩互殴". |
| Rear/support foot force chain | Partial | Yes | Partial | Prompt includes boot on column base, knee bend, water squeeze, and rebound, but does not state rear-foot/support-foot drive through ground into hip/shoulder/forearm. |
| Knee compression | Yes | Medium | No | Prompt says "膝盖弯曲" and later "膝盖压缩", but it is not bound to an explosive force chain and immediate impact timing. |
| Waist/hip drives shoulder, shoulder drives forearm | Partial | Yes | Partial | Prompt says "肩膀和腰胯继续向前压", but does not make waist/hip -> shoulder -> forearm a mandatory kinetic chain. |
| Column-base foot point as short trigger | Partial | Yes | Partial | Prompt says weight on column base "少于 0.40s", but 0.70s-1.15s gives 0.45s of screen time around foot placement, which may read as action display rather than instant trigger. |
| No hang time / no jump display / no parkour display | Partial | Yes | Partial | Prompt bans floating, wall-running, roof route, and long parkour, but does not explicitly say "no hang time" or "do not display the foot plant as a jump pose". |
| Immediate hit after foot contact | Weak | Yes | Partial | Prompt places foot plant 0.70s-1.15s and impact 1.15s-1.65s. That gives the model room to stage a soft rebound before impact. |
| Hit-stop only at impact, 0.10s-0.15s | Partial | Yes | Partial | Prompt says only key impacts have extremely short hit-stop, but does not specify `0.10s-0.15s`. |
| 5-6 contact beats retained | Yes | Low | No | Prompt requires at least 6 contact beats and schedules early, middle, and final contacts. |
| Tail keeps fighting / no idle tail | Yes | Low | No | Final 0.8s requires at least two contact beats and cuts during attack/guard/recoil/re-entry. |
| Environmental causality / no structural breakage | Yes | Low | No | Prompt binds railing movement to body/forearm/shoulder pressure and bans cracks, splinters, holes, collapse, and spontaneous damage. |
| Actor causality with Fenshou/Shuangji names | Yes | Low | No | Beats consistently name Fenshou and Shuangji and specify attack/defense roles. |
| Terrain affordance as tactical trigger, not spectacle | Partial | Yes | Partial | Prompt says one terrain assist only, but the time allocation and repeated "改变攻击角度" wording may make the terrain moment the display subject. |

## Direct Answers to K130 Audit Questions

1. V005 prompt explicitly wrote real speed and continuous combat, but did not strongly write quick attack / quick guard / quick counter as repeated hard constraints.
2. It partially forbids slow / static behavior, but does not explicitly ban full-clip slow motion, turn-based rhythm, or planted static exchange in the same clear language used by Source V1.2.
3. It includes fragments of force generation: boot contact, knee bend, waist/hip pressure, shoulder/forearm impact. It does not clearly write the complete chain: support foot -> knee compression -> hip/waist torque -> shoulder drive -> forearm/hammerfist impact.
4. It writes the column-base foot point as short and singular, but the 0.70s-1.15s setup plus 1.15s-1.65s impact can still read as a staged rebound display.
5. It bans floating, wall-running, roof route, and long parkour; it does not explicitly ban hang time or jump display, and it does not require contact-to-impact to happen almost immediately.
6. It says only key impact has very short hit-stop, but does not specify `0.10s-0.15s`.
7. It keeps 6 contact beats and the tail keeps fighting. This part is source-compliant.
8. Source rules read but not effectively translated: fast attack/guard/counter, explicit no turn-based/planted fighting, exact hit-stop duration, and complete kinetic force chain.
9. Potentially soft-inducing sentences include the long foot-plant window, "身体短暂侧斜向上改变角度", "短促反弹，改变攻击角度", and repeated "柱基 / 柱脚" setup language before the impact. These can make the model display a soft terrain move rather than snap directly into impact.
10. V006 must add strong force-chain constraints, shorter terrain-trigger timing, no hang-time / no jump-display language, exact hit-stop duration, and immediate follow-up beats.

## Suspected Soft-Force Causes

1. The prompt over-allocated time to terrain setup.
   - 0.70s-1.15s foot placement plus 1.15s-1.65s impact creates almost one second around the terrain move.
   - The model likely interpreted this as a visible jump/rebound action instead of a single explosive trigger.

2. The kinetic chain was fragmented.
   - Knee, hip, shoulder, forearm appear as separate descriptive details.
   - They are not written as one mandatory sequential force path.

3. The word "rebound" may have softened the action.
   - "短促反弹" can invite upward bounce or pose.
   - For V006, use "脚点一触即压缩发力，身体不离线，立刻砸中" style constraints.

4. The prompt protected terrain clarity at the expense of impact.
   - It asks to see the boot on the column base and the surface contact clearly.
   - That can cause the model to linger on leg display, despite "腿部单独展示超过 0.35 秒" being banned.

5. The speed rule was global but not operational.
   - "真实速度" alone is less forceful than explicit "快速出招、快速格挡、快速反击、不得一招一停、不得回合制".

6. Hit-stop was underspecified.
   - "极短 hit-stop" is directionally correct, but V006 should specify `0.10s-0.15s only at impact`.

## V006 Required Prompt Patches

V006 should include these as hard constraints:

1. Global rhythm:
   - "全片真实速度，快速出招、快速格挡、快速反击。不要整段慢动作，不要长时间升格，不要回合制，不要一招一停，不要站桩互殴。"

2. Terrain trigger:
   - "柱基脚点不是动作展示，只是 0.10s-0.18s 的爆发触发器。脚掌一触即压缩发力，不能停在柱基上摆姿势。"

3. No jump / no hang time:
   - "无滞空，不展示跳跃，不展示跑酷，不沿柱子上跑，身体不离开近身攻击线。"

4. Immediate hit:
   - "脚点接触后 0.12s-0.20s 内必须命中护架或肩甲。"

5. Full force chain:
   - "支撑脚蹬地 / 柱基脚点压缩 -> 膝盖压缩 -> 腰胯短促拧转 -> 肩线压下 -> 右前臂 / 锤拳式下砸命中。这个发力链必须连续，不可拆成展示动作。"

6. Hit-stop:
   - "只有命中瞬间 0.10s-0.15s hit-stop，其余动作保持真实速度。"

7. Post-impact density:
   - "命中后 0.20s 内必须进入下一次接触，至少两个快速 follow-up contact beats，不允许命中后摆姿势或停住。"

8. Keep V1.11 strengths:
   - first clear contact within `0.15s-0.30s`.
   - at least `5-6` clear contact beats.
   - every contact has attack path, contact point, defensive reaction, body/foot result, rebound, and re-entry.
   - final 0.8s has at least two contact/re-entry beats and cuts mid-action.

9. Keep environmental causality:
   - railing, water, sleeves, hair, armor droplets, and column occlusion only respond to body contact or force direction.
   - no structural damage unless a future shot explicitly designs it.

## Source Rules Read But Not Effectively Translated Into V005

- Source V1.2 fast combat language:
  - quick attack.
  - quick guard.
  - quick evade.
  - quick counter.
  - no full-clip slow motion.
  - no turn-based display.
  - no planted static exchange.

- Source V1.2 impact physics:
  - body part absorbs force.
  - shoulder/forearm load visibly.
  - knees sink to buffer.
  - short contact pause / hit-stop is bounded.
  - environment feedback erupts from contact point.

- Source V1.11 speed-up boundary:
  - local speed-up is useful only if action structure already works.
  - V005 appears to need prompt redesign, not only speed-up.

## Source Update Recommendation

Do not update Source immediately from V005 alone.

Recommendation:

- Use V005 as a case study in the next V006 prompt design.
- If V006 succeeds after adding explicit force-chain constraints, update Source with a new "terrain-triggered force-chain" rule.
- If V006 still fails, audit whether Dreamina has a systematic weakness with terrain-assisted close combat before changing Source.

Candidate future Source addition after V006:

- "For terrain-assisted combat, terrain contact must be written as a short force trigger, not a visible parkour display. Bind foot point, knee compression, waist/hip torque, shoulder drive, weapon/forearm line, impact, hit-stop, and follow-up contact into one timed chain."

## Safety

- Dreamina was not run.
- No submit was run.
- No query_result was run.
- No download was run.
- No retry or resubmit was run.
- No media was created.
- No package was prepared.
- `sources/` was read-only and not modified.
- Runtime code was not modified.
- `configs/providers.json` was not modified.
- No media was staged.
- `final_master=false`
- `locked=false`

## Final Verdict

SHOT03_V005_SOURCE_COMPLIANCE_AUDIT_READY_V006_FORCE_CHAIN_REDESIGN_REQUIRED
