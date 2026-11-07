# src/my_project/cli.py
import typer

from my_project.core.logging import configure_loggers
from my_project.core.math_ops import div

# Initialize logging when the CLI starts
configure_loggers()

app = typer.Typer(help="A simple division CLI tool.")


@app.command()
def divide(
    x: float = typer.Argument(..., help="The numerator"),
    y: float = typer.Argument(..., help="The denominator"),
):
    """Divide X by Y."""
    result = div(x, y)
    if result is not None:
        typer.echo(f"Result: {x} / {y} = {result}")
    else:
        typer.echo("Error: Division by zero.", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
