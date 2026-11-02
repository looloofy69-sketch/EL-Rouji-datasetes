# Electronic Public Procurement Portal and SME Market Access in Algeria

**Snapshot:** 2 November 2026  
**Status:** legal/functional specification confirmed; end-to-end live portal behavior not independently tested.

## 1. Executive assessment

Algeria's public-procurement modernization has moved beyond a general statutory requirement. An interministerial order dated **4 February 2026**, published in Official Journal No. 17 on **2 March 2026**, now specifies the content and management of the electronic public procurement portal.

The order defines a real transaction and information system:
- free access to tender documents;
- registration for contracting authorities and economic operators;
- publication of anticipated procurement programmes, concluded contracts from the prior financial year, legal texts, notices, price indices and lists of excluded/forbidden operators;
- multi-criteria search and alerts;
- document upload/download and information exchange;
- electronic bid submission;
- electronic signature and timestamping;
- integrity, confidentiality/encryption, event logs, interoperability and secure electronic archiving.

The Ministry of Finance is the functional administrator of the portal. Its DGB website invites operators to register, while NESDA publishes a supplier-facing guide and says it provides support and training for micro-enterprises entering the portal. These are operational ecosystem signals. However, the portal host timed out during direct technical access in this research pass, so end-to-end registration, bid submission, electronic signature, result tracking and data export have not been independently tested.

**Commercial consequence:** the public portal itself is a government-provided system. The potential supplier opportunity is complementary: help eligible SMEs become procurement-ready, integrate their business records with bid workflows, manage evidence/deadlines, or build procurement intelligence from lawfully accessible data. A replacement portal or unsupported scraping product is not justified.

## 2. Legal foundation and timeline

### 2.1 Law 23-12 establishes the portal and data functions

Law No. 23-12 of 5 August 2023 establishes:
- Article 105: an electronic public procurement portal managed by the Ministry of Finance;
- Article 106: information/documents passing through the portal form a database, with bidder application files archived and reusable in later procurement procedures;
- Article 107: contracting authorities must make competition documents electronically available according to a schedule fixed by ministerial order, and economic operators must submit bids electronically according to that schedule;
- Article 108: an annual economic census of concluded public contracts is conducted by Ministry of Finance services, with contracting authorities required to respond. [S130]

These articles indicate that the portal is not merely an online noticeboard. It is intended to support procurement workflows, bidder records, electronic submission and annual economic reporting.

### 2.2 Implementing order of 4 February 2026

The interministerial order of 4 February 2026, published in Official Journal No. 17 on 2 March 2026, specifies the portal content and management modalities under Article 105. It explicitly abrogates the prior 17 November 2013 order governing the earlier electronic portal. [S141]

This is an important refinement to the Article 110/112 transition analysis:
- the 2013 portal-specific order has been expressly abrogated by Article 9 of the 2026 order;
- other regulatory provisions under the old procurement framework may continue where not contrary to Law 23-12 and until replacement texts are published, under Article 112;
- each old regulation must be examined separately; it is incorrect to state that all 2015 regulatory material either remains wholly valid or is wholly extinguished.

## 3. Portal information published

Article 3 of the 2026 order requires the portal to publish:
1. legislation/regulations and legal opinions relating to public procurement;
2. forecast programmes of public procurement projects planned for the current financial year;
3. public contracts concluded during the preceding financial year;
4. lists of economic operators temporarily or permanently excluded from participation;
5. lists of operators prohibited from participation;
6. price indices;
7. published notices;
8. other information/documents relevant to the portal. [S141]

### Why this matters

If these data are accessible in a structured and reusable form, the portal could enable:
- procurement opportunity discovery and classification;
- forward-looking procurement calendars;
- analysis of buyer/sector/lot demand;
- supplier and awardee history;
- price-index and contract-value benchmarking;
- analysis of market concentration and recurring purchase categories;
- alerting for relevant opportunities and changes.

The order establishes publication obligations, but not that all information is available as open data, via an API, in bulk export or under unrestricted reuse terms. The data's completeness, update cadence, search functionality and licensing need to be tested.

## 4. Portal functions and controls

Article 4 lists portal functions:
- registration of contracting authorities and economic operators;
- multi-criteria search;
- alerts for new items;
- exchange of information between authorities and operators;
- document upload and download;
- electronic submission of bids;
- electronic signature of documents;
- timestamping. [S141]

