import pytest
from src.homework.c_decisions.decisions import (
    get_letter_grade_if,
    get_letter_grade_switch,
    get_letter_grade,
)

@pytest.mark.parametrize("score, expected", [
    (95, "A"),
    (85, "B"),
    (75, "C"),
    (65, "D"),
    (50, "F"),
])
def test_get_letter_grade_if(score, expected):
    assert get_letter_grade_if(score) == expected

@pytest.mark.parametrize("score, expected", [
    (95, "A"),
    (85, "B"),
    (75, "C"),
    (65, "D"),
    (50, "F"),
])
def test_get_letter_grade_switch(score, expected):
    assert get_letter_grade_switch(score) == expected

def test_alias_func_exists():
    assert get_letter_grade(95) == "A"

@pytest.mark.parametrize("bad", [-1, 101])
def test_out_of_range_raises(bad):
    with pytest.raises(ValueError):
        get_letter_grade_if(bad)
    with pytest.raises(ValueError):
        get_letter_grade_switch(bad)
