import time
import functools
from typing import Callable, Any, Type

def retry_session(attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tries, current_delay = attempts, delay
            while tries > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries -= 1
                    if tries == 0:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

class GameNetworkLayer:
    def __init__(self, timeout: int = 5):
        self.timeout = timeout

    @retry_session(attempts=4, delay=0.5)
    def fetch_match_data(self, match_id: str):
        print(f"Fetching match: {match_id}")
        # Simulated unstable network call
        if time.time() % 2 < 1:
            raise ConnectionError("Packet loss detected")
        return {"status": "victory", "id": match_id}