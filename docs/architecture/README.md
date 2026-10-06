# SENTINEL-X Architecture

## System Boundaries

SENTINEL-X is organized around four core domains:

- **Ingestion:** accepts authorized or synthetic security observations.
- **Intelligence:** normalizes indicators and contextual data.
- **Correlation:** connects observations into entities, campaigns, and incidents.
- **Analyst Experience:** exposes defensible findings through dashboards and cases.

## Data Flow

```
Sources
  |
  v
Ingestion -> Normalization -> Validation
                         |
                         v
                 Intelligence Store
                         |
                +--------+--------+
                |                 |
                v                 v
          Correlation        AI Analysis
                |                 |
                +--------+--------+
                         |
                         v
                    Risk Engine
                         |
                         v
                 Incident / Case
                         |
                         v
                  Analyst Console
```

## Design Goals

- Auditability
- Least privilege
- Deterministic core analytics
- Explainable risk decisions
- Clear provenance for intelligence
- Safe synthetic demonstration data
- Replaceable AI provider
