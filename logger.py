import logging

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

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

    def set_level(self, level):
        self.logger.setLevel(level)

    def remove_handler(self):
        self.logger.removeHandler(self.handler)
        self.handler.close()