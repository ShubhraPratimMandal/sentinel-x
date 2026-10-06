CREATE TABLE IF NOT EXISTS entities (
    id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    name TEXT NOT NULL,
    confidence INTEGER NOT NULL CHECK (confidence BETWEEN 0 AND 100)
);

CREATE TABLE IF NOT EXISTS relationships (
    id BIGSERIAL PRIMARY KEY,
    source_entity_id TEXT NOT NULL REFERENCES entities(id),
    target_entity_id TEXT NOT NULL REFERENCES entities(id),
    relationship_type TEXT NOT NULL,
    confidence INTEGER NOT NULL CHECK (confidence BETWEEN 0 AND 100),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS evidence (
    id TEXT PRIMARY KEY,
    incident_id TEXT NOT NULL REFERENCES incidents(id),
    evidence_type TEXT NOT NULL,
    summary TEXT NOT NULL,
    source TEXT NOT NULL,
    confidence INTEGER NOT NULL CHECK (confidence BETWEEN 0 AND 100),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS incident_techniques (
    incident_id TEXT NOT NULL REFERENCES incidents(id),
    technique_id TEXT NOT NULL,
    technique_name TEXT NOT NULL,
    confidence INTEGER NOT NULL CHECK (confidence BETWEEN 0 AND 100),
    PRIMARY KEY (incident_id, technique_id)
);

CREATE INDEX IF NOT EXISTS idx_relationship_source ON relationships(source_entity_id);
CREATE INDEX IF NOT EXISTS idx_relationship_target ON relationships(target_entity_id);
CREATE INDEX IF NOT EXISTS idx_evidence_incident ON evidence(incident_id);
