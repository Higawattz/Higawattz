# Atlassian Governance Audit Kit

A recruiter-friendly portfolio project that demonstrates how Atlassian platform administration can be translated into governance, audit readiness and executive visibility.

## Business Context

Large organizations often run Jira, Confluence and Bitbucket as critical engineering platforms. Over time, plugins, projects, permissions, workflows and service requests can become difficult to govern without a repeatable review process.

This project shows a simplified, non-confidential approach to analyzing Atlassian-related operational data and producing a governance report.

## What This Demonstrates

- Jira / Confluence / Bitbucket administration mindset
- Plugin and add-on governance
- Audit evidence preparation
- KPI extraction for leadership reporting
- Risk-oriented thinking for DevTools platforms
- Clear documentation for technical and non-technical reviewers

## Repository Structure

```text
sample_data/
  jira_issues.csv      # Fictional operational requests and incidents
  plugins.csv          # Fictional plugin inventory
src/
  governance_report.py # Python script that generates governance findings
```

## How to Run

```bash
python src/governance_report.py
```

The script reads fictional sample data and prints a governance summary with incident distribution, SLA exposure, plugin risk and review recommendations.

## Recruiter Validation

This project maps directly to experience with:

- Atlassian Stack: Jira, Confluence, Bitbucket, JSM
- ServiceNow-style incident/request governance
- Internal audit support and evidence collection
- Plugin homologation and platform lifecycle management
- Executive indicators and operational dashboards

## Next Improvements

- Export report to Markdown or CSV
- Add severity scoring rules
- Add plugin lifecycle review dates
- Add Confluence page ownership checks
- Add Bitbucket repository governance checks
