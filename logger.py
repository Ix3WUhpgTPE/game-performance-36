import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1)
    handler.setFormatter(formatter)
    handler.suffix = '%Y-%m-%d'

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    logger = setup_logger('my_logger', 'game_play.log')
    logger.info('Logger initialized and ready.')
    logger.error('This is a test error message.')
    logger.debug('Debugging information is logged here.')