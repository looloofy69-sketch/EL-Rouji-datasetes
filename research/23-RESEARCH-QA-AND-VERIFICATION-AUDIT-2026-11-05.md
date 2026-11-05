# Research QA and Verification Audit — 5 November 2026

**Repository:** `looloofy69-sketch/EL-Rouji-datasetes`  
**Branch:** `main`  
**Purpose:** verify the integrity of the existing research archive, correct freshness overclaims and introduce repeatable structural checks.  
**Product decision:** none. This audit does not select or validate a product.

## 1. Executive result

The archive is structurally coherent, but its evidence freshness is not uniform. The main failure risk is not broken navigation or missing source IDs; it is treating an incomplete legal-source search as proof that a regulation does not exist.

| Area | Result | Evidence / limitation |
|---|---|---|
| Repository identity | Pass | Public repository, default branch `main`; last push recorded 2 Nov 2026. |
| Archive structure | Pass | 23 numbered research documents (00–22), plus README, index and source register. |
| Source IDs | Pass | S01–S164 were unique and sequential before this audit; S165–S166 added for the current Gazette check. |
| Citation resolution | Pass | All bracketed source references in research documents 00–22, README and index resolved to the source register. |
| Local Markdown links | Pass | No broken local Markdown targets found across the 25 research documents/navigation files checked; relative links into root `docs/` were resolved from their actual file location. |
| External URL reachability | Not verified | Offline structural checks do not fetch external links. A link in the register is not proof that it still works. |
| Claim-level traceability | Partial | Source IDs exist, but the archive does not yet assign stable claim IDs or maintain a machine-readable claim-to-source/counter-evidence graph. |
| Legal freshness — Law 23-12 | Blocked / partial | The official SGG latest-issues listing reports JO No. 76 (29 Oct 2026), but its separate calendar page retrieved here stops at No. 57. Later Gazette PDFs were not retrievable in this research environment. Article 107 and the general implementing decree are therefore not verified for JO Nos. 60–76. [S157–S159, S165–S166] |
| Repository licensing | Decision required | GitHub repository metadata has no declared license. Public visibility is not a reuse license. Third-party source rights remain separate. |

## 2. What was checked

### 2.1 Structural integrity

- Enumerated the research directory and confirmed the numbered sequence 00–22.
- Checked source-register IDs for uniqueness and ordering.
- Parsed citation ranges and individual source references across the research documents and navigation files.
- Checked relative Markdown links, including links from `research/00-CHARTER.md` to root-level `docs/`.
- Confirmed the new procurement report is linked from the research README and index.
- Confirmed the source register retains a source-use notes section.

No missing source IDs or broken local Markdown paths were found in the checked archive.

### 2.2 Legal-source freshness correction

The prior procurement analysis correctly distinguished Article 105 (portal content/management) from Article 107 (electronic exchange and bid responses according to a Finance Minister timetable). Its weakness was the freshness boundary: UpGrowth's article says its Gazette review extended through No. 59, dated 16 August 2026. That cannot establish the position as of 5 November. [S159]

The SGG's official landing-page latest-issues listing reports No. 76 dated 29 October, with Nos. 73–75 immediately preceding it. The separate official 2026 calendar page retrieved in this pass still shows only through No. 57. [S165–S166]

PDF retrieval attempts for later issues, including Nos. 74–76, failed in this research environment. This is a tooling/access limitation, not evidence that the PDFs or their contents do not exist. The archive therefore now uses the precise status:

> **Article 107 timetable and general implementing decree: not verified for Official Journal Nos. 60–76.**

It must not state “no order exists,” “no decree was published,” or “paper submission remains universally valid” until the relevant official issue sequence is inspected.

### 2.3 Evidence classification and traceability

The current archive distinguishes official legal text, official programme/agency statements, procurement notices, provisional awards, vendor claims and hypotheses in prose. However, the source register is not yet a complete claim ledger.

The next version should assign stable claim IDs (for example, `CLM-PROC-001`) and store:
- exact, atomic claim;
- supporting source IDs and pinpoint article/page/paragraph;
- contradictory or limiting evidence;
- event date, publication date and access date;
- geography, sample, denominator and unit where applicable;
- claim status (verified, bounded, disputed, stale, unverified);
- confidence and refresh trigger;
- affected hypotheses and decisions.

A source can be authoritative while still not proving the inference attached to it. Legal publication, implementation, operational use and commercial demand must remain separate states.

## 3. Repeatable QA added

Added:
- `scripts/validate_research.py` — offline structural validator;
- `tests/test_validate_research.py` — unit tests;
- a CI step in `.github/workflows/dataset-validation.yml`.

The validator checks:
1. source-register IDs are present, unique, ordered and gap-free;
2. every bracketed citation resolves to a registered source ID;
3. local Markdown links resolve within the repository;
4. key archive metadata dates are parsed and stale dates are warned about.

It intentionally does **not**:
- request external URLs or certify that a source page remains live;
- verify factual claims, legal interpretation or whether a law is in force;
- establish dataset licenses, consent or rights to reuse source material;
- assess source independence, representativeness or evidentiary sufficiency.

Commands:

```bash
python scripts/validate_research.py
python -m unittest discover -s tests -v
```

**Verified CI result:** GitHub Actions run [42056904055](https://github.com/looloofy69-sketch/EL-Rouji-datasetes/actions/runs/42056904055), for commit `200a98b6875cc17972f9aeb384fbdc541fdd269a`, completed successfully. The validator checked 27 Markdown files, 166 source IDs, 582 citation occurrences and 54 local links: **0 errors, 0 warnings**. The full test suite ran 11 tests: **11 passed**. This verifies the repository state at that commit; later changes should trigger another run.

## 4. Must-fix next

1. **Complete the legal scan:** obtain and inspect JO Nos. 60–76 in French and Arabic; search for Law 23-12, Articles 41, 58, 105–112, Article 107's timetable, and the general implementing decree.
2. **Resolve the official-index mismatch:** record which SGG index endpoint is current and whether the annual calendar is stale.
3. **Add claim IDs:** start with the procurement-law claims and material opportunity conclusions; expand to older documents as they are revised.
4. **Decide repository licensing:** select an explicit license for original research notes only after reviewing the repository's intended reuse. Do not relicense third-party content.
5. **Inspect CI:** verify the workflow run for the commit that added the research validator and test step.

## 5. Accepted limitations

- No product or market opportunity is validated by this audit.
- No representative tender sample, supplier interviews, paid pilot or contract-to-cash dataset exists in the current evidence.
- Provisional awards remain pre-contract evidence until final award, notification, delivery, acceptance, payment and renewal are checked.
- No external-link crawler or automated factual/legal verification system has been added; human review remains required.

## 6. Decision

**Keep the current opportunity map open.** The archive passes structural reference checks, but the legal implementation status remains unresolved for the latest Gazette range and the supplier-side opportunities remain unvalidated. The next research cycle should close evidence gaps before adding more product concepts.
