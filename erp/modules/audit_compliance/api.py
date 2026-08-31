"""
AuraLedger AUDIT_COMPLIANCE Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.audit_compliance.services import AuditTrailLogService
from erp.modules.audit_compliance.services import AccessControlLogService
from erp.modules.audit_compliance.services import ComplianceRuleService
from erp.modules.audit_compliance.services import ComplianceCheckRunService
from erp.modules.audit_compliance.services import ReconciliationAnomalyService
from erp.modules.audit_compliance.services import ApprovalChainService
from erp.modules.audit_compliance.services import ApprovalStepService
from erp.modules.audit_compliance.services import SystemSettingChangeService
from erp.modules.audit_compliance.services import AuditChecklistService
from erp.modules.audit_compliance.services import ComplianceExceptionService
from erp.modules.audit_compliance.services import ComplianceAuditScheduleService
from erp.modules.audit_compliance.services import SOXControlPointService

class Audit_complianceApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._audittraillog_service = AuditTrailLogService()
        self._accesscontrollog_service = AccessControlLogService()
        self._compliancerule_service = ComplianceRuleService()
        self._compliancecheckrun_service = ComplianceCheckRunService()
        self._reconciliationanomaly_service = ReconciliationAnomalyService()
        self._approvalchain_service = ApprovalChainService()
        self._approvalstep_service = ApprovalStepService()
        self._systemsettingchange_service = SystemSettingChangeService()
        self._auditchecklist_service = AuditChecklistService()
        self._complianceexception_service = ComplianceExceptionService()
        self._complianceauditschedule_service = ComplianceAuditScheduleService()
        self._soxcontrolpoint_service = SOXControlPointService()

    def create_audittraillog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/audittraillogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._audittraillog_service.create_audittraillog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_audittraillog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/audittraillogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._audittraillog_service.get_audittraillog(record_id)
            if not obj:
                return {"status": "error", "message": "AuditTrailLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_audittraillog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/audittraillogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._audittraillog_service.update_audittraillog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_audittraillog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/audittraillogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._audittraillog_service.delete_audittraillog(record_id)
            if not success:
                return {"status": "error", "message": "AuditTrailLog not found", "code": 404}
            return {"status": "success", "message": "AuditTrailLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_audittraillogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/audittraillogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._audittraillog_service.list_all_audittraillogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_audittraillog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/audittraillogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._audittraillog_service.verify_audittraillog_workflow_state(record_id)
            res = self._audittraillog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_accesscontrollog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/accesscontrollogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._accesscontrollog_service.create_accesscontrollog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_accesscontrollog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/accesscontrollogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._accesscontrollog_service.get_accesscontrollog(record_id)
            if not obj:
                return {"status": "error", "message": "AccessControlLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_accesscontrollog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/accesscontrollogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._accesscontrollog_service.update_accesscontrollog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_accesscontrollog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/accesscontrollogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._accesscontrollog_service.delete_accesscontrollog(record_id)
            if not success:
                return {"status": "error", "message": "AccessControlLog not found", "code": 404}
            return {"status": "success", "message": "AccessControlLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_accesscontrollogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/accesscontrollogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._accesscontrollog_service.list_all_accesscontrollogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_accesscontrollog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/accesscontrollogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._accesscontrollog_service.verify_accesscontrollog_workflow_state(record_id)
            res = self._accesscontrollog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_compliancerule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/compliancerules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._compliancerule_service.create_compliancerule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_compliancerule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/compliancerules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._compliancerule_service.get_compliancerule(record_id)
            if not obj:
                return {"status": "error", "message": "ComplianceRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_compliancerule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/compliancerules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._compliancerule_service.update_compliancerule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_compliancerule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/compliancerules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._compliancerule_service.delete_compliancerule(record_id)
            if not success:
                return {"status": "error", "message": "ComplianceRule not found", "code": 404}
            return {"status": "success", "message": "ComplianceRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_compliancerules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/compliancerules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._compliancerule_service.list_all_compliancerules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_compliancerule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/compliancerules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._compliancerule_service.verify_compliancerule_workflow_state(record_id)
            res = self._compliancerule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_compliancecheckrun_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/compliancecheckruns"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
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
            obj = self._compliancecheckrun_service.create_compliancecheckrun(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_compliancecheckrun_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/compliancecheckruns/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._compliancecheckrun_service.get_compliancecheckrun(record_id)
            if not obj:
                return {"status": "error", "message": "ComplianceCheckRun not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_compliancecheckrun_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/compliancecheckruns/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._compliancecheckrun_service.update_compliancecheckrun(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_compliancecheckrun_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/compliancecheckruns/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._compliancecheckrun_service.delete_compliancecheckrun(record_id)
            if not success:
                return {"status": "error", "message": "ComplianceCheckRun not found", "code": 404}
            return {"status": "success", "message": "ComplianceCheckRun deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_compliancecheckruns_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/compliancecheckruns"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._compliancecheckrun_service.list_all_compliancecheckruns()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_compliancecheckrun_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/compliancecheckruns/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._compliancecheckrun_service.verify_compliancecheckrun_workflow_state(record_id)
            res = self._compliancecheckrun_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_reconciliationanomaly_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/reconciliationanomalys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._reconciliationanomaly_service.create_reconciliationanomaly(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_reconciliationanomaly_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/reconciliationanomalys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._reconciliationanomaly_service.get_reconciliationanomaly(record_id)
            if not obj:
                return {"status": "error", "message": "ReconciliationAnomaly not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_reconciliationanomaly_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/reconciliationanomalys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._reconciliationanomaly_service.update_reconciliationanomaly(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_reconciliationanomaly_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/reconciliationanomalys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._reconciliationanomaly_service.delete_reconciliationanomaly(record_id)
            if not success:
                return {"status": "error", "message": "ReconciliationAnomaly not found", "code": 404}
            return {"status": "success", "message": "ReconciliationAnomaly deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_reconciliationanomalys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/reconciliationanomalys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._reconciliationanomaly_service.list_all_reconciliationanomalys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_reconciliationanomaly_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/reconciliationanomalys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._reconciliationanomaly_service.verify_reconciliationanomaly_workflow_state(record_id)
            res = self._reconciliationanomaly_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_approvalchain_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/approvalchains"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._approvalchain_service.create_approvalchain(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_approvalchain_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/approvalchains/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._approvalchain_service.get_approvalchain(record_id)
            if not obj:
                return {"status": "error", "message": "ApprovalChain not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_approvalchain_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/approvalchains/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._approvalchain_service.update_approvalchain(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_approvalchain_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/approvalchains/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._approvalchain_service.delete_approvalchain(record_id)
            if not success:
                return {"status": "error", "message": "ApprovalChain not found", "code": 404}
            return {"status": "success", "message": "ApprovalChain deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_approvalchains_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/approvalchains"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._approvalchain_service.list_all_approvalchains()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_approvalchain_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/approvalchains/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._approvalchain_service.verify_approvalchain_workflow_state(record_id)
            res = self._approvalchain_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_approvalstep_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/approvalsteps"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
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
            obj = self._approvalstep_service.create_approvalstep(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_approvalstep_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/approvalsteps/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._approvalstep_service.get_approvalstep(record_id)
            if not obj:
                return {"status": "error", "message": "ApprovalStep not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_approvalstep_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/approvalsteps/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._approvalstep_service.update_approvalstep(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_approvalstep_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/approvalsteps/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._approvalstep_service.delete_approvalstep(record_id)
            if not success:
                return {"status": "error", "message": "ApprovalStep not found", "code": 404}
            return {"status": "success", "message": "ApprovalStep deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_approvalsteps_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/approvalsteps"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._approvalstep_service.list_all_approvalsteps()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_approvalstep_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/approvalsteps/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._approvalstep_service.verify_approvalstep_workflow_state(record_id)
            res = self._approvalstep_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_systemsettingchange_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/systemsettingchanges"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._systemsettingchange_service.create_systemsettingchange(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_systemsettingchange_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/systemsettingchanges/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._systemsettingchange_service.get_systemsettingchange(record_id)
            if not obj:
                return {"status": "error", "message": "SystemSettingChange not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_systemsettingchange_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/systemsettingchanges/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._systemsettingchange_service.update_systemsettingchange(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_systemsettingchange_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/systemsettingchanges/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._systemsettingchange_service.delete_systemsettingchange(record_id)
            if not success:
                return {"status": "error", "message": "SystemSettingChange not found", "code": 404}
            return {"status": "success", "message": "SystemSettingChange deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_systemsettingchanges_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/systemsettingchanges"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._systemsettingchange_service.list_all_systemsettingchanges()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_systemsettingchange_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/systemsettingchanges/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._systemsettingchange_service.verify_systemsettingchange_workflow_state(record_id)
            res = self._systemsettingchange_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_auditchecklist_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/auditchecklists"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._auditchecklist_service.create_auditchecklist(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_auditchecklist_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/auditchecklists/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._auditchecklist_service.get_auditchecklist(record_id)
            if not obj:
                return {"status": "error", "message": "AuditChecklist not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_auditchecklist_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/auditchecklists/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._auditchecklist_service.update_auditchecklist(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_auditchecklist_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/auditchecklists/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._auditchecklist_service.delete_auditchecklist(record_id)
            if not success:
                return {"status": "error", "message": "AuditChecklist not found", "code": 404}
            return {"status": "success", "message": "AuditChecklist deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_auditchecklists_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/auditchecklists"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._auditchecklist_service.list_all_auditchecklists()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_auditchecklist_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/auditchecklists/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._auditchecklist_service.verify_auditchecklist_workflow_state(record_id)
            res = self._auditchecklist_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_complianceexception_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/complianceexceptions"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._complianceexception_service.create_complianceexception(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_complianceexception_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/complianceexceptions/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._complianceexception_service.get_complianceexception(record_id)
            if not obj:
                return {"status": "error", "message": "ComplianceException not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_complianceexception_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/complianceexceptions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._complianceexception_service.update_complianceexception(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_complianceexception_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/complianceexceptions/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._complianceexception_service.delete_complianceexception(record_id)
            if not success:
                return {"status": "error", "message": "ComplianceException not found", "code": 404}
            return {"status": "success", "message": "ComplianceException deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_complianceexceptions_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/complianceexceptions"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._complianceexception_service.list_all_complianceexceptions()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_complianceexception_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/complianceexceptions/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._complianceexception_service.verify_complianceexception_workflow_state(record_id)
            res = self._complianceexception_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_complianceauditschedule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/complianceauditschedules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
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
            obj = self._complianceauditschedule_service.create_complianceauditschedule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_complianceauditschedule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/complianceauditschedules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._complianceauditschedule_service.get_complianceauditschedule(record_id)
            if not obj:
                return {"status": "error", "message": "ComplianceAuditSchedule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_complianceauditschedule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/complianceauditschedules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._complianceauditschedule_service.update_complianceauditschedule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_complianceauditschedule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/complianceauditschedules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._complianceauditschedule_service.delete_complianceauditschedule(record_id)
            if not success:
                return {"status": "error", "message": "ComplianceAuditSchedule not found", "code": 404}
            return {"status": "success", "message": "ComplianceAuditSchedule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_complianceauditschedules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/complianceauditschedules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._complianceauditschedule_service.list_all_complianceauditschedules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_complianceauditschedule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/complianceauditschedules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._complianceauditschedule_service.verify_complianceauditschedule_workflow_state(record_id)
            res = self._complianceauditschedule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_soxcontrolpoint_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/soxcontrolpoints"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._soxcontrolpoint_service.create_soxcontrolpoint(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_soxcontrolpoint_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/soxcontrolpoints/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            obj = self._soxcontrolpoint_service.get_soxcontrolpoint(record_id)
            if not obj:
                return {"status": "error", "message": "SOXControlPoint not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_soxcontrolpoint_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/audit_compliance/soxcontrolpoints/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "audit_compliance_manager"])
            obj = self._soxcontrolpoint_service.update_soxcontrolpoint(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_soxcontrolpoint_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/audit_compliance/soxcontrolpoints/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._soxcontrolpoint_service.delete_soxcontrolpoint(record_id)
            if not success:
                return {"status": "error", "message": "SOXControlPoint not found", "code": 404}
            return {"status": "success", "message": "SOXControlPoint deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_soxcontrolpoints_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/audit_compliance/soxcontrolpoints"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "audit_compliance_user"])
            items = self._soxcontrolpoint_service.list_all_soxcontrolpoints()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_soxcontrolpoint_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/audit_compliance/soxcontrolpoints/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "audit_compliance_user"])
            is_valid = self._soxcontrolpoint_service.verify_soxcontrolpoint_workflow_state(record_id)
            res = self._soxcontrolpoint_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

