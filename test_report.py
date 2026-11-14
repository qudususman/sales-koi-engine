import unittest
from orders import filter_valid_orders
from discounts import apply_tier_discount
from report import build_sales_summary

class TestSalesKPI(unittest.TestCase):
def test_filter_valid_orders(self):
sample = [
{"id": 1, "amount": 100, "status": "completed"},
{"id": 2, "amount": 50, "status": "cancelled"},
{"id": 3, "amount": -10, "status": "shipped"},
]
self.assertEqual(len(filter_valid_orders(sample)), 1)

def test_gold_discount(self):
self.assertEqual(apply_tier_discount(200.0, "gold"), 180.0)

def test_build_sales_summary(self):
sample = [
{"id": 1, "amount": 200, "status": "completed"},
{"id": 2, "amount": 300, "status": "shipped"},
]
summary = build_sales_summary(sample, tier="silver")
self.assertEqual(summary["order_count"], 2)
self.assertEqual(summary["net_revenue"], 475.0)

if __name__ == "__main__":
unittest.main()
