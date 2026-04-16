# Lark CI/CD 集成测试计划

## Phase 1 — 验证基础 CI

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 1.1 | 创建项目 + 推送到 GitHub | Claude | ✅ |
| 1.2 | 确认 CI workflow 跑通 | Amay：打开 Actions 页面确认 | ⬜ |

## Phase 2 — 配置 Lark 机器人

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 2.1 | 在 Lark 群创建自定义机器人（Custom Bot） | Amay | ⬜ |
| 2.2 | 复制机器人的 Webhook URL 给 Claude | Amay | ⬜ |
| 2.3 | 本地 curl 测试 webhook 能通 | Claude | ⬜ |

## Phase 3 — 配置 GitHub Secret

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 3.1 | GitHub repo → Settings → Secrets → Actions → 添加 `LARK_WEBHOOK_URL` | Amay | ⬜ |

## Phase 4 — 测试 Staging 通知（push main 触发）

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 4.1 | 做一个小改动 push 到 main | Claude | ⬜ |
| 4.2 | 确认 GitHub Actions 跑通 | Amay | ⬜ |
| 4.3 | 确认 Lark 群收到绿色 staging 卡片 | Amay | ⬜ |

## Phase 5 — 测试 Production 通知（push tag 触发）

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 5.1 | 创建并推送一个 tag（如 `2026.16.0`） | Claude | ⬜ |
| 5.2 | 确认 GitHub Actions 跑通 | Amay | ⬜ |
| 5.3 | 确认 Lark 群收到蓝色 production 卡片 | Amay | ⬜ |

## Phase 6 — 测试失败通知（可选）

| # | 步骤 | 谁做 | 状态 |
|---|---|---|---|
| 6.1 | 故意推一个会失败的代码到 main | Claude | ⬜ |
| 6.2 | 确认 Lark 群收到红色失败卡片 | Amay | ⬜ |
| 6.3 | 恢复正常代码 | Claude | ⬜ |
