"""
AuraLedger CASH_BANK Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.cash_bank.services import BankAccountService
from erp.modules.cash_bank.services import BankStatementService
from erp.modules.cash_bank.services import StatementLineService
from erp.modules.cash_bank.services import BankReconciliationService
from erp.modules.cash_bank.services import BankTransferService
from erp.modules.cash_bank.services import CashTransactionService
from erp.modules.cash_bank.services import ReconciliationMatchService
from erp.modules.cash_bank.services import PettyCashLogService
from erp.modules.cash_bank.services import BankChargeConfigService
from erp.modules.cash_bank.services import CashDrawerService
from erp.modules.cash_bank.services import DepositSlipService
from erp.modules.cash_bank.services import BankRoutingRegistryService

class Cash_bankApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._bankaccount_service = BankAccountService()
        self._bankstatement_service = BankStatementService()
        self._statementline_service = StatementLineService()
        self._bankreconciliation_service = BankReconciliationService()
        self._banktransfer_service = BankTransferService()
        self._cashtransaction_service = CashTransactionService()
        self._reconciliationmatch_service = ReconciliationMatchService()
        self._pettycashlog_service = PettyCashLogService()
        self._bankchargeconfig_service = BankChargeConfigService()
        self._cashdrawer_service = CashDrawerService()
        self._depositslip_service = DepositSlipService()
        self._bankroutingregistry_service = BankRoutingRegistryService()

    def create_bankaccount_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankaccounts"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
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
            obj = self._bankaccount_service.create_bankaccount(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_bankaccount_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankaccounts/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._bankaccount_service.get_bankaccount(record_id)
            if not obj:
                return {"status": "error", "message": "BankAccount not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_bankaccount_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/bankaccounts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._bankaccount_service.update_bankaccount(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_bankaccount_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/bankaccounts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._bankaccount_service.delete_bankaccount(record_id)
            if not success:
                return {"status": "error", "message": "BankAccount not found", "code": 404}
            return {"status": "success", "message": "BankAccount deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_bankaccounts_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankaccounts"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._bankaccount_service.list_all_bankaccounts()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_bankaccount_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankaccounts/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._bankaccount_service.verify_bankaccount_workflow_state(record_id)
            res = self._bankaccount_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_bankstatement_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankstatements"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._bankstatement_service.create_bankstatement(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_bankstatement_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankstatements/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._bankstatement_service.get_bankstatement(record_id)
            if not obj:
                return {"status": "error", "message": "BankStatement not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_bankstatement_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/bankstatements/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._bankstatement_service.update_bankstatement(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_bankstatement_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/bankstatements/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._bankstatement_service.delete_bankstatement(record_id)
            if not success:
                return {"status": "error", "message": "BankStatement not found", "code": 404}
            return {"status": "success", "message": "BankStatement deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_bankstatements_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankstatements"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._bankstatement_service.list_all_bankstatements()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_bankstatement_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankstatements/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._bankstatement_service.verify_bankstatement_workflow_state(record_id)
            res = self._bankstatement_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_statementline_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/statementlines"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._statementline_service.create_statementline(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_statementline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/statementlines/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._statementline_service.get_statementline(record_id)
            if not obj:
                return {"status": "error", "message": "StatementLine not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_statementline_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/statementlines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._statementline_service.update_statementline(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_statementline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/statementlines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._statementline_service.delete_statementline(record_id)
            if not success:
                return {"status": "error", "message": "StatementLine not found", "code": 404}
            return {"status": "success", "message": "StatementLine deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_statementlines_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/statementlines"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._statementline_service.list_all_statementlines()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_statementline_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/statementlines/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._statementline_service.verify_statementline_workflow_state(record_id)
            res = self._statementline_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_bankreconciliation_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankreconciliations"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._bankreconciliation_service.create_bankreconciliation(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_bankreconciliation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._bankreconciliation_service.get_bankreconciliation(record_id)
            if not obj:
                return {"status": "error", "message": "BankReconciliation not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_bankreconciliation_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/bankreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._bankreconciliation_service.update_bankreconciliation(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_bankreconciliation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/bankreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._bankreconciliation_service.delete_bankreconciliation(record_id)
            if not success:
                return {"status": "error", "message": "BankReconciliation not found", "code": 404}
            return {"status": "success", "message": "BankReconciliation deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_bankreconciliations_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankreconciliations"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._bankreconciliation_service.list_all_bankreconciliations()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_bankreconciliation_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankreconciliations/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._bankreconciliation_service.verify_bankreconciliation_workflow_state(record_id)
            res = self._bankreconciliation_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_banktransfer_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/banktransfers"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._banktransfer_service.create_banktransfer(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_banktransfer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/banktransfers/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._banktransfer_service.get_banktransfer(record_id)
            if not obj:
                return {"status": "error", "message": "BankTransfer not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_banktransfer_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/banktransfers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._banktransfer_service.update_banktransfer(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_banktransfer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/banktransfers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._banktransfer_service.delete_banktransfer(record_id)
            if not success:
                return {"status": "error", "message": "BankTransfer not found", "code": 404}
            return {"status": "success", "message": "BankTransfer deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_banktransfers_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/banktransfers"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._banktransfer_service.list_all_banktransfers()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_banktransfer_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/banktransfers/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._banktransfer_service.verify_banktransfer_workflow_state(record_id)
            res = self._banktransfer_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_cashtransaction_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/cashtransactions"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._cashtransaction_service.create_cashtransaction(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_cashtransaction_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/cashtransactions/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._cashtransaction_service.get_cashtransaction(record_id)
            if not obj:
                return {"status": "error", "message": "CashTransaction not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_cashtransaction_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/cashtransactions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._cashtransaction_service.update_cashtransaction(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_cashtransaction_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/cashtransactions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._cashtransaction_service.delete_cashtransaction(record_id)
            if not success:
                return {"status": "error", "message": "CashTransaction not found", "code": 404}
            return {"status": "success", "message": "CashTransaction deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_cashtransactions_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/cashtransactions"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._cashtransaction_service.list_all_cashtransactions()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_cashtransaction_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/cashtransactions/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._cashtransaction_service.verify_cashtransaction_workflow_state(record_id)
            res = self._cashtransaction_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_reconciliationmatch_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/reconciliationmatchs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._reconciliationmatch_service.create_reconciliationmatch(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_reconciliationmatch_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/reconciliationmatchs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._reconciliationmatch_service.get_reconciliationmatch(record_id)
            if not obj:
                return {"status": "error", "message": "ReconciliationMatch not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_reconciliationmatch_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/reconciliationmatchs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._reconciliationmatch_service.update_reconciliationmatch(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_reconciliationmatch_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/reconciliationmatchs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._reconciliationmatch_service.delete_reconciliationmatch(record_id)
            if not success:
                return {"status": "error", "message": "ReconciliationMatch not found", "code": 404}
            return {"status": "success", "message": "ReconciliationMatch deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_reconciliationmatchs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/reconciliationmatchs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._reconciliationmatch_service.list_all_reconciliationmatchs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_reconciliationmatch_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/reconciliationmatchs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._reconciliationmatch_service.verify_reconciliationmatch_workflow_state(record_id)
            res = self._reconciliationmatch_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_pettycashlog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/pettycashlogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._pettycashlog_service.create_pettycashlog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_pettycashlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/pettycashlogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._pettycashlog_service.get_pettycashlog(record_id)
            if not obj:
                return {"status": "error", "message": "PettyCashLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_pettycashlog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/pettycashlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._pettycashlog_service.update_pettycashlog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_pettycashlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/pettycashlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._pettycashlog_service.delete_pettycashlog(record_id)
            if not success:
                return {"status": "error", "message": "PettyCashLog not found", "code": 404}
            return {"status": "success", "message": "PettyCashLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_pettycashlogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/pettycashlogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._pettycashlog_service.list_all_pettycashlogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_pettycashlog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/pettycashlogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._pettycashlog_service.verify_pettycashlog_workflow_state(record_id)
            res = self._pettycashlog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_bankchargeconfig_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankchargeconfigs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._bankchargeconfig_service.create_bankchargeconfig(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_bankchargeconfig_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankchargeconfigs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._bankchargeconfig_service.get_bankchargeconfig(record_id)
            if not obj:
                return {"status": "error", "message": "BankChargeConfig not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_bankchargeconfig_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/bankchargeconfigs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._bankchargeconfig_service.update_bankchargeconfig(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_bankchargeconfig_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/bankchargeconfigs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._bankchargeconfig_service.delete_bankchargeconfig(record_id)
            if not success:
                return {"status": "error", "message": "BankChargeConfig not found", "code": 404}
            return {"status": "success", "message": "BankChargeConfig deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_bankchargeconfigs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankchargeconfigs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._bankchargeconfig_service.list_all_bankchargeconfigs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_bankchargeconfig_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankchargeconfigs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._bankchargeconfig_service.verify_bankchargeconfig_workflow_state(record_id)
            res = self._bankchargeconfig_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_cashdrawer_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/cashdrawers"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._cashdrawer_service.create_cashdrawer(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_cashdrawer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/cashdrawers/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._cashdrawer_service.get_cashdrawer(record_id)
            if not obj:
                return {"status": "error", "message": "CashDrawer not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_cashdrawer_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/cashdrawers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._cashdrawer_service.update_cashdrawer(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_cashdrawer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/cashdrawers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._cashdrawer_service.delete_cashdrawer(record_id)
            if not success:
                return {"status": "error", "message": "CashDrawer not found", "code": 404}
            return {"status": "success", "message": "CashDrawer deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_cashdrawers_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/cashdrawers"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._cashdrawer_service.list_all_cashdrawers()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_cashdrawer_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/cashdrawers/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._cashdrawer_service.verify_cashdrawer_workflow_state(record_id)
            res = self._cashdrawer_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_depositslip_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/depositslips"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._depositslip_service.create_depositslip(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_depositslip_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/depositslips/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._depositslip_service.get_depositslip(record_id)
            if not obj:
                return {"status": "error", "message": "DepositSlip not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_depositslip_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/depositslips/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._depositslip_service.update_depositslip(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_depositslip_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/depositslips/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._depositslip_service.delete_depositslip(record_id)
            if not success:
                return {"status": "error", "message": "DepositSlip not found", "code": 404}
            return {"status": "success", "message": "DepositSlip deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_depositslips_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/depositslips"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._depositslip_service.list_all_depositslips()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_depositslip_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/depositslips/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._depositslip_service.verify_depositslip_workflow_state(record_id)
            res = self._depositslip_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_bankroutingregistry_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankroutingregistrys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._bankroutingregistry_service.create_bankroutingregistry(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_bankroutingregistry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankroutingregistrys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            obj = self._bankroutingregistry_service.get_bankroutingregistry(record_id)
            if not obj:
                return {"status": "error", "message": "BankRoutingRegistry not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_bankroutingregistry_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cash_bank/bankroutingregistrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cash_bank_manager"])
            obj = self._bankroutingregistry_service.update_bankroutingregistry(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_bankroutingregistry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cash_bank/bankroutingregistrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._bankroutingregistry_service.delete_bankroutingregistry(record_id)
            if not success:
                return {"status": "error", "message": "BankRoutingRegistry not found", "code": 404}
            return {"status": "success", "message": "BankRoutingRegistry deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_bankroutingregistrys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cash_bank/bankroutingregistrys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cash_bank_user"])
            items = self._bankroutingregistry_service.list_all_bankroutingregistrys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_bankroutingregistry_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cash_bank/bankroutingregistrys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cash_bank_user"])
            is_valid = self._bankroutingregistry_service.verify_bankroutingregistry_workflow_state(record_id)
            res = self._bankroutingregistry_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

