# Research Queue — Next Landscape Passes

**Updated:** 5 November 2026  
**Purpose:** direct the next research cycle toward uncertainties most likely to change the opportunity map.

## Priority 0 — archive integrity and procurement-law freshness

- Retrieve and inspect official French and Arabic Gazette PDFs for JO Nos. 60–76; record a reproducible issue-by-issue search for Law 23-12, Article 107, the general implementing decree, Article 41 and Article 58.
- Resolve the SGG website freshness conflict: latest-issues listing reports No. 76, while the parsed annual calendar still ends at No. 57.
- Do not close the Article 107 timetable question from UpGrowth's scan through No. 59. Record exact issue/page/date and effective-date language if found.
- Introduce claim-level IDs for material assertions and link each claim to one or more source IDs, counter-evidence, confidence and refresh trigger.
- Decide whether to publish an explicit license for original research notes. Do not imply rights over linked third-party source material.
- Run `python scripts/validate_research.py` and `python -m unittest discover -s tests -v` after research-archive changes. The validator checks local structure only; manual source/legal review remains mandatory.

## Priority 1 — regulatory implementation and trust infrastructure

### Questions
- Have the classification and cataloguing references required by Decree 25-320 been formally published?
- Was the additional secure-interconnection decree ordered on 20 September 2026 promulgated?
- What are the scope, standards, network interfaces, procurement path and supplier qualification rules?
- What is the current operational status of the national certification authority and trust list under Law 26-02?
- Which trust-service providers are authorized, for which specific services, and what integrations are available?
- What regulations or guidance operationalize the processing logs, DPO and impact-assessment provisions of Law 25-11?

### Decision impact
Could validate or reject an opportunity in data governance, privacy operations, trust-service integration or public-sector delivery.

## Priority 4 — buyer and workflow mapping by sector

Build a sector workflow map for:
1. Agriculture and food systems.
2. Health and medical administration.
3. Manufacturing and industrial services.
4. Construction and public works.
5. Logistics, transport and warehousing.
6. Commerce, retail and wholesale distribution.
7. Financial services and payments.
8. Tourism and hospitality.
9. Public administration and service delivery.

For each sector identify buyer/user, top recurring workflows, source systems, documents/data, delay/error costs, current tools, procurement route and reachable channel.

### Document-integrity and status checks

- Resolve the CERIST 2026 managed-cyber consultation page versus the linked specification PDF that ends with a 2024 deadline.
- Confirm whether 2026 public procurement notices resulted in award, delivery and renewal.
- Cross-check GIE register expiry dates that conflict with “Valid” statuses directly with GIE.
- Verify the certificate scope and issuer for providers advertising ISO 27001-certified SOC/CSIRT services.

## Priority 4 — agriculture, healthcare and manufacturing

### Agriculture
- Verify which SNAI modules are actually in production and what the data-sharing/API policy permits.
- Identify farm, crop and wilaya segments with installed and paying agritech users.
- Test FITO, AirCrop, Felatech and SIPTECH offers for actual availability, field coverage, reliability and ROI.
- Determine install/maintenance cost per farm or season, farmer willingness to pay, channel partner and seasonality.
- Separate Agripreneurs opportunity sheets and challenge projects from operating businesses and paid demand.

### Healthcare
- After the **15 November 2026** CHU target, verify facility-by-facility deployment, live EHR modules, daily users and inter-facility exchange.
- Find supplier names, procurement awards, contract values, acceptance criteria, renewals and support arrangements.
- Map EHR, PACS/RIS, LIS, pharmacy, telemedicine and patient identity/consent integration.
- Hands-on compare SmartAvicenne, eSiha, CabiSanté, Hakim-DZ, Nawi-Med, MCM Systems and COMPOS; distinguish shipped modules from roadmap items.
- Review data protection, local hosting/backup, encryption, access, audit and incident-response controls before any health-data workflow.

### Manufacturing
- Select two subsectors (e.g. food processing, metalworking, plastics or building materials) and map workflows end to end.
- Identify installed ERP/MES/CMMS/WMS, machine vendors, systems integrators and point solutions.
- Quantify one measurable loss per workflow (downtime, scrap, rework, stockout, energy, delayed delivery or manual reporting).
- Compare product, integration, managed service and financing/lease models; include plant visits and OT constraints.

