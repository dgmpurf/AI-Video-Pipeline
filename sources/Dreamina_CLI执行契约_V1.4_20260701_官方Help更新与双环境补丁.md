# Dreamina_CLI执行契约_V1.4_20260701_官方Help更新与双环境补丁

> 类型：Dreamina CLI execution contract supplement
> 状态：待用户手动应用；手动上传 / 同步后作为 official Source 使用。
> 依据：`PHASE_DREAMINA_CLI_UPDATE_HELP_LOGIN_SKILL_SNAPSHOT_V1_4_10` and `DREAMINA_CLI_HELP_SNAPSHOT_AFTER_UPDATE_20260701`

## 1. Purpose

This supplement records the 2026-07-01 Dreamina CLI refresh evidence after official v1.4.10 / 2026-06-26 installer metadata.

It does not replace runtime canary checks. Current runtime `dreamina <command> -h` remains the highest command fact source.

## 2. Version Evidence

Old K266/K268 evidence chain:

```text
version: 46b5b0e-dirty
commit: 46b5b0e
build_time: 2026-06-03T19:39:25Z
```

Current binary version:

```text
version: 2a20fff-dirty
commit: 2a20fff
build_time: 2026-06-26T06:36:39Z
```

Installer metadata:

```text
version: v1.4.10
release_date: 2026-06-26
```

## 3. PowerShell vs Linux CLI Rule

Preferred live execution path for this Windows/Codex workspace:

```text
C:/Users/msjpurf/bin/dreamina.exe
```

Reason:

- This PowerShell-visible CLI returned the current binary version.
- `user_credit` succeeded.
- Non-sensitive evidence showed `vip_level=maestro` and `total_credit=1637`.

Linux installed path:

```text
/home/ke/.local/bin/dreamina
```

Rule:

Do not use the Linux CLI for live submit unless `dreamina login checklogin` has succeeded and `dreamina user_credit` succeeds in that same Linux environment.

## 4. Help Update Summary

The 2026-07-01 help snapshot adds or confirms:

- `text2image --generate_num` with range `1-10`
- `image2image --generate_num` with range `1-10`
- `seedance2.0_vip` supports `4k` in `text2video`
- `seedance2.0_vip` supports `4k` in `image2video`
- `seedance2.0_vip` supports `4k` in `frames2video`
- `seedance2.0_vip` supports `4k` in `multimodal2video`
- `seedance2.0mini` appears in supported video model lists where shown by help
- image/video command help uses Seedance 1.x model names where applicable
- `multimodal2video` still supports repeated `--image`

## 5. K266/K268 Failure Relevance

K266/K268 repeated empty submit failures happened on an older CLI evidence chain. The refreshed CLI materially changes command help and may affect future submit behavior, but no fix is proven until a future authorized submit succeeds.

Do not claim the old failure is fixed based only on update/help evidence.

## 6. Future Submit Gate

Every future live submit phase must still:

1. Confirm `sources/` is clean.
2. Run canary/preflight in the actual execution environment.
3. Verify `dreamina version`.
4. Verify `dreamina user_credit`.
5. Verify `dreamina <target command> -h`.
6. Verify package command fields against current help.
7. Execute only the human-authorized live action.
8. Keep submit, query, download, retry, resubmit, final, and lock separate unless explicitly macro-authorized.

## 7. No Automatic Source Or Route Mutation

This Source candidate does not authorize:

- submit
- query
- download
- retry
- resubmit
- batch
- media creation
- final
- lock
- Codex modification of official `sources/`

## 8. Recommended Operational Rule

For SHOT-04 R02a K269D/K269 planning, use the refreshed help snapshot for command-contract review, but require a fresh live-phase canary before any one-submit-only action.
