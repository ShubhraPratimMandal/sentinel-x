# SENTINEL-X

### Advanced Cyber Intelligence & Threat Analysis Platform

> A defensive cybersecurity research platform for threat intelligence fusion, incident analysis, entity correlation, AI-assisted investigation, and security operations visualization.

**Project Status:** 🟡 Active Development  
**Classification:** Public Research / Demonstration  
**Primary Focus:** Cybersecurity • Threat Intelligence • AI • Security Analytics • Cloud

---

## Mission

SENTINEL-X is a portfolio-grade cyber intelligence platform designed to demonstrate how disparate security observations can be normalized, correlated, scored, investigated, and presented to analysts through a unified operational interface.

The platform uses **synthetic and authorized defensive data** for demonstrations. It is not designed for unauthorized surveillance, intrusion, exploitation, or targeting of real-world systems.

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
                     ┌──────────────────────────┐
                     │       SENTINEL-X         │
                     │   Intelligence Platform  │
                     └────────────┬─────────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
      │ Threat Intel│      │ AI Analysis │      │ Investigation│
      │    Layer    │      │    Layer    │      │     Layer    │
      └──────┬──────┘      └──────┬──────┘      └──────┬──────┘
             └────────────────────┼────────────────────┘
                                  ▼
                     ┌──────────────────────────┐
                     │ Correlation / Risk Engine│
                     └────────────┬─────────────┘
                                  ▼
                     ┌──────────────────────────┐
                     │ Analyst Command Interface │
                     └────────────┬─────────────┘
                                  ▼
                     ┌──────────────────────────┐
                     │ Cases • Alerts • Reports │
                     └──────────────────────────┘
```

## Repository Structure

```text
sentinel-x/
├── apps/
│   ├── web/                 # Analyst web application
│   └── api/                 # FastAPI service
├── services/
│   ├── correlation/         # Event/entity correlation engine
│   ├── intelligence/        # Threat intelligence processing
│   └── ai/                  # AI-assisted analysis services
├── data/
│   ├── synthetic/            # Safe demo datasets
│   └── schemas/              # Data contracts
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

## Development Principles

1. **Defensive by design**
2. **Synthetic data by default**
3. **Least privilege**
4. **Auditable actions**
5. **Explainable risk scoring**
6. **Secure secrets handling**
7. **Test before release**
8. **Clear separation between facts, correlations, and hypotheses**

## Planned Technology Stack

| Layer | Planned Technology |
|---|---|
| Frontend | React + TypeScript |
| UI | Tailwind CSS |
| API | Python + FastAPI |
| Database | PostgreSQL |
| Cache / Jobs | Redis |
| AI / Analytics | Python |
| Containers | Docker |
| CI/CD | GitHub Actions |
| Cloud | Oracle Cloud Infrastructure |
| Graph Analysis | Graph-based relationship model |

## Roadmap

### Phase 1
- [x] Repository initialized
- [ ] Architecture baseline
- [ ] Web application shell
- [ ] API service
- [ ] Database foundation
- [ ] Docker development environment

### Phase 2
- [ ] IOC registry
- [ ] Event normalization
- [ ] Correlation engine
- [ ] Risk scoring
- [ ] Incident management
- [ ] ATT&CK mapping

### Phase 3
- [ ] Investigation workspace
- [ ] Entity graph
- [ ] Timeline analysis
- [ ] Threat visualization
- [ ] Analyst workflow

### Phase 4
- [ ] AI assistant
- [ ] Report generation
- [ ] Confidence-aware analysis
- [ ] Advanced analytics

### Phase 5
- [ ] Security hardening
- [ ] CI/CD
- [ ] OCI deployment
- [ ] Production documentation
- [ ] Public demo release

## Safety Boundary

SENTINEL-X is intended for **authorized defensive research, education, and security operations simulation**. The project must not be used to gain unauthorized access to systems, conduct covert surveillance, evade security controls, or target individuals or organizations.

## Author

**Shubhra Pratim Mandal**  
Cybersecurity • AI • Cloud Computing • Computer Science
