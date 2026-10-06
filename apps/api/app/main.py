import os
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from .data import ALERTS, INCIDENTS, INDICATORS, TIMELINE
from .models import SystemOverview
from .risk import posture

VERSION = "0.3.0"

app = FastAPI(
    title="SENTINEL-X API",
    version=VERSION,
    description="Defensive cyber intelligence and threat analysis API.",
)

allowed_origins = os.getenv("SENTINEL_ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in allowed_origins if x.strip()],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    response.headers["Cache-Control"] = "no-store"
    return response

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "operational", "service": "sentinel-x-api", "version": VERSION}

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
        "environment": os.getenv("SENTINEL_ENV", "development"),
        "mode": "defensive-research",
        "data_mode": "synthetic",
        "services": {
            "api": "operational",
            "intelligence": "operational",
            "correlation": "operational",
            "ai": "standby",
        },
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

@app.get("/api/v1/incidents/{incident_id}/timeline")
def incident_timeline(incident_id: str):
    if not any(x.id == incident_id for x in INCIDENTS):
        raise HTTPException(status_code=404, detail="Incident not found")
    return {
        "incident_id": incident_id,
        "events": sorted(
            [x.model_dump() for x in TIMELINE if x.incident_id == incident_id],
            key=lambda x: x["timestamp"],
        ),
    }

@app.get("/api/v1/incidents/{incident_id}/workflow")
def incident_workflow(incident_id: str):
    incident = next((x for x in INCIDENTS if x.id == incident_id), None)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return {
        "incident_id": incident_id,
        "workflow": [
            {"stage": "TRIAGE", "status": "COMPLETE", "owner": "ANALYST-01"},
            {"stage": "INVESTIGATION", "status": "ACTIVE" if incident.status == "INVESTIGATING" else "QUEUED", "owner": "ANALYST-01"},
            {"stage": "CONTAINMENT", "status": "PENDING", "owner": "RESPONSE-TEAM"},
            {"stage": "RECOVERY", "status": "PENDING", "owner": "RESPONSE-TEAM"},
            {"stage": "LESSONS_LEARNED", "status": "PENDING", "owner": "CASE-MANAGER"},
        ],
        "next_action": "Validate evidence and document analyst disposition before containment.",
    }

@app.get("/api/v1/incidents/{incident_id}/report", response_class=PlainTextResponse)
def incident_report(incident_id: str):
    incident = next((x for x in INCIDENTS if x.id == incident_id), None)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    events = [x for x in TIMELINE if x.incident_id == incident_id]
    lines = [
        "SENTINEL-X INCIDENT REPORT",
        f"CASE: {incident.id}",
        f"TITLE: {incident.title}",
        f"SEVERITY: {incident.severity}",
        f"STATUS: {incident.status}",
        f"RISK SCORE: {incident.score}/100",
        "",
        "TECHNIQUES: " + ", ".join(incident.technique_ids),
        "INDICATORS: " + ", ".join(incident.indicator_ids),
        "",
        "TIMELINE",
    ]
    lines.extend(f"- {x.timestamp.isoformat()} | {x.event_type} | {x.description} | confidence={x.confidence}%" for x in events)
    lines += ["", "ANALYST NOTE: Synthetic defensive research data. Validate evidence before operational decisions."]
    return "\n".join(lines)

@app.get("/api/v1/analytics/risk-distribution")
def risk_distribution():
    buckets = {"0-24": 0, "25-49": 0, "50-74": 0, "75-89": 0, "90-100": 0}
    for alert in ALERTS:
        score = alert.score
        if score < 25: buckets["0-24"] += 1
        elif score < 50: buckets["25-49"] += 1
        elif score < 75: buckets["50-74"] += 1
        elif score < 90: buckets["75-89"] += 1
        else: buckets["90-100"] += 1
    return {"buckets": buckets, "method": "score-bucket distribution over synthetic alerts"}

@app.get("/api/v1/analytics/explain/{incident_id}")
def explain_risk(incident_id: str):
    incident = next((x for x in INCIDENTS if x.id == incident_id), None)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    evidence = [
        {"factor": "Alert severity", "weight": 35, "reason": incident.severity},
        {"factor": "Risk score", "weight": 30, "reason": f"{incident.score}/100"},
        {"factor": "Technique coverage", "weight": 20, "reason": f"{len(incident.technique_ids)} mapped techniques"},
        {"factor": "Indicator coverage", "weight": 15, "reason": f"{len(incident.indicator_ids)} linked indicators"},
    ]
    return {"incident_id": incident_id, "factors": evidence, "recommendation": "Prioritize corroboration and analyst review.", "confidence": 82}

@app.get("/api/v1/graph")
def graph():
    return {
        "nodes": [
            {"id": "INC-2026-0042", "type": "incident", "label": "Credential anomaly cluster"},
            {"id": "IOC-0001", "type": "indicator", "label": "198.51.100.42"},
            {"id": "T1110", "type": "technique", "label": "Brute Force"},
            {"id": "T1078", "type": "technique", "label": "Valid Accounts"},
            {"id": "AUTH-GATEWAY", "type": "sensor", "label": "AUTH-GATEWAY"},
        ],
        "edges": [
            {"source": "INC-2026-0042", "target": "IOC-0001", "type": "CONTAINS_INDICATOR"},
            {"source": "INC-2026-0042", "target": "T1110", "type": "MAPPED_TO_TECHNIQUE"},
            {"source": "INC-2026-0042", "target": "T1078", "type": "MAPPED_TO_TECHNIQUE"},
            {"source": "INC-2026-0042", "target": "AUTH-GATEWAY", "type": "OBSERVED_BY"},
        ],
    }

@app.post("/api/v1/ai/analyze")
def ai_analyze(case_id: str = Query(min_length=3, max_length=80)):
    incident = next((x for x in INCIDENTS if x.id == case_id), None)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return {
        "case_id": case_id,
        "mode": "advisory",
        "summary": f"{incident.title} is currently {incident.status.lower()} with a risk score of {incident.score}/100.",
        "observed": ["Synthetic security observations are correlated to this case.", "The case is mapped to defensive ATT&CK techniques."],
        "hypotheses": ["The evidence may represent a coordinated authentication pattern; analyst validation is required."],
        "gaps": ["Additional independent source corroboration is recommended before attribution."],
        "confidence": 78,
        "disclaimer": "AI output is advisory and must be verified against source evidence.",
    }

@app.get("/api/v1/search")
def search(q: str = Query(min_length=2, max_length=100)):
    needle = q.lower()
    return {
        "query": q,
        "indicators": [x for x in INDICATORS if needle in x.value.lower() or needle in x.id.lower()],
        "alerts": [x for x in ALERTS if needle in x.title.lower() or needle in x.id.lower()],
        "incidents": [x for x in INCIDENTS if needle in x.title.lower() or needle in x.id.lower()],
    }
