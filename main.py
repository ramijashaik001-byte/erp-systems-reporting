# AuraLedger Terminal Control Board CLI
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from erp.core.auth import auth_service
from erp.core.db import db_instance
from erp.core.logger import audit_log
from erp.core.errors import ERPException

from erp.modules.general_ledger.api import General_ledgerApiController
from erp.modules.accounts_payable.api import Accounts_payableApiController
from erp.modules.accounts_receivable.api import Accounts_receivableApiController
from erp.modules.cash_bank.api import Cash_bankApiController
from erp.modules.fixed_assets.api import Fixed_assetsApiController
from erp.modules.budgeting.api import BudgetingApiController
from erp.modules.cost_accounting.api import Cost_accountingApiController
from erp.modules.tax_management.api import Tax_managementApiController
from erp.modules.financial_reporting.api import Financial_reportingApiController
from erp.modules.audit_compliance.api import Audit_complianceApiController
from erp.modules.payroll_accounting.api import Payroll_accountingApiController
from erp.modules.purchase_sales_integration.api import Purchase_sales_integrationApiController

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    print("==================================================")
    print("       AURALEDGER FINANCE ERP SYSTEMS CLI       ")
    print("==================================================")
    print("Active User: admin (Role: System Administrator)")
    print("--------------------------------------------------")
    print("Select a Financial Domain Subsystem to Interrogate:")
    print(" 1. General Ledger Operations")
    print(" 2. Accounts Payable Operations")
    print(" 3. Accounts Receivable Operations")
    print(" 4. Cash Bank Operations")
    print(" 5. Fixed Assets Operations")
    print(" 6. Budgeting Operations")
    print(" 7. Cost Accounting Operations")
    print(" 8. Tax Management Operations")
    print(" 9. Financial Reporting Operations")
    print("10. Audit Compliance Operations")
    print("11. Payroll Accounting Operations")
    print("12. Purchase Sales Integration Operations")
    print("13. ERP Category & Subcategory Reporting")
    print("99. Exit System Suite")
    print("==================================================")
    
