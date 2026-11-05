"""Tests for offline research-archive structural QA."""
from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.validate_research import validate_research


class ValidateResearchTests(unittest.TestCase):
    def make_archive(self, root: Path) -> None:
        research = root / "research"
        docs = root / "docs"
        research.mkdir(parents=True)
        docs.mkdir()
        (research / "SOURCES.md").write_text(
            "# Source Register\n\n| ID | Source |\n|---|---|\n"
            "| S01 | [Official source](https://example.test/source) |\n"
            "| S02 | [Second source](https://example.test/second) |\n"
            "\n## Source-use notes\n",
            encoding="utf-8",
        )
        (docs / "POLICY.md").write_text("# Policy\n", encoding="utf-8")
        (research / "README.md").write_text(
            "# Archive\n\n[Policy](../docs/POLICY.md)\n\nEvidence [S01–S02].\n",
            encoding="utf-8",
        )

    def test_valid_archive_and_relative_root_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            report = validate_research(root, date(2026, 11, 5))
            self.assertEqual(report.errors, [])
            self.assertEqual(report.source_ids_checked, 2)
            self.assertEqual(report.citations_checked, 2)
            self.assertEqual(report.links_checked, 1)

    def test_unregistered_citation_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            p = root / "research" / "README.md"
            p.write_text(p.read_text(encoding="utf-8") + "\nMissing [S03].\n", encoding="utf-8")
            report = validate_research(root)
            self.assertTrue(any("no source-register entry" in e for e in report.errors))

    def test_duplicate_source_ids_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            p = root / "research" / "SOURCES.md"
            p.write_text(p.read_text(encoding="utf-8") + "| S02 | duplicate |\n", encoding="utf-8")
            report = validate_research(root)
            self.assertTrue(any("Duplicate source IDs" in e for e in report.errors))

    def test_broken_local_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            p = root / "research" / "README.md"
            p.write_text(p.read_text(encoding="utf-8") + "\n[Broken](missing.md)\n", encoding="utf-8")
            report = validate_research(root)
            self.assertTrue(any("broken local link" in e for e in report.errors))

    def test_external_links_are_not_fetched(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            report = validate_research(root)
            self.assertEqual(report.errors, [])
            self.assertEqual(report.links_checked, 1)


if __name__ == "__main__":
    unittest.main()
