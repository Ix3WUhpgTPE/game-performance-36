from typing import List, Dict, Union, Any
import time

def calculate_frame_budget(refresh_rate: int, overhead_ms: float = 1.5) -> float:
    """
    calculates the precise milliseconds available per frame 
    accounting for system overhead in high-perf gaming contexts.
    """
    total_frame_time: float = 1000.0 / refresh_rate
    return max(0.0, total_frame_time - overhead_ms)

def sanitize_telemetry_data(payload: Dict[str, Any]) -> Dict[str, Union[str, float]]:
    """
    flattens nested telemetry objects to optimize serialization performance 
    for real-time metric streaming.
    """
    sanitized: Dict[str, Union[str, float]] = {}
    for key, value in payload.items():
        if isinstance(value, dict):
            for sub_key, sub_val in value.items():
                sanitized[f"{key}_{sub_key}"] = float(sub_val) if isinstance(sub_val, (int, float)) else str(sub_val)
        else:
            sanitized[key] = value
    return sanitized

def throttled_execution(func: callable, interval: float) -> callable:
    """
    decorator applying a time-based execution gate to prevent 
    performance spikes in event-driven loops.
    """
    last_run: float = 0.0
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal last_run
        now: float = time.time()
        if now - last_run > interval:
            last_run = now
            return func(*args, **kwargs)
        return None
    return wrapper