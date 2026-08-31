"""
AuraLedger FIXED_ASSETS Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.fixed_assets.services import AssetService
from erp.modules.fixed_assets.services import AssetCategoryService
from erp.modules.fixed_assets.services import AssetDepreciationScheduleService
from erp.modules.fixed_assets.services import AssetMaintenanceService
from erp.modules.fixed_assets.services import AssetTransferService
from erp.modules.fixed_assets.services import AssetDisposalService
from erp.modules.fixed_assets.services import AssetRevaluationService
from erp.modules.fixed_assets.services import InsurancePolicyService
from erp.modules.fixed_assets.services import AssetInsuranceClaimService
from erp.modules.fixed_assets.services import AssetLocationService
from erp.modules.fixed_assets.services import LeasedAssetRecordService
from erp.modules.fixed_assets.services import DepreciationMethodRuleService

class Fixed_assetsApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._asset_service = AssetService()
        self._assetcategory_service = AssetCategoryService()
        self._assetdepreciationschedule_service = AssetDepreciationScheduleService()
        self._assetmaintenance_service = AssetMaintenanceService()
        self._assettransfer_service = AssetTransferService()
        self._assetdisposal_service = AssetDisposalService()
        self._assetrevaluation_service = AssetRevaluationService()
        self._insurancepolicy_service = InsurancePolicyService()
        self._assetinsuranceclaim_service = AssetInsuranceClaimService()
        self._assetlocation_service = AssetLocationService()
        self._leasedassetrecord_service = LeasedAssetRecordService()
        self._depreciationmethodrule_service = DepreciationMethodRuleService()

    def create_asset_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assets"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "name" not in payload:
                return {"status": "error", "message": "Missing required parameter: name", "code": 400}
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "purchase_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: purchase_date", "code": 400}
            if "purchase_value" not in payload:
                return {"status": "error", "message": "Missing required parameter: purchase_value", "code": 400}
            if "salvage_value" not in payload:
                return {"status": "error", "message": "Missing required parameter: salvage_value", "code": 400}
            if "useful_life_years" not in payload:
                return {"status": "error", "message": "Missing required parameter: useful_life_years", "code": 400}
            obj = self._asset_service.create_asset(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_asset_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assets/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._asset_service.get_asset(record_id)
            if not obj:
                return {"status": "error", "message": "Asset not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_asset_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._asset_service.update_asset(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_asset_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._asset_service.delete_asset(record_id)
            if not success:
                return {"status": "error", "message": "Asset not found", "code": 404}
            return {"status": "success", "message": "Asset deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assets_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assets"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._asset_service.list_all_assets()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_asset_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assets/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._asset_service.verify_asset_workflow_state(record_id)
            res = self._asset_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetcategory_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetcategorys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assetcategory_service.create_assetcategory(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetcategory_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetcategorys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetcategory_service.get_assetcategory(record_id)
            if not obj:
                return {"status": "error", "message": "AssetCategory not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetcategory_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetcategorys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetcategory_service.update_assetcategory(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetcategory_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetcategorys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetcategory_service.delete_assetcategory(record_id)
            if not success:
                return {"status": "error", "message": "AssetCategory not found", "code": 404}
            return {"status": "success", "message": "AssetCategory deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetcategorys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetcategorys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetcategory_service.list_all_assetcategorys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetcategory_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetcategorys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetcategory_service.verify_assetcategory_workflow_state(record_id)
            res = self._assetcategory_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetdepreciationschedule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetdepreciationschedules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
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
            obj = self._assetdepreciationschedule_service.create_assetdepreciationschedule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetdepreciationschedule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetdepreciationschedules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetdepreciationschedule_service.get_assetdepreciationschedule(record_id)
            if not obj:
                return {"status": "error", "message": "AssetDepreciationSchedule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetdepreciationschedule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetdepreciationschedules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetdepreciationschedule_service.update_assetdepreciationschedule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetdepreciationschedule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetdepreciationschedules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetdepreciationschedule_service.delete_assetdepreciationschedule(record_id)
            if not success:
                return {"status": "error", "message": "AssetDepreciationSchedule not found", "code": 404}
            return {"status": "success", "message": "AssetDepreciationSchedule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetdepreciationschedules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetdepreciationschedules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetdepreciationschedule_service.list_all_assetdepreciationschedules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetdepreciationschedule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetdepreciationschedules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetdepreciationschedule_service.verify_assetdepreciationschedule_workflow_state(record_id)
            res = self._assetdepreciationschedule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetmaintenance_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetmaintenances"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assetmaintenance_service.create_assetmaintenance(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetmaintenance_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetmaintenances/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetmaintenance_service.get_assetmaintenance(record_id)
            if not obj:
                return {"status": "error", "message": "AssetMaintenance not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetmaintenance_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetmaintenances/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetmaintenance_service.update_assetmaintenance(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetmaintenance_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetmaintenances/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetmaintenance_service.delete_assetmaintenance(record_id)
            if not success:
                return {"status": "error", "message": "AssetMaintenance not found", "code": 404}
            return {"status": "success", "message": "AssetMaintenance deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetmaintenances_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetmaintenances"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetmaintenance_service.list_all_assetmaintenances()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetmaintenance_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetmaintenances/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetmaintenance_service.verify_assetmaintenance_workflow_state(record_id)
            res = self._assetmaintenance_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assettransfer_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assettransfers"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assettransfer_service.create_assettransfer(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assettransfer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assettransfers/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assettransfer_service.get_assettransfer(record_id)
            if not obj:
                return {"status": "error", "message": "AssetTransfer not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assettransfer_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assettransfers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assettransfer_service.update_assettransfer(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assettransfer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assettransfers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assettransfer_service.delete_assettransfer(record_id)
            if not success:
                return {"status": "error", "message": "AssetTransfer not found", "code": 404}
            return {"status": "success", "message": "AssetTransfer deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assettransfers_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assettransfers"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assettransfer_service.list_all_assettransfers()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assettransfer_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assettransfers/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assettransfer_service.verify_assettransfer_workflow_state(record_id)
            res = self._assettransfer_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetdisposal_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetdisposals"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assetdisposal_service.create_assetdisposal(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetdisposal_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetdisposals/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetdisposal_service.get_assetdisposal(record_id)
            if not obj:
                return {"status": "error", "message": "AssetDisposal not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetdisposal_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetdisposals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetdisposal_service.update_assetdisposal(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetdisposal_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetdisposals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetdisposal_service.delete_assetdisposal(record_id)
            if not success:
                return {"status": "error", "message": "AssetDisposal not found", "code": 404}
            return {"status": "success", "message": "AssetDisposal deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetdisposals_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetdisposals"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetdisposal_service.list_all_assetdisposals()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetdisposal_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetdisposals/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetdisposal_service.verify_assetdisposal_workflow_state(record_id)
            res = self._assetdisposal_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetrevaluation_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetrevaluations"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assetrevaluation_service.create_assetrevaluation(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetrevaluation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetrevaluations/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetrevaluation_service.get_assetrevaluation(record_id)
            if not obj:
                return {"status": "error", "message": "AssetRevaluation not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetrevaluation_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetrevaluations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetrevaluation_service.update_assetrevaluation(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetrevaluation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetrevaluations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetrevaluation_service.delete_assetrevaluation(record_id)
            if not success:
                return {"status": "error", "message": "AssetRevaluation not found", "code": 404}
            return {"status": "success", "message": "AssetRevaluation deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetrevaluations_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetrevaluations"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetrevaluation_service.list_all_assetrevaluations()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetrevaluation_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetrevaluations/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetrevaluation_service.verify_assetrevaluation_workflow_state(record_id)
            res = self._assetrevaluation_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_insurancepolicy_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/insurancepolicys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._insurancepolicy_service.create_insurancepolicy(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_insurancepolicy_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/insurancepolicys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._insurancepolicy_service.get_insurancepolicy(record_id)
            if not obj:
                return {"status": "error", "message": "InsurancePolicy not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_insurancepolicy_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/insurancepolicys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._insurancepolicy_service.update_insurancepolicy(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_insurancepolicy_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/insurancepolicys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._insurancepolicy_service.delete_insurancepolicy(record_id)
            if not success:
                return {"status": "error", "message": "InsurancePolicy not found", "code": 404}
            return {"status": "success", "message": "InsurancePolicy deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_insurancepolicys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/insurancepolicys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._insurancepolicy_service.list_all_insurancepolicys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_insurancepolicy_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/insurancepolicys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._insurancepolicy_service.verify_insurancepolicy_workflow_state(record_id)
            res = self._insurancepolicy_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetinsuranceclaim_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetinsuranceclaims"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assetinsuranceclaim_service.create_assetinsuranceclaim(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetinsuranceclaim_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetinsuranceclaims/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetinsuranceclaim_service.get_assetinsuranceclaim(record_id)
            if not obj:
                return {"status": "error", "message": "AssetInsuranceClaim not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetinsuranceclaim_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetinsuranceclaims/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetinsuranceclaim_service.update_assetinsuranceclaim(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetinsuranceclaim_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetinsuranceclaims/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetinsuranceclaim_service.delete_assetinsuranceclaim(record_id)
            if not success:
                return {"status": "error", "message": "AssetInsuranceClaim not found", "code": 404}
            return {"status": "success", "message": "AssetInsuranceClaim deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetinsuranceclaims_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetinsuranceclaims"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetinsuranceclaim_service.list_all_assetinsuranceclaims()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetinsuranceclaim_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetinsuranceclaims/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetinsuranceclaim_service.verify_assetinsuranceclaim_workflow_state(record_id)
            res = self._assetinsuranceclaim_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_assetlocation_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetlocations"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._assetlocation_service.create_assetlocation(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_assetlocation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetlocations/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._assetlocation_service.get_assetlocation(record_id)
            if not obj:
                return {"status": "error", "message": "AssetLocation not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_assetlocation_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/assetlocations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._assetlocation_service.update_assetlocation(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_assetlocation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/assetlocations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._assetlocation_service.delete_assetlocation(record_id)
            if not success:
                return {"status": "error", "message": "AssetLocation not found", "code": 404}
            return {"status": "success", "message": "AssetLocation deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_assetlocations_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/assetlocations"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._assetlocation_service.list_all_assetlocations()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_assetlocation_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/assetlocations/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._assetlocation_service.verify_assetlocation_workflow_state(record_id)
            res = self._assetlocation_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_leasedassetrecord_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/leasedassetrecords"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._leasedassetrecord_service.create_leasedassetrecord(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_leasedassetrecord_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/leasedassetrecords/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._leasedassetrecord_service.get_leasedassetrecord(record_id)
            if not obj:
                return {"status": "error", "message": "LeasedAssetRecord not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_leasedassetrecord_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/leasedassetrecords/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._leasedassetrecord_service.update_leasedassetrecord(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_leasedassetrecord_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/leasedassetrecords/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._leasedassetrecord_service.delete_leasedassetrecord(record_id)
            if not success:
                return {"status": "error", "message": "LeasedAssetRecord not found", "code": 404}
            return {"status": "success", "message": "LeasedAssetRecord deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_leasedassetrecords_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/leasedassetrecords"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._leasedassetrecord_service.list_all_leasedassetrecords()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_leasedassetrecord_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/leasedassetrecords/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._leasedassetrecord_service.verify_leasedassetrecord_workflow_state(record_id)
            res = self._leasedassetrecord_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_depreciationmethodrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/depreciationmethodrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._depreciationmethodrule_service.create_depreciationmethodrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_depreciationmethodrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/depreciationmethodrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            obj = self._depreciationmethodrule_service.get_depreciationmethodrule(record_id)
            if not obj:
                return {"status": "error", "message": "DepreciationMethodRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_depreciationmethodrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/fixed_assets/depreciationmethodrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "fixed_assets_manager"])
            obj = self._depreciationmethodrule_service.update_depreciationmethodrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_depreciationmethodrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/fixed_assets/depreciationmethodrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._depreciationmethodrule_service.delete_depreciationmethodrule(record_id)
            if not success:
                return {"status": "error", "message": "DepreciationMethodRule not found", "code": 404}
            return {"status": "success", "message": "DepreciationMethodRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_depreciationmethodrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/fixed_assets/depreciationmethodrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "fixed_assets_user"])
            items = self._depreciationmethodrule_service.list_all_depreciationmethodrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_depreciationmethodrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/fixed_assets/depreciationmethodrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "fixed_assets_user"])
            is_valid = self._depreciationmethodrule_service.verify_depreciationmethodrule_workflow_state(record_id)
            res = self._depreciationmethodrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

