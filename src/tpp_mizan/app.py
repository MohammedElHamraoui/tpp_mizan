# src/tpp_mizan/app.py
import logging

from fastapi import FastAPI, HTTPException

from tpp_mizan.core.logging import configure_loggers
from tpp_mizan.core.math_ops import div

# Initialize logging when the API module is loaded
logger = logging.getLogger(__name__)
configure_loggers()


app = FastAPI(title="My Project API")


@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to My Project API"}


@app.get("/divide/{x}/{y}")
def divide(x: float, y: float):
    logger.info("API request: divide %s by %s", x, y)
    try:
        result = div(x, y)
        return {"x": x, "y": y, "result": result}
    except ZeroDivisionError as e:
        logger.error("API error: %s", e)
        # Return a proper HTTP 400 error instead of a 500 server crash
        raise HTTPException(status_code=400, detail=str(e))
