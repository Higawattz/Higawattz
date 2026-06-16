from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUES = ROOT / "sample_data" / "jira_issues.csv"
PLUGINS = ROOT / "sample_data" / "plugins.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def as_bool(value: str) -> bool:
    return value.strip().lower() == "true"


def issue_summary(issues: list[dict[str, str]]) -> list[str]:
    by_platform = Counter(issue["platform"] for issue in issues)
    breached = [issue for issue in issues if as_bool(issue["sla_breached"])]
    critical = [issue for issue in issues if issue["priority"] == "critical"]
    avg_resolution = sum(float(issue["resolution_hours"]) for issue in issues) / len(issues)

    return [
        f"Total records reviewed: {len(issues)}",
        f"SLA breaches: {len(breached)}",
        f"Critical records: {len(critical)}",
        f"Average resolution time: {avg_resolution:.1f} hours",
        "Platform distribution: " + ", ".join(f"{k}={v}" for k, v in sorted(by_platform.items())),
    ]


def plugin_findings(plugins: list[dict[str, str]]) -> list[str]:
    findings: list[str] = []
    for plugin in plugins:
        days = int(plugin["last_review_days"])
        expired = plugin["license_status"] == "expired"
        critical = as_bool(plugin["business_critical"])

        if expired:
            findings.append(f"HIGH: {plugin['plugin']} has expired license status.")
        elif critical and days > 90:
            findings.append(f"MEDIUM: {plugin['plugin']} is business critical and needs review ({days} days).")
        elif days > 180:
            findings.append(f"MEDIUM: {plugin['plugin']} has not been reviewed in {days} days.")

    return findings or ["No plugin governance exceptions found."]


def recommendations() -> list[str]:
    return [
        "Review expired and high-risk plugins before the next audit cycle.",
        "Track SLA breaches by platform and owner to prioritize reliability work.",
        "Maintain an owner and review date for every critical plugin.",
        "Publish monthly governance indicators for leadership visibility.",
    ]


def main() -> None:
    issues = read_csv(ISSUES)
    plugins = read_csv(PLUGINS)

    print("# Atlassian Governance Report")
    print("\n## Operational Summary")
    for line in issue_summary(issues):
        print(f"- {line}")

    print("\n## Plugin Governance Findings")
    for finding in plugin_findings(plugins):
        print(f"- {finding}")

    print("\n## Recommendations")
    for item in recommendations():
        print(f"- {item}")


if __name__ == "__main__":
    main()
