# Product Hypothesis: Exception-First Document Operations

**Version:** 0.1 hypothesis  
**Date:** 1 November 2026  
**Status:** discovery only; not a product specification.

## 1. Target problem

Businesses and accounting practices receive documents from multiple sources and must decide what each represents, whether it is valid or duplicated, whether it matches related records, and what action should follow.

The candidate problem is not document OCR itself. It is the **cost of resolving uncertainty and inconsistency across a document workflow**.

## 2. Initial target workflows

### Workflow A — supplier documents into accounting preparation

Potential inputs: supplier invoices and credit notes, receipts and expenses, purchase orders, delivery notes, bank/payment evidence.

Potential actions:
1. capture and classify;
2. extract schema-bound fields and item rows;
3. identify supplier and document type;
4. validate arithmetic, totals, tax fields and identifiers;
5. identify duplicate/near-duplicate records;
6. compare with available PO, delivery and payment records;
7. create an exception with evidence and reason code;
8. request human review or missing information;
9. export approved results to incumbent software.

### Workflow B — procurement-to-payment for a distributor

Potential inputs: purchase order, supplier invoice, delivery/receipt note, return or credit note, bank or settlement record.

Potential exceptions: quantity/price mismatch, partial or split delivery, duplicate invoice, unrecorded credit note, payment amount/reference mismatch, missing supporting evidence.

Do not assume these are frequent or costly; workflow observation must establish that.

## 3. Proposed system boundary

The product should be an integration and control layer, not a replacement for accounting ledgers, ERP inventory masters, invoicing/tax filing systems, banking/payment systems or document-management repositories.

Source systems remain authoritative. The proposed layer stores references, extracted evidence, review decisions and reconciliation status according to an agreed retention policy.

## 4. Architectural principles

### Intake
- controlled channels: upload, monitored email, API or approved scan ingestion;
- explicit tenant/customer boundaries;
- file-type/size validation and malware scanning;
- content hashing and duplicate detection;
- quarantine for malformed or unsafe input.

### Processing
- OCR/layout parsing separate from language-model extraction;
- strict schemas per document class;
- field-level confidence and provenance (page, region, text span, extraction method);
- arithmetic and business-rule validation through deterministic code;
- model output is a proposal, never a ledger posting.

### Reconciliation
- explicit canonical entities for supplier, document, PO, delivery, payment, credit note and review case;
- matching uses identifiers, totals, dates, quantities and configurable tolerances;
- ambiguous matches remain unresolved; never silently force a link;
- retain the evidence and rule behind every proposed match.

### Human review
- queue ordered by financial impact, deadline and uncertainty;
- source view beside extracted values;
- correction capture with actor, timestamp, old/new value and reason;
- approval required for high-impact actions;
- reviewer feedback may improve rules/evaluation, but is not automatically training data.

### Integration and export
- start with one existing accounting system or stable CSV/XLSX contract;
- idempotent imports/exports;
- preserve external record IDs and reconciliation references;
- retries, dead-letter handling and audit logs;
- no write-back until explicitly authorized and validated.

## 5. Data and evaluation strategy

Before building extraction models:
- obtain representative, permissioned documents;
- label critical fields and exception classes with qualified reviewers;
- split by supplier/source and time to limit leakage;
- retain difficult cases: poor scans, duplicates, uncommon layouts, credits, mixed scripts;
- report field-level exact match and false-positive/abstention rates by document type;
- measure downstream correction and exception-resolution time.

Synthetic data tests parsers and boundaries; it cannot establish production accuracy or buyer value.

## 6. Defensibility hypothesis

Potential defensibility comes from deep local workflow integration, high-quality exception taxonomies, trusted audit trails, measured performance on permissioned local documents, decreasing integration cost and a distribution channel through accounting practices or sector ecosystems.

OCR or the LLM component alone is not a durable moat.

## 7. Non-goals for a first version

- full ERP or accounting ledger;
- generic OCR service;
- replacement for tax filing;
- autonomous posting without review;
- universal support for every document and accounting package;
- foundation-model training;
- indefinite retention of customer documents;
- legal-compliance certification claims.

## 8. Primary unknowns

1. Which exception class is frequent and expensive?
2. Who owns the budget?
3. Do current products already solve it?
4. Can incumbent systems expose records reliably?
5. Can critical-field precision reduce total reviewer effort?
6. What data/retention terms can buyers authorize?
7. Can pricing exceed support and integration cost?

## 9. Competitive boundary update

This hypothesis is narrower than a general invoice capture or supplier statement reconciliation tool. AutoEntry and Dext already advertise and document those capabilities, including line-item extraction, duplicate detection and supplier-statement matching. [S19–S22]

A potential local product must therefore demonstrate at least one of the following against actual alternatives:
- integration with local accounting or operational systems that users already rely on;
- reliable extraction/validation on local document patterns where existing software fails;
- exception resolution across multiple disconnected systems rather than another isolated document inbox;
- a materially better workflow for a defined local vertical or accountant portfolio.

These remain unproven. The product hypothesis should be rejected if hands-on tests show the existing systems already solve the target workflow with comparable reviewer effort and total cost.
