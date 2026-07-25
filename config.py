import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIRECTORY = 'logs'
LOG_FILENAME = 'game_performance.log'
LOG_PATH = os.path.join(LOG_DIRECTORY, LOG_FILENAME)

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logger = logging.getLogger('GamePerformanceLogger')
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(LOG_PATH, maxBytes=5 * 1024 * 1024, backupCount=3)
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)