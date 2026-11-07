# tests/tpp_mizan/test_cli.py
from typer.testing import CliRunner

from tpp_mizan.cli import app

runner = CliRunner()


def test_cli_add():
    result = runner.invoke(app, ["add", "10", "2"])
    assert result.exit_code == 0
    assert "Result: 10.0 + 2.0 = 12.0" in result.output


def test_cli_subtract():
    result = runner.invoke(app, ["subtract", "10", "2"])
    assert result.exit_code == 0
    assert "Result: 10.0 - 2.0 = 8.0" in result.output


def test_cli_multiply():
    result = runner.invoke(app, ["multiply", "10", "2"])
    assert result.exit_code == 0
    assert "Result: 10.0 * 2.0 = 20.0" in result.output


def test_cli_divide_success():
    result = runner.invoke(app, ["divide", "10", "2"])
    assert result.exit_code == 0
    assert "Result: 10.0 / 2.0 = 5.0" in result.output


def test_cli_divide_by_zero():
    result = runner.invoke(app, ["divide", "10", "0"])
    assert result.exit_code == 1
    assert "Error: Division by zero." in result.output


def test_cli_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "tpp-mizan" in result.output


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "add" in result.output
    assert "subtract" in result.output
    assert "multiply" in result.output
    assert "divide" in result.output
