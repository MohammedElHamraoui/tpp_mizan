# tests/my_project/core/test_math_ops.py
import pytest

from my_project.core.math_ops import div


def test_div_success():
    assert div(10.0, 2.0) == 5.0


def test_div_by_zero():
    # Verify that calling div with 0 raises a ZeroDivisionError
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        div(10.0, 0.0)
