# Data Governance, Privacy, and Licensing

**Status:** baseline policy proposal; it must be reviewed against the actual jurisdictions, sources, and intended processing before operational adoption.

## 1. Governance principles

Data must be fit for a declared purpose, traceable to its origin, access-controlled according to risk, and removable when required. Data quality and legal permission are separate gates: a technically clean dataset may still be prohibited for a given use.

## 2. Data classification

| Class | Examples | Default handling |
|---|---|---|
| Public and approved | Public-domain material or content with documented redistribution rights | May be released after provenance and quality review |
| Internal synthetic | Invented test users, products, and messages | Safe for routine development if it contains no real credentials or copied personal data |
| Licensed/restricted | Third-party text or commercial data with conditions | Keep access-limited; record terms and permitted uses |
| Personal/confidential | User conversations, account exports, identifiable records | Do not commit to this public repository; require a lawful basis, purpose, access controls, retention limits, and review |
| Secret/credential | API keys, tokens, passwords, private keys | Never place in datasets, manifests, logs, commits, or examples |

A public source is not automatically public-domain or freely redistributable.

## 3. Provenance and license review

For each source, record:
- Publisher/owner and canonical source reference.
- Acquisition date and collection method.
- License or written permission basis, including version/date of terms where relevant.
- Whether redistribution, modification, commercial use, and model training are allowed.
- Attribution/notice requirements.
- Source-specific restrictions and removal/contact instructions.
- Hash of the acquired source or released artifact where appropriate.

Do not bypass access controls, authentication, robots restrictions, contractual limits, or source rate limits. If rights are unclear, do not publish or train on the data until a qualified reviewer decides.

## 4. Personal and sensitive data

Prefer synthetic examples. If real personal data is proposed:
1. Document the purpose and necessity.
2. Identify the legal basis and required notices/consent with qualified review.
3. Minimize fields and retention.
4. Assess whether the data includes health, financial, identity, biometric, children’s, or other sensitive information.
5. Determine access, encryption, deletion, export, and incident-response controls.
6. Test re-identification risk where de-identification is claimed.
7. Prevent public Git history from becoming the storage channel.

Do not commit raw customer conversations, CVs, account exports, payment details, private support threads, or images of identifiable people without explicit approval and a suitable controlled storage design. In most cases, use synthetic/de-identified evaluation cases instead.

## 5. Intended-use tags

Each dataset must explicitly declare one or more of:
- `evaluation`
- `testing`
- `analytics`
- `retrieval`
- `training`
- `documentation`

The data owner must approve each intended use. In particular, an evaluation dataset must not silently be repurposed as model-training material. Training use needs a separate review of source rights, personal data, consent/opt-out commitments, retention, and downstream model implications.

## 6. Access and retention

- Restrict access to the minimum required people and systems.
- Publish only dataset versions approved for public release.
- Keep secrets out of version control; use a secrets manager for credentials.
- Define a retention period and deletion trigger for every restricted dataset.
- Document copies and downstream consumers so a withdrawal can be propagated.
- Avoid storing raw user prompts in analytics by default.
- Use access logs for controlled stores where risk warrants them.

## 7. Security and integrity

- Validate file types and sizes before processing.
- Treat input files and dataset rows as untrusted.
- Use checksums for released artifacts.
- Scan scripts and archives; never execute arbitrary data-derived code.
- Use least-privilege access to artifact storage.
- Review dependency and pipeline changes before release.
- If sensitive data is committed accidentally, restrict/remove access, rotate exposed credentials if applicable, and follow a documented incident process. A later file deletion does not erase prior Git history or existing clones.

## 8. Ownership and approval

Each dataset release requires:
- A named data owner (person/team, not a secret or token).
- A reviewer for provenance, licensing, and privacy.
- A technical reviewer for schema, quality, and reproducibility.
- A recorded approval decision and date.
- A withdrawal contact/process.

This document is a proposed operational baseline, not a legal certification or statement that any current dataset has completed review.
