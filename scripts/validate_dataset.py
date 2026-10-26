#!/usr/bin/env python3
"""Validate an EL-Rouji dataset manifest and its JSONL release files.

Standard-library only. Checks structure and integrity; human review is still required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

STATUSES = {"proposed", "collecting", "cleaning", "review", "approved", "released", "deprecated", "withdrawn"}
LANGUAGE_TAG = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
SHA256 = re.compile(r"^[a-fA-F0-9]{64}$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED_RECORD_FIELDS = ("id", "schemaVersion", "datasetId", "taskType", "language", "input")
REQUIRED_METADATA_FIELDS = ("sourceType", "licenseRef", "reviewStatus")


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.records_checked = 0
        self.files_checked = 0

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_date(value: Any, field: str, report: Validation, required: bool = False) -> None:
    if value is None and not required:
        return
    if not isinstance(value, str) or not ISO_DATE.fullmatch(value):
        report.error(f"{field} must be an ISO date (YYYY-MM-DD).")
        return
    try:
        date.fromisoformat(value)
    except ValueError:
        report.error(f"{field} must be a valid ISO date (YYYY-MM-DD).")


def read_json(path: Path, report: Validation) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except OSError as exc:
        report.error(f"Cannot read {path}: {exc}")
    except json.JSONDecodeError as exc:
        report.error(f"Invalid JSON in {path} at line {exc.lineno}, column {exc.colno}.")
    return None


def resolve_data_path(manifest_dir: Path, raw_path: Any, report: Validation, label: str) -> Path | None:
    if not nonempty_string(raw_path):
        report.error(f"{label}.path must be a non-empty relative path.")
        return None
    candidate = Path(raw_path)
    if candidate.is_absolute():
        report.error(f"{label}.path must be relative to the manifest directory.")
        return None
    base = manifest_dir.resolve()
    resolved = (base / candidate).resolve()
    try:
        resolved.relative_to(base)
    except ValueError:
        report.error(f"{label}.path escapes the manifest directory: {raw_path!r}.")
        return None
    return resolved


def validate_record(record: Any, line_number: int, dataset_id: str, schema_version: str,
                    source_refs: set[str], seen_ids: set[str], released: bool, report: Validation) -> None:
    label = f"record line {line_number}"
    if not isinstance(record, dict):
        report.error(f"{label} must be a JSON object.")
        return

    for key in REQUIRED_RECORD_FIELDS:
        if key not in record:
            report.error(f"{label} is missing required field {key!r}.")
    for key in ("id", "schemaVersion", "datasetId", "taskType", "language"):
        if key in record and not nonempty_string(record[key]):
            report.error(f"{label}.{key} must be a non-empty string.")

    record_id = record.get("id")
    if nonempty_string(record_id):
        if record_id in seen_ids:
            report.error(f"{label} duplicates record id {record_id!r}.")
        seen_ids.add(record_id)

    if record.get("datasetId") != dataset_id:
        report.error(f"{label}.datasetId does not match the manifest datasetId.")
    if record.get("schemaVersion") != schema_version:
        report.error(f"{label}.schemaVersion does not match the manifest schemaVersion.")
    language = record.get("language")
    if nonempty_string(language) and not LANGUAGE_TAG.fullmatch(language):
        report.error(f"{label}.language is not a supported language-tag shape: {language!r}.")
    if "input" in record and not isinstance(record["input"], dict):
        report.error(f"{label}.input must be an object.")

    metadata = record.get("metadata")
    if not isinstance(metadata, dict):
        report.error(f"{label}.metadata must be an object.")
        return
    for key in REQUIRED_METADATA_FIELDS:
        if not nonempty_string(metadata.get(key)):
            report.error(f"{label}.metadata.{key} must be a non-empty string.")
    license_ref = metadata.get("licenseRef")
    if nonempty_string(license_ref) and license_ref not in source_refs:
        report.error(f"{label}.metadata.licenseRef does not resolve to a manifest source/license reference.")
    if released and metadata.get("reviewStatus") != "approved":
        report.error(f"{label}.metadata.reviewStatus must be 'approved' for a released dataset.")


def validate_manifest(manifest_path: Path) -> Validation:
    report = Validation()
    manifest = read_json(manifest_path, report)
    if not isinstance(manifest, dict):
        if not report.errors:
            report.error("The manifest root must be a JSON object.")
        return report

    for field in ("datasetId", "name", "version", "status", "owner", "description", "schemaVersion"):
        if not nonempty_string(manifest.get(field)):
            report.error(f"manifest.{field} must be a non-empty string.")

    status = manifest.get("status")
    if nonempty_string(status) and status not in STATUSES:
        report.error(f"manifest.status must be one of: {', '.join(sorted(STATUSES))}.")
    parse_date(manifest.get("createdAt"), "manifest.createdAt", report, required=True)
    if manifest.get("reviewedAt") is not None:
        parse_date(manifest.get("reviewedAt"), "manifest.reviewedAt", report)

    intended_use = manifest.get("intendedUse")
    if not isinstance(intended_use, list) or not intended_use or any(not nonempty_string(v) for v in intended_use):
        report.error("manifest.intendedUse must be a non-empty array of strings.")

    sources = manifest.get("sources")
    source_refs: set[str] = set()
    source_ids: set[str] = set()
    if not isinstance(sources, list) or not sources:
        report.error("manifest.sources must contain at least one documented source/license entry.")
        sources = []
    for index, source in enumerate(sources):
        label = f"manifest.sources[{index}]"
        if not isinstance(source, dict):
            report.error(f"{label} must be an object.")
            continue
        source_id = source.get("sourceId")
        if not nonempty_string(source_id):
            report.error(f"{label}.sourceId must be a non-empty string.")
        elif source_id in source_ids:
            report.error(f"{label}.sourceId {source_id!r} is duplicated.")
        else:
            source_ids.add(source_id)
            source_refs.add(source_id)
        for key in ("publisher", "reference", "licenseName", "licenseReference"):
            if not nonempty_string(source.get(key)):
                report.error(f"{label}.{key} must be a non-empty string.")
        for key in ("licenseName", "licenseReference"):
            if nonempty_string(source.get(key)):
                source_refs.add(source[key])

    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        report.error("manifest.files must list at least one release artifact.")
        files = []

    jsonl_files = 0
    seen_record_ids: set[str] = set()
    dataset_id = manifest.get("datasetId") if isinstance(manifest.get("datasetId"), str) else ""
    schema_version = manifest.get("schemaVersion") if isinstance(manifest.get("schemaVersion"), str) else ""
    released = status == "released"

    for index, item in enumerate(files):
        label = f"manifest.files[{index}]"
        if not isinstance(item, dict):
            report.error(f"{label} must be an object.")
            continue
        file_path = resolve_data_path(manifest_path.parent, item.get("path"), report, label)
        if file_path is None:
            continue
        if not file_path.is_file():
            report.error(f"{label} references a missing file: {item.get('path')!r}.")
            continue

        raw = file_path.read_bytes()
        report.files_checked += 1
        declared_hash = item.get("sha256")
        if not isinstance(declared_hash, str) or not SHA256.fullmatch(declared_hash):
            report.error(f"{label}.sha256 must be a 64-character SHA-256 hex digest.")
        elif hashlib.sha256(raw).hexdigest().lower() != declared_hash.lower():
            report.error(f"{label}.sha256 does not match the current artifact bytes.")

        fmt = item.get("format")
        if fmt != "jsonl":
            report.error(f"{label}.format {fmt!r} is not supported; use 'jsonl'.")
            continue
        jsonl_files += 1
        declared_count = item.get("recordCount")
        if isinstance(declared_count, bool) or not isinstance(declared_count, int) or declared_count < 0:
            report.error(f"{label}.recordCount must be a non-negative integer.")

        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            report.error(f"{label} must be UTF-8 encoded.")
            continue

        count = 0
        for line_number, line in enumerate(content.splitlines(), start=1):
            if not line.strip():
                report.error(f"{item.get('path')}:{line_number} is blank; JSONL must contain one object per line.")
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                report.error(f"{item.get('path')}:{line_number} is invalid JSON (column {exc.colno}).")
                continue
            count += 1
            validate_record(record, line_number, dataset_id, schema_version, source_refs, seen_record_ids, released, report)
        report.records_checked += count
        if isinstance(declared_count, int) and not isinstance(declared_count, bool) and declared_count != count:
            report.error(f"{label}.recordCount declares {declared_count}, but {count} records were found.")

    if files and jsonl_files == 0:
        report.error("No JSONL release file was validated.")

    if released:
        if not isinstance(manifest.get("reviewedAt"), str):
            report.error("Released datasets require manifest.reviewedAt.")
        privacy = manifest.get("privacyAssessment")
        if not isinstance(privacy, dict):
            report.error("Released datasets require a privacyAssessment object.")
        else:
            if privacy.get("approvedForRelease") is not True:
                report.error("Released datasets require privacyAssessment.approvedForRelease=true.")
            if privacy.get("containsPersonalData") not in (False, "no", "false"):
                report.error("Released datasets must have a reviewed 'no personal data' determination.")
            if privacy.get("sensitiveDataReview") not in ("complete", "approved", "passed"):
                report.error("Released datasets require a completed sensitive-data review.")
    elif status in ("proposed", "collecting", "cleaning", "review"):
        report.warn(f"Dataset status is {status!r}; validation does not approve it for production use.")

    if not report.errors:
        report.warn("Structural validation passed; licensing, consent, privacy, and semantic quality still require human review.")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True, help="Path to manifest.json")
    args = parser.parse_args()
    report = validate_manifest(args.manifest.resolve())
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for issue in report.errors:
        print(f"ERROR: {issue}")
    print(f"Checked {report.files_checked} file(s) and {report.records_checked} record(s); "
          f"{len(report.errors)} error(s), {len(report.warnings)} warning(s).")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
