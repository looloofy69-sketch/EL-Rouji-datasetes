#!/usr/bin/env python3
"""Offline structural QA for the EL-Rouji research archive.

Checks source-register integrity, citation resolution, local Markdown links and
freshness metadata. It does not fetch external URLs or certify factual/legal claims.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

SOURCE_ROW = re.compile(r"^\|\s*(S\d+)\s*\|", re.MULTILINE)
CITATION = re.compile(
    r"\[(S\d+(?:\s*[–-]\s*S\d+)?(?:\s*,\s*S\d+(?:\s*[–-]\s*S\d+)?)*)\]"
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
DATE_FIELDS = {
    "research/README.md": (r"\*\*Snapshot:\*\*\s*(\d{1,2} \w+ \d{4})", "snapshot"),
    "research/RESEARCH_INDEX.md": (r"\*\*Last updated:\*\*\s*(\d{1,2} \w+ \d{4})", "index"),
    "research/12-RESEARCH-QUEUE.md": (r"\*\*Updated:\*\*\s*(\d{1,2} \w+ \d{4})", "queue"),
    "research/10-DECISION-INTELLIGENCE.md": (r"\*\*As of:\*\*\s*(\d{1,2} \w+ \d{4})", "decision register"),
}
MONTHS = {m: i for i, m in enumerate(
    ("January February March April May June July August September October November December").split(), 1
)}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    files_checked: int = 0
    citations_checked: int = 0
    links_checked: int = 0
    source_ids_checked: int = 0

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_archive_date(raw: str) -> date | None:
    parts = raw.split()
    if len(parts) != 3:
        return None
    try:
        return date(int(parts[2]), MONTHS[parts[1]], int(parts[0]))
    except (ValueError, KeyError):
        return None


def expand_citation(token: str, report: Report, label: str) -> set[str]:
    match = re.fullmatch(r"(S\d+)\s*[–-]\s*(S\d+)", token)
    if not match:
        return {token}
    left, right = match.groups()
    a, b = int(left[1:]), int(right[1:])
    if a > b:
        report.error(f"{label}: descending source range {token!r}.")
        return set()
    width = max(len(left) - 1, len(right) - 1)
    return {f"S{number:0{width}d}" for number in range(a, b + 1)}


def resolve_local_link(raw: str, source_file: Path, root: Path) -> Path | None:
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return None
    destination = raw.split(maxsplit=1)[0].strip("<>")
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    return (source_file.parent / path).resolve()


def validate_research(root: Path, as_of: date | None = None, stale_after_days: int = 14) -> Report:
    report = Report()
    root = root.resolve()
    research = root / "research"
    sources_path = research / "SOURCES.md"
    if not research.is_dir():
        report.error(f"Research directory does not exist: {research}")
        return report
    if not sources_path.is_file():
        report.error("research/SOURCES.md is missing.")
        return report

    source_text = sources_path.read_text(encoding="utf-8")
    source_ids = SOURCE_ROW.findall(source_text)
    report.source_ids_checked = len(source_ids)
    if not source_ids:
        report.error("No source-register rows were found.")
    if len(source_ids) != len(set(source_ids)):
        duplicates = sorted({sid for sid in source_ids if source_ids.count(sid) > 1})
        report.error(f"Duplicate source IDs: {', '.join(duplicates)}.")
    numeric = [int(sid[1:]) for sid in source_ids]
    if numeric != sorted(numeric):
        report.error("Source IDs are not in ascending numeric order.")
    if numeric and numeric != list(range(numeric[0], numeric[-1] + 1)):
        report.error("Source register contains a gap in its numeric ID sequence.")
    if "## Source-use notes" not in source_text:
        report.error("Source register is missing the 'Source-use notes' section.")

    registered = set(source_ids)
    markdown_files = sorted(research.rglob("*.md"))
    report.files_checked = len(markdown_files)
    cited: set[str] = set()

    for path in markdown_files:
        content = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()

        for match in CITATION.finditer(content):
            for raw_token in match.group(1).split(","):
                token = raw_token.strip()
                expanded = expand_citation(token, report, relative)
                for sid in expanded:
                    report.citations_checked += 1
                    cited.add(sid)
                    if sid not in registered:
                        report.error(f"{relative}: citation {sid} has no source-register entry.")

        for match in MARKDOWN_LINK.finditer(content):
            raw_target = match.group(1)
            parsed = urlsplit(raw_target.strip().split(maxsplit=1)[0].strip("<>"))
            if parsed.scheme or parsed.netloc or raw_target.strip().startswith("#"):
                continue
            target = resolve_local_link(raw_target, path, root)
            if target is None:
                continue
            report.links_checked += 1
            try:
                target.relative_to(root)
            except ValueError:
                report.error(f"{relative}: local link escapes repository root: {raw_target!r}.")
                continue
            if not target.exists():
                report.error(f"{relative}: broken local link {raw_target!r}.")

    for sid in sorted(registered - cited, key=lambda value: int(value[1:])):
        report.warn(f"{sid} is registered but not cited by a research Markdown file.")

    if as_of is not None:
        for rel, (pattern, label) in DATE_FIELDS.items():
            path = root / rel
            if not path.is_file():
                report.warn(f"Freshness metadata file missing: {rel}.")
                continue
            match = re.search(pattern, path.read_text(encoding="utf-8"))
            if not match:
                report.warn(f"Could not parse {label} date in {rel}.")
                continue
            parsed_date = parse_archive_date(match.group(1))
            if parsed_date is None:
                report.warn(f"Invalid {label} date {match.group(1)!r} in {rel}.")
                continue
            age = (as_of - parsed_date).days
            if age > stale_after_days:
                report.warn(f"{label} metadata is {age} days old ({parsed_date.isoformat()}).")

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    parser.add_argument("--stale-after-days", type=int, default=14)
    args = parser.parse_args()

    report = validate_research(args.root, args.as_of, args.stale_after_days)
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(
        f"Checked {report.files_checked} Markdown file(s), "
        f"{report.source_ids_checked} source ID(s), "
        f"{report.citations_checked} citation occurrence(s), "
        f"{report.links_checked} local link(s): "
        f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)."
    )
    print("External URL reachability, source truth and legal status are not tested.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
