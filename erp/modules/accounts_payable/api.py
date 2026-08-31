"""
AuraLedger ACCOUNTS_PAYABLE Module - REST Controller Endpoints
Generated automatically for the AuraLedger system.
Contains routing handlers simulating REST API endpoints.
"""
from typing import Dict, Any, List
from erp.core.auth import auth_service
from erp.core.errors import ERPException
from erp.core.logger import audit_log
from erp.modules.accounts_payable.services import VendorService
from erp.modules.accounts_payable.services import PurchaseInvoiceService
from erp.modules.accounts_payable.services import InvoiceLineService
from erp.modules.accounts_payable.services import VendorPaymentService
from erp.modules.accounts_payable.services import PaymentTermService
from erp.modules.accounts_payable.services import APAgingIntervalService
from erp.modules.accounts_payable.services import PurchaseDebitNoteService
from erp.modules.accounts_payable.services import VendorCreditBalanceService
from erp.modules.accounts_payable.services import VendorCategoryService
from erp.modules.accounts_payable.services import APReportPreferenceService
from erp.modules.accounts_payable.services import Vendor1099TaxService
from erp.modules.accounts_payable.services import APDisbursementRuleService

class Accounts_payableApiController:
    """REST API Controller for handling module routes and requests."""
    def __init__(self):
        self._vendor_service = VendorService()
        self._purchaseinvoice_service = PurchaseInvoiceService()
        self._invoiceline_service = InvoiceLineService()
        self._vendorpayment_service = VendorPaymentService()
        self._paymentterm_service = PaymentTermService()
        self._apaginginterval_service = APAgingIntervalService()
        self._purchasedebitnote_service = PurchaseDebitNoteService()
        self._vendorcreditbalance_service = VendorCreditBalanceService()
        self._vendorcategory_service = VendorCategoryService()
        self._apreportpreference_service = APReportPreferenceService()
        self._vendor1099tax_service = Vendor1099TaxService()
        self._apdisbursementrule_service = APDisbursementRuleService()

    def create_vendor_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendors"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "name" not in payload:
                return {"status": "error", "message": "Missing required parameter: name", "code": 400}
            if "email" not in payload:
                return {"status": "error", "message": "Missing required parameter: email", "code": 400}
            if "phone" not in payload:
                return {"status": "error", "message": "Missing required parameter: phone", "code": 400}
            if "terms" not in payload:
                return {"status": "error", "message": "Missing required parameter: terms", "code": 400}
            if "balance_owed" not in payload:
                return {"status": "error", "message": "Missing required parameter: balance_owed", "code": 400}
            obj = self._vendor_service.create_vendor(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_vendor_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendors/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._vendor_service.get_vendor(record_id)
            if not obj:
                return {"status": "error", "message": "Vendor not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_vendor_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/vendors/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._vendor_service.update_vendor(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_vendor_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/vendors/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._vendor_service.delete_vendor(record_id)
            if not success:
                return {"status": "error", "message": "Vendor not found", "code": 404}
            return {"status": "success", "message": "Vendor deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_vendors_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendors"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._vendor_service.list_all_vendors()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_vendor_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendors/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._vendor_service.verify_vendor_workflow_state(record_id)
            res = self._vendor_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_purchaseinvoice_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/purchaseinvoices"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "invoice_number" not in payload:
                return {"status": "error", "message": "Missing required parameter: invoice_number", "code": 400}
            if "vendor_id" not in payload:
                return {"status": "error", "message": "Missing required parameter: vendor_id", "code": 400}
            if "invoice_date" not in payload:
                return {"status": "error", "message": "Missing required parameter: invoice_date", "code": 400}
            if "amount_due" not in payload:
                return {"status": "error", "message": "Missing required parameter: amount_due", "code": 400}
            if "status" not in payload:
                return {"status": "error", "message": "Missing required parameter: status", "code": 400}
            obj = self._purchaseinvoice_service.create_purchaseinvoice(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_purchaseinvoice_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/purchaseinvoices/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._purchaseinvoice_service.get_purchaseinvoice(record_id)
            if not obj:
                return {"status": "error", "message": "PurchaseInvoice not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_purchaseinvoice_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/purchaseinvoices/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._purchaseinvoice_service.update_purchaseinvoice(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_purchaseinvoice_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/purchaseinvoices/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._purchaseinvoice_service.delete_purchaseinvoice(record_id)
            if not success:
                return {"status": "error", "message": "PurchaseInvoice not found", "code": 404}
            return {"status": "success", "message": "PurchaseInvoice deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_purchaseinvoices_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/purchaseinvoices"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._purchaseinvoice_service.list_all_purchaseinvoices()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_purchaseinvoice_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/purchaseinvoices/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._purchaseinvoice_service.verify_purchaseinvoice_workflow_state(record_id)
            res = self._purchaseinvoice_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_invoiceline_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/invoicelines"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._invoiceline_service.create_invoiceline(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_invoiceline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/invoicelines/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._invoiceline_service.get_invoiceline(record_id)
            if not obj:
                return {"status": "error", "message": "InvoiceLine not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_invoiceline_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/invoicelines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._invoiceline_service.update_invoiceline(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_invoiceline_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/invoicelines/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._invoiceline_service.delete_invoiceline(record_id)
            if not success:
                return {"status": "error", "message": "InvoiceLine not found", "code": 404}
            return {"status": "success", "message": "InvoiceLine deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_invoicelines_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/invoicelines"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._invoiceline_service.list_all_invoicelines()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_invoiceline_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/invoicelines/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._invoiceline_service.verify_invoiceline_workflow_state(record_id)
            res = self._invoiceline_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_vendorpayment_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendorpayments"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._vendorpayment_service.create_vendorpayment(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_vendorpayment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendorpayments/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._vendorpayment_service.get_vendorpayment(record_id)
            if not obj:
                return {"status": "error", "message": "VendorPayment not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_vendorpayment_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/vendorpayments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._vendorpayment_service.update_vendorpayment(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_vendorpayment_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/vendorpayments/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._vendorpayment_service.delete_vendorpayment(record_id)
            if not success:
                return {"status": "error", "message": "VendorPayment not found", "code": 404}
            return {"status": "success", "message": "VendorPayment deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_vendorpayments_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendorpayments"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._vendorpayment_service.list_all_vendorpayments()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_vendorpayment_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendorpayments/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._vendorpayment_service.verify_vendorpayment_workflow_state(record_id)
            res = self._vendorpayment_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_paymentterm_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/paymentterms"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._paymentterm_service.create_paymentterm(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_paymentterm_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/paymentterms/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._paymentterm_service.get_paymentterm(record_id)
            if not obj:
                return {"status": "error", "message": "PaymentTerm not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_paymentterm_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/paymentterms/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._paymentterm_service.update_paymentterm(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_paymentterm_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/paymentterms/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._paymentterm_service.delete_paymentterm(record_id)
            if not success:
                return {"status": "error", "message": "PaymentTerm not found", "code": 404}
            return {"status": "success", "message": "PaymentTerm deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_paymentterms_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/paymentterms"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._paymentterm_service.list_all_paymentterms()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_paymentterm_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/paymentterms/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._paymentterm_service.verify_paymentterm_workflow_state(record_id)
            res = self._paymentterm_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_apaginginterval_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/apagingintervals"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
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
            obj = self._apaginginterval_service.create_apaginginterval(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_apaginginterval_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/apagingintervals/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._apaginginterval_service.get_apaginginterval(record_id)
            if not obj:
                return {"status": "error", "message": "APAgingInterval not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_apaginginterval_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/apagingintervals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._apaginginterval_service.update_apaginginterval(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_apaginginterval_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/apagingintervals/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._apaginginterval_service.delete_apaginginterval(record_id)
            if not success:
                return {"status": "error", "message": "APAgingInterval not found", "code": 404}
            return {"status": "success", "message": "APAgingInterval deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_apagingintervals_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/apagingintervals"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._apaginginterval_service.list_all_apagingintervals()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_apaginginterval_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/apagingintervals/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._apaginginterval_service.verify_apaginginterval_workflow_state(record_id)
            res = self._apaginginterval_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_purchasedebitnote_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/purchasedebitnotes"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
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
            obj = self._purchasedebitnote_service.create_purchasedebitnote(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_purchasedebitnote_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/purchasedebitnotes/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._purchasedebitnote_service.get_purchasedebitnote(record_id)
            if not obj:
                return {"status": "error", "message": "PurchaseDebitNote not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_purchasedebitnote_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/purchasedebitnotes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._purchasedebitnote_service.update_purchasedebitnote(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_purchasedebitnote_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/purchasedebitnotes/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._purchasedebitnote_service.delete_purchasedebitnote(record_id)
            if not success:
                return {"status": "error", "message": "PurchaseDebitNote not found", "code": 404}
            return {"status": "success", "message": "PurchaseDebitNote deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_purchasedebitnotes_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/purchasedebitnotes"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._purchasedebitnote_service.list_all_purchasedebitnotes()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_purchasedebitnote_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/purchasedebitnotes/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._purchasedebitnote_service.verify_purchasedebitnote_workflow_state(record_id)
            res = self._purchasedebitnote_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_vendorcreditbalance_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendorcreditbalances"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
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
            obj = self._vendorcreditbalance_service.create_vendorcreditbalance(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_vendorcreditbalance_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendorcreditbalances/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._vendorcreditbalance_service.get_vendorcreditbalance(record_id)
            if not obj:
                return {"status": "error", "message": "VendorCreditBalance not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_vendorcreditbalance_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/vendorcreditbalances/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._vendorcreditbalance_service.update_vendorcreditbalance(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_vendorcreditbalance_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/vendorcreditbalances/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._vendorcreditbalance_service.delete_vendorcreditbalance(record_id)
            if not success:
                return {"status": "error", "message": "VendorCreditBalance not found", "code": 404}
            return {"status": "success", "message": "VendorCreditBalance deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_vendorcreditbalances_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendorcreditbalances"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._vendorcreditbalance_service.list_all_vendorcreditbalances()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_vendorcreditbalance_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendorcreditbalances/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._vendorcreditbalance_service.verify_vendorcreditbalance_workflow_state(record_id)
            res = self._vendorcreditbalance_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_vendorcategory_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendorcategorys"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._vendorcategory_service.create_vendorcategory(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_vendorcategory_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendorcategorys/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._vendorcategory_service.get_vendorcategory(record_id)
            if not obj:
                return {"status": "error", "message": "VendorCategory not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_vendorcategory_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/vendorcategorys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._vendorcategory_service.update_vendorcategory(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_vendorcategory_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/vendorcategorys/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._vendorcategory_service.delete_vendorcategory(record_id)
            if not success:
                return {"status": "error", "message": "VendorCategory not found", "code": 404}
            return {"status": "success", "message": "VendorCategory deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_vendorcategorys_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendorcategorys"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._vendorcategory_service.list_all_vendorcategorys()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_vendorcategory_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendorcategorys/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._vendorcategory_service.verify_vendorcategory_workflow_state(record_id)
            res = self._vendorcategory_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_apreportpreference_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/apreportpreferences"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._apreportpreference_service.create_apreportpreference(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_apreportpreference_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/apreportpreferences/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._apreportpreference_service.get_apreportpreference(record_id)
            if not obj:
                return {"status": "error", "message": "APReportPreference not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_apreportpreference_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/apreportpreferences/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._apreportpreference_service.update_apreportpreference(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_apreportpreference_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/apreportpreferences/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._apreportpreference_service.delete_apreportpreference(record_id)
            if not success:
                return {"status": "error", "message": "APReportPreference not found", "code": 404}
            return {"status": "success", "message": "APReportPreference deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_apreportpreferences_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/apreportpreferences"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._apreportpreference_service.list_all_apreportpreferences()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_apreportpreference_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/apreportpreferences/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._apreportpreference_service.verify_apreportpreference_workflow_state(record_id)
            res = self._apreportpreference_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_vendor1099tax_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendor1099taxs"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
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
            obj = self._vendor1099tax_service.create_vendor1099tax(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_vendor1099tax_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendor1099taxs/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._vendor1099tax_service.get_vendor1099tax(record_id)
            if not obj:
                return {"status": "error", "message": "Vendor1099Tax not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_vendor1099tax_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/vendor1099taxs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._vendor1099tax_service.update_vendor1099tax(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_vendor1099tax_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/vendor1099taxs/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._vendor1099tax_service.delete_vendor1099tax(record_id)
            if not success:
                return {"status": "error", "message": "Vendor1099Tax not found", "code": 404}
            return {"status": "success", "message": "Vendor1099Tax deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_vendor1099taxs_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/vendor1099taxs"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._vendor1099tax_service.list_all_vendor1099taxs()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_vendor1099tax_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/vendor1099taxs/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._vendor1099tax_service.verify_vendor1099tax_workflow_state(record_id)
            res = self._vendor1099tax_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def create_apdisbursementrule_endpoint(self, token: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/apdisbursementrules"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            if "code" not in payload:
                return {"status": "error", "message": "Missing required parameter: code", "code": 400}
            if "description" not in payload:
                return {"status": "error", "message": "Missing required parameter: description", "code": 400}
            if "status_state" not in payload:
                return {"status": "error", "message": "Missing required parameter: status_state", "code": 400}
            obj = self._apdisbursementrule_service.create_apdisbursementrule(payload)
            return {"status": "success", "data": obj.to_dict(), "code": 201}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def get_apdisbursementrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/apdisbursementrules/{id}"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            obj = self._apdisbursementrule_service.get_apdisbursementrule(record_id)
            if not obj:
                return {"status": "error", "message": "APDisbursementRule not found", "code": 404}
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def update_apdisbursementrule_endpoint(self, token: str, record_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """REST Endpoint: PUT /api/v1/accounts_payable/apdisbursementrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller", "accounts_payable_manager"])
            obj = self._apdisbursementrule_service.update_apdisbursementrule(record_id, payload)
            return {"status": "success", "data": obj.to_dict(), "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def delete_apdisbursementrule_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: DELETE /api/v1/accounts_payable/apdisbursementrules/{id}"""
        try:
            auth_service.authorize(token, ["admin", "controller"])
            success = self._apdisbursementrule_service.delete_apdisbursementrule(record_id)
            if not success:
                return {"status": "error", "message": "APDisbursementRule not found", "code": 404}
            return {"status": "success", "message": "APDisbursementRule deleted successfully", "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def list_apdisbursementrules_endpoint(self, token: str) -> Dict[str, Any]:
        """REST Endpoint: GET /api/v1/accounts_payable/apdisbursementrules"""
        try:
            auth_service.authorize(token, ["ledger", "auditor", "accounts_payable_user"])
            items = self._apdisbursementrule_service.list_all_apdisbursementrules()
            return {"status": "success", "data": [i.to_dict() for i in items], "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

    def run_apdisbursementrule_workflow_endpoint(self, token: str, record_id: str) -> Dict[str, Any]:
        """REST Endpoint: POST /api/v1/accounts_payable/apdisbursementrules/{id}/workflow"""
        try:
            auth_service.authorize(token, ["ledger", "accounts_payable_user"])
            is_valid = self._apdisbursementrule_service.verify_apdisbursementrule_workflow_state(record_id)
            res = self._apdisbursementrule_service.simulated_domain_workflow_1(record_id, "api_trigger")
            return {"status": "success", "data": res, "code": 200}
        except ERPException as e:
            return {"status": "error", "message": str(e), "code": 400}

