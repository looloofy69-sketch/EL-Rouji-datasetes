# Decision Intelligence: Current Hypotheses, Dependencies and Change Triggers

**As of:** 1 November 2026  
**Status:** living decision register; no product commitment implied.

## 1. Cross-landscape findings that now matter

### A. National data governance and public interoperability

Presidential Decree 25-320 creates a national framework composed of data-classification, source-cataloguing and interoperability components. It defines data quality across completeness, consistency between systems, accuracy and timeliness. The national interoperability system is intended for public institutions and public-service entities; the decree describes a secure interconnection network separate from the public internet. Access by public-service organizations requires coordination, classification/cataloguing and source approval for a stated purpose. [S23]

On 20 September 2026, the Council of Ministers ordered preparation of a further presidential decree covering secure digital interconnection, sector representation and inter-wilaya links. This is an official policy signal, not evidence that the later decree has already been promulgated or that private suppliers can access the network. [S26]

**Implication:** create a public-sector data governance/interoperability research lane. Study data classification, catalogues, quality, metadata, lineage, integration, security and procurement. Do not assume a commercial API or unrestricted public data access.

### B. Privacy operations and data accountability

Law 25-11 amends Algeria's personal-data law. Its text introduces processing-activity registers for controllers and processors, automated logs for personal-data operations, a data-protection-officer role, and impact assessments where processing is likely to create high risks, including when new technologies are used. The automated log provisions identify operations such as collection, storage, extraction, consultation, transmission, matching/interconnection, encryption and deletion; their application details are to be set by regulation. [S25]

**Implication:** privacy operations, data mapping, processing records, audit trails, DPO workflows and impact-assessment support deserve a separate market and legal research lane. Do not assume a software-only product or an enforcement timetable. Determine implementing rules, ANPDP guidance, affected organizations, current compliance practices and who pays.

### C. Electronic trust infrastructure

Law 26-02 covers trust services and electronic identification. The qualified electronic signature is the form assimilated to a handwritten signature; qualified seals and timestamps carry specific integrity/origin/time presumptions; qualified electronic registered delivery has evidence-related presumptions. Trust-service providers face authorization, audit and operational requirements. Article 27 requires data collected by trust-service providers to be hosted nationally, subject to applicable law for transfers abroad. [S24]

**Implication:** investigate the provider ecosystem, trust lists, implementation rules and integration opportunities. A startup may be better positioned as an application/integration layer using authorized providers than as the regulated trust provider itself. The provider route is a regulated activity, not a normal SaaS feature.

### D. Sector digitalization is uneven

- The national agricultural information system was launched on 29 June 2026 to provide updated sector data for central and local governance. This establishes a government modernization initiative; access rights, interfaces, data completeness and private-sector opportunities remain unknown. [S31]
- In September 2026, the Health Ministry reported that nationwide health digitization, particularly electronic medical records, was nearing a final deployment phase. This is a programme-status statement; actual facility coverage, interoperability, uptime, procurement and vendor access need verification. [S32]
- Public-works qualification/classification and engineering-office approval services were being added to a national digital-services portal in September 2026. This shows digitization of a specific administrative workflow, not proof of an open market for replacement portals. [S33]
- Small Algerian manufacturing studies indicate early or gradual digital adoption, with cost, skills and technology/organizational readiness barriers. Samples are limited and non-equivalent, so they are signals for further research rather than population estimates. [S34]

**Implication:** research by sector and workflow. The public-sector project may be a buyer, a source of standards, a partner channel or a competitor to private services; distinguish these roles.

### E. Payments and fintech infrastructure

Bank of Algeria materials list the 2025 framework for payment service providers, and a 2026 regulation establishing the National Payments Committee. The Bank's communiqué says Djezzy Payment Services received authorization to constitute as a PSP, to be followed by an application for operating approval. This is an ecosystem-opening signal, not evidence that the PSP was already fully licensed or live. [S35]

**Implication:** map merchant acquiring, payment providers, banks, settlement, disputes, APIs, reconciliation and regulation. Do not build a payment institution or handle regulated funds without the required approvals.

### F. Algerian language technology

