import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a custom logger
logger = logging.getLogger(__name__)

# Define helper functions for logging

def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_debug(message):
    logger.debug(message)


def log_critical(message):
    logger.critical(message)  


def log_exception(exc):
    logger.exception(exc)