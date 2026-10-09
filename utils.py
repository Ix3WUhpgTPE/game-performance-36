import time
import random
import functools
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("game_network")

def jittery_fibonacci_retry(
    retries: int = 4,
    base_delay: float = 0.05,
    allowed_exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    A non-linear retry mechanism utilizing a Fibonacci progression and randomized 
    jitter to stagger reconnection storming from active game clients.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            fib_prev, fib_curr = base_delay, base_delay
            
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as exc:
                    if attempt == retries:
                        raise exc
                    
                    # Stagger network requests with randomized scale factor
                    jitter = random.uniform(0.8, 1.3)
                    wait_time = fib_curr * jitter
                    
                    # Advance sequence
                    fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
                    
                    logger.warning(
                        "Network event '%s' errored (attempt %d/%d). Retrying in %.3fs... Error: %s",
                        func.__name__, attempt, retries, wait_time, exc
                    )
                    time.sleep(wait_time)
        return wrapper
    return decorator