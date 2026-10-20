from typing import Union, Optional, Callable

Numeric = Union[int, float]

def frame_rate_cap(limit: Numeric) -> Callable[[Numeric], Numeric]:
    """
    factory for strict frame rate bounding.
    returns a function that clamps input to a performance-friendly range.
    """
    def validator(fps: Numeric) -> Numeric:
        return min(max(0, fps), limit)
    return validator

def validate_latency(ms: Numeric, threshold: Numeric = 50.0) -> bool:
    """
    check against input lag thresholds.
    returns true if latency is within the acceptable gaming window.
    """
    return ms <= threshold

def sanitize_config_value(value: Optional[str], default: str = "off") -> str:
    """
    string normalization for game settings.
    ensures user inputs conform to expected toggle states.
    """
    allowed = {"on", "off", "ultra", "low"}
    clean_val = str(value).lower() if value else ""
    return clean_val if clean_val in allowed else default

class PerformanceGuard:
    """
    context manager for tracking performance metrics.
    """
    def __init__(self, target: str):
        self.target = target

    def __enter__(self) -> None:
        pass

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        pass