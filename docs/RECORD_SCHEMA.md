# Record Schema and Manifest Contract

This document defines a minimal proposed record shape for EL-Rouji dataset artifacts. It is a contract proposal, not a claim that the repository currently contains validated datasets.

## 1. Recommended JSONL structure

Use UTF-8 JSON Lines (`records.jsonl`) for one-record-per-line corpora and evaluation sets. Keep binary files outside JSONL and reference them by safe, versioned artifact identifiers or approved URIs.

Example synthetic evaluation record:

```json
{
  "id": "eval-core-000001",
  "schemaVersion": "1.0",
  "datasetId": "eval-core",
  "taskType": "assistant_response",
  "language": "en",
  "locale": "en-DZ",
  "input": {
    "messages": [
      { "role": "user", "content": "Explain a simple percentage calculation." }
    ]
  },
  "expected": {
    "criteria": [
      "Explains the method clearly",
      "Uses a mathematically correct example"
    ],
    "mustNot": [
      "Invent a source"
    ]
  },
  "metadata": {
    "split": "test",
    "sourceType": "synthetic",
    "licenseRef": "INTERNAL-SYNTHETIC",
    "reviewStatus": "pending"
  }
}
```

The values above are invented placeholders for schema illustration, not test results or a released dataset. Do not put hidden chain-of-thought, personal records, secrets, or unlicensed source text into expected fields.

## 2. Required fields

| Field | Type | Rule |
|---|---|---|
| `id` | string | Stable, unique within the dataset version |
| `schemaVersion` | string | Must match the declared schema contract |
| `datasetId` | string | Must match the manifest |
| `taskType` | string | Allow-listed purpose, e.g. assistant_response, research_citation, attachment_validation |
| `language` | string | Valid language tag or documented project code |
| `input` | object | Minimal input needed for the declared test/use |
| `metadata.sourceType` | string | E.g. synthetic, licensed, public-domain, user-consented |
| `metadata.licenseRef` | string | Reference to the manifest's source/license record |
| `metadata.reviewStatus` | string | Must not be treated as approved unless explicitly approved |

The `expected` object is task-specific. For open-ended tasks, use clear evaluation criteria/rubrics instead of presenting one wording as the only correct answer.

## 3. Language and locale

- Use BCP 47 language tags where practical: `en`, `fr`, `ar`.
- Use a documented locale tag when dialect/region matters, e.g. `ar-DZ` for Algerian Arabic.
- Distinguish language, script, and dialect; Arabic script alone does not establish a specific dialect.
- Mark mixed-language inputs explicitly where useful.
- Do not claim native-speaker validation unless an appropriately qualified reviewer completed it.

## 4. Manifest

Every released dataset must have a `manifest.json` based on [the template](../templates/dataset-manifest.template.json). At minimum, it must record dataset ID, version, status, owner, intended use, schema version, source/license references, record counts, quality report, creation/review timestamps, and checksums.

## 5. Validation requirements

A release validator should check:
1. Every line parses as exactly one JSON object.
2. Required keys are present and have the expected types.
3. IDs are unique and stable.
4. The record's dataset ID and schema version match the manifest.
5. Language tags and enumerated task types are valid.
6. Metadata refers to a declared source/license record.
7. The record has no disallowed secrets, personal data, or unapproved sensitive material.
8. Train/dev/test splits do not leak duplicates across splits.
9. Data is sorted/deterministic where the pipeline expects reproducible output.
10. Counts and SHA-256 checksums match the manifest/release files.

## 6. Schema evolution

- Patch changes may clarify descriptions without changing validated semantics.
- Minor versions may add optional fields while preserving existing consumers.
- Major versions may rename/remove fields or change meaning and require migration.
- Every released version is immutable; publish a new version rather than silently editing a released artifact.
- Consumers must reject unsupported major schema versions explicitly.
