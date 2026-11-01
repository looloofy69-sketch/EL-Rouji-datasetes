# Sector Landscape: Payments, Logistics, Public Services and Tourism in Algeria

**Snapshot:** 1 November 2026  
**Status:** first-pass landscape map; no product or market-entry decision.

## 1. Executive assessment

The second sector pass reveals distinct digital ecosystems:

- **Payments/fintech:** a formal PSP framework is in effect. Djezzy Payment Services has received authorization to constitute as a PSP, but a separate application for operating approval must follow. This creates new infrastructure possibilities within a regulated entry boundary.
- **Logistics/e-commerce:** merchant and courier operations already have multiple commercial products, fulfillment providers, courier APIs, free integration services and open-source unified courier adapters. Generic COD dashboards and courier aggregation are crowded hypotheses.
- **Ports/customs:** SERPORT describes an APCS Port Community System launched in 2021, while ALCES exposes selected customs services for travelers. A 2025 legal paper raises questions about institutional governance of the port-community platform. Traveler self-service is not proof of freight/customs single-window integration.
- **Construction/public works:** the Ministry announced an online portal extension for contractor qualification/classification and engineering-office approvals. This is an administrative workflow signal, not proof of a general construction-management market.
- **Higher education:** the 2026 orientation/registration system is a deployed public digital service at substantial scale, including an LLM assistant.
- **Tourism/hospitality:** research reports fragmented tourism-specific infrastructure and low interoperability between payment gateways and hotel systems. Local products already target travel agencies and hotel PMS workflows.

## 2. Payments and financial infrastructure

### 2.1 Regulatory perimeter

Bank of Algeria Regulation No. 25-02 of 14 April 2025 establishes the conditions for authorization to constitute, licensing and exercising activities as a Payment Service Provider (PSP). It defines PSP activity as requiring approval by the Governor of the Bank of Algeria and prohibits unauthorized entities from using the PSP designation or equivalent wording. [S89]

Instruction No. 06-2025 of 17 August 2025 defines operational rules for PSP activity, including remote payment-account opening through a secure technological process, account levels and other operating requirements. The full rulebook must be read before designing a product involving payment accounts or execution of regulated services. [S90]

The Monetary and Banking Council authorized **Djezzy Payment Services** to constitute as a PSP. The Bank of Algeria explicitly says a subsequent application for operating approval must be submitted within 12 months from notification of the constitution authorization. Constitution authorization is not equivalent to full operating authorization or a live commercial PSP service. [S91]

**Boundary:** software that helps merchants reconcile payments, manage checkout or integrate an authorized provider is different from becoming a PSP, holding customer funds or executing regulated payment services. Legal review is required before crossing that boundary.

### 2.2 Ecosystem questions

Map separately:
- banks and account/payment rails;
- CIB and Edahabia acquiring/acceptance;
- mobile and postal payment services;
- PSP applicants, approved entities and their final operating status;
- merchant acquiring, settlement, chargebacks/disputes and refunds;
- APIs, SDKs, webhooks, sandbox access and technical onboarding;
- POS hardware, QR and online checkout;
- merchant reconciliation and accounting exports;
- agent networks, cash-in/cash-out and distribution;
- AML/KYC, fraud controls, customer protection, security and data obligations.

Potential software opportunities may exist around merchant integration, reconciliation, dispute workflow, fraud operations and PSP back-office. None is validated by the regulatory opening alone. Obtain written API terms, fees, transaction volumes, buyer budgets, competitors and evidence of real usage.

## 3. Logistics, e-commerce and last-mile operations

### 3.1 Existing commercial platforms

**ECOSERVICE** markets an integrated platform for e-commerce service providers: order confirmation, preparation, stock, delivery tracking, payment/returns, affiliate management, API links to Facebook, Shopify, WooCommerce, Google Sheets and Leadvertex, plus integration with more than 60 delivery providers. It also advertises return-risk tooling, a courier mobile app and SMS notifications. These are vendor-published capabilities; customer count, provider coverage, reliability and economics are unverified. [S100]

**COD Scale** markets the full COD merchant lifecycle: multi-store order management, courier integrations, ad tracking, COD finance and an AI operations agent. It describes store integrations with WooCommerce, Shopify and YouCan and local courier/address features. Treat performance claims as vendor claims pending hands-on testing. [S101]

**GHL** markets fulfillment for Algerian merchants: call-center order confirmation, warehouse storage, preparation, delivery across 58 wilayas and COD payout within 72 hours. Its site displays a 92% delivery figure. These are provider claims; verify denominator, delivery definition, period, exclusions, returns and settlement terms before using them economically. [S102]

### 3.2 Developer infrastructure and courier APIs

The public GitHub project **courier-dz** describes a unified Node.js API client for 94 Algerian courier providers across 11 API engines. It normalizes order, tracking, rate and label data, maps provider-specific tracking statuses to a canonical dictionary, and includes rate limiting/retry behavior. The repository exposes an MIT license and a versioned package. This is evidence that courier API fragmentation is a recognized developer problem and an open-source abstraction already exists. It is not proof all 94 adapters work reliably in production or that merchants adopt the library. [S103]