### Evidence limits
- Do not equate fibre connectivity with live clinical records.
- Do not treat startup programme registration, opportunity sheets or product roadmaps as paid adoption.
- Do not extrapolate a single manufacturing case or small survey to all Algerian factories.

## Priority 5 — payments, logistics, ports and customs

### Payments
- Verify each PSP's state: authorization to constitute, application for operating approval, approved, operational and live merchant products.
- Inspect Regulation 25-02 and Instruction 06-2025 for allowed services, limits, agent models, KYC/AML and technology controls.
- Map banks/acquirers, CIB/Edahabia, mobile/postal services and PSP providers; collect developer docs, API access, fees, settlement and dispute processes.
- Identify merchant software needs that do not require becoming a PSP: checkout integration, reconciliation, returns, chargeback/dispute evidence and payment-to-invoice matching.

### Logistics and ports
- Test ECOSERVICE, COD Scale and GHL with real workflow cases and comparable data; verify return rates, delivery definitions, COD payout times, integration failures and service fees.
- Inspect courier-dz tests, adapter completeness, release cadence, licensing and API quotas; test DZBuild's shipping API availability, error behavior and reliability.
- Separate last-mile COD from B2B freight, warehouses, cold chain and port operations.
- Verify APCS implementation, operator/governance, port coverage, interfaces, adoption and service levels.
- Resolve the legal/operational status of the port-community system under Decree 21-147.
- Establish exactly which ALCES functions cover commercial freight versus traveler declarations and vehicle TPD.

## Priority 6 — construction, education and tourism

### Construction/public works
- Verify launch and actual usage of contractor qualification/classification and engineering-office approval services on the national portal.
- Map tender/bid preparation, subcontractor qualification, site records, materials, progress claims and payment certificates.
- Identify government portal integration boundaries and the existing construction ERP/BIM/project-management vendors.

### Higher education
- Test the MESRS orientation LLM on correctness, coverage, source provenance, hallucinations, accessibility and peak-load behavior.
- Map campus-level student records, scheduling, examinations, certificates, research administration, alumni and university-life systems.
- Distinguish national systems from institution-specific products; investigate integration rather than replacement by default.

### Tourism/hospitality
- Trial SAAFIR and Matares, document pricing and modules, verify active customers, OTA/channel manager integration, payment/gateway support, accounting/tax behavior and support.
- Map travel agency, hotel, tour operator and destination workflows separately.
- Validate the payment/hotel-system fragmentation claim with actual establishments and current product configurations.
- Test seasonality, occupancy and willingness to pay before estimating SaaS economics.

## Priority 5 — competition and alternatives

For every promising workflow map:
- local direct competitors;
- international direct competitors;
- adjacent platforms and suites;
- system integrators and outsourcing providers;
- manual and spreadsheet workflows;
- internal build options;
- the option of doing nothing.

Perform hands-on testing where possible. A feature page alone is not evidence of usable functionality.

## Priority 6 — payment and economic rails

Research:
- status and licensing of PSPs;
- CIB/Edahabia/BaridiMob and new acceptance rails;
- merchant settlement and dispute processes;
- available bank/PSP APIs and partner programmes;
- pricing and transaction costs;
- digital-business billing and subscription collection constraints.

Separate a payment-service business from software that supports merchants or financial institutions.

## Priority 2 — public-sector cybersecurity and procurement

### Questions
- Which institutions have created and staffed the structures required by Presidential Decree 26-07?
- Which roles are staffed, outsourced or still vacant?
- What budgets, certifications, security clearances, references and procurement processes apply?
- Which tenders have been awarded for security audits, SOC operations, monitoring, incident response, backup and recovery?
- Which vendors repeatedly win these contracts and what capabilities do they demonstrate?
- What are the current GIE Monétique accreditation scopes and validity for Intervalle, Keystone, MN Advising, CYBEARS, 3S Pay, UNIDEES and Mazars?
- Which bidders and awarded contract values are visible for SOC, MDR, security audit, incident response, backup and anti-DDoS contracts?
- What are comparable local prices for a defined pentest, SI audit, SOC/MDR package, incident-response retainer and OT assessment?
- Which incumbent channels (Ooredoo, Icosnet, AYRADE, Algérie Télécom, Djezzy/GDSS) deliver security in-house versus through partners?
- What is the role of national cybersecurity agencies and the ANPDP in oversight and assistance?

