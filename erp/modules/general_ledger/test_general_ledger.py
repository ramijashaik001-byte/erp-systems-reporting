"""
AuraLedger GENERAL_LEDGER Module - Unit Test Suite
Generated automatically for the AuraLedger system.
Contains test cases targeting the general_ledger models and service workflows.
"""
import unittest
from erp.core.auth import auth_service
from erp.core.errors import ValidationError, WorkflowError
from erp.modules.general_ledger.models import Account
from erp.modules.general_ledger.services import AccountService
from erp.modules.general_ledger.utils import export_accounts_to_csv, import_accounts_from_csv
from erp.modules.general_ledger.models import JournalEntry
from erp.modules.general_ledger.services import JournalEntryService
from erp.modules.general_ledger.utils import export_journalentrys_to_csv, import_journalentrys_from_csv
from erp.modules.general_ledger.models import JournalLine
from erp.modules.general_ledger.services import JournalLineService
from erp.modules.general_ledger.utils import export_journallines_to_csv, import_journallines_from_csv
from erp.modules.general_ledger.models import TransactionType
from erp.modules.general_ledger.services import TransactionTypeService
from erp.modules.general_ledger.utils import export_transactiontypes_to_csv, import_transactiontypes_from_csv
from erp.modules.general_ledger.models import Currency
from erp.modules.general_ledger.services import CurrencyService
from erp.modules.general_ledger.utils import export_currencys_to_csv, import_currencys_from_csv
from erp.modules.general_ledger.models import AccountingPeriod
from erp.modules.general_ledger.services import AccountingPeriodService
from erp.modules.general_ledger.utils import export_accountingperiods_to_csv, import_accountingperiods_from_csv
from erp.modules.general_ledger.models import FiscalYear
from erp.modules.general_ledger.services import FiscalYearService
from erp.modules.general_ledger.utils import export_fiscalyears_to_csv, import_fiscalyears_from_csv
from erp.modules.general_ledger.models import LedgerBalance
from erp.modules.general_ledger.services import LedgerBalanceService
from erp.modules.general_ledger.utils import export_ledgerbalances_to_csv, import_ledgerbalances_from_csv
from erp.modules.general_ledger.models import LedgerReconciliation
from erp.modules.general_ledger.services import LedgerReconciliationService
from erp.modules.general_ledger.utils import export_ledgerreconciliations_to_csv, import_ledgerreconciliations_from_csv
from erp.modules.general_ledger.models import ClosingEntry
from erp.modules.general_ledger.services import ClosingEntryService
from erp.modules.general_ledger.utils import export_closingentrys_to_csv, import_closingentrys_from_csv
from erp.modules.general_ledger.models import RecurringJournal
from erp.modules.general_ledger.services import RecurringJournalService
from erp.modules.general_ledger.utils import export_recurringjournals_to_csv, import_recurringjournals_from_csv
from erp.modules.general_ledger.models import AccrualRule
from erp.modules.general_ledger.services import AccrualRuleService
from erp.modules.general_ledger.utils import export_accrualrules_to_csv, import_accrualrules_from_csv