**DZBuild** documents courier connections for merchants, including order submission, tracking IDs, delivery rates and stop-desk data. It also offers a free shipping API abstraction with endpoints for orders, tracking, rates, desks, courier catalogue, wilayas and communes. This further reduces the novelty of a generic unified courier API. [S104]

### 3.3 Competitive conclusion

The following are not differentiators by themselves: COD order dashboards, confirmation call centres, courier aggregation, tracking synchronization, order preparation/stock, COD reconciliation, return-risk flags and SMS notifications.

Narrower areas still worth examining:
- performance and cash reconciliation across couriers/3PLs and merchant systems;
- exception recovery when delivery statuses and COD settlement records disagree;
- B2B freight, warehouse and multi-leg transport beyond consumer e-commerce;
- route/warehouse optimization with measured operating costs;
- specialized vertical handling (cold chain, medical goods, industrial parts);
- cross-border and port/customs workflows subject to official interfaces.

Even these gaps require workflow evidence and competitor tests.

## 4. Ports, customs and trade facilitation

### 4.1 Port community systems

SERPORT's AL MARSA page describes **APCS (Algerian Port Community System)** as launched in 2021 and intended to centralize information exchange among shipping companies, port authorities and operators. Described functions include a common portal for Algerian ports, e-payment, logistics, billing and vessel-call management. The page also describes a broader PMS/Smart Port/BIM programme with blockchain, IoT, AI, geospatial and tracking elements. Distinguish the APCS core platform from the broader modernization vision and verify which features are actually deployed and used at each port. [S94]

A 2025 legal study on Executive Decree 21-147 and the port community platform argues that the framework established a digital port-management concept but raises a governance issue around the absence/unclear operation of the legally designated managing entity. This is an academic analysis, not a regulator ruling; it creates a diligence question about operational governance, responsibilities and platform scope. [S95]

### 4.2 Customs system ALCES

Official Algerian embassy notices describe the **Algerian Customs Electronic System (ALCES)** external portal for travelers to create accounts and remotely declare foreign currency/valuables and personal belongings, or subscribe to a customs transit/pass document (TPD) for vehicles for temporary entry/exit. These are specific traveler-facing services. The material reviewed does not establish that ALCES is a fully integrated freight-import/export single window or disclose public APIs for third-party vendors. Do not generalize this service into claims about commercial freight clearance. [S96]

### 4.3 Research questions

- Which APCS functions are live by port and operator?
- What does Decree 21-147 require, who is the system operator, and has institutional governance been resolved?
- What interfaces exist for shipping lines, freight forwarders, terminal operators, customs, banks and inland transport?
- What are the user adoption, uptime, data quality and process-time results?
- Which ALCES functions apply to commercial freight and which are traveler self-service only?
- Which tenders and contracts exist for ports, customs integration, tracking, identity, security and operations?

## 5. Construction and public works

APS reported on 1 September 2026 that the Ministry of Public Works and Basic Infrastructure's digital portal was to add services for submission of professional qualification/classification files for construction companies and accreditation files for private engineering offices through the national digital-services portal, with the new services scheduled from the following Sunday. [S97]

This is a concrete administrative workflow involving company records, qualifications, document submissions, approvals and status. It may create needs around applicant-side document preparation, integration, notifications and professional-record management. But the public portal itself is a government service and may displace standalone administrative tools.

It does not establish demand for a general construction ERP, BIM platform or project-management SaaS.

Further workflows to map: tender discovery, bid preparation, guarantees, subcontractor qualification, site diaries, progress measurement, material procurement, delivery notes, safety, inspections, change orders, claims, payment certificates and handover. Separate public works from private construction and large contractors from small subcontractors.

## 6. Higher education and public digital services

The Ministry of Higher Education announced that the 2026 baccalaureate orientation/registration guide was digitized, with online orientation and registration procedures beginning 15 July 2026. It also described an LLM-based assistant to answer student questions and data-mining tools to analyze preferences and improve the orientation process. [S92]

On 30 July 2026, the Ministry reported that the orientation process was conducted 100% digitally, with 391,018 students assigned and 97% receiving one of their preferred choices. These are official Ministry-reported figures, not an independent evaluation of placement quality, fairness or system reliability. [S93]

The Ministry's platform directory also lists student orientation, student records, alumni, university-life and other digital-service platforms. This demonstrates a multi-platform public ecosystem, not one isolated chatbot. [S94]

**Implication:** generic student-admission/orientation software is not a novel opportunity for the national higher-education process. Potential adjacent gaps may concern campus-level systems, interoperability, student services, learning administration, research/innovation management, data governance, accessibility and integrations with employers. Procurement and institutional autonomy need mapping.

## 7. Tourism and hospitality

### 7.1 Sector evidence and current products

A 2026 Algerian tourism digital-transformation study analyzing indicators from 2020–2025 reports a gap between mature foundational connectivity and a fragmented tourism-specific digital ecosystem. It identifies low interoperability between payment gateways and hospitality-management systems and weak data-driven destination marketing. It is a descriptive/analytical study, not a direct willingness-to-pay survey of hotels or agencies. [S98]