The language-technology landscape is richer than the earlier scan suggested:
- NADI 2026 covers robust ASR, dialect identification, dialectal TTS, speech translation and spoken understanding across 11 countries, with blind test sets and public leaderboards. [S27]
- Arab Voices provides a standardized view of 31 dialectal Arabic speech datasets across 14 dialects. It can support comparative evaluation, but must not be assumed to cover every Algerian variety or permit unrestricted reuse. [S28]
- ELNER-DZ is a publicly listed Algerian Arabic/Arabizi NER and entity-linking dataset; its license, data construction, source composition and evaluation quality need inspection before operational use. [S29]
- A 2026 study extends work on Algerian Darija NER/entity linking; the article is restricted-access, so methods and license cannot yet be fully inspected. [S30]
- A recent Algerian ASR paper reports a large remaining error rate on code-switched speech and named entities, even after system improvements. [S12]

**Implication:** a defensible path may involve evaluation, localization, data quality and domain-specific components rather than training a broad foundation model. Commercial buyer and licensing remain open.

### G. Public-sector security structures and procurement

Presidential Decree 26-07, published in Official Journal No. 04 on 18 January 2026, requires each public institution, administration and public body to create a structure responsible for information-system security and personal-data protection, independent of the IT structure and attached to the organization's top official. Its tasks include security policy, risk mapping/remediation, security and cyber-resilience solutions, audits, continuous monitoring, immediate incident reporting, privacy-law coordination and staff training. [S36]

The decree also connects the security structure with public procurement: it coordinates integration of information-security and confidentiality clauses when outsourcing is used. It specifies coordination with the national information-systems security agency and the national personal-data authority. [S36]

**Implication:** a potential service market exists around audit readiness, security operations, risk registers, incident response, subcontractor assurance, training and privacy/security evidence. But this is not yet a measured buyer market. Need verify actual staffing, guidance, procurement budgets, vendor eligibility and contract awards.

### H. Cloud, compute and managed infrastructure

ARPCE's cloud-service page defines a general-authorization route for hosting/storage services, describing technical and commercial project documentation, infrastructure architecture, storage, backup, security systems and hosting premises. Its dated directory contains 20 providers, with four entries marked as being in a regularization process on the page. The directory displays March 2025 as its update date; recheck current status with ARPCE. [S37]

A local provider map now includes:
- AYRADE, whose stock-exchange profile reports cloud authorization and a 1 billion DZD 2026 public offering for data-center expansion. [S41]
- ICOSNET, advertising local public cloud, VPS and dedicated NVIDIA GPU-as-a-Service. [S38]
- AventureCloudz, launched by Djezzy, Algeria Venture and Taubyte as a developer cloud hosted on the Djezzy Cloud marketplace. The current website displays example apps, but public SLA, pricing, capacity and full production maturity are not established. [S39–S40]
- Djezzy and Armonika's August 2026 partnership to develop sovereign-cloud and virtualization solutions. [S45]
- CERIST, an ARPCE-authorized cloud operator that advertises VPS, Swift/S3 object storage, NFS/SMB, backups, virtual networking, VPN, firewall and load balancing; it also procures GPU, SOC, backup/restore and cybersecurity services. [S37, S42–S44, S47]
- eBS, advertising hosting, managed infrastructure, backup, security and a Tier III 85 m² data-center facility at Sidi Abdellah; details are vendor claims and some pages may be dated. [S48–S49]

**Implication:** commodity hosting is not an empty market. Investigate managed AI deployments, cloud migration, backup/recovery, GPU workload scheduling, specialized security, and integration on top of incumbent infrastructure before considering infrastructure capex. Determine how ARPCE authorization applies to a software-only SaaS or managed-service model before launch.

### I. Procurement signals are not contract proof

CERIST's 2026 procurement notices include GPU computing, SOC video-wall equipment, backup/restore, anti-DDoS and a 12-month managed cybersecurity service for audit, continuous monitoring and incident response. These are specific institutional demand signals. The notices alone do not establish awards, delivered systems, spend, renewal or a market-wide procurement volume. [S42–S44]

**Implication:** monitor consultation, clarification/addendum, deadline, award, delivery/acceptance and renewal as distinct lifecycle states. An awarded contract and repeat purchase are stronger evidence than a notice.

