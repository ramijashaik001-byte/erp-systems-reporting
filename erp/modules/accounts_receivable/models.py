"""
AuraLedger ACCOUNTS_RECEIVABLE Module - Database Models
Generated automatically for the AuraLedger system.
Contains ORM models for managing data structures.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, date
import json
from erp.core.db import BaseModel
from erp.core.errors import ValidationError
from erp.core.logger import audit_log

class Customer(BaseModel):
    """
    Model representing a Customer in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to Customer.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._company_name = kwargs.get("company_name", "Acme Financial Corp")
        self._email = kwargs.get("email", "billing@acmefin.com")
        self._phone = kwargs.get("phone", "+15551029")
        self._credit_limit = kwargs.get("credit_limit", 50000.00)
        self._outstanding_balance = kwargs.get("outstanding_balance", 12500.00)

    @property
    def company_name(self) -> str:
        """Get the value of company_name."""
        return self._company_name

    @company_name.setter
    def company_name(self, value: str):
        """Set the value of company_name with validation."""
        if value is None:
            raise ValidationError("company_name cannot be None.")
        self.validate_company_name(value)
        self._company_name = value
        self.update_timestamp()

    def validate_company_name(self, value: str):
        """Validate requirements for company_name."""
        if not isinstance(value, str):
            raise ValidationError("company_name must be a string.")
        if len(value) < 1:
            raise ValidationError("company_name cannot be empty.")

    @property
    def email(self) -> str:
        """Get the value of email."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Set the value of email with validation."""
        if value is None:
            raise ValidationError("email cannot be None.")
        self.validate_email(value)
        self._email = value
        self.update_timestamp()

    def validate_email(self, value: str):
        """Validate requirements for email."""
        if not isinstance(value, str):
            raise ValidationError("email must be a string.")
        if len(value) < 1:
            raise ValidationError("email cannot be empty.")

    @property
    def phone(self) -> str:
        """Get the value of phone."""
        return self._phone

    @phone.setter
    def phone(self, value: str):
        """Set the value of phone with validation."""
        if value is None:
            raise ValidationError("phone cannot be None.")
        self.validate_phone(value)
        self._phone = value
        self.update_timestamp()

    def validate_phone(self, value: str):
        """Validate requirements for phone."""
        if not isinstance(value, str):
            raise ValidationError("phone must be a string.")
        if len(value) < 1:
            raise ValidationError("phone cannot be empty.")

    @property
    def credit_limit(self) -> float:
        """Get the value of credit_limit."""
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, value: float):
        """Set the value of credit_limit with validation."""
        if value is None:
            raise ValidationError("credit_limit cannot be None.")
        self.validate_credit_limit(value)
        self._credit_limit = value
        self.update_timestamp()

    def validate_credit_limit(self, value: float):
        """Validate requirements for credit_limit."""
        if not isinstance(value, (int, float)):
            raise ValidationError("credit_limit must be numeric.")
        if value < 0:
            raise ValidationError("credit_limit cannot be negative.")

    @property
    def outstanding_balance(self) -> float:
        """Get the value of outstanding_balance."""
        return self._outstanding_balance

    @outstanding_balance.setter
    def outstanding_balance(self, value: float):
        """Set the value of outstanding_balance with validation."""
        if value is None:
            raise ValidationError("outstanding_balance cannot be None.")
        self.validate_outstanding_balance(value)
        self._outstanding_balance = value
        self.update_timestamp()

    def validate_outstanding_balance(self, value: float):
        """Validate requirements for outstanding_balance."""
        if not isinstance(value, (int, float)):
            raise ValidationError("outstanding_balance must be numeric.")
        if value < 0:
            raise ValidationError("outstanding_balance cannot be negative.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the Customer model to a dict."""
        data = super().to_dict()
        data["company_name"] = self._company_name
        data["email"] = self._email
        data["phone"] = self._phone
        data["credit_limit"] = self._credit_limit
        data["outstanding_balance"] = self._outstanding_balance
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Customer":
        """Deserialize a Customer object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert Customer to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_customer_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("customer_model", f"Checking integrity of Customer ID: {self.id}")
        return len(self.id) > 10

class SalesInvoice(BaseModel):
    """
    Model representing a SalesInvoice in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to SalesInvoice.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._invoice_number = kwargs.get("invoice_number", "INV-40912")
        self._customer_id = kwargs.get("customer_id", "cust-acme-123")
        self._issue_date = kwargs.get("issue_date", "2026-08-31")
        self._due_date = kwargs.get("due_date", "2026-09-30")
        self._subtotal = kwargs.get("subtotal", 12000.00)
        self._tax_amount = kwargs.get("tax_amount", 1200.00)
        self._total_amount = kwargs.get("total_amount", 13200.00)

    @property
    def invoice_number(self) -> str:
        """Get the value of invoice_number."""
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, value: str):
        """Set the value of invoice_number with validation."""
        if value is None:
            raise ValidationError("invoice_number cannot be None.")
        self.validate_invoice_number(value)
        self._invoice_number = value
        self.update_timestamp()

    def validate_invoice_number(self, value: str):
        """Validate requirements for invoice_number."""
        if not isinstance(value, str):
            raise ValidationError("invoice_number must be a string.")
        if len(value) < 1:
            raise ValidationError("invoice_number cannot be empty.")

    @property
    def customer_id(self) -> str:
        """Get the value of customer_id."""
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value: str):
        """Set the value of customer_id with validation."""
        if value is None:
            raise ValidationError("customer_id cannot be None.")
        self.validate_customer_id(value)
        self._customer_id = value
        self.update_timestamp()

    def validate_customer_id(self, value: str):
        """Validate requirements for customer_id."""
        if not isinstance(value, str):
            raise ValidationError("customer_id must be a string.")
        if len(value) < 1:
            raise ValidationError("customer_id cannot be empty.")

    @property
    def issue_date(self) -> str:
        """Get the value of issue_date."""
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value: str):
        """Set the value of issue_date with validation."""
        if value is None:
            raise ValidationError("issue_date cannot be None.")
        self.validate_issue_date(value)
        self._issue_date = value
        self.update_timestamp()

    def validate_issue_date(self, value: str):
        """Validate requirements for issue_date."""
        if not isinstance(value, str):
            raise ValidationError("issue_date must be a string.")
        if len(value) < 1:
            raise ValidationError("issue_date cannot be empty.")

    @property
    def due_date(self) -> str:
        """Get the value of due_date."""
        return self._due_date

    @due_date.setter
    def due_date(self, value: str):
        """Set the value of due_date with validation."""
        if value is None:
            raise ValidationError("due_date cannot be None.")
        self.validate_due_date(value)
        self._due_date = value
        self.update_timestamp()

    def validate_due_date(self, value: str):
        """Validate requirements for due_date."""
        if not isinstance(value, str):
            raise ValidationError("due_date must be a string.")
        if len(value) < 1:
            raise ValidationError("due_date cannot be empty.")

    @property
    def subtotal(self) -> float:
        """Get the value of subtotal."""
        return self._subtotal

    @subtotal.setter
    def subtotal(self, value: float):
        """Set the value of subtotal with validation."""
        if value is None:
            raise ValidationError("subtotal cannot be None.")
        self.validate_subtotal(value)
        self._subtotal = value
        self.update_timestamp()

    def validate_subtotal(self, value: float):
        """Validate requirements for subtotal."""
        if not isinstance(value, (int, float)):
            raise ValidationError("subtotal must be numeric.")

    @property
    def tax_amount(self) -> float:
        """Get the value of tax_amount."""
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value: float):
        """Set the value of tax_amount with validation."""
        if value is None:
            raise ValidationError("tax_amount cannot be None.")
        self.validate_tax_amount(value)
        self._tax_amount = value
        self.update_timestamp()

    def validate_tax_amount(self, value: float):
        """Validate requirements for tax_amount."""
        if not isinstance(value, (int, float)):
            raise ValidationError("tax_amount must be numeric.")
        if value < 0:
            raise ValidationError("tax_amount cannot be negative.")

    @property
    def total_amount(self) -> float:
        """Get the value of total_amount."""
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        """Set the value of total_amount with validation."""
        if value is None:
            raise ValidationError("total_amount cannot be None.")
        self.validate_total_amount(value)
        self._total_amount = value
        self.update_timestamp()

    def validate_total_amount(self, value: float):
        """Validate requirements for total_amount."""
        if not isinstance(value, (int, float)):
            raise ValidationError("total_amount must be numeric.")
        if value < 0:
            raise ValidationError("total_amount cannot be negative.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the SalesInvoice model to a dict."""
        data = super().to_dict()
        data["invoice_number"] = self._invoice_number
        data["customer_id"] = self._customer_id
        data["issue_date"] = self._issue_date
        data["due_date"] = self._due_date
        data["subtotal"] = self._subtotal
        data["tax_amount"] = self._tax_amount
        data["total_amount"] = self._total_amount
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SalesInvoice":
        """Deserialize a SalesInvoice object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert SalesInvoice to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def calculate_total(self) -> float:
        """Calculate invoice total amount."""
        return self._subtotal + self._tax_amount

class InvoiceItem(BaseModel):
    """
    Model representing a InvoiceItem in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to InvoiceItem.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "INVOICEITEM-001")
        self._description = kwargs.get("description", "Standard record of type InvoiceItem")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the InvoiceItem model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InvoiceItem":
        """Deserialize a InvoiceItem object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert InvoiceItem to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_invoiceitem_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("invoiceitem_model", f"Checking integrity of InvoiceItem ID: {self.id}")
        return len(self.id) > 10

class CustomerReceipt(BaseModel):
    """
    Model representing a CustomerReceipt in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to CustomerReceipt.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "CUSTOMERRECEIPT-001")
        self._description = kwargs.get("description", "Standard record of type CustomerReceipt")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the CustomerReceipt model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomerReceipt":
        """Deserialize a CustomerReceipt object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert CustomerReceipt to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_customerreceipt_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("customerreceipt_model", f"Checking integrity of CustomerReceipt ID: {self.id}")
        return len(self.id) > 10

class CreditLimitLog(BaseModel):
    """
    Model representing a CreditLimitLog in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to CreditLimitLog.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "CREDITLIMITLOG-001")
        self._description = kwargs.get("description", "Standard record of type CreditLimitLog")
        self._amount = kwargs.get("amount", 1000.00)
        self._base_currency = kwargs.get("base_currency", "USD")
        self._count_value = kwargs.get("count_value", 10)
        self._seq_num = kwargs.get("seq_num", 1)
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def amount(self) -> float:
        """Get the value of amount."""
        return self._amount

    @amount.setter
    def amount(self, value: float):
        """Set the value of amount with validation."""
        if value is None:
            raise ValidationError("amount cannot be None.")
        self.validate_amount(value)
        self._amount = value
        self.update_timestamp()

    def validate_amount(self, value: float):
        """Validate requirements for amount."""
        if not isinstance(value, (int, float)):
            raise ValidationError("amount must be numeric.")
        if value < 0:
            raise ValidationError("amount cannot be negative.")

    @property
    def base_currency(self) -> str:
        """Get the value of base_currency."""
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value: str):
        """Set the value of base_currency with validation."""
        if value is None:
            raise ValidationError("base_currency cannot be None.")
        self.validate_base_currency(value)
        self._base_currency = value
        self.update_timestamp()

    def validate_base_currency(self, value: str):
        """Validate requirements for base_currency."""
        if not isinstance(value, str):
            raise ValidationError("base_currency must be a string.")
        if len(value) < 1:
            raise ValidationError("base_currency cannot be empty.")

    @property
    def count_value(self) -> int:
        """Get the value of count_value."""
        return self._count_value

    @count_value.setter
    def count_value(self, value: int):
        """Set the value of count_value with validation."""
        if value is None:
            raise ValidationError("count_value cannot be None.")
        self.validate_count_value(value)
        self._count_value = value
        self.update_timestamp()

    def validate_count_value(self, value: int):
        """Validate requirements for count_value."""
        if not isinstance(value, (int, float)):
            raise ValidationError("count_value must be numeric.")
        if value < 0:
            raise ValidationError("count_value cannot be negative.")

    @property
    def seq_num(self) -> int:
        """Get the value of seq_num."""
        return self._seq_num

    @seq_num.setter
    def seq_num(self, value: int):
        """Set the value of seq_num with validation."""
        if value is None:
            raise ValidationError("seq_num cannot be None.")
        self.validate_seq_num(value)
        self._seq_num = value
        self.update_timestamp()

    def validate_seq_num(self, value: int):
        """Validate requirements for seq_num."""
        if not isinstance(value, (int, float)):
            raise ValidationError("seq_num must be numeric.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the CreditLimitLog model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["amount"] = self._amount
        data["base_currency"] = self._base_currency
        data["count_value"] = self._count_value
        data["seq_num"] = self._seq_num
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CreditLimitLog":
        """Deserialize a CreditLimitLog object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert CreditLimitLog to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_creditlimitlog_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("creditlimitlog_model", f"Checking integrity of CreditLimitLog ID: {self.id}")
        return len(self.id) > 10

class ARAgingInterval(BaseModel):
    """
    Model representing a ARAgingInterval in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to ARAgingInterval.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "ARAGINGINTERVAL-001")
        self._description = kwargs.get("description", "Standard record of type ARAgingInterval")
        self._count_value = kwargs.get("count_value", 10)
        self._seq_num = kwargs.get("seq_num", 1)
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def count_value(self) -> int:
        """Get the value of count_value."""
        return self._count_value

    @count_value.setter
    def count_value(self, value: int):
        """Set the value of count_value with validation."""
        if value is None:
            raise ValidationError("count_value cannot be None.")
        self.validate_count_value(value)
        self._count_value = value
        self.update_timestamp()

    def validate_count_value(self, value: int):
        """Validate requirements for count_value."""
        if not isinstance(value, (int, float)):
            raise ValidationError("count_value must be numeric.")
        if value < 0:
            raise ValidationError("count_value cannot be negative.")

    @property
    def seq_num(self) -> int:
        """Get the value of seq_num."""
        return self._seq_num

    @seq_num.setter
    def seq_num(self, value: int):
        """Set the value of seq_num with validation."""
        if value is None:
            raise ValidationError("seq_num cannot be None.")
        self.validate_seq_num(value)
        self._seq_num = value
        self.update_timestamp()

    def validate_seq_num(self, value: int):
        """Validate requirements for seq_num."""
        if not isinstance(value, (int, float)):
            raise ValidationError("seq_num must be numeric.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the ARAgingInterval model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["count_value"] = self._count_value
        data["seq_num"] = self._seq_num
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ARAgingInterval":
        """Deserialize a ARAgingInterval object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert ARAgingInterval to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_araginginterval_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("araginginterval_model", f"Checking integrity of ARAgingInterval ID: {self.id}")
        return len(self.id) > 10

class SalesCreditNote(BaseModel):
    """
    Model representing a SalesCreditNote in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to SalesCreditNote.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "SALESCREDITNOTE-001")
        self._description = kwargs.get("description", "Standard record of type SalesCreditNote")
        self._amount = kwargs.get("amount", 1000.00)
        self._base_currency = kwargs.get("base_currency", "USD")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def amount(self) -> float:
        """Get the value of amount."""
        return self._amount

    @amount.setter
    def amount(self, value: float):
        """Set the value of amount with validation."""
        if value is None:
            raise ValidationError("amount cannot be None.")
        self.validate_amount(value)
        self._amount = value
        self.update_timestamp()

    def validate_amount(self, value: float):
        """Validate requirements for amount."""
        if not isinstance(value, (int, float)):
            raise ValidationError("amount must be numeric.")
        if value < 0:
            raise ValidationError("amount cannot be negative.")

    @property
    def base_currency(self) -> str:
        """Get the value of base_currency."""
        return self._base_currency

    @base_currency.setter
    def base_currency(self, value: str):
        """Set the value of base_currency with validation."""
        if value is None:
            raise ValidationError("base_currency cannot be None.")
        self.validate_base_currency(value)
        self._base_currency = value
        self.update_timestamp()

    def validate_base_currency(self, value: str):
        """Validate requirements for base_currency."""
        if not isinstance(value, str):
            raise ValidationError("base_currency must be a string.")
        if len(value) < 1:
            raise ValidationError("base_currency cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the SalesCreditNote model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["amount"] = self._amount
        data["base_currency"] = self._base_currency
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SalesCreditNote":
        """Deserialize a SalesCreditNote object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert SalesCreditNote to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_salescreditnote_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("salescreditnote_model", f"Checking integrity of SalesCreditNote ID: {self.id}")
        return len(self.id) > 10

class DunningNotice(BaseModel):
    """
    Model representing a DunningNotice in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to DunningNotice.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "DUNNINGNOTICE-001")
        self._description = kwargs.get("description", "Standard record of type DunningNotice")
        self._scheduled_date = kwargs.get("scheduled_date", "2026-08-31")
        self._period_code = kwargs.get("period_code", "2026-08")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def scheduled_date(self) -> str:
        """Get the value of scheduled_date."""
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, value: str):
        """Set the value of scheduled_date with validation."""
        if value is None:
            raise ValidationError("scheduled_date cannot be None.")
        self.validate_scheduled_date(value)
        self._scheduled_date = value
        self.update_timestamp()

    def validate_scheduled_date(self, value: str):
        """Validate requirements for scheduled_date."""
        if not isinstance(value, str):
            raise ValidationError("scheduled_date must be a string.")
        if len(value) < 1:
            raise ValidationError("scheduled_date cannot be empty.")

    @property
    def period_code(self) -> str:
        """Get the value of period_code."""
        return self._period_code

    @period_code.setter
    def period_code(self, value: str):
        """Set the value of period_code with validation."""
        if value is None:
            raise ValidationError("period_code cannot be None.")
        self.validate_period_code(value)
        self._period_code = value
        self.update_timestamp()

    def validate_period_code(self, value: str):
        """Validate requirements for period_code."""
        if not isinstance(value, str):
            raise ValidationError("period_code must be a string.")
        if len(value) < 1:
            raise ValidationError("period_code cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the DunningNotice model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["scheduled_date"] = self._scheduled_date
        data["period_code"] = self._period_code
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DunningNotice":
        """Deserialize a DunningNotice object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert DunningNotice to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_dunningnotice_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("dunningnotice_model", f"Checking integrity of DunningNotice ID: {self.id}")
        return len(self.id) > 10

class CustomerCategory(BaseModel):
    """
    Model representing a CustomerCategory in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to CustomerCategory.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "CUSTOMERCATEGORY-001")
        self._description = kwargs.get("description", "Standard record of type CustomerCategory")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the CustomerCategory model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CustomerCategory":
        """Deserialize a CustomerCategory object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert CustomerCategory to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_customercategory_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("customercategory_model", f"Checking integrity of CustomerCategory ID: {self.id}")
        return len(self.id) > 10

class ARReportPreference(BaseModel):
    """
    Model representing a ARReportPreference in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to ARReportPreference.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "ARREPORTPREFERENCE-001")
        self._description = kwargs.get("description", "Standard record of type ARReportPreference")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the ARReportPreference model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ARReportPreference":
        """Deserialize a ARReportPreference object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert ARReportPreference to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_arreportpreference_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("arreportpreference_model", f"Checking integrity of ARReportPreference ID: {self.id}")
        return len(self.id) > 10

class ARCollectionRule(BaseModel):
    """
    Model representing a ARCollectionRule in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to ARCollectionRule.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "ARCOLLECTIONRULE-001")
        self._description = kwargs.get("description", "Standard record of type ARCollectionRule")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the ARCollectionRule model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ARCollectionRule":
        """Deserialize a ARCollectionRule object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert ARCollectionRule to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_arcollectionrule_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("arcollectionrule_model", f"Checking integrity of ARCollectionRule ID: {self.id}")
        return len(self.id) > 10

class LateFeePolicy(BaseModel):
    """
    Model representing a LateFeePolicy in the accounts_receivable module.
    This class encapsulates validations, serialization, business rules,
    and custom properties unique to LateFeePolicy.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._code = kwargs.get("code", "LATEFEEPOLICY-001")
        self._description = kwargs.get("description", "Standard record of type LateFeePolicy")
        self._status_state = kwargs.get("status_state", "ACTIVE")

    @property
    def code(self) -> str:
        """Get the value of code."""
        return self._code

    @code.setter
    def code(self, value: str):
        """Set the value of code with validation."""
        if value is None:
            raise ValidationError("code cannot be None.")
        self.validate_code(value)
        self._code = value
        self.update_timestamp()

    def validate_code(self, value: str):
        """Validate requirements for code."""
        if not isinstance(value, str):
            raise ValidationError("code must be a string.")
        if len(value) < 1:
            raise ValidationError("code cannot be empty.")

    @property
    def description(self) -> str:
        """Get the value of description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the value of description with validation."""
        if value is None:
            raise ValidationError("description cannot be None.")
        self.validate_description(value)
        self._description = value
        self.update_timestamp()

    def validate_description(self, value: str):
        """Validate requirements for description."""
        if not isinstance(value, str):
            raise ValidationError("description must be a string.")
        if len(value) < 1:
            raise ValidationError("description cannot be empty.")

    @property
    def status_state(self) -> str:
        """Get the value of status_state."""
        return self._status_state

    @status_state.setter
    def status_state(self, value: str):
        """Set the value of status_state with validation."""
        if value is None:
            raise ValidationError("status_state cannot be None.")
        self.validate_status_state(value)
        self._status_state = value
        self.update_timestamp()

    def validate_status_state(self, value: str):
        """Validate requirements for status_state."""
        if not isinstance(value, str):
            raise ValidationError("status_state must be a string.")
        if len(value) < 1:
            raise ValidationError("status_state cannot be empty.")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the LateFeePolicy model to a dict."""
        data = super().to_dict()
        data["code"] = self._code
        data["description"] = self._description
        data["status_state"] = self._status_state
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LateFeePolicy":
        """Deserialize a LateFeePolicy object from a dict."""
        return cls(**data)

    def to_json(self) -> str:
        """Convert LateFeePolicy to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def run_latefeepolicy_integrity_check(self) -> bool:
        """Standard model integrity evaluation checks."""
        audit_log("latefeepolicy_model", f"Checking integrity of LateFeePolicy ID: {self.id}")
        return len(self.id) > 10