### Decision impact
Could reveal opportunities in managed security, audit readiness, privacy/security operations, integration and training—or show that the market is closed to a new entrant without credentials and institutional references. GIE approval is scope-specific to payment-system evaluation; it is not a universal cyber licence.

## Cloud and compute questions

- Confirm the current ARPCE authorization status and service scope of providers listed in its dated directory.
- Compare AYRADE, Icosnet, AventureCloudz, Djezzy/Armonika, CERIST Cloud and eBS on compute, storage, GPU, network, IAM, backup, observability, APIs, SLA, pricing and actual production availability.
- Identify actual customer workloads and usage levels; do not infer adoption from marketing claims.
- Follow public procurement from tender notice through award, acceptance and renewal.
- Compare managed local infrastructure against international cloud and self-hosted alternatives on cost per successful workload.

## Priority 3 — infrastructure, cloud authorization and deployment economics

Map local hosting/data-center providers, cloud regions, colocation, connectivity, bandwidth, power reliability, GPU access/import constraints, managed security and technical support. Benchmark local hosting against foreign managed services and self-hosting on real total cost and legal scope.

## Priority 7 — language and data assets

- inspect NADI 2026 and Arab Voices task coverage for Algerian varieties;
- inspect ELNER-DZ license, provenance, construction, label quality and splits;
- compare Algerian ASR, NER, retrieval and dialect evaluation papers;
- identify gaps in domain-specific vocabulary, named entities, transliteration, code-switching and speech noise;
- investigate a funded buyer before designing a new dataset.

## Priority 8 — market sizing and economics

Do not size the entire AI market. After a workflow is identified, use bottom-up estimates:
- number of target organizations in the exact segment;
- share with the workflow and required digital readiness;
- monthly task/document/transaction volume;
- current cost and economic loss;
- obtainable price and channel reach;
- service and integration capacity;
- retention and expansion potential.

Record low/base/high assumptions and distinguish known counts from estimated conversion factors.

## Priority 1 — procurement outcomes, DIH implementation and strategy execution

### CERIST and public institutions
- Track 02/CERIST/2026 managed cybersecurity through corrected technical specification, final award, contract value, service commencement and renewal.
- Obtain outcomes for CERIST consultations 04 (backup/restore), 05 (anti-DDoS), 06/07 (GPU), 08 (SOC video wall) and 09 (Zimbra support renewal).
- Follow consultation 09 through its 8 November 2026 deadline; identify selected supplier, supported release scope, upgrade plan and renewal terms.
- Find comparable procurements and award notices at universities, hospitals, utilities, telecoms, research institutions and other sensitive sectors named by the national strategy.
- Distinguish consultation, award, contract signature, delivery/acceptance and renewal.

### DIHMA and Green Innovation Hub
- Obtain full consortium membership, final service catalogues, signed agreements, operational plans and support/funding terms.
- Determine first SME cohorts, DMA/IMA diagnostics, observed problems and resulting paid projects.
- Map how suppliers are selected, whether external vendors can become delivery partners, and how performance is evaluated.
- Track whether the DIHs generate implementation opportunities or mainly diagnostic/training activity.

### National cybersecurity strategy
- Map the four strategic axes to ASSI guidance, standards, sector implementation requirements, staffing and procurement.
- Identify measurable targets, milestones and responsible institutions if published.
- Check whether private-sector entities in critical sectors are directly addressed by implementation guidance, and what proof/assurance suppliers must provide.
- Search for implementing decrees, circulars, standards and sector-specific technical requirements.

## Priority 2 — electronic procurement portal implementation and supplier workflow

### Verify live portal behavior
- Complete a legitimate supplier registration flow using an authorized test/company account if available.
- Test multi-criteria search, tender alerts, free download of specifications, addenda and deadline updates.
- Verify electronic bid upload, file formats/size limits, e-signature, timestamp receipt, submission correction and post-submission tracking.
- Test how the portal handles groups/consortia, subcontractors, guarantees, certificates and reusable bidder dossiers.
- Verify portal availability, support process, access errors and audit/receipt downloads. Distinguish legal capability from deployed functionality.

### Procurement data and intelligence
- Check whether forecast procurement programmes, previous-year concluded contracts, price indices, excluded/prohibited operators and award records are queryable/exportable in bulk.
- Check search filters, pagination, date coverage, duplicate/updated notices and stable identifiers.
- Determine reuse/API/scraping terms before building datasets or commercial intelligence products.
- Identify buyer/user personas: suppliers, incubators, banks, guarantee funds, DIHs, consultants and procurement officers.

