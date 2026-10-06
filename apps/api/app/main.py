from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from .data import ALERTS, INCIDENTS, INDICATORS, TIMELINE
from .models import SystemOverview
from .risk import posture

app = FastAPI(
    title="SENTINEL-X API",
    version="0.2.0",
    description="Defensive cyber intelligence and threat analysis API.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "operational", "service": "sentinel-x-api", "version": "0.2.0"}

@app.get("/api/v1/system/overview", response_model=SystemOverview)
def overview() -> SystemOverview:
    return SystemOverview(
        active_cases=len(INCIDENTS),
        correlated_events=1842,
        high_risk_iocs=sum(i.severity in ("HIGH", "CRITICAL") for i in INDICATORS),
        analyst_queue=sum(a.status != "CLOSED" for a in ALERTS),
        threat_posture=posture([a.score for a in ALERTS]),
        open_alerts=sum(a.status == "OPEN" for a in ALERTS),
        incidents=len(INCIDENTS),
        generated_at=datetime.now(timezone.utc),
    )

@app.get("/api/v1/system/status")
def system_status() -> dict:
    return {
        "platform": "SENTINEL-X",
        "environment": "development",
        "mode": "defensive-research",
        "data_mode": "synthetic",
        "services": {"api": "operational", "intelligence": "operational", "correlation": "operational", "ai": "standby"},
    }

@app.get("/api/v1/indicators")
def indicators(indicator_type: str | None = Query(default=None), severity: str | None = Query(default=None)):
    rows = INDICATORS
    if indicator_type:
        rows = [x for x in rows if x.indicator_type == indicator_type]
    if severity:
        rows = [x for x in rows if x.severity == severity.upper()]
    return rows

@app.get("/api/v1/indicators/{indicator_id}")
def indicator(indicator_id: str):
    for row in INDICATORS:
        if row.id == indicator_id:
            return row
    raise HTTPException(status_code=404, detail="Indicator not found")

@app.get("/api/v1/alerts")
def alerts(status: str | None = Query(default=None), severity: str | None = Query(default=None)):
    rows = ALERTS
    if status:
        rows = [x for x in rows if x.status == status.upper()]
    if severity:
        rows = [x for x in rows if x.severity == severity.upper()]
    return rows

@app.get("/api/v1/incidents")
def incidents(status: str | None = Query(default=None)):
    rows = INCIDENTS
    if status:
        rows = [x for x in rows if x.status == status.upper()]
    return rows

@app.get("/api/v1/incidents/{incident_id}")
def incident(incident_id: str):
    for row in INCIDENTS:
        if row.id == incident_id:
            return {"incident": row, "timeline": [x for x in TIMELINE if x.incident_id == incident_id]}
    raise HTTPException(status_code=404, detail="Incident not found")

@app.get("/api/v1/search")
def search(q: str = Query(min_length=2, max_length=100)):
    needle = q.lower()
    return {
        "query": q,
        "indicators": [x for x in INDICATORS if needle in x.value.lower() or needle in x.id.lower()],
        "alerts": [x for x in ALERTS if needle in x.title.lower() or needle in x.id.lower()],
        "incidents": [x for x in INCIDENTS if needle in x.title.lower() or needle in x.id.lower()],
    }
