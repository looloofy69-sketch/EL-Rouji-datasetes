# Dataset Release Validator

**Status:** validation utility implemented; no production dataset is included or approved by this tool.

## Purpose

scripts/validate_dataset.py is a dependency-free Python command-line utility that checks a dataset manifest and its JSON Lines (JSONL) release artifacts. It verifies required structure, file containment, SHA-256 digests, declared record counts, required record fields, unique record IDs, dataset/schema consistency, and source/license references.

It is a release-integrity gate, not a privacy classifier or legal review. A successful run does not prove that content is licensed, consented, factually sound, free of personal data, or safe for model training.

## Run locally

Requirements: Python 3.10 or later; no third-party packages.

    python -m unittest discover -s tests -v
    python scripts/validate_dataset.py --manifest path/to/manifest.json

The command returns exit code 0 when structural validation passes and 1 when validation errors are found. Warnings do not fail the command by themselves. A manifest with status "released" additionally requires a review date, completed sensitive-data review, explicit privacy approval, a reviewed determination that the release contains no personal data, and metadata.reviewStatus "approved" for every record.

Artifact paths are resolved relative to the manifest directory. Absolute paths and paths escaping that directory are rejected. Each artifact must declare a correct SHA-256 digest. JSONL files must be UTF-8, contain one JSON object per non-blank line, and match the declared recordCount.

## Continuous integration

GitHub Actions runs the standard-library unit tests on pushes and pull requests. The tests use temporary synthetic fixtures; they do not add a released dataset to this repository.

## Deliberate limitations

- Only JSONL release files are supported; other artifact formats are rejected explicitly.
- The validator does not automatically discover personal data, infer consent, verify external URLs, interpret license terms, compare train/dev/test splits across files, or assess semantic quality.
- Human review remains mandatory before a dataset is approved, released, or used for training.
- A valid manifest is not a substitute for a data card, quality report, source records, or release-owner approval.