### SME supplier enablement
- Observe real micro-enterprise/SME bid preparation and identify failure modes: registration, document validity, tax/social certificates, technical references, guarantees, eligibility, lots, deadlines and electronic submission.
- Measure hours per bid, rejection reason, cost of guarantees, win rate, payment delay and repeat tender participation.
- Compare third-party bid support against free DGB/NESDA onboarding and public portal functions.
- Test whether an external tool can add value without storing portal passwords or private keys or bypassing the official submission flow.

## Priority 2 — public procurement access for SMEs and labelled startups

### Article 58 reserved needs
- Identify tender notices/specifications that expressly cite Article 58 or reserve lots/markets for small enterprises, very small enterprises or labelled startups.
- Check whether the reserved category includes SMEs, TPEs and labelled startups in the same 20% ceiling and how contracting authorities calculate that ceiling.
- Collect the authority's justification where a satisfiable need is not reserved; test whether this is recorded in procurement presentation reports.
- Determine how startup-label status is checked at bid submission and contract award.
- Compare actual qualification thresholds, guarantees, turnover/experience criteria, contract sizes, payment terms and technical obligations for reserved vs ordinary lots.
- Find awarded contracts under Article 58 and record awardee type, amount, delivery and renewal; no applied example has yet been confirmed in this research pass.

### Article 41 direct negotiation
- Locate the final implementing texts and any operational guidance for labelled startups with unique/innovative digital solutions.
- Find actual use cases, approvals, procurement decisions and awards under Article 41.
- Establish how contracting authorities assess uniqueness/innovation and what evidence is required.

### Transition rules
- Apply Article 110 to procedures and contracts based on their notice/consultation/notification dates.
- Under Article 112, distinguish provisions contrary to Law 23-12 (abrogated) from regulatory matters remaining in force until replacement texts.
- Do not infer that the entire 2015 decree is either wholly current or wholly repealed; map each relevant regulatory clause against Law 23-12 and later implementing texts.

## Priority 2 — enterprise R&D/innovation spending and open-innovation conversion

### Article 119 demand-side mechanism
- Identify Algerian-law companies with annual turnover at/above DZD 2bn by sector using official registries, annual reports and audited disclosures.
- Separate turnover qualification from taxable-profit base; estimate theoretical spending only where both are evidenced.
- Find the final list of eligible sectors and modalities in the implementing regulation.
- Confirm whether the R&D&I declaration service has opened, what its 31 January deadline applies to, and how next-year commitments are declared.
- Verify whether scale-up labels are eligible despite Article 119 wording naming startups/incubators.

### Article 147 quater allowance and open innovation
- Verify current DGI guidance/circular and the 22 April 2025 amendment to the 9 May 2023 order.
- Inspect contract templates and mandatory IP, deliverable, milestone, duration, payment and termination fields.
- Confirm eligible expenses, required proof, invoicing and audit treatment with current DGI guidance.
- Identify companies that have claimed the allowance and startups/incubators that have been contracted.
- Count signed, delivered and paid projects separately from platform sign-ups or problem submissions.

### Open Innovation platform
- Build an inventory of actual company challenges currently posted.
- Identify buyer, problem owner, sector, budget signal, deadline, data/site access, and expected result.
- Track startup proposals, selection, contracts, deliverables, acceptance and follow-on work.
- Determine whether the platform's 2024 challenge page and problem-submission service remain actively maintained.

## Priority 3 — SME finance, guarantees and investment-incentive execution

### NESDA
- Confirm creation and expansion eligibility for software, IT services, installation/maintenance and equipment-based digital businesses.
- Verify current funding ceilings, own contributions, repayment terms, tax benefits, guarantees and local agency process.
- Distinguish self-finance, mixed 50/50 and triangular 70% bank structures; use the detailed profile/region table rather than a generic ratio.
- Follow actual applications to approval, disbursement, project completion and repayment; programme pages alone do not establish conversion.

### FGAR
- Verify the correct product (general FGAR versus MEDA), eligible sector, creation/development status and credit purpose.
- Obtain current bank quotes and FGAR fee/coverage calculation for a real project.
- Confirm whether collateral/security is still required, the process sequence and typical approval time.
- Track actual guarantee certificates and financed projects, not just announced ceilings.

