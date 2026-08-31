"""
AuraLedger COST_ACCOUNTING Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.cost_accounting.services import CostObjectService
from erp.modules.cost_accounting.services import CostPoolService
from erp.modules.cost_accounting.services import CostDriverService
from erp.modules.cost_accounting.services import AllocationRuleService
from erp.modules.cost_accounting.services import CostAllocationRunService
from erp.modules.cost_accounting.services import ActivityRateService
from erp.modules.cost_accounting.services import DirectExpenseService
from erp.modules.cost_accounting.services import OverheadRateService
from erp.modules.cost_accounting.services import CostDistributionService
from erp.modules.cost_accounting.services import CostRateSheetService
from erp.modules.cost_accounting.services import CostAllocationMapService
from erp.modules.cost_accounting.services import ActivityCostPoolService

class Cost_accountingApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._costobject_service = CostObjectService()
        self._costpool_service = CostPoolService()
        self._costdriver_service = CostDriverService()
        self._allocationrule_service = AllocationRuleService()
        self._costallocationrun_service = CostAllocationRunService()
        self._activityrate_service = ActivityRateService()
        self._directexpense_service = DirectExpenseService()
        self._overheadrate_service = OverheadRateService()
        self._costdistribution_service = CostDistributionService()
        self._costratesheet_service = CostRateSheetService()
        self._costallocationmap_service = CostAllocationMapService()
        self._activitycostpool_service = ActivityCostPoolService()

    def create_costobject_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costobjects"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._costobject_service.create_costobject(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costobject_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costobjects/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costobject_service.get_costobject(record_id)
            if not obj:
                return {"status": "error", "message": "CostObject not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costobject_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costobjects/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costobject_service.update_costobject(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costobject_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costobjects/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costobject_service.delete_costobject(record_id)
            if not success:
                return {"status": "error", "message": "CostObject not found", "code": 404}
            return {"status": "success", "message": "CostObject deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costobjects_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costobjects"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costobject_service.list_all_costobjects()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costobject_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costobjects/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costobject_service.verify_costobject_workflow_state(record_id)
            res = self._costobject_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costpool_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costpools"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._costpool_service.create_costpool(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costpool_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costpools/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costpool_service.get_costpool(record_id)
            if not obj:
                return {"status": "error", "message": "CostPool not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costpool_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costpools/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costpool_service.update_costpool(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costpool_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costpools/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costpool_service.delete_costpool(record_id)
            if not success:
                return {"status": "error", "message": "CostPool not found", "code": 404}
            return {"status": "success", "message": "CostPool deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costpools_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costpools"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costpool_service.list_all_costpools()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costpool_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costpools/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costpool_service.verify_costpool_workflow_state(record_id)
            res = self._costpool_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costdriver_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costdrivers"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._costdriver_service.create_costdriver(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costdriver_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costdrivers/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costdriver_service.get_costdriver(record_id)
            if not obj:
                return {"status": "error", "message": "CostDriver not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costdriver_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costdrivers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costdriver_service.update_costdriver(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costdriver_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costdrivers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costdriver_service.delete_costdriver(record_id)
            if not success:
                return {"status": "error", "message": "CostDriver not found", "code": 404}
            return {"status": "success", "message": "CostDriver deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costdrivers_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costdrivers"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costdriver_service.list_all_costdrivers()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costdriver_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costdrivers/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costdriver_service.verify_costdriver_workflow_state(record_id)
            res = self._costdriver_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_allocationrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/allocationrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._allocationrule_service.create_allocationrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_allocationrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/allocationrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._allocationrule_service.get_allocationrule(record_id)
            if not obj:
                return {"status": "error", "message": "AllocationRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_allocationrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/allocationrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._allocationrule_service.update_allocationrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_allocationrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/allocationrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._allocationrule_service.delete_allocationrule(record_id)
            if not success:
                return {"status": "error", "message": "AllocationRule not found", "code": 404}
            return {"status": "success", "message": "AllocationRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_allocationrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/allocationrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._allocationrule_service.list_all_allocationrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_allocationrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/allocationrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._allocationrule_service.verify_allocationrule_workflow_state(record_id)
            res = self._allocationrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costallocationrun_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costallocationruns"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "amount" not in payload:
                return {"status": "error", "message": "Missing required parameter: amount", "code": 400}
            if "base_currency" not in payload:
                return {"status": "error", "message": "Missing required parameter: base_currency", "code": 400}
            if "scheduled_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: scheduled_date", "code": 400}
            if "period_code" not in payload:
                return {"status": "error", "message": "Missing required parameter: period_code", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._costallocationrun_service.create_costallocationrun(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costallocationrun_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costallocationruns/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costallocationrun_service.get_costallocationrun(record_id)
            if not obj:
                return {"status": "error", "message": "CostAllocationRun not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costallocationrun_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costallocationruns/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costallocationrun_service.update_costallocationrun(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costallocationrun_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costallocationruns/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costallocationrun_service.delete_costallocationrun(record_id)
            if not success:
                return {"status": "error", "message": "CostAllocationRun not found", "code": 404}
            return {"status": "success", "message": "CostAllocationRun deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costallocationruns_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costallocationruns"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costallocationrun_service.list_all_costallocationruns()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costallocationrun_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costallocationruns/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costallocationrun_service.verify_costallocationrun_workflow_state(record_id)
            res = self._costallocationrun_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_activityrate_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/activityrates"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._activityrate_service.create_activityrate(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_activityrate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/activityrates/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._activityrate_service.get_activityrate(record_id)
            if not obj:
                return {"status": "error", "message": "ActivityRate not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_activityrate_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/activityrates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._activityrate_service.update_activityrate(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_activityrate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/activityrates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._activityrate_service.delete_activityrate(record_id)
            if not success:
                return {"status": "error", "message": "ActivityRate not found", "code": 404}
            return {"status": "success", "message": "ActivityRate deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_activityrates_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/activityrates"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._activityrate_service.list_all_activityrates()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_activityrate_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/activityrates/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._activityrate_service.verify_activityrate_workflow_state(record_id)
            res = self._activityrate_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_directexpense_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/directexpenses"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._directexpense_service.create_directexpense(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_directexpense_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/directexpenses/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._directexpense_service.get_directexpense(record_id)
            if not obj:
                return {"status": "error", "message": "DirectExpense not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_directexpense_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/directexpenses/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._directexpense_service.update_directexpense(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_directexpense_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/directexpenses/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._directexpense_service.delete_directexpense(record_id)
            if not success:
                return {"status": "error", "message": "DirectExpense not found", "code": 404}
            return {"status": "success", "message": "DirectExpense deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_directexpenses_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/directexpenses"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._directexpense_service.list_all_directexpenses()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_directexpense_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/directexpenses/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._directexpense_service.verify_directexpense_workflow_state(record_id)
            res = self._directexpense_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_overheadrate_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/overheadrates"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._overheadrate_service.create_overheadrate(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_overheadrate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/overheadrates/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._overheadrate_service.get_overheadrate(record_id)
            if not obj:
                return {"status": "error", "message": "OverheadRate not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_overheadrate_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/overheadrates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._overheadrate_service.update_overheadrate(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_overheadrate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/overheadrates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._overheadrate_service.delete_overheadrate(record_id)
            if not success:
                return {"status": "error", "message": "OverheadRate not found", "code": 404}
            return {"status": "success", "message": "OverheadRate deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_overheadrates_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/overheadrates"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._overheadrate_service.list_all_overheadrates()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_overheadrate_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/overheadrates/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._overheadrate_service.verify_overheadrate_workflow_state(record_id)
            res = self._overheadrate_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costdistribution_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costdistributions"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._costdistribution_service.create_costdistribution(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costdistribution_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costdistributions/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costdistribution_service.get_costdistribution(record_id)
            if not obj:
                return {"status": "error", "message": "CostDistribution not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costdistribution_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costdistributions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costdistribution_service.update_costdistribution(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costdistribution_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costdistributions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costdistribution_service.delete_costdistribution(record_id)
            if not success:
                return {"status": "error", "message": "CostDistribution not found", "code": 404}
            return {"status": "success", "message": "CostDistribution deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costdistributions_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costdistributions"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costdistribution_service.list_all_costdistributions()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costdistribution_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costdistributions/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costdistribution_service.verify_costdistribution_workflow_state(record_id)
            res = self._costdistribution_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costratesheet_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costratesheets"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._costratesheet_service.create_costratesheet(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costratesheet_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costratesheets/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costratesheet_service.get_costratesheet(record_id)
            if not obj:
                return {"status": "error", "message": "CostRateSheet not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costratesheet_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costratesheets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costratesheet_service.update_costratesheet(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costratesheet_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costratesheets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costratesheet_service.delete_costratesheet(record_id)
            if not success:
                return {"status": "error", "message": "CostRateSheet not found", "code": 404}
            return {"status": "success", "message": "CostRateSheet deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costratesheets_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costratesheets"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costratesheet_service.list_all_costratesheets()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costratesheet_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costratesheets/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costratesheet_service.verify_costratesheet_workflow_state(record_id)
            res = self._costratesheet_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costallocationmap_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costallocationmaps"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._costallocationmap_service.create_costallocationmap(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costallocationmap_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costallocationmaps/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._costallocationmap_service.get_costallocationmap(record_id)
            if not obj:
                return {"status": "error", "message": "CostAllocationMap not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costallocationmap_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/costallocationmaps/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._costallocationmap_service.update_costallocationmap(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costallocationmap_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/costallocationmaps/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costallocationmap_service.delete_costallocationmap(record_id)
            if not success:
                return {"status": "error", "message": "CostAllocationMap not found", "code": 404}
            return {"status": "success", "message": "CostAllocationMap deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costallocationmaps_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/costallocationmaps"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._costallocationmap_service.list_all_costallocationmaps()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costallocationmap_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/costallocationmaps/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._costallocationmap_service.verify_costallocationmap_workflow_state(record_id)
            res = self._costallocationmap_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_activitycostpool_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/activitycostpools"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
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
            obj = self._activitycostpool_service.create_activitycostpool(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_activitycostpool_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/activitycostpools/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            obj = self._activitycostpool_service.get_activitycostpool(record_id)
            if not obj:
                return {"status": "error", "message": "ActivityCostPool not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_activitycostpool_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/cost_accounting/activitycostpools/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "cost_accounting_manager"])
            obj = self._activitycostpool_service.update_activitycostpool(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_activitycostpool_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/cost_accounting/activitycostpools/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._activitycostpool_service.delete_activitycostpool(record_id)
            if not success:
                return {"status": "error", "message": "ActivityCostPool not found", "code": 404}
            return {"status": "success", "message": "ActivityCostPool deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_activitycostpools_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/cost_accounting/activitycostpools"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "cost_accounting_user"])
            items = self._activitycostpool_service.list_all_activitycostpools()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_activitycostpool_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/cost_accounting/activitycostpools/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "cost_accounting_user"])
            is_valid = self._activitycostpool_service.verify_activitycostpool_workflow_state(record_id)
            res = self._activitycostpool_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

