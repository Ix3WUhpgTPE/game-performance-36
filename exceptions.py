import time
import functools
from typing import Callable, Any

class NetworkGlitch(Exception):
    pass

def retry_logic(attempts: int = 3, delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_ex = None
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, NetworkGlitch) as e:
                    last_ex = e
                    if i < attempts - 1:
                        time.sleep(delay * (2 ** i))
            raise last_ex
        return wrapper
    return decorator

@retry_logic(attempts=4, delay=0.2)
def fetch_game_data(endpoint: str):
    # Simulate volatile gaming server connection
    if time.time() % 2 > 1:
        raise NetworkGlitch("packet loss detected")
    return {"status": "ready", "endpoint": endpoint}