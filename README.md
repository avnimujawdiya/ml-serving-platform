# 🤖 ML Serving Platform

A simple machine learning model registry and serving API — built with **FastAPI + PostgreSQL + Docker** 🐍🐘🐳

This project also doubles as practice for real-world Git/GitHub teamwork: every feature starts as an **Issue**, gets built on its own **branch**, and goes through a proper **Pull Request** before joining the main project — just like how real software teams (and open source projects) work! 🚀

---

## 🎯 What Does This Project Actually Do?

Think of it like a mini version of what big AI companies use behind the scenes:

1. 📦 You **register** a machine learning model (give it a name, version, etc.)
2. 🔮 People can send data to it and get a **prediction** back
3. 📝 Every prediction gets **logged**, so you always know what happened
4. 🔑 Only people with a valid **API key** are allowed to use it

It's a small, real version of the kind of system that lets a trained AI model actually be *used* by other apps — not just sit in a notebook.

---

## 🛠️ Built With

| What | Used For |
|---|---|
| 🐍 Python 3.11 | The main language |
| ⚡ FastAPI | Turns Python code into a working web API |
| 🐘 PostgreSQL | Stores all the data (users, models, predictions) |
| 🔗 SQLAlchemy | Lets Python talk to the database easily |
| 🧬 Alembic | Tracks every change made to the database, like a history log |
| 🐳 Docker | Packages everything so it runs the same on any computer |
| 🔑 API Keys | Keeps the API secure — no key, no access |

---

## 📁 How the Project is Organized

```
ml-serving-platform/
├── app/
│   ├── api/         📍 all the actual endpoints live here
│   ├── core/         🔐 the security/login logic
│   ├── db/           🗄️ database connection setup
│   ├── models/       🧱 defines what each database table looks like
│   ├── schemas/       📋 defines what JSON in/out should look like
│   └── main.py        🚪 the front door of the app
├── alembic/            📜 history of every database change ever made
├── docker-compose.yml  🐳 tells Docker what to run
├── Dockerfile           🐳 the recipe for building the app
└── requirements.txt     📦 list of Python packages needed
```

---

## 🚀 How to Run This Yourself

**You'll need:** Docker Desktop installed (with WSL2 if you're on Windows)

```bash
git clone https://github.com/avnimujawdiya/ml-serving-platform.git
cd ml-serving-platform
docker compose up --build
```

That's it! Docker will set up everything — the database and the API — automatically. ✨

**First time only**, apply the database migrations:
```bash
docker compose run api alembic upgrade head
```

Once it's running, check these out in your browser:
- 📖 **Interactive API docs:** http://localhost:8000/docs
- ❤️ **Health check:** http://localhost:8000/health

---

## 🔌 What You Can Actually Do With the API (so far)

| Method | Endpoint | Need a key? 🔑 | What it does |
|---|---|---|---|
| `GET` | `/health` | ❌ No | Just checks "is the server alive?" |
| `GET` | `/me` | ✅ Yes | Shows info about whoever is logged in |
| `POST` | `/models` | ✅ Yes | Registers a brand new model |

> 🔑 **How auth works:** add a header called `X-API-Key` with your secret key to any request. No key (or a wrong one) = `401 Unauthorized` 🚫

---

## 🗃️ What's Stored in the Database

**`users`** 👤 — people allowed to use the API
- id, email, api_key, created_at

**`models`** 🧠 — every ML model that's been registered
- id, name, version, framework, file_path, status, created_at

**`predictions`** 🔮 — every prediction ever made *(coming soon — table's ready, endpoint isn't yet!)*
- id, model_id, input_data, output_data, latency_ms, created_at

Every single change to these tables is tracked by Alembic — nothing is ever changed by hand. 🧬

---

## 🔁 How Features Get Built (the workflow)

Every new feature follows the exact same steps — like a mini assembly line:

1. 📝 Open a GitHub **Issue** describing what needs to be built
2. 🌿 Create a new **branch** just for that issue
3. 💻 Write the code, test it locally
4. ⬆️ Push the branch, open a **Pull Request**
5. 👀 Review it (even solo — read it like a stranger would!)
6. ✅ **Merge** it into the main project
7. 🎉 Issue automatically closes!

This is the same flow real engineering teams use every day — practicing it solo means it's already second nature by the time teamwork comes into play.

---

## 🗺️ Progress So Far

| # | Feature | Status |
|---|---|---|
| 1 | 🐳 Docker + Postgres + FastAPI set up | ✅ Done |
| 2 | 🧬 Database migrations + core tables | ✅ Done |
| 3 | 🔑 API key authentication | ✅ Done |
| 4 | 📦 Register a model (`POST /models`) | ✅ Done |
| 5 | 🔮 Actually serve predictions | 🔜 In Progress |
| 6 | 📜 View past predictions | ⬜ Planned |
| 7 | 📊 Model accuracy/speed stats | ⬜ Planned |
| 8 | 🆕 Support multiple model versions | ⬜ Planned |
| 9 | 🚦 Rate limiting | ⬜ Planned |
| 10 | 🤖 Automated testing (CI) | ⬜ Planned |
| 11 | 📉 Detect when a model's predictions get weird | ⬜ Planned |

---

## 💡 Why I Built This

To get real practice with two things at once:
- **Actually building** the kind of backend system used in production ML platforms (not just training models in a notebook)
- **Actually practicing** the Git/GitHub workflow real engineering teams use — issues, branches, pull requests, reviews — solo first, so it's muscle memory before working with a team again 💪