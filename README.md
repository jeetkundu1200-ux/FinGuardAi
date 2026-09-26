# 🛡️ FinGuard AI

> A modern transaction-risk lookup and fraud-search application with a FastAPI backend, a responsive frontend, and a synthetic 15,000-record transaction dataset.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)
![Dataset](https://img.shields.io/badge/Dataset-15%2C000%20synthetic%20records-5b8cff)

## ✨ Overview

FinGuard AI is a demonstration fraud-analysis application designed to make transaction investigation quick and understandable.

It supports:

- 🔎 Exact UTR transaction lookup
- 💬 Natural-language-style fraud search in the frontend
- 📊 Risk scoring from 0–100
- 🚨 LOW / MEDIUM / HIGH risk classification
- 💳 UPI and Card transaction filtering
- 📍 State and city filtering
- 💰 Amount and risk-score ranges
- ❤️ Transaction and fraud statistics
- 📚 Automatic FastAPI Swagger/OpenAPI documentation
- ☁️ Vercel-ready serverless deployment

The supplied frontend is a self-contained demo UI. The backend in `api/index.py` exposes the same transaction data through a clean REST API.

## 🧠 Risk model used by the demo

The dataset contains a `Risk_Score_0_100` field.

| Score | Risk level |
|---:|---|
| `< 30` | 🟢 LOW |
| `30–69` | 🟡 MEDIUM |
| `≥ 70` | 🔴 HIGH |

These thresholds are demonstration rules, not a production financial-risk model.

## 📦 Project structure

```text
FinGuard-AI/
├── api/
│   └── index.py              # FastAPI backend / Vercel Function
├── data/
│   └── transactions.json     # 15,000 synthetic transactions
├── docs/
│   └── API.md                # API reference
├── index.html                # Frontend demo
├── requirements.txt          # Python dependencies
├── vercel.json               # Vercel configuration
├── .env.example              # Environment variable template
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FinGuard-AI.git
cd FinGuard-AI
```

### 2. Create a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn api.index:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/api/docs
```

### 5. Open the frontend

For the static frontend, you can open `index.html` directly in a browser.

> Note: the supplied `index.html` currently contains its own embedded demo dataset and frontend search logic. The new FastAPI backend is provided as a separate API layer so the project can be migrated to API-backed frontend requests without changing the visual design.

## ☁️ Deploy to Vercel

Vercel supports Python Functions and can deploy a FastAPI backend from the `api/` directory. The project structure here follows that deployment model. 

### Option A — GitHub → Vercel

1. Push this folder to GitHub.
2. Open Vercel.
3. Import the GitHub repository.
4. Keep the project root at the repository root.
5. Deploy.
6. After deployment, test:

```text
https://YOUR-PROJECT.vercel.app/api/health
https://YOUR-PROJECT.vercel.app/api/stats
https://YOUR-PROJECT.vercel.app/api/docs
```

### Option B — Vercel CLI

Install the CLI:

```bash
npm i -g vercel
```

Then:

```bash
vercel
```

For production:

```bash
vercel --prod
```

## 🔌 API endpoints

### Health

```http
GET /api/health
```

Example response:

```json
{
  "status": "healthy",
  "records_loaded": 15000
}
```

### API information

```http
GET /api
```

### Transaction lookup

```http
GET /api/transaction/{UTR_ID}
```

Example:

```text
/api/transaction/UTR26082400001107
```

### Search

```http
GET /api/search
```

Supported filters:

| Parameter | Example |
|---|---|
| `label` | `Fraud` |
| `risk` | `HIGH` |
| `method` | `UPI` |
| `state` | `West Bengal` |
| `city` | `Kolkata` |
| `min_amount` | `40000` |
| `max_amount` | `100000` |
| `min_risk` | `70` |
| `max_risk` | `100` |
| `limit` | `20` |

Example:

```text
/api/search?risk=HIGH&method=UPI&state=Delhi&min_amount=40000&limit=10
```

### Statistics

```http
GET /api/stats
```

Returns total records, fraud/genuine counts, and LOW/MEDIUM/HIGH risk counts.

## 🧪 Example curl commands

```bash
curl http://127.0.0.1:8000/api/health
```

```bash
curl http://127.0.0.1:8000/api/transaction/UTR26082400001107
```

```bash
curl "http://127.0.0.1:8000/api/search?risk=HIGH&method=UPI&limit=5"
```

```bash
curl http://127.0.0.1:8000/api/stats
```

## 🔐 Security notes

This repository is a demonstration project.

The included dataset is synthetic and should not be treated as real banking or personally identifiable financial information.

For a production deployment:

- Do not expose real customer transaction data in a public repository.
- Add authentication and authorization.
- Add rate limiting.
- Validate and sanitize all user input.
- Move transaction storage to a proper database.
- Store secrets in Vercel Environment Variables.
- Add audit logging.
- Add monitoring and alerting.
- Use HTTPS-only production access.
- Do not expose sensitive payment credentials, card numbers, CVV values, passwords, or authentication secrets.

## 📈 Future improvements

- PostgreSQL / Supabase transaction storage
- JWT or OAuth authentication
- Real-time transaction ingestion
- Isolation Forest anomaly detection
- Supervised fraud classification
- Explainable risk scoring
- Redis caching
- Pagination and cursor-based search
- Admin dashboard
- Model monitoring
- Automated tests and CI/CD

## 🧩 Architecture

```text
                    ┌─────────────────────┐
                    │     User / Browser  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     index.html      │
                    │   FinGuard AI UI    │
                    └──────────┬──────────┘
                               │
                         REST / JSON
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Vercel Function   │
                    │   FastAPI / Python  │
                    │     api/index.py    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ transactions.json   │
                    │ 15,000 synthetic    │
                    │ transaction records │
                    └─────────────────────┘
```

## ⚠️ Important

FinGuard AI is an educational/demo application. Its risk score and fraud labels are based on the supplied synthetic dataset and demonstration logic. They should not be used as the sole basis for real financial decisions.

## 📄 License

Released under the MIT License. See [`LICENSE`](./LICENSE).

## 👤 Project

**FinGuard AI**  
Transaction Risk Lookup & Fraud Search

Built for learning, demonstration, and hackathon/project presentation purposes.
