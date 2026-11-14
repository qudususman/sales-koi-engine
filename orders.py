def filter_valid_orders(orders: list[dict]) -> list[dict]:
valid = []
for order in orders:
amount = float(order.get("amount", 0))
status = str(order.get("status", "")).lower()
if amount > 0 and status in {"completed", "shipped"}:
valid.append(order)
return valid

def calculate_total_revenue(orders: list[dict]) -> float:
return round(sum(float(o["amount"]) for o in filter_valid_orders(orders)), 2)

