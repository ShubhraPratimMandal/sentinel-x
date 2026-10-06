from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field

Severity = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]

class Indicator(BaseModel):
    id: str
    indicator_type: Literal["ipv4", "domain", "url", "sha256"]
    value: str
    confidence: int = Field(ge=0, le=100)
    severity: Severity
    source: str
    first_seen: datetime
    last_seen: datetime

class Alert(BaseModel):
    id: str
    title: str
    severity: Severity
    source: str
    status: Literal["OPEN", "INVESTIGATING", "CLOSED"]
    score: int = Field(ge=0, le=100)
    created_at: datetime

class Incident(BaseModel):
    id: str
    title: str
    severity: Severity
    status: Literal["OPEN", "INVESTIGATING", "CONTAINED", "CLOSED"]
    score: int = Field(ge=0, le=100)
    technique_ids: list[str] = []
    indicator_ids: list[str] = []
    created_at: datetime
    updated_at: datetime

class TimelineEvent(BaseModel):
    id: str
    incident_id: str
    timestamp: datetime
    event_type: str
    description: str
    confidence: int = Field(ge=0, le=100)

class AuditEvent(BaseModel):
    id: str
    actor: str
    action: str
    target: str
    timestamp: datetime
    outcome: Literal["SUCCESS", "REVIEW", "DENIED"]
    details: str = ""

class SystemOverview(BaseModel):
    active_cases: int
    correlated_events: int
    high_risk_iocs: int
    analyst_queue: int
    threat_posture: int
    open_alerts: int
    incidents: int
    generated_at: datetime

def now() -> datetime:
    return datetime.now(timezone.utc)
