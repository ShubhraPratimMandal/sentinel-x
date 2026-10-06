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

INSERT INTO entities (id,entity_type,name,confidence)
VALUES
('ENT-0001','incident','INC-2026-0042',96),
('ENT-0002','indicator','IOC-0001',94),
('ENT-0003','technique','T1110',90),
('ENT-0004','technique','T1078',88),
('ENT-0005','sensor','AUTH-GATEWAY',91)
ON CONFLICT (id) DO NOTHING;

INSERT INTO relationships (source_entity_id,target_entity_id,relationship_type,confidence)
VALUES
('ENT-0001','ENT-0002','CONTAINS_INDICATOR',94),
('ENT-0001','ENT-0003','MAPPED_TO_TECHNIQUE',90),
('ENT-0001','ENT-0004','MAPPED_TO_TECHNIQUE',88),
('ENT-0001','ENT-0005','OBSERVED_BY',91)
ON CONFLICT DO NOTHING;

INSERT INTO incident_techniques (incident_id,technique_id,technique_name,confidence)
VALUES
('INC-2026-0042','T1110','Brute Force',90),
('INC-2026-0042','T1078','Valid Accounts',88)
ON CONFLICT DO NOTHING;
