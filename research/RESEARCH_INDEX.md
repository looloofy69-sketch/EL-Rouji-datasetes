# Research Index

**Last updated:** 1 November 2026  
**Current phase:** Opportunity qualification, before product commitment.

## Executive position

The research does **not** justify building another general e-commerce platform, COD dashboard, accounting package or generic OCR product for Algeria. Current providers already advertise substantial overlap in those categories.

The strongest remaining hypothesis is an **exception-first document-operations and reconciliation layer**: connect to incumbent systems, classify and extract business documents, cross-check them against related records, expose uncertainty and evidence, and route exceptions to a human reviewer. This is a hypothesis, not a validated market gap.

No production dataset, customer workflow observation, paid pilot, willingness-to-pay result or product-market fit has been established.

## Research passes

| Pass | Question | Current result | Status |
|---|---|---|---|
| 1 | Where are AI, software, infrastructure and market shifts occurring? | AI adoption is increasing, but embedded business value and agent reliability remain uneven. Algeria has expanding digital reach and structural commerce frictions. | Landscape baseline |
| 2 | Which opportunities have demand and defensibility? | Generic AI tools and all-in-one commerce/accounting categories are crowded. Operational integration and exception handling appear more promising. | Qualified, not validated |
| 3 | Does Algeria provide a practical initial market? | Connectivity and digitization are growing; e-commerce remains cash-heavy and payment growth partly reflects non-retail administrative transactions. | Mixed evidence |
| 4 | Is document intelligence a viable wedge? | Extraction alone is commoditizing. Cross-document validation, provenance, exception workflow and incumbent compatibility may differentiate. | Primary hypothesis |
| 5 | What would disprove the hypothesis? | Existing software may solve the costly exceptions; reviewer labor or integration may eliminate savings; representative data may be inaccessible. | Pilot design pending |

## Key findings

1. **AI adoption is not business transformation.** The UK 2026 representative business survey reports 32% adoption, 50% of adopters reporting a productivity increase (generally modest), and 14% rating AI highly or critically important. This is UK evidence, not an Algeria estimate. [S01]
2. **Business AI value likely requires workflow integration.** The OECD 2026 D4SME survey reports increasing off-the-shelf use but uneven strategic, targeted and secure integration. Its 2,000+ SME sample across 12 OECD countries is explicitly non-representative. [S02]
3. **Agent reliability is a deployment constraint.** An ICML 2026 study of 306 practitioners across 26 domains reports that 68% of production agents execute at most 10 steps before human intervention and 74% rely primarily on human evaluation. [S04]
4. **Algeria's online payment growth needs careful interpretation.** First-half 2026 online payments reportedly grew 52% by count and 867% by value; AADL 3, Hadj fees and Eid-related purchases were cited as major value drivers. This is not equivalent to retail e-commerce growth. [S08]
5. **Algerian language capability is promising but difficult.** CAFE provides roughly 37 hours of spontaneous Algerian Arabic/French/English code-switching speech; recent ASR results still show a substantial error gap on code-switched speech and named entities. [S10–S12]
6. **The local product field is competitive.** KIO and COD Scale market integrated commerce/COD operations; Facturili, Fisira and DZ Compta market overlapping invoicing/accounting workflows, including AI extraction claims. [S13–S17]
7. **Extraction accuracy must be evaluated on real documents.** An October 2026 EMNLP Industry Track study found synthetic documents overestimated accuracy by 38–45 percentage points on one real-document category; aggregate scores concealed large category-level differences. [S03]

## Preliminary opportunity ranking

| Opportunity | Attractiveness | Confidence | Main uncertainty |
|---|---|---|---|
| Exception-first document operations/reconciliation | High | Medium-low | Is there a recurring, expensive, unsolved local exception? |
| Vertical workflow automation | High | Medium | Which narrow workflow has budget, volume and reachable buyers? |
| Agent evaluation/reliability | Medium-high | Medium | Differentiation against international tools; urgency and buyer |
| Algerian Arabic/code-switching technology | Long-term technical potential | Medium for technical need; low for commercial path | Rights, representative data, budget and buyer |
| General e-commerce/ERP/invoicing platform | Low for initial entry | Medium-high | Crowded product surface and support burden |

These are qualitative judgments, not measured market scores.

## Immediate next research

1. Map an accountant's monthly supplier-document workflow from receipt to posted entry and client follow-up.
2. Map a distributor's procurement-to-payment workflow, including invoice, PO, delivery note, return and settlement.
3. Identify exceptions that are frequent, costly, difficult to resolve and not handled adequately by existing products.
4. Obtain permissioned representative samples and establish human-reviewed ground truth before measuring extraction.
5. Compare competitor products in hands-on tests, not by feature-page claims.
6. Model onboarding, human review, support, storage, inference and integration cost.
7. Seek a paid pilot before building a broad platform.

## Known gaps

- No representative Algerian SME AI-adoption survey is established here.
- No reliable current TAM/SAM/SOM calculation has been completed.
- No current census of active accounting practices and their client portfolios has been verified.
- Competitor functionality, customer counts and uptime are vendor-reported unless independently tested.
- No customer interviews, workflow observations, real document samples, paid pilots or renewal evidence are recorded.
- Legal interpretations are research notes, not legal advice; implementation requires qualified Algerian tax/accounting review.

## Latest competitive correction

The document-operations idea has been narrowed again. AutoEntry and Dext already offer supplier document capture, extraction, duplicate controls and supplier-statement reconciliation. The concept is therefore **not** a novel generic document-processing product. The only remaining hypothesis is a locally differentiated interoperability/exception-control workflow, pending hands-on product comparison and direct workflow evidence. [S19–S22]

This reduces confidence in the idea and strengthens the no-broad-build decision.
