import logging

class GameLogger:
    def __init__(self, name='GameLogger'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('game.log')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Usage Example:
if __name__ == '__main__':
    log = GameLogger()
    log.info('Game started')
    log.debug('Player moved to position (10, 20)')
    log.warning('Low health warning')
    log.error('Player died')
    log.critical('Game crashed unexpectedly')