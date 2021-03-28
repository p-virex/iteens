import logging
import logging.config
import os
import sys

from logging import FileHandler

LOG_FOLDER = 'Logs'

if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)

OUTPUT_LOG = 'python.log'

DATEFORMAT = '%Y-%m-%d %H:%M:%S'

FOLDER_LOGS = os.path.join(os.getcwd(), LOG_FOLDER)


CONSOLE_FORMATTER = logging.Formatter(
    fmt="%(asctime)s > %(filename)s > %(lineno)s > %(levelname)s : %(message)s",
    datefmt=DATEFORMAT
)

LOGGER_FORMATTER = logging.Formatter(
    fmt="%(asctime)s > %(module)s > %(levelname)s : %(message)s",
    datefmt=DATEFORMAT
)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(CONSOLE_FORMATTER)
    console_handler.setLevel(logging.DEBUG)
    return console_handler


def get_current_launch_file_handler():
    file_handler = FileHandler(os.path.join(FOLDER_LOGS, OUTPUT_LOG), mode='w', encoding='utf-8')
    file_handler.setFormatter(LOGGER_FORMATTER)
    file_handler.setLevel(logging.INFO)
    return file_handler


root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(get_console_handler())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(get_current_launch_file_handler())
