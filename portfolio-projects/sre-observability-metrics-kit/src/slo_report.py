from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCIDENTS = ROOT / "sample_data" / "incidents.csv"


def read_incidents() -> list[dict[str, str]]:
    with INCIDENTS.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def duration(incident: dict[str, str]) -> int:
    return int(incident["end_minutes"]) - int(incident["start_minutes"])


def calculate_mtbf(incidents: list[dict[str, str]]) -> float:
    starts = sorted(int(item["start_minutes"]) for item in incidents)
    gaps = [starts[index] - starts[index - 1] for index in range(1, len(starts))]
    return sum(gaps) / len(gaps) if gaps else 0.0


def main() -> None:
    incidents = read_incidents()
    durations = [duration(item) for item in incidents]
    mttr = sum(durations) / len(durations)
    mtbf = calculate_mtbf(incidents)
    breaches = [item for item in incidents if duration(item) > int(item["sla_minutes"])]
    by_service = Counter(item["service"] for item in incidents)
    by_severity = Counter(item["severity"] for item in incidents)

    print("# SRE Reliability Report")
    print("\n## Executive Summary")
    print(f"- Incidents reviewed: {len(incidents)}")
    print(f"- MTTR: {mttr:.1f} minutes")
    print(f"- MTBF: {mtbf:.1f} minutes")
    print(f"- SLA breaches: {len(breaches)}")

    print("\n## Incidents by Service")
    for service, total in sorted(by_service.items()):
        print(f"- {service}: {total}")

    print("\n## Incidents by Severity")
    for severity, total in sorted(by_severity.items()):
        print(f"- {severity}: {total}")

    print("\n## Recommended Actions")
    print("- Prioritize services with recurring incidents before adding new dashboard panels.")
    print("- Review SLA breaches with service owners and create follow-up actions.")
    print("- Pair MTTR reduction with post-incident learning and automation opportunities.")
    print("- Use MTBF trends to identify platform reliability improvements.")


if __name__ == "__main__":
    main()
