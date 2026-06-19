import logging
import sys

class Logger:
    def __init__(self, name='GameLogger', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def validate_input(self, user_input):
        if not isinstance(user_input, str):
            self.log_error('Input must be a string')
            return False
        if user_input.strip() == '':
            self.log_warning('Empty input received')
            return False
        return True

if __name__ == '__main__':
    logger = Logger()
    inputs = ['valid input', '', 123, None]
    for inp in inputs:
        if logger.validate_input(inp):
            logger.log_info(f'Valid input: {inp}')
        else:
            logger.log_warning(f'Invalid input: {inp}')
