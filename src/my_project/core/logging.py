# src/my_project/core/logging.py
import logging
import logging.config
import os
from pathlib import Path

from yaml import safe_load


def configure_loggers():
    package_dir = Path(__file__).resolve().parent.parent
    config_path = package_dir / "config" / "my_log.yaml"

    with open(config_path) as f:
        config = safe_load(f)

    # Dynamically set log path to project root
    project_root = package_dir.parent.parent
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    config["handlers"]["json_file"]["filename"] = str(log_dir / "my_project.json.log")

    # Override log level from env
    env_log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    config["loggers"]["my_project"]["level"] = env_log_level

    logging.config.dictConfig(config)
