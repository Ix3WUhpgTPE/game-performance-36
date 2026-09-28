import time
import functools
import logging

logger = logging.getLogger('game-performance-36')

def retry_network(max_attempts=3, delay=1.0, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'Network failure after {attempts} attempts')
                        raise e
                    logger.warning(f'Network retry {attempts}/{max_attempts} in {current_delay}s')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

class AsyncNetworkBurst:
    def __init__(self, capacity=5):
        self.tokens = capacity
    
    def consume(self):
        if self.tokens > 0:
            self.tokens -= 1
            return True
        return False