Article 5 requires system design to preserve:
- **Integrity:** scan/document formats that protect immutability, electronic signature and identified/authenticated economic operators.
- **Confidentiality:** exchanged documents protected by an encryption system.
- **Traceability:** event logs for electronic information exchanges and timestamped acknowledgements showing receipt date/time for every electronic bid or bid on electronic media.
- **Interoperability:** standards and references enabling different systems to communicate and exchange data.
- **Secure electronic archiving:** preservation of digitized documents in a secure electronic archive. [S141]

Article 6 conditions access to reserved features on registration. The authority/operator completes an enrollment form and designates the individual authorized to use the reserved functions; the organization remains responsible for use of its credentials. Article 8 says technical portal characteristics must be non-discriminatory and must not obstruct operators' access. [S141]

These requirements may create integration and assurance needs, but they also mean third-party tools should not handle bid credentials or sensitive submission material without strong authorization, security controls and contractual clarity.

## 5. Operational access and supplier support

The DGB's official page invites economic operators to register online on the public procurement portal or in person at the DGB to consult calls for competition and download tender specifications. [S142]

NESDA has a dedicated supplier-facing portal guide. It describes:
- viewing consultations and public contracts;
- following ongoing competition notices;
- downloading specifications and required documents;
- electronic bid submission and tender participation;
- tracking bid status and results;
- online operator registration, including organization details and required supporting records;
- agency-organized training/workshops to help micro-enterprises use the portal. [S143]

This creates a useful lead for SME onboarding and bid-support research: NESDA sees supplier registration and use of the procurement portal as an area requiring guidance and training.

However, a support guide is not evidence of how many suppliers are registered, how many submit bids electronically, rejection rates, actual portal uptime or the commercial value of third-party assistance. The direct portal did not complete a technical access check in this pass.

## 6. Relationship to Articles 41 and 58

The portal is the common transaction layer; access privileges and procurement eligibility still come from substantive procurement law.

### Article 41 — direct negotiation

A labelled startup providing digitalization/innovation services with a unique and innovative solution may be considered under an exceptional direct-negotiation case. This is not a general bypass of competition or an automatic award. [S130]

### Article 58 — reserved needs

Where certain needs can be satisfied by SMEs, very small enterprises or labelled startups, the contracting authority must reserve the corresponding markets for eligible categories unless it justifies an exception. The law allows a separate specification or lot, within a 20% maximum of public procurement. The 20% wording is a ceiling, not a guaranteed startup quota. The denominator, category split and actual application remain to be verified. [S130]

**Commercial consequence:** Article 58 could be more relevant than Article 41 for ordinary eligible goods/services or smaller procurement lots. A supplier may qualify through SME/startup status and technical capacity even if its solution is not unique/innovative enough for Article 41. That interpretation should be confirmed with procurement counsel and tested against actual tender documents.

## 6A. General implementing decree and phased electronic submission — status as at 2 November 2026

The Government's official 18 March 2026 communiqué says examination of a draft executive decree fixing the application modalities of Law 23-12 had begun. Its 30 April 2026 communiqué says the Government had finalized examination of that draft after several sessions. Neither statement establishes that the text was subsequently signed, promulgated or published in the Official Journal. No final general application decree was located in this research pass; that is a bounded search finding, not a legal certification that no later text exists. [S157–S158]

A separate operational point is important: **Article 107 of Law 23-12 makes electronic exchange and electronic bidder responses subject to a timetable fixed by an order of the Minister of Finance.** The February 2026 order in Official Journal No. 17 concerns Article 105 (portal content and management); it is not itself the Article 107 timetable. The latter was not located in this pass. UpGrowth, a commercial tender-support provider, also states that it had not found the timetable order in its Gazette archive and says suppliers should follow the instructions in each tender notice; this is a secondary source and should be checked against the complete official register. [S130, S141, S159]

This distinction changes how to read the CERIST examples: its 2026 SOC-wall notice asked for email/fax submission and its Zimbra-support notice specified email. These notices demonstrate that non-portal channels were still being specified in this limited sample after the Article 105 order; they do **not** prove nationwide non-adoption, non-compliance or contradiction with Article 107 while the phased timetable and tender-specific requirements remain to be established. Follow the applicable tender notice, not an assumed universal electronic-submission date. [S162–S163]

The Article 41 position also needs scope precision. Article 41 has several exceptional negotiation cases. An interministerial order of 9 October 2025 does implement the cultural/artistic-services case under its first indent; that is not the separate labelled-startup digital/innovation exception. DGB's 5 May 2026 statement specifically said the startup-related implementing texts were being finalized. [S164, S131]

