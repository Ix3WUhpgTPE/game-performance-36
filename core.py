import time
import random
from typing import Callable, Any, TypeVar

R = TypeVar("R")

class NetworkSyncError(Exception):
    """Custom exception for persistent network failure in game loop."""
    pass

class FrameAwareRetry:
    """Retry engine aligning backoff pauses with simulated engine frame ticks."""
    
    def __init__(self, max_retries: int = 4, target_fps: int = 144):
        self.max_retries = max_retries
        self.tick_duration = 1.0 / target_fps

    def __call__(self, func: Callable[..., R]) -> Callable[..., R]:
        def wrapper(*args: Any, **kwargs: Any) -> R:
            last_exception = None
            current_backoff_ticks = 1

            for attempt in range(1, self.max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    if attempt == self.max_retries:
                        break
                    
                    sleep_ticks = current_backoff_ticks + random.randint(0, 2)
                    time.sleep(sleep_ticks * self.tick_duration)
                    current_backoff_ticks *= 2

            raise NetworkSyncError(
                f"Sync failed across {self.max_retries} attempts. Last error: {last_exception}"
            ) from last_exception

        return wrapper

@FrameAwareRetry(max_retries=3, target_fps=60)
def transmit_fps_metrics(server_ip: str, frame_data: dict) -> dict:
    if random.random() > 0.3:
        raise TimeoutError("UDP packet dropped during telemetry frame sync")
    return {"status": "ok", "ack_ticks": random.randint(1, 5)}