class TestGeneralledgerModule(unittest.TestCase):
    """Unit tests verifying models and workflows of the general_ledger module."""
    def setUp(self):
        self.token = auth_service.authenticate("admin")
        self._account_service = AccountService()
        self._journalentry_service = JournalEntryService()
        self._journalline_service = JournalLineService()
        self._transactiontype_service = TransactionTypeService()
        self._currency_service = CurrencyService()
        self._accountingperiod_service = AccountingPeriodService()
        self._fiscalyear_service = FiscalYearService()
        self._ledgerbalance_service = LedgerBalanceService()
        self._ledgerreconciliation_service = LedgerReconciliationService()
        self._closingentry_service = ClosingEntryService()
        self._recurringjournal_service = RecurringJournalService()
        self._accrualrule_service = AccrualRuleService()

    def test_model_account_creation(self):
        """Verify instantiation and attribute validation for Account."""
        obj = Account(**{"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"})
        self.assertEqual(obj.account_number, {"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"}[f"account_number"])
        self.assertEqual(obj.name, {"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"}[f"name"])
        self.assertEqual(obj.account_type, {"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"}[f"account_type"])
        self.assertEqual(obj.balance, {"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"}[f"balance"])
        self.assertEqual(obj.currency, {"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"}[f"currency"])

    def test_service_account_crud(self):
        """Verify service CRUD operations for Account."""
        created = self._account_service.create_account({"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"})
        self.assertIsNotNone(created.id)
        fetched = self._account_service.get_account(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._account_service.update_account(created.id, {"account_number": "updated_val_x"})
        self.assertEqual(getattr(updated, "account_number"), "updated_val_x")
        all_items = self._account_service.list_all_accounts()
        self.assertTrue(len(all_items) > 0)
        deleted = self._account_service.delete_account(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_account(self):
        """Verify domain custom workflow process logic on Account."""
        created = self._account_service.create_account({"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"})
        self.assertTrue(self._account_service.verify_account_workflow_state(created.id))
        res = self._account_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._account_service.delete_account(created.id)

    def test_validation_bounds_account(self):
        """Test validation bounds and non-existent get behavior for Account."""
        self.assertIsNone(self._account_service.get_account("invalid_id_value"))
        created = self._account_service.create_account({"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"})
        self.assertIsNotNone(created.id)
        self._account_service.delete_account(created.id)

    def test_csv_export_import_account(self):
        """Verify data serialization via CSV utility functions for Account."""
        created = self._account_service.create_account({"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"})
        csv_out = export_accounts_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_accounts_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._account_service.delete_account(created.id)

    def test_model_journalentry_creation(self):
        """Verify instantiation and attribute validation for JournalEntry."""
        obj = JournalEntry(**{"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00})
        self.assertEqual(obj.entry_number, {"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00}[f"entry_number"])
        self.assertEqual(obj.description, {"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00}[f"description"])
        self.assertEqual(obj.posted_date, {"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00}[f"posted_date"])
        self.assertEqual(obj.status, {"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00}[f"status"])
        self.assertEqual(obj.total_debit, {"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00}[f"total_debit"])

    def test_service_journalentry_crud(self):
        """Verify service CRUD operations for JournalEntry."""
        created = self._journalentry_service.create_journalentry({"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00})
        self.assertIsNotNone(created.id)
        fetched = self._journalentry_service.get_journalentry(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._journalentry_service.update_journalentry(created.id, {"entry_number": "updated_val_x"})
        self.assertEqual(getattr(updated, "entry_number"), "updated_val_x")
        all_items = self._journalentry_service.list_all_journalentrys()
        self.assertTrue(len(all_items) > 0)
        deleted = self._journalentry_service.delete_journalentry(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_journalentry(self):
        """Verify domain custom workflow process logic on JournalEntry."""
        created = self._journalentry_service.create_journalentry({"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00})
        self.assertTrue(self._journalentry_service.verify_journalentry_workflow_state(created.id))
        res = self._journalentry_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._journalentry_service.delete_journalentry(created.id)

    def test_validation_bounds_journalentry(self):
        """Test validation bounds and non-existent get behavior for JournalEntry."""
        self.assertIsNone(self._journalentry_service.get_journalentry("invalid_id_value"))
        created = self._journalentry_service.create_journalentry({"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00})
        self.assertIsNotNone(created.id)
        self._journalentry_service.delete_journalentry(created.id)

    def test_csv_export_import_journalentry(self):
        """Verify data serialization via CSV utility functions for JournalEntry."""
        created = self._journalentry_service.create_journalentry({"entry_number": "JE-2026-08-001", "description": "Record monthly payroll accrual", "posted_date": "2026-08-31", "status": "POSTED", "total_debit": 4500.00})
        csv_out = export_journalentrys_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_journalentrys_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._journalentry_service.delete_journalentry(created.id)

    def test_model_journalline_creation(self):
        """Verify instantiation and attribute validation for JournalLine."""
        obj = JournalLine(**{"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.status_state, {"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_journalline_crud(self):
        """Verify service CRUD operations for JournalLine."""
        created = self._journalline_service.create_journalline({"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._journalline_service.get_journalline(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._journalline_service.update_journalline(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._journalline_service.list_all_journallines()
        self.assertTrue(len(all_items) > 0)
        deleted = self._journalline_service.delete_journalline(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_journalline(self):
        """Verify domain custom workflow process logic on JournalLine."""
        created = self._journalline_service.create_journalline({"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"})
        self.assertTrue(self._journalline_service.verify_journalline_workflow_state(created.id))
        res = self._journalline_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._journalline_service.delete_journalline(created.id)

    def test_validation_bounds_journalline(self):
        """Test validation bounds and non-existent get behavior for JournalLine."""
        self.assertIsNone(self._journalline_service.get_journalline("invalid_id_value"))
        created = self._journalline_service.create_journalline({"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._journalline_service.delete_journalline(created.id)

    def test_csv_export_import_journalline(self):
        """Verify data serialization via CSV utility functions for JournalLine."""
        created = self._journalline_service.create_journalline({"code": "JOURNALLINE-001", "description": "Standard record of type JournalLine", "status_state": "ACTIVE"})
        csv_out = export_journallines_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_journallines_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._journalline_service.delete_journalline(created.id)

    def test_model_transactiontype_creation(self):
        """Verify instantiation and attribute validation for TransactionType."""
        obj = TransactionType(**{"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.status_state, {"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_transactiontype_crud(self):
        """Verify service CRUD operations for TransactionType."""
        created = self._transactiontype_service.create_transactiontype({"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._transactiontype_service.get_transactiontype(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._transactiontype_service.update_transactiontype(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._transactiontype_service.list_all_transactiontypes()
        self.assertTrue(len(all_items) > 0)
        deleted = self._transactiontype_service.delete_transactiontype(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_transactiontype(self):
        """Verify domain custom workflow process logic on TransactionType."""
        created = self._transactiontype_service.create_transactiontype({"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"})
        self.assertTrue(self._transactiontype_service.verify_transactiontype_workflow_state(created.id))
        res = self._transactiontype_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._transactiontype_service.delete_transactiontype(created.id)

    def test_validation_bounds_transactiontype(self):
        """Test validation bounds and non-existent get behavior for TransactionType."""
        self.assertIsNone(self._transactiontype_service.get_transactiontype("invalid_id_value"))
        created = self._transactiontype_service.create_transactiontype({"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._transactiontype_service.delete_transactiontype(created.id)

    def test_csv_export_import_transactiontype(self):
        """Verify data serialization via CSV utility functions for TransactionType."""
        created = self._transactiontype_service.create_transactiontype({"code": "TRANSACTIONTYPE-001", "description": "Standard record of type TransactionType", "status_state": "ACTIVE"})
        csv_out = export_transactiontypes_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_transactiontypes_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._transactiontype_service.delete_transactiontype(created.id)

    def test_model_currency_creation(self):
        """Verify instantiation and attribute validation for Currency."""
        obj = Currency(**{"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.status_state, {"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_currency_crud(self):
        """Verify service CRUD operations for Currency."""
        created = self._currency_service.create_currency({"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._currency_service.get_currency(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._currency_service.update_currency(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._currency_service.list_all_currencys()
        self.assertTrue(len(all_items) > 0)
        deleted = self._currency_service.delete_currency(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_currency(self):
        """Verify domain custom workflow process logic on Currency."""
        created = self._currency_service.create_currency({"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"})
        self.assertTrue(self._currency_service.verify_currency_workflow_state(created.id))
        res = self._currency_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._currency_service.delete_currency(created.id)

    def test_validation_bounds_currency(self):
        """Test validation bounds and non-existent get behavior for Currency."""
        self.assertIsNone(self._currency_service.get_currency("invalid_id_value"))
        created = self._currency_service.create_currency({"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._currency_service.delete_currency(created.id)

    def test_csv_export_import_currency(self):
        """Verify data serialization via CSV utility functions for Currency."""
        created = self._currency_service.create_currency({"code": "CURRENCY-001", "description": "Standard record of type Currency", "status_state": "ACTIVE"})
        csv_out = export_currencys_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_currencys_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._currency_service.delete_currency(created.id)

    def test_model_accountingperiod_creation(self):
        """Verify instantiation and attribute validation for AccountingPeriod."""
        obj = AccountingPeriod(**{"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.scheduled_date, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"scheduled_date"])
        self.assertEqual(obj.period_code, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"period_code"])
        self.assertEqual(obj.count_value, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"count_value"])
        self.assertEqual(obj.seq_num, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"seq_num"])
        self.assertEqual(obj.status_state, {"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"status_state"])

    def test_service_accountingperiod_crud(self):
        """Verify service CRUD operations for AccountingPeriod."""
        created = self._accountingperiod_service.create_accountingperiod({"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._accountingperiod_service.get_accountingperiod(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._accountingperiod_service.update_accountingperiod(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._accountingperiod_service.list_all_accountingperiods()
        self.assertTrue(len(all_items) > 0)
        deleted = self._accountingperiod_service.delete_accountingperiod(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_accountingperiod(self):
        """Verify domain custom workflow process logic on AccountingPeriod."""
        created = self._accountingperiod_service.create_accountingperiod({"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertTrue(self._accountingperiod_service.verify_accountingperiod_workflow_state(created.id))
        res = self._accountingperiod_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._accountingperiod_service.delete_accountingperiod(created.id)

    def test_validation_bounds_accountingperiod(self):
        """Test validation bounds and non-existent get behavior for AccountingPeriod."""
        self.assertIsNone(self._accountingperiod_service.get_accountingperiod("invalid_id_value"))
        created = self._accountingperiod_service.create_accountingperiod({"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._accountingperiod_service.delete_accountingperiod(created.id)

    def test_csv_export_import_accountingperiod(self):
        """Verify data serialization via CSV utility functions for AccountingPeriod."""
        created = self._accountingperiod_service.create_accountingperiod({"code": "ACCOUNTINGPERIOD-001", "description": "Standard record of type AccountingPeriod", "scheduled_date": "2026-08-31", "period_code": "2026-08", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        csv_out = export_accountingperiods_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_accountingperiods_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._accountingperiod_service.delete_accountingperiod(created.id)

    def test_model_fiscalyear_creation(self):
        """Verify instantiation and attribute validation for FiscalYear."""
        obj = FiscalYear(**{"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.scheduled_date, {"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"}[f"scheduled_date"])
        self.assertEqual(obj.period_code, {"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"}[f"period_code"])
        self.assertEqual(obj.status_state, {"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_fiscalyear_crud(self):
        """Verify service CRUD operations for FiscalYear."""
        created = self._fiscalyear_service.create_fiscalyear({"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._fiscalyear_service.get_fiscalyear(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._fiscalyear_service.update_fiscalyear(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._fiscalyear_service.list_all_fiscalyears()
        self.assertTrue(len(all_items) > 0)
        deleted = self._fiscalyear_service.delete_fiscalyear(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_fiscalyear(self):
        """Verify domain custom workflow process logic on FiscalYear."""
        created = self._fiscalyear_service.create_fiscalyear({"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"})
        self.assertTrue(self._fiscalyear_service.verify_fiscalyear_workflow_state(created.id))
        res = self._fiscalyear_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._fiscalyear_service.delete_fiscalyear(created.id)

    def test_validation_bounds_fiscalyear(self):
        """Test validation bounds and non-existent get behavior for FiscalYear."""
        self.assertIsNone(self._fiscalyear_service.get_fiscalyear("invalid_id_value"))
        created = self._fiscalyear_service.create_fiscalyear({"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._fiscalyear_service.delete_fiscalyear(created.id)

    def test_csv_export_import_fiscalyear(self):
        """Verify data serialization via CSV utility functions for FiscalYear."""
        created = self._fiscalyear_service.create_fiscalyear({"code": "FISCALYEAR-001", "description": "Standard record of type FiscalYear", "scheduled_date": "2026-08-31", "period_code": "2026-08", "status_state": "ACTIVE"})
        csv_out = export_fiscalyears_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_fiscalyears_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._fiscalyear_service.delete_fiscalyear(created.id)

    def test_model_ledgerbalance_creation(self):
        """Verify instantiation and attribute validation for LedgerBalance."""
        obj = LedgerBalance(**{"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.amount, {"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"amount"])
        self.assertEqual(obj.base_currency, {"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"base_currency"])
        self.assertEqual(obj.status_state, {"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_ledgerbalance_crud(self):
        """Verify service CRUD operations for LedgerBalance."""
        created = self._ledgerbalance_service.create_ledgerbalance({"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._ledgerbalance_service.get_ledgerbalance(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._ledgerbalance_service.update_ledgerbalance(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._ledgerbalance_service.list_all_ledgerbalances()
        self.assertTrue(len(all_items) > 0)
        deleted = self._ledgerbalance_service.delete_ledgerbalance(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_ledgerbalance(self):
        """Verify domain custom workflow process logic on LedgerBalance."""
        created = self._ledgerbalance_service.create_ledgerbalance({"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertTrue(self._ledgerbalance_service.verify_ledgerbalance_workflow_state(created.id))
        res = self._ledgerbalance_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._ledgerbalance_service.delete_ledgerbalance(created.id)

    def test_validation_bounds_ledgerbalance(self):
        """Test validation bounds and non-existent get behavior for LedgerBalance."""
        self.assertIsNone(self._ledgerbalance_service.get_ledgerbalance("invalid_id_value"))
        created = self._ledgerbalance_service.create_ledgerbalance({"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._ledgerbalance_service.delete_ledgerbalance(created.id)

    def test_csv_export_import_ledgerbalance(self):
        """Verify data serialization via CSV utility functions for LedgerBalance."""
        created = self._ledgerbalance_service.create_ledgerbalance({"code": "LEDGERBALANCE-001", "description": "Standard record of type LedgerBalance", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        csv_out = export_ledgerbalances_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_ledgerbalances_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._ledgerbalance_service.delete_ledgerbalance(created.id)

    def test_model_ledgerreconciliation_creation(self):
        """Verify instantiation and attribute validation for LedgerReconciliation."""
        obj = LedgerReconciliation(**{"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.status_state, {"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_ledgerreconciliation_crud(self):
        """Verify service CRUD operations for LedgerReconciliation."""
        created = self._ledgerreconciliation_service.create_ledgerreconciliation({"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._ledgerreconciliation_service.get_ledgerreconciliation(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._ledgerreconciliation_service.update_ledgerreconciliation(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._ledgerreconciliation_service.list_all_ledgerreconciliations()
        self.assertTrue(len(all_items) > 0)
        deleted = self._ledgerreconciliation_service.delete_ledgerreconciliation(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_ledgerreconciliation(self):
        """Verify domain custom workflow process logic on LedgerReconciliation."""
        created = self._ledgerreconciliation_service.create_ledgerreconciliation({"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"})
        self.assertTrue(self._ledgerreconciliation_service.verify_ledgerreconciliation_workflow_state(created.id))
        res = self._ledgerreconciliation_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._ledgerreconciliation_service.delete_ledgerreconciliation(created.id)

    def test_validation_bounds_ledgerreconciliation(self):
        """Test validation bounds and non-existent get behavior for LedgerReconciliation."""
        self.assertIsNone(self._ledgerreconciliation_service.get_ledgerreconciliation("invalid_id_value"))
        created = self._ledgerreconciliation_service.create_ledgerreconciliation({"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._ledgerreconciliation_service.delete_ledgerreconciliation(created.id)

    def test_csv_export_import_ledgerreconciliation(self):
        """Verify data serialization via CSV utility functions for LedgerReconciliation."""
        created = self._ledgerreconciliation_service.create_ledgerreconciliation({"code": "LEDGERRECONCILIATION-001", "description": "Standard record of type LedgerReconciliation", "status_state": "ACTIVE"})
        csv_out = export_ledgerreconciliations_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_ledgerreconciliations_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._ledgerreconciliation_service.delete_ledgerreconciliation(created.id)

    def test_model_closingentry_creation(self):
        """Verify instantiation and attribute validation for ClosingEntry."""
        obj = ClosingEntry(**{"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.count_value, {"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"count_value"])
        self.assertEqual(obj.seq_num, {"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"seq_num"])
        self.assertEqual(obj.status_state, {"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}[f"status_state"])

    def test_service_closingentry_crud(self):
        """Verify service CRUD operations for ClosingEntry."""
        created = self._closingentry_service.create_closingentry({"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._closingentry_service.get_closingentry(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._closingentry_service.update_closingentry(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._closingentry_service.list_all_closingentrys()
        self.assertTrue(len(all_items) > 0)
        deleted = self._closingentry_service.delete_closingentry(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_closingentry(self):
        """Verify domain custom workflow process logic on ClosingEntry."""
        created = self._closingentry_service.create_closingentry({"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertTrue(self._closingentry_service.verify_closingentry_workflow_state(created.id))
        res = self._closingentry_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._closingentry_service.delete_closingentry(created.id)

    def test_validation_bounds_closingentry(self):
        """Test validation bounds and non-existent get behavior for ClosingEntry."""
        self.assertIsNone(self._closingentry_service.get_closingentry("invalid_id_value"))
        created = self._closingentry_service.create_closingentry({"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._closingentry_service.delete_closingentry(created.id)

    def test_csv_export_import_closingentry(self):
        """Verify data serialization via CSV utility functions for ClosingEntry."""
        created = self._closingentry_service.create_closingentry({"code": "CLOSINGENTRY-001", "description": "Standard record of type ClosingEntry", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"})
        csv_out = export_closingentrys_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_closingentrys_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._closingentry_service.delete_closingentry(created.id)

    def test_model_recurringjournal_creation(self):
        """Verify instantiation and attribute validation for RecurringJournal."""
        obj = RecurringJournal(**{"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.status_state, {"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_recurringjournal_crud(self):
        """Verify service CRUD operations for RecurringJournal."""
        created = self._recurringjournal_service.create_recurringjournal({"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._recurringjournal_service.get_recurringjournal(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._recurringjournal_service.update_recurringjournal(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._recurringjournal_service.list_all_recurringjournals()
        self.assertTrue(len(all_items) > 0)
        deleted = self._recurringjournal_service.delete_recurringjournal(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_recurringjournal(self):
        """Verify domain custom workflow process logic on RecurringJournal."""
        created = self._recurringjournal_service.create_recurringjournal({"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"})
        self.assertTrue(self._recurringjournal_service.verify_recurringjournal_workflow_state(created.id))
        res = self._recurringjournal_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._recurringjournal_service.delete_recurringjournal(created.id)

    def test_validation_bounds_recurringjournal(self):
        """Test validation bounds and non-existent get behavior for RecurringJournal."""
        self.assertIsNone(self._recurringjournal_service.get_recurringjournal("invalid_id_value"))
        created = self._recurringjournal_service.create_recurringjournal({"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._recurringjournal_service.delete_recurringjournal(created.id)

    def test_csv_export_import_recurringjournal(self):
        """Verify data serialization via CSV utility functions for RecurringJournal."""
        created = self._recurringjournal_service.create_recurringjournal({"code": "RECURRINGJOURNAL-001", "description": "Standard record of type RecurringJournal", "status_state": "ACTIVE"})
        csv_out = export_recurringjournals_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_recurringjournals_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._recurringjournal_service.delete_recurringjournal(created.id)

    def test_model_accrualrule_creation(self):
        """Verify instantiation and attribute validation for AccrualRule."""
        obj = AccrualRule(**{"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertEqual(obj.code, {"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"code"])
        self.assertEqual(obj.description, {"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"description"])
        self.assertEqual(obj.amount, {"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"amount"])
        self.assertEqual(obj.base_currency, {"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"base_currency"])
        self.assertEqual(obj.status_state, {"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}[f"status_state"])

    def test_service_accrualrule_crud(self):
        """Verify service CRUD operations for AccrualRule."""
        created = self._accrualrule_service.create_accrualrule({"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        fetched = self._accrualrule_service.get_accrualrule(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)
        updated = self._accrualrule_service.update_accrualrule(created.id, {"code": "updated_val_x"})
        self.assertEqual(getattr(updated, "code"), "updated_val_x")
        all_items = self._accrualrule_service.list_all_accrualrules()
        self.assertTrue(len(all_items) > 0)
        deleted = self._accrualrule_service.delete_accrualrule(created.id)
        self.assertTrue(deleted)

    def test_business_workflow_accrualrule(self):
        """Verify domain custom workflow process logic on AccrualRule."""
        created = self._accrualrule_service.create_accrualrule({"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertTrue(self._accrualrule_service.verify_accrualrule_workflow_state(created.id))
        res = self._accrualrule_service.simulated_domain_workflow_1(created.id, "test_run")
        self.assertEqual(res.get("workflow_step"), 1)
        self.assertEqual(res.get("status"), "completed")
        self._accrualrule_service.delete_accrualrule(created.id)

    def test_validation_bounds_accrualrule(self):
        """Test validation bounds and non-existent get behavior for AccrualRule."""
        self.assertIsNone(self._accrualrule_service.get_accrualrule("invalid_id_value"))
        created = self._accrualrule_service.create_accrualrule({"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        self.assertIsNotNone(created.id)
        self._accrualrule_service.delete_accrualrule(created.id)

    def test_csv_export_import_accrualrule(self):
        """Verify data serialization via CSV utility functions for AccrualRule."""
        created = self._accrualrule_service.create_accrualrule({"code": "ACCRUALRULE-001", "description": "Standard record of type AccrualRule", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"})
        csv_out = export_accrualrules_to_csv([created.to_dict()])
        self.assertTrue(len(csv_out) > 0)
        imported = import_accrualrules_from_csv(csv_out)
        self.assertEqual(len(imported), 1)
        self._accrualrule_service.delete_accrualrule(created.id)