**SAAFIR** by SARL Whenrak markets an all-in-one SaaS for Algerian travel agencies: reservations, accounting, group tours, payroll, schedules, contracts, tasks, inter-agency network, Omra/Hadj workflows, multi-branch analytics and an AI assistant/document extraction. Its company page says the software is designed for Algerian travel agencies and operated by Whenrak. Deployment count, customer usage, booking integrations and commercial retention are not established. [S99]

**Matares** markets an AI-native property-management system for Algerian hotels covering reservations, reception, housekeeping, invoicing, occupancy/revenue reporting and channel management. It advertises French-language operation, local support and hotel onboarding. These are product statements; confirm production references, OTA connections, local tax/accounting behavior, uptime and adoption. [S100]

### 7.2 Tourism/hospitality workflows

- travel agency booking, supplier allotments and client files;
- flights, hotels, package tours, visas, Omra/Hadj and group departures;
- inter-agency inventory/resale and settlement;
- hotel reservations, channel management, check-in/out, housekeeping, POS, billing and night audit;
- payment acceptance, refunds, deposits and reconciliation;
- guest profiles, consent, communications and CRM;
- destination marketing, content, reviews and local experience providers;
- transport transfers, guides, activity providers and excursion capacity.

### 7.3 Competitive implications

Generic agency ERP and hotel PMS are already targeted by local products. Global OTAs add another competitive layer. Potentially underserved areas may be data/transaction interoperability, accounting/payment reconciliation, distribution channels, multilingual discovery, local supplier connectivity and small-property onboarding. Seasonal demand, low occupancy, OTA dependence and fragmented independent operators can make recurring SaaS economics difficult.

Do not infer a product gap from an academic finding of fragmentation until named systems, integrations, price points and workflows are tested.

## 8. Cross-sector comparison

| Sector | Existing public/digital infrastructure | Private supply / competitors | Main unknown |
|---|---|---|---|
| Payments | Bank of Algeria PSP framework and remote-account rules | Banks, card/postal rails, acquiring providers and new PSP entrants | Final PSP operating licences, usable APIs, merchant fees and demand |
| Last-mile logistics | Courier provider APIs and merchant/courier data rails | COD Scale, Ecoservice, GHL, DZBuild, courier-dz and delivery firms | Reliability, cash leakage, returns, settlement and non-e-commerce freight workflows |
| Ports/customs | APCS described as launched; ALCES traveler services available | Port operators, freight forwarders, shipping IT and integrators | APCS coverage/governance, APIs, freight/customs scope and procurement |
| Construction | National digital portal adding contractor/engineering-office qualification workflows | Construction ERP/BIM/project systems and document services | Actual live process, usage, integration and contractor budget |
| Higher education | Large-scale digital orientation/registration with LLM assistant | Campus systems, learning platforms and service providers | Integration with internal university systems and procurement scope |
| Tourism | Digital booking/payment ecosystem developing | SAAFIR for agencies, Matares for hotels, OTAs and international PMS | Paying installations, channel integrations and seasonality |

## 9. Decision guardrails

1. Do not build a generic COD dashboard or courier aggregator; local platforms and open-source integration layers already cover substantial functionality.
2. Do not become a PSP by inference. Confirm legal status, capital, authorization, operating licence and rules before any regulated activity.
3. Do not call ALCES a freight single window based only on traveler services.
4. Do not assume APCS's full AL MARSA vision is deployed. Verify live scope, port coverage, governance and interfaces.
5. Do not build general university admissions software against a live national platform without identifying a separate institutional workflow.
6. Do not build another generic travel-agency or hotel PMS before competitor testing and paid-buyer evidence.
7. Separate public-sector suppliers/procurement from private-market buyers; routes and sales cycles differ.

## 10. Next research actions

- **Payments:** map PSP authorization/operating status; inspect Regulation 25-02 and Instruction 06-2025 in detail; obtain bank/PSP merchant/API documents, fees, settlement cycles and technical onboarding conditions.
- **Logistics:** benchmark COD Scale, ECOSERVICE and GHL; inspect courier-dz code/tests/license; test courier status reconciliation, webhook reliability, returns and COD settlement; expand beyond last mile into ports, warehouses and B2B freight.
- **Ports/customs:** obtain APCS current operating description, port coverage, governance/operator documents, tenders and interfaces; map the boundary between ALCES traveler flows and commercial freight procedures.
- **Construction:** verify which portal services are live, obtain procedures/data fields, identify integrators and tender awards, map contractor-side workflows.
- **Education:** measure student experience, AI answer quality, service availability and integration with campus records; identify non-overlapping university operations.
- **Tourism:** interview agencies and hotels; compare SAAFIR and Matares trials, pricing, integrations and adoption; test payment/OTA/channel-manager behavior.

## 11. Current conclusion

**Keep these as separate market lanes.** Payments is regulated infrastructure; last-mile delivery is already competitive; ports/customs have national systems whose exact scope and governance need verification; higher education has a major live digital service; construction is adding administrative workflows; tourism has integration concerns and local software entrants.

None should be selected from desk research alone. Test system maturity, procurement/operating access, product behavior, buyer workflows, prices and economic consequences first.