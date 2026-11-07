# src/tpp_mizan/core/math_ops.py
import logging

logger = logging.getLogger(__name__)


def add(x: float, y: float) -> float:
    """Add x and y."""
    logger.info("Performing addition: %s + %s", x, y)
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract y from x."""
    logger.info("Performing subtraction: %s - %s", x, y)
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply x by y."""
    logger.info("Performing multiplication: %s * %s", x, y)
    return x * y


def div(x: float, y: float) -> float:
    """Divide x by y. Raises ZeroDivisionError if y is 0."""
    if y == 0:
        # Pure function: no logging, just raise the domain exception
        raise ZeroDivisionError("Cannot divide by zero")
    logger.info("Performing division: %s / %s", x, y)
    return x / y
