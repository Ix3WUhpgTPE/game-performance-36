import time
import random
import asyncio
import functools
import inspect
from typing import Callable, Any, Type, Tuple

def resilient_retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    max_attempts: int = 5,
    base_delay: float = 0.1,
    backoff_factor: float = 1.618,
    max_jitter: float = 0.05
) -> Callable:
    """
    A dual-mode (sync/async) retry decorator using Golden Ratio backoff
    and micro-jitter to mitigate thundering herd problems in game matches.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def calculate_delay(attempt: int) -> float: 
            delay = base_delay * (backoff_factor ** attempt)
            jitter = random.uniform(-max_jitter, max_jitter) * delay
            return max(0.01, delay + jitter)

        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_attempts - 1:
                        raise err
                    await asyncio.sleep(calculate_delay(attempt))

        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_attempts - 1:
                        raise err
                    time.sleep(calculate_delay(attempt))

        return async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper

    return decorator