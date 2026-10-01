import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-36')

def with_retry(max_attempts=3, backoff=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'Critical network failure after {attempts} attempts: {e}')
                        raise
                    sleep_time = backoff * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    logger.warning(f'Retrying {func.__name__} in {sleep_time:.2f}s...')
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@with_retry(max_attempts=4)
def fetch_server_metrics(url):
    # Simulate network instability for performance tracking
    if random.random() < 0.7:
        raise ConnectionError('Packet loss detected')
    return {'ping': 'low', 'status': 'optimized'}