Article 112 remains the transition rule: regulatory provisions continue insofar as they are not contrary to Law 23-12 until replacement regulations are published. Do not assume that the entire 2015 presidential decree either remains wholly applicable or has been wholly displaced; test the individual rule, relevant implementing text and tender launch/notification date. [S130]

## 7. Potential supplier opportunities around the portal

| Opportunity | Target user/buyer | Possible offer | Main validation needed |
|---|---|---|---|
| SME procurement readiness | Micro-enterprises, SMEs, labelled startups | Registration support, supplier-file readiness, bid calendar, eligibility checklist, document completeness, tender response workflow | Are SMEs willing to pay for help that NESDA/DGB already support? What tasks remain unassisted? |
| Bid operations software | Frequent government suppliers | Tender intake, requirement extraction, deadline/task tracking, evidence reuse, document-version control, internal approvals | Does portal export/access support automation? Can the workflow be added without duplicating free portal features? |
| Procurement intelligence | Suppliers, integrators, consultants, investors | Sector/authority forecasts, awardee history, price/contract benchmarking, opportunity alerts | Structured-data access, permitted reuse, coverage, data quality and customer willingness to pay |
| Tender compliance and evidence management | SMEs and companies handling many bids | Reusable company credentials, tax/social certificates, technical references, bid templates, audit logs | Legal handling, secure storage, customer responsibility and integration with portal requirements |
| Supplier and award analytics | Banks, guarantee funds, incubators, DIHs, business associations | Supplier performance/contract history analytics and market maps | Data rights, lawful processing, completeness and whether institutions have budget |
| Secure integration/e-signature | Procurement software providers and high-volume bidders | Document-signing, timestamp, archiving, secure exchange and ERP connectors | Law 26-02, trust-provider access, standards, certification, portal interfaces |

The opportunity is complementary to government infrastructure. Do not build a competing portal, scrape restricted information, or automate bid submission without explicit authorized interfaces and user consent.

## 8. Risks and constraints

- **Free government baseline:** tender search, downloads, registration and submission are official portal functions; third-party software must solve a meaningful adjacent job.
- **SME ability to pay:** micro-enterprises may need support but cannot always afford subscription software or full-service tender consulting.
- **Data access and reuse:** published documents do not automatically grant permission for bulk extraction, republishing or profiling. Verify access terms and applicable data-protection/administrative-document rules.
- **Credential security:** bid submission and electronic signature are high-impact functions. Avoid storing portal passwords or private keys unless an authorized, secure design and legal basis exist.
- **Procurement timing:** tenders and addenda can change quickly; stale opportunities can cause commercial and legal harm.
- **Eligibility:** supplier registration does not guarantee qualification; tender-specific financial, technical, professional and guarantee requirements still apply.
- **Competition:** consultants, accountants, professional bodies, incubators, NESDA, integrators and existing procurement-support services may already perform parts of this work.
- **Portal maturity:** the 2026 order defines functionality, but live coverage, support, uptime and electronic-submission adoption are not independently verified.

## 9. Next research tests

1. Inspect live portal behavior for registration, search, alerts, tender downloads, electronic bid submission, signature, timestamp receipts, status and results.
2. Obtain the official portal user manual, FAQ, registration requirements, file-size/formats, signing method, support channels and service-level commitments.
3. Determine whether public tender notices, forecast programmes, awarded-contract records and price indices are searchable, exportable, API-accessible or legally reusable in bulk.
4. Review a representative sample of tender documents to count how many cite Articles 41 or 58, reserve lots for SMEs/startups, or state eligibility conditions.
5. Search Article 58 use in tenders and award notices; no confirmed Article 58 startup award has yet been found in this research pass.
6. Interview/research SMEs that already bid: identify rejected bids, document errors, guarantee costs, deadline failures, qualification constraints and bid-preparation hours.
7. Compare SME paid willingness-to-pay against the free DGB/NESDA assistance and private tender consultants.
8. Map integrations with accounting, tax/social-security certificates, e-signature/trust providers, company registers and bank guarantees.
9. Measure procurement data quality and potential value of contract-award/price intelligence before building any dataset or service.

## 10. Current decision

**Treat the national e-procurement portal as an operating public digital infrastructure whose legal functionality is now formally specified.** Continue research into supplier enablement and procurement intelligence, but do not build a replacement portal or assume data is open.

The most promising hypothesis is a narrowly scoped product/service that reduces SME bid-preparation failure and helps frequent suppliers interpret procurement demand—provided the free government portal leaves a measurable problem and supplier economics support paid assistance.