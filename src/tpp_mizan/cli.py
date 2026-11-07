# src/tpp_mizan/cli.py
import logging

import typer

from tpp_mizan.core.logging import configure_loggers
from tpp_mizan.core.math_ops import div

# Initialize logging when the CLI starts
configure_loggers()
logger = logging.getLogger(__name__)

app = typer.Typer(help="A simple division CLI tool.")


@app.command()
def divide(
    x: float = typer.Argument(..., help="The numerator"),
    y: float = typer.Argument(..., help="The denominator"),
):
    """Divide X by Y."""
    logger.info("CLI request: divide %s by %s", x, y)  # <-- Add this
    try:
        result = div(x, y)
        logger.info("CLI success: %s / %s = %s", x, y, result)  # <-- Add this
        typer.echo(f"Result: {x} / {y} = {result}")
    except ZeroDivisionError as e:
        logger.error("CLI error: %s", e)  # <-- Add this
        typer.echo("Error: Division by zero.", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
