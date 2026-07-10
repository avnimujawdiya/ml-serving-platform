# 🤖 ML Serving Platform

A production-grade machine learning model registry and serving API — built with **FastAPI + PostgreSQL + Docker** 🐍🐘🐳

This project also doubles as practice for real-world Git/GitHub teamwork: every feature starts as an **Issue**, gets built on its own **branch**, and goes through a proper **Pull Request** before joining the main project — just like how real software teams (and open source projects) work! 🚀

> ✅ **Project complete — all 10 issues shipped and merged.**

---

## 🎯 What Does This Project Actually Do?

Think of it like a mini version of what big AI companies use behind the scenes:

1. 📦 **Register** a machine learning model (name, version, framework, file location)
2. 🔮 **Send data** to it and get a real **prediction** back
3. 📝 Every prediction gets **logged** automatically — input, output, latency
4. 📊 **Query stats** — total predictions, average latency per model
5. 🆕 **Version your models** — register v2, old version auto-deprecates
6. 🚦 **Rate limiting** — API keys are capped at 5 requests per minute
7. 🔑 Only people with a valid **API key** are allowed in
8. 🤖 **CI pipeline** runs automatically on every PR (lint + migrations + tests)

It's a small, real version of the kind of system that lets a trained AI model actually be *used* by other apps — not just sit in a notebook.

---

## 🛠️ Built With

| What | Used For |
|---|---|
| 🐍 Python 3.11 | The main language |
| ⚡ FastAPI | Turns Python code into a working web API |
| 🐘 PostgreSQL 16 | Stores all the data (users, models, predictions) |
| 🔗 SQLAlchemy | Lets Python talk to the database without raw SQL |
| 🧬 Alembic | Tracks every schema change like a git history for the database |
| 🐳 Docker + Compose | Packages everything so it runs the same on any computer |
| 🔑 API Keys | Keeps the API secure — no key, no access |
| 🤖 GitHub Actions | Runs tests automatically on every PR |
| 🧠 scikit-learn | The actual ML library powering predictions |

---

## 📁 How the Project is Organized

```
ml-serving-platform/
├── app/
│   ├── api/                📍 all endpoints (models, predict, predictions, metrics)
│   ├── core/               🔐 auth + rate limiting logic
│   ├── db/                 🗄️ database connection + base class
│   ├── models/             🧱 SQLAlchemy table definitions
│   ├── schemas/            📋 Pydantic request/response shapes
│   └── main.py             🚪 FastAPI app entrypoint
├── alembic/                📜 full migration history
│   └── versions/
├── ml_models/              🧠 trained .pkl model files
├── scripts/                🛠️ one-off scripts (train_model.py, train_model_v2.py)
├── tests/                  🧪 pytest test suite
├── .github/workflows/      🤖 GitHub Actions CI
├── docker-compose.yml      🐳 defines db + api services
├── Dockerfile              🐳 recipe for building the API image
└── requirements.txt        📦 all Python dependencies
```

---

## 🚀 How to Run This Yourself

**You'll need:** Docker Desktop installed (with WSL2 if you're on Windows)

```bash
git clone https://github.com/avnimujawdiya/ml-serving-platform.git
cd ml-serving-platform
docker compose up --build
```

That's it! Docker sets up everything — database and API — automatically. ✨

**First time only**, apply the database migrations:
```bash
docker compose run api alembic upgrade head
```

Once it's running, open these in your browser:
- 📖 **Interactive API docs:** http://localhost:8000/docs
- ❤️ **Health check:** http://localhost:8000/health

---

## 🔌 Full API Reference

| Method | Endpoint | Auth 🔑 | What it does |
|---|---|---|---|
| `GET` | `/health` | ❌ | Liveness check |
| `GET` | `/me` | ✅ | Returns authenticated user info |
| `POST` | `/models` | ✅ | Register a model (auto-deprecates old version) |
| `POST` | `/predict/{model_id}` | ✅ | Run inference by model ID, log result |
| `POST` | `/predict/by-name/{name}` | ✅ | Run inference using latest active version by name |
| `GET` | `/predictions` | ✅ | List all predictions (filterable by `?model_id=`) |
| `GET` | `/models/{id}/metrics` | ✅ | Total predictions + avg latency for a model |

> 🔑 **Auth:** send `X-API-Key: <your_key>` header on every protected request. Missing or wrong key → `401 Unauthorized` 🚫
>
> 🚦 **Rate limiting:** more than 5 requests per minute from one API key → `429 Too Many Requests`

---

## 🗃️ Database Schema

**`users`** 👤 — who can call the API
- `id`, `email` (unique), `api_key` (unique), `created_at`

**`models`** 🧠 — registered ML models
- `id`, `name`, `version`, `framework`, `file_path`, `status` (active/deprecated), `created_at`

**`predictions`** 🔮 — every inference ever logged
- `id`, `model_id` → `models.id` (FK), `input_data` (JSONB), `output_data` (JSONB), `latency_ms`, `created_at`

**`rate_limits`** 🚦 — request tracking per API key
- `id`, `api_key`, `window_start`, `request_count`, `created_at`

Every schema change is tracked as an Alembic migration file — nothing ever touched by hand. 🧬

---

## 🔁 How Every Feature Was Built

Every single feature followed the exact same loop:

1. 📝 Open a **GitHub Issue** describing the task
2. 🌿 Create a **branch**: `issue-N-short-description`
3. 💻 Write the code, test locally
4. ⬆️ Commit, push, open a **Pull Request** with `Closes #N`
5. 👀 **Self-review** the diff in "Files changed"
6. ✅ **Squash-merge** into main
7. 🎉 Issue **auto-closes**, branch deleted

This is the same flow real engineering teams use every day.

---

## 🤖 CI Pipeline (GitHub Actions)

Every PR automatically runs:
1. **Lint** with `flake8` (max line length 120)
2. **Migrations** — `alembic upgrade head` against a real Postgres container
3. **Tests** — `pytest tests/` with 3 test cases

PRs can't merge with a broken CI run. ✅

---

## ✅ Complete Feature Roadmap

| # | Feature | Status |
|---|---|---|
| 1 | 🐳 Docker + Postgres + FastAPI skeleton | ✅ Done |
| 2 | 🧬 Alembic migrations + core tables | ✅ Done |
| 3 | 🔑 API key authentication middleware | ✅ Done |
| 4 | 📦 `POST /models` — register a model | ✅ Done |
| 5 | 🔮 `POST /predict/{model_id}` — real ML inference | ✅ Done |
| 6 | 📜 `GET /predictions` — view logged predictions | ✅ Done |
| 7 | 📊 `GET /models/{id}/metrics` — stats endpoint | ✅ Done |
| 8 | 🆕 Model versioning + predict-by-name | ✅ Done |
| 9 | 🚦 Rate limiting per API key | ✅ Done |
| 10 | 🤖 GitHub Actions CI (lint + migrations + tests) | ✅ Done |

---

## 💡 Why I Built This

To practice two things together:

- **Actually building** the kind of backend system used in production ML platforms — not just training models in a notebook, but serving them through a real API with auth, logging, versioning, and monitoring
- **Actually practicing** the Git/GitHub workflow real engineering teams use — issues, branches, pull requests, self-review, squash-merges — solo first, so it's already muscle memory before working with a team again 💪

---

## 👩‍💻 Author

**Avni Mujawdiya** — AI & Data Science student at JECRC University

GitHub: [@avnimujawdiya](https://github.com/avnimujawdiya)
