# tests/my_project/test_cli.py
from typer.testing import CliRunner

from my_project.cli import app

runner = CliRunner()  # No special parameters needed


def test_cli_divide_success():
    result = runner.invoke(app, ["10", "2"])
    assert result.exit_code == 0
    assert "Result: 10.0 / 2.0 = 5.0" in result.output  # Changed to .output


def test_cli_divide_by_zero():
    result = runner.invoke(app, ["10", "0"])
    assert result.exit_code == 1
    assert "Error: Division by zero." in result.output  # Changed to .output
