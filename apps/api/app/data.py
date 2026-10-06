from .models import Alert, Incident, Indicator, TimelineEvent, now

INDICATORS = [
    Indicator(id="IOC-0001", indicator_type="ipv4", value="198.51.100.42", confidence=94, severity="CRITICAL", source="SYNTHETIC-SENSOR-A", first_seen=now(), last_seen=now()),
    Indicator(id="IOC-0002", indicator_type="domain", value="telemetry-lab.example", confidence=81, severity="HIGH", source="SYNTHETIC-DNS", first_seen=now(), last_seen=now()),
    Indicator(id="IOC-0003", indicator_type="sha256", value="0"*64, confidence=73, severity="MEDIUM", source="SYNTHETIC-ENDPOINT", first_seen=now(), last_seen=now()),
    Indicator(id="IOC-0004", indicator_type="url", value="https://demo.invalid/resource", confidence=66, severity="MEDIUM", source="SYNTHETIC-WEB", first_seen=now(), last_seen=now()),
]

ALERTS = [
    Alert(id="SX-0421", severity="CRITICAL", title="Synthetic credential anomaly cluster", source="AUTH-GATEWAY", status="INVESTIGATING", score=91, created_at=now()),
    Alert(id="SX-0418", severity="HIGH", title="Suspicious DNS observation group", source="DNS-SENSOR", status="OPEN", score=78, created_at=now()),
    Alert(id="SX-0415", severity="MEDIUM", title="Repeated failed authentication pattern", source="IDENTITY", status="OPEN", score=61, created_at=now()),
]

INCIDENTS = [
    Incident(id="INC-2026-0042", title="Credential anomaly cluster", severity="CRITICAL", status="INVESTIGATING", score=91, technique_ids=["T1110", "T1078"], indicator_ids=["IOC-0001"], created_at=now(), updated_at=now()),
    Incident(id="INC-2026-0041", title="Synthetic DNS correlation", severity="HIGH", status="OPEN", score=78, technique_ids=["T1071.004"], indicator_ids=["IOC-0002"], created_at=now(), updated_at=now()),
]

TIMELINE = [
    TimelineEvent(id="EV-1001", incident_id="INC-2026-0042", timestamp=now(), event_type="DETECTION", description="Synthetic authentication anomaly detected.", confidence=96),
    TimelineEvent(id="EV-1002", incident_id="INC-2026-0042", timestamp=now(), event_type="CORRELATION", description="Events correlated by source, timing, and indicator relationship.", confidence=88),
    TimelineEvent(id="EV-1003", incident_id="INC-2026-0042", timestamp=now(), event_type="TRIAGE", description="Analyst triage elevated the incident for investigation.", confidence=93),
]
