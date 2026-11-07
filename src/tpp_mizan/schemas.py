# src/tpp_mizan/schemas.py
from typing import Literal

from pydantic import BaseModel


class MathResult(BaseModel):
    """Standard response model for all math operations."""

    operation: Literal["add", "subtract", "multiply", "divide"]
    x: float
    y: float
    result: float
