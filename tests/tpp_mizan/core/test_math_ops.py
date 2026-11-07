# tests/tpp_mizan/core/test_math_ops.py
import pytest

from tpp_mizan.core.math_ops import add, div, multiply, subtract


def test_add():
    assert add(10.0, 2.0) == 12.0


def test_subtract():
    assert subtract(10.0, 2.0) == 8.0


def test_multiply():
    assert multiply(10.0, 2.0) == 20.0


def test_div_success():
    assert div(10.0, 2.0) == 5.0


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        div(10.0, 0.0)