### CGCI-PME
- Check borrower thresholds, sector exclusions, eligible equipment/leasing, covered amount and bank collateral.
- Verify current TPE delegated guarantee terms separately from the CGCI-PME product.
- Confirm bank participation and guarantee availability before relying on the coverage in a cash-flow model.

### AAPI
- Determine which software, data-center, cybersecurity, industrial IoT or renewable-energy projects qualify for priority-sector or zone regimes.
- Confirm registration-before-realization timing, eligible assets/services and exemption period for each regime.
- Check the formal structural-investment thresholds (>=500 jobs, >=DZD10bn) before treating it as relevant to an SME.
- Trace registered investment projects to actual incentive certificates, imports/equipment and operational delivery.

### Funding-route comparison
For each viable business model, compare ASF equity/quasi-equity, corporate open innovation, NESDA loan, bank debt supported by FGAR/CGCI and AAPI investment incentives on:
- maximum capital and timing;
- founder cash contribution;
- repayment/ownership dilution;
- permitted expense categories/assets;
- guarantee/collateral;
- eligibility and exclusions;
- time to disbursement and required proof;
- ability to cover working capital, payroll and customer payment delays.

## Procurement supplier-side research follow-on

### Procurement-law transition and contract evidence
- Monitor Official Journal issues after the Government's 30 Apr 2026 completed-review communiqué for final publication of the general implementing decree; record the exact publication/effective date and transitional treatment.
- Locate the Article 107 Finance Minister timetable for mandatory electronic exchange/submission. Do not equate the Article 105 portal-management order with the Article 107 schedule.
- Check the tender-specific legal basis for email, fax and paper submission in post-March 2026 procedures; distinguish allowed phase-in from old process persistence.
- Follow CERIST provisional awards 15/2025 and 16/2025 to final award, contract notification, delivery, acceptance, payment and renewal.
- Expand the sample beyond CERIST: compare research centres, universities, hospitals, utilities, municipalities and central ministries; record channel, number of bidders, award method and lifecycle state.
- Track Article 41 by its seven separate legal cases; do not extrapolate a sector-specific order to the labelled-startup exception. Track Article 58 separately.



### Competitive benchmark
- Compare the same 100-tender sample across the official portal and at least three paid providers.
- Measure recall, precision, duplicate rates, update latency, addendum detection, award linkage, entity resolution and normalized-price accuracy.
- Obtain written current quotes; record plan coverage, tax, archive range, data export rights and service-level commitments.
- Test document retrieval, translation, filing and representation as delivered services, not just website claims.

### Supplier bid-readiness
- Build a taxonomy of eligibility and rejection failure: expired/missing evidence, technical nonconformity, guarantee, forms, deadline, signature/channel and missed addendum.
- Estimate bid frequency, preparation hours, cost per bid, win rate, preventable failure rate and repeated evidence reuse.
- Compare micro-enterprise, SME, specialist service provider and larger-contractor workflows; do not pool them into one average.
- Test willingness to pay for self-service workflow software versus one-time bid review and managed bid operations.

### Contract-to-cash and finance
- Obtain current CGMP and bank guarantee conditions, fees, collateral, approval times, eligible contract types and availability by company segment.
- Measure certified-invoice-to-payment time, receivables mobilization usage, advance guarantees, guarantee release times and late-payment claim use.
- Check whether CGMP/banks expose permitted integration or referral channels; otherwise model them as external human workflows.
- Determine whether invoice/progress/guarantee handoffs create enough repeated administrative work to justify a paid tool.

### Article 58 and portal operation
- Search full tender specifications and award documents for reserved lots/eligible categories and justified exceptions; separate “not stated” from “not applicable”.
- Test portal registration, search, alerts, free document download, upload, e-signature, timestamp receipt, status tracking, helpdesk and support from a standard supplier account.
- Check whether data can be exported or reused commercially; do not assume the 2026 order creates an open API or blanket reuse licence.

## Research pass exit criteria

A lane can be deprioritized when:
- no credible buyer or budget owner emerges;
- the workflow is infrequent or low impact;
- existing alternatives solve it adequately;
- legal/data access is not feasible;
- infrastructure or integration makes delivery uneconomic;
- the expected service burden destroys margin.

A lane should advance only when a concrete buyer/workflow and a measurable validation path exist.
