# Dataset Pipelines and Quality Assurance

**Status:** pipeline requirements only; executable ETL/validation jobs have not yet been added.

## 1. Target pipeline

```text
Approved source list
       |
       v
Acquire -> Raw quarantine -> Parse/normalize -> Deduplicate
                                      |
                                      v
                              Privacy/license review
                                      |
                                      v
                             Schema and quality checks
                                      |
                                      v
                             Human review / approval
                                      |
                                      v
                       Versioned release + checksums/report
```

Raw material should be immutable during processing and stored according to its sensitivity and license. Do not use this public repository for confidential raw data.

## 2. Reproducibility

For any data transformation, record:
- Source snapshot/reference and acquisition time.
- Script/tool version and configuration.
- Required dependency versions.
- Deterministic ordering and random seed if sampling is used.
- Input/output checksums and record counts.
- Rejected-record count with safe, non-sensitive reason codes.
- Manual edits and reviewer identity/date.
- Dataset/schema version produced.

A pipeline should be repeatable from an approved source snapshot. If a source changes over time, capture a new snapshot/version rather than overwriting a prior released artifact.

## 3. Quality dimensions

| Dimension | Minimum check |
|---|---|
| Completeness | Required fields present; missing-value rates reported |
| Validity | Types, enums, language tags, URLs and lengths conform to schema |
| Uniqueness | Duplicate IDs and duplicate/near-duplicate examples reported |
| Consistency | Cross-field values and manifest metadata agree |
| Accuracy | Samples are reviewed against source or domain criteria |
| Balance/coverage | Relevant languages, dialects, task types, and difficulty levels are represented as intended |
| Safety/privacy | Secrets, sensitive data, and prohibited material are absent or quarantined |
| Provenance | Every row can be tied to an approved source/process |
| Freshness | Time-sensitive sources have dates and a refresh policy |
| Leakage | Evaluation sets do not unintentionally share duplicates with training/development sets |

Do not optimize for a single aggregate quality score that hides failures in privacy, source rights, or critical subsets.

## 4. Splits and evaluation integrity

When train/dev/test splits are relevant:
- Split by source, user/author, conversation, or related group where needed to avoid near-duplicate leakage.
- Keep evaluation sets read-only after release.
- Document sampling methodology and known representativeness limits.
- Keep gold labels/rubrics access-limited where necessary to prevent accidental tuning against the test.
- Report per-language and per-task results instead of only an overall average.
- Do not make model-performance claims without a versioned dataset, scoring method, and recorded run.

For datasets used only in manual product QA, splits may not be relevant; document why.

## 5. Release checks

A release should fail if:
- Required manifest values are missing.
- Rights/status are not approved for the intended use.
- Schema validation fails.
- Duplicate IDs exist.
- Required checksums are missing or incorrect.
- A secrets/privacy scan finds unresolved sensitive content.
- The record count does not match the manifest.
- The quality report or owner approval is absent.

Some checks should be blocking (rights, privacy, schema, secret scanning); others can produce warnings that require reviewer disposition. Define thresholds by dataset type rather than guessing universal values.

## 6. Reports

Each release should include a machine-readable quality report with:
- Validator and schema versions.
- Record counts before/after transformation.
- Valid, rejected, and duplicate counts.
- Missingness by field.
- Language/task distribution.
- Known limitations and sampling caveats.
- Review status and approval record.
- Artifact checksums.

Avoid including raw sensitive examples in reports or CI logs.
