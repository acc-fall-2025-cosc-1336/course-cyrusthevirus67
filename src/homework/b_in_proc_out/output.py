from typing import Final

# HW02 constant
TAX_RATE: Final[float] = 0.0675  # 6.75%

def get_sales_tax_amount(meal_amount: float) -> float:
    """Return sales tax = meal_amount * TAX_RATE."""
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount: float, tip_rate: float) -> float:
    """Return tip amount = meal_amount * tip_rate (tip_rate as decimal, e.g., 0.15 for 15%)."""
    return meal_amount * tip_rate

# Keep this so older HW01 tests won't crash if they run
def multiply_numbers(a: float, b: float) -> float:
    """Return a * b (for HW01 compatibility)."""
    return a * b
