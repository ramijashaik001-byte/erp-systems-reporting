"""
AuraLedger PURCHASE_SALES_INTEGRATION Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.purchase_sales_integration.services import PurchaseOrderMatchService
from erp.modules.purchase_sales_integration.services import SalesOrderBillingService
from erp.modules.purchase_sales_integration.services import InventoryValueLogService
from erp.modules.purchase_sales_integration.services import FIFOQueueEntryService
from erp.modules.purchase_sales_integration.services import LIFOQueueEntryService
from erp.modules.purchase_sales_integration.services import StockValuationRunService
from erp.modules.purchase_sales_integration.services import CostOfGoodsSoldAdjustmentService
from erp.modules.purchase_sales_integration.services import IntegrationLogService
from erp.modules.purchase_sales_integration.services import IntegrationMappingService
from erp.modules.purchase_sales_integration.services import IntegrationErrorLogService
from erp.modules.purchase_sales_integration.services import GLAccountMappingRuleService
from erp.modules.purchase_sales_integration.services import SubledgerReconciliationLogService

class Purchase_sales_integrationApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._purchaseordermatch_service = PurchaseOrderMatchService()
        self._salesorderbilling_service = SalesOrderBillingService()
        self._inventoryvaluelog_service = InventoryValueLogService()
        self._fifoqueueentry_service = FIFOQueueEntryService()
        self._lifoqueueentry_service = LIFOQueueEntryService()
        self._stockvaluationrun_service = StockValuationRunService()
        self._costofgoodssoldadjustment_service = CostOfGoodsSoldAdjustmentService()
        self._integrationlog_service = IntegrationLogService()
        self._integrationmapping_service = IntegrationMappingService()
        self._integrationerrorlog_service = IntegrationErrorLogService()
        self._glaccountmappingrule_service = GLAccountMappingRuleService()
        self._subledgerreconciliationlog_service = SubledgerReconciliationLogService()

    def create_purchaseordermatch_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/purchaseordermatchs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._purchaseordermatch_service.create_purchaseordermatch(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_purchaseordermatch_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/purchaseordermatchs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._purchaseordermatch_service.get_purchaseordermatch(record_id)
            if not obj:
                return {"status": "error", "message": "PurchaseOrderMatch not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_purchaseordermatch_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/purchaseordermatchs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._purchaseordermatch_service.update_purchaseordermatch(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_purchaseordermatch_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/purchaseordermatchs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._purchaseordermatch_service.delete_purchaseordermatch(record_id)
            if not success:
                return {"status": "error", "message": "PurchaseOrderMatch not found", "code": 404}
            return {"status": "success", "message": "PurchaseOrderMatch deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_purchaseordermatchs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/purchaseordermatchs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._purchaseordermatch_service.list_all_purchaseordermatchs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_purchaseordermatch_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/purchaseordermatchs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._purchaseordermatch_service.verify_purchaseordermatch_workflow_state(record_id)
            res = self._purchaseordermatch_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_salesorderbilling_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/salesorderbillings"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._salesorderbilling_service.create_salesorderbilling(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_salesorderbilling_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/salesorderbillings/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._salesorderbilling_service.get_salesorderbilling(record_id)
            if not obj:
                return {"status": "error", "message": "SalesOrderBilling not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_salesorderbilling_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/salesorderbillings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._salesorderbilling_service.update_salesorderbilling(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_salesorderbilling_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/salesorderbillings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._salesorderbilling_service.delete_salesorderbilling(record_id)
            if not success:
                return {"status": "error", "message": "SalesOrderBilling not found", "code": 404}
            return {"status": "success", "message": "SalesOrderBilling deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_salesorderbillings_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/salesorderbillings"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._salesorderbilling_service.list_all_salesorderbillings()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_salesorderbilling_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/salesorderbillings/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._salesorderbilling_service.verify_salesorderbilling_workflow_state(record_id)
            res = self._salesorderbilling_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_inventoryvaluelog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/inventoryvaluelogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._inventoryvaluelog_service.create_inventoryvaluelog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_inventoryvaluelog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/inventoryvaluelogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._inventoryvaluelog_service.get_inventoryvaluelog(record_id)
            if not obj:
                return {"status": "error", "message": "InventoryValueLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_inventoryvaluelog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/inventoryvaluelogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._inventoryvaluelog_service.update_inventoryvaluelog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_inventoryvaluelog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/inventoryvaluelogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._inventoryvaluelog_service.delete_inventoryvaluelog(record_id)
            if not success:
                return {"status": "error", "message": "InventoryValueLog not found", "code": 404}
            return {"status": "success", "message": "InventoryValueLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_inventoryvaluelogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/inventoryvaluelogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._inventoryvaluelog_service.list_all_inventoryvaluelogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_inventoryvaluelog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/inventoryvaluelogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._inventoryvaluelog_service.verify_inventoryvaluelog_workflow_state(record_id)
            res = self._inventoryvaluelog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_fifoqueueentry_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/fifoqueueentrys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._fifoqueueentry_service.create_fifoqueueentry(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_fifoqueueentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/fifoqueueentrys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._fifoqueueentry_service.get_fifoqueueentry(record_id)
            if not obj:
                return {"status": "error", "message": "FIFOQueueEntry not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_fifoqueueentry_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/fifoqueueentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._fifoqueueentry_service.update_fifoqueueentry(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_fifoqueueentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/fifoqueueentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._fifoqueueentry_service.delete_fifoqueueentry(record_id)
            if not success:
                return {"status": "error", "message": "FIFOQueueEntry not found", "code": 404}
            return {"status": "success", "message": "FIFOQueueEntry deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_fifoqueueentrys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/fifoqueueentrys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._fifoqueueentry_service.list_all_fifoqueueentrys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_fifoqueueentry_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/fifoqueueentrys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._fifoqueueentry_service.verify_fifoqueueentry_workflow_state(record_id)
            res = self._fifoqueueentry_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_lifoqueueentry_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/lifoqueueentrys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._lifoqueueentry_service.create_lifoqueueentry(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_lifoqueueentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/lifoqueueentrys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._lifoqueueentry_service.get_lifoqueueentry(record_id)
            if not obj:
                return {"status": "error", "message": "LIFOQueueEntry not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_lifoqueueentry_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/lifoqueueentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._lifoqueueentry_service.update_lifoqueueentry(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_lifoqueueentry_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/lifoqueueentrys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._lifoqueueentry_service.delete_lifoqueueentry(record_id)
            if not success:
                return {"status": "error", "message": "LIFOQueueEntry not found", "code": 404}
            return {"status": "success", "message": "LIFOQueueEntry deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_lifoqueueentrys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/lifoqueueentrys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._lifoqueueentry_service.list_all_lifoqueueentrys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_lifoqueueentry_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/lifoqueueentrys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._lifoqueueentry_service.verify_lifoqueueentry_workflow_state(record_id)
            res = self._lifoqueueentry_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_stockvaluationrun_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/stockvaluationruns"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._stockvaluationrun_service.create_stockvaluationrun(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_stockvaluationrun_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/stockvaluationruns/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._stockvaluationrun_service.get_stockvaluationrun(record_id)
            if not obj:
                return {"status": "error", "message": "StockValuationRun not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_stockvaluationrun_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/stockvaluationruns/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._stockvaluationrun_service.update_stockvaluationrun(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_stockvaluationrun_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/stockvaluationruns/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._stockvaluationrun_service.delete_stockvaluationrun(record_id)
            if not success:
                return {"status": "error", "message": "StockValuationRun not found", "code": 404}
            return {"status": "success", "message": "StockValuationRun deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_stockvaluationruns_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/stockvaluationruns"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._stockvaluationrun_service.list_all_stockvaluationruns()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_stockvaluationrun_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/stockvaluationruns/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._stockvaluationrun_service.verify_stockvaluationrun_workflow_state(record_id)
            res = self._stockvaluationrun_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_costofgoodssoldadjustment_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/costofgoodssoldadjustments"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._costofgoodssoldadjustment_service.create_costofgoodssoldadjustment(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_costofgoodssoldadjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/costofgoodssoldadjustments/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._costofgoodssoldadjustment_service.get_costofgoodssoldadjustment(record_id)
            if not obj:
                return {"status": "error", "message": "CostOfGoodsSoldAdjustment not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_costofgoodssoldadjustment_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/costofgoodssoldadjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._costofgoodssoldadjustment_service.update_costofgoodssoldadjustment(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_costofgoodssoldadjustment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/costofgoodssoldadjustments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._costofgoodssoldadjustment_service.delete_costofgoodssoldadjustment(record_id)
            if not success:
                return {"status": "error", "message": "CostOfGoodsSoldAdjustment not found", "code": 404}
            return {"status": "success", "message": "CostOfGoodsSoldAdjustment deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_costofgoodssoldadjustments_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/costofgoodssoldadjustments"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._costofgoodssoldadjustment_service.list_all_costofgoodssoldadjustments()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_costofgoodssoldadjustment_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/costofgoodssoldadjustments/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._costofgoodssoldadjustment_service.verify_costofgoodssoldadjustment_workflow_state(record_id)
            res = self._costofgoodssoldadjustment_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_integrationlog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/integrationlogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._integrationlog_service.create_integrationlog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_integrationlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/integrationlogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._integrationlog_service.get_integrationlog(record_id)
            if not obj:
                return {"status": "error", "message": "IntegrationLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_integrationlog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/integrationlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._integrationlog_service.update_integrationlog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_integrationlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/integrationlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._integrationlog_service.delete_integrationlog(record_id)
            if not success:
                return {"status": "error", "message": "IntegrationLog not found", "code": 404}
            return {"status": "success", "message": "IntegrationLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_integrationlogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/integrationlogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._integrationlog_service.list_all_integrationlogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_integrationlog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/integrationlogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._integrationlog_service.verify_integrationlog_workflow_state(record_id)
            res = self._integrationlog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_integrationmapping_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/integrationmappings"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._integrationmapping_service.create_integrationmapping(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_integrationmapping_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/integrationmappings/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._integrationmapping_service.get_integrationmapping(record_id)
            if not obj:
                return {"status": "error", "message": "IntegrationMapping not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_integrationmapping_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/integrationmappings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._integrationmapping_service.update_integrationmapping(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_integrationmapping_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/integrationmappings/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._integrationmapping_service.delete_integrationmapping(record_id)
            if not success:
                return {"status": "error", "message": "IntegrationMapping not found", "code": 404}
            return {"status": "success", "message": "IntegrationMapping deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_integrationmappings_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/integrationmappings"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._integrationmapping_service.list_all_integrationmappings()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_integrationmapping_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/integrationmappings/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._integrationmapping_service.verify_integrationmapping_workflow_state(record_id)
            res = self._integrationmapping_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_integrationerrorlog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/integrationerrorlogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._integrationerrorlog_service.create_integrationerrorlog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_integrationerrorlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/integrationerrorlogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._integrationerrorlog_service.get_integrationerrorlog(record_id)
            if not obj:
                return {"status": "error", "message": "IntegrationErrorLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_integrationerrorlog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/integrationerrorlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._integrationerrorlog_service.update_integrationerrorlog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_integrationerrorlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/integrationerrorlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._integrationerrorlog_service.delete_integrationerrorlog(record_id)
            if not success:
                return {"status": "error", "message": "IntegrationErrorLog not found", "code": 404}
            return {"status": "success", "message": "IntegrationErrorLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_integrationerrorlogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/integrationerrorlogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._integrationerrorlog_service.list_all_integrationerrorlogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_integrationerrorlog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/integrationerrorlogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._integrationerrorlog_service.verify_integrationerrorlog_workflow_state(record_id)
            res = self._integrationerrorlog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_glaccountmappingrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/glaccountmappingrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
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
            obj = self._glaccountmappingrule_service.create_glaccountmappingrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_glaccountmappingrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/glaccountmappingrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._glaccountmappingrule_service.get_glaccountmappingrule(record_id)
            if not obj:
                return {"status": "error", "message": "GLAccountMappingRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_glaccountmappingrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/glaccountmappingrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._glaccountmappingrule_service.update_glaccountmappingrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_glaccountmappingrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/glaccountmappingrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._glaccountmappingrule_service.delete_glaccountmappingrule(record_id)
            if not success:
                return {"status": "error", "message": "GLAccountMappingRule not found", "code": 404}
            return {"status": "success", "message": "GLAccountMappingRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_glaccountmappingrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/glaccountmappingrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._glaccountmappingrule_service.list_all_glaccountmappingrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_glaccountmappingrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/glaccountmappingrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._glaccountmappingrule_service.verify_glaccountmappingrule_workflow_state(record_id)
            res = self._glaccountmappingrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_subledgerreconciliationlog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/subledgerreconciliationlogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._subledgerreconciliationlog_service.create_subledgerreconciliationlog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_subledgerreconciliationlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/subledgerreconciliationlogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            obj = self._subledgerreconciliationlog_service.get_subledgerreconciliationlog(record_id)
            if not obj:
                return {"status": "error", "message": "SubledgerReconciliationLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_subledgerreconciliationlog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/purchase_sales_integration/subledgerreconciliationlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "purchase_sales_integration_manager"])
            obj = self._subledgerreconciliationlog_service.update_subledgerreconciliationlog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_subledgerreconciliationlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/purchase_sales_integration/subledgerreconciliationlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._subledgerreconciliationlog_service.delete_subledgerreconciliationlog(record_id)
            if not success:
                return {"status": "error", "message": "SubledgerReconciliationLog not found", "code": 404}
            return {"status": "success", "message": "SubledgerReconciliationLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_subledgerreconciliationlogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/purchase_sales_integration/subledgerreconciliationlogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "purchase_sales_integration_user"])
            items = self._subledgerreconciliationlog_service.list_all_subledgerreconciliationlogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_subledgerreconciliationlog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/purchase_sales_integration/subledgerreconciliationlogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "purchase_sales_integration_user"])
            is_valid = self._subledgerreconciliationlog_service.verify_subledgerreconciliationlog_workflow_state(record_id)
            res = self._subledgerreconciliationlog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

