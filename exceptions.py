from typing import Optional, Any

class PerformanceBaseError(Exception):
    """Base exception for all game-performance-36 issues."""
    def __init__(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context: dict[str, Any] = context or {}

class FrameDropError(PerformanceBaseError):
    """Raised when frame rate falls below configured thresholds."""
    pass

class ResourceLeakError(PerformanceBaseError):
    """Raised when memory or gpu usage exceeds safe limits."""
    pass

class InitializationError(PerformanceBaseError):
    """Raised when the engine fails to hook into the game process."""
    pass

def raise_if_critical(condition: bool, error_cls: type[PerformanceBaseError], message: str) -> None:
    """Conditional performance exception trigger mechanism."""
    if condition:
        raise error_cls(message)

if __name__ == '__main__':
    try:
        raise_if_critical(True, InitializationError, "Engine hook failed")
    except PerformanceBaseError as e:
        print(f"Caught performance anomaly: {e}")