from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "sample_data" / "docker_images.csv"

COST_PER_GB = {
    "hot": 0.11,
    "warm": 0.06,
    "cold": 0.025,
    "archive": 0.008,
}


def read_images() -> list[dict[str, str]]:
    with IMAGES.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def recommended_tier(last_pull_days: int, pulls_last_30_days: int, environment: str) -> str:
    if environment == "production" and pulls_last_30_days >= 100:
        return "hot"
    if last_pull_days <= 60:
        return "warm"
    if last_pull_days <= 180:
        return "cold"
    return "archive"


def main() -> None:
    images = read_images()
    by_tier: dict[str, float] = defaultdict(float)
    current_hot_cost = 0.0
    optimized_cost = 0.0

    print("# Docker Storage Optimization Report")
    print("\n## Image Recommendations")

    for image in images:
        size = float(image["size_gb"])
        last_pull_days = int(image["last_pull_days"])
        pulls = int(image["pulls_last_30_days"])
        tier = recommended_tier(last_pull_days, pulls, image["environment"])
        monthly_cost = size * COST_PER_GB[tier]
        current_cost = size * COST_PER_GB["hot"]

        by_tier[tier] += size
        current_hot_cost += current_cost
        optimized_cost += monthly_cost

        print(
            f"- {image['image']} ({size:.1f} GB): recommend {tier.upper()} "
            f"storage, estimated monthly cost ${monthly_cost:.2f}"
        )

    savings = current_hot_cost - optimized_cost
    savings_percent = (savings / current_hot_cost) * 100 if current_hot_cost else 0

    print("\n## Tier Distribution")
    for tier in ["hot", "warm", "cold", "archive"]:
        print(f"- {tier}: {by_tier[tier]:.1f} GB")

    print("\n## Cost Summary")
    print(f"- Current all-hot estimate: ${current_hot_cost:.2f}/month")
    print(f"- Optimized tiered estimate: ${optimized_cost:.2f}/month")
    print(f"- Estimated savings: ${savings:.2f}/month ({savings_percent:.1f}%)")

    print("\n## Governance Recommendations")
    print("- Define retention policy by environment and repository owner.")
    print("- Archive images with no pulls after the approved retention window.")
    print("- Keep production high-traffic images in hot storage.")
    print("- Review exception lists with platform, security and application owners.")


if __name__ == "__main__":
    main()
