import logging
import os.path

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = f'{CURRENT_DIR}/logs.log'
LOG_LEVEL = logging.DEBUG

logging.basicConfig(filename=LOG_PATH, filemode="w", format="%(name)s → %(levelname)s: %(message)s", level=LOG_LEVEL)
