import logging
import logging.config
import os
from pathlib import Path

from dotenv import load_dotenv
from yaml import safe_load

# 1. Load environment variables from the .env file at project root
load_dotenv()

logger = logging.getLogger(__name__)


def configure_loggers():
    # 1. Get the directory where THIS python file lives (src/my_project/)
    package_dir = Path(__file__).resolve().parent

    # 2. Point directly to the config folder next to it
    config_path = package_dir / "config" / "my_log.yaml"

    # 3. Load the YAML
    with open(config_path) as f:
        config = safe_load(f)

    # 4. Dynamically set the log file path to a root-level 'logs' folder
    project_root = package_dir.parent.parent
    log_dir = project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)  # Creates 'logs' if it doesn't exist

    # Inject the absolute path into the config
    config["handlers"]["json_file"]["filename"] = str(log_dir / "my_project.json.log")

    # 5. Dynamically override log level from environment (defaults to DEBUG)
    env_log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    config["loggers"]["my_project"]["level"] = env_log_level

    # 6. Apply configuration
    logging.config.dictConfig(config)
    logger.info(f"Logging configured. Level: {env_log_level}")


def main():
    x = input("What's x? ")
    if not is_numeric_string(x):
        logger.warning("%s is not a number", x)
        return

    y = input("What's y? ")
    if not is_numeric_string(y):
        logger.warning("%s is not a number", y)
        return

    result = div(float(x), float(y))
    if result is not None:
        logger.info("Div: %s / %s = %s", x, y, result)


def div(x, y):
    """Divide function"""
    try:
        return x / y
    except ZeroDivisionError:
        # logger.exception automatically logs the full traceback!
        logger.exception("A math error occurred: Division by zero!")
        return None


def is_numeric_string(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def run():
    configure_loggers()
    main()
