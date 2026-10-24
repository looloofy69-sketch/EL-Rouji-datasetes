# EL-Rouji Datasets

**Status:** governance and dataset contracts initialized; no production dataset is included yet.  
**Baseline:** 24 October 2026  
**Related application:** [EL-Rouji](https://github.com/looloofy69-sketch/EL-Rouji)

## Purpose

This repository is the controlled home for datasets used to evaluate, improve, and document EL-Rouji. It is intended to separate reusable data assets from application source code and future job-processing code.

At this baseline, this repository contains documentation and templates only. It does **not** claim that any dataset has been collected, cleaned, licensed, approved, or used to train a model.

## Initial scope

Priority dataset families proposed for review:

1. **Evaluation prompts and expected criteria** — repeatable tests of answer quality, safety, instruction following, and citations.
2. **Language and localization examples** — Arabic, Algerian Darija, French, English, and mixed-script examples, with source and consent controls appropriate to each item.
3. **Tool/workflow fixtures** — synthetic requests and expected behavior for chat modes, file analysis, research outputs, and future job APIs.
4. **Synthetic test data** — non-personal examples for regression, validation, and boundary testing.
5. **Curated knowledge collections** — only when each source's license, provenance, update policy, and redistribution rights are recorded.

These are proposed categories, not a claim that the corresponding datasets already exist.

## Repository map

- [Dataset catalog](docs/DATASET_CATALOG.md)
- [Data governance and privacy](docs/DATA_GOVERNANCE.md)
- [Record schema and manifest contract](docs/RECORD_SCHEMA.md)
- [Pipelines and quality gates](docs/PIPELINES_AND_QA.md)
- [Contribution rules](docs/CONTRIBUTING.md)
- [Dataset manifest template](templates/dataset-manifest.template.json)
- [Record template](templates/record.template.json)

## Non-negotiable rules

- Record origin, owner, license, collection method, language, and version for every dataset.
- Do not commit passwords, API keys, private conversations, personal records, or unreviewed user uploads.
- Do not ingest scraped or third-party content until its terms and redistribution rights have been reviewed.
- Keep raw source data separate from transformed releases and test fixtures.
- Prefer synthetic or properly de-identified data for tests.
- Do not claim data is anonymous merely because obvious names were removed.
- Every published version must have a machine-readable manifest, quality report, and checksum.
- Document whether a dataset is for evaluation, retrieval, analytics, or model training. These uses are not interchangeable.

## Release maturity

A dataset may move through proposed, collecting, cleaning, review, approved, released, deprecated, and withdrawn states. Only approved/released versions should be consumed by production workflows, and only if their declared intended use permits it.

## Related repositories

- [EL-Rouji core app](https://github.com/looloofy69-sketch/EL-Rouji)
- [EL-Rouji-jobs](https://github.com/looloofy69-sketch/EL-Rouji-jobs)
- E-commerce project documentation: [E-commerce-EL-Rouji-](https://github.com/looloofy69-sketch/E-commerce-EL-Rouji-)

Questions about legal basis, consent, licenses, sensitive data, or model-training rights require human review before release.
