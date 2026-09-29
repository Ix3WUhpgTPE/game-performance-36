from typing import Optional, Any

class PerformanceError(Exception):
    """Base exception for the game-performance-36 engine."""
    def __init__(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context = context or {}

class FrameDropError(PerformanceError):
    """Raised when the render pipeline latency exceeds thresholds."""
    def __init__(self, fps: float, target: float) -> None:
        super().__init__(f"frame rate dropped to {fps}, target {target}", {"fps": fps, "target": target})

class AssetLoadTimeout(PerformanceError):
    """Raised when resource streaming exceeds buffer time."""
    def __init__(self, asset_id: str, elapsed: float) -> None:
        super().__init__(f"timeout loading {asset_id} after {elapsed}s", {"asset_id": asset_id})

class ThermalThrottleWarning(PerformanceError):
    """Alert for hardware-level clock speed reduction events."""
    def __init__(self, temperature: float) -> None:
        super().__init__(f"thermal throttling active at {temperature}C", {"temp": temperature})

def raise_if_critical(condition: bool, exception_class: type[PerformanceError], *args: Any) -> None:
    """Conditional exception raiser for performance pipeline stability."""
    if condition:
        raise exception_class(*args)