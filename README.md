# SENTINEL-X

### Advanced Cyber Intelligence & Threat Analysis Platform

> A defensive cybersecurity research platform for threat intelligence fusion, incident analysis, entity correlation, AI-assisted investigation, and security operations visualization.

**Project Status:** 🟡 Active Development  
**Current Release:** 0.3.0-analyst-operations  
**Classification:** Public Research / Demonstration  
**Primary Focus:** Cybersecurity • Threat Intelligence • AI • Security Analytics • Cloud

---

## Mission

SENTINEL-X is a portfolio-grade cyber intelligence platform designed to demonstrate how disparate security observations can be normalized, correlated, scored, investigated, and presented to analysts through a unified operational interface.

The platform uses **synthetic and authorized defensive data** for demonstrations. It is not designed for unauthorized surveillance, intrusion, exploitation, or targeting of real-world systems.

## Current Build

The first vertical slice is now established:

- React + TypeScript analyst console
- FastAPI service with health and system-status endpoints
- Docker Compose development stack
- PostgreSQL and Redis service foundations
- Architecture and threat-model documentation
- Synthetic-data boundary
- GitHub Actions repository validation
- Security and contribution policies
- Dark analyst command-center UI foundation

## Core Capabilities

- Threat intelligence and IOC management
- Security event normalization and correlation
- Risk scoring and prioritization
- Incident and case management
- Entity relationship analysis
- MITRE ATT&CK-aligned technique mapping
- Investigation timelines
- Threat visualization
- AI-assisted defensive analysis
- Analyst notes and evidence tracking
- API-driven architecture
- Containerized deployment
- Automated testing and CI

## High-Level Architecture

```text
                     +--------------------------+
                     |       SENTINEL-X         |
                     |   Intelligence Platform  |
                     +------------+-------------+
                                  |
             +--------------------+--------------------+
             v                    v                    v
      +-------------+      +-------------+      +-------------+
      | Threat Intel|      | AI Analysis |      | Investigation|
      |    Layer    |      |    Layer    |      |     Layer    |
      +------+------+      +------+------+      +------+------+
             +--------------------+--------------------+
                                  v
                     +--------------------------+
                     | Correlation / Risk Engine|
                     +------------+-------------+
                                  v
                     +--------------------------+
                     | Analyst Command Interface |
                     +------------+-------------+
                                  v
                     +--------------------------+
                     | Cases • Alerts • Reports |
                     +--------------------------+
```

## Repository Structure

```text
sentinel-x/
├── apps/
│   ├── web/                 # Analyst web application
│   └── api/                 # FastAPI service
├── services/
│   ├── correlation/         # Event/entity correlation engine
│   ├── intelligence/       # Threat intelligence processing
│   └── ai/                  # AI-assisted analysis services
├── data/
│   ├── synthetic/           # Safe demo datasets
│   └── schemas/             # Data contracts
├── database/
│   ├── migrations/
│   └── seeds/
├── docs/
│   ├── architecture/
│   ├── security/
│   ├── api/
│   └── operations/
├── infra/
│   ├── docker/
│   └── oci/
├── tests/
│   ├── unit/
│   └── integration/
├── .github/
│   └── workflows/
├── docker-compose.yml
├── .env.example
├── SECURITY.md
├── CONTRIBUTING.md
└── README.md
```

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React + TypeScript + Vite |
| UI | Custom dark analyst console CSS |
| API | Python + FastAPI |
| Database | PostgreSQL |
| Cache / Jobs | Redis |
| AI / Analytics | Python |
| Containers | Docker |
| CI/CD | GitHub Actions |
| Cloud | Oracle Cloud Infrastructure |
| Graph Analysis | Graph-based relationship model |

## Roadmap

### Phase 1 — Foundation
- [x] Repository initialized
- [x] Architecture baseline
- [x] Web application shell
- [x] API service
- [x] Database service foundation
- [x] Docker development environment
- [x] CI repository validation

### Phase 2 — Intelligence Core
- [x] IOC registry
- [x] Event normalization foundation
- [x] Correlation engine foundation
- [x] Risk scoring
- [x] Incident management foundation
- [x] ATT&CK mapping foundation

### Phase 3 — Analyst Operations
- [x] Investigation workspace foundation
- [x] Entity graph foundation
- [x] Timeline analysis
- [x] Threat visualization foundation
- [x] Analyst workflow
- [x] Audit trail

### Phase 4 — AI & Analytics
- [x] Advisory AI analyst endpoint
- [x] Report generation
- [x] Confidence-aware analysis
- [x] Advanced analytics
- [x] Explainable recommendations

### Phase 5 — Cloud & Release
- [x] Security hardening baseline
- [x] CI/CD + CodeQL + public demo pipeline
- [x] OCI deployment template
- [x] Production-readiness documentation
- [x] Public demo workflow

## Release & Demonstration

The repository includes a GitHub Pages workflow for the public synthetic-data demonstration. The web console falls back to offline demo data when the API is unavailable. This is a research/demo release, not an operational intelligence system.

## Local Development

See [Local Development](docs/operations/local-development.md).

Quick start:

```bash
docker compose up --build
```

Then open `http://localhost:5173`.

## Safety Boundary

SENTINEL-X is intended for **authorized defensive research, education, and security operations simulation**. The project must not be used to gain unauthorized access to systems, conduct covert surveillance, evade security controls, or target individuals or organizations.

## Author

**Shubhra Pratim Mandal**  
Cybersecurity • AI • Cloud Computing • Computer Science
