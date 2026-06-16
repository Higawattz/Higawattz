# SRE Observability Metrics Kit

A portfolio project focused on incident analysis, reliability indicators and operational visibility for technology teams.

## Business Context

SRE is not only about dashboards. It is about making reliability measurable, actionable and visible to engineering and leadership teams.

This project uses fictional incident data to calculate operational metrics such as MTTR, MTBF, SLA exposure and service impact distribution.

## What This Demonstrates

- Reliability metrics thinking
- MTTR, MTBF and SLA analysis
- Incident prioritization
- Operational dashboard foundations
- Communication between technical teams and leadership

## Repository Structure

```text
sample_data/incidents.csv # Fictional incident records
src/slo_report.py         # Reliability report generator
```

## How to Run

```bash
python src/slo_report.py
```

## Recruiter Validation

This project maps to experience with SRE practices, DataDog dashboards, Grafana, Prometheus, Nimsoft, troubleshooting, incident management and executive visibility.

## Next Improvements

- Export metrics to JSON for dashboard ingestion
- Add SLO burn-rate calculations
- Add service ownership mapping
- Add Power BI-ready CSV outputs