### J. Cybersecurity services, accreditation and delivery competition

The provider field now includes broad telco/cloud/integrator channels (Ooredoo, Icosnet, AYRADE, Djezzy/GDSS), specialist cyber/GRC firms (Intervalle, UNIDEES, CYBEARS, Keystone, MN Advising, 3S Pay), international assurance/certification providers (SGS, Mazars) and cross-border boutiques (CYBERWAVE). Their advertised scopes overlap in audit, GRC, SOC/MDR, incident response, training, cloud security and payment assessment. Vendor capabilities and operating performance remain unverified unless independently tested. [S50–S60, S64, S66]

GIE Monétique's approved-evaluation register lists providers and exact accreditation scopes for payment-system homologation. This is a meaningful entry barrier for specified payment evaluation work, but it is not a universal cybersecurity licence. The register contains expiry/status inconsistencies (including records past their stated expiry but still labelled “Valide”); confirm all credentials with GIE before relying on them. Its process describes a dossier, review, potential pilot with a GIE stakeholder, evaluation and scope-specific approval. [S50–S51]

**Implication:** generic cybersecurity services are already supplied by several local and international providers. Differentiation must be tested in a specific vertical, operating model, response-time/service guarantee, deployment constraint, productized evidence workflow or qualification scope. 24/7 SOC/MDR has high staffing, tooling and liability costs; do not infer attractive economics from advertised service menus.

CERIST's page lists a 2026 managed-cybersecurity consultation, but its linked PDF extracted text ends with a 30 October 2024 deadline. Treat the specification as mismatched/stale until CERIST confirms the correct file. The notice establishes a procurement lead, not an award or current technical requirement. [S62–S63]

### K. Enterprise R&D spending, open innovation and startup market access

Article 119 of Finance Law 2026 requires Algerian-law establishments with annual turnover at or above DZD2bn to allocate at least 1% of taxable profit to R&D/innovation. Activities may be internal or conducted through open-innovation programmes with labelled startups/incubators; implementing regulation must establish sector scope and application modalities. The R&D&I declaration service is still marked “opening soon”, and its page includes scale-ups although statutory wording does not. [S18, S121–S122]

This is separate from Article 147 quater of the 2025 Finance Law, which gives a capped taxable-profit allowance for qualifying R&D/open-innovation spend. The 2025 law repealed Article 171, and the 22 April 2025 interministerial order updated the 9 May 2023 order to Article 147 quater while retaining the six-month contract and mandatory terms. The Open Innovation site still cites the older Article 171 / Finance Law 2023 wording, so official law and amended order take precedence over stale explanatory website text. [S117–S120, S123]

The Open Innovation platform accepts company challenges; however, posting, matching, signed contract, delivery and payment are separate states. ASF offers equity/quasi-equity and partner introductions for labelled startups, but its published headline metrics are fund-reported; its DZD1.3bn figure is partner introductions, not cash invested. [S123–S129]

Law 23-12 creates two distinct market-access mechanisms:

- **Article 41:** an exceptional direct-negotiation route for labelled startups providing digitalization/innovation services with unique and innovative solutions.
- **Article 58:** when specified needs can be satisfied by small or very small enterprises or labelled startups (or qualifying employers of persons with disabilities), the contracting authority must reserve those markets exclusively for the eligible category unless it justifies an exception. The identified needs may be split into a separate specification or lot within a 20% maximum of public procurement. This is a ceiling, not a guaranteed 20% quota for startups, and its denominator/category split need operational clarification. [S130]

The DGB's latest located official statement (5 May 2026) says Article 41 implementing texts were being finalized. It does not establish Article 58 implementation status. No actual procurement notice/award applying Article 58 to a labelled startup has yet been verified in this research pass. [S131]

Articles 110 and 112 clarify the transition: procedures initiated before Law 23-12's entry into force, and contracts notified before that date, retain the specified treatment under Presidential Decree 15-247; regulatory provisions continue to apply insofar as they are not contrary to Law 23-12 until replacement regulations are published. It is therefore inaccurate to infer either that the whole 2015 decree is fully current or that all of it ceased to apply immediately. [S130]

