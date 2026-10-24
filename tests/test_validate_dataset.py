"""Tests for the dependency-free EL-Rouji dataset validator."""
from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_dataset import validate_manifest


def make_manifest(root: Path, released: bool = False) -> Path:
    record = {
        "id": "eval-001",
        "schemaVersion": "1.0",
        "datasetId": "eval-demo",
        "taskType": "assistant_response",
        "language": "ar-DZ",
        "input": {"messages": [{"role": "user", "content": "Synthetic test input"}]},
        "expected": {"criteria": ["Answer is relevant"], "mustNot": []},
        "metadata": {
            "split": "test",
            "sourceType": "synthetic",
            "licenseRef": "synthetic-source",
            "reviewStatus": "approved" if released else "pending",
        },
    }
    raw = (json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    (root / "records.jsonl").write_bytes(raw)
    doc = {
        "datasetId": "eval-demo",
        "name": "Synthetic validator fixture",
        "version": "0.1.0",
        "status": "released" if released else "review",
        "owner": "test-suite",
        "description": "Non-production synthetic fixture.",
        "intendedUse": ["evaluation"],
        "schemaVersion": "1.0",
        "languages": ["ar-DZ"],
        "createdAt": "2026-10-24",
        "reviewedAt": "2026-10-24" if released else None,
        "sources": [{
            "sourceId": "synthetic-source",
            "publisher": "EL-Rouji test fixture",
            "reference": "internal-test-fixture",
            "acquiredAt": "2026-10-24",
            "licenseName": "INTERNAL-SYNTHETIC",
            "licenseReference": "internal-synthetic",
            "redistributionAllowed": False,
            "trainingAllowed": False,
            "attributionRequired": False,
            "notes": "Synthetic test only.",
        }],
        "files": [{
            "path": "records.jsonl",
            "format": "jsonl",
            "recordCount": 1,
            "sha256": hashlib.sha256(raw).hexdigest(),
        }],
        "qualityReport": "quality-report.json",
        "privacyAssessment": {
            "containsPersonalData": False if released else "unknown",
            "sensitiveDataReview": "complete" if released else "pending",
            "approvedForRelease": released,
        },
        "knownLimitations": ["Synthetic fixture; not a real evaluation set."],
        "withdrawalProcedure": "Remove this test fixture.",
    }
    path = root / "manifest.json"
    path.write_text(json.dumps(doc, indent=2), encoding="utf-8")
    return path


class ValidateDatasetTests(unittest.TestCase):
    def test_review_manifest_passes_with_warning(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            report = validate_manifest(make_manifest(Path(temp)))
            self.assertEqual(report.errors, [])
            self.assertTrue(any("not production use" in warning for warning in report.warnings))
            self.assertEqual(report.records_checked, 1)

    def test_valid_released_manifest_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            report = validate_manifest(make_manifest(Path(temp), released=True))
            self.assertEqual(report.errors, [])

    def test_checksum_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest = make_manifest(Path(temp))
            (Path(temp) / "records.jsonl").write_text("{}\n", encoding="utf-8")
            report = validate_manifest(manifest)
            self.assertTrue(any("sha256 does not match" in error for error in report.errors))

    def test_duplicate_ids_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = make_manifest(root)
            raw = (root / "records.jsonl").read_text(encoding="utf-8")
            duplicated = raw + raw
            (root / "records.jsonl").write_text(duplicated, encoding="utf-8")
            doc = json.loads(manifest.read_text(encoding="utf-8"))
            doc["files"][0]["recordCount"] = 2
            doc["files"][0]["sha256"] = hashlib.sha256(duplicated.encode()).hexdigest()
            manifest.write_text(json.dumps(doc), encoding="utf-8")
            report = validate_manifest(manifest)
            self.assertTrue(any("duplicates record id" in error for error in report.errors))

    def test_release_without_privacy_approval_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest = make_manifest(Path(temp), released=True)
            doc = json.loads(manifest.read_text(encoding="utf-8"))
            doc["privacyAssessment"]["approvedForRelease"] = False
            manifest.write_text(json.dumps(doc), encoding="utf-8")
            report = validate_manifest(manifest)
            self.assertTrue(any("approvedForRelease=true" in error for error in report.errors))

    def test_path_traversal_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            manifest = make_manifest(Path(temp))
            doc = json.loads(manifest.read_text(encoding="utf-8"))
            doc["files"][0]["path"] = "../outside.jsonl"
            manifest.write_text(json.dumps(doc), encoding="utf-8")
            report = validate_manifest(manifest)
            self.assertTrue(any("escapes the manifest directory" in error for error in report.errors))


if __name__ == "__main__":
    unittest.main()
