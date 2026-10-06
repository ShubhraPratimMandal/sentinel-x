# OCI Deployment Blueprint

SENTINEL-X is designed to be deployable on Oracle Cloud Infrastructure.

Suggested topology: Internet -> OCI Load Balancer -> Containerized Web/API -> Private application network -> PostgreSQL + Redis.

Recommended controls:
- Private database subnet.
- Restricted network security groups.
- OCI Vault for secrets.
- TLS at the load balancer.
- Centralized logging and monitoring.
- Least-privilege IAM.
- PostgreSQL backups.
- Separation of synthetic demo data from authorized operational data.

Deployment sequence:
1. Build and scan images.
2. Push images to OCI Container Registry.
3. Provision network and private services.
4. Configure OCI Vault secrets.
5. Deploy web and API services.
6. Run database migrations.
7. Configure health checks.
8. Verify health and system-status endpoints.
9. Enable monitoring and backups.

This is an architecture blueprint, not a claim that the public repository is currently deployed to OCI.
