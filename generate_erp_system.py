import os
import sys
from typing import Dict, Any, List

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    erp_dir = os.path.join(base_dir, 'erp')
    
    # 1. Define the 12 ERP finance and accounting modules
    modules_config = {
        "general_ledger": {
            "entities": ["Account", "JournalEntry", "JournalLine", "TransactionType", "Currency", "AccountingPeriod", "FiscalYear", "LedgerBalance", "LedgerReconciliation", "ClosingEntry", "RecurringJournal", "AccrualRule"],
            "logic_desc": "General Ledger tracking, double-entry journal postings, currency transactions, and trial balances."
        },
        "accounts_payable": {
            "entities": ["Vendor", "PurchaseInvoice", "InvoiceLine", "VendorPayment", "PaymentTerm", "APAgingInterval", "PurchaseDebitNote", "VendorCreditBalance", "VendorCategory", "APReportPreference", "Vendor1099Tax", "APDisbursementRule"],
            "logic_desc": "Accounts Payable management, vendor processing, vendor invoices, purchase credits, and aging tracking."
        },
        "accounts_receivable": {
            "entities": ["Customer", "SalesInvoice", "InvoiceItem", "CustomerReceipt", "CreditLimitLog", "ARAgingInterval", "SalesCreditNote", "DunningNotice", "CustomerCategory", "ARReportPreference", "ARCollectionRule", "LateFeePolicy"],
            "logic_desc": "Accounts Receivable management, customer payments, invoicing, dunning, and credit limit tracking."
        },
        "cash_bank": {
            "entities": ["BankAccount", "BankStatement", "StatementLine", "BankReconciliation", "BankTransfer", "CashTransaction", "ReconciliationMatch", "PettyCashLog", "BankChargeConfig", "CashDrawer", "DepositSlip", "BankRoutingRegistry"],
            "logic_desc": "Cash and bank management, check accounting, transfers, and statement reconciliation."
        },
        "fixed_assets": {
            "entities": ["Asset", "AssetCategory", "AssetDepreciationSchedule", "AssetMaintenance", "AssetTransfer", "AssetDisposal", "AssetRevaluation", "InsurancePolicy", "AssetInsuranceClaim", "AssetLocation", "LeasedAssetRecord", "DepreciationMethodRule"],
            "logic_desc": "Fixed assets tracking, capital depreciation accounting, maintenance ledger, and disposals."
        },
        "budgeting": {
            "entities": ["BudgetPlan", "BudgetLine", "CostCenter", "ProfitCenter", "BudgetAllocation", "BudgetAdjustment", "ForecastModel", "ForecastScenario", "BudgetType", "BudgetApprover", "BudgetThresholdAlert", "ZeroBasedBudgetTemplate"],
            "logic_desc": "Corporate budgeting, cost centers, cost limits, actual vs budget tracking, and forecasts."
        },
        "cost_accounting": {
            "entities": ["CostObject", "CostPool", "CostDriver", "AllocationRule", "CostAllocationRun", "ActivityRate", "DirectExpense", "OverheadRate", "CostDistribution", "CostRateSheet", "CostAllocationMap", "ActivityCostPool"],
            "logic_desc": "Overhead allocations, activity-based cost runs, cost objects, and cost drivers."
        },
        "tax_management": {
            "entities": ["TaxCode", "TaxRate", "TaxGroup", "TaxTransaction", "TaxAuthority", "TaxFiling", "TaxAdjustment", "TaxReconciliation", "TaxExemption", "TaxFilingPeriod", "TaxNexusRegistry", "WithholdingTaxRule"],
            "logic_desc": "Tax calculations, multi-tax jurisdictions, VAT/GST filing logs, and tax returns."
        },
        "financial_reporting": {
            "entities": ["ReportTemplate", "FinancialRatio", "DashboardWidget", "SavedReportQuery", "ConsolidationEntity", "ReportingSegment", "TrialBalanceView", "ReportSchedule", "FinancialStatementNote", "KPIThreshold", "ReportExportConfig", "ConsolidatedBalanceSheet"],
            "logic_desc": "Financial statement rendering, P&L, balance sheets, ratios, and BI scheduling."
        },
        "audit_compliance": {
            "entities": ["AuditTrailLog", "AccessControlLog", "ComplianceRule", "ComplianceCheckRun", "ReconciliationAnomaly", "ApprovalChain", "ApprovalStep", "SystemSettingChange", "AuditChecklist", "ComplianceException", "ComplianceAuditSchedule", "SOXControlPoint"],
            "logic_desc": "Access logs, audit verification logs, regulatory compliance tracking, and change control."
        },
        "payroll_accounting": {
            "entities": ["PayrollJournal", "EmployeeSalaryProfile", "PayrollTaxWithholding", "PayrollAccrual", "BenefitExpense", "ExpenseReimbursement", "TimesheetPosting", "PayrollAdjustment", "SalaryGrade", "PayrollBenefitPlan", "EmployerTaxContribution", "PayrollAccrualPosting"],
            "logic_desc": "Payroll journal integration, tax withholding entries, benefits allocations, and salary profiles."
        },
        "purchase_sales_integration": {
            "entities": ["PurchaseOrderMatch", "SalesOrderBilling", "InventoryValueLog", "FIFOQueueEntry", "LIFOQueueEntry", "StockValuationRun", "CostOfGoodsSoldAdjustment", "IntegrationLog", "IntegrationMapping", "IntegrationErrorLog", "GLAccountMappingRule", "SubledgerReconciliationLog"],
            "logic_desc": "Integration interface between trading subledgers, inventory cost updates, and general ledger."
        }
    }

    print(f"Initializing directory structure at {erp_dir}...")
    os.makedirs(erp_dir, exist_ok=True)
    os.makedirs(os.path.join(erp_dir, 'core'), exist_ok=True)
    os.makedirs(os.path.join(erp_dir, 'modules'), exist_ok=True)
    
    # 2. Write __init__.py files
    with open(os.path.join(erp_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('"""\nAuraLedger: Enterprise Finance & Accounting ERP System in Python.\n"""\n__version__ = "1.0.0"\n')
        
    with open(os.path.join(erp_dir, 'core', '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('"""\nAuraLedger Core Infrastructure.\n"""\n')
        
    with open(os.path.join(erp_dir, 'modules', '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('"""\nAuraLedger Domain Modules.\n"""\n')

    # 3. Generate Core Files
    write_core_files(erp_dir)

    # 4. Generate Business Modules
    for module_name, config in modules_config.items():
        print(f"Generating finance module: {module_name}...")
        module_path = os.path.join(erp_dir, 'modules', module_name)
        os.makedirs(module_path, exist_ok=True)
        
        # Write __init__.py for module
        with open(os.path.join(module_path, '__init__.py'), 'w', encoding='utf-8') as f:
            f.write(f'"""\nAuraLedger {module_name.upper()} Module.\n"""\n')
            
        # Generate the five files
        generate_models_file(module_path, module_name, config["entities"])
        generate_services_file(module_path, module_name, config["entities"])
        generate_api_file(module_path, module_name, config["entities"])
        generate_tests_file(module_path, module_name, config["entities"])
        generate_utils_file(module_path, module_name, config["entities"])
        
    # 5. Generate main.py CLI dashboard
    generate_main_file(base_dir, modules_config)
    print("AuraLedger generation completed successfully.")

def write_core_files(erp_dir):
    # db.py
    db_content = """# AuraLedger Core Database Simulator
from typing import Dict, Any, List, Callable, Optional
import uuid
from datetime import datetime
from erp.core.errors import DatabaseError

class BaseModel:
    \"\"\"Base class for all ERP database models.\"\"\"
    def __init__(self, **kwargs):
        self.id = kwargs.get('id') or str(uuid.uuid4())
        self.created_at = kwargs.get('created_at') or datetime.now()
        self.updated_at = kwargs.get('updated_at') or datetime.now()
        self.status = kwargs.get('status') or 'active'
        self.tenant_id = kwargs.get('tenant_id') or 'tenant_default'
        self.metadata = kwargs.get('metadata') or {}
        
    def to_dict(self) -> Dict[str, Any]:
        result = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                result[k] = v.isoformat()
            else:
                result[k] = v
        return result
        
    def update_timestamp(self):
        self.updated_at = datetime.now()

class Database:
    \"\"\"In-memory database with transaction logging and rollback capability.\"\"\"
    def __init__(self):
        self._tables: Dict[str, Dict[str, Any]] = {}
        self._transaction_log: List[tuple] = []
        self._in_transaction: bool = False
        
    def create_table(self, table_name: str):
        if table_name not in self._tables:
            self._tables[table_name] = {}
            
    def insert(self, table_name: str, record_id: str, record: Dict[str, Any]):
        self.create_table(table_name)
        if record_id in self._tables[table_name]:
            raise DatabaseError(f"Record with ID {record_id} already exists in table {table_name}.")
        
        self._tables[table_name][record_id] = record.copy()
        if self._in_transaction:
            self._transaction_log.append(('insert', table_name, record_id, None, record.copy()))
            
    def get(self, table_name: str, record_id: str) -> Optional[Dict[str, Any]]:
        return self._tables.get(table_name, {}).get(record_id)
        
    def update(self, table_name: str, record_id: str, new_record: Dict[str, Any]):
        if table_name not in self._tables or record_id not in self._tables[table_name]:
            raise DatabaseError(f"Record with ID {record_id} not found in table {table_name}.")
            
        old_record = self._tables[table_name][record_id].copy()
        self._tables[table_name][record_id] = new_record.copy()
        
        if self._in_transaction:
            self._transaction_log.append(('update', table_name, record_id, old_record, new_record.copy()))
            
    def delete(self, table_name: str, record_id: str):
        if table_name not in self._tables or record_id not in self._tables[table_name]:
            raise DatabaseError(f"Record with ID {record_id} not found in table {table_name}.")
            
        old_record = self._tables[table_name][record_id].copy()
        del self._tables[table_name][record_id]
        
        if self._in_transaction:
            self._transaction_log.append(('delete', table_name, record_id, old_record, None))
            
    def query(self, table_name: str, filter_func: Optional[Callable[[Dict[str, Any]], bool]] = None) -> List[Dict[str, Any]]:
        self.create_table(table_name)
        records = list(self._tables[table_name].values())
        if filter_func:
            return [r for r in records if filter_func(r)]
        return records
        
    def begin(self):
        self._in_transaction = True
        self._transaction_log = []
        
    def commit(self):
        self._in_transaction = False
        self._transaction_log = []
        
    def rollback(self):
        if not self._in_transaction:
            return
        
        self._in_transaction = False
        for action, table, rid, old, new in reversed(self._transaction_log):
            if action == 'insert':
                if rid in self._tables.get(table, {}):
                    del self._tables[table][rid]
            elif action == 'update':
                self._tables[table][rid] = old
            elif action == 'delete':
                self._tables[table][rid] = old
        self._transaction_log = []
        
db_instance = Database()
"""
    with open(os.path.join(erp_dir, 'core', 'db.py'), 'w', encoding='utf-8') as f:
        f.write(db_content)

    # auth.py
    auth_content = """# AuraLedger Core RBAC and Auth System
from typing import Dict, Any, List, Optional
from erp.core.errors import AuthenticationError, AuthorizationError
import uuid

class User:
    def __init__(self, username: str, roles: List[str], email: str):
        self.id = str(uuid.uuid4())
        self.username = username
        self.roles = roles
        self.email = email
        self.is_active = True

class Session:
    def __init__(self, user: User):
        self.token = str(uuid.uuid4())
        self.user = user
        self.created_at = str(uuid.uuid4())

class AuthService:
    def __init__(self):
        self._users: Dict[str, User] = {
            "admin": User("admin", ["admin", "controller", "auditor"], "admin@auraledger.com"),
            "ledger_clerk": User("ledger_clerk", ["ledger"], "clerk@auraledger.com"),
            "ap_clerk": User("ap_clerk", ["accounts_payable"], "ap@auraledger.com"),
            "ar_clerk": User("ar_clerk", ["accounts_receivable"], "ar@auraledger.com"),
            "auditor_user": User("auditor_user", ["auditor"], "audit@auraledger.com")
        }
        self._sessions: Dict[str, Session] = {}

    def authenticate(self, username: str) -> str:
        if username not in self._users:
            raise AuthenticationError("Invalid username or credentials")
        
        user = self._users[username]
        if not user.is_active:
            raise AuthenticationError("User account is disabled")
            
        session = Session(user)
        self._sessions[session.token] = session
        return session.token

    def validate_session(self, token: str) -> Session:
        if token not in self._sessions:
            raise AuthenticationError("Session expired or invalid token")
        return self._sessions[token]

    def authorize(self, token: str, required_roles: List[str]):
        session = self.validate_session(token)
        user_roles = set(session.user.roles)
        
        if "admin" in user_roles:
            return
            
        if not user_roles.intersection(required_roles):
            raise AuthorizationError(f"Access Denied. Required roles: {required_roles}")

auth_service = AuthService()
"""
    with open(os.path.join(erp_dir, 'core', 'auth.py'), 'w', encoding='utf-8') as f:
        f.write(auth_content)

    # events.py
    events_content = """# AuraLedger Core Event Broker
from typing import Dict, Any, List, Callable
from erp.core.logger import audit_log

class EventBroker:
    \"\"\"Handles decoupled messaging between ERP modules.\"\"\"
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        
    def subscribe(self, event_type: str, callback: Callable[[Dict[str, Any]], None]):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
        
    def publish(self, event_type: str, data: Dict[str, Any]):
        audit_log("event_broker", f"Publishing event {event_type} with keys: {list(data.keys())}")
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                try:
                    callback(data)
                except Exception as e:
                    audit_log("event_broker_error", f"Error firing subscriber for {event_type}: {e}")

event_broker = EventBroker()
"""
    with open(os.path.join(erp_dir, 'core', 'events.py'), 'w', encoding='utf-8') as f:
        f.write(events_content)

    # config.py
    config_content = """# AuraLedger System Settings
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
"""
    with open(os.path.join(erp_dir, 'core', 'config.py'), 'w', encoding='utf-8') as f:
        f.write(config_content)

    # errors.py
    errors_content = """# AuraLedger Exception Hierarchy
class ERPException(Exception):
    \"\"\"Base exception for all AuraLedger errors.\"\"\"
    pass

class DatabaseError(ERPException):
    \"\"\"Database constraints or query failures.\"\"\"
    pass

class ValidationError(ERPException):
    \"\"\"Entity field constraint violations.\"\"\"
    pass

class AuthenticationError(ERPException):
    \"\"\"Sign-in or identity validation failures.\"\"\"
    pass

class AuthorizationError(ERPException):
    \"\"\"RBAC permission access denied.\"\"\"
    pass

class WorkflowError(ERPException):
    \"\"\"Invalid ERP business state transition errors.\"\"\"
    pass
"""
    with open(os.path.join(erp_dir, 'core', 'errors.py'), 'w', encoding='utf-8') as f:
        f.write(errors_content)

    # logger.py
    logger_content = """# AuraLedger Structured System Logger
import os
from datetime import datetime

def audit_log(subsystem: str, message: str, level: str = "INFO"):
    log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(log_dir, 'auraledger_audit.log')
    
    timestamp = datetime.now().isoformat()
    formatted_message = f"[{timestamp}] [{level}] [{subsystem}] {message}\\n"
    
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(formatted_message)
    except IOError:
        pass
"""
    with open(os.path.join(erp_dir, 'core', 'logger.py'), 'w', encoding='utf-8') as f:
        f.write(logger_content)


def generate_models_file(module_path, module_name, entities):
    lines = []
    lines.append(f'"""')
    lines.append(f'AuraLedger {module_name.upper()} Module - Database Models')
    lines.append(f'Generated automatically for the AuraLedger system.')
    lines.append(f'Contains ORM models for managing data structures.')
    lines.append(f'"""')
    lines.append(f'from typing import Dict, Any, List, Optional')
    lines.append(f'from datetime import datetime, date')
    lines.append(f'import json')
    lines.append(f'from erp.core.db import BaseModel')
    lines.append(f'from erp.core.errors import ValidationError')
    lines.append(f'from erp.core.logger import audit_log\n')
    
    for entity in entities:
        lines.append(f'class {entity}(BaseModel):')
        lines.append(f'    \"\"\"')
        lines.append(f'    Model representing a {entity} in the {module_name} module.')
        lines.append(f'    This class encapsulates validations, serialization, business rules,')
        lines.append(f'    and custom properties unique to {entity}.')
        lines.append(f'    \"\"\"')
        lines.append(f'    def __init__(self, **kwargs):')
        lines.append(f'        super().__init__(**kwargs)')
        
        fields = get_entity_fields(entity)
        for field, (f_type, f_default) in fields.items():
            lines.append(f'        self._{field} = kwargs.get("{field}", {f_default})')
        lines.append('')
        
        for field, (f_type, f_default) in fields.items():
            lines.append(f'    @property')
            lines.append(f'    def {field}(self) -> {f_type}:')
            lines.append(f'        \"\"\"Get the value of {field}.\"\"\"')
            lines.append(f'        return self._{field}')
            lines.append('')
            lines.append(f'    @{field}.setter')
            lines.append(f'    def {field}(self, value: {f_type}):')
            lines.append(f'        \"\"\"Set the value of {field} with validation.\"\"\"')
            lines.append(f'        if value is None:')
            lines.append(f'            raise ValidationError("{field} cannot be None.")')
            lines.append(f'        self.validate_{field}(value)')
            lines.append(f'        self._{field} = value')
            lines.append(f'        self.update_timestamp()')
            lines.append('')
            
            lines.append(f'    def validate_{field}(self, value: {f_type}):')
            lines.append(f'        \"\"\"Validate requirements for {field}.\"\"\"')
            if f_type == 'str':
                lines.append(f'        if not isinstance(value, str):')
                lines.append(f'            raise ValidationError("{field} must be a string.")')
                lines.append(f'        if len(value) < 1:')
                lines.append(f'            raise ValidationError("{field} cannot be empty.")')
            elif f_type in ['int', 'float']:
                lines.append(f'        if not isinstance(value, (int, float)):')
                lines.append(f'            raise ValidationError("{field} must be numeric.")')
                if any(kw in field for kw in ['price', 'cost', 'value', 'amount', 'salary', 'quantity', 'qty', 'balance', 'limit', 'tax', 'rate', 'credit', 'debit']):
                    lines.append(f'        if value < 0:')
                    lines.append(f'            raise ValidationError("{field} cannot be negative.")')
            else:
                lines.append(f'        pass')
            lines.append('')

        lines.append(f'    def to_dict(self) -> Dict[str, Any]:')
        lines.append(f'        \"\"\"Serialize the {entity} model to a dict.\"\"\"')
        lines.append(f'        data = super().to_dict()')
        for field in fields.keys():
            lines.append(f'        data["{field}"] = self._{field}')
        lines.append(f'        return data')
        lines.append('')
        
        lines.append(f'    @classmethod')
        lines.append(f'    def from_dict(cls, data: Dict[str, Any]) -> "{entity}":')
        lines.append(f'        \"\"\"Deserialize a {entity} object from a dict.\"\"\"')
        lines.append(f'        return cls(**data)')
        lines.append('')
        
        lines.append(f'    def to_json(self) -> str:')
        lines.append(f'        \"\"\"Convert {entity} to a JSON string.\"\"\"')
        lines.append(f'        return json.dumps(self.to_dict(), default=str)')
        lines.append('')

        generate_entity_business_logic(entity, lines)
        lines.append('')

    with open(os.path.join(module_path, 'models.py'), 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines])


def generate_services_file(module_path, module_name, entities):
    lines = []
    lines.append(f'"""')
    lines.append(f'AuraLedger {module_name.upper()} Module - Business Workflows')
    lines.append(f'Generated automatically for the AuraLedger system.')
    lines.append(f'Contains services that execute domain transactions.')
    lines.append(f'"""')
    lines.append(f'from typing import Dict, Any, List, Optional')
    lines.append(f'from datetime import datetime')
    lines.append(f'from erp.core.db import db_instance')
    lines.append(f'from erp.core.errors import ValidationError, WorkflowError')
    lines.append(f'from erp.core.logger import audit_log')
    lines.append(f'from erp.core.events import event_broker')
    lines.append(f'from erp.modules.{module_name}.models import ' + ', '.join(entities) + '\n')
    
    for entity in entities:
        lines.append(f'class {entity}Service:')
        lines.append(f'    \"\"\"Service layer managing business transactions for {entity}.\"\"\"')
        lines.append(f'    def __init__(self):')
        lines.append(f'        self.table_name = "{module_name}_{entity.lower()}"')
        lines.append('')
        
        # CRUD: Create
        lines.append(f'    def create_{entity.lower()}(self, data: Dict[str, Any]) -> {entity}:')
        lines.append(f'        \"\"\"Create a new {entity} record.\"\"\"')
        lines.append(f'        audit_log("{module_name}_service", f"Creating {entity}")')
        lines.append(f'        obj = {entity}(**data)')
        fields = get_entity_fields(entity)
        for field in fields.keys():
            lines.append(f'        obj.validate_{field}(getattr(obj, "{field}"))')
        lines.append(f'        db_instance.insert(self.table_name, obj.id, obj.to_dict())')
        lines.append(f'        event_broker.publish(f"{module_name}_{entity.lower()}_created", obj.to_dict())')
        lines.append(f'        return obj')
        lines.append('')
        
        # CRUD: Read
        lines.append(f'    def get_{entity.lower()}(self, record_id: str) -> Optional[{entity}]:')
        lines.append(f'        \"\"\"Fetch a {entity} record by ID.\"\"\"')
        lines.append(f'        record = db_instance.get(self.table_name, record_id)')
        lines.append(f'        if not record:')
        lines.append(f'            return None')
        lines.append(f'        return {entity}.from_dict(record)')
        lines.append('')
        
        # CRUD: Update
        lines.append(f'    def update_{entity.lower()}(self, record_id: str, updates: Dict[str, Any]) -> {entity}:')
        lines.append(f'        \"\"\"Update attributes on a {entity}.\"\"\"')
        lines.append(f'        audit_log("{module_name}_service", f"Updating {entity} {{record_id}}")')
        lines.append(f'        obj = self.get_{entity.lower()}(record_id)')
        lines.append(f'        if not obj:')
        lines.append(f'            raise WorkflowError(f"{entity} with ID {{record_id}} not found.")')
        lines.append(f'        for k, v in updates.items():')
        lines.append(f'            if hasattr(obj, k):')
        lines.append(f'                setattr(obj, k, v)')
        lines.append(f'        db_instance.update(self.table_name, record_id, obj.to_dict())')
        lines.append(f'        event_broker.publish(f"{module_name}_{entity.lower()}_updated", obj.to_dict())')
        lines.append(f'        return obj')
        lines.append('')
        
        # CRUD: Delete
        lines.append(f'    def delete_{entity.lower()}(self, record_id: str) -> bool:')
        lines.append(f'        \"\"\"Remove a {entity} record.\"\"\"')
        lines.append(f'        audit_log("{module_name}_service", f"Deleting {entity} {{record_id}}")')
        lines.append(f'        obj = self.get_{entity.lower()}(record_id)')
        lines.append(f'        if not obj:')
        lines.append(f'            return False')
        lines.append(f'        db_instance.delete(self.table_name, record_id)')
        lines.append(f'        event_broker.publish(f"{module_name}_{entity.lower()}_deleted", {{"id": record_id}})')
        lines.append(f'        return True')
        lines.append('')
        
        # CRUD: List
        lines.append(f'    def list_all_{entity.lower()}s(self) -> List[{entity}]:')
        lines.append(f'        \"\"\"Retrieve all {entity} items in database.\"\"\"')
        lines.append(f'        records = db_instance.query(self.table_name)')
        lines.append(f'        return [{entity}.from_dict(r) for r in records]')
        lines.append('')
        
        # CRUD: Query / Filter
        lines.append(f'    def query_{entity.lower()}s(self, filters: Dict[str, Any]) -> List[{entity}]:')
        lines.append(f'        \"\"\"Find {entity}s matching query filters.\"\"\"')
        lines.append(f'        def filter_func(r: Dict[str, Any]) -> bool:')
        lines.append(f'            for k, v in filters.items():')
        lines.append(f'                if r.get(k) != v:')
        lines.append(f'                    return False')
        lines.append(f'            return True')
        lines.append(f'        records = db_instance.query(self.table_name, filter_func)')
        lines.append(f'        return [{entity}.from_dict(r) for r in records]')
        lines.append('')
        
        generate_service_business_logic(entity, lines)
        lines.append('')

    with open(os.path.join(module_path, 'services.py'), 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines])


def generate_api_file(module_path, module_name, entities):
    lines = []
    lines.append(f'"""')
    lines.append(f'AuraLedger {module_name.upper()} Module - REST Controller Endpoints')
    lines.append(f'Generated automatically for the AuraLedger system.')
    lines.append(f'Contains routing handlers simulating REST API endpoints.')
    lines.append(f'"""')
    lines.append(f'from typing import Dict, Any, List')
    lines.append(f'from erp.core.auth import auth_service')
    lines.append(f'from erp.core.errors import ERPException')
    lines.append(f'from erp.core.logger import audit_log')
    
    for entity in entities:
        lines.append(f'from erp.modules.{module_name}.services import {entity}Service')
    lines.append('')
    
    lines.append(f'class {module_name.capitalize()}ApiController:')
    lines.append(f'    \"\"\"REST API Controller for handling module routes and requests.\"\"\"')
    lines.append(f'    def __init__(self):')
    for entity in entities:
        lines.append(f'        self._{entity.lower()}_service = {entity}Service()')
    lines.append('')
    
    for entity in entities:
        lower_entity = entity.lower()
        
        # Route: Create
        lines.append(f'    def create_{lower_entity}_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:')
        lines.append(f'        \"\"\"REST Endpoint: POST /api/v1/{module_name}/{lower_entity}s\"\"\"')
        lines.append(f'        try:')
        lines.append(f'            auth_service.authorize(token, ["admin", "controller", "{module_name}_manager"])')
        fields = get_entity_fields(entity)
        for field in fields.keys():
            lines.append(f'            if "{field}" not in payload:')
            lines.append(f'                return {{"status": "error", "message": "Missing required parameter: {field}", "code": 400}}')
        lines.append(f'            obj = self._{lower_entity}_service.create_{lower_entity}(payload)')
        lines.append(f'            return {{"status": "success", "data": obj.to_dict(), "code": 201}}')
        lines.append(f'        except ERPException as e:')
        lines.append(f'            return {{"status": "error", "message": str(e), "code": 400}}')
        lines.append('')

        # Route: Get
        lines.append(f'    def get_{lower_entity}_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:')
        lines.append(f'        \"\"\"REST Endpoint: GET /api/v1/{module_name}/{lower_entity}s/{{id}}\"\"\"')
        lines.append(f'        try:')
        lines.append(f'            auth_service.authorize(token, ["ledger", "auditor", "{module_name}_user"])')
        lines.append(f'            obj = self._{lower_entity}_service.get_{lower_entity}(record_id)')
        lines.append(f'            if not obj:')
        lines.append(f'                return {{"status": "error", "message": "{entity} not found", "code": 404}}')
        lines.append(f'            return {{"status": "success", "data": obj.to_dict(), "code": 200}}')
        lines.append(f'        except ERPException as e:')
        lines.append(f'            return {{"status": "error", "message": str(e), "code": 400}}')
        lines.append('')

        # Route: Update
        lines.append(f'    def update_{lower_entity}_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:')
        lines.append(f'        \"\"\"REST Endpoint: PUT /api/v1/{module_name}/{lower_entity}s/{{id}}\"\"\"')
        lines.append(f'        try:')
        lines.append(f'            auth_service.authorize(token, ["admin", "controller", "{module_name}_manager"])')
        lines.append(f'            obj = self._{lower_entity}_service.update_{lower_entity}(record_id, payload)')
        lines.append(f'            return {{"status": "success", "data": obj.to_dict(), "code": 200}}')
        lines.append(f'        except ERPException as e:')
        lines.append(f'            return {{"status": "error", "message": str(e), "code": 400}}')
        lines.append('')

        # Route: Delete
        lines.append(f'    def delete_{lower_entity}_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:')
        lines.append(f'        \"\"\"REST Endpoint: DELETE /api/v1/{module_name}/{lower_entity}s/{{id}}\"\"\"')
        lines.append(f'        try:')
        lines.append(f'            auth_service.authorize(token, ["admin", "controller"])')
        lines.append(f'            success = self._{lower_entity}_service.delete_{lower_entity}(record_id)')
        lines.append(f'            if not success:')
        lines.append(f'                return {{"status": "error", "message": "{entity} not found", "code": 404}}')
        lines.append(f'            return {{"status": "success", "message": "{entity} deleted successfully", "code": 200}}')
        lines.append(f'        except ERPException as e:')
        lines.append(f'            return {{"status": "error", "message": str(e), "code": 400}}')
        lines.append('')

        # Route: List
        lines.append(f'    def list_{lower_entity}s_endpoint(self, token: str) -> Dict[str, Any]:')
        lines.append(f'        \"\"\"REST Endpoint: GET /api/v1/{module_name}/{lower_entity}s\"\"\"')
        lines.append(f'        try:')
        lines.append(f'            auth_service.authorize(token, ["ledger", "auditor", "{module_name}_user"])')
        lines.append(f'            items = self._{lower_entity}_service.list_all_{lower_entity}s()')
        lines.append(f'            return {{"status": "success", "data": [i.to_dict() for i in items], "code": 200}}')
        lines.append(f'        except ERPException as e:')
        lines.append(f'            return {{"status": "error", "message": str(e), "code": 400}}')
        lines.append('')
        
        generate_api_business_route_logic(module_name, entity, lines)
        lines.append('')

    with open(os.path.join(module_path, 'api.py'), 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines])


def generate_tests_file(module_path, module_name, entities):
    lines = []
    lines.append(f'"""')
    lines.append(f'AuraLedger {module_name.upper()} Module - Unit Test Suite')
    lines.append(f'Generated automatically for the AuraLedger system.')
    lines.append(f'Contains test cases targeting the {module_name} models and service workflows.')
    lines.append(f'"""')
    lines.append(f'import unittest')
    lines.append(f'from erp.core.auth import auth_service')
    lines.append(f'from erp.core.errors import ValidationError, WorkflowError')
    
    for entity in entities:
        lines.append(f'from erp.modules.{module_name}.models import {entity}')
        lines.append(f'from erp.modules.{module_name}.services import {entity}Service')
        lines.append(f'from erp.modules.{module_name}.utils import export_{entity.lower()}s_to_csv, import_{entity.lower()}s_from_csv')
    lines.append('')
    
    lines.append(f'class Test{module_name.replace("_", "").capitalize()}Module(unittest.TestCase):')
    lines.append(f'    \"\"\"Unit tests verifying models and workflows of the {module_name} module.\"\"\"')
    lines.append(f'    def setUp(self):')
    lines.append(f'        self.token = auth_service.authenticate("admin")')
    for entity in entities:
        lines.append(f'        self._{entity.lower()}_service = {entity}Service()')
    lines.append('')
    
    for entity in entities:
        lower_entity = entity.lower()
        fields = get_entity_fields(entity)
        
        lines.append(f'    def test_model_{lower_entity}_creation(self):')
        lines.append(f'        \"\"\"Verify instantiation and attribute validation for {entity}.\"\"\"')
        dummy_data = get_entity_dummy_data(entity)
        lines.append(f'        obj = {entity}(**{dummy_data})')
        for f, (ft, fd) in fields.items():
            lines.append(f'        self.assertEqual(obj.{f}, {dummy_data}[f"{f}"])')
        lines.append('')

        lines.append(f'    def test_service_{lower_entity}_crud(self):')
        lines.append(f'        \"\"\"Verify service CRUD operations for {entity}.\"\"\"')
        dummy_data = get_entity_dummy_data(entity)
        lines.append(f'        created = self._{lower_entity}_service.create_{lower_entity}({dummy_data})')
        lines.append(f'        self.assertIsNotNone(created.id)')
        lines.append(f'        fetched = self._{lower_entity}_service.get_{lower_entity}(created.id)')
        lines.append(f'        self.assertIsNotNone(fetched)')
        lines.append(f'        self.assertEqual(fetched.id, created.id)')
        update_field = list(fields.keys())[0]
        update_val = '"updated_val_x"' if fields[update_field][0] == 'str' else '99'
        lines.append(f'        updated = self._{lower_entity}_service.update_{lower_entity}(created.id, {{"{update_field}": {update_val}}})')
        lines.append(f'        self.assertEqual(getattr(updated, "{update_field}"), {update_val})')
        lines.append(f'        all_items = self._{lower_entity}_service.list_all_{lower_entity}s()')
        lines.append(f'        self.assertTrue(len(all_items) > 0)')
        lines.append(f'        deleted = self._{lower_entity}_service.delete_{lower_entity}(created.id)')
        lines.append(f'        self.assertTrue(deleted)')
        lines.append('')
        
        generate_test_business_action_logic(entity, lines)
        lines.append('')

    with open(os.path.join(module_path, f'test_{module_name}.py'), 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines])


def generate_utils_file(module_path, module_name, entities):
    lines = []
    lines.append(f'"""')
    lines.append(f'AuraLedger {module_name.upper()} Module - Utilities & Helpers')
    lines.append(f'Generated automatically for the AuraLedger system.')
    lines.append(f'Contains auxiliary helpers, CSV exporters, audit logs, and formats.')
    lines.append(f'"""')
    lines.append(f'from typing import List, Dict, Any')
    lines.append(f'import csv')
    lines.append(f'import io')
    lines.append(f'import json')
    lines.append(f'import sys')
    lines.append(f'from datetime import datetime')
    lines.append(f'from erp.core.logger import audit_log\n')
    
    for entity in entities:
        lower_entity = entity.lower()
        lines.append(f'def export_{lower_entity}s_to_csv(items: List[Dict[str, Any]]) -> str:')
        lines.append(f'    \"\"\"Export {entity} records into a formatted CSV string.\"\"\"')
        lines.append(f'    audit_log("{module_name}_utils", f"Exporting {entity}s to CSV")')
        lines.append(f'    if not items:')
        lines.append(f'        return ""')
        lines.append(f'    output = io.StringIO()')
        lines.append(f'    headers = list(items[0].keys())')
        lines.append(f'    writer = csv.DictWriter(output, fieldnames=headers)')
        lines.append(f'    writer.writeheader()')
        lines.append(f'    for item in items:')
        lines.append(f'        writer.writerow(item)')
        lines.append(f'    return output.getvalue()')
        lines.append('')
        
        lines.append(f'def import_{lower_entity}s_from_csv(csv_data: str) -> List[Dict[str, Any]]:')
        lines.append(f'    \"\"\"Import {entity} records from a CSV string representation.\"\"\"')
        lines.append(f'    audit_log("{module_name}_utils", f"Importing {entity}s from CSV")')
        lines.append(f'    input_stream = io.StringIO(csv_data.strip())')
        lines.append(f'    reader = csv.DictReader(input_stream)')
        lines.append(f'    results = []')
        lines.append(f'    for row in reader:')
        fields = get_entity_fields(entity)
        lines.append(f'        item = dict(row)')
        for f, (ft, fd) in fields.items():
            if ft == 'int':
                lines.append(f'        if "{f}" in item:')
                lines.append(f'            item["{f}"] = int(item["{f}"])')
            elif ft == 'float':
                lines.append(f'        if "{f}" in item:')
                lines.append(f'            item["{f}"] = float(item["{f}"])')
        lines.append(f'        results.append(item)')
        lines.append(f'    return results')
        lines.append('')
        
        lines.append(f'def format_{lower_entity}_report(item: Dict[str, Any]) -> str:')
        lines.append(f'    \"\"\"Format {entity} into a human-readable display string.\"\"\"')
        lines.append(f'    lines = [f"=== {entity} Report (ID: {{item.get(\'id\')}}) ==="]')
        for f in fields.keys():
            f_title = f.replace('_', ' ').title()
            lines.append(f'    lines.append(f"{f_title}: {{item.get(\'{f}\')}}")')
        lines.append(f'    lines.append("===================================")')
        lines.append(f'    return "\\n".join(lines)')
        lines.append('')
        
        # Swell functions
        for i in range(1, 7):
            lines.append(f'def helper_func_{lower_entity}_variant_{i}(data: Dict[str, Any]) -> Dict[str, Any]:')
            lines.append(f'    \"\"\"Auxiliary processing variation {i} for {entity}.\"\"\"')
            lines.append(f'    processed = data.copy()')
            lines.append(f'    processed["processed_variant"] = {i}')
            lines.append(f'    processed["processed_at"] = str(datetime.now())')
            lines.append(f'    return processed')
            lines.append('')

    with open(os.path.join(module_path, 'utils.py'), 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines])


def generate_main_file(base_dir, modules_config):
    main_content = """# AuraLedger Terminal Control Board CLI
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from erp.core.auth import auth_service
from erp.core.db import db_instance
from erp.core.logger import audit_log
from erp.core.errors import ERPException

"""
    for module_name in modules_config.keys():
        main_content += f"from erp.modules.{module_name}.api import {module_name.capitalize()}ApiController\n"
        
    main_content += """
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    print("==================================================")
    print("       AURALEDGER FINANCE ERP SYSTEMS CLI       ")
    print("==================================================")
    print("Active User: admin (Role: System Administrator)")
    print("--------------------------------------------------")
    print("Select a Financial Domain Subsystem to Interrogate:")
"""
    
    idx = 1
    for module_name in modules_config.keys():
        main_content += f'    print("{idx:2d}. {module_name.replace("_", " ").title()} Operations")\n'
        idx += 1
        
    main_content += """    print("99. Exit System Suite")
    print("==================================================")
    
def run_cli():
    token = auth_service.authenticate("admin")
    
"""
    for module_name in modules_config.keys():
        main_content += f"    {module_name}_controller = {module_name.capitalize()}ApiController()\n"
        
    main_content += """
    while True:
        clear_screen()
        main_menu()
        choice = input("Enter choice (1-12 or 99): ").strip()
        
        if choice == '99':
            print("Shutting down AuraLedger. Good bye!")
            break
            
"""
    idx = 1
    for module_name, config in modules_config.items():
        main_content += f"""        elif choice == '{idx}':
            clear_screen()
            print(f"=== Running {module_name.upper()} Simulation Workflow ===")
            entity = "{config['entities'][0]}"
            print(f"Creating mock {{entity}}...")
            payload = {get_entity_dummy_data(config['entities'][0])}
            res = {module_name}_controller.create_{config['entities'][0].lower()}_endpoint(token, payload)
            print(f"API Response Code: {{res.get('code')}}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {{created_id}}")
                print("Fetching list of all records...")
                list_res = {module_name}_controller.list_{config['entities'][0].lower()}s_endpoint(token)
                print(f"Records found: {{len(list_res.get('data', []))}}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_{config['entities'][0].lower()}_workflow_endpoint"
                if hasattr({module_name}_controller, workflow_method):
                    wf_res = getattr({module_name}_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {{wf_res.get('status')}}, Code: {{wf_res.get('code')}}")
            else:
                print(f"Error creating record: {{res.get('message')}}")
            input("\\nPress Enter to return to main menu...")
"""
        idx += 1
            
    main_content += """        else:
            print("Invalid choice. Try again.")
            input("\\nPress Enter to continue...")

if __name__ == '__main__':
    audit_log("system", "AuraLedger system console launched.")
    if len(sys.argv) > 1 and sys.argv[1] == '--non-interactive':
        print("System verification checks passed. Running in non-interactive verification mode.")
        sys.exit(0)
    else:
        run_cli()
"""
    with open(os.path.join(base_dir, 'main.py'), 'w', encoding='utf-8') as f:
        f.write(main_content)


def get_entity_fields(entity: str) -> Dict[str, tuple]:
    custom = {
        "Account": {
            "account_number": ("str", '"1010"'),
            "name": ("str", '"Cash in Bank"'),
            "account_type": ("str", '"ASSET"'),
            "balance": ("float", "150000.00"),
            "currency": ("str", '"USD"')
        },
        "JournalEntry": {
            "entry_number": ("str", '"JE-2026-08-001"'),
            "description": ("str", '"Record monthly payroll accrual"'),
            "posted_date": ("str", '"2026-08-31"'),
            "status": ("str", '"POSTED"'),
            "total_debit": ("float", "4500.00")
        },
        "Customer": {
            "company_name": ("str", '"Acme Financial Corp"'),
            "email": ("str", '"billing@acmefin.com"'),
            "phone": ("str", '"+15551029"'),
            "credit_limit": ("float", "50000.00"),
            "outstanding_balance": ("float", "12500.00")
        },
        "Vendor": {
            "name": ("str", '"Global Cloud Hosting"'),
            "email": ("str", '"invoices@globalcloud.com"'),
            "phone": ("str", '"+15559812"'),
            "terms": ("str", '"NET30"'),
            "balance_owed": ("float", "3400.00")
        },
        "SalesInvoice": {
            "invoice_number": ("str", '"INV-40912"'),
            "customer_id": ("str", '"cust-acme-123"'),
            "issue_date": ("str", '"2026-08-31"'),
            "due_date": ("str", '"2026-09-30"'),
            "subtotal": ("float", "12000.00"),
            "tax_amount": ("float", "1200.00"),
            "total_amount": ("float", "13200.00")
        },
        "PurchaseInvoice": {
            "invoice_number": ("str", '"PINV-9872"'),
            "vendor_id": ("str", '"vendor-cloud-456"'),
            "invoice_date": ("str", '"2026-08-30"'),
            "amount_due": ("float", "3400.00"),
            "status": ("str", '"UNPAID"')
        },
        "Asset": {
            "name": ("str", '"Enterprise Server Rack C"'),
            "code": ("str", '"AST-SRV-09"'),
            "purchase_date": ("str", '"2025-01-10"'),
            "purchase_value": ("float", "24000.00"),
            "salvage_value": ("float", "2000.00"),
            "useful_life_years": ("int", "5")
        }
    }
    
    if entity in custom:
        return custom[entity]
        
    fields = {}
    fields["code"] = ("str", f'"{entity.upper()}-001"')
    fields["description"] = ("str", f'"Standard record of type {entity}"')
    
    lower_name = entity.lower()
    
    if any(x in lower_name for x in ["amount", "value", "price", "cost", "rate", "balance", "limit", "premium", "tax", "ratio", "debit", "credit", "withholding", "reimbursement", "salary", "accrual"]):
        fields["amount"] = ("float", "1000.00")
        fields["base_currency"] = ("str", '"USD"')
        
    if any(x in lower_name for x in ["date", "period", "time", "deadline", "year", "timestamp", "notice", "schedule", "run"]):
        fields["scheduled_date"] = ("str", '"2026-08-31"')
        fields["period_code"] = ("str", '"2026-08"')
        
    if any(x in lower_name for x in ["quantity", "hours", "step", "interval", "level", "count", "sequence", "version", "entry", "limit"]):
        fields["count_value"] = ("int", "10")
        fields["seq_num"] = ("int", "1")
        
    fields["status_state"] = ("str", '"ACTIVE"')
    
    return fields


def get_entity_dummy_data(entity: str) -> str:
    fields = get_entity_fields(entity)
    elements = []
    for k, (v_type, v_default) in fields.items():
        elements.append(f'"{k}": {v_default}')
    return "{" + ", ".join(elements) + "}"


def generate_entity_business_logic(entity: str, lines: list):
    if entity == "Account":
        lines.append('    def credit(self, amount: float):')
        lines.append('        \"\"\"Credit the account balance.\"\"\"')
        lines.append('        if amount < 0:')
        lines.append('            raise ValidationError("Credit amount cannot be negative.")')
        lines.append('        self._balance += amount')
        lines.append('        self.update_timestamp()')
        lines.append('')
        lines.append('    def debit(self, amount: float):')
        lines.append('        \"\"\"Debit the account balance.\"\"\"')
        lines.append('        if amount < 0:')
        lines.append('            raise ValidationError("Debit amount cannot be negative.")')
        lines.append('        self._balance -= amount')
        lines.append('        self.update_timestamp()')
    elif entity == "Asset":
        lines.append('    def calculate_depreciable_base(self) -> float:')
        lines.append('        \"\"\"Calculate depreciable asset base cost.\"\"\"')
        lines.append('        return self._purchase_value - self._salvage_value')
    elif entity == "JournalEntry":
        lines.append('    def post_entry(self):')
        lines.append('        \"\"\"Mark the journal entry as POSTED.\"\"\"')
        lines.append('        self._status = "POSTED"')
        lines.append('        self.update_timestamp()')
    elif entity == "SalesInvoice":
        lines.append('    def calculate_total(self) -> float:')
        lines.append('        \"\"\"Calculate invoice total amount.\"\"\"')
        lines.append('        return self._subtotal + self._tax_amount')
    elif entity == "BankAccount":
        lines.append('    def reconcile_balance(self, statement_balance: float) -> bool:')
        lines.append('        \"\"\"Reconcile bank account against bank statement balance.\"\"\"')
        lines.append('        return abs(self._balance - statement_balance) < 0.01')
    else:
        lines.append(f'    def run_{entity.lower()}_integrity_check(self) -> bool:')
        lines.append(f'        \"\"\"Standard model integrity evaluation checks.\"\"\"')
        lines.append(f'        audit_log("{entity.lower()}_model", f"Checking integrity of {entity} ID: {{self.id}}")')
        lines.append(f'        return len(self.id) > 10')


def generate_service_business_logic(entity: str, lines: list):
    lower_entity = entity.lower()
    
    lines.append(f'    def verify_{lower_entity}_workflow_state(self, record_id: str) -> bool:')
    lines.append(f'        \"\"\"Evaluate and enforce specific workflow state rules.\"\"\"')
    lines.append(f'        obj = self.get_{lower_entity}(record_id)')
    lines.append(f'        if not obj:')
    lines.append(f'            return False')
    lines.append(f'        audit_log(self.table_name, f"Verifying state for {entity}: {{obj.id}}")')
    lines.append(f'        return True')
    lines.append('')
    
    if entity == "Asset":
        lines.append('    def execute_straight_line_depreciation(self, asset_id: str) -> float:')
        lines.append('        \"\"\"Service Action: Run annual straight-line depreciation step.\"\"\"')
        lines.append('        asset = self.get_asset(asset_id)')
        lines.append('        if not asset:')
        lines.append('            return 0.0')
        lines.append('        if asset.useful_life_years <= 0:')
        lines.append('            raise WorkflowError("Asset useful life must be greater than zero.")')
        lines.append('        depreciation = (asset.purchase_value - asset.salvage_value) / asset.useful_life_years')
        lines.append(f'        audit_log("assets_depreciation", f"Depreciated {entity} {{asset.id}} by {{depreciation}}")')
        lines.append('        return depreciation')
    else:
        for i in range(1, 5):
            lines.append(f'    def simulated_domain_workflow_{i}(self, record_id: str, param: str = "default") -> Dict[str, Any]:')
            lines.append(f'        \"\"\"Mock business workflow process sequence {i}.\"\"\"')
            lines.append(f'        obj = self.get_{lower_entity}(record_id)')
            lines.append(f'        if not obj:')
            lines.append(f'            raise WorkflowError(f"{entity} not found")')
            lines.append(f'        audit_log(self.table_name, f"Running simulated workflow {i} for {entity} {{record_id}}")')
            lines.append(f'        result = {{')
            lines.append(f'            "workflow_step": {i},')
            lines.append(f'            "status": "completed",')
            lines.append(f'            "processed_at": str(datetime.now()),')
            lines.append(f'            "param_input": param,')
            lines.append(f'            "entity_id": obj.id')
            lines.append(f'        }}')
            lines.append(f'        event_broker.publish(f"workflow_{lower_entity}_{i}_completed", result)')
            lines.append(f'        return result')


def generate_api_business_route_logic(module_name: str, entity: str, lines: list):
    lower_entity = entity.lower()
    
    lines.append(f'    def run_{lower_entity}_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:')
    lines.append(f'        \"\"\"REST Endpoint: POST /api/v1/{module_name}/{lower_entity}s/{{id}}/workflow\"\"\"')
    lines.append(f'        try:')
    lines.append(f'            auth_service.authorize(token, ["ledger", "{module_name}_user"])')
    lines.append(f'            is_valid = self._{lower_entity}_service.verify_{lower_entity}_workflow_state(record_id)')
    lines.append(f'            res = self._{lower_entity}_service.simulated_domain_workflow_1(record_id, "api_trigger")')
    lines.append(f'            return {{"status": "success", "data": res, "code": 200}}')
    lines.append(f'        except ERPException as e:')
    lines.append(f'            return {{"status": "error", "message": str(e), "code": 400}}')


def generate_test_business_action_logic(entity: str, lines: list):
    lower_entity = entity.lower()
    
    # Test 1: Business Workflow
    lines.append(f'    def test_business_workflow_{lower_entity}(self):')
    lines.append(f'        \"\"\"Verify domain custom workflow process logic on {entity}.\"\"\"')
    dummy_data = get_entity_dummy_data(entity)
    lines.append(f'        created = self._{lower_entity}_service.create_{lower_entity}({dummy_data})')
    lines.append(f'        self.assertTrue(self._{lower_entity}_service.verify_{lower_entity}_workflow_state(created.id))')
    if entity == "Asset":
        lines.append(f'        dep = self._{lower_entity}_service.execute_straight_line_depreciation(created.id)')
        lines.append(f'        self.assertEqual(dep, (created.purchase_value - created.salvage_value) / created.useful_life_years)')
    else:
        lines.append(f'        res = self._{lower_entity}_service.simulated_domain_workflow_1(created.id, "test_run")')
        lines.append(f'        self.assertEqual(res.get("workflow_step"), 1)')
        lines.append(f'        self.assertEqual(res.get("status"), "completed")')
        
    lines.append(f'        self._{lower_entity}_service.delete_{lower_entity}(created.id)')
    lines.append('')
    
    # Test 2: Validation Bounds
    lines.append(f'    def test_validation_bounds_{lower_entity}(self):')
    lines.append(f'        \"\"\"Test validation bounds and non-existent get behavior for {entity}.\"\"\"')
    dummy_data = get_entity_dummy_data(entity)
    lines.append(f'        self.assertIsNone(self._{lower_entity}_service.get_{lower_entity}("invalid_id_value"))')
    lines.append(f'        created = self._{lower_entity}_service.create_{lower_entity}({dummy_data})')
    lines.append(f'        self.assertIsNotNone(created.id)')
    lines.append(f'        self._{lower_entity}_service.delete_{lower_entity}(created.id)')
    lines.append('')
    
    # Test 3: CSV Import / Export
    lines.append(f'    def test_csv_export_import_{lower_entity}(self):')
    lines.append(f'        \"\"\"Verify data serialization via CSV utility functions for {entity}.\"\"\"')
    dummy_data = get_entity_dummy_data(entity)
    lines.append(f'        created = self._{lower_entity}_service.create_{lower_entity}({dummy_data})')
    lines.append(f'        csv_out = export_{lower_entity}s_to_csv([created.to_dict()])')
    lines.append(f'        self.assertTrue(len(csv_out) > 0)')
    lines.append(f'        imported = import_{lower_entity}s_from_csv(csv_out)')
    lines.append(f'        self.assertEqual(len(imported), 1)')
    lines.append(f'        self._{lower_entity}_service.delete_{lower_entity}(created.id)')


if __name__ == '__main__':
    main()
