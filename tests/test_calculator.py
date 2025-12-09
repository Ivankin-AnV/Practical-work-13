import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax
)


# ---------------------------
# Тесты для расчета простого интереса
# ---------------------------

def test_simple_interest_basic():
    assert calculate_simple_interest(1000, 5, 2) == 100.0
    assert calculate_simple_interest(1500, 3, 1) == 45.0

def test_simple_interest_zero():
    assert calculate_simple_interest(0, 5, 10) == 0
    assert calculate_simple_interest(1000, 0, 5) == 0

def test_simple_interest_negative():
    with pytest.raises(ValueError):
        calculate_simple_interest(-100, 5, 2)
    with pytest.raises(ValueError):
        calculate_simple_interest(100, -5, 2)
    with pytest.raises(ValueError):
        calculate_simple_interest(100, 5, -2)

# ---------------------------
# Тесты для расчета сложных процентов
# ---------------------------

def test_compound_interest_basic():
    assert round(calculate_compound_interest(1000, 10, 1), 2) == 1100.0
    assert round(calculate_compound_interest(2000, 5, 2, n=4), 2) == 2208.97


def test_compound_interest_zero():
    assert calculate_compound_interest(0, 10, 5) == 0
    assert calculate_compound_interest(1000, 0, 5) == 1000

def test_compound_interest_invalid():
    with pytest.raises(ValueError):
        calculate_compound_interest(-1000, 10, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, -10, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 10, -1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 10, 1, n=0)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 10, 1, n=-3)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 10, 1, n=2.5)

# ---------------------------
# Тесты для расчета налога
# ---------------------------

def test_tax_basic():
    assert calculate_tax(1000, 10) == 100
    assert calculate_tax(500, 5) == 25

def test_tax_zero():
    assert calculate_tax(0, 10) == 0
    assert calculate_tax(100, 0) == 0

def test_tax_invalid():
    with pytest.raises(ValueError):
        calculate_tax(-100, 10)
    with pytest.raises(ValueError):
        calculate_tax(100, -5)
    with pytest.raises(ValueError):
        calculate_tax(100, 150)
