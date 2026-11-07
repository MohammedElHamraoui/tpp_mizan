# tests/conftest.py
import logging

import pytest

from tpp_mizan.core import logging as applog


@pytest.fixture(autouse=True)
def _isolate_logs(tmp_path, monkeypatch):
    # 1. Force logs to a unique temporary directory for this specific test
    monkeypatch.setenv("TPP_MIZAN_LOG_DIR", str(tmp_path / "logs"))

    # 2. Guard against a stray .env file overriding the log level during tests
    monkeypatch.delenv("LOG_LEVEL", raising=False)

    # 3. Allow configure_loggers() to run fresh
    applog._CONFIGURED = False

    yield

    # 4. Cleanup: Explicitly close and remove all handlers to prevent cross-test bleed
    pkg_logger = logging.getLogger("tpp_mizan")
    for handler in list(pkg_logger.handlers):
        handler.close()
        pkg_logger.removeHandler(handler)

    # 5. Reset the guard for the next test
    applog._CONFIGURED = False
