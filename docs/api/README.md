# SENTINEL-X API

Base URL in local development: `http://localhost:8000`

## Health

`GET /health`

Returns API availability and version.

## System

- `GET /api/v1/system/overview`
- `GET /api/v1/system/status`

## Intelligence

- `GET /api/v1/indicators`
- `GET /api/v1/indicators/{indicator_id}`
- `GET /api/v1/alerts`
- `GET /api/v1/incidents`
- `GET /api/v1/incidents/{incident_id}`
- `GET /api/v1/search?q=...`
- `GET /api/v1/graph`

## AI Analyst

`POST /api/v1/ai/analyze?case_id=INC-2026-0042`

The current implementation is an advisory deterministic demonstration. It does not execute external actions and does not claim attribution.

Interactive OpenAPI documentation is available at `/docs` when the API is running.
