import logging

# Configure the logger to display messages in the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Logger:
    """
    A simple logger class for logging messages.
    Supports different levels of logging: DEBUG, INFO, WARNING, ERROR, CRITICAL.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize the logger with the given name.
        :param name: Name of the logger.
        """
        self.logger = logging.getLogger(name)

    def debug(self, message: str) -> None:
        """
        Log a message at DEBUG level.
        :param message: The message to log.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Log a message at INFO level.
        :param message: The message to log.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Log a message at WARNING level.
        :param message: The message to log.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Log a message at ERROR level.
        :param message: The message to log.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Log a message at CRITICAL level.
        :param message: The message to log.
        """
        self.logger.critical(message)