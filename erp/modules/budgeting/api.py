"""
AuraLedger BUDGETING Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.budgeting.services import BudgetPlanService
from erp.modules.budgeting.services import BudgetLineService
from erp.modules.budgeting.services import CostCenterService
from erp.modules.budgeting.services import ProfitCenterService
from erp.modules.budgeting.services import BudgetAllocationService
from erp.modules.budgeting.services import BudgetAdjustmentService
from erp.modules.budgeting.services import ForecastModelService
from erp.modules.budgeting.services import ForecastScenarioService
from erp.modules.budgeting.services import BudgetTypeService
from erp.modules.budgeting.services import BudgetApproverService
from erp.modules.budgeting.services import BudgetThresholdAlertService
from erp.modules.budgeting.services import ZeroBasedBudgetTemplateService

class BudgetingApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._budgetplan_service = BudgetPlanService()
        self._budgetline_service = BudgetLineService()
        self._costcenter_service = CostCenterService()
        self._profitcenter_service = ProfitCenterService()
        self._budgetallocation_service = BudgetAllocationService()
        self._budgetadjustment_service = BudgetAdjustmentService()
        self._forecastmodel_service = ForecastModelService()
        self._forecastscenario_service = ForecastScenarioService()
        self._budgettype_service = BudgetTypeService()
        self._budgetapprover_service = BudgetApproverService()
        self._budgetthresholdalert_service = BudgetThresholdAlertService()
        self._zerobasedbudgettemplate_service = ZeroBasedBudgetTemplateService()

    def create_budgetplan_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetplans"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgetplan_service.create_budgetplan(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgetplan_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetplans/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgetplan_service.get_budgetplan(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetPlan not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgetplan_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgetplans/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgetplan_service.update_budgetplan(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgetplan_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgetplans/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgetplan_service.delete_budgetplan(record_id)
            if not success:
                return {"status": "error", "message": "BudgetPlan not found", "code": 404}
            return {"status": "success", "message": "BudgetPlan deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgetplans_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetplans"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgetplan_service.list_all_budgetplans()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgetplan_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetplans/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgetplan_service.verify_budgetplan_workflow_state(record_id)
            res = self._budgetplan_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_budgetline_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetlines"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgetline_service.create_budgetline(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgetline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetlines/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgetline_service.get_budgetline(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetLine not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgetline_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgetlines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgetline_service.update_budgetline(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgetline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgetlines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgetline_service.delete_budgetline(record_id)
            if not success:
                return {"status": "error", "message": "BudgetLine not found", "code": 404}
            return {"status": "success", "message": "BudgetLine deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgetlines_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetlines"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgetline_service.list_all_budgetlines()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgetline_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetlines/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgetline_service.verify_budgetline_workflow_state(record_id)
            res = self._budgetline_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costcenter_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/costcenters"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
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
            obj = self._costcenter_service.create_costcenter(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costcenter_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/costcenters/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._costcenter_service.get_costcenter(record_id)
            if not obj:
                return {"status": "error", "message": "CostCenter not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costcenter_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/costcenters/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._costcenter_service.update_costcenter(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costcenter_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/costcenters/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costcenter_service.delete_costcenter(record_id)
            if not success:
                return {"status": "error", "message": "CostCenter not found", "code": 404}
            return {"status": "success", "message": "CostCenter deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costcenters_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/costcenters"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._costcenter_service.list_all_costcenters()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costcenter_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/costcenters/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._costcenter_service.verify_costcenter_workflow_state(record_id)
            res = self._costcenter_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_profitcenter_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/profitcenters"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._profitcenter_service.create_profitcenter(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_profitcenter_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/profitcenters/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._profitcenter_service.get_profitcenter(record_id)
            if not obj:
                return {"status": "error", "message": "ProfitCenter not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_profitcenter_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/profitcenters/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._profitcenter_service.update_profitcenter(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_profitcenter_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/profitcenters/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._profitcenter_service.delete_profitcenter(record_id)
            if not success:
                return {"status": "error", "message": "ProfitCenter not found", "code": 404}
            return {"status": "success", "message": "ProfitCenter deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_profitcenters_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/profitcenters"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._profitcenter_service.list_all_profitcenters()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_profitcenter_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/profitcenters/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._profitcenter_service.verify_profitcenter_workflow_state(record_id)
            res = self._profitcenter_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_budgetallocation_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetallocations"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgetallocation_service.create_budgetallocation(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgetallocation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetallocations/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgetallocation_service.get_budgetallocation(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetAllocation not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgetallocation_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgetallocations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgetallocation_service.update_budgetallocation(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgetallocation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgetallocations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgetallocation_service.delete_budgetallocation(record_id)
            if not success:
                return {"status": "error", "message": "BudgetAllocation not found", "code": 404}
            return {"status": "success", "message": "BudgetAllocation deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgetallocations_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetallocations"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgetallocation_service.list_all_budgetallocations()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgetallocation_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetallocations/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgetallocation_service.verify_budgetallocation_workflow_state(record_id)
            res = self._budgetallocation_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_budgetadjustment_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetadjustments"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgetadjustment_service.create_budgetadjustment(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgetadjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetadjustments/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgetadjustment_service.get_budgetadjustment(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetAdjustment not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgetadjustment_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgetadjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgetadjustment_service.update_budgetadjustment(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgetadjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgetadjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgetadjustment_service.delete_budgetadjustment(record_id)
            if not success:
                return {"status": "error", "message": "BudgetAdjustment not found", "code": 404}
            return {"status": "success", "message": "BudgetAdjustment deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgetadjustments_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetadjustments"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgetadjustment_service.list_all_budgetadjustments()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgetadjustment_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetadjustments/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgetadjustment_service.verify_budgetadjustment_workflow_state(record_id)
            res = self._budgetadjustment_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_forecastmodel_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/forecastmodels"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._forecastmodel_service.create_forecastmodel(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_forecastmodel_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/forecastmodels/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._forecastmodel_service.get_forecastmodel(record_id)
            if not obj:
                return {"status": "error", "message": "ForecastModel not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_forecastmodel_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/forecastmodels/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._forecastmodel_service.update_forecastmodel(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_forecastmodel_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/forecastmodels/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._forecastmodel_service.delete_forecastmodel(record_id)
            if not success:
                return {"status": "error", "message": "ForecastModel not found", "code": 404}
            return {"status": "success", "message": "ForecastModel deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_forecastmodels_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/forecastmodels"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._forecastmodel_service.list_all_forecastmodels()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_forecastmodel_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/forecastmodels/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._forecastmodel_service.verify_forecastmodel_workflow_state(record_id)
            res = self._forecastmodel_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_forecastscenario_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/forecastscenarios"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._forecastscenario_service.create_forecastscenario(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_forecastscenario_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/forecastscenarios/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._forecastscenario_service.get_forecastscenario(record_id)
            if not obj:
                return {"status": "error", "message": "ForecastScenario not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_forecastscenario_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/forecastscenarios/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._forecastscenario_service.update_forecastscenario(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_forecastscenario_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/forecastscenarios/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._forecastscenario_service.delete_forecastscenario(record_id)
            if not success:
                return {"status": "error", "message": "ForecastScenario not found", "code": 404}
            return {"status": "success", "message": "ForecastScenario deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_forecastscenarios_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/forecastscenarios"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._forecastscenario_service.list_all_forecastscenarios()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_forecastscenario_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/forecastscenarios/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._forecastscenario_service.verify_forecastscenario_workflow_state(record_id)
            res = self._forecastscenario_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_budgettype_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgettypes"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgettype_service.create_budgettype(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgettype_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgettypes/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgettype_service.get_budgettype(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetType not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgettype_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgettypes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgettype_service.update_budgettype(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgettype_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgettypes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgettype_service.delete_budgettype(record_id)
            if not success:
                return {"status": "error", "message": "BudgetType not found", "code": 404}
            return {"status": "success", "message": "BudgetType deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgettypes_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgettypes"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgettype_service.list_all_budgettypes()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgettype_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgettypes/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgettype_service.verify_budgettype_workflow_state(record_id)
            res = self._budgettype_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_budgetapprover_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetapprovers"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgetapprover_service.create_budgetapprover(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgetapprover_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetapprovers/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgetapprover_service.get_budgetapprover(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetApprover not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgetapprover_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgetapprovers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgetapprover_service.update_budgetapprover(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgetapprover_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgetapprovers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgetapprover_service.delete_budgetapprover(record_id)
            if not success:
                return {"status": "error", "message": "BudgetApprover not found", "code": 404}
            return {"status": "success", "message": "BudgetApprover deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgetapprovers_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetapprovers"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgetapprover_service.list_all_budgetapprovers()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgetapprover_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetapprovers/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgetapprover_service.verify_budgetapprover_workflow_state(record_id)
            res = self._budgetapprover_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_budgetthresholdalert_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetthresholdalerts"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._budgetthresholdalert_service.create_budgetthresholdalert(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_budgetthresholdalert_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetthresholdalerts/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._budgetthresholdalert_service.get_budgetthresholdalert(record_id)
            if not obj:
                return {"status": "error", "message": "BudgetThresholdAlert not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_budgetthresholdalert_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/budgetthresholdalerts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._budgetthresholdalert_service.update_budgetthresholdalert(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_budgetthresholdalert_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/budgetthresholdalerts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._budgetthresholdalert_service.delete_budgetthresholdalert(record_id)
            if not success:
                return {"status": "error", "message": "BudgetThresholdAlert not found", "code": 404}
            return {"status": "success", "message": "BudgetThresholdAlert deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_budgetthresholdalerts_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/budgetthresholdalerts"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._budgetthresholdalert_service.list_all_budgetthresholdalerts()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_budgetthresholdalert_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/budgetthresholdalerts/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._budgetthresholdalert_service.verify_budgetthresholdalert_workflow_state(record_id)
            res = self._budgetthresholdalert_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_zerobasedbudgettemplate_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/zerobasedbudgettemplates"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._zerobasedbudgettemplate_service.create_zerobasedbudgettemplate(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_zerobasedbudgettemplate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/zerobasedbudgettemplates/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            obj = self._zerobasedbudgettemplate_service.get_zerobasedbudgettemplate(record_id)
            if not obj:
                return {"status": "error", "message": "ZeroBasedBudgetTemplate not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_zerobasedbudgettemplate_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/budgeting/zerobasedbudgettemplates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "budgeting_manager"])
            obj = self._zerobasedbudgettemplate_service.update_zerobasedbudgettemplate(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_zerobasedbudgettemplate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/budgeting/zerobasedbudgettemplates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._zerobasedbudgettemplate_service.delete_zerobasedbudgettemplate(record_id)
            if not success:
                return {"status": "error", "message": "ZeroBasedBudgetTemplate not found", "code": 404}
            return {"status": "success", "message": "ZeroBasedBudgetTemplate deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_zerobasedbudgettemplates_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/budgeting/zerobasedbudgettemplates"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "budgeting_user"])
            items = self._zerobasedbudgettemplate_service.list_all_zerobasedbudgettemplates()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_zerobasedbudgettemplate_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/budgeting/zerobasedbudgettemplates/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "budgeting_user"])
            is_valid = self._zerobasedbudgettemplate_service.verify_zerobasedbudgettemplate_workflow_state(record_id)
            res = self._zerobasedbudgettemplate_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

