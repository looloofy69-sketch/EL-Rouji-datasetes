# Competitive Landscape: Algeria and Adjacent Products

**Snapshot date:** 1 November 2026  
**Evidence standard:** capability descriptions are vendor-published unless stated otherwise.

## 1. Commerce and COD operations

### KIO

KIO markets an Algerian commerce ecosystem spanning online stores, POS, customer profiles and a central operations/ERP layer. Its pages advertise inventory synchronization, offline POS, COD fraud screening, payment support and local courier integrations. KIO's public site claims more than 10,000 active merchants; this is a vendor claim, not an independently audited customer count. [S13]

**Implication:** a generic store builder, POS, stock synchronizer or COD fraud dashboard would face direct overlap.

### COD Scale

COD Scale markets a multi-store COD operating platform with order management, courier connections, ad tracking, delivered-profit calculations, reconciliation and an AI operations agent. Its site advertises 80+ carrier connections and integrations with WooCommerce, Shopify and YouCan. These are vendor statements; integration depth, reliability and customer outcomes have not been independently tested. [S14]

**Implication:** a generic COD dashboard, courier aggregator or profit tracker is not an open wedge without a materially better underserved workflow.

## 2. Invoicing and accounting

### Facturili

Facturili advertises Algerian invoicing/accounting workflows including VAT/SCF, quotes, invoices, credit notes, customer/payment tracking, accounting exports, G50 preparation, recurring invoices and stock management. Its pricing page displays monthly tiers of 2,900 DZD, 5,900 DZD and 11,900 DZD. Pricing and feature availability are vendor-published and should be rechecked before a commercial comparison. [S15]

### Fisira

Fisira's public product and pricing page advertises invoicing, stock, supplier workflows and an accounting tier with AI invoice scanning, accounting journals, reconciliation, G50 and financial statements. It displays annual prices of 11,900 DZD, 22,000 DZD and 35,000 DZD. This makes generic invoice scanning a weak differentiation claim. Extraction accuracy and operational performance have not been independently tested. [S16]

### DZ Compta

DZ Compta positions itself as a cloud platform for Algerian accounting practices, with SCF accounting, CNAS payroll and stock workflows. It advertises 186+ business features and says access is being opened in waves to validate practice workflows. Feature count and capability statements are vendor claims; production maturity and customer base require verification. [S17]

## 3. Competitive conclusion

A general OCR/document-capture system for Algerian accounting is not sufficiently differentiated. Multiple products already advertise invoicing, accounting preparation, AI scanning, stock, payroll, G50 and/or reconciliation.

A potential gap must be narrower than "AI reads invoices." Candidate areas:
- reconciliation across systems and document types when source records are inconsistent;
- exception resolution for missing, duplicated or mismatched supplier documents;
- evidence provenance and reviewer correction history across a firm's client portfolio;
- robust exports/connectors for heterogeneous incumbent accounting tools;
- monitoring and auditability for data quality and correction propagation;
- vertical workflows where mismatch creates an identifiable financial loss or compliance burden.

These are hypotheses, not confirmed gaps.

## 4. Hands-on competitive test

For each serious competitor, obtain a real trial or structured demo and run the same cases:
1. poor-quality, rotated or stamped invoice;
2. multi-page invoice and item-level extraction;
3. duplicate invoice with changed filename or scan;
4. mismatch among purchase order, invoice and delivery note;
5. partial delivery, credit note and return;
6. tax/identifier anomaly;
7. bank statement to invoice/payment reconciliation;
8. reviewer correction history and audit export;
9. multi-client/accountant separation and permissions;
10. API/export quality and failure recovery.

Score observed field accuracy, exception recall, false positives, reviewer time, integrations, pricing, onboarding and support—not feature checkboxes.

## 8. International document-workflow benchmarks

The first product hypothesis must be narrowed further. Supplier-document intake, extraction, duplicate detection and statement-to-invoice reconciliation are established capabilities in international products:

- **AutoEntry** captures purchase invoices, receipts, purchase credit notes, supplier statements, sales invoices, sales credits and bank statements. It extracts invoice totals, tax summaries and optional line items, and applies arithmetic checks. [S19]
- **AutoEntry supplier reconciliation** matches uploaded supplier statements against purchase invoices in its workspace. Its help material says the workflow is limited to purchases/supplier statements and remains separate from reconciliation performed in the connected accounting product. [S20]
- **Dext** reconciles supplier statements against invoices in Dext and connected accounting software using supplier and reference data, with amount/date fallbacks. [S21]
- **Dext duplicate detection** compares extracted fields using type-specific rules; its own documentation describes cases where missing or inconsistent extraction fields allow duplicates through. The rules are scoped to Dext cost items rather than every record already posted into a ledger. [S22]

**Consequence:** extraction, duplicate detection and supplier-statement matching are not defensible features by themselves. A proposed product must show a specific local or vertical advantage that existing suites do not already deliver.

### Remaining gap hypotheses to test

1. **Local-system interoperability:** usable imports/exports or APIs across the accounting, banking, POS, e-commerce and courier systems actually used by target Algerian firms.
2. **Local document interpretation:** measured performance on Algerian invoice layouts, stamps, supplier identifiers, Arabic/French/mixed text and locally used forms—not just language support claims.
3. **Cross-system exception control:** reconciliation where the relevant evidence is spread across separate accounting, procurement, inventory, delivery, payment and messaging systems.
4. **Local rule transparency:** configurable, reviewer-visible checks that are useful to the accountant/operator without pretending to provide legal certification.
5. **Portfolio-level exception operations:** prioritization, reminders, evidence requests, reviewer assignment and audit history across many client entities.

No evidence yet establishes that any of these gaps are unserved in Algeria. They are questions for direct competitor testing and customer workflow observation.

### Required competitor test

The same permissioned document cases should be run through local products (Fisira, Facturili, DZ Compta where accessible) and international benchmarks (Dext, AutoEntry where accessible). Record actual inputs supported, extraction accuracy, duplicate/statement match behavior, connected accounting systems, export/API limits, exception handling, reviewer time, price and data-hosting terms.

Do not infer missing functionality from marketing pages or from the absence of public API documentation.