**Implication:** corporate open-innovation contracts may form a real commercialization channel. To prove it, identify qualifying large firms, actual funded challenges, contract values, deliverables, paid invoices, renewals and the legal documentation required. Do not treat a tax deduction or expenditure obligation as evidence of startup revenue.

### M. Electronic procurement portal and supplier enablement

The 4 February 2026 interministerial order (Official Journal No. 17, 2 March 2026) operationalizes Article 105 of Law 23-12. It defines a public portal publishing procurement legislation/opinions, forecast procurement programmes, previous-year concluded contracts, excluded/prohibited operators, price indices and notices. It includes registration, multi-criteria search, alerts, information exchange, document upload/download, bid submission, electronic signature and timestamping. The system must preserve document integrity, confidentiality/encryption, event traceability, interoperability and secure electronic archiving. [S141]

DGB invites economic operators to register. NESDA describes portal access, electronic bid submission and result tracking, and says it conducts training/workshops to help micro-enterprises use the service. The portal's public hostname did not complete an independent technical-access check during this pass, so actual feature availability, reliability and usage still need testing. [S142–S143]

**Potential adjacent offers:** SME tender/bid readiness; reusable supplier evidence and compliance files; deadline/addendum tracking; procurement data/award analytics; tender-price/sector intelligence; and integrations with accounting, tax/social-security certificates, e-signature and guarantee providers.

**Boundary:** the government portal is the official transaction system. A third-party product must add measurable value beyond free portal functions, use lawful data access, protect bid credentials and not replace official electronic submission.

### L. SME financing, guarantees and investment incentives

The financing ecosystem contains distinct mechanisms: NESDA micro-enterprise financing (up to DZD10m through self, mixed or triangular structures); FGAR bank-credit guarantees (10–80% by project risk in the general route, up to DZD100m guarantee); CGCI-PME guarantees for eligible tangible investment credits/leasing (up to DZD350m eligible credit, 80% creation/60% development coverage, subject to sector exclusions); and AAPI investment incentives tied to priority-sector, zone or structuring projects requiring prior registration. [S132–S140]

These are not interchangeable:
- NESDA offers agency/bank loan participation for eligible micro-enterprises, not venture capital.
- FGAR and CGCI guarantee banks; the enterprise remains liable for the loan and may still need collateral.
- AAPI incentives are attached to a qualifying registered investment, not ordinary operating expenditure.
- ASF remains a separate labelled-startup equity/quasi-equity route. [S129]

**Implication:** funding availability should be tested against business model capital intensity. A software-first product may fit startup/open-innovation/ASF pathways; an equipment-heavy integrator may need bank debt and guarantee support; a micro-enterprise field-service model may fit NESDA; a larger asset project may fit AAPI if the sector and registration conditions are met. No eligibility or approval is presumed.

## 2. Opportunity themes to keep open

| Theme | What could be built or sold | What must be proven |
|---|---|---|
| Data governance and privacy operations | Data inventories, processing registers, flow maps, audit logs, DPIA workflows, DPO tools or managed services | Implementing rules, enforcement, buyer, budget and willingness to pay |
| Trust-service ecosystem | Application integrations, signature/seal validation, timestamp workflows, evidence preservation, provider integrations | Authorized providers, standards, APIs, fees, trust-list status and market adoption |
| Public data interoperability | Data catalogs, data quality, metadata, integration adapters, security and implementation support | Scope of public projects, procurement, accreditation, access and vendor eligibility |
| Payments/fintech operations | Merchant integration, reconciliation, payment operations, dispute workflows, finance analytics | PSP/bank APIs, licensing boundary, merchant volumes and economics |
| Sector-specific operations | Agriculture, health, manufacturing, public works or logistics workflow software | Specific buyer, process, existing systems, budget, data access and measurable problem |
| Language technology | Speech/text evaluation, entity resolution, transcription QA, multilingual search and localized models | Dataset rights, field quality, funded buyer, representative evaluation and cost |
| Cloud, compute and managed infrastructure | Local data centers, developer clouds and GPU/cyber procurement are developing. | Current authorization, SLA, capacity, utilization, workload demand and incumbent economics. |
| Cybersecurity services and assurance | Decree 26-07 creates public-sector security structures; local integrators, specialists and GIE-scoped evaluation bodies already supply services. | Actual outsourcing budgets, award records, credentials, customer outcomes, SLAs and cost-to-serve. |
| Enterprise open innovation and startup market access | Article 119 creates a large-enterprise R&D/innovation allocation; Article 147 quater and the Open Innovation platform support qualifying startup partnerships. | Implementing rules, label eligibility, actual challenges/contracts, buyer budgets, tax evidence and repeat paid delivery. |
| Public procurement Articles 41 and 58 | Article 41 permits narrow direct negotiation for unique/innovative labelled-startup digital solutions; Article 58 reserves certain satisfiable needs for SMEs/TPEs/labelled startups unless justified, within a 20% ceiling. | Implementing procedure, 20% calculation, actual reserved tenders/awards, qualifications and payment/acceptance. |
| Electronic procurement supplier enablement and intelligence | A 2026 order defines official portal functions, data content and secure submission; NESDA offers SME onboarding help. | Live feature maturity, accessible/exportable data, reuse terms, SME bid pain, rejection rates, paid demand and security responsibilities. |
| SME finance and investment incentives | NESDA, FGAR, CGCI-PME and AAPI provide distinct debt, guarantee and investment-incentive routes. | Product/project eligibility, bank participation, collateral, sector exclusions, disbursement timing and project economics. |
| Agent assurance | Workflow-specific testing, observability, policy checks, recovery and audit | Buyer urgency, measurable failures and competitive difference |

