import time
import functools
import random

def retry_network_call(max_retries=3, backoff_factor=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_retries:
                        raise e
                    sleep_time = backoff_factor * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def async_retry(max_retries=3):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if i == max_retries - 1:
                        raise e
                    await asyncio.sleep(1)
        return wrapper
    return decorator