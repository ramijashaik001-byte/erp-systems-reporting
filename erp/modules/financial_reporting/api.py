"""
AuraLedger FINANCIAL_REPORTING Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.financial_reporting.services import ReportTemplateService
from erp.modules.financial_reporting.services import FinancialRatioService
from erp.modules.financial_reporting.services import DashboardWidgetService
from erp.modules.financial_reporting.services import SavedReportQueryService
from erp.modules.financial_reporting.services import ConsolidationEntityService
from erp.modules.financial_reporting.services import ReportingSegmentService
from erp.modules.financial_reporting.services import TrialBalanceViewService
from erp.modules.financial_reporting.services import ReportScheduleService
from erp.modules.financial_reporting.services import FinancialStatementNoteService
from erp.modules.financial_reporting.services import KPIThresholdService
from erp.modules.financial_reporting.services import ReportExportConfigService
from erp.modules.financial_reporting.services import ConsolidatedBalanceSheetService

class Financial_reportingApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._reporttemplate_service = ReportTemplateService()
        self._financialratio_service = FinancialRatioService()
        self._dashboardwidget_service = DashboardWidgetService()
        self._savedreportquery_service = SavedReportQueryService()
        self._consolidationentity_service = ConsolidationEntityService()
        self._reportingsegment_service = ReportingSegmentService()
        self._trialbalanceview_service = TrialBalanceViewService()
        self._reportschedule_service = ReportScheduleService()
        self._financialstatementnote_service = FinancialStatementNoteService()
        self._kpithreshold_service = KPIThresholdService()
        self._reportexportconfig_service = ReportExportConfigService()
        self._consolidatedbalancesheet_service = ConsolidatedBalanceSheetService()

    def create_reporttemplate_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reporttemplates"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._reporttemplate_service.create_reporttemplate(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_reporttemplate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reporttemplates/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._reporttemplate_service.get_reporttemplate(record_id)
            if not obj:
                return {"status": "error", "message": "ReportTemplate not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_reporttemplate_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/reporttemplates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._reporttemplate_service.update_reporttemplate(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_reporttemplate_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/reporttemplates/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._reporttemplate_service.delete_reporttemplate(record_id)
            if not success:
                return {"status": "error", "message": "ReportTemplate not found", "code": 404}
            return {"status": "success", "message": "ReportTemplate deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_reporttemplates_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reporttemplates"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._reporttemplate_service.list_all_reporttemplates()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_reporttemplate_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reporttemplates/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._reporttemplate_service.verify_reporttemplate_workflow_state(record_id)
            res = self._reporttemplate_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_financialratio_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/financialratios"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
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
            obj = self._financialratio_service.create_financialratio(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_financialratio_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/financialratios/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._financialratio_service.get_financialratio(record_id)
            if not obj:
                return {"status": "error", "message": "FinancialRatio not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_financialratio_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/financialratios/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._financialratio_service.update_financialratio(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_financialratio_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/financialratios/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._financialratio_service.delete_financialratio(record_id)
            if not success:
                return {"status": "error", "message": "FinancialRatio not found", "code": 404}
            return {"status": "success", "message": "FinancialRatio deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_financialratios_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/financialratios"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._financialratio_service.list_all_financialratios()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_financialratio_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/financialratios/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._financialratio_service.verify_financialratio_workflow_state(record_id)
            res = self._financialratio_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_dashboardwidget_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/dashboardwidgets"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._dashboardwidget_service.create_dashboardwidget(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_dashboardwidget_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/dashboardwidgets/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._dashboardwidget_service.get_dashboardwidget(record_id)
            if not obj:
                return {"status": "error", "message": "DashboardWidget not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_dashboardwidget_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/dashboardwidgets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._dashboardwidget_service.update_dashboardwidget(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_dashboardwidget_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/dashboardwidgets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._dashboardwidget_service.delete_dashboardwidget(record_id)
            if not success:
                return {"status": "error", "message": "DashboardWidget not found", "code": 404}
            return {"status": "success", "message": "DashboardWidget deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_dashboardwidgets_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/dashboardwidgets"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._dashboardwidget_service.list_all_dashboardwidgets()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_dashboardwidget_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/dashboardwidgets/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._dashboardwidget_service.verify_dashboardwidget_workflow_state(record_id)
            res = self._dashboardwidget_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_savedreportquery_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/savedreportquerys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._savedreportquery_service.create_savedreportquery(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_savedreportquery_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/savedreportquerys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._savedreportquery_service.get_savedreportquery(record_id)
            if not obj:
                return {"status": "error", "message": "SavedReportQuery not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_savedreportquery_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/savedreportquerys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._savedreportquery_service.update_savedreportquery(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_savedreportquery_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/savedreportquerys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._savedreportquery_service.delete_savedreportquery(record_id)
            if not success:
                return {"status": "error", "message": "SavedReportQuery not found", "code": 404}
            return {"status": "success", "message": "SavedReportQuery deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_savedreportquerys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/savedreportquerys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._savedreportquery_service.list_all_savedreportquerys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_savedreportquery_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/savedreportquerys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._savedreportquery_service.verify_savedreportquery_workflow_state(record_id)
            res = self._savedreportquery_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_consolidationentity_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/consolidationentitys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._consolidationentity_service.create_consolidationentity(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_consolidationentity_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/consolidationentitys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._consolidationentity_service.get_consolidationentity(record_id)
            if not obj:
                return {"status": "error", "message": "ConsolidationEntity not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_consolidationentity_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/consolidationentitys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._consolidationentity_service.update_consolidationentity(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_consolidationentity_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/consolidationentitys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._consolidationentity_service.delete_consolidationentity(record_id)
            if not success:
                return {"status": "error", "message": "ConsolidationEntity not found", "code": 404}
            return {"status": "success", "message": "ConsolidationEntity deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_consolidationentitys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/consolidationentitys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._consolidationentity_service.list_all_consolidationentitys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_consolidationentity_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/consolidationentitys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._consolidationentity_service.verify_consolidationentity_workflow_state(record_id)
            res = self._consolidationentity_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_reportingsegment_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reportingsegments"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._reportingsegment_service.create_reportingsegment(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_reportingsegment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reportingsegments/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._reportingsegment_service.get_reportingsegment(record_id)
            if not obj:
                return {"status": "error", "message": "ReportingSegment not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_reportingsegment_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/reportingsegments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._reportingsegment_service.update_reportingsegment(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_reportingsegment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/reportingsegments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._reportingsegment_service.delete_reportingsegment(record_id)
            if not success:
                return {"status": "error", "message": "ReportingSegment not found", "code": 404}
            return {"status": "success", "message": "ReportingSegment deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_reportingsegments_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reportingsegments"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._reportingsegment_service.list_all_reportingsegments()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_reportingsegment_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reportingsegments/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._reportingsegment_service.verify_reportingsegment_workflow_state(record_id)
            res = self._reportingsegment_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_trialbalanceview_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/trialbalanceviews"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
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
            obj = self._trialbalanceview_service.create_trialbalanceview(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_trialbalanceview_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/trialbalanceviews/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._trialbalanceview_service.get_trialbalanceview(record_id)
            if not obj:
                return {"status": "error", "message": "TrialBalanceView not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_trialbalanceview_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/trialbalanceviews/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._trialbalanceview_service.update_trialbalanceview(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_trialbalanceview_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/trialbalanceviews/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._trialbalanceview_service.delete_trialbalanceview(record_id)
            if not success:
                return {"status": "error", "message": "TrialBalanceView not found", "code": 404}
            return {"status": "success", "message": "TrialBalanceView deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_trialbalanceviews_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/trialbalanceviews"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._trialbalanceview_service.list_all_trialbalanceviews()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_trialbalanceview_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/trialbalanceviews/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._trialbalanceview_service.verify_trialbalanceview_workflow_state(record_id)
            res = self._trialbalanceview_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_reportschedule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reportschedules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
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
            obj = self._reportschedule_service.create_reportschedule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_reportschedule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reportschedules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._reportschedule_service.get_reportschedule(record_id)
            if not obj:
                return {"status": "error", "message": "ReportSchedule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_reportschedule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/reportschedules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._reportschedule_service.update_reportschedule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_reportschedule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/reportschedules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._reportschedule_service.delete_reportschedule(record_id)
            if not success:
                return {"status": "error", "message": "ReportSchedule not found", "code": 404}
            return {"status": "success", "message": "ReportSchedule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_reportschedules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reportschedules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._reportschedule_service.list_all_reportschedules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_reportschedule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reportschedules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._reportschedule_service.verify_reportschedule_workflow_state(record_id)
            res = self._reportschedule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_financialstatementnote_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/financialstatementnotes"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._financialstatementnote_service.create_financialstatementnote(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_financialstatementnote_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/financialstatementnotes/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._financialstatementnote_service.get_financialstatementnote(record_id)
            if not obj:
                return {"status": "error", "message": "FinancialStatementNote not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_financialstatementnote_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/financialstatementnotes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._financialstatementnote_service.update_financialstatementnote(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_financialstatementnote_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/financialstatementnotes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._financialstatementnote_service.delete_financialstatementnote(record_id)
            if not success:
                return {"status": "error", "message": "FinancialStatementNote not found", "code": 404}
            return {"status": "success", "message": "FinancialStatementNote deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_financialstatementnotes_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/financialstatementnotes"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._financialstatementnote_service.list_all_financialstatementnotes()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_financialstatementnote_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/financialstatementnotes/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._financialstatementnote_service.verify_financialstatementnote_workflow_state(record_id)
            res = self._financialstatementnote_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_kpithreshold_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/kpithresholds"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._kpithreshold_service.create_kpithreshold(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_kpithreshold_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/kpithresholds/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._kpithreshold_service.get_kpithreshold(record_id)
            if not obj:
                return {"status": "error", "message": "KPIThreshold not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_kpithreshold_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/kpithresholds/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._kpithreshold_service.update_kpithreshold(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_kpithreshold_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/kpithresholds/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._kpithreshold_service.delete_kpithreshold(record_id)
            if not success:
                return {"status": "error", "message": "KPIThreshold not found", "code": 404}
            return {"status": "success", "message": "KPIThreshold deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_kpithresholds_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/kpithresholds"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._kpithreshold_service.list_all_kpithresholds()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_kpithreshold_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/kpithresholds/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._kpithreshold_service.verify_kpithreshold_workflow_state(record_id)
            res = self._kpithreshold_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_reportexportconfig_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reportexportconfigs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._reportexportconfig_service.create_reportexportconfig(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_reportexportconfig_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reportexportconfigs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._reportexportconfig_service.get_reportexportconfig(record_id)
            if not obj:
                return {"status": "error", "message": "ReportExportConfig not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_reportexportconfig_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/reportexportconfigs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._reportexportconfig_service.update_reportexportconfig(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_reportexportconfig_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/reportexportconfigs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._reportexportconfig_service.delete_reportexportconfig(record_id)
            if not success:
                return {"status": "error", "message": "ReportExportConfig not found", "code": 404}
            return {"status": "success", "message": "ReportExportConfig deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_reportexportconfigs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/reportexportconfigs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._reportexportconfig_service.list_all_reportexportconfigs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_reportexportconfig_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/reportexportconfigs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._reportexportconfig_service.verify_reportexportconfig_workflow_state(record_id)
            res = self._reportexportconfig_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_consolidatedbalancesheet_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/consolidatedbalancesheets"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
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
            obj = self._consolidatedbalancesheet_service.create_consolidatedbalancesheet(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_consolidatedbalancesheet_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/consolidatedbalancesheets/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            obj = self._consolidatedbalancesheet_service.get_consolidatedbalancesheet(record_id)
            if not obj:
                return {"status": "error", "message": "ConsolidatedBalanceSheet not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_consolidatedbalancesheet_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/financial_reporting/consolidatedbalancesheets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "financial_reporting_manager"])
            obj = self._consolidatedbalancesheet_service.update_consolidatedbalancesheet(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_consolidatedbalancesheet_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/financial_reporting/consolidatedbalancesheets/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._consolidatedbalancesheet_service.delete_consolidatedbalancesheet(record_id)
            if not success:
                return {"status": "error", "message": "ConsolidatedBalanceSheet not found", "code": 404}
            return {"status": "success", "message": "ConsolidatedBalanceSheet deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_consolidatedbalancesheets_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/financial_reporting/consolidatedbalancesheets"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "financial_reporting_user"])
            items = self._consolidatedbalancesheet_service.list_all_consolidatedbalancesheets()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_consolidatedbalancesheet_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/financial_reporting/consolidatedbalancesheets/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "financial_reporting_user"])
            is_valid = self._consolidatedbalancesheet_service.verify_consolidatedbalancesheet_workflow_state(record_id)
            res = self._consolidatedbalancesheet_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

