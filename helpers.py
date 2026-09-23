import time
import random
import functools
from typing import Callable, Any

def retry_operation(retries: int = 3, backoff: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_ex = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    sleep_time = backoff * (2 ** attempt) + (random.random() * 0.1)
                    time.sleep(sleep_time)
            raise last_ex
        return wrapper
    return decorator

def sync_network_call(func: Callable):
    @retry_operation(retries=5, backoff=1.0)
    def executed_call(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return executed_call