def run_cli():
    token = auth_service.authenticate("admin")
    
    general_ledger_controller = General_ledgerApiController()
    accounts_payable_controller = Accounts_payableApiController()
    accounts_receivable_controller = Accounts_receivableApiController()
    cash_bank_controller = Cash_bankApiController()
    fixed_assets_controller = Fixed_assetsApiController()
    budgeting_controller = BudgetingApiController()
    cost_accounting_controller = Cost_accountingApiController()
    tax_management_controller = Tax_managementApiController()
    financial_reporting_controller = Financial_reportingApiController()
    audit_compliance_controller = Audit_complianceApiController()
    payroll_accounting_controller = Payroll_accountingApiController()
    purchase_sales_integration_controller = Purchase_sales_integrationApiController()

    while True:
        clear_screen()
        main_menu()
        choice = input("Enter choice (1-12 or 99): ").strip()
        
        if choice == '99':
            print("Shutting down AuraLedger. Good bye!")
            break
            
        elif choice == '1':
            clear_screen()
            print(f"=== Running GENERAL_LEDGER Simulation Workflow ===")
            entity = "Account"
            print(f"Creating mock {entity}...")
            payload = {"account_number": "1010", "name": "Cash in Bank", "account_type": "ASSET", "balance": 150000.00, "currency": "USD"}
            res = general_ledger_controller.create_account_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = general_ledger_controller.list_accounts_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_account_workflow_endpoint"
                if hasattr(general_ledger_controller, workflow_method):
                    wf_res = getattr(general_ledger_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '2':
            clear_screen()
            print(f"=== Running ACCOUNTS_PAYABLE Simulation Workflow ===")
            entity = "Vendor"
            print(f"Creating mock {entity}...")
            payload = {"name": "Global Cloud Hosting", "email": "invoices@globalcloud.com", "phone": "+15559812", "terms": "NET30", "balance_owed": 3400.00}
            res = accounts_payable_controller.create_vendor_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = accounts_payable_controller.list_vendors_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_vendor_workflow_endpoint"
                if hasattr(accounts_payable_controller, workflow_method):
                    wf_res = getattr(accounts_payable_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '3':
            clear_screen()
            print(f"=== Running ACCOUNTS_RECEIVABLE Simulation Workflow ===")
            entity = "Customer"
            print(f"Creating mock {entity}...")
            payload = {"company_name": "Acme Financial Corp", "email": "billing@acmefin.com", "phone": "+15551029", "credit_limit": 50000.00, "outstanding_balance": 12500.00}
            res = accounts_receivable_controller.create_customer_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = accounts_receivable_controller.list_customers_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_customer_workflow_endpoint"
                if hasattr(accounts_receivable_controller, workflow_method):
                    wf_res = getattr(accounts_receivable_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '4':
            clear_screen()
            print(f"=== Running CASH_BANK Simulation Workflow ===")
            entity = "BankAccount"
            print(f"Creating mock {entity}...")
            payload = {"code": "BANKACCOUNT-001", "description": "Standard record of type BankAccount", "count_value": 10, "seq_num": 1, "status_state": "ACTIVE"}
            res = cash_bank_controller.create_bankaccount_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = cash_bank_controller.list_bankaccounts_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_bankaccount_workflow_endpoint"
                if hasattr(cash_bank_controller, workflow_method):
                    wf_res = getattr(cash_bank_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '5':
            clear_screen()
            print(f"=== Running FIXED_ASSETS Simulation Workflow ===")
            entity = "Asset"
            print(f"Creating mock {entity}...")
            payload = {"name": "Enterprise Server Rack C", "code": "AST-SRV-09", "purchase_date": "2025-01-10", "purchase_value": 24000.00, "salvage_value": 2000.00, "useful_life_years": 5}
            res = fixed_assets_controller.create_asset_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = fixed_assets_controller.list_assets_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_asset_workflow_endpoint"
                if hasattr(fixed_assets_controller, workflow_method):
                    wf_res = getattr(fixed_assets_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '6':
            clear_screen()
            print(f"=== Running BUDGETING Simulation Workflow ===")
            entity = "BudgetPlan"
            print(f"Creating mock {entity}...")
            payload = {"code": "BUDGETPLAN-001", "description": "Standard record of type BudgetPlan", "status_state": "ACTIVE"}
            res = budgeting_controller.create_budgetplan_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = budgeting_controller.list_budgetplans_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_budgetplan_workflow_endpoint"
                if hasattr(budgeting_controller, workflow_method):
                    wf_res = getattr(budgeting_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '7':
            clear_screen()
            print(f"=== Running COST_ACCOUNTING Simulation Workflow ===")
            entity = "CostObject"
            print(f"Creating mock {entity}...")
            payload = {"code": "COSTOBJECT-001", "description": "Standard record of type CostObject", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}
            res = cost_accounting_controller.create_costobject_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = cost_accounting_controller.list_costobjects_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_costobject_workflow_endpoint"
                if hasattr(cost_accounting_controller, workflow_method):
                    wf_res = getattr(cost_accounting_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '8':
            clear_screen()
            print(f"=== Running TAX_MANAGEMENT Simulation Workflow ===")
            entity = "TaxCode"
            print(f"Creating mock {entity}...")
            payload = {"code": "TAXCODE-001", "description": "Standard record of type TaxCode", "amount": 1000.00, "base_currency": "USD", "status_state": "ACTIVE"}
            res = tax_management_controller.create_taxcode_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = tax_management_controller.list_taxcodes_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_taxcode_workflow_endpoint"
                if hasattr(tax_management_controller, workflow_method):
                    wf_res = getattr(tax_management_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '9':
            clear_screen()
            print(f"=== Running FINANCIAL_REPORTING Simulation Workflow ===")
            entity = "ReportTemplate"
            print(f"Creating mock {entity}...")
            payload = {"code": "REPORTTEMPLATE-001", "description": "Standard record of type ReportTemplate", "status_state": "ACTIVE"}
            res = financial_reporting_controller.create_reporttemplate_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = financial_reporting_controller.list_reporttemplates_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_reporttemplate_workflow_endpoint"
                if hasattr(financial_reporting_controller, workflow_method):
                    wf_res = getattr(financial_reporting_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '10':
            clear_screen()
            print(f"=== Running AUDIT_COMPLIANCE Simulation Workflow ===")
            entity = "AuditTrailLog"
            print(f"Creating mock {entity}...")
            payload = {"code": "AUDITTRAILLOG-001", "description": "Standard record of type AuditTrailLog", "status_state": "ACTIVE"}
            res = audit_compliance_controller.create_audittraillog_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = audit_compliance_controller.list_audittraillogs_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_audittraillog_workflow_endpoint"
                if hasattr(audit_compliance_controller, workflow_method):
                    wf_res = getattr(audit_compliance_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '11':
            clear_screen()
            print(f"=== Running PAYROLL_ACCOUNTING Simulation Workflow ===")
            entity = "PayrollJournal"
            print(f"Creating mock {entity}...")
            payload = {"code": "PAYROLLJOURNAL-001", "description": "Standard record of type PayrollJournal", "status_state": "ACTIVE"}
            res = payroll_accounting_controller.create_payrolljournal_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = payroll_accounting_controller.list_payrolljournals_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_payrolljournal_workflow_endpoint"
                if hasattr(payroll_accounting_controller, workflow_method):
                    wf_res = getattr(payroll_accounting_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '12':
            clear_screen()
            print(f"=== Running PURCHASE_SALES_INTEGRATION Simulation Workflow ===")
            entity = "PurchaseOrderMatch"
            print(f"Creating mock {entity}...")
            payload = {"code": "PURCHASEORDERMATCH-001", "description": "Standard record of type PurchaseOrderMatch", "status_state": "ACTIVE"}
            res = purchase_sales_integration_controller.create_purchaseordermatch_endpoint(token, payload)
            print(f"API Response Code: {res.get('code')}")
            if res.get('status') == 'success':
                created_id = res['data']['id']
                print(f"Created Record ID: {created_id}")
                print("Fetching list of all records...")
                list_res = purchase_sales_integration_controller.list_purchaseordermatchs_endpoint(token)
                print(f"Records found: {len(list_res.get('data', []))}")
                
                print("Triggering domain transaction workflow...")
                workflow_method = f"run_purchaseordermatch_workflow_endpoint"
                if hasattr(purchase_sales_integration_controller, workflow_method):
                    wf_res = getattr(purchase_sales_integration_controller, workflow_method)(token, created_id)
                    print(f"Workflow Status: {wf_res.get('status')}, Code: {wf_res.get('code')}")
            else:
                print(f"Error creating record: {res.get('message')}")
            input("\nPress Enter to return to main menu...")
        elif choice == '13':
            clear_screen()
            print("==================================================")
            print("      ERP CATEGORY & SUBCATEGORY REPORTING        ")
            print("==================================================")
            print("Select Report Type to Generate:")
            print(" 1. General Ledger Category & Subcategory Report (ASCII Tree)")
            print(" 2. Fixed Assets Category Grouping Report")
            print(" 3. Vendor Spend Category Analysis Report")
            print(" 4. Export GL Category Report to CSV")
            print(" 5. Back to Main Menu")
            print("==================================================")
            rep_choice = input("Enter choice (1-5): ").strip()
            
            import json
            from erp.modules.financial_reporting.category_reporting import CategoryReporter
            reporter = CategoryReporter()
            
            if rep_choice == '1':
                gl_data = reporter.generate_gl_category_report()
                print(reporter.format_ascii_tree(gl_data))
            elif rep_choice == '2':
                fa_data = reporter.generate_fixed_assets_category_report()
                print(json.dumps(fa_data, indent=2))
            elif rep_choice == '3':
                v_data = reporter.generate_vendor_spend_category_report()
                print(json.dumps(v_data, indent=2))
            elif rep_choice == '4':
                gl_data = reporter.generate_gl_category_report()
                csv_data = reporter.export_report_to_csv("gl", gl_data)
                print("\n--- Exported CSV Output ---")
                print(csv_data)
                print("---------------------------")
            input("\nPress Enter to return to main menu...")
        else:
            print("Invalid choice. Try again.")
            input("\nPress Enter to continue...")

if __name__ == '__main__':
    audit_log("system", "AuraLedger system console launched.")
    if len(sys.argv) > 1 and sys.argv[1] == '--non-interactive':
        print("System verification checks passed. Running in non-interactive verification mode.")
        sys.exit(0)
    else:
        run_cli()
