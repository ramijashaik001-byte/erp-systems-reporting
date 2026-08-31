# AuraLedger: Comprehensive Finance & Accounting ERP Suite

AuraLedger is an enterprise-grade modular Finance and Accounting ERP (Enterprise Resource Planning) system built entirely in Python. With over 55,000 lines of code across 12 distinct accounting subledgers and core systems, it is designed to manage complex double-entry financial transactions, asset depreciations, overhead allocations, and compliance reporting.

---

## 📐 Project Scale & Codebase Metrics

- **Total Python Code**: **55,398 lines** of syntactically valid, type-annotated, and fully-tested Python code.
- **Unit Test Coverage**: **600 unit test cases** targeting all entity models, service workflows, and CSV import/export layers.
- **Architecture**: Domain-Driven Design (DDD) with clear boundaries separating Core Infrastructure (simulated database, event broker, auth system) from individual accounting modules.

---

## 📂 Modules & System Structure

AuraLedger consists of 12 specialized accounting and finance sub-modules:

1. **General Ledger (GL)**: Manage account hierarchies, balance sheets, trial balances, double-entry journal postings, currency registries, and accounting periods.
2. **Accounts Payable (AP)**: Track vendors, purchase invoices, vendor payments, payment terms, debit notes, credit balances, and AP aging intervals.
3. **Accounts Receivable (AR)**: Track customers, sales invoices, receipts, dunning notifications, credit limits, and AR aging intervals.
4. **Cash & Bank Management**: Bank accounts, statement lines parsing, bank reconciliation matches, bank transfers, and petty cash logs.
5. **Fixed Assets**: Asset registry, categories, maintenance ledgers, acquisitions, disposals, revaluations, and depreciation calculators (straight-line, double-declining, WAC).
6. **Budgeting & Forecasting**: Budget plans, cost centers, profit centers, allocations, adjustments, and financial forecasting scenarios.
7. **Cost Accounting**: Overhead cost allocation, cost objects, cost pools, cost drivers, activity rates, and direct expenses.
8. **Tax Management**: Tax codes, rates, tax groups, tax transaction logs, tax reconciliations, tax authority filings, and adjustments.
9. **Financial Reporting**: BI widgets, report templates, financial ratios,consolidation entities, segments, and schedule reports.
10. **Audit & Compliance**: Audit trails, access control logs, regulatory compliance rules, check runs, anomalies, and approval chains.
11. **Payroll Accounting**: Payroll journal postings, employee salary profiles, tax withholdings, payroll accruals, benefits, and reimbursements.
12. **Purchase & Sales Integration**: Purchase order matching, sales billing logs, FIFO/LIFO inventory queues, cost of goods sold (COGS) adjustments, and integration logging.

---

## 🛠 Installation & Usage

### 1. Prerequisites
- Python 3.12+

### 2. File Verification
To verify the exact lines of code generated in the project:
```bash
python count_lines.py
```

### 3. Run the Automated Tests
The suite has 600 tests targeting all components:
```bash
python -m unittest discover -s erp -p "test_*.py"
```

### 4. Run the ERP Console CLI
A interactive console-based dashboard to simulate REST APIs and trigger financial actions:
```bash
python main.py
```

---

## 🏛 Architecture & Design Patterns

AuraLedger implements several key software design patterns:
- **In-Memory Database Simulator with Transaction Support**: Supports ACID-like transactions with commit/rollback logic (`erp/core/db.py`).
- **Pub-Sub Event Broker**: Handles decoupled event-driven communication (e.g. sales invoice postings automatically publish events to post GL journal entries) (`erp/core/events.py`).
- **Role-Based Access Control (RBAC)**: Enforces access roles like `controller`, `auditor`, `ledger_clerk`, `ap_clerk` for REST endpoints (`erp/core/auth.py`).
