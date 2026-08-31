import unittest
from erp.core.db import db_instance
from erp.modules.financial_reporting.category_reporting import CategoryReporter

class TestCategoryReporting(unittest.TestCase):
    def setUp(self):
        self.reporter = CategoryReporter()

    def test_gl_category_report(self):
        report = self.reporter.generate_gl_category_report()
        self.assertIn("balance_sheet_summary", report)
        self.assertIn("hierarchical_data", report)
        self.assertGreaterEqual(len(report["hierarchical_data"]), 1)

    def test_fixed_assets_category_report(self):
        report = self.reporter.generate_fixed_assets_category_report()
        self.assertIn("hierarchical_data", report)
        self.assertGreaterEqual(len(report["hierarchical_data"]), 1)

    def test_vendor_spend_category_report(self):
        report = self.reporter.generate_vendor_spend_category_report()
        self.assertIn("hierarchical_data", report)
        self.assertGreaterEqual(len(report["hierarchical_data"]), 1)

    def test_format_ascii_tree(self):
        report = self.reporter.generate_gl_category_report()
        tree_str = self.reporter.format_ascii_tree(report)
        self.assertIn("Balance Sheet Summary", tree_str)
        self.assertIn("ASSET", tree_str)

    def test_export_report_to_csv(self):
        report = self.reporter.generate_gl_category_report()
        csv_str = self.reporter.export_report_to_csv("gl", report)
        self.assertIn("Category,Subcategory", csv_str)
