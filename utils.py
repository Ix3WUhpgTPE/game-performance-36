import time
import random
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("game_perf.net")

class NetworkRespawnError(Exception):
    """Raised when all packet respawn attempts fail."""
    pass

def retry_network_op(
    max_respawns: int = 3,
    base_ping_ms: float = 50.0,
    backoff_multiplier: float = 2.0,
    allowed_exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """
    Decorator executing network operations with a gaming-inspired
    ping jitter exponential backoff strategy upon packet loss.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            respawn_count = 0
            current_delay = base_ping_ms / 1000.0

            while True:
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as err:
                    respawn_count += 1
                    if respawn_count > max_respawns:
                        logger.error(f"[NetDesync] Call to {func.__name__} dropped after {max_respawns} retries: {err}")
                        raise NetworkRespawnError(f"Server connection lost in {func.__name__}: {err}") from err

                    jitter = random.uniform(0.8, 1.4)
                    sleep_time = current_delay * jitter
                    logger.warning(
                        f"[PacketLoss] Retry {respawn_count}/{max_respawns} for {func.__name__}. "
                        f"Respawning payload in {sleep_time * 1000:.1f}ms..."
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff_multiplier

        return wrapper
    return decorator
