import time
import random
from functools import wraps

def jitter_retry(max_retries=3, backoff=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_retries:
                        raise e
                    delay = (backoff * (2 ** attempts)) + (random.uniform(0, 0.1))
                    time.sleep(delay)
        return wrapper
    decorator.retry_meta = {'max': max_retries, 'policy': 'exponential-jitter'}
    return decorator

@jitter_retry(max_retries=5)
def execute_network_call(payload):
    if random.random() < 0.7:
        raise ConnectionError("packet loss in game lobby")
    return {"status": "success", "data": payload}

if __name__ == "__main__":
    try:
        result = execute_network_call({"match_id": 42})
        print(f"Sync success: {result}")
    except Exception as err:
        print(f"Critical failure after retries: {err}")