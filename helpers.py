import time
import functools
import random

def retry_network(max_attempts=3, base_delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    # Exponential backoff with a sprinkle of chaos for game servers
                    sleep_time = (base_delay * (2 ** (attempts - 1))) + (random.random() * 0.5)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def validate_packet(data):
    if not data or not isinstance(data, dict):
        raise ValueError('corrupted packet structure')
    return True