# src/tpp_mizan/core/math_ops.py
# Removed logger import and instantiation since we no longer need it here.


def add(x: float, y: float) -> float:
    """Add x and y."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract y from x."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply x by y."""
    return x * y


def div(x: float, y: float) -> float:
    """Divide x by y. Raises ZeroDivisionError if y is 0."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
