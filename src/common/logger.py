import logging
import os

from src.variables import (
    log_format,
    PROJECT_DIR,
)


logs_dir_path = f"{PROJECT_DIR}/logs"
if not os.path.isdir(logs_dir_path):
    os.mkdir(logs_dir_path)


def logger_setup(
        log_name: str,
        filename: str,
        level=logging.INFO,
) -> logging.Logger:
    """
    Sets up a new logger config.

    :param log_name: Name of Logger. Make sure unique name is given for each Log
    :param filename: Name of filename
    :param level: Logger level of severity
    :returns: An instance of the Logger class
    """
    # Set up formatting style
    formatter = logging.Formatter(log_format)

    handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)

    # Create logger with name, level and handler
    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Configure logging settings
log_error = logger_setup("error", "logs/error.log")
