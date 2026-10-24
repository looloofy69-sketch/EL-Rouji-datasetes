# Dataset Catalog and Status Model

This catalog starts as a planning inventory. An entry below defines a possible dataset family; it does not mean data has been collected or approved.

## Proposed catalog

| ID | Dataset family | Intended use | Required review | Initial status |
|---|---|---|---|---|
| `eval-core` | General assistant evaluation cases | Regression/evaluation | Expected criteria, safety checks, duplication and licensing review | Proposed |
| `eval-multilingual` | English/French/Arabic/Darija evaluation examples | Localization quality checks | Language variety, dialect labeling, consent/provenance, reviewer validation | Proposed |
| `eval-research` | Research questions with source-grounded evaluation criteria | Citation and evidence evaluation | Source availability, publication dates, allowed reuse, stale-source handling | Proposed |
| `eval-attachments` | Synthetic image and text-analysis fixtures | Attachment QA | File safety, no sensitive real-world material, format/size metadata | Proposed |
| `eval-tools` | Calculator, prompt-starter, and API-boundary fixtures | Regression/security tests | Expected outcomes and non-executable inputs | Proposed |
| `synthetic-commerce` | Fake products, carts, orders, and delivery cases | E-commerce development and QA | Must contain synthetic identities and payment references only | Proposed |
| `curated-knowledge` | Licensed/approved reference material | Retrieval or knowledge grounding | Rights, attribution, freshness, source authority, removal process | Proposed |

## Required metadata for every dataset

Every catalog entry must reference a manifest containing:
- Stable dataset ID and human-readable name.
- Version, status, owner, and intended use.
- Language and locale tags where applicable.
- Data sources and collection/transformation process.
- License/permission basis and attribution requirements.
- Personal/sensitive-data assessment.
- Schema version and record count.
- Quality checks and known limitations.
- Checksums, creation date, and review date.
- Retention, withdrawal, and deletion instructions.

See [manifest template](../templates/dataset-manifest.template.json).

## Status definitions

- **Proposed:** scope is a plan only; no usage permitted.
- **Collecting:** data acquisition is in progress under an approved plan.
- **Cleaning:** transformations and deduplication are underway.
- **Review:** data and rights checks are awaiting approval.
- **Approved:** approved for the exact declared purpose and environment.
- **Released:** a versioned artifact and its validation report are published.
- **Deprecated:** still identifiable but should not be selected for new uses.
- **Withdrawn:** must not be used; downstream consumers must remove or replace it as instructed.

Approval is purpose-specific. Permission to evaluate a system does not automatically confer permission to train a model or redistribute a dataset.

## Dataset release naming

Recommended release layout:

```text
datasets/
  <dataset-id>/
    <version>/
      manifest.json
      records.jsonl
      quality-report.json
      SHA256SUMS
```

Large, licensed, personal, or access-restricted datasets should not be committed directly to a public Git repository. Store approved data in a suitable controlled artifact store and keep only safe metadata, scripts, and checksums in Git.

## Promotion requirements

Do not promote a dataset to Released until:
1. The intended use and access level are approved.
2. Source provenance and rights have been documented.
3. Schema and validation checks pass.
4. Duplicates, malformed records, and sensitive-data risks have been reviewed.
5. A quality report and checksum file exist.
6. The release has an owner and a withdrawal procedure.
