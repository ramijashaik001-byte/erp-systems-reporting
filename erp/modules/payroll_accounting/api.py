"""
AuraLedger PAYROLL_ACCOUNTING Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.payroll_accounting.services import PayrollJournalService
from erp.modules.payroll_accounting.services import EmployeeSalaryProfileService
from erp.modules.payroll_accounting.services import PayrollTaxWithholdingService
from erp.modules.payroll_accounting.services import PayrollAccrualService
from erp.modules.payroll_accounting.services import BenefitExpenseService
from erp.modules.payroll_accounting.services import ExpenseReimbursementService
from erp.modules.payroll_accounting.services import TimesheetPostingService
from erp.modules.payroll_accounting.services import PayrollAdjustmentService
from erp.modules.payroll_accounting.services import SalaryGradeService
from erp.modules.payroll_accounting.services import PayrollBenefitPlanService
from erp.modules.payroll_accounting.services import EmployerTaxContributionService
from erp.modules.payroll_accounting.services import PayrollAccrualPostingService

class Payroll_accountingApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._payrolljournal_service = PayrollJournalService()
        self._employeesalaryprofile_service = EmployeeSalaryProfileService()
        self._payrolltaxwithholding_service = PayrollTaxWithholdingService()
        self._payrollaccrual_service = PayrollAccrualService()
        self._benefitexpense_service = BenefitExpenseService()
        self._expensereimbursement_service = ExpenseReimbursementService()
        self._timesheetposting_service = TimesheetPostingService()
        self._payrolladjustment_service = PayrollAdjustmentService()
        self._salarygrade_service = SalaryGradeService()
        self._payrollbenefitplan_service = PayrollBenefitPlanService()
        self._employertaxcontribution_service = EmployerTaxContributionService()
        self._payrollaccrualposting_service = PayrollAccrualPostingService()

    def create_payrolljournal_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrolljournals"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._payrolljournal_service.create_payrolljournal(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_payrolljournal_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrolljournals/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._payrolljournal_service.get_payrolljournal(record_id)
            if not obj:
                return {"status": "error", "message": "PayrollJournal not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_payrolljournal_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/payrolljournals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._payrolljournal_service.update_payrolljournal(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_payrolljournal_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/payrolljournals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._payrolljournal_service.delete_payrolljournal(record_id)
            if not success:
                return {"status": "error", "message": "PayrollJournal not found", "code": 404}
            return {"status": "success", "message": "PayrollJournal deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_payrolljournals_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrolljournals"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._payrolljournal_service.list_all_payrolljournals()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_payrolljournal_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrolljournals/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._payrolljournal_service.verify_payrolljournal_workflow_state(record_id)
            res = self._payrolljournal_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_employeesalaryprofile_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/employeesalaryprofiles"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._employeesalaryprofile_service.create_employeesalaryprofile(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_employeesalaryprofile_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/employeesalaryprofiles/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._employeesalaryprofile_service.get_employeesalaryprofile(record_id)
            if not obj:
                return {"status": "error", "message": "EmployeeSalaryProfile not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_employeesalaryprofile_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/employeesalaryprofiles/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._employeesalaryprofile_service.update_employeesalaryprofile(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_employeesalaryprofile_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/employeesalaryprofiles/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._employeesalaryprofile_service.delete_employeesalaryprofile(record_id)
            if not success:
                return {"status": "error", "message": "EmployeeSalaryProfile not found", "code": 404}
            return {"status": "success", "message": "EmployeeSalaryProfile deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_employeesalaryprofiles_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/employeesalaryprofiles"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._employeesalaryprofile_service.list_all_employeesalaryprofiles()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_employeesalaryprofile_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/employeesalaryprofiles/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._employeesalaryprofile_service.verify_employeesalaryprofile_workflow_state(record_id)
            res = self._employeesalaryprofile_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_payrolltaxwithholding_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrolltaxwithholdings"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._payrolltaxwithholding_service.create_payrolltaxwithholding(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_payrolltaxwithholding_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrolltaxwithholdings/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._payrolltaxwithholding_service.get_payrolltaxwithholding(record_id)
            if not obj:
                return {"status": "error", "message": "PayrollTaxWithholding not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_payrolltaxwithholding_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/payrolltaxwithholdings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._payrolltaxwithholding_service.update_payrolltaxwithholding(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_payrolltaxwithholding_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/payrolltaxwithholdings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._payrolltaxwithholding_service.delete_payrolltaxwithholding(record_id)
            if not success:
                return {"status": "error", "message": "PayrollTaxWithholding not found", "code": 404}
            return {"status": "success", "message": "PayrollTaxWithholding deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_payrolltaxwithholdings_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrolltaxwithholdings"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._payrolltaxwithholding_service.list_all_payrolltaxwithholdings()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_payrolltaxwithholding_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrolltaxwithholdings/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._payrolltaxwithholding_service.verify_payrolltaxwithholding_workflow_state(record_id)
            res = self._payrolltaxwithholding_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_payrollaccrual_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrollaccruals"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._payrollaccrual_service.create_payrollaccrual(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_payrollaccrual_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrollaccruals/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._payrollaccrual_service.get_payrollaccrual(record_id)
            if not obj:
                return {"status": "error", "message": "PayrollAccrual not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_payrollaccrual_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/payrollaccruals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._payrollaccrual_service.update_payrollaccrual(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_payrollaccrual_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/payrollaccruals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._payrollaccrual_service.delete_payrollaccrual(record_id)
            if not success:
                return {"status": "error", "message": "PayrollAccrual not found", "code": 404}
            return {"status": "success", "message": "PayrollAccrual deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_payrollaccruals_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrollaccruals"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._payrollaccrual_service.list_all_payrollaccruals()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_payrollaccrual_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrollaccruals/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._payrollaccrual_service.verify_payrollaccrual_workflow_state(record_id)
            res = self._payrollaccrual_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_benefitexpense_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/benefitexpenses"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._benefitexpense_service.create_benefitexpense(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_benefitexpense_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/benefitexpenses/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._benefitexpense_service.get_benefitexpense(record_id)
            if not obj:
                return {"status": "error", "message": "BenefitExpense not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_benefitexpense_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/benefitexpenses/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._benefitexpense_service.update_benefitexpense(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_benefitexpense_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/benefitexpenses/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._benefitexpense_service.delete_benefitexpense(record_id)
            if not success:
                return {"status": "error", "message": "BenefitExpense not found", "code": 404}
            return {"status": "success", "message": "BenefitExpense deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_benefitexpenses_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/benefitexpenses"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._benefitexpense_service.list_all_benefitexpenses()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_benefitexpense_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/benefitexpenses/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._benefitexpense_service.verify_benefitexpense_workflow_state(record_id)
            res = self._benefitexpense_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_expensereimbursement_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/expensereimbursements"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._expensereimbursement_service.create_expensereimbursement(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_expensereimbursement_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/expensereimbursements/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._expensereimbursement_service.get_expensereimbursement(record_id)
            if not obj:
                return {"status": "error", "message": "ExpenseReimbursement not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_expensereimbursement_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/expensereimbursements/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._expensereimbursement_service.update_expensereimbursement(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_expensereimbursement_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/expensereimbursements/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._expensereimbursement_service.delete_expensereimbursement(record_id)
            if not success:
                return {"status": "error", "message": "ExpenseReimbursement not found", "code": 404}
            return {"status": "success", "message": "ExpenseReimbursement deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_expensereimbursements_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/expensereimbursements"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._expensereimbursement_service.list_all_expensereimbursements()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_expensereimbursement_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/expensereimbursements/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._expensereimbursement_service.verify_expensereimbursement_workflow_state(record_id)
            res = self._expensereimbursement_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_timesheetposting_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/timesheetpostings"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._timesheetposting_service.create_timesheetposting(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_timesheetposting_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/timesheetpostings/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._timesheetposting_service.get_timesheetposting(record_id)
            if not obj:
                return {"status": "error", "message": "TimesheetPosting not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_timesheetposting_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/timesheetpostings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._timesheetposting_service.update_timesheetposting(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_timesheetposting_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/timesheetpostings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._timesheetposting_service.delete_timesheetposting(record_id)
            if not success:
                return {"status": "error", "message": "TimesheetPosting not found", "code": 404}
            return {"status": "success", "message": "TimesheetPosting deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_timesheetpostings_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/timesheetpostings"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._timesheetposting_service.list_all_timesheetpostings()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_timesheetposting_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/timesheetpostings/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._timesheetposting_service.verify_timesheetposting_workflow_state(record_id)
            res = self._timesheetposting_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_payrolladjustment_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrolladjustments"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._payrolladjustment_service.create_payrolladjustment(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_payrolladjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrolladjustments/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._payrolladjustment_service.get_payrolladjustment(record_id)
            if not obj:
                return {"status": "error", "message": "PayrollAdjustment not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_payrolladjustment_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/payrolladjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._payrolladjustment_service.update_payrolladjustment(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_payrolladjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/payrolladjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._payrolladjustment_service.delete_payrolladjustment(record_id)
            if not success:
                return {"status": "error", "message": "PayrollAdjustment not found", "code": 404}
            return {"status": "success", "message": "PayrollAdjustment deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_payrolladjustments_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrolladjustments"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._payrolladjustment_service.list_all_payrolladjustments()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_payrolladjustment_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrolladjustments/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._payrolladjustment_service.verify_payrolladjustment_workflow_state(record_id)
            res = self._payrolladjustment_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_salarygrade_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/salarygrades"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._salarygrade_service.create_salarygrade(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_salarygrade_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/salarygrades/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._salarygrade_service.get_salarygrade(record_id)
            if not obj:
                return {"status": "error", "message": "SalaryGrade not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_salarygrade_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/salarygrades/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._salarygrade_service.update_salarygrade(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_salarygrade_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/salarygrades/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._salarygrade_service.delete_salarygrade(record_id)
            if not success:
                return {"status": "error", "message": "SalaryGrade not found", "code": 404}
            return {"status": "success", "message": "SalaryGrade deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_salarygrades_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/salarygrades"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._salarygrade_service.list_all_salarygrades()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_salarygrade_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/salarygrades/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._salarygrade_service.verify_salarygrade_workflow_state(record_id)
            res = self._salarygrade_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_payrollbenefitplan_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrollbenefitplans"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._payrollbenefitplan_service.create_payrollbenefitplan(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_payrollbenefitplan_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrollbenefitplans/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._payrollbenefitplan_service.get_payrollbenefitplan(record_id)
            if not obj:
                return {"status": "error", "message": "PayrollBenefitPlan not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_payrollbenefitplan_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/payrollbenefitplans/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._payrollbenefitplan_service.update_payrollbenefitplan(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_payrollbenefitplan_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/payrollbenefitplans/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._payrollbenefitplan_service.delete_payrollbenefitplan(record_id)
            if not success:
                return {"status": "error", "message": "PayrollBenefitPlan not found", "code": 404}
            return {"status": "success", "message": "PayrollBenefitPlan deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_payrollbenefitplans_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrollbenefitplans"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._payrollbenefitplan_service.list_all_payrollbenefitplans()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_payrollbenefitplan_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrollbenefitplans/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._payrollbenefitplan_service.verify_payrollbenefitplan_workflow_state(record_id)
            res = self._payrollbenefitplan_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_employertaxcontribution_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/employertaxcontributions"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._employertaxcontribution_service.create_employertaxcontribution(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_employertaxcontribution_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/employertaxcontributions/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._employertaxcontribution_service.get_employertaxcontribution(record_id)
            if not obj:
                return {"status": "error", "message": "EmployerTaxContribution not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_employertaxcontribution_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/employertaxcontributions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._employertaxcontribution_service.update_employertaxcontribution(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_employertaxcontribution_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/employertaxcontributions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._employertaxcontribution_service.delete_employertaxcontribution(record_id)
            if not success:
                return {"status": "error", "message": "EmployerTaxContribution not found", "code": 404}
            return {"status": "success", "message": "EmployerTaxContribution deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_employertaxcontributions_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/employertaxcontributions"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._employertaxcontribution_service.list_all_employertaxcontributions()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_employertaxcontribution_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/employertaxcontributions/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._employertaxcontribution_service.verify_employertaxcontribution_workflow_state(record_id)
            res = self._employertaxcontribution_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_payrollaccrualposting_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrollaccrualpostings"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
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
            obj = self._payrollaccrualposting_service.create_payrollaccrualposting(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_payrollaccrualposting_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrollaccrualpostings/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            obj = self._payrollaccrualposting_service.get_payrollaccrualposting(record_id)
            if not obj:
                return {"status": "error", "message": "PayrollAccrualPosting not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_payrollaccrualposting_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/payroll_accounting/payrollaccrualpostings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "payroll_accounting_manager"])
            obj = self._payrollaccrualposting_service.update_payrollaccrualposting(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_payrollaccrualposting_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/payroll_accounting/payrollaccrualpostings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._payrollaccrualposting_service.delete_payrollaccrualposting(record_id)
            if not success:
                return {"status": "error", "message": "PayrollAccrualPosting not found", "code": 404}
            return {"status": "success", "message": "PayrollAccrualPosting deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_payrollaccrualpostings_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/payroll_accounting/payrollaccrualpostings"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "payroll_accounting_user"])
            items = self._payrollaccrualposting_service.list_all_payrollaccrualpostings()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_payrollaccrualposting_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/payroll_accounting/payrollaccrualpostings/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "payroll_accounting_user"])
            is_valid = self._payrollaccrualposting_service.verify_payrollaccrualposting_workflow_state(record_id)
            res = self._payrollaccrualposting_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

