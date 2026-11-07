import pytest

from tpp_mizan.core import logging as applog


@pytest.fixture(autouse=True)
def _isolate_logs(tmp_path, monkeypatch):
    monkeypatch.setenv("TPP_MIZAN_LOG_DIR", str(tmp_path / "logs"))
    applog._CONFIGURED = False
    yield
    applog._CONFIGURED = False
