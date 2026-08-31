"""
AuraLedger TAX_MANAGEMENT Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.tax_management.services import TaxCodeService
from erp.modules.tax_management.services import TaxRateService
from erp.modules.tax_management.services import TaxGroupService
from erp.modules.tax_management.services import TaxTransactionService
from erp.modules.tax_management.services import TaxAuthorityService
from erp.modules.tax_management.services import TaxFilingService
from erp.modules.tax_management.services import TaxAdjustmentService
from erp.modules.tax_management.services import TaxReconciliationService
from erp.modules.tax_management.services import TaxExemptionService
from erp.modules.tax_management.services import TaxFilingPeriodService
from erp.modules.tax_management.services import TaxNexusRegistryService
from erp.modules.tax_management.services import WithholdingTaxRuleService

class Tax_managementApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._taxcode_service = TaxCodeService()
        self._taxrate_service = TaxRateService()
        self._taxgroup_service = TaxGroupService()
        self._taxtransaction_service = TaxTransactionService()
        self._taxauthority_service = TaxAuthorityService()
        self._taxfiling_service = TaxFilingService()
        self._taxadjustment_service = TaxAdjustmentService()
        self._taxreconciliation_service = TaxReconciliationService()
        self._taxexemption_service = TaxExemptionService()
        self._taxfilingperiod_service = TaxFilingPeriodService()
        self._taxnexusregistry_service = TaxNexusRegistryService()
        self._withholdingtaxrule_service = WithholdingTaxRuleService()

    def create_taxcode_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxcodes"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxcode_service.create_taxcode(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxcode_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxcodes/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxcode_service.get_taxcode(record_id)
            if not obj:
                return {"status": "error", "message": "TaxCode not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxcode_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxcodes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxcode_service.update_taxcode(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxcode_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxcodes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxcode_service.delete_taxcode(record_id)
            if not success:
                return {"status": "error", "message": "TaxCode not found", "code": 404}
            return {"status": "success", "message": "TaxCode deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxcodes_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxcodes"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxcode_service.list_all_taxcodes()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxcode_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxcodes/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxcode_service.verify_taxcode_workflow_state(record_id)
            res = self._taxcode_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxrate_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxrates"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxrate_service.create_taxrate(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxrate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxrates/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxrate_service.get_taxrate(record_id)
            if not obj:
                return {"status": "error", "message": "TaxRate not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxrate_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxrates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxrate_service.update_taxrate(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxrate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxrates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxrate_service.delete_taxrate(record_id)
            if not success:
                return {"status": "error", "message": "TaxRate not found", "code": 404}
            return {"status": "success", "message": "TaxRate deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxrates_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxrates"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxrate_service.list_all_taxrates()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxrate_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxrates/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxrate_service.verify_taxrate_workflow_state(record_id)
            res = self._taxrate_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxgroup_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxgroups"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxgroup_service.create_taxgroup(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxgroup_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxgroups/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxgroup_service.get_taxgroup(record_id)
            if not obj:
                return {"status": "error", "message": "TaxGroup not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxgroup_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxgroups/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxgroup_service.update_taxgroup(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxgroup_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxgroups/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxgroup_service.delete_taxgroup(record_id)
            if not success:
                return {"status": "error", "message": "TaxGroup not found", "code": 404}
            return {"status": "success", "message": "TaxGroup deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxgroups_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxgroups"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxgroup_service.list_all_taxgroups()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxgroup_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxgroups/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxgroup_service.verify_taxgroup_workflow_state(record_id)
            res = self._taxgroup_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxtransaction_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxtransactions"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxtransaction_service.create_taxtransaction(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxtransaction_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxtransactions/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxtransaction_service.get_taxtransaction(record_id)
            if not obj:
                return {"status": "error", "message": "TaxTransaction not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxtransaction_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxtransactions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxtransaction_service.update_taxtransaction(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxtransaction_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxtransactions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxtransaction_service.delete_taxtransaction(record_id)
            if not success:
                return {"status": "error", "message": "TaxTransaction not found", "code": 404}
            return {"status": "success", "message": "TaxTransaction deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxtransactions_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxtransactions"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxtransaction_service.list_all_taxtransactions()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxtransaction_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxtransactions/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxtransaction_service.verify_taxtransaction_workflow_state(record_id)
            res = self._taxtransaction_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxauthority_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxauthoritys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxauthority_service.create_taxauthority(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxauthority_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxauthoritys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxauthority_service.get_taxauthority(record_id)
            if not obj:
                return {"status": "error", "message": "TaxAuthority not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxauthority_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxauthoritys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxauthority_service.update_taxauthority(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxauthority_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxauthoritys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxauthority_service.delete_taxauthority(record_id)
            if not success:
                return {"status": "error", "message": "TaxAuthority not found", "code": 404}
            return {"status": "success", "message": "TaxAuthority deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxauthoritys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxauthoritys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxauthority_service.list_all_taxauthoritys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxauthority_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxauthoritys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxauthority_service.verify_taxauthority_workflow_state(record_id)
            res = self._taxauthority_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxfiling_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxfilings"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxfiling_service.create_taxfiling(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxfiling_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxfilings/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxfiling_service.get_taxfiling(record_id)
            if not obj:
                return {"status": "error", "message": "TaxFiling not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxfiling_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxfilings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxfiling_service.update_taxfiling(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxfiling_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxfilings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxfiling_service.delete_taxfiling(record_id)
            if not success:
                return {"status": "error", "message": "TaxFiling not found", "code": 404}
            return {"status": "success", "message": "TaxFiling deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxfilings_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxfilings"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxfiling_service.list_all_taxfilings()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxfiling_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxfilings/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxfiling_service.verify_taxfiling_workflow_state(record_id)
            res = self._taxfiling_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxadjustment_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxadjustments"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxadjustment_service.create_taxadjustment(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxadjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxadjustments/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxadjustment_service.get_taxadjustment(record_id)
            if not obj:
                return {"status": "error", "message": "TaxAdjustment not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxadjustment_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxadjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxadjustment_service.update_taxadjustment(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxadjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxadjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxadjustment_service.delete_taxadjustment(record_id)
            if not success:
                return {"status": "error", "message": "TaxAdjustment not found", "code": 404}
            return {"status": "success", "message": "TaxAdjustment deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxadjustments_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxadjustments"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxadjustment_service.list_all_taxadjustments()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxadjustment_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxadjustments/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxadjustment_service.verify_taxadjustment_workflow_state(record_id)
            res = self._taxadjustment_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxreconciliation_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxreconciliations"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxreconciliation_service.create_taxreconciliation(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxreconciliation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxreconciliation_service.get_taxreconciliation(record_id)
            if not obj:
                return {"status": "error", "message": "TaxReconciliation not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxreconciliation_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxreconciliation_service.update_taxreconciliation(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxreconciliation_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxreconciliations/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxreconciliation_service.delete_taxreconciliation(record_id)
            if not success:
                return {"status": "error", "message": "TaxReconciliation not found", "code": 404}
            return {"status": "success", "message": "TaxReconciliation deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxreconciliations_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxreconciliations"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxreconciliation_service.list_all_taxreconciliations()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxreconciliation_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxreconciliations/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxreconciliation_service.verify_taxreconciliation_workflow_state(record_id)
            res = self._taxreconciliation_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxexemption_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxexemptions"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxexemption_service.create_taxexemption(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxexemption_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxexemptions/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxexemption_service.get_taxexemption(record_id)
            if not obj:
                return {"status": "error", "message": "TaxExemption not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxexemption_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxexemptions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxexemption_service.update_taxexemption(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxexemption_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxexemptions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxexemption_service.delete_taxexemption(record_id)
            if not success:
                return {"status": "error", "message": "TaxExemption not found", "code": 404}
            return {"status": "success", "message": "TaxExemption deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxexemptions_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxexemptions"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxexemption_service.list_all_taxexemptions()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxexemption_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxexemptions/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxexemption_service.verify_taxexemption_workflow_state(record_id)
            res = self._taxexemption_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxfilingperiod_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxfilingperiods"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxfilingperiod_service.create_taxfilingperiod(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxfilingperiod_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxfilingperiods/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxfilingperiod_service.get_taxfilingperiod(record_id)
            if not obj:
                return {"status": "error", "message": "TaxFilingPeriod not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxfilingperiod_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxfilingperiods/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxfilingperiod_service.update_taxfilingperiod(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxfilingperiod_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxfilingperiods/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxfilingperiod_service.delete_taxfilingperiod(record_id)
            if not success:
                return {"status": "error", "message": "TaxFilingPeriod not found", "code": 404}
            return {"status": "success", "message": "TaxFilingPeriod deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxfilingperiods_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxfilingperiods"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxfilingperiod_service.list_all_taxfilingperiods()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxfilingperiod_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxfilingperiods/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxfilingperiod_service.verify_taxfilingperiod_workflow_state(record_id)
            res = self._taxfilingperiod_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_taxnexusregistry_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxnexusregistrys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._taxnexusregistry_service.create_taxnexusregistry(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_taxnexusregistry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxnexusregistrys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._taxnexusregistry_service.get_taxnexusregistry(record_id)
            if not obj:
                return {"status": "error", "message": "TaxNexusRegistry not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_taxnexusregistry_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/taxnexusregistrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._taxnexusregistry_service.update_taxnexusregistry(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_taxnexusregistry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/taxnexusregistrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._taxnexusregistry_service.delete_taxnexusregistry(record_id)
            if not success:
                return {"status": "error", "message": "TaxNexusRegistry not found", "code": 404}
            return {"status": "success", "message": "TaxNexusRegistry deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_taxnexusregistrys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/taxnexusregistrys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._taxnexusregistry_service.list_all_taxnexusregistrys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_taxnexusregistry_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/taxnexusregistrys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._taxnexusregistry_service.verify_taxnexusregistry_workflow_state(record_id)
            res = self._taxnexusregistry_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_withholdingtaxrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/withholdingtaxrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
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
            obj = self._withholdingtaxrule_service.create_withholdingtaxrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_withholdingtaxrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/withholdingtaxrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            obj = self._withholdingtaxrule_service.get_withholdingtaxrule(record_id)
            if not obj:
                return {"status": "error", "message": "WithholdingTaxRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_withholdingtaxrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/tax_management/withholdingtaxrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "tax_management_manager"])
            obj = self._withholdingtaxrule_service.update_withholdingtaxrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_withholdingtaxrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/tax_management/withholdingtaxrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._withholdingtaxrule_service.delete_withholdingtaxrule(record_id)
            if not success:
                return {"status": "error", "message": "WithholdingTaxRule not found", "code": 404}
            return {"status": "success", "message": "WithholdingTaxRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_withholdingtaxrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/tax_management/withholdingtaxrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "tax_management_user"])
            items = self._withholdingtaxrule_service.list_all_withholdingtaxrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_withholdingtaxrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/tax_management/withholdingtaxrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "tax_management_user"])
            is_valid = self._withholdingtaxrule_service.verify_withholdingtaxrule_workflow_state(record_id)
            res = self._withholdingtaxrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

