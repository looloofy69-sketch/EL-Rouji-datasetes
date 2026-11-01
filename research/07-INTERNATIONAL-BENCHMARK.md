# International Benchmark: Document Capture and Reconciliation

**Date:** 1 November 2026  
**Purpose:** test whether the document-operations hypothesis is genuinely differentiated.

## 1. Why this comparison matters

The product hypothesis initially emphasized supplier-document capture, extraction, duplicate detection, supplier statement matching and exception review. Those are not novel capabilities. International products already document them, so a generic implementation would compete on breadth, quality, price and integration against mature suites.

## 2. AutoEntry

AutoEntry's documentation lists purchase invoices/bills, receipts, purchase credit notes, supplier statements, sales invoices/bills, sales credit notes, bank statements and expense documents as supported types. It extracts invoice totals, tax summaries and optional full line-item data, and describes arithmetic validation. It can export bank statement data as CSV/Excel. [S19]

Its supplier statement reconciliation matches uploaded supplier statements with purchase invoices in its own workspace. The help center says this feature is for purchases/supplier statements and is separate from reconciliation workflows in an integrated accounting product. [S20]

## 3. Dext

Dext documents supplier-statement reconciliation against invoices in Dext and connected accounting software. Matching uses supplier name and document reference, with amount/date fallbacks when references are missing or inconsistent. [S21]

Dext's duplicate detection is rule-based on extracted fields and document type. Its documentation describes failure cases caused by missing or inconsistent fields and states that duplicate detection runs within Dext's own cost-item scope; transactions already posted into accounting software require other checks. [S22]

## 4. What this invalidates

The following are not differentiators on their own:
- invoice/receipt OCR;
- supplier and invoice field extraction;
- line-item capture;
- duplicate detection;
- supplier-statement-to-invoice matching;
- basic export to accounting products;
- generic human review queues.

A feature checklist that includes these functions would not establish an open market gap.

## 5. What may remain differentiated

Potentially differentiated work must be proven in an Algerian workflow:
- dependable connectors/imports across locally used accounting, banking, inventory, POS, courier and commerce systems;
- local SCF/fiscal workflow support with reviewable rules and no unsupported compliance claims;
- strong extraction/validation for real Arabic/French/mixed-script local documents, stamps and identifiers;
- exception resolution across separate systems and operational handoffs;
- portfolio-level evidence requests, assignment, reminders and reviewer audit history;
- lower total cost for a defined segment compared with the incumbent workflow.

The current research does not prove that local products lack these capabilities. Lack of public API documentation is not evidence that an integration is unavailable.

## 6. Comparative test protocol

Use the same authorized sample and score each product on:
1. supported document types and channels;
2. critical-field precision/recall by document type;
3. supplier identity resolution;
4. duplicate detection and false-positive behavior;
5. statement-to-invoice matching;
6. PO/invoice/delivery/payment cross-matching;
7. handling of credits, partials, missing pages and mixed scripts;
8. reviewer time and correction history;
9. connected accounting products and export/API limits;
10. data location, retention, deletion and commercial pricing.

A meaningful gap exists only if a target user's required workflow fails in existing products and a prototype improves total cost or control measurably.

## 7. Updated decision

**Do not build a generic document extraction/reconciliation product.** Continue discovery only around a locally specific, cross-system exception workflow. If incumbent tools already handle the workflow, stop or select a different vertical problem.
