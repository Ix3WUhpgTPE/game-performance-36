import math
from typing import Any, Dict, List

class TelemetryAnomaly(Exception):
    """Raised when game telemetry produces physically impossible metrics."""
    pass

class ResilientFrameHandler:
    def __init__(self, target_fps: float = 60.0):
        self.target_fps = target_fps
        self.last_valid_delta = 1.0 / target_fps
        self.history: List[float] = []

    def sanitize_metric(self, raw_val: Any, default: float) -> float:
        """Safe extraction using dynamic type coercion and bounds checking."""
        try:
            if raw_val is None or isinstance(raw_val, (bool, str)):
                raise TelemetryAnomaly(f"Invalid payload type: {type(raw_val)}")
            
            val = float(raw_val)
            if math.isnan(val) or math.isinf(val) or val < 0:
                raise TelemetryAnomaly(f"Out of bounds metric value: {val}")
            return val
        except (ValueError, TypeError, TelemetryAnomaly):
            if self.history:
                return sum(self.history) / len(self.history)
            return default

    def execute_safe_frame(self, frame_id: int, raw_metrics: Dict[str, Any]) -> Dict[str, float]:
        """Process frame telemetry, swallowing edge-case corruptions gracefully."""
        clean_data = {}
        fallback_map = {
            "frame_time_ms": self.last_valid_delta * 1000.0,
            "fps": self.target_fps,
            "gpu_temp_c": 65.0,
            "vram_used_mb": 0.0
        }

        for key, default_val in fallback_map.items():
            val = self.sanitize_metric(raw_metrics.get(key), default_val)
            
            if key == "frame_time_ms" and val == 0.0:
                val = 0.001
            
            clean_data[key] = round(val, 4)

        self.history.append(clean_data["frame_time_ms"])
        if len(self.history) > 10:
            self.history.pop(0)

        self.last_valid_delta = clean_data["frame_time_ms"] / 1000.0
        return clean_data