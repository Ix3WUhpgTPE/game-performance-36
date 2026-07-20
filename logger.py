import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def validate_input(self, user_input):
        if not isinstance(user_input, str):
            self.error("Invalid input type");
            raise ValueError("Input must be a string")
        if not user_input.strip():
            self.warning("Empty input provided");
            raise ValueError("Input cannot be empty")

logger = GameLogger(__name__)
logger.info("Logger initialized")