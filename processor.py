import time
import functools
import random
from typing import Callable, Any

def retry_with_backoff(retries: int = 3, base_delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    delay = base_delay * (2 ** attempt) + (random.random() * 0.1)
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

class NetworkProcessor:
    @retry_with_backoff(retries=3)
    def fetch_game_data(self, endpoint: str):
        # Simulated unstable network call
        if random.random() < 0.7:
            raise ConnectionError('Packet loss encountered')
        return {'status': 'success', 'data': 'payload_0x42'}

def process_stream():
    processor = NetworkProcessor()
    try:
        return processor.fetch_game_data('api/v1/sync')
    except Exception as err:
        return {'status': 'failed', 'reason': str(err)}