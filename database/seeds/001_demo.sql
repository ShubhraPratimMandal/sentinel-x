INSERT INTO indicators (id, indicator_type, value, confidence, severity, source, first_seen, last_seen)
VALUES
('IOC-0001','ipv4','198.51.100.42',94,'CRITICAL','SYNTHETIC-SENSOR-A',NOW(),NOW()),
('IOC-0002','domain','telemetry-lab.example',81,'HIGH','SYNTHETIC-DNS',NOW(),NOW()),
('IOC-0003','sha256',repeat('0',64),73,'MEDIUM','SYNTHETIC-ENDPOINT',NOW(),NOW())
ON CONFLICT (id) DO NOTHING;

INSERT INTO incidents (id,title,severity,status,score,created_at,updated_at)
VALUES
('INC-2026-0042','Credential anomaly cluster','CRITICAL','INVESTIGATING',91,NOW(),NOW()),
('INC-2026-0041','Synthetic DNS correlation','HIGH','OPEN',78,NOW(),NOW())
ON CONFLICT (id) DO NOTHING;
