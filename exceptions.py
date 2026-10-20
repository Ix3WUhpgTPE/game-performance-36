import sys
import time
from typing import Callable, Any, Type, Dict


class PerformanceAnomalyError(Exception):
    """Base anomaly exception with bitmasked severity and auto-telemetry."""

    def __init__(self, message: str, severity_mask: int = 0b001, frame_delta: float = 0.0):
        super().__init__(message)
        self.severity_mask = severity_mask
        self.frame_delta = frame_delta
        self.timestamp = time.monotonic()

    @property
    def is_critical(self) -> bool:
        return bool(self.severity_mask & 0b100)


class FrameTimeSpikeError(PerformanceAnomalyError):
    """Raised when a single frame exceeds permissible render budget."""
    pass


class GPUThrottlingDetected(PerformanceAnomalyError):
    """Raised when clock speed drops unexpectedly under load."""
    pass


class EdgeCaseRegistry:
    _RECOVERY_HOOKS: Dict[Type[PerformanceAnomalyError], Callable] = {}

    @classmethod
    def register_recovery(cls, exc_type: Type[PerformanceAnomalyError]):
        def decorator(func: Callable):
            cls._RECOVERY_HOOKS[exc_type] = func
            return func
        return decorator

    @classmethod
    def mitigate(cls, exc: PerformanceAnomalyError) -> Any:
        handler = cls._RECOVERY_HOOKS.get(type(exc))
        if handler:
            return handler(exc)
        return {"status": "degraded", "fallback_target_fps": 30}


def telemetry_shield(default_return: Any = None):
    """Decorator to intercept frame edge cases and execute dynamic recovery."""
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PerformanceAnomalyError as exc:
                sys.stderr.write(f"[ANOMALY INTERCEPTED] {exc} (Mask: {bin(exc.severity_mask)})\n")
                return EdgeCaseRegistry.mitigate(exc)
            except ZeroDivisionError:
                synthetic_exc = FrameTimeSpikeError("Zero frame delta detected", severity_mask=0b101)
                return EdgeCaseRegistry.mitigate(synthetic_exc)
        return wrapper
    return decorator
