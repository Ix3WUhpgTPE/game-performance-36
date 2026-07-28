import logging

class GameLogger:
    def __init__(self, name='GameLogger'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('game_events.log')
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_event(self, event_type, message):
        if event_type.upper() == 'INFO':
            self.logger.info(message)
        elif event_type.upper() == 'WARNING':
            self.logger.warning(message)
        elif event_type.upper() == 'ERROR':
            self.logger.error(message)
        else:
            self.logger.debug(f'Unknown event type: {event_type} - {message}')

    def close(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)

# Example usage:
# logger = GameLogger()
# logger.log_event('INFO', 'Game started')
# logger.close()