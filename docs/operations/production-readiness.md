# Production Readiness

SENTINEL-X is a portfolio/research platform. Before production or organizational use, complete the following.

## Security

- [x] Security response policy
- [x] Secure response headers
- [x] Strict CORS configuration via environment
- [x] CodeQL workflow
- [x] Dependabot
- [ ] External penetration test
- [ ] Independent threat-model review
- [ ] Secrets management integration
- [ ] Centralized identity and RBAC
- [ ] Formal logging retention policy

## Reliability

- [x] Health endpoint
- [x] CI tests
- [x] Containerized development stack
- [ ] Multi-instance deployment
- [ ] Database backup/restore drill
- [ ] Disaster recovery test
- [ ] Load testing

## Release

- [x] Public demo workflow
- [x] API documentation
- [x] OCI deployment template
- [ ] Production OCI deployment
- [ ] Custom domain and TLS
- [ ] Signed release artifacts

Never present the research build as a deployed operational intelligence system until the unchecked controls have been completed and independently validated.
