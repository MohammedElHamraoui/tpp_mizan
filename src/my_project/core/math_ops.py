# src/my_project/core/math_ops.py
import logging

logger = logging.getLogger(__name__)


def div(x: float, y: float) -> float:
    """Divide x by y. Raises ZeroDivisionError if y is 0."""
    if y == 0:
        logger.error("A math error occurred: Division by zero!")
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
