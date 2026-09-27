import pytest

from toolkit.calculator import calculate_expression
from toolkit.errors import DivisionByZeroError, InvalidExpression, VacuousExpression

import subprocess
import sys

@pytest.mark.parametrize("expression, expected", [
    ("2+3*4", 14),
    ("10/4", 2.5),
    ("-2*-3", 6),
    ("1+-2", -1),
    (" 2 + 3 ", 5),
])
def test_calculate(expression, expected):
    assert calculate_expression(expression) == expected


@pytest.mark.parametrize("expression", [" ", "2#1", "a + 3", "2+2+", "2*/3"])
def test_invalid_expression(expression):
    with pytest.raises(InvalidExpression):
        calculate_expression(expression)


def test_empty_expression():
    with pytest.raises(VacuousExpression):
        calculate_expression("")


def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate_expression("1/0")


