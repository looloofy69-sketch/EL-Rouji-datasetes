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

## 2. Opportunity themes to keep open

| Theme | What could be built or sold | What must be proven |
|---|---|---|
| Data governance and privacy operations | Data inventories, processing registers, flow maps, audit logs, DPIA workflows, DPO tools or managed services | Implementing rules, enforcement, buyer, budget and willingness to pay |
| Trust-service ecosystem | Application integrations, signature/seal validation, timestamp workflows, evidence preservation, provider integrations | Authorized providers, standards, APIs, fees, trust-list status and market adoption |
| Public data interoperability | Data catalogs, data quality, metadata, integration adapters, security and implementation support | Scope of public projects, procurement, accreditation, access and vendor eligibility |
| Payments/fintech operations | Merchant integration, reconciliation, payment operations, dispute workflows, finance analytics | PSP/bank APIs, licensing boundary, merchant volumes and economics |
| Sector-specific operations | Agriculture, health, manufacturing, public works or logistics workflow software | Specific buyer, process, existing systems, budget, data access and measurable problem |
| Language technology | Speech/text evaluation, entity resolution, transcription QA, multilingual search and localized models | Dataset rights, field quality, funded buyer, representative evaluation and cost |
| Cloud, compute and managed infrastructure | Local data centers, developer clouds and GPU/cyber procurement are developing. | Current authorization, SLA, capacity, utilization, workload demand and incumbent economics. |\n| Agent assurance | Workflow-specific testing, observability, policy checks, recovery and audit | Buyer urgency, measurable failures and competitive difference |

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

