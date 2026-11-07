# src/tpp_mizan/__init__.py
"""TPP Mizan: FastAPI + CLI template."""

from importlib.metadata import PackageNotFoundError, version

try:
    # Reads the version directly from pyproject.toml
    __version__ = version("tpp-mizan")
except PackageNotFoundError:  # pragma: no cover
    # Fallback if the package is run directly without being installed
    __version__ = "0.1.0"
