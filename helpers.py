import time
from typing import Generator, Iterator, Callable, Any

def fps_estimator(alpha: float = 0.15) -> Generator[float, float, None]:
    """
    Stateful FPS estimator using a generator coroutine.
    Yields the smoothed FPS value when sent the frame delta time (dt).
    """
    dt = yield 0.0
    smoothed_fps = 1.0 / (dt if dt > 0 else 0.016)
    while True:
        dt = yield smoothed_fps
        if dt > 0:
            instant_fps = 1.0 / dt
            smoothed_fps = (alpha * instant_fps) + ((1.0 - alpha) * smoothed_fps)

class BudgetTracker:
    """
    A context manager tracking execution budget for performance-critical frames.
    Returns a dictionary to dynamically check or alter budget parameters mid-frame.
    """
    def __init__(self, target_fps: float = 60.0):
        self.limit = 1.0 / target_fps
        self.start = 0.0

    def __enter__(self) -> dict[str, float]:
        self.start = time.perf_counter()
        self.info = {"limit": self.limit, "elapsed": 0.0, "over_budget": 0.0}
        return self.info

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        elapsed = time.perf_counter() - self.start
        self.info["elapsed"] = elapsed
        self.info["over_budget"] = max(0.0, elapsed - self.info["limit"])
        return False

def load_balancer(tasks: list[Callable[[], Any]], max