## 3. Current decision guardrails

1. No commitment to the document-operations hypothesis until it beats local and international competitors on a specific workflow.
2. Do not treat government digitization announcements as open procurement or accessible data.
3. Do not treat regulatory obligations as a paying market until the affected organization, enforcement path, budget owner and purchase route are identified.
4. Do not treat a dataset's public listing as model-training permission; inspect license, provenance, terms and quality.
5. Do not equate a PSP's authorization to constitute with final authorization to operate.
6. Do not equate technical need with a profitable business.
7. Keep product, services, infrastructure and integration business models in scope.

## 4. Reopening conditions

Reopen document operations if hands-on competitor testing exposes a costly local exception that incumbents fail to handle.

Promote privacy operations if implementing rules, ANPDP enforcement/guidance, organizational buyers and budget evidence converge.

Promote public interoperability if the new decree, technical references, secure network scope, procurement notices and supplier qualification become observable.

Promote trust-service integration if authorized providers and usable APIs/partner channels become available.

Promote language technology if a funded buyer and lawful representative data can be secured.

Promote a sector vertical only after observing a recurring workflow and validating current alternatives.


## 5. New decision guardrails

8. Treat the ARPCE cloud directory as a dated directory; verify current authorization and exact service scope with the regulator.
9. Do not equate an infrastructure partnership, product demo or published roadmap with production availability or SLA.
10. Do not treat tender notices as awards, delivery or recurring revenue; follow the full procurement lifecycle.
11. Compare local cloud offerings on total cost per successful workload, including storage, network, support, backup, security, egress and compliance.
12. Prefer partnership/workload layers over data-center or GPU capex until utilization, power, procurement and support economics are demonstrated.

## 6. New decision guardrails

13. Do not treat GIE Monétique accreditation as a universal cybersecurity licence; verify the exact scope and validity for each entity.
14. Do not rely on a register's “Valid” label where the stated expiry date has passed; confirm directly with the issuer.
15. Do not treat a 2026 procurement webpage as validating a linked attachment whose own text contains a 2024 deadline.
16. Do not enter commodity audit, pentest, firewall management or generic SOC without evidence of a specific underserved buyer/workflow and sustainable staffing economics.

## 7. Public procurement interpretation guardrails

17. Do not conflate Article 41 direct negotiation (unique/innovative labelled-startup solution) with Article 58 reservation of needs for SMEs/TPEs/labelled startups.
18. The Article 58 20% language is a maximum ceiling over the stated public-procurement category, not a guaranteed startup allocation or revenue forecast.
19. For Article 58, verify that the need is satisfiable by an eligible category and check the contracting authority's written justification if not reserved.
20. Apply Article 110/112 transition rules by procedure launch, specification approval and contract notification dates; assess old regulatory provisions individually for conflict with Law 23-12.
