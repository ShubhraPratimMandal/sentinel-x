# Oracle Cloud Infrastructure Deployment

This directory contains a **deployment template**, not an already-provisioned cloud environment.

## Target architecture

OCI Load Balancer
→ private application subnet
→ SENTINEL-X API/Web containers
→ private PostgreSQL and Redis services

## Required inputs

- OCI tenancy / user authentication
- compartment OCID
- region
- availability domain
- container registry namespace
- DNS/TLS configuration

## Deployment controls

1. Keep PostgreSQL and Redis private.
2. Expose only HTTPS through the load balancer.
3. Store credentials in OCI Vault.
4. Use least-privilege dynamic groups and IAM policies.
5. Enable OCI Logging and Monitoring.
6. Configure backups before loading any authorized data.
7. Use synthetic data for the public demonstration environment.

## Important

Running Terraform against an OCI tenancy creates billable cloud resources. Review the plan before applying it. The public repository does not contain cloud credentials.
