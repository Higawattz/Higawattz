# Pipeline Governance Checklist

Use this checklist to review whether a CI/CD pipeline is ready for enterprise use.

## Required Controls

- [ ] Pipeline has an owner or responsible squad.
- [ ] Pipeline uses a reusable template or Shared Library.
- [ ] Logs include timestamps and build identifiers.
- [ ] Static checks are enabled where applicable.
- [ ] Unit tests are visible in the pipeline result.
- [ ] Security scan stage exists or has documented exception.
- [ ] Artifact versioning is deterministic.
- [ ] Deployment approval is required for controlled environments.
- [ ] Failure notifications are routed to the responsible team.
- [ ] Delivery metrics can support DORA analysis.

## Operational Metrics

| Metric | Why it matters |
|---|---|
| Lead Time | Shows how long work takes to reach production-like environments |
| Deployment Frequency | Shows delivery cadence |
| Change Failure Rate | Shows stability of changes |
| MTTR | Shows recovery capability |

## Review Cadence

- Monthly for critical production pipelines
- Quarterly for internal tools
- After major platform upgrades or audit findings
