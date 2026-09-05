import time
import functools
import random

def retry_network_ops(max_attempts=3, base_delay=0.5, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = base_delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    jitter = random.uniform(0, 0.1 * current_delay)
                    time.sleep(current_delay + jitter)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_ops(max_attempts=5)
def sync_game_state(payload):
    # Simulated unstable network call
    if random.random() < 0.7:
        raise ConnectionError("Packet loss detected")
    return {"status": "success", "data": payload}