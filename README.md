# 🛡️ FinGuard AI

### AI-Based Real-Time Financial Fraud Detection

> **FinGuard AI** is a fintech fraud-risk platform that lets users look up a UTR and inspect transaction-level risk indicators from a **15,000-record synthetic/demo transaction dataset**.

[![FinTech](https://img.shields.io/badge/Theme-Fin--Tech-5b7cff?style=for-the-badge)](#)
[![Records](https://img.shields.io/badge/Dataset-15%2C000%20Records-21e6a1?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Demo-ffb020?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-Unspecified-lightgrey?style=for-the-badge)](#-license)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](#-contributing)

---

## 📑 Table of Contents

- [What is FinGuard AI?](#-what-is-finguard-ai)
- [Current Application Features](#-current-application-features)
- [Example](#-example)
- [Current Implementation](#️-current-implementation)
- [Proposed AI Fraud-Detection Architecture](#-proposed-ai-fraud-detection-architecture)
- [Proposed Real-Time Flow](#️-proposed-real-time-flow)
- [Technology Direction](#️-technology-direction)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Dataset](#-dataset)
- [UI Design](#-ui-design)
- [Known Limitations](#-known-limitations)
- [FAQ](#-faq)
- [Roadmap](#️-roadmap)
- [Built With](#-built-with)
- [HyperFusion 2026](#-hyperfusion-2026)
- [Team NEXORA](#-team-nexora)
- [Contributing](#-contributing)
- [Research & References](#-research--references)
- [Disclaimer](#️-disclaimer)
- [License](#-license)
- [Contact](#-contact)

---

## 🚀 Dashboard Preview

Add the dashboard screenshot generated for this project to:

```text
assets/finguard-dashboard-preview.png
```

Then this image will appear automatically on GitHub:

![FinGuard AI Dashboard Preview](assets/finguard-dashboard-preview.png)

---

## 🎯 What is FinGuard AI?

FinGuard AI is a **UTR Transaction Risk Lookup** application built around a transaction dataset containing **15,000 synthetic/demo records**.

A user enters a UTR ID, and the application:

1. Searches the local transaction dataset.
2. Retrieves the matching transaction.
3. Displays a **0–100 risk score**.
4. Assigns a risk level.
5. Shows transaction, device, network, behavioural and security attributes.
6. Displays the recorded fraud-risk reason.

The current lookup application is a **working front-end/demo implementation**. The larger AI fraud-detection architecture described below is the proposed production direction for the project.

---

## ✨ Current Application Features

### 🔎 UTR Lookup

Enter a UTR ID such as:

```text
UTR26082400001107
```

The application searches the embedded transaction dataset and returns the matching record.

### 📊 Risk Score

Each transaction contains a recorded `Risk_Score_0_100` value.

The current application uses these thresholds:

| Score | Risk Level |
|---:|---|
| `< 30` | 🟢 Low Risk |
| `30–69` | 🟡 Medium Risk |
| `≥ 70` | 🔴 High Risk |

### 🧾 Transaction Details

The lookup result can display:

- Transaction ID
- Fraud / Genuine label
- Amount
- Payment method
- Sender
- Receiver
- UPI ID
- Card token
- Timestamp
- City
- State
- Network type
- Device type
- Device trust
- Beneficiary type
- Previous transactions with receiver
- Transaction frequency
- Time pattern
- Location pattern
- Authentication signal
- Network risk
- Account security
- Behaviour pattern

### 🧠 Risk Explanation

Each dataset record contains a `Fraud_Risk_Reason` field, which is displayed with the transaction result.

### 📱 Responsive Interface

The current interface is designed as a lightweight responsive web page with a dark fintech-style visual design.

### 💻 Prerequisites / Browser Support

No installation, build step, or backend is required to run the current demo.

- Any modern browser (Chrome, Firefox, Edge, Safari — latest two versions)
- JavaScript enabled
- No internet connection required after the page is loaded, since the dataset is embedded client-side
- Optional: Python 3 (or any static file server) if you prefer serving the file over `http://` instead of opening it directly via `file://`

---

## 🧪 Example

Example transaction lookup:

```text
UTR ID
UTR26082400001107

Transaction
TXN26082400001107

Label
Fraud

Risk Score
85 / 100

Risk Level
HIGH RISK

Reason
Authentication and velocity anomalies
```

> The dataset is synthetic/demo data and should not be treated as real financial transaction data.

---

## 🏗️ Current Implementation

The current uploaded application is intentionally lightweight:

```text
index.html
README.md
```

The main application is contained in a single self-contained HTML file.

### Current architecture

```text
                ┌──────────────────────┐
                │      User / UI       │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     UTR Input        │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Local Transaction   │
                │   Dataset (15,000)   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   UTR Lookup / Map   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Risk Score + Details │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Risk Result Display  │
                └──────────────────────┘
```

The application creates a lookup map from the embedded records and matches the entered UTR against `UTR_ID`.

---

## 🤖 Proposed AI Fraud-Detection Architecture

For the full FinGuard AI vision, the proposed architecture places the fraud engine between a payment gateway and the bank/core system.

```text
UPI / CARD TRANSACTION
          │
          ▼
     API GATEWAY
          │
          ▼
  FEATURE EXTRACTION
          │
          ▼
      AI FRAUD MODEL
          │
          ▼
   RISK SCORING ENGINE
          │
     ┌────┼────┐
     ▼    ▼    ▼
   ALLOW FLAG BLOCK
```

### Detection approach

The proposed system combines:

- **Supervised machine learning**
- **Anomaly detection**
- **Rule-based detection**
- **Behavioural profiling**
- **Continuous 0–100 risk scoring**
- **Feedback-driven adaptive learning**

The HyperFusion 2026 proposal identifies:

- XGBoost / Random Forest for supervised classification
- Autoencoder / Isolation Forest for anomaly detection
- FastAPI / Flask for inference APIs
- Kafka for event streaming
- MongoDB / PostgreSQL for storage
- AWS / cloud deployment
- React.js for the application interface
- OAuth2 / encryption for security

These technologies describe the **proposed architecture**, not all components currently implemented in the uploaded demo.

---

## ⚙️ Proposed Real-Time Flow

```text
Transaction
     │
     ▼
Feature Extraction
     │
     ├── Amount
     ├── Time
     ├── Location
     ├── Device
     ├── Network
     ├── Authentication
     ├── Account Security
     └── Behaviour Pattern
     │
     ▼
ML + Anomaly Detection + Rules
     │
     ▼
Risk Score (0–100)
     │
     ├── 0–29   → ALLOW
     ├── 30–69  → FLAG / REVIEW
     └── 70–100 → BLOCK
```

> These proposed boundaries match the Low / Medium / High thresholds used in the current demo (see [Risk Score](#-risk-score)) so the two stay consistent as the project evolves.

---

## 🛠️ Technology Direction

| Layer | Current Demo | Proposed Full System |
|---|---|---|
| Interface | HTML / CSS / JavaScript | React.js |
| Dataset | Embedded synthetic records | Database / transaction stream |
| Lookup | Client-side UTR map | API service |
| Risk value | Stored dataset score | ML + anomaly + rules |
| API | Not required by current demo | FastAPI / Flask |
| Streaming | Not implemented | Apache Kafka |
| Database | Embedded dataset | MongoDB / PostgreSQL |
| ML | Not executed in current UI | XGBoost / Random Forest / anomaly models |
| Deployment | Static web page | Cloud / AWS |
| Security | Demo scope | OAuth2 / encryption |

---

## 📁 Project Structure

```text
FinGuard-AI/
│
├── index.html
├── README.md
│
└── assets/
    └── finguard-dashboard-preview.png
```

If you later split the application into a frontend/backend architecture, the repository can evolve into:

```text
FinGuard-AI/
├── frontend/
├── backend/
├── ml/
├── data/
├── assets/
└── README.md
```

---

## 🚀 Getting Started

### Option 1 — Open directly

The current application is self-contained.

Open:

```text
index.html
```

in a modern web browser.

### Option 2 — Run with a local web server

From the project directory:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

---

## 🔍 Dataset

The current demo contains:

```text
15,000 transaction records
```

The records include UTR IDs, transaction IDs, labels, amounts, payment methods, sender/receiver information, timestamps, location, device/network attributes, behavioural signals, risk scores and fraud-risk reasons.

**Important:** The supplied dataset is explicitly described as **synthetic/demo data**. It must not be interpreted as real customer or banking data.

---

## 🎨 UI Design

The current interface follows a dark fintech dashboard style with:

- Dark navy background
- Blue primary actions
- Green low-risk indicators
- Amber medium-risk indicators
- Red high-risk indicators
- Transaction result cards
- Risk score presentation
- Responsive layout

The visual direction is intended to communicate a **financial-security / fraud-monitoring** product rather than a generic data lookup page.

---

## ⚠️ Known Limitations

Being transparent about the current demo's scope:

- **No real detection logic.** Risk scores and reasons are pre-computed values stored in the dataset, not the output of a live model — the app performs lookup and display only.
- **No backend or persistence.** Everything runs client-side in the browser; there is no API, database, or server component yet.
- **Not built for real transactions.** The dataset is synthetic and the app has no authentication, encryption, or audit logging — it is not suitable for production or real financial data.
- **Single-file architecture.** `index.html` currently contains markup, styles, and the embedded dataset together, which will need to be split out as the project grows (see [Project Structure](#-project-structure)).

---

## ❓ FAQ

**Q: Can I look up a real transaction?**
No. The dataset is 15,000 synthetic/demo records — it contains no real customer or banking data.

**Q: Does this actually detect fraud in real time?**
Not yet. The current app looks up a pre-scored record by UTR. Real-time detection is described in [Proposed AI Fraud-Detection Architecture](#-proposed-ai-fraud-detection-architecture) as the intended production direction.

**Q: Do I need to install anything to try it?**
No — see [Prerequisites / Browser Support](#-prerequisites--browser-support). Just open `index.html` in a browser.

**Q: Where do I find a sample UTR to try?**
See the [Example](#-example) section for a sample UTR ID and its expected result.

---

## 🗺️ Roadmap

### Phase 1 — Current Demo

- [x] UTR lookup
- [x] 15,000-record dataset
- [x] Risk score display
- [x] Low / Medium / High classification
- [x] Transaction detail display
- [x] Fraud-risk reason display
- [x] Responsive UI

### Phase 2 — AI Engine

- [ ] Feature engineering pipeline
- [ ] Fraud classification model
- [ ] Anomaly detection model
- [ ] Rule engine
- [ ] Model evaluation
- [ ] Explainable risk factors
- [ ] Model feedback loop

### Phase 3 — Production Architecture

- [ ] FastAPI / Flask backend
- [ ] Database integration
- [ ] Authentication
- [ ] Kafka transaction streaming
- [ ] Cloud deployment
- [ ] Security controls
- [ ] Monitoring and logging

### Phase 4 — Advanced Platform

- [ ] Analyst dashboard
- [ ] Real-time transaction stream
- [ ] Fraud trend analytics
- [ ] Model monitoring
- [ ] Automated feedback and retraining
- [ ] Production payment-gateway integration

---

## 🏆 HyperFusion 2026

**Project:** FinGuard AI  
**Theme:** Fin-Tech  
**Team:** Team NEXORA

The HyperFusion 2026 proposal defines FinGuard AI as a real-time financial fraud-detection concept targeting UPI and card transactions, with a proposed risk-scoring and decision layer designed around rapid transaction analysis.

---

## 🧩 Built With

This project was built with the help of **Claude Sonnet 5** (Anthropic), used as a development assistant for:

- Writing and structuring the frontend (`index.html` — HTML/CSS/JS)
- Building the FastAPI backend (`api/index.py`) for the Vercel deployment
- Drafting and refining this README and project documentation

**Important for judges:** No AI model runs inside the live application. The `Risk_Score_0_100` and `Fraud_Risk_Reason` values are pre-computed fields stored directly in the synthetic dataset — the current demo performs lookup and display only, it does not perform live inference. Claude was a tool used *to build* the project, not a component running *inside* it. Live AI-driven scoring (XGBoost / anomaly detection) is planned for **Phase 2** of the [Roadmap](#️-roadmap).

---

Built by **Team NEXORA** for **HyperFusion 2026**.

---

## 🤝 Contributing

This project started as a hackathon prototype for HyperFusion 2026. Contributions, issues, and feature suggestions are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a pull request describing what you changed and why

For larger changes (e.g. work toward Phase 2/3 of the roadmap), please open an issue first to discuss the approach.

---

## 📚 Research & References

The project proposal references the following resources:

1. **NPCI — UPI Overview & Ecosystem** — [npci.org.in](https://www.npci.org.in/what-we-do/upi/product-overview)
2. **RBI — Digital Payment Security Controls** — [rbi.org.in](https://www.rbi.org.in/)
3. **XGBoost — Official Documentation** — [xgboost.readthedocs.io](https://xgboost.readthedocs.io/)
4. **Apache Kafka — Official Documentation** — [kafka.apache.org](https://kafka.apache.org/documentation/)
5. **Kaggle — Credit Card Fraud Detection Dataset** — [kaggle.com](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## ⚠️ Disclaimer

FinGuard AI is a **prototype / demonstration project**.

The current UTR lookup application uses synthetic/demo transaction data and should not be used to make real financial, banking, fraud, or payment decisions.

The proposed AI architecture is a project design direction and does not represent a production-certified fraud-detection system.

---

## 📄 License

No license has been specified for this project yet. Until a license is added, all rights are reserved by **Team NEXORA**, and the code should not be reused or redistributed without permission.

> Consider adding an open-source license (e.g. MIT, Apache 2.0) if you intend for others to reuse this code.

---

## 📬 Contact

For questions, feedback, or collaboration inquiries about FinGuard AI, please reach out via the repository's **Issues** tab or contact **Team NEXORA** through the HyperFusion 2026 event organizers.

---

## ⭐ FinGuard AI

> **Detect risk. Explain the signal. Protect the transaction.**

**FinGuard AI — Protect Before the Payment Clears.**
