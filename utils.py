import time
import random
from functools import wraps

def retry_with_backoff(retries=3, backoff_in_seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if x == retries:
                        raise e
                    sleep_time = (backoff_in_seconds * (2 ** x) + random.uniform(0, 1))
                    time.sleep(sleep_time)
                    x += 1
        return wrapper
    return decorator

@retry_with_backoff(retries=3)
def fetch_game_data(endpoint):
    # Simulate volatile network state in game engine
    if random.random() < 0.7:
        raise ConnectionError("Packet loss detected")
    return {"status": "ready", "tick": 128}