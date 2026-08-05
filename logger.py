import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def validate_input(self, input_value):
        if not isinstance(input_value, (int, str)):
            self.log_error('Invalid input type')
            return False
        return True

logger = GameLogger('GamePerformanceLogger')

# Sample input processing loop
input_values = [10, 'valid_input', None]
for value in input_values:
    if logger.validate_input(value):
        logger.log_info(f'Processing: {value}')
    else:
        logger.log_warning(f'Skipped invalid input: {value}')