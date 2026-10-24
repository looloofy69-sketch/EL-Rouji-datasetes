# Contributing Datasets

This repository is a controlled data workspace. A contribution is not approved merely because it passes a parser.

## Before proposing data

1. Identify the dataset ID, purpose, consumers, and allowed use.
2. Document source, owner, acquisition method, license/permission, and attribution.
3. Classify sensitivity and assess privacy/re-identification risk.
4. Prefer synthetic examples where real data is not essential.
5. Check for secrets, personal data, copyrighted/source-restricted material, and duplicate leakage.
6. Add or update the manifest and schema documentation.
7. Provide reproducible validation steps and a quality report.

## What must not be submitted

- API keys, passwords, session tokens, private keys, or credentials.
- Raw customer or user conversation exports.
- Real payment card data, bank-account details, or identity documents.
- Private files or images containing identifiable people without explicit approval and a controlled handling plan.
- Scraped or licensed data whose rights do not permit the intended storage/use.
- Malware, executable payloads, or arbitrary scripts disguised as data.
- Unreviewed data labeled "anonymous" solely because names were removed.

## Pull-request checklist

- [ ] Dataset purpose and intended use are declared.
- [ ] Source provenance and license terms are documented.
- [ ] Manifest is complete and accurately identifies the version/status.
- [ ] Schema validation passes and IDs are unique.
- [ ] Privacy/secret scan is clean or findings are resolved.
- [ ] Deduplication and split-leakage checks are documented where relevant.
- [ ] Quality report and checksums are present.
- [ ] Dataset owner and appropriate reviewer approve the release.
- [ ] Changelog and catalog are updated.
- [ ] Removal/withdrawal instructions are documented where required.

## Release immutability

Do not silently alter a released artifact. Publish a new version with a change record and compatibility notes. If a release must be withdrawn, update its status and document downstream removal/replacement actions. Removing a file from the latest commit does not erase it from prior Git history.
