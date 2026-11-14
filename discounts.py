def apply_tier_discount(amount: float, tier: str) -> float:
rates = {"standard": 0.0, "silver": 0.05, "gold": 0.10}
rate = rates.get(tier.lower(), 0.0)
return round(amount * (1 - rate), 2)

def calculate_commission(net_amount: float, rate: float = 0.08) -> float:
if net_amount <= 0:
return 0.0
return round(net_amount * rate, 2)



