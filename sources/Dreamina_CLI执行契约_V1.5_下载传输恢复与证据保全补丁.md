# Dreamina_CLI执行契约_V1.5_下载传输恢复与证据保全补丁

> 类型：P0 Dreamina CLI execution contract supplement  
> 状态：候选，待用户手动应用  
> 适用：query_result、媒体下载、download route reset、敏感 URL、ffmpeg/ffprobe、Windows filesystem  
> 本文件不授权任何 live 操作。

---

## 0. 一句话结论

```text
CLI query success 不保证 CLI 内置下载器能完成响应体传输。
重复确认 body-read timeout 后，同一 --download_dir 路线必须耗尽；
只能在 fresh human authorization 下，切换为 fresh query-only URL + ephemeral direct HTTP transport。
```

## 1. 证据边界

在 Windows 环境、Dreamina binary `2a20fff-dirty` 下，四条已远端 success 的视频结果在：

```text
dreamina query_result --submit_id <id> --download_dir <dir>
```

中两轮均于约 34 秒返回：

```text
DOWNLOAD_TRANSPORT_BODY_READ_TIMEOUT
context deadline exceeded (Client.Timeout or context cancellation while reading body)
```

每次产生非零部分 MP4，说明：

- generation/query 结果存在；
- 传输已开始；
- 失败层级是 CLI download response-body transport；
- 不能把该错误重分类为 generation failure。

这是版本与环境绑定的实测证据，不代表所有未来 CLI 版本都会失败。未来仍以 fresh `dreamina version` 与 runtime help 为最高命令事实源。

## 2. Route exhaustion

同一 submit ID 的同一 CLI download route：

- 默认一次调用；
- 失败后若人类批准一次 replacement 且再次得到相同 body-read timeout，则该路线 `EXHAUSTED`；
- 不得继续第三次同命令重试；
- retry/resubmit/download replacement 均需 fresh explicit human authorization；
- route reset 必须使用结构不同的 transport，而不是重新包装相同命令。

## 3. 受限 Direct HTTP recovery

只有同时满足以下条件才可使用：

1. 远端 query 已为 terminal success；
2. CLI `--download_dir` route 已明确耗尽；
3. fresh human authorization 明确允许 query-only URL 与 direct HTTP；
4. signed URL 可在内存中取得；
5. URL 不会持久化；
6. 有固定 HTTP client、timeout、partial-file、resume 和技术校验合同。

推荐结构：

```text
one fresh query_result without --download_dir
→ parse exactly one HTTPS video URL in memory
→ pass URL through process memory or curl --config - stdin
→ same-volume .part file
→ bounded transfer
→ optional single resume for allowlisted transient errors
→ same-volume rename
→ SHA-256 + ffprobe + complete ffmpeg decode
```

## 4. Signed URL 保密边界

禁止 signed URL 或其 hash 出现在：

- argv；
- environment variable；
- config/response/temp file；
- shell history / transcript；
- stdout/stderr persistence；
- report / JSON / manifest / Git；
- debug exception text。

允许持久化的只有：

```yaml
url_observed_in_memory: true/false
url_scheme: HTTPS
url_persisted: false
url_hash_persisted: false
```

应使用结构化 redaction，而不是 blanket substring scan。

## 5. HTTP transfer contract

一个被授权的参考合同：

```yaml
follow_redirects: true
fail_on_http_error: true
connect_timeout_seconds: 30
total_timeout_seconds: 300
low_speed_limit_bytes_per_second: 1024
low_speed_time_seconds: 120
same_volume_partial_file: true
initial_transfer_count: 1
maximum_resume_count: 1
```

仅允许对 transient transport interruption 使用同一 fresh URL 断点续传。不得在 401/403/404、签名拒绝、证书失败、磁盘失败或 URL 无效时 resume。

## 6. Preflight evidence persistence

每个独立 preflight 命令的结果必须在执行下一项可能失败的检查前进入内存 record 或临时 evidence：

```text
run help
→ capture exit code/stdout/stderr hash/required flags
→ persist local preflight evidence
→ only then run ffprobe/ffmpeg/path checks
```

不得把 help、PATH discovery、ffprobe 和 serialization 放在一个“后项失败会抹掉前项证据”的脆弱 PowerShell 表达式中。

## 7. ffmpeg / ffprobe

在依赖它们的 combined executor 前必须：

- 解析 absolute path；
- 验证 regular file、bytes、SHA-256 和 version；
- 后续使用绝对路径；
- 不在执行中切换 binary；
- 不依赖 PATH 恰好存在。

当前已验证环境曾使用：

```text
C:/ffmpeg/bin/ffprobe.exe
C:/ffmpeg/bin/ffmpeg.exe
```

未来仍需 fresh identity verification。

## 8. Windows filesystem

跨盘 directory rename 不是可移植操作。媒体临时文件应优先与最终目标位于同一 volume。

如必须跨盘：

```text
exclusive destination create
→ copy bytes
→ flush/close
→ compare byte count
→ compare SHA-256
→ delete source only after equality
```

本地 move/copy 失败不得自动触发新的 Provider 下载。

## 9. Failure evidence

失败记录至少保存：

- exit code；
- elapsed time；
- timeout；
- stdout/stderr bytes 与 SHA-256；
- sanitized failure class；
- structurally redacted sanitized message；
- partial-file bytes 与 SHA-256；
- raw output persisted = false；
- signed URL persisted = false。

不能只保存 `stderr_bytes` 而丢失可诊断语义。

## 10. Authority boundary

本文件不授权：

- query；
- download；
- direct HTTP；
- retry/resubmit；
- credit；
- Source write；
- semantic review；
- production/final/lock。
