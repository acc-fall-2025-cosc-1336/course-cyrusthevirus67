import pytest
from homework.b_in_proc_out.output import TAX_RATE, get_sales_tax_amount, get_tip_amount

def test_sales_tax_on_20_dollars():
    assert get_sales_tax_amount(20.0) == pytest.approx(20.0 * TAX_RATE, rel=1e-12)

@pytest.mark.parametrize("meal", [0.0, 12.34, 99.99, 1.11])
def test_sales_tax_various(meal):
    assert get_sales_tax_amount(meal) == pytest.approx(meal * TAX_RATE, rel=1e-12)

def test_tip_basic_15_percent_on_20():
    assert get_tip_amount(20.0, 0.15) == pytest.approx(3.0, rel=1e-12)

@pytest.mark.parametrize("meal,rate,expected", [
    (50.0, 0.20, 10.0),
    (80.0, 0.10, 8.0),
    (0.0,  0.18, 0.0),
    (12.34, 0.175, 2.1595),
])
def test_tip_various(meal, rate, expected):
    assert get_tip_amount(meal, rate) == pytest.approx(expected, rel=1e-12)
