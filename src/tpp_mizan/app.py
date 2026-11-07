# src/tpp_mizan/app.py
import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from tpp_mizan.core.logging import configure_loggers
from tpp_mizan.core.math_ops import add, div, multiply, subtract
from tpp_mizan.schemas import MathResult


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    configure_loggers()
    yield


logger = logging.getLogger(__name__)
app = FastAPI(title="TPP Mizan API", lifespan=lifespan)


@app.get("/")
def read_root() -> dict[str, str]:
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to TPP Mizan API"}


@app.get("/add/{x}/{y}", response_model=MathResult)
def add_endpoint(x: float, y: float) -> MathResult:
    logger.info("API request: add %s + %s", x, y)
    return MathResult(operation="add", x=x, y=y, result=add(x, y))


@app.get("/subtract/{x}/{y}", response_model=MathResult)
def subtract_endpoint(x: float, y: float) -> MathResult:
    logger.info("API request: subtract %s - %s", x, y)
    return MathResult(operation="subtract", x=x, y=y, result=subtract(x, y))


@app.get("/multiply/{x}/{y}", response_model=MathResult)
def multiply_endpoint(x: float, y: float) -> MathResult:
    logger.info("API request: multiply %s * %s", x, y)
    return MathResult(operation="multiply", x=x, y=y, result=multiply(x, y))


@app.get("/divide/{x}/{y}", response_model=MathResult)
def divide_endpoint(x: float, y: float) -> MathResult:
    logger.info("API request: divide %s / %s", x, y)
    try:
        return MathResult(operation="divide", x=x, y=y, result=div(x, y))
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None
