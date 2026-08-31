"""
AuraLedger GENERAL_LEDGER Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.general_ledger.services import AccountService
from erp.modules.general_ledger.services import JournalEntryService
from erp.modules.general_ledger.services import JournalLineService
from erp.modules.general_ledger.services import TransactionTypeService
from erp.modules.general_ledger.services import CurrencyService
from erp.modules.general_ledger.services import AccountingPeriodService
from erp.modules.general_ledger.services import FiscalYearService
from erp.modules.general_ledger.services import LedgerBalanceService
from erp.modules.general_ledger.services import LedgerReconciliationService
from erp.modules.general_ledger.services import ClosingEntryService
from erp.modules.general_ledger.services import RecurringJournalService
from erp.modules.general_ledger.services import AccrualRuleService

class General_ledgerApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
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

    def create_account_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/accounts"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "account_number" not in payload:
                return {"status": "error", "message": "Missing required parameter: account_number", "code": 400}
            if "name" not in payload:
                return {"status": "error", "message": "Missing required parameter: name", "code": 400}
            if "account_type" not in payload:
                return {"status": "error", "message": "Missing required parameter: account_type", "code": 400}
            if "balance" not in payload:
                return {"status": "error", "message": "Missing required parameter: balance", "code": 400}
            if "currency" not in payload:
                return {"status": "error", "message": "Missing required parameter: currency", "code": 400}
            obj = self._account_service.create_account(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_account_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/accounts/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._account_service.get_account(record_id)
            if not obj:
                return {"status": "error", "message": "Account not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_account_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/accounts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._account_service.update_account(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_account_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/accounts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._account_service.delete_account(record_id)
            if not success:
                return {"status": "error", "message": "Account not found", "code": 404}
            return {"status": "success", "message": "Account deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_accounts_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/accounts"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._account_service.list_all_accounts()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_account_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/accounts/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._account_service.verify_account_workflow_state(record_id)
            res = self._account_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_journalentry_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/journalentrys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "entry_number" not in payload:
                return {"status": "error", "message": "Missing required parameter: entry_number", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "posted_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: posted_date", "code": 400}
            if "status" not in payload:
                return {"status": "error", "message": "Missing required parameter: status", "code": 400}
            if "total_debit" not in payload:
                return {"status": "error", "message": "Missing required parameter: total_debit", "code": 400}
            obj = self._journalentry_service.create_journalentry(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_journalentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/journalentrys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._journalentry_service.get_journalentry(record_id)
            if not obj:
                return {"status": "error", "message": "JournalEntry not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_journalentry_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/journalentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._journalentry_service.update_journalentry(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_journalentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/journalentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._journalentry_service.delete_journalentry(record_id)
            if not success:
                return {"status": "error", "message": "JournalEntry not found", "code": 404}
            return {"status": "success", "message": "JournalEntry deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_journalentrys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/journalentrys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._journalentry_service.list_all_journalentrys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_journalentry_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/journalentrys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._journalentry_service.verify_journalentry_workflow_state(record_id)
            res = self._journalentry_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_journalline_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/journallines"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._journalline_service.create_journalline(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_journalline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/journallines/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._journalline_service.get_journalline(record_id)
            if not obj:
                return {"status": "error", "message": "JournalLine not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_journalline_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/journallines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._journalline_service.update_journalline(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_journalline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/journallines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._journalline_service.delete_journalline(record_id)
            if not success:
                return {"status": "error", "message": "JournalLine not found", "code": 404}
            return {"status": "success", "message": "JournalLine deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_journallines_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/journallines"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._journalline_service.list_all_journallines()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_journalline_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/journallines/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._journalline_service.verify_journalline_workflow_state(record_id)
            res = self._journalline_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_transactiontype_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/transactiontypes"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._transactiontype_service.create_transactiontype(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_transactiontype_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/transactiontypes/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._transactiontype_service.get_transactiontype(record_id)
            if not obj:
                return {"status": "error", "message": "TransactionType not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_transactiontype_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/transactiontypes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._transactiontype_service.update_transactiontype(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_transactiontype_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/transactiontypes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._transactiontype_service.delete_transactiontype(record_id)
            if not success:
                return {"status": "error", "message": "TransactionType not found", "code": 404}
            return {"status": "success", "message": "TransactionType deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_transactiontypes_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/transactiontypes"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._transactiontype_service.list_all_transactiontypes()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_transactiontype_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/transactiontypes/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._transactiontype_service.verify_transactiontype_workflow_state(record_id)
            res = self._transactiontype_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_currency_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/currencys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._currency_service.create_currency(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_currency_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/currencys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._currency_service.get_currency(record_id)
            if not obj:
                return {"status": "error", "message": "Currency not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_currency_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/currencys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._currency_service.update_currency(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_currency_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/currencys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._currency_service.delete_currency(record_id)
            if not success:
                return {"status": "error", "message": "Currency not found", "code": 404}
            return {"status": "success", "message": "Currency deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_currencys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/currencys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._currency_service.list_all_currencys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_currency_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/currencys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._currency_service.verify_currency_workflow_state(record_id)
            res = self._currency_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_accountingperiod_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/accountingperiods"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "scheduled_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: scheduled_date", "code": 400}
            if "period_code" not in payload:
                return {"status": "error", "message": "Missing required parameter: period_code", "code": 400}
            if "count_value" not in payload:
                return {"status": "error", "message": "Missing required parameter: count_value", "code": 400}
            if "seq_num" not in payload:
                return {"status": "error", "message": "Missing required parameter: seq_num", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._accountingperiod_service.create_accountingperiod(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_accountingperiod_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/accountingperiods/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._accountingperiod_service.get_accountingperiod(record_id)
            if not obj:
                return {"status": "error", "message": "AccountingPeriod not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_accountingperiod_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/accountingperiods/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._accountingperiod_service.update_accountingperiod(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_accountingperiod_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/accountingperiods/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._accountingperiod_service.delete_accountingperiod(record_id)
            if not success:
                return {"status": "error", "message": "AccountingPeriod not found", "code": 404}
            return {"status": "success", "message": "AccountingPeriod deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_accountingperiods_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/accountingperiods"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._accountingperiod_service.list_all_accountingperiods()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_accountingperiod_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/accountingperiods/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._accountingperiod_service.verify_accountingperiod_workflow_state(record_id)
            res = self._accountingperiod_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_fiscalyear_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/fiscalyears"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "scheduled_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: scheduled_date", "code": 400}
            if "period_code" not in payload:
                return {"status": "error", "message": "Missing required parameter: period_code", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._fiscalyear_service.create_fiscalyear(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_fiscalyear_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/fiscalyears/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._fiscalyear_service.get_fiscalyear(record_id)
            if not obj:
                return {"status": "error", "message": "FiscalYear not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_fiscalyear_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/fiscalyears/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._fiscalyear_service.update_fiscalyear(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_fiscalyear_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/fiscalyears/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._fiscalyear_service.delete_fiscalyear(record_id)
            if not success:
                return {"status": "error", "message": "FiscalYear not found", "code": 404}
            return {"status": "success", "message": "FiscalYear deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_fiscalyears_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/fiscalyears"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._fiscalyear_service.list_all_fiscalyears()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_fiscalyear_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/fiscalyears/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._fiscalyear_service.verify_fiscalyear_workflow_state(record_id)
            res = self._fiscalyear_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_ledgerbalance_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/ledgerbalances"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "amount" not in payload:
                return {"status": "error", "message": "Missing required parameter: amount", "code": 400}
            if "base_currency" not in payload:
                return {"status": "error", "message": "Missing required parameter: base_currency", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._ledgerbalance_service.create_ledgerbalance(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_ledgerbalance_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/ledgerbalances/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._ledgerbalance_service.get_ledgerbalance(record_id)
            if not obj:
                return {"status": "error", "message": "LedgerBalance not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_ledgerbalance_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/ledgerbalances/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._ledgerbalance_service.update_ledgerbalance(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_ledgerbalance_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/ledgerbalances/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._ledgerbalance_service.delete_ledgerbalance(record_id)
            if not success:
                return {"status": "error", "message": "LedgerBalance not found", "code": 404}
            return {"status": "success", "message": "LedgerBalance deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_ledgerbalances_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/ledgerbalances"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._ledgerbalance_service.list_all_ledgerbalances()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_ledgerbalance_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/ledgerbalances/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._ledgerbalance_service.verify_ledgerbalance_workflow_state(record_id)
            res = self._ledgerbalance_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_ledgerreconciliation_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/ledgerreconciliations"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._ledgerreconciliation_service.create_ledgerreconciliation(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_ledgerreconciliation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/ledgerreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._ledgerreconciliation_service.get_ledgerreconciliation(record_id)
            if not obj:
                return {"status": "error", "message": "LedgerReconciliation not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_ledgerreconciliation_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/ledgerreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._ledgerreconciliation_service.update_ledgerreconciliation(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_ledgerreconciliation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/ledgerreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._ledgerreconciliation_service.delete_ledgerreconciliation(record_id)
            if not success:
                return {"status": "error", "message": "LedgerReconciliation not found", "code": 404}
            return {"status": "success", "message": "LedgerReconciliation deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_ledgerreconciliations_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/ledgerreconciliations"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._ledgerreconciliation_service.list_all_ledgerreconciliations()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_ledgerreconciliation_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/ledgerreconciliations/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._ledgerreconciliation_service.verify_ledgerreconciliation_workflow_state(record_id)
            res = self._ledgerreconciliation_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_closingentry_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/closingentrys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "count_value" not in payload:
                return {"status": "error", "message": "Missing required parameter: count_value", "code": 400}
            if "seq_num" not in payload:
                return {"status": "error", "message": "Missing required parameter: seq_num", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._closingentry_service.create_closingentry(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_closingentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/closingentrys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._closingentry_service.get_closingentry(record_id)
            if not obj:
                return {"status": "error", "message": "ClosingEntry not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_closingentry_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/closingentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._closingentry_service.update_closingentry(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_closingentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/closingentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._closingentry_service.delete_closingentry(record_id)
            if not success:
                return {"status": "error", "message": "ClosingEntry not found", "code": 404}
            return {"status": "success", "message": "ClosingEntry deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_closingentrys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/closingentrys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._closingentry_service.list_all_closingentrys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_closingentry_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/closingentrys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._closingentry_service.verify_closingentry_workflow_state(record_id)
            res = self._closingentry_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_recurringjournal_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/recurringjournals"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._recurringjournal_service.create_recurringjournal(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_recurringjournal_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/recurringjournals/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._recurringjournal_service.get_recurringjournal(record_id)
            if not obj:
                return {"status": "error", "message": "RecurringJournal not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_recurringjournal_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/recurringjournals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._recurringjournal_service.update_recurringjournal(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_recurringjournal_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/recurringjournals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._recurringjournal_service.delete_recurringjournal(record_id)
            if not success:
                return {"status": "error", "message": "RecurringJournal not found", "code": 404}
            return {"status": "success", "message": "RecurringJournal deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_recurringjournals_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/recurringjournals"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._recurringjournal_service.list_all_recurringjournals()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_recurringjournal_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/recurringjournals/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._recurringjournal_service.verify_recurringjournal_workflow_state(record_id)
            res = self._recurringjournal_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_accrualrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/accrualrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "amount" not in payload:
                return {"status": "error", "message": "Missing required parameter: amount", "code": 400}
            if "base_currency" not in payload:
                return {"status": "error", "message": "Missing required parameter: base_currency", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._accrualrule_service.create_accrualrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_accrualrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/accrualrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            obj = self._accrualrule_service.get_accrualrule(record_id)
            if not obj:
                return {"status": "error", "message": "AccrualRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_accrualrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/general_ledger/accrualrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "general_ledger_manager"])
            obj = self._accrualrule_service.update_accrualrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_accrualrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/general_ledger/accrualrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._accrualrule_service.delete_accrualrule(record_id)
            if not success:
                return {"status": "error", "message": "AccrualRule not found", "code": 404}
            return {"status": "success", "message": "AccrualRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_accrualrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/general_ledger/accrualrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "general_ledger_user"])
            items = self._accrualrule_service.list_all_accrualrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_accrualrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/general_ledger/accrualrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "general_ledger_user"])
            is_valid = self._accrualrule_service.verify_accrualrule_workflow_state(record_id)
            res = self._accrualrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

