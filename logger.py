import logging

class GameLogger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def set_level(self, level):
        self.logger.setLevel(level)

# Example usage
if __name__ == '__main__':
    game_logger = GameLogger('GamePerformance')
    game_logger.info('Game has started')
    game_logger.warning('Low memory warning')
    game_logger.error('An error occurred')
    game_logger.critical('Critical issue')
    game_logger.debug('Debugging information')