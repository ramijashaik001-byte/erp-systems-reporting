# AuraLedger System Settings
class AppConfig:
    DEBUG = True
    APP_NAME = "AuraLedger Finance & Accounting Suite"
    DEFAULT_CURRENCY = "USD"
    AUDIT_LOG_FILE = "auraledger_audit.log"
    ENABLED_MODULES = [
        "general_ledger", "accounts_payable", "accounts_receivable", "cash_bank",
        "fixed_assets", "budgeting", "cost_accounting", "tax_management",
        "financial_reporting", "audit_compliance", "payroll_accounting", "purchase_sales_integration"
    ]
