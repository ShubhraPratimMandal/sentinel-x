# SENTINEL-X Threat Model

## Assets

- User accounts and roles
- Investigation cases
- Intelligence records
- Audit logs
- Configuration and secrets
- AI prompts and outputs

## Threat Categories

| Threat | Example | Primary Control |
|---|---|---|
| Credential theft | Compromised analyst account | Strong authentication and short-lived sessions |
| Privilege abuse | Analyst accesses restricted cases | RBAC and authorization checks |
| Injection | Malicious input reaches a query layer | Parameterized queries and validation |
| Data poisoning | False intelligence enters the platform | Provenance, validation, confidence |
| Secret exposure | API key committed to Git | Environment variables and secret scanning |
| Model misuse | Unsupported AI conclusions | Source grounding and confidence labels |

## Security Principle

The AI layer is advisory. It must not silently invent evidence or perform autonomous actions against external systems.
