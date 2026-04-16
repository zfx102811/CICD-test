# Lark CI/CD 集成测试计划

## Phase 1 — 验证基础 CI

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 1.1 | 创建项目 + 推送到 GitHub | Claude | ✅ |
| 1.2 | 确认 CI workflow 跑通 | Amay | ✅ |

## Phase 2 — 配置 Lark 机器人

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 2.1 | 在 Lark 群创建自定义机器人（Custom Bot） | Amay | ✅ |
| 2.2 | 复制机器人的 Webhook URL 给 Claude | Amay | ✅ |
| 2.3 | 本地 curl 测试 webhook 能通 | Claude | ✅ |

## Phase 3 — 配置 GitHub Secret

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 3.1 | GitHub repo → Settings → Secrets → Actions → 添加 `LARK_WEBHOOK_URL` | Amay | ✅ |

## Phase 4 — 测试 Staging 通知（push main 触发）

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 4.1 | 做一个小改动 push 到 main | Claude | ✅ |
| 4.2 | 确认 GitHub Actions 跑通 | Amay | ✅ |
| 4.3 | 确认 Lark 群收到绿色 staging 卡片 | Amay | ✅ |

## Phase 5 — 测试 Production 通知（push tag 触发）

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 5.1 | 创建并推送一个 tag（2026.16.0） | Claude | ✅ |
| 5.2 | 确认 GitHub Actions 跑通 | Amay | ✅ |
| 5.3 | 确认 Lark 群收到蓝色 production 卡片 | Amay | ✅ |

## Phase 6 — 测试失败通知

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 6.1 | 故意推一个会失败的代码到 main | Claude | ✅ |
| 6.2 | 确认 Lark 群收到红色失败卡片 | Amay | ✅ |
| 6.3 | 恢复正常代码 | Claude | ✅ |

## 全部完成 ✅

## 踩坑记录

1. **YAML heredoc 缩进问题** — `run: |` 块中的内容有缩进，bash heredoc 的结束标记（如 `EOF`）必须在行首才能匹配，导致所有 heredoc 方案失败
2. **GitHub Secret 首字符丢失** — 粘贴 webhook URL 到 GitHub Secret 时，`https` 的 `h` 被截掉，变成 `ttps://`，导致 `curl: Protocol "ttps" not supported`
3. **解决方案** — 用 `printf` + `%s` 构造 JSON 写入临时文件，再用 `curl -d @file` 发送，彻底避免 shell 引号和 YAML 转义的冲突

## 移植到 sti-platform 的要点

1. 将 `deploy-notify.yml` 复制到 `sti-platform/.github/workflows/`
2. 在 sti-platform repo 的 GitHub Settings 添加 `LARK_WEBHOOK_URL` secret（注意完整 URL）
3. 将 "Simulate staging deploy" 替换为真实部署步骤（SSH / docker compose pull 等）
4. 按需调整卡片内容和触发条件
