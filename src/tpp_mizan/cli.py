# src/tpp_mizan/cli.py
import logging

import typer

from tpp_mizan import __version__
from tpp_mizan.core.logging import configure_loggers
from tpp_mizan.core.math_ops import add, div, multiply, subtract

# Logger is instantiated here, but handlers are attached later by configure_loggers()
logger = logging.getLogger(__name__)

app = typer.Typer(
    help="TPP Mizan: A production-ready math CLI tool for Tech Print Pack.",
    no_args_is_help=True,
    add_completion=False,
)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"tpp-mizan {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,  # <-- Changed from None to False to satisfy mypy strict mode
        "--version",
        # "-v" removed: reserved for future --verbose logging flag
        callback=version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
) -> None:
    """TPP Mizan CLI entry point."""
    # Initialize logging ONLY when the CLI is actually invoked.
    configure_loggers()


@app.command(name="add")
def add_cmd(
    x: float = typer.Argument(..., help="First number"),
    y: float = typer.Argument(..., help="Second number"),
) -> None:
    """Add X and Y."""
    logger.info("CLI request: add %s + %s", x, y)
    result = add(x, y)
    logger.info("CLI success: %s + %s = %s", x, y, result)
    typer.echo(f"Result: {x} + {y} = {result}")


@app.command(name="subtract")
def subtract_cmd(
    x: float = typer.Argument(..., help="Number to subtract from"),
    y: float = typer.Argument(..., help="Number to subtract"),
) -> None:
    """Subtract Y from X."""
    logger.info("CLI request: subtract %s - %s", x, y)
    result = subtract(x, y)
    logger.info("CLI success: %s - %s = %s", x, y, result)
    typer.echo(f"Result: {x} - {y} = {result}")


@app.command(name="multiply")
def multiply_cmd(
    x: float = typer.Argument(..., help="First number"),
    y: float = typer.Argument(..., help="Second number"),
) -> None:
    """Multiply X by Y."""
    logger.info("CLI request: multiply %s * %s", x, y)
    result = multiply(x, y)
    logger.info("CLI success: %s * %s = %s", x, y, result)
    typer.echo(f"Result: {x} * {y} = {result}")


@app.command(name="divide")
def divide_cmd(
    x: float = typer.Argument(..., help="The numerator"),
    y: float = typer.Argument(..., help="The denominator"),
) -> None:
    """Divide X by Y."""
    logger.info("CLI request: divide %s / %s", x, y)
    try:
        result = div(x, y)
        logger.info("CLI success: %s / %s = %s", x, y, result)
        typer.echo(f"Result: {x} / {y} = {result}")
    except ZeroDivisionError as e:
        # Log as WARNING: it's a client input error, not a system crash
        logger.warning("CLI division error: %s", e)
        typer.echo("Error: Division by zero.", err=True)
        raise typer.Exit(code=1) from None
