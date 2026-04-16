# cicd-test

Lark + GitHub Actions CI/CD integration playground.

## Structure

```
app/main.py              — minimal FastAPI app
Dockerfile               — production-ready image
docker-compose.yml       — local run
.github/workflows/
  ci.yml                 — basic CI (every push)
  deploy-notify.yml      — staging/production deploy + Lark notification
```

## Setup

1. Create a Lark Custom Bot in your group chat, copy the webhook URL
2. In GitHub repo: Settings → Secrets → Actions → add `LARK_WEBHOOK_URL`
3. Push to `main` → triggers staging deploy + Lark notification
4. Push a tag → triggers production deploy + Lark notification

## Local test

```bash
docker compose up --build
curl http://localhost:8000/health
```

## Test Lark webhook locally

```bash
curl -X POST "<your-webhook-url>" \
  -H "Content-Type: application/json" \
  -d '{"msg_type":"text","content":{"text":"[TEST] hello from cicd-test"}}'
```
