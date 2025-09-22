import pytest
from homework.b_in_proc_out.output import multiply_numbers

@pytest.mark.parametrize("a,b,expected", [
    (7, 7, 49),
    (5, 5, 25),
    (0, 5, 0),
    (-3, 4, -12),
    (2.5, 2, 5.0),
])
def test_multiply_numbers(a, b, expected):
    assert multiply_numbers(a, b) == expected
