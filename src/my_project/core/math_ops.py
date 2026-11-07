# src/my_project/core/math_ops.py
import logging

logger = logging.getLogger(__name__)


def div(x: float, y: float) -> float | None:
    """Divide function"""
    try:
        return x / y
    except ZeroDivisionError:
        logger.exception("A math error occurred: Division by zero!")
        return None
