import math
from dataclasses import dataclass
from typing import Any, Dict


class TelemetryValidationError(ValueError):
    """Raised when game telemetry data fails edge-case integrity checks."""
    pass


@dataclass(frozen=True)
class FrameMetric:
    timestamp_ms: float
    frame_time_ms: float
    gpu_temp_c: float
    vram_usage_mb: float


class TelemetryGuard:
    """Dynamic validator for game frame telemetry with creative edge-case guards."""

    __slots__ = ('_last_timestamp', '_max_jitter_ms', '_strict_mode')

    def __init__(self, max_jitter_ms: float = 250.0, strict_mode: bool = False):
        self._last_timestamp: float = -1.0
        self._max_jitter_ms: float = max_jitter_ms
        self._strict_mode: bool = strict_mode

    def sanitize_metric(self, raw_data: Dict[str, Any]) -> FrameMetric:
        """Validates and sanitizes incoming frame telemetry against corrupt edge cases."""
        if not isinstance(raw_data, dict) or not raw_data:
            raise TelemetryValidationError("Malformed telemetry payload: expected non-empty dictionary.")

        required_keys = {'ts', 'frametime', 'gpu_temp', 'vram'}
        if missing := required_keys - raw_data.keys():
            raise TelemetryValidationError(f"Missing required telemetry attributes: {missing}")

        ts = float(raw_data['ts'])
        ft = float(raw_data['frametime'])
        temp = float(raw_data['gpu_temp'])
        vram = float(raw_data['vram'])

        # Edge case: Floating point anomalies (NaN, Inf)
        for key, val in [('ts', ts), ('frametime', ft), ('gpu_temp', temp), ('vram', vram)]:
            if math.isnan(val) or math.isinf(val):
                if self._strict_mode:
                    raise TelemetryValidationError(f"Unstable float value '{val}' detected in metric '{key}'.")
                val = 0.0 if math.isnan(val) else (9999.0 if val > 0 else -1.0)
                if key == 'ts': ts = val
                elif key == 'frametime': ft = max(0.1, val)
                elif key == 'gpu_temp': temp = val
                elif key == 'vram': vram = val

        # Edge case: Non-monotonic timestamps or frame time anomalies
        if self._last_timestamp >= 0 and ts <= self._last_timestamp:
            delta = abs(ts - self._last_timestamp)
            if delta > self._max_jitter_ms and self._strict_mode:
                raise TelemetryValidationError(f"Timestamp regression or extreme jitter detected: {delta}ms")
            ts = self._last_timestamp + 0.001

        ft = max(0.01, min(ft, 10000.0))
        temp = max(-273.15, min(temp, 150.0))
        vram = max(0.0, vram)

        self._last_timestamp = ts
        return FrameMetric(
            timestamp_ms=round(ts, 3),
            frame_time_ms=round(ft, 3),
            gpu_temp_c=round(temp, 1),
            vram_usage_mb=round(vram, 2)
        )

    def safe_fps(self, metric: FrameMetric) -> float:
        """Calculates FPS safely mitigating division by zero or extreme spikes."""
        try:
            fps = 1000.0 / metric.frame_time_ms
            return round(min(fps, 10000.0), 2)
        except ZeroDivisionError:
            return 0.0
