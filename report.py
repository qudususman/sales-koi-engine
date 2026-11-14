from orders import filter_valid_orders, calculate_total_revenue
from discounts import apply_tier_discount, calculate_commission

def build_sales_summary(orders: list[dict], tier: str = "standard") -> dict:
valid = filter_valid_orders(orders)
gross = calculate_total_revenue(valid)
net = apply_tier_discount(gross, tier)
return {
"order_count": len(valid),
"gross_revenue": gross,
"net_revenue": net,
"commission": calculate_commission(net),
}

