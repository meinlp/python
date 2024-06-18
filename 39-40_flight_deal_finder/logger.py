import logging
import json


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'filename': record.filename,
            'funcName': record.funcName,
            'lineno': record.lineno
        }
        return json.dumps(log_record)


logger = logging.getLogger('jsonLogger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = JsonFormatter()
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def log(level, message):
    if level == 'debug':
        logger.debug(message)
    elif level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
