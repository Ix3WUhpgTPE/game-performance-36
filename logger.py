import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f'{name}.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)

# Example usage:
if __name__ == '__main__':
    game_logger = GameLogger('game_performance')
    game_logger.info('Game started')
    game_logger.warning('Low memory warning')
    game_logger.error('An error occurred')
    game_logger.debug('Debug information')
    game_logger.critical('Critical error!')