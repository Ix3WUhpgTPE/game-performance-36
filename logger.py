import logging
import sys
import functools

class PerformanceLogger:
    def __init__(self, name='game-perf'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def safe_execute(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (MemoryError, RuntimeError) as e:
                self.logger.critical(f'Critical system failure in {func.__name__}: {e}')
                raise
            except Exception as e:
                self.logger.error(f'Unexpected jitter in {func.__name__}: {type(e).__name__} -> {e}')
                return None
        return wrapper

perf_logger = PerformanceLogger()

def log_game_event(func):
    return perf_logger.safe_execute(func)