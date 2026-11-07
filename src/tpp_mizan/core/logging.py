# src/tpp_mizan/core/logging.py
import logging
import logging.config
import os
from pathlib import Path

from dotenv import load_dotenv  # <-- Added import
from yaml import safe_load

_CONFIGURED = False  # <-- Guard against double initialization


def configure_loggers() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return

    package_dir = Path(__file__).resolve().parent.parent
    config_path = package_dir / "config" / "my_log.yaml"

    with open(config_path) as f:
        config = safe_load(f)

    # Dynamically set log path to project root, OR override via env var
    project_root = package_dir.parent.parent

    # Load environment variables from .env file in the project root
    # This justifies keeping the python-dotenv dependency!
    load_dotenv(project_root / ".env", override=False)

    log_dir = Path(os.getenv("TPP_MIZAN_LOG_DIR", str(project_root / "logs")))
    log_dir.mkdir(parents=True, exist_ok=True)

    config["handlers"]["json_file"]["filename"] = str(log_dir / "tpp_mizan.json.log")
    config["handlers"]["timed_file"]["filename"] = str(log_dir / "tpp_mizan_timed.log")

    # Override log level from env
    env_log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    config["loggers"]["tpp_mizan"]["level"] = env_log_level
    config["handlers"]["c_handler"]["level"] = env_log_level

    logging.config.dictConfig(config)
    _CONFIGURED = True
