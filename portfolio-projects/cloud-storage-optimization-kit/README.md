# Cloud Storage Optimization Kit

A portfolio project inspired by enterprise Docker storage optimization and cost governance initiatives.

## Business Context

Container image repositories can grow quickly in enterprise environments. Without retention rules, usage analysis and tiering strategy, storage costs increase and platform governance becomes harder.

This project uses fictional Docker image inventory data to estimate monthly cost by storage tier and identify optimization opportunities.

## What This Demonstrates

- Cloud cost optimization thinking
- Docker image lifecycle governance
- Hot / warm / cold / archive storage tiering
- Business-oriented infrastructure analysis
- Practical modeling with Python

## Repository Structure

```text
sample_data/docker_images.csv # Fictional Docker image inventory
src/storage_optimizer.py      # Cost and tiering estimator
```

## How to Run

```bash
python src/storage_optimizer.py
```

## Recruiter Validation

This project maps to my TechChallenge / 4DS experience, where Docker storage optimization generated million-level savings and supported infrastructure modernization.

## Next Improvements

- Add retention policy simulation
- Export optimization plan to CSV
- Add repository owner mapping
- Add risk scoring for images without recent pulls
- Add cloud-provider cost profile presets
