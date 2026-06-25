# ML Serving Platform

A lightweight machine learning model registry and serving API — built to practice production-grade backend engineering (databases, migrations, authentication, containerization) and real Git/GitHub collaboration workflows (issue → branch → PR → review → merge).

## What This Project Does

This platform lets you:
- Register ML models with metadata (name, version, framework, file location)
- Serve predictions through versioned REST endpoints *(in progress)*
- Log every prediction for auditability and monitoring *(in progress)*
- Authenticate every request via API key

It's a simplified version of real-world ML infrastructure — the layer that sits between "a model trained in a notebook" and "a model other software can actually call."

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | FastAPI |
| Database | PostgreSQL 16 |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Containerization | Docker & Docker Compose |
| Auth | API key (header-based) |

---

## Project Structure

```
ml-serving-platform/
├── app/
│   ├── api/            # route definitions (APIRouter per resource)
│   │   └── models.py
│   ├── core/           # auth/security logic
│   │   └── security.py
│   ├── db/             # database connection + base class
│   │   ├── base.py
│   │   └── session.py
│   ├── models/         # SQLAlchemy table definitions
│   │   ├── user.py
│   │   ├── model.py
│   │   └── prediction.py
│   ├── schemas/        # Pydantic request/response shapes
│   │   └── model.py
│   └── main.py         # FastAPI app entrypoint
├── alembic/             # database migration history
│   └── versions/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env                 # local config (not committed)
```

---

## Getting Started

**Prerequisites:** Docker Desktop (with WSL2 backend on Windows)

```bash
git clone https://github.com/avnimujawdiya/ml-serving-platform.git
cd ml-serving-platform
docker compose up --build
```

This starts:
- A PostgreSQL container (`db`) on port `5432`
- The FastAPI app (`api`) on port `8000`

Once running:
- **API docs (interactive):** http://localhost:8000/docs
- **Health check:** http://localhost:8000/health

**Apply database migrations** (first run only):
```bash
docker compose run api alembic upgrade head
```

---

## API Endpoints (current)

| Method | Endpoint | Auth required | Description |
|---|---|---|---|
| GET | `/health` | No | Basic liveness check |
| GET | `/me` | Yes | Returns the authenticated user's info |
| POST | `/models` | Yes | Register a new model (name, version, framework, file path) |

**Authentication:** send a header `X-API-Key: <your_key>` on any protected route. Missing or invalid keys return `401 Unauthorized`.

---

## Database Schema

**`users`** — registered API consumers
- `id`, `email` (unique), `api_key` (unique), `created_at`

**`models`** — registered ML models
- `id`, `name`, `version`, `framework`, `file_path`, `status`, `created_at`

**`predictions`** — every inference logged *(table exists, not yet wired to an endpoint)*
- `id`, `model_id` (foreign key → `models.id`), `input_data` (JSONB), `output_data` (JSONB), `latency_ms`, `created_at`

All schema changes are tracked as Alembic migration files in `alembic/versions/` — never edited directly in the database.

---

## Development Workflow

Every feature follows the same loop, practiced solo to build real Git discipline:

1. Open a GitHub Issue describing the task
2. Branch off `main`: `issue-N-short-description`
3. Implement, test locally
4. Commit, push, open a PR with `Closes #N` in the description
5. Self-review the diff
6. Squash-merge into `main`
7. Issue auto-closes; branch deleted

---

## Progress / Roadmap

| # | Feature | Status |
|---|---|---|
| 1 | Docker Compose + Postgres + FastAPI skeleton | ✅ Done |
| 2 | Alembic migrations + core SQLAlchemy models | ✅ Done |
| 3 | API key authentication middleware | ✅ Done |
| 4 | `POST /models` — register a model | ✅ Done |
| 5 | `POST /predict/{model_id}` — serve real predictions | 🔜 In progress |
| 6 | `GET /predictions` — view logged predictions | ⬜ Planned |
| 7 | `GET /models/{id}/metrics` — accuracy/latency stats | ⬜ Planned |
| 8 | Model versioning (multiple versions per model) | ⬜ Planned |
| 9 | Rate limiting per API key | ⬜ Planned |
| 10 | CI pipeline (GitHub Actions: lint + test + migration check) | ⬜ Planned |
| 11 | Basic prediction drift detection | ⬜ Planned |

---

## Why This Project Exists

Built to practice two things together: real MLOps-adjacent backend patterns (model registries, inference serving, schema migrations) and the actual day-to-day discipline of professional software development — issue tracking, branching, code review, and merge hygiene — run solo to internalize the workflow before relying on a team.
