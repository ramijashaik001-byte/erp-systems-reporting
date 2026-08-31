"""
AuraLedger ACCOUNTS_RECEIVABLE Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.accounts_receivable.services import CustomerService
from erp.modules.accounts_receivable.services import SalesInvoiceService
from erp.modules.accounts_receivable.services import InvoiceItemService
from erp.modules.accounts_receivable.services import CustomerReceiptService
from erp.modules.accounts_receivable.services import CreditLimitLogService
from erp.modules.accounts_receivable.services import ARAgingIntervalService
from erp.modules.accounts_receivable.services import SalesCreditNoteService
from erp.modules.accounts_receivable.services import DunningNoticeService
from erp.modules.accounts_receivable.services import CustomerCategoryService
from erp.modules.accounts_receivable.services import ARReportPreferenceService
from erp.modules.accounts_receivable.services import ARCollectionRuleService
from erp.modules.accounts_receivable.services import LateFeePolicyService

class Accounts_receivableApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._customer_service = CustomerService()
        self._salesinvoice_service = SalesInvoiceService()
        self._invoiceitem_service = InvoiceItemService()
        self._customerreceipt_service = CustomerReceiptService()
        self._creditlimitlog_service = CreditLimitLogService()
        self._araginginterval_service = ARAgingIntervalService()
        self._salescreditnote_service = SalesCreditNoteService()
        self._dunningnotice_service = DunningNoticeService()
        self._customercategory_service = CustomerCategoryService()
        self._arreportpreference_service = ARReportPreferenceService()
        self._arcollectionrule_service = ARCollectionRuleService()
        self._latefeepolicy_service = LateFeePolicyService()

    def create_customer_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/customers"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "company_name" not in payload:
                return {"status": "error", "message": "Missing required parameter: company_name", "code": 400}
            if "email" not in payload:
                return {"status": "error", "message": "Missing required parameter: email", "code": 400}
            if "phone" not in payload:
                return {"status": "error", "message": "Missing required parameter: phone", "code": 400}
            if "credit_limit" not in payload:
                return {"status": "error", "message": "Missing required parameter: credit_limit", "code": 400}
            if "outstanding_balance" not in payload:
                return {"status": "error", "message": "Missing required parameter: outstanding_balance", "code": 400}
            obj = self._customer_service.create_customer(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_customer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/customers/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._customer_service.get_customer(record_id)
            if not obj:
                return {"status": "error", "message": "Customer not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_customer_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/customers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._customer_service.update_customer(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_customer_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/customers/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._customer_service.delete_customer(record_id)
            if not success:
                return {"status": "error", "message": "Customer not found", "code": 404}
            return {"status": "success", "message": "Customer deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_customers_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/customers"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._customer_service.list_all_customers()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_customer_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/customers/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._customer_service.verify_customer_workflow_state(record_id)
            res = self._customer_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_salesinvoice_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/salesinvoices"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "invoice_number" not in payload:
                return {"status": "error", "message": "Missing required parameter: invoice_number", "code": 400}
            if "customer_id" not in payload:
                return {"status": "error", "message": "Missing required parameter: customer_id", "code": 400}
            if "issue_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: issue_date", "code": 400}
            if "due_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: due_date", "code": 400}
            if "subtotal" not in payload:
                return {"status": "error", "message": "Missing required parameter: subtotal", "code": 400}
            if "tax_amount" not in payload:
                return {"status": "error", "message": "Missing required parameter: tax_amount", "code": 400}
            if "total_amount" not in payload:
                return {"status": "error", "message": "Missing required parameter: total_amount", "code": 400}
            obj = self._salesinvoice_service.create_salesinvoice(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_salesinvoice_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/salesinvoices/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._salesinvoice_service.get_salesinvoice(record_id)
            if not obj:
                return {"status": "error", "message": "SalesInvoice not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_salesinvoice_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/salesinvoices/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._salesinvoice_service.update_salesinvoice(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_salesinvoice_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/salesinvoices/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._salesinvoice_service.delete_salesinvoice(record_id)
            if not success:
                return {"status": "error", "message": "SalesInvoice not found", "code": 404}
            return {"status": "success", "message": "SalesInvoice deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_salesinvoices_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/salesinvoices"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._salesinvoice_service.list_all_salesinvoices()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_salesinvoice_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/salesinvoices/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._salesinvoice_service.verify_salesinvoice_workflow_state(record_id)
            res = self._salesinvoice_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_invoiceitem_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/invoiceitems"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._invoiceitem_service.create_invoiceitem(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_invoiceitem_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/invoiceitems/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._invoiceitem_service.get_invoiceitem(record_id)
            if not obj:
                return {"status": "error", "message": "InvoiceItem not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_invoiceitem_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/invoiceitems/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._invoiceitem_service.update_invoiceitem(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_invoiceitem_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/invoiceitems/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._invoiceitem_service.delete_invoiceitem(record_id)
            if not success:
                return {"status": "error", "message": "InvoiceItem not found", "code": 404}
            return {"status": "success", "message": "InvoiceItem deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_invoiceitems_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/invoiceitems"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._invoiceitem_service.list_all_invoiceitems()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_invoiceitem_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/invoiceitems/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._invoiceitem_service.verify_invoiceitem_workflow_state(record_id)
            res = self._invoiceitem_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_customerreceipt_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/customerreceipts"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._customerreceipt_service.create_customerreceipt(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_customerreceipt_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/customerreceipts/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._customerreceipt_service.get_customerreceipt(record_id)
            if not obj:
                return {"status": "error", "message": "CustomerReceipt not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_customerreceipt_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/customerreceipts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._customerreceipt_service.update_customerreceipt(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_customerreceipt_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/customerreceipts/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._customerreceipt_service.delete_customerreceipt(record_id)
            if not success:
                return {"status": "error", "message": "CustomerReceipt not found", "code": 404}
            return {"status": "success", "message": "CustomerReceipt deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_customerreceipts_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/customerreceipts"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._customerreceipt_service.list_all_customerreceipts()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_customerreceipt_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/customerreceipts/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._customerreceipt_service.verify_customerreceipt_workflow_state(record_id)
            res = self._customerreceipt_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_creditlimitlog_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/creditlimitlogs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "amount" not in payload:
                return {"status": "error", "message": "Missing required parameter: amount", "code": 400}
            if "base_currency" not in payload:
                return {"status": "error", "message": "Missing required parameter: base_currency", "code": 400}
            if "count_value" not in payload:
                return {"status": "error", "message": "Missing required parameter: count_value", "code": 400}
            if "seq_num" not in payload:
                return {"status": "error", "message": "Missing required parameter: seq_num", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._creditlimitlog_service.create_creditlimitlog(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_creditlimitlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/creditlimitlogs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._creditlimitlog_service.get_creditlimitlog(record_id)
            if not obj:
                return {"status": "error", "message": "CreditLimitLog not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_creditlimitlog_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/creditlimitlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._creditlimitlog_service.update_creditlimitlog(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_creditlimitlog_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/creditlimitlogs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._creditlimitlog_service.delete_creditlimitlog(record_id)
            if not success:
                return {"status": "error", "message": "CreditLimitLog not found", "code": 404}
            return {"status": "success", "message": "CreditLimitLog deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_creditlimitlogs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/creditlimitlogs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._creditlimitlog_service.list_all_creditlimitlogs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_creditlimitlog_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/creditlimitlogs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._creditlimitlog_service.verify_creditlimitlog_workflow_state(record_id)
            res = self._creditlimitlog_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_araginginterval_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/aragingintervals"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
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
            obj = self._araginginterval_service.create_araginginterval(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_araginginterval_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/aragingintervals/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._araginginterval_service.get_araginginterval(record_id)
            if not obj:
                return {"status": "error", "message": "ARAgingInterval not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_araginginterval_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/aragingintervals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._araginginterval_service.update_araginginterval(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_araginginterval_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/aragingintervals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._araginginterval_service.delete_araginginterval(record_id)
            if not success:
                return {"status": "error", "message": "ARAgingInterval not found", "code": 404}
            return {"status": "success", "message": "ARAgingInterval deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_aragingintervals_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/aragingintervals"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._araginginterval_service.list_all_aragingintervals()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_araginginterval_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/aragingintervals/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._araginginterval_service.verify_araginginterval_workflow_state(record_id)
            res = self._araginginterval_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_salescreditnote_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/salescreditnotes"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
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
            obj = self._salescreditnote_service.create_salescreditnote(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_salescreditnote_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/salescreditnotes/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._salescreditnote_service.get_salescreditnote(record_id)
            if not obj:
                return {"status": "error", "message": "SalesCreditNote not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_salescreditnote_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/salescreditnotes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._salescreditnote_service.update_salescreditnote(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_salescreditnote_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/salescreditnotes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._salescreditnote_service.delete_salescreditnote(record_id)
            if not success:
                return {"status": "error", "message": "SalesCreditNote not found", "code": 404}
            return {"status": "success", "message": "SalesCreditNote deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_salescreditnotes_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/salescreditnotes"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._salescreditnote_service.list_all_salescreditnotes()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_salescreditnote_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/salescreditnotes/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._salescreditnote_service.verify_salescreditnote_workflow_state(record_id)
            res = self._salescreditnote_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_dunningnotice_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/dunningnotices"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
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
            obj = self._dunningnotice_service.create_dunningnotice(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_dunningnotice_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/dunningnotices/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._dunningnotice_service.get_dunningnotice(record_id)
            if not obj:
                return {"status": "error", "message": "DunningNotice not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_dunningnotice_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/dunningnotices/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._dunningnotice_service.update_dunningnotice(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_dunningnotice_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/dunningnotices/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._dunningnotice_service.delete_dunningnotice(record_id)
            if not success:
                return {"status": "error", "message": "DunningNotice not found", "code": 404}
            return {"status": "success", "message": "DunningNotice deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_dunningnotices_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/dunningnotices"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._dunningnotice_service.list_all_dunningnotices()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_dunningnotice_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/dunningnotices/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._dunningnotice_service.verify_dunningnotice_workflow_state(record_id)
            res = self._dunningnotice_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_customercategory_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/customercategorys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._customercategory_service.create_customercategory(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_customercategory_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/customercategorys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._customercategory_service.get_customercategory(record_id)
            if not obj:
                return {"status": "error", "message": "CustomerCategory not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_customercategory_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/customercategorys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._customercategory_service.update_customercategory(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_customercategory_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/customercategorys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._customercategory_service.delete_customercategory(record_id)
            if not success:
                return {"status": "error", "message": "CustomerCategory not found", "code": 404}
            return {"status": "success", "message": "CustomerCategory deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_customercategorys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/customercategorys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._customercategory_service.list_all_customercategorys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_customercategory_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/customercategorys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._customercategory_service.verify_customercategory_workflow_state(record_id)
            res = self._customercategory_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_arreportpreference_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/arreportpreferences"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._arreportpreference_service.create_arreportpreference(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_arreportpreference_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/arreportpreferences/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._arreportpreference_service.get_arreportpreference(record_id)
            if not obj:
                return {"status": "error", "message": "ARReportPreference not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_arreportpreference_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/arreportpreferences/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._arreportpreference_service.update_arreportpreference(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_arreportpreference_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/arreportpreferences/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._arreportpreference_service.delete_arreportpreference(record_id)
            if not success:
                return {"status": "error", "message": "ARReportPreference not found", "code": 404}
            return {"status": "success", "message": "ARReportPreference deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_arreportpreferences_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/arreportpreferences"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._arreportpreference_service.list_all_arreportpreferences()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_arreportpreference_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/arreportpreferences/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._arreportpreference_service.verify_arreportpreference_workflow_state(record_id)
            res = self._arreportpreference_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_arcollectionrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/arcollectionrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._arcollectionrule_service.create_arcollectionrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_arcollectionrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/arcollectionrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._arcollectionrule_service.get_arcollectionrule(record_id)
            if not obj:
                return {"status": "error", "message": "ARCollectionRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_arcollectionrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/arcollectionrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._arcollectionrule_service.update_arcollectionrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_arcollectionrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/arcollectionrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._arcollectionrule_service.delete_arcollectionrule(record_id)
            if not success:
                return {"status": "error", "message": "ARCollectionRule not found", "code": 404}
            return {"status": "success", "message": "ARCollectionRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_arcollectionrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/arcollectionrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._arcollectionrule_service.list_all_arcollectionrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_arcollectionrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/arcollectionrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._arcollectionrule_service.verify_arcollectionrule_workflow_state(record_id)
            res = self._arcollectionrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_latefeepolicy_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/latefeepolicys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._latefeepolicy_service.create_latefeepolicy(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_latefeepolicy_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/latefeepolicys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            obj = self._latefeepolicy_service.get_latefeepolicy(record_id)
            if not obj:
                return {"status": "error", "message": "LateFeePolicy not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_latefeepolicy_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_receivable/latefeepolicys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_receivable_manager"])
            obj = self._latefeepolicy_service.update_latefeepolicy(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_latefeepolicy_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_receivable/latefeepolicys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._latefeepolicy_service.delete_latefeepolicy(record_id)
            if not success:
                return {"status": "error", "message": "LateFeePolicy not found", "code": 404}
            return {"status": "success", "message": "LateFeePolicy deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_latefeepolicys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_receivable/latefeepolicys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_receivable_user"])
            items = self._latefeepolicy_service.list_all_latefeepolicys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_latefeepolicy_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_receivable/latefeepolicys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_receivable_user"])
            is_valid = self._latefeepolicy_service.verify_latefeepolicy_workflow_state(record_id)
            res = self._latefeepolicy_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

