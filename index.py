"""
FinGuard AI — Transaction Risk API
Vercel Serverless / FastAPI backend.

The API uses the synthetic transaction dataset in data/transactions.json.
It is intentionally stateless and requires no database for the demo.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "transactions.json"

DATA_LOAD_ERROR: Optional[str] = None
TRANSACTIONS: list[dict] = []
BY_UTR: dict[str, dict] = {}

try:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        TRANSACTIONS = json.load(f)
    BY_UTR = {str(row.get("UTR_ID", "")).upper(): row for row in TRANSACTIONS}
except Exception as exc:  # noqa: BLE001 - deliberately broad: this must never crash cold start
    # Loading the dataset must never take down the whole function. If the file is
    # missing (e.g. not bundled by the deployment) or malformed, keep the app
    # running with an empty dataset and surface a clear error via /api/health
    # instead of a bare 500 FUNCTION_INVOCATION_FAILED.
    DATA_LOAD_ERROR = f"{type(exc).__name__}: {exc}"

app = FastAPI(
    title="FinGuard AI API",
    version="1.0.0",
    description="Transaction lookup, fraud search and risk statistics API.",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Useful for local development and separate frontend hosting.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def risk_level(score: float) -> str:
    if score < 30:
        return "LOW"
    if score < 70:
        return "MEDIUM"
    return "HIGH"


def enrich(row: dict) -> dict:
    result = dict(row)
    score = float(result.get("Risk_Score_0_100") or 0)
    result["Risk_Level"] = risk_level(score)
    return result


@app.get("/api")
def api_root():
    return {
        "name": "FinGuard AI API",
        "version": "1.0.0",
        "status": "online" if DATA_LOAD_ERROR is None else "degraded",
        "records": len(TRANSACTIONS),
        "data_load_error": DATA_LOAD_ERROR,
        "docs": "/api/docs",
    }


@app.get("/api/health")
def health():
    if DATA_LOAD_ERROR is not None:
        raise HTTPException(
            status_code=503,
            detail=f"Dataset failed to load: {DATA_LOAD_ERROR}",
        )
    return {"status": "healthy", "records_loaded": len(TRANSACTIONS)}


@app.get("/api/transaction/{utr}")
def get_transaction(utr: str):
    if DATA_LOAD_ERROR is not None:
        raise HTTPException(status_code=503, detail=f"Dataset unavailable: {DATA_LOAD_ERROR}")
    row = BY_UTR.get(utr.upper())
    if row is None:
        raise HTTPException(status_code=404, detail="UTR ID not found")
    return enrich(row)


@app.get("/api/search")
def search_transactions(
    label: Optional[str] = Query(None, description="Fraud or Genuine"),
    risk: Optional[str] = Query(None, description="LOW, MEDIUM or HIGH"),
    method: Optional[str] = Query(None, description="UPI or Card"),
    state: Optional[str] = None,
    city: Optional[str] = None,
    min_amount: Optional[float] = Query(None, ge=0),
    max_amount: Optional[float] = Query(None, ge=0),
    min_risk: Optional[float] = Query(None, ge=0, le=100),
    max_risk: Optional[float] = Query(None, ge=0, le=100),
    limit: int = Query(20, ge=1, le=100),
):
    results = TRANSACTIONS

    if label:
        wanted = label.strip().lower()
        results = [r for r in results if str(r.get("Label", "")).lower() == wanted]

    if risk:
        wanted = risk.strip().upper()
        results = [
            r for r in results
            if risk_level(float(r.get("Risk_Score_0_100") or 0)) == wanted
        ]

    if method:
        wanted = method.strip().lower()
        results = [
            r for r in results
            if str(r.get("Payment_Method", "")).lower() == wanted
        ]

    if state:
        wanted = state.strip().lower()
        results = [r for r in results if str(r.get("State", "")).lower() == wanted]

    if city:
        wanted = city.strip().lower()
        results = [r for r in results if str(r.get("City", "")).lower() == wanted]

    if min_amount is not None:
        results = [r for r in results if float(r.get("Amount_INR") or 0) >= min_amount]

    if max_amount is not None:
        results = [r for r in results if float(r.get("Amount_INR") or 0) <= max_amount]

    if min_risk is not None:
        results = [
            r for r in results
            if float(r.get("Risk_Score_0_100") or 0) >= min_risk
        ]

    if max_risk is not None:
        results = [
            r for r in results
            if float(r.get("Risk_Score_0_100") or 0) <= max_risk
        ]

    return {
        "count": len(results),
        "returned": min(len(results), limit),
        "filters": {
            "label": label,
            "risk": risk,
            "method": method,
            "state": state,
            "city": city,
            "min_amount": min_amount,
            "max_amount": max_amount,
            "min_risk": min_risk,
            "max_risk": max_risk,
        },
        "results": [enrich(r) for r in results[:limit]],
    }


@app.get("/api/stats")
def stats():
    fraud = sum(1 for r in TRANSACTIONS if r.get("Label") == "Fraud")
    genuine = len(TRANSACTIONS) - fraud
    low = sum(
        1 for r in TRANSACTIONS
        if risk_level(float(r.get("Risk_Score_0_100") or 0)) == "LOW"
    )
    medium = sum(
        1 for r in TRANSACTIONS
        if risk_level(float(r.get("Risk_Score_0_100") or 0)) == "MEDIUM"
    )
    high = sum(
        1 for r in TRANSACTIONS
        if risk_level(float(r.get("Risk_Score_0_100") or 0)) == "HIGH"
    )
    return {
        "total": len(TRANSACTIONS),
        "fraud": fraud,
        "genuine": genuine,
        "risk_levels": {"low": low, "medium": medium, "high": high},
    }


# Local development:
#   uvicorn api.index:app --reload
